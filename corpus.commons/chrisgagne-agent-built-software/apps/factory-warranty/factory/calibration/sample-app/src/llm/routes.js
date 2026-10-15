import { sendJson } from '../http.js';
import { listNotes } from '../notes/repo.js';
import { summariseNotes } from './summarise.js';
import { sendEmailTool } from './tools.js';

export const SUMMARY_NOTE_LIMIT = 50;

/** @param {('sent' | 'failed')[]} outcomes */
function emailStatus(outcomes) {
  if (outcomes.includes('sent')) return 'sent';
  return outcomes.length ? 'failed' : 'not_sent';
}

/**
 * @param {import('../router.js').Router} router
 * @param {{
 *   db: any,
 *   auth: import('../router.js').Handler,
 *   llm: import('./client.js').LlmClient,
 *   mailer: import('../mail/mailer.js').Mailer,
 *   log: import('../log.js').Logger,
 * }} deps
 */
export function summaryRoutes(router, { db, auth, llm, mailer, log }) {
  router.post('/notes/summary', auth, async (req, res) => {
    const emailToUser = req.body.email === true;
    const tag = typeof req.body.tag === 'string' && req.body.tag ? req.body.tag : null;
    const notes = listNotes(db, req.user.id, { limit: SUMMARY_NOTE_LIMIT, tag });
    if (notes.length === 0) {
      return sendJson(res, 200, { summary: 'There are no notes to summarise yet.', email: null });
    }

    const tools = [sendEmailTool({ mailer, recipient: req.user.email })];
    let result;
    try {
      result = await summariseNotes({ llm, notes, emailToUser, tools, log });
    } catch (err) {
      log.error('summary failed', { userId: req.user.id, error: err.message });
      return sendJson(res, 502, { error: 'The summary service is unavailable. Try again shortly.' });
    }

    sendJson(res, 200, {
      summary: result.summary,
      email: emailToUser ? { to: req.user.email, status: emailStatus(result.emailOutcomes) } : null,
    });
  });
}
