import { createHash, randomBytes } from 'node:crypto';

export const SESSION_TTL_MS = 7 * 24 * 60 * 60 * 1000;

/** @param {string} token */
const hashToken = (token) => createHash('sha256').update(token).digest('hex');

/**
 * Server-side sessions. The client holds a random token; the database holds only its hash.
 * @param {import('node:sqlite').DatabaseSync} db
 */
export function createSessionStore(db, { now = Date.now, ttlMs = SESSION_TTL_MS } = {}) {
  return {
    ttlMs,

    /** @param {number} userId */
    create(userId) {
      const token = randomBytes(32).toString('base64url');
      const createdAt = now();
      const expiresAt = createdAt + ttlMs;
      db.prepare('INSERT INTO sessions (token_hash, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)').run(
        hashToken(token),
        userId,
        createdAt,
        expiresAt,
      );
      return { token, expiresAt };
    },

    /** @param {string | undefined} token */
    lookup(token) {
      if (!token) return null;
      const row = db.prepare('SELECT user_id, expires_at FROM sessions WHERE token_hash = ?').get(hashToken(token));
      if (!row) return null;
      if (Number(row.expires_at) <= now()) {
        db.prepare('DELETE FROM sessions WHERE token_hash = ?').run(hashToken(token));
        return null;
      }
      return { userId: Number(row.user_id), expiresAt: Number(row.expires_at) };
    },

    /** @param {string} token */
    destroy(token) {
      db.prepare('DELETE FROM sessions WHERE token_hash = ?').run(hashToken(token));
    },
  };
}

/** @typedef {ReturnType<typeof createSessionStore>} SessionStore */
