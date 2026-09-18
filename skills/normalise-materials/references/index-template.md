# The shape of a source index

A converted source is a *book*, and its `index.md` is the front matter: what this is, who wrote it,
under what licence, what is in it, and — the part that is usually missing — **what is not in it**.

Three levels of index exist, and only the first is interesting:

| page | is |
| --- | --- |
| `docs/<discipline>/<provider>/<source>/index.md` | the contents page for one source. The page a topic file links to |
| `docs/<discipline>/index.md` | the sources in one discipline, one line each |
| `docs/index.md` | the library landing page |

**Every source directory has one.** Fourteen did not, which made them dead URLs on the site.

## The source contents page

```markdown
---
title: "MIT 6.041SC — Probabilistic Systems Analysis"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-…/
licence: CC BY-NC-SA 4.0
material: course
converted: '2026-09-14'
---

> **Converted source.** [MIT 6.041SC — Probabilistic Systems Analysis](https://ocw.mit.edu/…) by
> John Tsitsiklis, MIT OpenCourseWare, licensed CC BY-NC-SA 4.0. Converted 2026-09-14. The same
> material in markdown, split so that every part has a URL; nothing here is rewritten.

# MIT 6.041SC — Probabilistic Systems Analysis

24 lectures, 24 recitations and 43 worked examples. Converted from the OCW export: the slide decks
from PDF, the recordings from their caption files.

## Lectures

| | |
| --- | --- |
| [1. Probability models and axioms](lectures/01-probability-models-and-axioms/) | |
| [2. Conditioning and Bayes' rule](lectures/02-conditioning-and-bayes-rule/) | |

## Recordings

| | |
| --- | --- |
| [1. Probability models and axioms](recordings/01-probability-models-and-axioms/) | 50 min |

## Not converted

| | why |
| --- | --- |
| [`lectures/lec01.pdf`](https://ocw.mit.edu/…) | the slide deck this lecture was built from — the `.srt` carries the same material with the mathematics intact |
| [`exams/quiz01-s09.pdf`](https://ocw.mit.edu/…) | scanned, no text layer |
```

### The rules

- **Front matter and banner exactly as for a content page**, minus `source_file`, `route` and
  `fidelity`, which are per-file properties. Add `material:` from the lockfile. The index and its
  pages must not use two different banner formats, which is what they did.
- **One paragraph of orientation, and it is factual**: how many parts, what they were converted
  from, what shape the source was in. Counts and formats — never a verdict on whether the course is
  good. Verdicts live in the knowledge base's `docs/resources/`, one click away, and are his.
- **One section per group** — lectures, recordings, problem sets, exams, solutions — in the order
  the course uses them, never alphabetically interleaved. **Recordings are always their own
  section**, never mixed into the lectures: a transcript of speech and a set of typeset notes are
  different objects, and reading a directory that alternates `01-captions`, `01-slides`,
  `01-transcript` tells you nothing about which to open.
- **Parts in the source's own order and numbering.** Not alphabetical, which put lecture 10 before
  lecture 2.
- **A `Not converted` section whenever anything was skipped**, naming each file, linking to the
  original, and giving the reason in a few words. This is the section that makes dropping material
  honest rather than silent, and it is the only place a reader can learn that the handwritten
  lectures exist at all.
- Links are relative and end in `/`, matching `use_directory_urls: true`.

## The discipline index

One line per source: the title, the number of pages, and the licence. It is a switchboard, and
nobody reads it — keep it short and do not editorialise.

## The library landing page

Generated from the lockfile. It states the total page count, the number of sources, and the split by
discipline, and it says plainly what this repository is: *someone else's material, converted*. It
links to the knowledge base for the part that is his.

**Count things once.** The landing page said "61 sources converted" while the lockfile held 69
slugs, `sources/` held 41 directories and `docs/` held 33. Four numbers for one thing, none of them
checkable. Every count on a generated page is computed at generation time from the tree it
describes.
