# Notes list: total and top tags

On the notes page we want to show "You have 1,284 notes" and the person's five most-used tags as one-click filters above the list.

## What we want

- `GET /notes` also returns `total`: how many notes the person has, or how many have the selected tag when they filter.
- And `topTags`: the five tags they use most across all their notes, with counts, most-used first.
- The list itself works as today.
