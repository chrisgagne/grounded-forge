const LEVELS = { debug: 10, info: 20, warn: 30, error: 40, silent: 100 };

/**
 * @typedef {(msg: string, fields?: Record<string, unknown>) => void} LogFn
 * @typedef {{ debug: LogFn, info: LogFn, warn: LogFn, error: LogFn }} Logger
 */

/** @returns {Logger} */
export function createLogger({ level = process.env.LOG_LEVEL ?? 'info', stream = process.stderr } = {}) {
  const threshold = LEVELS[level] ?? LEVELS.info;
  /** @param {keyof typeof LEVELS} lvl @param {string} msg @param {Record<string, unknown>} fields */
  const write = (lvl, msg, fields) => {
    if (LEVELS[lvl] < threshold) return;
    stream.write(`${JSON.stringify({ time: new Date().toISOString(), level: lvl, msg, ...fields })}\n`);
  };
  return {
    debug: (msg, fields = {}) => write('debug', msg, fields),
    info: (msg, fields = {}) => write('info', msg, fields),
    warn: (msg, fields = {}) => write('warn', msg, fields),
    error: (msg, fields = {}) => write('error', msg, fields),
  };
}

export const log = createLogger();
