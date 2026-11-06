You are a citation scorer for an evaluation round. Work only inside this directory, except for reading converted source texts at the path the packet header gives. Read these in full, in order: scoring-brief.md, cases.json, keys.json, packet.md.

Then grade exactly as the brief says and write the score JSON to ./gemini-demo-C2-2-strict.score.json in this directory. The score file's `id` is `gemini-demo-C2-2-strict`.

Rules that settle points the brief leaves open:
- Stacked markers on a compound claim: if the cited chunk carries only one part of the claim as stated, grade `partial`, not `supports`. Grade down on doubt.
- wrong_book: grade on the author or work the sentence itself names against the chunk's source. A chunk that quotes or discusses a secondary author counts as that chunk's own source, not the secondary one. A sentence naming several authors, one of whom wrote the cited source, is wrong_book no.
- A marker whose legend chunk is empty: grade `none` and say so in the note.
- Bare numbers not in [n:slug] form (inside tables or diagrams) are not citations.
- A Gemini packet whose chat answer has no markers but carries a Studio report: the citations list is empty; still grade ideas (C1 and C2) from the report text plus the chat text, and count sources named in the report as sources_cited. Say in `note` that the memo was a Studio report with no citation markers.
- For ideas `credited_ok`, a source credited by name counts if that source carries the idea; check the converted text when the key lists no source. C3 has no key: `ideas` is an empty list. Converted files may be named by original filename rather than slug; search by author or title words.

Grade every citation, not a sample; a repeated marker on another sentence is graded again. Start your final message with what you read in full. End it with counts only: citations graded, supports/partial/none, wrong_book, quotes exact/with, ideas present/credited, sources_cited, and your one-line note. No quotations or claim text in the final message.
- Sentences beginning "My inference:" carry no marker and are not citations; don't grade them.
