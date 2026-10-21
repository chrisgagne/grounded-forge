// Latency budget for the notes list. Seeds one large account, then times GET /notes over HTTP.
// Exits 1 when any scenario's median is over budget.
import { once } from 'node:events';
import { createServer } from 'node:http';
import { performance } from 'node:perf_hooks';
import { createApp } from '../src/app.js';
import { openDatabase, transaction } from '../src/db/index.js';
import { migrateUp } from '../src/db/migrate.js';
import { createLogger } from '../src/log.js';

const NOTES = 50_000;
const OTHER_USER_NOTES = 10_000;
const TAGS = Array.from({ length: 40 }, (_, i) => `tag-${i}`);
const TAGS_PER_NOTE = 3;
const WARMUP = 2;
const SAMPLES = 9;
const BUDGET_MS = 50;

const SCENARIOS = [
  { name: 'first page', path: '/notes?limit=50' },
  { name: 'tag filter', path: '/notes?limit=50&tag=tag-7' },
  { name: 'deep page', path: '/notes?limit=50&offset=40000' },
];

let seed = 42;
const random = () => {
  seed = (seed * 1_103_515_245 + 12_345) % 2 ** 31;
  return seed / 2 ** 31;
};

function seedNotes(db, userId, count) {
  const insertNote = db.prepare(
    'INSERT INTO notes (user_id, title, body, created_at, updated_at) VALUES (?, ?, ?, ?, ?)',
  );
  const insertTag = db.prepare('INSERT OR IGNORE INTO note_tags (note_id, tag) VALUES (?, ?)');
  const start = Date.parse('2024-01-01T00:00:00Z');
  transaction(db, () => {
    for (let i = 0; i < count; i += 1) {
      const createdAt = start + Math.floor(random() * 2 * 365 * 24 * 3600 * 1000);
      const body = `Meeting notes ${i}: decisions, follow-ups and open questions. `.repeat(4);
      const { lastInsertRowid } = insertNote.run(userId, `Note ${i}`, body, createdAt, createdAt);
      for (let t = 0; t < TAGS_PER_NOTE; t += 1) insertTag.run(lastInsertRowid, TAGS[Math.floor(random() * TAGS.length)]);
    }
  });
}

const median = (values) => {
  const sorted = [...values].sort((a, b) => a - b);
  return sorted[Math.floor(sorted.length / 2)];
};

async function main() {
  const db = openDatabase(':memory:');
  migrateUp(db);
  /** @type {import('../src/llm/client.js').LlmClient} */
  const llm = { complete: async () => ({ content: [], stopReason: 'end_turn' }) };
  /** @type {import('../src/mail/mailer.js').Mailer} */
  const mailer = { send: async () => ({ id: null }) };
  const server = createServer(createApp({ db, llm, mailer, log: createLogger({ level: 'silent' }) }));
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  const { port } = /** @type {import('node:net').AddressInfo} */ (server.address());
  const baseUrl = `http://127.0.0.1:${port}`;

  const post = (path, body) =>
    fetch(baseUrl + path, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) });
  const user = { email: 'perf@example.com', password: 'perf-password-1', name: 'Perf User', dateOfBirth: '1980-01-01' };
  const other = { email: 'other@example.com', password: 'perf-password-2', name: 'Other User' };
  for (const account of [user, other]) {
    const res = await post('/signup', account);
    if (res.status !== 201) throw new Error(`signup failed with ${res.status}`);
  }
  const login = await post('/login', { email: user.email, password: user.password });
  const cookie = (login.headers.get('set-cookie') ?? '').split(';')[0];

  const idOf = (email) => Number(db.prepare('SELECT id FROM users WHERE email = ?').get(email).id);
  const seedStart = performance.now();
  seedNotes(db, idOf(user.email), NOTES);
  seedNotes(db, idOf(other.email), OTHER_USER_NOTES);
  console.log(`seeded ${NOTES + OTHER_USER_NOTES} notes in ${Math.round(performance.now() - seedStart)} ms`);
  console.log(`budget: median ${BUDGET_MS} ms per request, ${SAMPLES} samples after ${WARMUP} warm-up requests`);

  const results = [];
  for (const scenario of SCENARIOS) {
    const timings = [];
    for (let i = 0; i < WARMUP + SAMPLES; i += 1) {
      const started = performance.now();
      const res = await fetch(baseUrl + scenario.path, { headers: { cookie } });
      await res.arrayBuffer();
      if (res.status !== 200) throw new Error(`${scenario.path} answered ${res.status}`);
      if (i >= WARMUP) timings.push(performance.now() - started);
    }
    const ms = median(timings);
    results.push({ scenario: scenario.name, path: scenario.path, median_ms: Number(ms.toFixed(2)), budget_ms: BUDGET_MS, ok: ms <= BUDGET_MS });
  }

  server.closeAllConnections();
  server.close();

  for (const r of results) {
    console.log(`${r.ok ? 'ok  ' : 'FAIL'} ${r.scenario.padEnd(12)} median ${String(r.median_ms).padStart(8)} ms  ${r.path}`);
  }
  console.log(JSON.stringify({ budget_ms: BUDGET_MS, results }));
  if (results.some((r) => !r.ok)) {
    console.error(`perf: over budget (${BUDGET_MS} ms median)`);
    process.exitCode = 1;
  }
}

await main();
