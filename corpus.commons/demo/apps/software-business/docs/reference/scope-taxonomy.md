# Distribution scope

The five-level taxonomy that governs which references ship in which app.

## Field locations

| Where | What it does |
|---|---|
| `**Scope:**` line in each deep reference's frontmatter | Declares the scope of that source |
| `max_scope:` in each build profile (`builds.yaml`) | Sets the profile's ceiling |
| `{scope}` suffix on packaged tarballs (`npm run package`) | Carries the most-restrictive scope in the bundle |

## Levels

| Rank | Scope | What goes here |
|---|---|---|
| 0 | `open` | Public-domain, CC0, CC BY, CC BY-SA, MIT, Apache, government works |
| 1 | `open-nc` | CC BY-NC, CC BY-NC-SA: open with non-commercial restriction |
| 2 | `copyrighted` | Published all-rights-reserved material the operator has legitimate access to |
| 3 | `confidential` | Bounded-access engagement material (client docs, past AARs, incident data) |
| 4 | `personal` | Operator's own private notes, journals, drafts |

Levels are monotonic in risk: higher rank means tighter redistribution.

## Build-time filter

A reference's scope rank is compared to its profile's `max_scope` rank. If reference rank > ceiling rank, the reference is excluded from that profile's build. The filter runs once at build time and is mechanical; no operator override.

| Profile `max_scope` | Admits | Excludes |
|---|---|---|
| `open` | open | open-nc, copyrighted, confidential, personal |
| `open-nc` | open, open-nc | copyrighted, confidential, personal |
| `copyrighted` | open, open-nc, copyrighted | confidential, personal |
| `confidential` | open, open-nc, copyrighted, confidential | personal |

`personal` is never admitted by any profile. It is excluded by construction.

## Package-time label

`npm run package` reads every shipped reference's `**Scope:**` line, computes the most-restrictive scope in the bundle, and stamps it into the tarball filename: `{app}-v{version}-{scope}.tar.gz`. The constraint travels with the artefact. The same tarball also contains `LICENCE-MANIFEST.md` listing every reference's individual scope and licence.

## Scope vs. licence

These are different fields and do diverge:

- **Licence** governs attribution and derivative rights (CC BY 4.0, CC BY-NC-SA 4.0, MIT, all-rights-reserved, etc.). It is a property of the source.
- **Scope** governs distribution risk in the operator's context. It is a property of the operator's intent.

A CC BY 4.0 paper used inside a confidential engagement is `Licence: CC BY 4.0`, `Scope: confidential`. Both ride on the deep reference.

Scope can only narrow distribution further; it cannot widen the rights the source's licence grants. Marking an all-rights-reserved source as `Scope: open` does not make it lawful to redistribute, and the build's mechanical filter does not arbitrate that question; the operator's licence-compliance check sits above the scope filter, not under it.

## See also

- `**Scope:**` field syntax in every deep reference at [`references/`](../../references/)
- The `max_scope` field in [`builds.yaml`](../../builds.yaml)
- The packager at [`scripts/package.js`](../../scripts/package.js)
- The architectural argument for the mechanism at [`docs/architecture/copyright.md`](../architecture/copyright.md)
