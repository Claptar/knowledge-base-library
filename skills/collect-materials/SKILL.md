---
name: collect-materials
description: Finds and fetches learning materials from a known provider — MIT OCW, Berkeley course sites, GitHub course organisations, university department pages, preprint servers. Use when he wants materials *gathered* rather than judged or taught: "find the Berkeley stat courses", "get me everything from 6.041", "what's in this course org", "is there a course site for X", "download these lecture notes", "add these to resources". Owns the per-provider recipes — URL patterns, where the real material actually lives, what is gated behind a login, and which licence claims are traps. Produces catalogue entries and files in sources/, not a conversation and not a verdict. Use study-mentor when the question is whether a source is any *good*, and adapt-material or adapt-recordings to rewrite one.
---

# Collect Materials

## What this is for

Finding material from a provider is a **mechanical** problem, and it is the same problem every
time for a given provider: where the real files live, what the URL pattern is, what looks public
but is gated, and which licence statement is about the content rather than the website template.
That knowledge is expensive to rediscover and cheap to write down, so this skill writes it down.

**This skill does not judge sources.** Whether a text is worth his time is the `study-mentor`
skill's step 4, which reads its own `taste.md` and writes the verdict. Hand off rather than
improvising a verdict here: a catalogue entry written by this skill carries `Status: unvetted`, and
that is the honest state until someone has actually read the thing.

The division that matters:

| | Owns |
| --- | --- |
| **this skill** | *where it is, whether it can be opened, what licence it carries* |
| `study-mentor` step 4 | *whether it is any good, and what is wrong with it* |

## This skill spans two repositories

The material and the verdict on it live apart, and the split is by authorship:

| Goes to | What |
| --- | --- |
| **this repository** — the library | the download in `sources/<slug>/`, and its entry in `sources/sources.lock.yml` |
| **the knowledge base**, next door | the catalogue entry and its verdict, in `docs/resources/` |

A catalogue entry is *his judgement about a source* and belongs with his notes; the bytes are
someone else's and belong here. `study-mentor` reads the catalogue, never `sources/`.

## The rule that keeps this skill worth having

**Every time you fetch from a provider that has no reference file, write one.** A provider is a
site with a *pattern* — a university department, a course-hosting org, a preprint server, a
publisher. The first harvest from it is research; every one after should be lookup.

Read `references/<provider>.md` before fetching. If there is none, harvest, then create it from
`references/_template.md` and record what you actually verified — not what the site claims. An
hour spent finding that the real material was in a GitHub org rather than on the website is an
hour nobody should spend twice.

Existing recipes:

- `references/mit-ocw.md` — OCW course exports
- `references/berkeley.md` — Berkeley department sites, vanity domains, cross-listings
- `references/github-courses.md` — course material held in GitHub orgs and repos

## Step 1 — identify the provider, and read its recipe

Name the provider before fetching anything. "Find me the Berkeley stat courses" is a `berkeley.md`
job; a lone arXiv link is not a provider job at all — just fetch it.

If a recipe exists, follow it and skip the discovery work. If the recipe turns out to be **wrong**,
that is the most valuable thing you will learn in the session: fix the file, and say in your summary
that it changed. A recipe nobody corrects becomes a confident source of stale instructions, which is
worse than no recipe.

## Step 2 — find where the material actually is

The website is often not the material. Three patterns, all seen in practice:

- **The site is a render of a repository.** Berkeley statistics course sites are Jekyll builds of
  `github.com/berkeley-stat<num>/<semester>`. The repo has the source, the history, and sometimes
  files the site does not link.
- **The site is a shell around a login.** "Lecture notes will be posted on the class website" often
  means a campus LMS — bCourses, Canvas, Moodle. Not reachable, and no amount of searching changes
  that. Mark `Access: unreadable` and say which login it needs.
- **The real material is on an instructor's personal page**, often at a `~username` path, and often
  with directory listing disabled — so the folder 404s while the files inside it fetch fine.
  A search engine will find the files the directory hides.

## Step 3 — resolve the licence before writing anything down

Both repositories publish a site, so a licence error is the one mistake here with consequences
outside them. The rule for what may be converted is in [`AGENTS.md`](../../AGENTS.md); the rule for
what an *adaptation* may do with it is in the knowledge base. What this skill adds is the failure
mode specific to harvesting:

**The licence on the repository is frequently not the licence on the content.** A course website
repo commonly carries the MIT licence of its *Jekyll theme*, complete with the theme author's name
in the copyright line, and the GitHub API reports it as the repository's licence. Recording that as
the course's licence would publish an adaptation that may not be published.

So: **read the LICENSE file, do not read the licence field.** If its copyright line names someone
who is not the course's author or institution, it is the template's licence and the content is
unlicensed — which means all rights reserved.

`unresolved` is a legitimate and safe answer: it means *not found*, not *not licensed*, and it
costs nothing — the source is still collected, and an unresolved licence only blocks adapting it.

## Step 4 — collect the papers too, as their own kind of source

**A paper is not a better course; it is a different object.** Notes and books teach a subject as it
is now understood. A paper is the record of someone arriving at the idea — the problem they were
stuck on, the alternative that looked equally good, the argument they had to make. That record is
what this knowledge base is for, because *how could I have come up with this?* is a question about
the route, and the route is what a published exposition removes.

The failure this step exists to prevent is **papers being absent from the harvest entirely**,
leaving a catalogue built only on second-hand accounts of other people's reasoning.

So, concretely, on any harvest:

- **Catalogue papers as first-class entries**, with `Kind: paper`, in the same subject file as the
  courses. The knowledge base's `docs/resources/cme-transcription.md` is what one looks like.
- **Harvest a syllabus's bibliography.** It is an expert's judgement about which papers matter,
  which is the expensive part, and it is usually the most valuable thing on a syllabus — often more
  so than the slides, and reachable even when the slides are behind a login.
- **When a method carries a name, find its paper.** Gillespie's SSA, the finite state projection,
  the Poisson representation. The secondary account almost always drops the conditions.
- **Collect both where both exist.** The paper carries the motivation, the notes carry the
  machinery and the exercises. Say which is which in the handoff to `study-mentor` — but do not
  write the verdict yourself.

## Step 5 — file it

- **Catalogue entry per source**, in the **knowledge base** repository's `docs/resources/` subject
  file, using the format in that repo's `skills/study-mentor/references/kb-structure.md`.
  `Status: unvetted` always — this skill has not read it. The slug is the source's identity
  everywhere: the catalogue anchor, the `sources/` directory name, and the `docs/` output path.
- **A new subject file** when a provider brings more than a handful of related sources, added to
  the knowledge base's `mkdocs.yml` nav or its strict build fails.
- **Files into `sources/<slug>/`** only when actually downloading. Gitignored, normalised at ingest
  by `scripts/`, never committed.
- **Update the lockfile after any download**, or the new material exists on one machine and nothing
  records that it should exist at all:

  ```bash
  uv run python scripts/lock_sources.py --apply
  ```

  Then **set `base:` by hand** on anything fetched from a web page rather than cloned — the scanner
  cannot infer an upstream from files on disk, so it marks them `restorable: never` until told
  otherwise. Getting this right is the difference between a source that rebuilds anywhere and one
  that quietly depends on a single laptop. `restore_sources.py` rebuilds from the lockfile;
  `--check` verifies on-disk copies against its checksums.
- **Say what you could not reach.** A list of thirty courses where eight are login-gated is more
  useful than a list of twenty-two, because the eight are the ones he might have a login for.

Report counts honestly: how many found, how many reachable, how many with a resolved licence. Those
three numbers differ, and the gaps between them are the useful part.

## Reference files

- `references/_template.md` — the shape of a provider recipe. Start here for a new one.
- `references/mit-ocw.md`, `references/berkeley.md`, `references/github-courses.md`
- `scripts/lock_sources.py` — record what `sources/` holds and what cannot be refetched.
- `scripts/restore_sources.py` — rebuild `sources/` from the lockfile; `--check` verifies it.
- `scripts/course_inventory.py`, `scripts/organise_course.py`, `scripts/normalise_names.py` —
  see what an export holds, sort it, rename it. All dry-run by default.
- `../normalise-materials/SKILL.md` — what happens to a source once it is here.
- [`AGENTS.md`](../../AGENTS.md) — what is converted, what is not, and the traps.

In the **knowledge base** repository, not this one: `study-mentor/references/kb-structure.md` for
the catalogue entry format, and `taste.md` before deciding a paper beats a course.
