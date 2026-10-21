# Location check of the grader's catches (2026-10-14)

A code check, not a model: for every held-out trial Sol graded as caught, does the blocking finding Sol credited point
into the code the real fix changed? The check takes the finding's file and line (in the buggy code under review) and
the fix's `git diff -U0 parent commit` hunks on the code files (old side, the same numbering), and counts a
finding as inside when its line falls within 5 lines of a hunk.

| Result | Trials |
|---|---|
| Inside the fix's lines (±5) | 31 |
| Same file, further away | 5 |
| A different file | 0 |

The five further away:
- rb04 t1 and t2, line 245, where the fix adds a guard at line 217. Sol's reason: the finding names the removed guard.
- rb08 t1, t2 and t3, line 36, where the fix adds a line at 30. Sol's reason: the finding names the weekend result
  the fix corrects.

This lowers one risk, that Sol credited findings about something else entirely, and leaves PROPOSED-G open: a location
match doesn't show that a finding describes the defect, and no human has checked the grader.
