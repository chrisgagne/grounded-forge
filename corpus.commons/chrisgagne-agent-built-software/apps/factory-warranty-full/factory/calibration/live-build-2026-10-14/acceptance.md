## AC-1: Creating a note with a tag that has capital letters (e.g. "Work") succeeds with 201, and the saved note's tags show the lowercase form ("work").
check: test/notes.test.js :: saves a capitalised tag in lowercase

## AC-2: Creating a note with a tag that has leading or trailing spaces (e.g. " work ") succeeds with 201, and the saved note's tags show the trimmed form ("work").
check: test/notes.test.js :: saves a tag with surrounding spaces trimmed

## AC-3: Creating a note with a tag that has both capitals and stray spaces ("Work ") succeeds with 201, and the tag is saved as "work".
check: test/notes.test.js :: saves a capitalised tag with stray spaces as lowercase and trimmed

## AC-4: Reading the note back later, either on its own or in the notes list, shows the normalised tag, not the form that was typed.
check: test/notes.test.js :: a normalised tag is what is returned when the note is read back

## AC-5: A note saved with a tag typed as "Work" appears when the list is filtered by `tag=work`.
check: test/notes.test.js :: a note tagged with a capitalised tag is found by its lowercase tag filter

## AC-6: Tags that become the same after lowercasing and trimming (e.g. "Work", " work", "work") are saved only once, and the note is created with 201.
check: test/notes.test.js :: tags that normalise to the same value are saved once

## AC-7: A tag that is still invalid after lowercasing and trimming (e.g. "Not A Tag" with internal spaces, "work!" with a disallowed character, or a tag longer than 32 characters once trimmed) is refused with 400, and no note is created.
check: test/notes.test.js :: refuses tags that are still invalid after lowercasing and trimming

## AC-8: A tag that is empty or only whitespace (e.g. "   ") is refused with 400, and no note is created.
assumption: A blank tag is refused, not silently dropped, because the story only asks to save corrected tags and says tags that are still invalid are refused as today.
check: test/notes.test.js :: refuses a tag that is blank after trimming

## AC-9: A tag that would start with a hyphen after trimming (e.g. " -work") is refused with 400.
check: test/notes.test.js :: refuses a tag that starts with a hyphen after trimming

## AC-10: Tags that are not strings, or a `tags` value that is not a list, are still refused with 400.
check: test/notes.test.js :: still refuses non-string tags and a non-list tags value

## AC-11: Sending more than 10 tags is still refused with 400, even if some of them become duplicates after lowercasing and trimming.
assumption: The 10-tag limit keeps counting the tags as sent, before normalisation and de-duplication, as it does today for exact duplicates.
check: test/notes.test.js :: still refuses more than 10 tags even when they normalise to fewer

## AC-12: Tags that are already lowercase and trimmed save exactly as before, and duplicates are still removed (e.g. ["work", "planning", "work"] gives ["planning", "work"]).
check: test/notes.test.js :: creates a note with de-duplicated tags

## AC-13: When a note is refused for an invalid tag, the error message is the same as it is today.
check: test/notes.test.js :: the error message for an invalid tag is unchanged

## AC-14: The `tag` filter on the notes list does not change: `tag=Work` matches only tags stored exactly as "Work", so it returns none of the notes saved with "work".
assumption: The story only covers saving tags, so the list filter is left as it is and is not lowercased or trimmed.
check: test/notes.test.js :: the list tag filter is not normalised
