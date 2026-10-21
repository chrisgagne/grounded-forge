import { requireSession } from './auth/middleware.js';
import { authRoutes } from './auth/routes.js';
import { createSessionStore } from './auth/sessions.js';
import { HttpError, sendJson } from './http.js';
import { summaryRoutes } from './llm/routes.js';
import { log as defaultLog } from './log.js';
import { noteRoutes } from './notes/routes.js';
import { Router } from './router.js';
import { userRoutes } from './users/routes.js';

/**
 * Builds the request handler. Every dependency with side effects is passed in.
 * @param {{
 *   db: import('node:sqlite').DatabaseSync,
 *   llm: import('./llm/client.js').LlmClient,
 *   mailer: import('./mail/mailer.js').Mailer,
 *   now?: () => number,
 *   log?: import('./log.js').Logger,
 *   sessionTtlMs?: number,
 * }} deps
 */
export function createApp({ db, llm, mailer, now = Date.now, log = defaultLog, sessionTtlMs }) {
  const sessions = createSessionStore(db, { now, ttlMs: sessionTtlMs });
  const auth = requireSession({ db, sessions });
  const router = new Router();

  authRoutes(router, { db, sessions, auth, now });
  userRoutes(router, { db, auth, now });
  noteRoutes(router, { db, auth, now });
  summaryRoutes(router, { db, auth, llm, mailer, log });

  /** @param {import('node:http').IncomingMessage} req @param {import('node:http').ServerResponse} res */
  return async function app(req, res) {
    try {
      await router.handle(req, res);
    } catch (err) {
      if (err instanceof HttpError) {
        sendJson(res, err.status, { error: err.message });
        return;
      }
      log.error('unhandled error', { method: req.method, path: req.url?.split('?')[0], error: err.message });
      if (!res.headersSent) sendJson(res, 500, { error: 'Internal server error' });
    }
  };
}
