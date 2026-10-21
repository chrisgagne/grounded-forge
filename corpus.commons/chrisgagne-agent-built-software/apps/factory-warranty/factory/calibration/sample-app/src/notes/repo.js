import { transaction } from '../db/index.js';

/**
 * @typedef {{ id: number, title: string, body: string, tags: string[], createdAt: number, updatedAt: number }} Note
 */

/** @returns {Note} */
function toNote(row) {
  return {
    id: Number(row.id),
    title: String(row.title),
    body: String(row.body),
    tags: JSON.parse(String(row.tags)),
    createdAt: Number(row.created_at),
    updatedAt: Number(row.updated_at),
  };
}

/**
 * A page of the user's notes, newest first, optionally only those with `tag`.
 * @returns {Note[]}
 */
export function listNotes(db, userId, { limit = 20, offset = 0, tag = null } = {}) {
  return db
    .prepare(
      `SELECT n.id, n.title, n.body, n.created_at, n.updated_at,
         (SELECT json_group_array(tag) FROM (SELECT tag FROM note_tags WHERE note_id = n.id ORDER BY tag)) AS tags
       FROM notes n
       WHERE n.user_id = ?
         AND (? IS NULL OR EXISTS (SELECT 1 FROM note_tags t WHERE t.note_id = n.id AND t.tag = ?))
       ORDER BY n.created_at DESC, n.id DESC
       LIMIT ? OFFSET ?`,
    )
    .all(userId, tag, tag, limit, offset)
    .map(toNote);
}

/** @returns {Note | null} */
export function getNote(db, userId, noteId) {
  const row = db
    .prepare(
      `SELECT n.id, n.title, n.body, n.created_at, n.updated_at,
         (SELECT json_group_array(tag) FROM (SELECT tag FROM note_tags WHERE note_id = n.id ORDER BY tag)) AS tags
       FROM notes n
       WHERE n.id = ? AND n.user_id = ?`,
    )
    .get(noteId, userId);
  return row ? toNote(row) : null;
}

/**
 * @param {any} db
 * @param {number} userId
 * @param {{ title: string, body: string, tags: string[], now: number }} input
 */
export function createNote(db, userId, { title, body, tags, now }) {
  return transaction(db, () => {
    const result = db
      .prepare('INSERT INTO notes (user_id, title, body, created_at, updated_at) VALUES (?, ?, ?, ?, ?)')
      .run(userId, title, body, now, now);
    const noteId = Number(result.lastInsertRowid);
    const insertTag = db.prepare('INSERT INTO note_tags (note_id, tag) VALUES (?, ?)');
    for (const tag of tags) insertTag.run(noteId, tag);
    return getNote(db, userId, noteId);
  });
}
