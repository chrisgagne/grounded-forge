CREATE TABLE note_tags (
  note_id INTEGER NOT NULL REFERENCES notes(id) ON DELETE CASCADE,
  tag TEXT NOT NULL,
  PRIMARY KEY (note_id, tag)
) WITHOUT ROWID;

CREATE INDEX note_tags_tag ON note_tags(tag, note_id);
