"""Per-artefact extraction handlers.

Each handler takes the source text (list of lines) and returns a list of
extraction records. Handlers are pure—no I/O, no global state—so the
dispatcher can run them in any order and merge their outputs.
"""
