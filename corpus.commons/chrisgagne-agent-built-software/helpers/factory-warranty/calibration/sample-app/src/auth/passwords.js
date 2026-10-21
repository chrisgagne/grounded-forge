import { randomBytes, scrypt, timingSafeEqual } from 'node:crypto';

const KEY_LENGTH = 64;
const PARAMS = { N: 16384, r: 8, p: 1 };

/**
 * @param {string} password
 * @param {Buffer} salt
 * @param {{ N: number, r: number, p: number }} params
 * @param {number} keyLength
 * @returns {Promise<Buffer>}
 */
function deriveKey(password, salt, params, keyLength) {
  return new Promise((resolve, reject) => {
    scrypt(password, salt, keyLength, params, (err, key) => (err ? reject(err) : resolve(key)));
  });
}

/** @param {string} password */
export async function hashPassword(password) {
  const salt = randomBytes(16);
  const key = await deriveKey(password, salt, PARAMS, KEY_LENGTH);
  return ['scrypt', PARAMS.N, PARAMS.r, PARAMS.p, salt.toString('base64'), key.toString('base64')].join('$');
}

/** @param {string} password @param {string} stored */
export async function verifyPassword(password, stored) {
  const parts = String(stored).split('$');
  if (parts.length !== 6 || parts[0] !== 'scrypt') return false;
  const [, N, r, p, salt, key] = parts;
  const expected = Buffer.from(key, 'base64');
  if (expected.length === 0) return false;
  const actual = await deriveKey(
    password,
    Buffer.from(salt, 'base64'),
    { N: Number(N), r: Number(r), p: Number(p) },
    expected.length,
  );
  return timingSafeEqual(actual, expected);
}
