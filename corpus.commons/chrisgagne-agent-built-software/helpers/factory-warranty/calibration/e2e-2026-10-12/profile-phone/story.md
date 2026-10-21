# Add an optional phone number to the profile

Some people want us to have a phone number for them, for account recovery later. For now we only need to store it and let them see and change it.

## What we want

- The profile has an optional phone number. People can set it at signup or change or clear it later on their profile.
- Phone numbers are stored in international form (E.164, like +64211234567). Anything else is refused with a clear error.
- People see their own phone number on their profile, and nobody else's.
- Existing accounts keep working and simply have no phone number.
