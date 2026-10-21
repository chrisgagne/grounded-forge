import { HttpError, sendJson } from '../http.js';
import { toProfile, updateProfile } from './repo.js';
import { validateDateOfBirth, validateName } from './validate.js';

/**
 * @param {import('../router.js').Router} router
 * @param {{ db: any, auth: import('../router.js').Handler, now: () => number }} deps
 */
export function userRoutes(router, { db, auth, now }) {
  router.get('/me', auth, (req, res) => {
    sendJson(res, 200, { user: toProfile(req.user) });
  });

  router.patch('/me', auth, (req, res) => {
    const changes = {};
    if ('name' in req.body) changes.name = validateName(req.body.name);
    if ('dateOfBirth' in req.body) changes.dateOfBirth = validateDateOfBirth(req.body.dateOfBirth, now());
    if ('email' in req.body || 'password' in req.body) {
      throw new HttpError(400, 'Email and password cannot be changed here');
    }
    const user = updateProfile(db, req.user.id, changes);
    sendJson(res, 200, { user: toProfile(user) });
  });
}
