/**
 * A judge session backed by the Claude Code CLI instead of the pi SDK.
 *
 * The SDK talks to the Anthropic API and needs an API key. This adapter drives
 * `claude -p` instead, so the judge runs on whatever authentication the CLI
 * already holds. It exposes the small part of the SDK session surface the
 * matcher and the classifier use: `prompt`, `messages`, `subscribe`, `abort`,
 * `dispose` and `sessionFile`.
 *
 * Turned on with REVIEW_BENCH_CLAUDE_CLI=1. The API path stays the default.
 *
 * Differences from the SDK session, which matter when comparing scores:
 * - the CLI appends the judge's system prompt to Claude Code's own, which the
 *   SDK session does not carry;
 * - effort stands in for the SDK's thinking level;
 * - the classifier's `read`/`grep`/`find`/`ls` tools become Read, Grep and Glob.
 */

import { spawn } from "child_process";
import { mkdtempSync, writeFileSync, rmSync, appendFileSync } from "fs";
import { tmpdir } from "os";
import { join } from "path";
import { randomUUID } from "crypto";

/** True when the judge should run on the CLI rather than the API. */
export function claudeCliJudge(): boolean {
  return process.env.REVIEW_BENCH_CLAUDE_CLI === "1";
}

export interface ClaudeCliSessionOptions {
  /** Working directory the session runs in (the repo checkout, for the classifier). */
  cwd: string;
  /** The judge's system prompt, appended to Claude Code's own. */
  systemPrompt: string;
  /** Model name passed to --model. */
  model: string;
  /** Effort level, standing in for the SDK's thinking level. */
  effort: "low" | "medium" | "high" | "xhigh";
  /** Built-in tools to allow. An empty list disables every tool. */
  tools: string[];
  /** Names the session in log lines. */
  label?: string;
}

interface CliUsage {
  input_tokens?: number;
  output_tokens?: number;
  cache_read_input_tokens?: number;
  cache_creation_input_tokens?: number;
}

type Listener = (event: any) => void;

const CLI = process.env.REVIEW_BENCH_CLAUDE_BIN ?? "claude";

/**
 * ReviewBench records the candidate's cost but not the judge's, so each turn's
 * cost is appended here when REVIEW_BENCH_CLI_COST_LOG names a file.
 */
function logTurn(row: Record<string, unknown>): void {
  const path = process.env.REVIEW_BENCH_CLI_COST_LOG;
  if (!path) return;
  try {
    appendFileSync(path, JSON.stringify(row) + "\n");
  } catch {
    // a missing cost line must not fail a judge call
  }
}

class ClaudeCliSession {
  readonly messages: any[] = [];
  readonly sessionFile: string;
  private readonly listeners: Listener[] = [];
  private readonly sessionId = randomUUID();
  private readonly workDir: string;
  private readonly promptFile: string;
  private readonly systemPromptFile: string;
  private started = false;
  /** `total_cost_usd` is cumulative over a resumed session, so turns report the delta. */
  private costSoFar = 0;
  private aborted = false;
  private child: ReturnType<typeof spawn> | null = null;

  constructor(private readonly opts: ClaudeCliSessionOptions) {
    this.workDir = mkdtempSync(join(tmpdir(), "rb-judge-cli-"));
    this.systemPromptFile = join(this.workDir, "system-prompt.txt");
    this.promptFile = join(this.workDir, "prompt.txt");
    writeFileSync(this.systemPromptFile, opts.systemPrompt);
    this.sessionFile = `claude session ${this.sessionId} (${opts.label ?? opts.model})`;
  }

  subscribe(listener: Listener): () => void {
    this.listeners.push(listener);
    return () => {
      const i = this.listeners.indexOf(listener);
      if (i >= 0) this.listeners.splice(i, 1);
    };
  }

  private emit(event: any): void {
    for (const l of this.listeners) {
      try {
        l(event);
      } catch {
        // a listener's failure is not the session's
      }
    }
  }

  private args(): string[] {
    const a = [
      "-p",
      "--output-format", "stream-json",
      "--verbose",
      "--model", this.opts.model,
      "--effort", this.opts.effort,
      "--safe-mode",
      "--setting-sources", "",
      "--strict-mcp-config",
      "--permission-mode", "dontAsk",
      "--permission-prompts", "none",
      "--tools", this.opts.tools.join(","),
      "--append-system-prompt-file", this.systemPromptFile,
    ];
    a.push(this.started ? "--resume" : "--session-id", this.sessionId);
    return a;
  }

  async prompt(message: string): Promise<void> {
    if (this.aborted) throw new Error("session aborted");
    writeFileSync(this.promptFile, message);
    this.messages.push({ role: "user", content: [{ type: "text", text: message }] });

    const { text, errorMessage } = await this.run(message);
    this.started = true;

    const assistant: any = { role: "assistant", content: [{ type: "text", text }] };
    if (errorMessage) assistant.errorMessage = errorMessage;
    this.messages.push(assistant);
    if (errorMessage) throw new Error(`Model error: ${errorMessage}`);
  }

  private run(message: string): Promise<{ text: string; errorMessage?: string }> {
    return new Promise((resolve, reject) => {
      const child = spawn(CLI, this.args(), {
        cwd: this.opts.cwd,
        stdio: ["pipe", "pipe", "pipe"],
        env: { ...process.env, CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: "1" },
      });
      this.child = child;

      let out = "";
      let err = "";
      let text = "";
      let errorMessage: string | undefined;
      let sawResult = false;

      const handleLine = (line: string) => {
        if (!line.trim()) return;
        let msg: any;
        try {
          msg = JSON.parse(line);
        } catch {
          return;
        }
        if (msg.type === "assistant" && Array.isArray(msg.message?.content)) {
          for (const block of msg.message.content) {
            if (block?.type === "tool_use") {
              this.emit({ type: "tool_execution_start", toolName: String(block.name ?? "unknown") });
            }
          }
          return;
        }
        if (msg.type === "result") {
          sawResult = true;
          if (typeof msg.result === "string") text = msg.result;
          if (msg.is_error || (msg.subtype && msg.subtype !== "success")) {
            errorMessage = String(msg.subtype ?? "error") + (typeof msg.result === "string" ? `: ${msg.result}` : "");
          }
          const u: CliUsage = msg.usage ?? {};
          const cumulative = Number(msg.total_cost_usd ?? 0);
          const turnCost = Math.max(0, cumulative - this.costSoFar);
          if (cumulative > this.costSoFar) this.costSoFar = cumulative;
          logTurn({
            at: new Date().toISOString(),
            label: this.opts.label ?? null,
            session: this.sessionId,
            turn: this.messages.filter((m) => m.role === "user").length,
            cost_usd: turnCost,
            input: u.input_tokens ?? 0,
            output: u.output_tokens ?? 0,
            cache_read: u.cache_read_input_tokens ?? 0,
            cache_write: u.cache_creation_input_tokens ?? 0,
          });
          this.emit({
            type: "turn_end",
            message: {
              usage: {
                input: u.input_tokens ?? 0,
                output: u.output_tokens ?? 0,
                cacheRead: u.cache_read_input_tokens ?? 0,
                cacheWrite: u.cache_creation_input_tokens ?? 0,
                cost: { total: turnCost },
              },
            },
          });
        }
      };

      child.stdout.setEncoding("utf8");
      child.stdout.on("data", (chunk: string) => {
        out += chunk;
        let nl: number;
        while ((nl = out.indexOf("\n")) >= 0) {
          const line = out.slice(0, nl);
          out = out.slice(nl + 1);
          handleLine(line);
        }
      });
      child.stderr.setEncoding("utf8");
      child.stderr.on("data", (chunk: string) => {
        err += chunk;
        if (err.length > 20000) err = err.slice(-20000);
      });

      child.on("error", reject);
      child.on("close", (code) => {
        this.child = null;
        if (out.trim()) handleLine(out);
        out = "";
        if (this.aborted) {
          reject(new Error("session aborted"));
          return;
        }
        if (code !== 0 || !sawResult) {
          reject(new Error(`claude -p exited ${code}${err ? `: ${err.trim().slice(-2000)}` : ""}`));
          return;
        }
        resolve({ text, errorMessage });
      });

      child.stdin.on("error", () => {
        // the CLI can close stdin early; the exit code is what matters
      });
      child.stdin.end(message);
    });
  }

  async abort(): Promise<void> {
    this.aborted = true;
    this.child?.kill("SIGTERM");
  }

  dispose(): void {
    this.child?.kill("SIGTERM");
    try {
      rmSync(this.workDir, { recursive: true, force: true });
    } catch {
      // nothing to do
    }
  }
}

/** Mirrors `createAgentSession`'s shape so call sites can swap one for the other. */
export async function createClaudeCliSession(
  opts: ClaudeCliSessionOptions,
): Promise<{ session: any }> {
  return { session: new ClaudeCliSession(opts) };
}
