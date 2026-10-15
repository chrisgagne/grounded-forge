import { parseCookies, sendJson } from '../http.js';
import { findUserById } from '../users/repo.js';

export const SESSION_COOKIE = 'sid';

/**
 * Route guard: resolves the session cookie to a user, or answers 401.
 * @param {{ db: any, sessions: import('./sessions.js').SessionStore }} deps
 * @returns {import('../router.js').Handler}
 */
export function requireSession({ db, sessions }) {
  return (req, res) => {
    const token = parseCookies(req.headers.cookie)[SESSION_COOKIE];
    const session = sessions.lookup(token);
    const user = session ? findUserById(db, session.userId) : null;
    if (!user) {
      sendJson(res, 401, { error: 'Sign in required' });
      return;
    }
    req.user = user;
    req.sessionToken = token;
  };
}
