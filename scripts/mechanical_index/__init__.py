"""Mechanical index extraction package.

Reads a converted markdown source and its discovery JSON, runs deterministic
handlers per author-curated artefact, emits structured extraction JSON for the
downstream semantic pass.

Entry point: preprocess.run(source_md_path, discovery_json_path, output_path)
"""
