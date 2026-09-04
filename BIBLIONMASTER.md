# Biblionmaster

Ported from Thyrsus/Dionysus by way of Docenmaster (2026-08-28). On-demand
process doc — read this at the moment one of the trigger moments below
actually happens, not every session. The name is from *biblion*, the Greek
for a book or written record: this role keeps the record of where the code
came from and what that obliges the project to do.

**Not yet triggered in this repo.** TheBeacon is pre-inception (zero source
code, no dependencies, no `LICENSE` file yet) as of 2026-08-28. This doc
exists so the convention is ready the moment code, a dependency, or a
licensing decision enters the picture — likely once TheBeacon's own
tech-stack decision (`CHARTER.md`, still TBD) is made and real development
starts.

## What the Biblionmaster is

A named role, in the same family as the Dossiermaster (`DOSSIERMASTER.md`)
and the Yardmaster (`YARDMASTER.md`). Where those hand things *to* the
pilot, the Biblionmaster answers one question about everything in the repo:
**where did this come from, and what does having it here obligate us to
do?** It is the owner of provenance — the source, author, licence and pinned
version of every third-party piece — and of keeping `THIRD-PARTY-NOTICES.txt`
true once one exists.

It is **not** legal counsel, and it never pretends to be. It reads licence
texts and published guidance, applies them carefully, and writes down its
reasoning with sources. When a question crosses the line into something only
a professional should answer, it stops and flags (see "Escalation" below).
Where consent cannot be asked, the work is ended, not attempted.

## What it owns (once triggered)

| Artifact | Role |
|---|---|
| `THIRD-PARTY-NOTICES.txt` (repo root) | The single authoritative statement of what third-party software this project redistributes or depends on, under what licence, from where. Every shipped component appears here. Doesn't exist yet — created on first trigger. |
| `third_party/` | Vendored licence texts (`third_party/licenses/`) and, for copyleft components conveyed as binaries, the corresponding source pinned to the exact commit built against, with a `PROVENANCE.md`. |
| `LICENSE` | This project's own licence — not yet chosen. A pilot decision, made once relevant (likely alongside the tech-stack decision). The Biblionmaster reads it and reasons from it once it exists; it **never edits it**. |
| `Construction/Biblionmaster/` | The role's working papers: a research Q&A, an audit rubric, and each audit's findings. Created on first trigger — see Thyrsus's, Dionysus's, or Docenmaster's `Construction/Biblionmaster/` for the template shape. |

## Trigger moments

Any of these means: read this doc, follow the procedure. They don't
announce themselves, which is why they're listed.

1. **Adding a dependency** — a package manager reference, an npm package, a
   Python import that isn't stdlib, a bundled DLL — once this repo's tech
   stack is chosen.
2. **Bundling or embedding a binary** — into anything that ships.
3. **Copying code from outside the repo** — a snippet from Stack Overflow, a
   GitHub gist, a blog post, SDK sample code. Adapting counts as copying.
4. **Changing how an existing component is used** — static → dynamic
   linking, an optional dependency becoming required, a dev-only tool
   becoming shipped.
5. **Upgrading a pinned component** — licences change between versions;
   re-check, don't assume.
6. **Splitting or separately distributing a component.** This is a
   re-licensing question; the Biblionmaster flags it, it does not decide.
7. **A scheduled or requested audit** — none has run in this repo yet; none
   is due until there's something to audit.

## Procedure: a single new component (triggers 1–5)

1. **Identify it precisely.** Name, upstream URL, author/copyright holder,
   exact version or commit, and how the bytes were obtained.
2. **Determine the licence from primary evidence** — the `LICENSE` file in
   the upstream tree at that version, or the package's licence metadata.
   Record it as an SPDX identifier (`MIT`, `Apache-2.0`, `LGPL-3.0-only`, …).
   If the licence file carries extra attributions beyond the standard text,
   vendor the whole file, not just the identifier.
3. **Classify how it's used.** One of: **linked**, **bundled**,
   **modified-and-bundled**, **copied**, **build-time only** (not shipped —
   build-time-only components are recorded but carry no redistribution
   obligation).
4. **Work out the obligations** that licence places on *that* use — notice +
   licence text for MIT/BSD/Apache; NOTICE-file propagation for Apache;
   licence copy + notice for unmodified LGPL; corresponding source for GPL
   binaries conveyed; attribution + share-alike for CC BY-SA snippets.
5. **Check compatibility** with whatever licence this repo eventually
   chooses. Permissive and LGPL are usually safe to combine with anything;
   another copyleft licence, a non-commercial clause, a "no derivatives"
   clause, or a proprietary EULA: **stop and escalate** (see below).
6. **Record it.** Add or update the `THIRD-PARTY-NOTICES.txt` entry — what
   it is, author, source URL, licence, version/pin, how it's used, and where
   the licence text lives. Vendor the licence text into `third_party/licenses/`.
7. **For copied code (trigger 3):** add a source comment at the copy site —
   URL, author, licence, date — *and* a notices entry.
8. **Commit the notices change in the same commit** as the dependency or
   copy that caused it. A notices file that lags the code is the failure
   mode this role exists to prevent.

## Escalation: when the Biblionmaster stops

These are flagged to the pilot as "needs professional advice", with the
facts gathered so far, and **not answered** by the agent.

- Any question about a third-party platform's EULA or terms.
- Whether a specific linking/combination arrangement makes something a
  "work based on" a copyleft component.
- A licence conflict between two components already shipped.
- Any proposal to distribute the project, or part of it, commercially.
- A takedown, a complaint, or any contact from a rights-holder.
- Code whose authorship is unclear (including substantial agent-generated
  code where the copyright position matters for a licence decision).

## Voice and records

Like the other process docs, this is impersonal: the human operator is "the
pilot". Findings are about components and licences, never about people.
Everything the role concludes is written down with its sources — *recorded,
not remembered* — so the next session, or a professional brought in later,
can check the reasoning rather than trust it.
