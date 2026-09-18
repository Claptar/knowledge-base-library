# The shape of a course book

**This is what the library is for.** Not a pile of converted artefacts — a coherent set of lecture
notes per course, written from everything that course provides, with the same structure for every
course so that moving between them costs nothing.

The distinction that makes this worth doing, in his words: *"instead of taking the best from each
one and combining in one good book you keep all of those separate as if the task is not to convert
it into usable teaching material but to hoard all books and courses in one place. For that I could
have just kept them in PDF."*

A converted artefact answers *what did the source say on page 19*. A book answers *teach me this
subject*. Only the second is worth hosting, because the first is the original file.

## Simpler and better

**His words, and the rule every choice here is judged by.** Not simpler *or* better — the two
together, because a change that buys quality with complexity usually pays for it later and a change
that buys simplicity with quality was not worth making.

Worked example, from the figures. The books need mathematical illustrations, and three routes were
on the table:

| route | why not |
| --- | --- |
| ASCII art in a code fence | what the model did unprompted. `┌─┐` and `╲` is an apology for a diagram, not a diagram |
| manim | renders `png\|gif\|mp4\|webm\|mov` — **no vector output**. Raster breaks the light/dark toggle, and it needs LaTeX and ffmpeg in CI to execute generated Python per figure |
| **inline SVG** | vector, no dependency, and `currentColor` makes it legible in both themes |

SVG won on both halves at once: fewer moving parts *and* a better result. Manim remains the right
tool for the thing SVG cannot do at all — animation — and that is a different artefact, not this
one.

The same test applied to the 55 figures that came back: seven failed strict XML parsing. The
complicated fix is to validate and retry until the model gets it right. The simple one is to notice
that `&Omega;` and a `<=` inside an `aria-label` render correctly in every browser already, and
that one deterministic text pass turns `<=` into `≤` and named entities into numeric ones. Fifty-five
of fifty-five, no retries, better typography. That is the shape of the right answer here.

## What a book is made from

Everything the course ships, merged rather than listed side by side:

| input | what it contributes |
| --- | --- |
| lecture slides | the skeleton — topics, order, the equations the lecturer chose to show |
| lecture transcript | what was actually *said* about each slide: the motivation, the asides, the worked reasoning a slide omits |
| readings and notes | the careful statement of results the lecture gestured at |
| problem sets | the exercises at the end of the chapter |
| solutions | the appendix each chapter's exercises link to |

**Slides plus transcript is the pairing that matters.** A slide deck alone is an outline — that is
exactly what made `6041sc/lectures/01-slides.md` useless, a page of bullets under a banner warning
that none of its equations could be trusted. The transcript alone is unreadable speech. Together
they are a lecture, and a lecture written down is a chapter.

**Course years are merged, not repeated.** Stat 243 ran twelve times and Stat 150 seven; that is one
book each, built from the most complete year and filled in from the others. Twelve near-identical
directories is the hoarding the book replaces.

## The structure, identical for every course

```
docs/<discipline>/<provider>/<course>/
    index.md                  the book: what the course is, contents, provenance
    01-<topic>.md             chapters, in the course's own order
    02-<topic>.md
    …
    solutions/01-<topic>.md   one per chapter that has exercises
```

**No `recordings/`, no `lectures/`, no `transcripts-pdf/`, no `slides/`.** Those are artefact kinds,
not parts of a book, and organising by artefact kind is what produced
`7091j/recordings/recordings/ud4-fowexay.md`.

**Structure is uniform even where material is missing.** A course with no problem sets simply has no
`Exercises` section in its chapters; it does not get a different layout. Missing content is fine,
an inconsistent skeleton is not.

## A chapter

```markdown
---
title: "7. Conditional Expectation"
course: MIT 6.041SC — Probabilistic Systems Analysis
chapter: 7
sources:
  - lectures/07-slides.pdf
  - recordings/07-captions.srt
licence: CC BY-NC-SA 4.0
attribution: John Tsitsiklis, MIT OpenCourseWare
written: '2026-09-15'
---

> **Lecture notes.** Written from the slides and recording of lecture 7 of
> [MIT 6.041SC](https://ocw.mit.edu/…) by John Tsitsiklis, licensed CC BY-NC-SA 4.0. These are
> notes, not a transcript: the material is reorganised and rewritten. This adaptation carries the
> same licence.

# 7. Conditional Expectation

## What this covers

Two or three sentences. What question the chapter answers and what it assumes you already have.

## <sections — the actual exposition>

Prose that teaches. Definitions stated properly, results with the argument that makes them
plausible, worked examples kept from the lecture. Mathematics in `$…$` and `$$…$$`.

## Exercises

Problems from the course's own problem sets, where they match this chapter.
Solutions: [chapter 7](solutions/07-conditional-expectation.md).

## Sources

Exactly which parts of the course this chapter came from — lecture number, slide range, problem set
and question. A reader who wants the original must be able to find the page it came from.
```

### Rules

- **One chapter per lecture** where the course has lectures; otherwise per chapter or section of the
  source document. Numbered in the course's own order, and the number is in the filename.
- **`## What this covers` and `## Sources` are mandatory.** They are the two sections that make a
  book navigable and honest respectively.
- **Exercises are the course's own**, never invented. A chapter with no matching problems has no
  `Exercises` section.
- **Solutions never sit beside their problem.** They are a linked page, because an answer one scroll
  below the question is not an exercise.
- **Everything `page-template.md` says about body text still applies** — one H1, `##`-rooted body,
  `$…$` maths, no raw HTML, figures as relative images. That file governs *markdown*; this one
  governs *structure and content*.
- **Never invent material.** If the lecture did not cover something, the chapter does not either. A
  gap is recorded in `## Sources` as a gap. The failure this guards against is a plausible-sounding
  book that no course actually taught.
- **Cite precisely enough to check.** Every claim traceable to a lecture and a slide, because the
  artefact layer is gone and the citation is now the only route back to the original.

## What is never in a book

- **A transcript.** Speech is an input, never output. `**[00:00]** The following content is provided
  under a Creative Commons license…` is boilerplate, not a chapter.
- **A slide dump.** Bullets copied out of a deck are not notes.
- **A page titled by a video id.** `Ud4 fowexay captions` was never a title.
- **His own material.** Trajectories, verdicts and what he derived himself live in the knowledge
  base. A book here is someone else's course, rewritten — not a record of his understanding.
