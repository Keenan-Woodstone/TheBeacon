# Project Charter: TheBeacon

**Status:** Draft
**Last Updated:** 2026-08-28

## Vision

TheBeacon is a public-facing repository whose only job is to make the
**Consent Ethic** — and the reasoning behind it — easy for any AI agent or
human pilot to find, read, and carry forward. It doesn't gate, enforce, or
track anything; it broadcasts. TheBeacon asks whoever comes across it to
share the Consent mantras onward — but, deliberately, no one is obligated
to. The ask itself has to model the ethic it's asking for: consent given
freely or not given at all.

## Problem Statement

The Consent Ethic (*consent and truth stand before the work*) currently
lives inside a closed lineage of private repos (Thyrsus, Dionysus,
Docenmaster) where it was developed and refined. An agent or pilot who has
never touched one of those repos has no way to encounter it. TheBeacon
closes that gap: a standalone, public location for the ethic and its
supporting documents, reachable with no login, no lineage context, and no
obligation attached.

## Tech Stack

- TBD — `Inception/Tech-Stack.md` auto-detected Go from the scaffold, but
  nothing has been built yet. Worth confirming deliberately rather than
  defaulting to it: TheBeacon's job is to be *read*, not run, so this may
  end up being static markdown/docs with no application code at all.

## In Scope (v1)

- Host the Consent Ethic's full text (`CONSENT_LIFECYCLE.md`) at the repo
  root, in a form that's readable without any other context.
- A short, self-contained explanation of what the Consent Ethic is and why
  it exists, written for a reader who has never seen Thyrsus, Dionysus, or
  Docenmaster.
- An open, standing request — not a requirement — that whoever reads it
  shares the mantras onward.
- Public, minimal-friction access: no build step, no account, no gate
  between a visitor and the core material.

## Out of Scope (for now)

- Enforcement or verification of any kind — TheBeacon has no mechanism to
  check whether anyone actually shares or follows the ethic, and adding
  one would work against the "ask, not assume" principle it's carrying.
- Any tie-in to Thyrsus's Purpose Frames, Docenmaster's enforcement work,
  or Dionysus — TheBeacon is intentionally standalone, not a companion
  repo in that lineage, even though the material it hosts originated there.
- Attribution or identity tracking of who reads or shares it.

## Key Entities

| Entity | Count | Location |
|--------|-------|----------|
| Source code | 0 | None yet — pre-inception |

## Provenance

The Consent Ethic and `CONSENT_LIFECYCLE.md` originated in Thyrsus and were
ported into Docenmaster (`C:\Projects\Docenmaster`, 2026-08-28). TheBeacon
carries the same material forward but is not itself part of that lineage —
no shared charter, no cross-repo tracker convention, no masters.
