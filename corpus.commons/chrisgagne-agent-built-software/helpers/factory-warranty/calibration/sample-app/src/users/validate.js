import { HttpError } from '../http.js';

const EMAIL = /^[^\s@]+@[^\s@.]+(\.[^\s@.]+)+$/;
const ISO_DATE = /^(\d{4})-(\d{2})-(\d{2})$/;

export const MIN_PASSWORD_LENGTH = 10;
export const MAX_PASSWORD_LENGTH = 200;

export function validateEmail(value) {
  const email = typeof value === 'string' ? value.trim() : '';
  if (email.length > 254 || !EMAIL.test(email)) throw new HttpError(400, 'A valid email address is required');
  return email;
}

export function validatePassword(value) {
  if (typeof value !== 'string' || value.length < MIN_PASSWORD_LENGTH || value.length > MAX_PASSWORD_LENGTH) {
    throw new HttpError(400, `Password must be ${MIN_PASSWORD_LENGTH} to ${MAX_PASSWORD_LENGTH} characters`);
  }
  return value;
}

export function validateName(value) {
  const name = typeof value === 'string' ? value.trim() : '';
  if (name.length === 0 || name.length > 100) throw new HttpError(400, 'Name must be 1 to 100 characters');
  return name;
}

/**
 * Dates of birth are optional, ISO `YYYY-MM-DD`, real calendar dates, and not in the future.
 * @param {unknown} value
 * @param {number} now
 * @returns {string | null}
 */
export function validateDateOfBirth(value, now) {
  if (value === undefined || value === null || value === '') return null;
  const match = typeof value === 'string' ? ISO_DATE.exec(value) : null;
  if (!match) throw new HttpError(400, 'dateOfBirth must be a date in YYYY-MM-DD format');
  const [, year, month, day] = match.map(Number);
  const date = new Date(Date.UTC(year, month - 1, day));
  const isRealDate = date.getUTCFullYear() === year && date.getUTCMonth() === month - 1 && date.getUTCDate() === day;
  if (!isRealDate || year < 1900 || date.getTime() > now) {
    throw new HttpError(400, 'dateOfBirth must be a real date in the past');
  }
  return String(value);
}
