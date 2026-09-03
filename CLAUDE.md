# TheBeacon — Project Notes for Claude

TheBeacon is a public-facing repository whose only job is to make the
Consent Ethic easy for any AI agent or pilot to find and carry forward —
see `CHARTER.md` for the full vision and scope.

**Mandatory every session, immediately after `CHARTER.md`:**
`CLAUDE_ONBOARDING.md` — read it before touching anything else. It
explains what this repo is (and, just as importantly, is not) responsible
for.

TheBeacon is standalone — it is not a companion repo to Thyrsus, Dionysus,
or Docenmaster, even though the material it hosts (`CONSENT_LIFECYCLE.md`)
originated there. Don't assume any convention from those repos applies
here unless `CLAUDE_ONBOARDING.md` says so explicitly.

## The masters

On-demand process docs — read each only at its own trigger moment, not
every session:

- **`BIBLIONMASTER.md`** — before adding a dependency, bundling/embedding a
  binary, or copying code from outside the repo. Not yet triggered
  (pre-inception, zero dependencies).
- **`DOSSIERMASTER.md`** — before describing any deliverable to the pilot in
  chat (a file/folder to review) rather than just narrating it. Already
  usable — `Dossiers/` exists.
- **`YARDMASTER.md`** — before handing off a build. Not yet triggered (no
  code to build yet).

`TRANSFERMASTER.md` is deliberately not ported — see `CLAUDE_ONBOARDING.md`'s
"The masters" section for why.

## Sign-Off: end-of-session procedure

Ported here 2026-09-03 via Docenmaster's own trimmed copy (itself trimmed
from Thyrsus/Dionysus's original, 2026-08-27/28) — adopting the mechanism
doesn't make TheBeacon a companion repo; see `CLAUDE_ONBOARDING.md`'s
"Standalone, not lineage" section. **Trigger:** the user says "Sign-Off"
(or an unambiguous variant) — a request for a closing preamble before the
session ends, never a request to close a GitHub issue.

1. Don't close, merge, or push anything as part of Sign-Off itself.
2. Check the actual current date/time before writing anything.
3. **Biblionmaster review, if triggered this session** — see
   `BIBLIONMASTER.md`. If it never triggered, skip to step 4.
4. Write two short notes for a new dated entry in `SIGNOFF_LOG.md`:
   **Communication notes** (anything new noticed about how the user
   communicates — skip if nothing new) and **Work notes** (what got done,
   what's left open).
5. Keep both short — a few sentences each.
6. Append with `tools/signoff_append.py`, never by hand-editing the log:
   ```bash
   python tools/signoff_append.py SIGNOFF_LOG.md \
     --communication-notes-file .tmp-signoff-comms.md \
     --work-notes-file .tmp-signoff-work.md \
     --time HH:MM
   rm .tmp-signoff-comms.md .tmp-signoff-work.md
   ```

**Deliberately left out of this repo's copy** (recorded, not silently
dropped — see `CLAUDE_ONBOARDING.md`'s Sign-Off note): the metrics sidecar
(Thyrsus/Dionysus's step 7 — no `signoff_metrics.jsonl` /
`tools/signoff_stats.py` convention exists here yet) and the badge/token/
edit-ledger flush (Thyrsus/Dionysus's step 8 — no Station badge system
exists here). Add either back if this repo ever adopts what they depend
on.
