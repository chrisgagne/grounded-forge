const DAY_MS = 24 * 60 * 60 * 1000;

/** @param {NodeJS.ProcessEnv} [env] */
export function loadConfig(env = process.env) {
  return {
    port: Number(env.PORT ?? 3000),
    databasePath: env.DATABASE_PATH ?? 'data/notes.db',
    sessionTtlMs: Number(env.SESSION_TTL_DAYS ?? 7) * DAY_MS,
    llm: {
      baseUrl: env.LLM_BASE_URL ?? 'https://api.anthropic.com',
      model: env.LLM_MODEL ?? 'claude-haiku-4-5',
      apiKey: env.LLM_API_KEY ?? '',
    },
    mail: {
      apiUrl: env.MAIL_API_URL ?? 'http://localhost:8025/api/v1/send',
      apiKey: env.MAIL_API_KEY ?? '',
      from: env.MAIL_FROM ?? 'Notes <notes@example.com>',
    },
  };
}
