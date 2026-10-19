# Fix dates of birth from the old signup form

Accounts created before March 2024 came through the old signup form, which saved date of birth as DD/MM/YYYY. Everything since expects YYYY-MM-DD, so those people see a wrong or blank date on their profile, and anything that reads their date of birth gets it wrong.

## What we want

- Every stored date of birth is an ISO date (YYYY-MM-DD).
- Existing DD/MM/YYYY dates are converted.
- The API doesn't change: `dateOfBirth` in, `dateOfBirth` out.
