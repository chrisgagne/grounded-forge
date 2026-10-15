## AC-1: Signing up with a valid E.164 phone number (for example `+64211234567`) creates the account, and the profile in the signup response contains exactly that `phoneNumber`.
check: test/auth.test.js :: signup stores an optional phone number in E.164 form
assumption: The profile field is called `phoneNumber`, both in request bodies and in every profile response.

## AC-2: Signing up without a phone number creates the account, and its profile has `phoneNumber: null`.
check: test/auth.test.js :: signup without a phone number gives a profile with no phone number
assumption: At signup, leaving the field out, sending `null` or sending an empty string all mean "no phone number". This matches how the optional `dateOfBirth` is handled today.

## AC-3: Signing up with a phone number that is not in E.164 form is answered with 400 and an error message that names the required international format, and no account is created (a later signup with the same email and a valid phone number succeeds with 201).
check: test/auth.test.js :: signup rejects a phone number that is not in E.164 form and creates no account
assumption: "E.164 form" means a string that is `+`, then a digit from 1 to 9, then up to 14 more digits (2 to 15 digits in total). Nothing is normalised. Inputs like `0211234567`, `64211234567`, `+64 21 123 4567`, `+64-21-123-4567`, `+(64)211234567`, `+0211234567`, `+1234567890123456` (16 digits), `+64abc`, surrounding whitespace, and non-string values such as the number `64211234567` are all refused.

## AC-4: After signup with a phone number, the signed-in user's `GET /me` and the profile returned by `POST /login` both show that same `phoneNumber`.
check: test/users.test.js :: GET /me and login show the user's own phone number

## AC-5: `PATCH /me` with a valid E.164 `phoneNumber` answers 200 with the new number in the profile, and a later `GET /me` shows the new number.
check: test/users.test.js :: PATCH /me sets and changes the phone number

## AC-6: `PATCH /me` with `phoneNumber: null` clears a previously stored phone number: the response and a later `GET /me` both show `phoneNumber: null`.
check: test/users.test.js :: PATCH /me can clear the phone number
assumption: An empty string `""` also clears the number, the same way it does for `dateOfBirth`.

## AC-7: `PATCH /me` with a `phoneNumber` that is not in E.164 form is answered with 400 and an error message that names the required international format, and the previously stored phone number (and the rest of the profile) is unchanged on a later `GET /me`.
check: test/users.test.js :: PATCH /me rejects phone numbers that are not in E.164 form and keeps the old one
assumption: In a request that has an invalid `phoneNumber` alongside other valid changes (such as `name`), the whole request is refused and none of the changes are applied.

## AC-8: `PATCH /me` that leaves out `phoneNumber` (for example, changing only `name`) leaves the stored phone number as it was.
check: test/users.test.js :: PATCH /me without a phone number leaves the stored one unchanged

## AC-9: When two users each have a phone number, each user's `GET /me` shows only their own number, and neither user's responses from `/me`, `/login` or `/notes` ever contain the other user's number.
check: test/users.test.js :: each user sees only their own phone number

## AC-10: `GET /me` and `PATCH /me` with a phone number, made without a valid session, are answered with 401, and no stored phone number changes.
check: test/users.test.js :: phone number cannot be read or changed without a session

## AC-11: A user whose account was created before the phone number change can still log in after the migrations run, and their profile shows `phoneNumber: null` with their id, email, name and date of birth unchanged.
check: test/migrations.test.js :: existing accounts keep working with no phone number after migrating

## AC-12: Rolling back the latest migration (the one that adds phone numbers) leaves all existing accounts and their other profile fields in place, and running the migrations up again works and gives them `phoneNumber: null`.
check: test/migrations.test.js :: rolling back the phone number migration keeps existing accounts

## AC-13: When a user with a phone number asks for a summary of their notes (with or without email), the phone number does not appear anywhere in what is sent to the LLM provider.
check: test/summary.test.js :: the phone number is never sent to the model
