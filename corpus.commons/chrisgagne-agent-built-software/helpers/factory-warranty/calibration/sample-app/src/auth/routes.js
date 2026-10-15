import { randomBytes } from 'node:crypto';
import { sendJson, sendNoContent } from '../http.js';
import { createUser, findCredentials, findUserByEmail, findUserById, toProfile } from '../users/repo.js';
import { validateDateOfBirth, validateEmail, validateName, validatePassword } from '../users/validate.js';
import { SESSION_COOKIE } from './middleware.js';
import { hashPassword, verifyPassword } from './passwords.js';

const DUMMY_HASH = await hashPassword(randomBytes(16).toString('hex'));

/** @param {string} token @param {number} maxAgeMs */
function sessionCookie(token, maxAgeMs) {
  const maxAge = Math.floor(maxAgeMs / 1000);
  return `${SESSION_COOKIE}=${token}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${maxAge}`;
}

/**
 * @param {import('../router.js').Router} router
 * @param {{ db: any, sessions: import('./sessions.js').SessionStore, auth: import('../router.js').Handler, now: () => number }} deps
 */
export function authRoutes(router, { db, sessions, auth, now }) {
  router.post('/signup', async (req, res) => {
    const email = validateEmail(req.body.email);
    const password = validatePassword(req.body.password);
    const name = validateName(req.body.name);
    const dateOfBirth = validateDateOfBirth(req.body.dateOfBirth, now());
    if (findUserByEmail(db, email)) {
      return sendJson(res, 409, { error: 'An account with that email already exists' });
    }
    const passwordHash = await hashPassword(password);
    const user = createUser(db, { email, passwordHash, name, dateOfBirth, createdAt: now() });
    sendJson(res, 201, { user: toProfile(user) });
  });

  router.post('/login', async (req, res) => {
    const email = typeof req.body.email === 'string' ? req.body.email.trim() : '';
    const password = typeof req.body.password === 'string' ? req.body.password : '';
    const account = findCredentials(db, email);
    const valid = await verifyPassword(password, account ? account.passwordHash : DUMMY_HASH);
    if (!account || !valid) {
      return sendJson(res, 401, { error: 'Invalid email or password' });
    }
    const session = sessions.create(account.id);
    sendJson(
      res,
      200,
      { user: toProfile(findUserById(db, account.id)) },
      { 'set-cookie': sessionCookie(session.token, sessions.ttlMs) },
    );
  });

  router.post('/logout', auth, (req, res) => {
    sessions.destroy(req.sessionToken);
    sendNoContent(res, { 'set-cookie': sessionCookie('', 0) });
  });
}
