# Flag code that evaluates strings built at run time

The factory's pinned semgrep rules (`factory/rules/semgrep/`) catch SQL built from strings, but nothing catches code that evaluates a string assembled at run time: JavaScript's `eval(x)` and `new Function(x)`, or Python's `eval(x)` and `exec(x)`. The OWASP Top 10 for Agentic Applications (ASI05) names this as a way generated code runs something nobody reviewed.

As the person who signs off a change, I want the gate and the factory check to flag a call to `eval`, `new Function`, or Python's `exec`, whose argument isn't a fixed string literal, so a change that adds one stops before it runs. A call with a plain string literal isn't flagged.
