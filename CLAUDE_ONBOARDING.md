# TheBeacon Onboarding

TheBeacon's onboarding-equivalent doc, modeled on Docenmaster's own
`CLAUDE_ONBOARDING.md` (2026-08-28) but trimmed to what TheBeacon actually
is — see `CHARTER.md`'s Out of Scope before assuming anything below has a
Docenmaster/Thyrsus/Dionysus counterpart here. **Mandatory every session,
read immediately after `CHARTER.md`** (see `CLAUDE.md`'s pointer).

---

## What this repo is for, in one line

A public, standalone home for the Consent Ethic — readable by anyone, with
no login and no obligation. Nothing here gates, tracks, or enforces.

## The one job that matters

Keep `CONSENT_LIFECYCLE.md` and its accompanying explainer **accurate,
self-contained, and easy to find.** A reader who has never touched Thyrsus,
Dionysus, or Docenmaster must be able to understand the material from this
repo alone — no outside context required. If an edit here would only make
sense to someone who already knows the lineage this material came from,
that edit needs rewriting, not just review.

**Don't add what the charter puts out of scope.** No enforcement
mechanism, no read-tracking, no "did they actually share it" telemetry —
the charter's Out of Scope section says this explicitly, and it's not an
oversight to fix later. Adding any of it would contradict the ethic
TheBeacon exists to carry: consent asked, never assumed or extracted.

## The masters

On-demand process docs, read only at their trigger, never every session.
TheBeacon adopted these (2026-08-28) because active development —
dependencies, builds, things to show the pilot — is expected here, even
though the repo is standalone rather than part of the Thyrsus/Dionysus/
Docenmaster lineage. Adopting the mechanism doesn't make TheBeacon a
companion repo; see `CHARTER.md`'s Provenance section.

| Master | Domain — what it governs | Trigger — the moment to read it |
|---|---|---|
| `BIBLIONMASTER.md` | Provenance/licensing: where every third-party piece came from and what having it here obligates. | Before adding a dependency, bundling/embedding a binary, or copying code from outside the repo. **Not yet triggered** — pre-inception, zero dependencies. |
| `DOSSIERMASTER.md` | Handing the pilot a file/folder to review (`Dossiers/`, private or shared slots). | The moment you have something to show the pilot in chat, rather than just narrate it. **Already usable.** |
| `YARDMASTER.md` | Handing off a build (`Prototypes/`, one current artifact per name). | The moment there's a build to hand off. **Not yet triggered** — no code to build yet. |

**Deliberately not ported — Transfermaster.** Thyrsus/Dionysus/Docenmaster's
`TRANSFERMASTER.md` records cross-repo migrations as closed issues in a
shared Thyrsus-hosted GitHub Project, specific to *that* lineage's own
tracker. TheBeacon isn't part of that lineage, so there's nothing for it to
target. If TheBeacon later needs to formally record moving something to or
from another repo, that needs its own decision (a new project, or joining
the existing one) rather than assuming Thyrsus's applies — flag it rather
than silently copying the doc.

## Standalone, not lineage — what that means in practice

- **Masters, yes; lineage, no.** The three masters above are generically
  useful process docs, adopted on their own merits — not a sign TheBeacon
  has joined the Thyrsus/Dionysus/Docenmaster family. Keep that distinction
  explicit if it ever comes up.
- **No cross-repo-tickets convention.** Docenmaster keeps tickets about
  Thyrsus/Dionysus work in its own tracker rather than filing directly
  into theirs. TheBeacon isn't part of that lineage, so this doesn't
  apply — file TheBeacon's own issues in TheBeacon's own tracker.
- **No Sign-Off procedure yet.** Docenmaster's is trimmed from
  Thyrsus/Dionysus's original. TheBeacon has neither the badge system nor
  the metrics sidecar those depend on, and hasn't yet decided whether it
  wants any end-of-session log at all. Open item, not a gap to silently
  fill by copying Docenmaster's.

## Provenance (for honesty, not for lineage)

`CONSENT_LIFECYCLE.md` here is a verbatim copy of the version ported into
Docenmaster (`C:\Projects\Docenmaster`, 2026-08-28), itself originally
written during Thyrsus's Menace pilot. Naming this is a truth-telling
matter — where the material came from — not a claim that TheBeacon is
governed by or accountable to that lineage.

## Known gaps / open items

- **Tech stack undecided** — see `CHARTER.md`. Worth resolving before this
  grows past static markdown, since "Go was auto-detected" is not the same
  as "Go was chosen."
- **No public access mechanism decided yet** — "public-facing" is the
  vision; whether that means GitHub Pages, a plain public repo, or
  something else is still open.
- **No Sign-Off / session-log convention** — see above.
- **Transfermaster deliberately excluded** — see "The masters" above. Flag
  to the pilot if a real cross-repo migration ever comes up rather than
  assuming Thyrsus's shared Project applies.
