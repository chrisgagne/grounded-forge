import { createServer } from 'node:http';
import { createApp } from './app.js';
import { loadConfig } from './config.js';
import { openDatabase } from './db/index.js';
import { migrateUp } from './db/migrate.js';
import { createLlmClient } from './llm/client.js';
import { log } from './log.js';
import { createMailer } from './mail/mailer.js';

const config = loadConfig();
const db = openDatabase(config.databasePath);
const applied = migrateUp(db);
if (applied.length) log.info('applied migrations', { applied });

const app = createApp({
  db,
  llm: createLlmClient(config.llm),
  mailer: createMailer(config.mail),
  sessionTtlMs: config.sessionTtlMs,
});

createServer(app).listen(config.port, () => log.info('listening', { port: config.port }));
