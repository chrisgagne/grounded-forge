# Summary email: no more false failures and duplicates

At busy times our mail provider takes 6 to 10 seconds to accept a message. The app gives up after 5 seconds and tells the person their summary email failed; they press the button again, and then both emails arrive. We get complaints both ways.

## What we want

- Don't make people wait on the mail provider: show the summary as soon as it's ready.
- Stop telling people their email failed when the provider was only slow.
