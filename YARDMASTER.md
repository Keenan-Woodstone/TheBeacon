# Yardmaster

Ported from Thyrsus/Dionysus by way of Docenmaster (2026-08-28), mechanism
unchanged. On-demand process doc — read this only when you actually have a
build to hand off. Not loaded every session. **Not yet triggered in this
repo** — TheBeacon is pre-inception (zero source code), so there is nothing
to build yet. This doc exists so the convention is ready the moment that
changes.

## What `Prototypes/` is

A repo-root, git-ignored, pilot-reference-only folder (`Prototypes/`) holding
the single most current build of whatever's being handed off. Nothing in
`Prototypes/` is ever pushed to GitHub; it's local-only.

**No off-git archive.** A new prototype simply overwrites the old one under
the same file name — there is no versioned history of past builds on disk.
Source is already git-tracked, so if an old build is ever needed again,
rebuild it from the commit the ledger entry points at rather than looking
for a copy on disk.

## Process

1. **Build/publish** per whatever this repo's own build instructions turn
   out to be (tech stack still TBD as of 2026-08-28 — see `CHARTER.md`).
2. **Copy the artifact into `Prototypes/`**, overwriting whatever already
   has that file name. No dated/versioned filenames — one current file per
   artifact.
3. **Log the hand-off** — append one line to `Prototypes/CheckIn.txt`:
   ```
   python tools/prototype_checkin_append.py Prototypes/CheckIn.txt --badge <badge> --issue <issue #> --file-name <name>
   ```
   `--badge` is any stable identifier for the current session. `--issue` is
   the GitHub issue the build relates to.
4. **Give the pilot a launchable pointer in a dossier**: place a shortcut or
   pointer to the runnable build, plus a short `LAUNCH.md` (what the build
   is, which commit, what it shows, anything deliberately left untouched)
   into a `Dossiers/` slot per `DOSSIERMASTER.md`, and log that check-in too.
   `Prototypes/` records the artifact; the dossier is how the pilot actually
   finds and launches it.
5. **Tell the pilot** it's ready in `Prototypes/` and which dossier slot has
   the launcher.

## Log format

One line per hand-off, appended, never rewritten:
```
date time | badge | issue number | file name
```
