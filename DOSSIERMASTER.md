# Dossiermaster

Ported from Thyrsus/Dionysus by way of Docenmaster (2026-08-28), mechanism
unchanged. On-demand process doc — read this only when you actually have
something to show the pilot for review. Not loaded every session.

## What `Dossiers/` is

A repo-root, pilot-reference-only folder (`Dossiers/`) for a file or folder an
agent wants the pilot to look at — a report, a screenshot set, a draft doc, a
test script for another session to follow — anything that isn't itself a
shipped deliverable. It has **two kinds of slot**, 20 of each:

| | Private | Shared |
|---|---|---|
| Slots | `Dossiers/#1/` … `Dossiers/#20/` | `Dossiers/Shared/#1/` … `Dossiers/Shared/#20/` |
| Git | **ignored** — this machine only | **tracked and pushed** — any clone sees it |
| Log | `Dossiers/CheckIn.txt` (local) | `Dossiers/Shared/CheckIn.txt` (tracked) |
| Use when | only the pilot, on this machine, needs it | another machine, another session, or the pilot's laptop needs it |

If nothing else needs to read it, keep it private. Anything placed in a
shared slot gets committed and pushed like source, so no secrets, no large
artefacts (that's `Prototypes/`, once this repo has builds to hand off).

**A note specific to TheBeacon:** this repo's own root is meant to stay
public-facing and read-only for outside visitors (see `CHARTER.md`). Even
shared dossier slots are for *the pilot's own* working material across
machines, not for the public-facing content itself — don't confuse a
`Dossiers/Shared/` submission with something meant for TheBeacon's visitors.

## Process

1. **Choose private or shared** (table above).
2. **Pick a slot.** Read the matching `CheckIn.txt`. For each slot 1–20, find
   its most recent entry (last occurrence of that dossier number in the log —
   later lines win). Use whichever slot has **no entry yet**; if all 20 have
   been used at least once, use the slot whose most recent entry is furthest
   back in the log (least recently used).
3. **Place the file or folder** into that slot, replacing whatever was there
   before. Shared slots carry a `.gitkeep` so the empty folder exists on every
   clone — leave it.
4. **Log the submission** — append one line to the matching log:
   ```
   python tools/dossier_checkin_append.py Dossiers/CheckIn.txt        --badge <badge> --issue <issue #> --dossier <N> --file-name <name>
   python tools/dossier_checkin_append.py Dossiers/Shared/CheckIn.txt --badge <badge> --issue <issue #> --dossier <N> --file-name <name>
   ```
   `--badge` is any stable identifier for the current session (TheBeacon has
   no Station badge-minting system — Thyrsus/Dionysus's is specific to those
   repos; a short session label is enough here). `--issue` is the GitHub
   issue the dossier relates to.
5. **Shared only:** commit the slot contents and the log line together
   (`Refs #<issue>`), and push if the reader is on another machine.
6. **Tell the pilot** which dossier to look at — "check Dossiers/#N" or
   "check Dossiers/Shared/#N".

## Log format

One line per submission, appended, never rewritten — same format in both logs:
```
date time | badge | issue number | dossier number | file name
```
Example: `2026-08-28 08:41 | claude-code | 11 | 2 | TheBeacon-draft/`

## Same process, every repo

This file, the two-kind layout, and `tools/dossier_checkin_append.py` are
identical in Dionysus, Thyrsus, Docenmaster, and BattleBrothers (pilot's
decision, 2026-08-23: "Dossiermaster needs to be updated across all
projects"). TheBeacon adopts the mechanism as of 2026-08-28 because it's a
generically useful review pattern — this does **not** make TheBeacon a
companion repo in that lineage; see `CHARTER.md`'s Provenance section.
Thyrsus/Dionysus also carry a Dossiermaster GUI snap-module for reviewing
slots visually — that's specific to Thyrsus's Purpose Frame/snap-module
architecture and doesn't apply here; the process above (folders + logs) is
the whole mechanism in this repo.
