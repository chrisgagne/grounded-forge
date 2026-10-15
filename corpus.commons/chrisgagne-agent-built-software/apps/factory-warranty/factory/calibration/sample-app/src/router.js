import { HttpError, readJson, sendJson } from './http.js';

/**
 * @typedef {import('node:http').IncomingMessage & {
 *   params: Record<string, string>,
 *   query: Record<string, string>,
 *   body: any,
 *   user?: import('./users/repo.js').User,
 *   sessionToken?: string,
 * }} Request
 * @typedef {import('node:http').ServerResponse} Response
 * @typedef {(req: Request, res: Response) => unknown} Handler
 */

const METHODS_WITH_BODY = new Set(['POST', 'PUT', 'PATCH']);

/** @param {string} value */
function decode(value) {
  try {
    return decodeURIComponent(value);
  } catch {
    throw new HttpError(400, 'Malformed URL');
  }
}

export class Router {
  /** @type {{ method: string, segments: string[], handlers: Handler[] }[]} */
  #routes = [];

  /** @param {string} method @param {string} path @param {...Handler} handlers */
  add(method, path, ...handlers) {
    this.#routes.push({ method, segments: path.split('/'), handlers });
    return this;
  }

  /** @param {string} path @param {...Handler} handlers */
  get(path, ...handlers) {
    return this.add('GET', path, ...handlers);
  }

  /** @param {string} path @param {...Handler} handlers */
  post(path, ...handlers) {
    return this.add('POST', path, ...handlers);
  }

  /** @param {string} path @param {...Handler} handlers */
  patch(path, ...handlers) {
    return this.add('PATCH', path, ...handlers);
  }

  /** @param {string} path @param {...Handler} handlers */
  delete(path, ...handlers) {
    return this.add('DELETE', path, ...handlers);
  }

  /** @param {import('node:http').IncomingMessage} incoming @param {Response} res */
  async handle(incoming, res) {
    const req = /** @type {Request} */ (incoming);
    const url = new URL(req.url ?? '/', 'http://localhost');
    const segments = url.pathname.split('/');
    let pathMatched = false;
    for (const route of this.#routes) {
      const params = matchSegments(route.segments, segments);
      if (!params) continue;
      pathMatched = true;
      if (route.method !== req.method) continue;
      req.params = params;
      req.query = Object.fromEntries(url.searchParams);
      req.body = METHODS_WITH_BODY.has(req.method) ? await readJson(req) : {};
      for (const handler of route.handlers) {
        await handler(req, res);
        if (res.writableEnded) return;
      }
      return;
    }
    if (pathMatched) sendJson(res, 405, { error: 'Method not allowed' });
    else sendJson(res, 404, { error: 'Not found' });
  }
}

/**
 * Matches a request path against a route pattern such as `/notes/:id`.
 * @param {string[]} pattern
 * @param {string[]} path
 * @returns {Record<string, string> | null}
 */
function matchSegments(pattern, path) {
  if (pattern.length !== path.length) return null;
  /** @type {Record<string, string>} */
  const params = {};
  for (let i = 0; i < pattern.length; i += 1) {
    if (pattern[i].startsWith(':')) {
      if (!path[i]) return null;
      params[pattern[i].slice(1)] = decode(path[i]);
    } else if (pattern[i] !== path[i]) {
      return null;
    }
  }
  return params;
}
