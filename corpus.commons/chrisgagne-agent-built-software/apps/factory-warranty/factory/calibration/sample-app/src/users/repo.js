/**
 * @typedef {{ id: number, email: string, name: string, dateOfBirth: string | null, createdAt: number }} User
 */

/** @returns {User} */
function toUser(row) {
  return {
    id: Number(row.id),
    email: String(row.email),
    name: String(row.name),
    dateOfBirth: row.date_of_birth === null ? null : String(row.date_of_birth),
    createdAt: Number(row.created_at),
  };
}

/** The shape of a user returned by the API. Never includes the password hash. */
/** @param {User} user */
export function toProfile(user) {
  return {
    id: user.id,
    email: user.email,
    name: user.name,
    dateOfBirth: user.dateOfBirth,
    createdAt: new Date(user.createdAt).toISOString(),
  };
}

export function createUser(db, { email, passwordHash, name, dateOfBirth, createdAt }) {
  const result = db
    .prepare('INSERT INTO users (email, password_hash, name, date_of_birth, created_at) VALUES (?, ?, ?, ?, ?)')
    .run(email, passwordHash, name, dateOfBirth, createdAt);
  return findUserById(db, Number(result.lastInsertRowid));
}

/** @returns {User | null} */
export function findUserById(db, id) {
  const row = db.prepare('SELECT id, email, name, date_of_birth, created_at FROM users WHERE id = ?').get(id);
  return row ? toUser(row) : null;
}

/** @returns {User | null} */
export function findUserByEmail(db, email) {
  const row = db.prepare('SELECT id, email, name, date_of_birth, created_at FROM users WHERE email = ?').get(email);
  return row ? toUser(row) : null;
}

/** @returns {{ id: number, passwordHash: string } | null} */
export function findCredentials(db, email) {
  const row = db.prepare('SELECT id, password_hash FROM users WHERE email = ?').get(email);
  return row ? { id: Number(row.id), passwordHash: String(row.password_hash) } : null;
}

/** @param {number} id @param {{ name?: string, dateOfBirth?: string | null }} changes */
export function updateProfile(db, id, changes) {
  const current = findUserById(db, id);
  if (!current) return null;
  const next = { ...current, ...changes };
  db.prepare('UPDATE users SET name = ?, date_of_birth = ? WHERE id = ?').run(next.name, next.dateOfBirth, id);
  return findUserById(db, id);
}
