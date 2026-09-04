# Design Decision: Bootstrap public discovery layer

**Issue:** #1
**Date:** 2026-08-28

## Content license: CC BY 4.0

**Alternatives considered:**
- **CC0** (public domain dedication) — most literal match for "no
  obligation attached," but severs the provenance thread CHARTER.md's
  Provenance section is explicit about (Thyrsus → Docenmaster → TheBeacon).
  Someone could republish the mantra with no trace back to where it came
  from.
- **Defer, record reasoning only** — satisfies the AC without picking a
  license, but leaves reuse rights ambiguous by silence for however long
  the deferral lasts, which works against "minimal-friction access."
- **CC BY 4.0 (chosen)** — free to copy, share, and adapt, provided the
  reuser credits TheBeacon. Keeps the provenance thread alive while still
  being maximally shareable. User confirmed this choice directly
  (2026-08-28) when asked to weigh the three options.

## Scope split: "Letter from the Agent" moved to #3

The original #1 scope included a rubric-gated "Letter from the Agent"
column. The rubric doesn't exist yet, and the framework's AC-gate markers
(`QA:`, `GATE: review`, `GATE: release`) don't have a token for "blocked on
an external prerequisite that isn't a review or release step" — forcing
one of those markers onto this AC would have been inaccurate.

Rather than leave #1 permanently unable to reach `in_review`, the rubric +
letter work was split into #3, following the framework's own precedent
that work owned by another checklist is removed, not annotated. #1 now
covers only the four deliverables that don't depend on the rubric
(README, explainer, share-ask, license) and can close on its own once
those are done.
