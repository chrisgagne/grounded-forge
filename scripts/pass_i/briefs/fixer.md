Pass I, fix-in-place mode, corpus `${corpus}`, slug `${slug}`.

- Deep reference: `${deep}` (${deep_lines} lines).
- Tape: `${tape}` (${tape_lines} lines). ${tape_desc} Read all of it.
- Original: ${original_line}
- Scope `${scope}`. ${second_leg_line}
${notes}
Page renders are rationed: at most ${render_cap}, with `pdftoppm -r 110 -f N -l N -png {original} $$TMPDIR/p{N}`, and stop rendering for good at the first empty or failed render. Use them for charts, diagrams and places where the tape is damaged. For a `[V]` quotation on a scanned source, check it against a tesseract OCR of its page first (the scanned-source check under Pass E of the protocol).

Run `python3 scripts/check-verbatim.py ${deep}` first. Write the log to `${log}`. **Do not stamp the deep reference and do not edit any "Pass I has not run." line**: the driver stamps once every leg is done. If a light reference or distillations exist, don't edit them, but list in the log every changed claim they might carry. Don't stage or commit anything.
