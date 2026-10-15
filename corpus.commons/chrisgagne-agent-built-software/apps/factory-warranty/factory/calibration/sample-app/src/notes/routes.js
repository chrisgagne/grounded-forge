import { HttpError, sendJson } from '../http.js';
import { createNote, getNote, listNotes } from './repo.js';

export const DEFAULT_PAGE_SIZE = 20;
export const MAX_PAGE_SIZE = 100;
const TAG = /^[a-z0-9][a-z0-9-]{0,31}$/;

/** @param {Record<string, any>} body */
export function validateNoteInput(body) {
  const title = typeof body.title === 'string' ? body.title.trim() : '';
  if (title.length === 0 || title.length > 200) throw new HttpError(400, 'title must be 1 to 200 characters');
  const text = body.body ?? '';
  if (typeof text !== 'string' || text.length > 20_000) {
    throw new HttpError(400, 'body must be text of at most 20000 characters');
  }
  const tags = body.tags ?? [];
  if (!Array.isArray(tags) || tags.length > 10 || !tags.every((tag) => typeof tag === 'string' && TAG.test(tag))) {
    throw new HttpError(400, 'tags must be at most 10 lowercase words (a-z, 0-9 and -)');
  }
  return { title, body: text, tags: [...new Set(tags)] };
}

/** @param {Record<string, string>} query */
function parsePaging(query) {
  const limit = query.limit === undefined ? DEFAULT_PAGE_SIZE : Number(query.limit);
  const offset = query.offset === undefined ? 0 : Number(query.offset);
  if (!Number.isInteger(limit) || limit < 1) throw new HttpError(400, 'limit must be a positive integer');
  if (!Number.isInteger(offset) || offset < 0) throw new HttpError(400, 'offset must be a non-negative integer');
  return { limit: Math.min(limit, MAX_PAGE_SIZE), offset };
}

/** @param {import('./repo.js').Note} note */
export function toNoteResponse(note) {
  return {
    id: note.id,
    title: note.title,
    body: note.body,
    tags: note.tags,
    createdAt: new Date(note.createdAt).toISOString(),
    updatedAt: new Date(note.updatedAt).toISOString(),
  };
}

/**
 * @param {import('../router.js').Router} router
 * @param {{ db: any, auth: import('../router.js').Handler, now: () => number }} deps
 */
export function noteRoutes(router, { db, auth, now }) {
  router.get('/notes', auth, (req, res) => {
    const { limit, offset } = parsePaging(req.query);
    const tag = req.query.tag || null;
    const notes = listNotes(db, req.user.id, { limit, offset, tag });
    sendJson(res, 200, { notes: notes.map(toNoteResponse), limit, offset });
  });

  router.post('/notes', auth, (req, res) => {
    const input = validateNoteInput(req.body);
    const note = createNote(db, req.user.id, { ...input, now: now() });
    sendJson(res, 201, { note: toNoteResponse(note) });
  });

  router.get('/notes/:id', auth, (req, res) => {
    const id = Number(req.params.id);
    const note = Number.isInteger(id) ? getNote(db, req.user.id, id) : null;
    if (!note) return sendJson(res, 404, { error: 'Note not found' });
    sendJson(res, 200, { note: toNoteResponse(note) });
  });
}
