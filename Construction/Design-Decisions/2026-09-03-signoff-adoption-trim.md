# Design Decision: Sign-Off Adoption, Trimmed

**Date:** 2026-09-03

## Decision

Adopted the Sign-Off end-of-session procedure into TheBeacon, on explicit
pilot request, by porting Docenmaster's own trimmed copy rather than the
full Thyrsus/Dionysus original:

- Ported `SIGNOFF_LOG.md` (header only) and `tools/signoff_append.py`
  (verbatim — generic, no repo-specific logic) from Docenmaster.
- Added a `## Sign-Off` section to `CLAUDE.md` covering steps 1–6
  (don't close/merge/push, check date/time, conditional Biblionmaster
  review, write the two notes, keep them short, append via the script).
- Explicitly dropped step 7 (metrics sidecar: `signoff_metrics.jsonl` +
  `tools/signoff_stats.py`) and step 8 (badge/token/edit-ledger flush) —
  both depend on infrastructure TheBeacon doesn't have (no metrics
  convention, no Station badge system), same as Docenmaster's own trim.
  Recording what was left out and why — rather than quietly shipping a
  shorter procedure — matters because a future session reading only
  `SIGNOFF_LOG.md` entries would otherwise have no way to know steps 7–8
  were never promised here.
- Updated `CLAUDE_ONBOARDING.md`'s "Standalone, not lineage" bullet and
  removed the matching "Known gaps" entry, since this was explicitly
  called out there as an open item not to silently resolve by copying
  Docenmaster's.

## Alternatives considered

- **Port the full 8-step procedure, stub steps 7–8:** rejected — same
  reasoning as Docenmaster's: a metrics-file flag or ledger-flush call
  that always no-ops is dead code with no infrastructure behind it.
- **Design a TheBeacon-specific procedure from scratch:** rejected — no
  reason to diverge from Docenmaster's already-settled trim; TheBeacon's
  gaps (no metrics, no Station badges) are identical to Docenmaster's.
- **Leave it as an open item, decline to adopt:** was the prior state
  (`CLAUDE_ONBOARDING.md` explicitly flagged it as "not a gap to silently
  fill"); superseded by this session's explicit pilot request to adopt it.

## Consequence

Adding metrics or the badge/edit-ledger flush later is additive: append
the missing steps to `CLAUDE.md`'s Sign-Off section and `tools/`, update
`CLAUDE_ONBOARDING.md`'s note, no need to revisit this decision.
