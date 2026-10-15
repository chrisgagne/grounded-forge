import assert from 'node:assert/strict';
import { mkdtempSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { test } from 'node:test';
import { openDatabase } from '../src/db/index.js';
import { appliedVersions, listMigrations, migrateDown, migrateUp } from '../src/db/migrate.js';

const tables = (db) =>
  db
    .prepare("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
    .all()
    .map((row) => row.name);

function scratchMigrations(t, files) {
  const dir = mkdtempSync(join(tmpdir(), 'migrations-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  for (const [name, sql] of Object.entries(files)) writeFileSync(join(dir, name), sql);
  return dir;
}

test('applies every migration to an empty database', () => {
  const db = openDatabase();
  const applied = migrateUp(db);
  assert.equal(applied.length, listMigrations().length);
  assert.deepEqual(
    appliedVersions(db),
    listMigrations().map((m) => m.version),
  );
  for (const table of ['users', 'sessions', 'notes', 'note_tags']) assert.ok(tables(db).includes(table), table);
});

test('running the migrations again applies nothing', () => {
  const db = openDatabase();
  migrateUp(db);
  assert.deepEqual(migrateUp(db), []);
});

test('rolls back the most recent migration', (t) => {
  const dir = scratchMigrations(t, {
    '0001_widgets.up.sql': 'CREATE TABLE widgets (id INTEGER PRIMARY KEY);',
    '0001_widgets.down.sql': 'DROP TABLE widgets;',
    '0002_gadgets.up.sql': 'CREATE TABLE gadgets (id INTEGER PRIMARY KEY);',
    '0002_gadgets.down.sql': 'DROP TABLE gadgets;',
  });
  const db = openDatabase();
  migrateUp(db, { dir });
  assert.deepEqual(migrateDown(db, { dir }), ['0002_gadgets']);
  assert.ok(tables(db).includes('widgets'));
  assert.ok(!tables(db).includes('gadgets'));
  assert.deepEqual(appliedVersions(db), ['0001']);
});

test('refuses to roll back a migration that has no down file', (t) => {
  const dir = scratchMigrations(t, { '0001_widgets.up.sql': 'CREATE TABLE widgets (id INTEGER PRIMARY KEY);' });
  const db = openDatabase();
  migrateUp(db, { dir });
  assert.throws(() => migrateDown(db, { dir }), /no down migration/);
  assert.deepEqual(appliedVersions(db), ['0001']);
});

test('a failing migration leaves no trace', (t) => {
  const dir = scratchMigrations(t, {
    '0001_broken.up.sql': 'CREATE TABLE half (id INTEGER PRIMARY KEY); THIS IS NOT SQL;',
  });
  const db = openDatabase();
  assert.throws(() => migrateUp(db, { dir }));
  assert.ok(!tables(db).includes('half'));
  assert.deepEqual(appliedVersions(db), []);
});
