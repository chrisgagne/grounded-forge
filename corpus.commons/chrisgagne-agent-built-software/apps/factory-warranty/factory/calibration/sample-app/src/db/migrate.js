import { existsSync, readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { transaction } from './index.js';

export const MIGRATIONS_DIR = fileURLToPath(new URL('../../migrations/', import.meta.url));

const UP_FILE = /^(\d{4})_([a-z0-9_]+)\.up\.sql$/;

/**
 * @typedef {{ version: string, name: string, up: string, down: string | null }} Migration
 */

/** @param {string} [dir] @returns {Migration[]} */
export function listMigrations(dir = MIGRATIONS_DIR) {
  return readdirSync(dir)
    .map((file) => UP_FILE.exec(file))
    .filter((match) => match !== null)
    .map(([file, version, name]) => {
      const down = join(dir, `${version}_${name}.down.sql`);
      return { version, name, up: join(dir, file), down: existsSync(down) ? down : null };
    })
    .sort((a, b) => a.version.localeCompare(b.version));
}

function ensureMigrationsTable(db) {
  db.exec(`CREATE TABLE IF NOT EXISTS schema_migrations (
    version TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    applied_at TEXT NOT NULL
  )`);
}

/** @returns {string[]} */
export function appliedVersions(db) {
  ensureMigrationsTable(db);
  return db
    .prepare('SELECT version FROM schema_migrations ORDER BY version')
    .all()
    .map((row) => String(row.version));
}

/** Applies every pending migration in version order. Returns the applied migration ids. */
export function migrateUp(db, { dir = MIGRATIONS_DIR } = {}) {
  const applied = new Set(appliedVersions(db));
  const pending = listMigrations(dir).filter((m) => !applied.has(m.version));
  for (const m of pending) {
    transaction(db, () => {
      db.exec(readFileSync(m.up, 'utf8'));
      db.prepare('INSERT INTO schema_migrations (version, name, applied_at) VALUES (?, ?, ?)').run(
        m.version,
        m.name,
        new Date().toISOString(),
      );
    });
  }
  return pending.map((m) => `${m.version}_${m.name}`);
}

/** Reverts the most recent `steps` migrations. Returns the reverted migration ids. */
export function migrateDown(db, { steps = 1, dir = MIGRATIONS_DIR } = {}) {
  const known = new Map(listMigrations(dir).map((m) => [m.version, m]));
  const reverted = [];
  for (const version of appliedVersions(db).reverse().slice(0, steps)) {
    const m = known.get(version);
    if (!m) throw new Error(`Migration ${version} is applied but its files are missing`);
    if (!m.down) throw new Error(`Migration ${version}_${m.name} has no down migration`);
    transaction(db, () => {
      db.exec(readFileSync(m.down, 'utf8'));
      db.prepare('DELETE FROM schema_migrations WHERE version = ?').run(version);
    });
    reverted.push(`${version}_${m.name}`);
  }
  return reverted;
}
