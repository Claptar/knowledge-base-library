---
title: "7. First Three Weeks Logistics"
course: "Berkeley Stat 243"
chapter: 7
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. First Three Weeks Logistics

## What this covers

This chapter documents the administrative structure of the first three weeks of Stat 243
(Berkeley, Fall 2021): what students were required to do and by when, what was optional, and
which tools the course expected them to pick up before the technical material started. It is not
a lecture on a technical topic — the source is the course's own to-do list and events calendar —
so it is presented here as a schedule and toolkit checklist rather than as a sequence of results.
It assumes only that the reader is following the course from its start; no programming or
statistics background is assumed beyond what is listed below.

## Week 1: getting set up

Before any technical content, the course opened with logistics:

- **Two required surveys**, due Friday August 27 at noon: a class survey, and a survey of
  possible office-hour times.
- **One optional survey**, same deadline, for anyone wanting an extra R help session — used only
  to schedule it.
- **Required reading**: Sections 1–3 of Unit 2, on getting CSV and similar data into and out of R
  and the pitfalls that arise, due by Monday August 30. Class time would only touch on a point or
  two from these sections, on the assumption the reading had been done.
- **Optional UNIX catch-up**: anyone not comfortable with the basic UNIX usage shown in the first
  class was pointed to a UNIX basics tutorial (with self-check questions, nothing to submit) and
  to a Friday UNIX help session, ahead of the following Wednesday's class.

The pattern set here — required items with hard deadlines, optional catch-up material for anyone
behind, and a help session timed just before the material is needed in class — repeats through
weeks 2 and 3.

## Weeks 2–3: shell, regular expressions, and version control

- **Optional R catch-up**: for anyone not yet at the level of modules 1–5 of the R bootcamp,
  working through those modules (and their breakout problems) by the end of the week of
  September 6, with a catch-up session offered for extra practice.
- **Required bash tutorial**, due Friday September 3 at 10am: work through a tutorial on using the
  bash shell and submit answers to its first 10 problems via bCourses, as plain text — no
  formatting or explanation required, and hand-written scanned answers were explicitly acceptable.
  Not every section of the tutorial was assigned; a list of sections to skip was given separately
  (Section 2 of the course's `unit4-bash.pdf`). A live demonstration of the bash shell in class on
  Wednesday September 1 was meant to support this.
- **Problem Set 1**, due Wednesday September 8 at 10am — the course's first graded problem set.
- **Required regular-expression reading and practice**, due Friday September 10 at 10am: the
  regex material in Section 3 of the bash tutorial (Section 3.6 excluded), plus Section 2.1 of a
  string-processing tutorial (with the `stringr` material in 2.1.2 as an optional focus), followed
  by a set of regex practice problems submitted through a Google form. This was graded only as
  complete or not — not one of the numbered problem sets.

## Events in the first three weeks

Alongside the to-do items, several sessions were scheduled, mixing optional support with required
sections:

- **Optional LaTeX sessions** (library-run), Thursday August 26 or Wednesday September 8, 4–5:30pm
  — recommended in particular for statistics graduate students, on the grounds that being able to
  typeset equations in LaTeX is worth having early.
- **Optional software/UNIX help session**, Friday August 27, noon–3:30pm, for installing software,
  getting a UNIX-style command line working, and basic UNIX usage — aimed at having everyone set
  up before the Wednesday September 1 class.
- **Optional R help session**, date/time to be determined by the survey above, for anyone below
  the R bootcamp modules 1–5 level.
- **Required section/lab, Friday September 3**: Git, setting up a GitHub repository for problem
  sets, and using RMarkdown/knitr to produce dynamic documents. Students attended only their
  registered section, given room capacity.
- **Required section/lab, Friday September 10**: assertions and testing. Same attendance rule.

Read together, the two lists show what the course treats as prerequisite machinery before any
statistical computing proper begins: a working UNIX-style shell, enough R to be productive, basic
regular expressions and string processing, and a Git/GitHub workflow for submitting problem sets
via reproducible documents (RMarkdown/knitr). The technical content of the course builds on top of
this toolkit rather than introducing it later.

## Sources

- `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/first_three_weeks/01-assignments-to-dos.md`
  — "Assignments / to-dos", Week 1 and Weeks 2–3 sections.
- `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/first_three_weeks/02-events.md`
  — "Events" list for the same period.
- Both converted losslessly (CC0-1.0) from `first_three_weeks.md` in the
  [berkeley-stat243/stat243-fall-2021](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/first_three_weeks.md)
  course repository.
- Referenced but not contained in these files, and not reproduced here: the class survey and
  office-hours survey (Google Forms), the UNIX basics tutorial, the R bootcamp (modules 1–5), the
  bash shell tutorial and its first 10 end-of-tutorial problems, `unit4-bash.pdf` (Section 2, for
  which sections to skip), the string-processing tutorial (Section 2.1), the regex practice-problem
  form, and the bCourses assignment submission page. Unit 2, Sections 1–3, on reading and writing
  CSV-type data in R, is likewise referenced but not included.

---

[← 6. Debugging in R](06-debugging-in-r.md) · [Contents](index.md) · [8. Reading: Infovis and Statistical Graphics →](08-reading-infovis-and-statistical-graphics.md)
