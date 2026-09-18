---
title: "10. Causal Inference: Course Structure"
course: "Berkeley Stat 156 Fall 2024"
chapter: 10
source: "https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf"
licence: "CC BY-NC 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 156 Fall 2024](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf), licensed CC BY-NC 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Causal Inference: Course Structure

## What this covers

This is the syllabus for Stat 256, *Causal Inference*, taught by Amanda Coston at UC Berkeley in
Fall 2024. It answers a narrower question than a lecture would: not "what is a causal effect" but
"what will this course make you read, do, and be graded on, and in what order." It assumes nothing
about causal inference itself — only what the syllabus states as prerequisite. Read it once before
the first substantive lecture, since the week-by-week outline below is the map the rest of the
course's chapters will fill in.

## What the course sets out to teach

The course is built around two representations of a causal question: the **potential outcomes
framework** and **causal diagrams**. Within that frame it covers randomized experiments,
observational studies, instrumental variables, and mediation analysis, with applications drawn
from medicine and public policy. The course is explicitly split between theory, delivered in
lecture, and application — derivations and worked problems, mostly in R — delivered in the GSI's
lab sections.

## Background the course assumes

- Stat 201 or Stat 210A is "highly recommended."
- Linear models and generalized linear models.
- Working fluency in R and LaTeX — LaTeX because scribed lecture notes (below) are typeset in it,
  R because the lab sections work in it.

Readings are drawn primarily from two textbooks:

- Ding, P. (2024). *A First Course in Causal Inference*. CRC Press — also available on arXiv in a
  slightly older version.
- Hernán, M. A., & Robins, J. (2020). *Causal Inference: What If*. CRC Press — available free
  online.

## The topics, week by week

The syllabus lays out nine topics across a twelve-week term:

| Week(s) | Topic |
|---|---|
| 1 | Association and paradoxes |
| 2 | Potential outcomes framework |
| 2–3 | Randomized experiments |
| 4–6 | Unconfounded observational studies |
| 7–8 | Instrumental variables |
| 9 | Sensitivity analysis |
| 10 | Negative controls |
| 11 | Principal stratification and mediation |
| 12 | Modern methods |

The shape of this list is worth noticing on its own: the course moves from the setting where
causal identification is easiest (a randomized experiment) to progressively weaker assumptions
that still let you identify an effect — unconfoundedness, then an instrument, then only a
sensitivity bound, then no unconfoundedness at all (negative controls) — before turning to effects
that are not simply "treatment versus control" (principal stratification, mediation).

## The reading list, mapped onto the topics

Each week of lecture is paired with one paper, assigned as a reading with a short written report
due on it. The pairing below is exactly the one the syllabus gives — paper and week together, in
order:

| Week | Reading |
|---|---|
| 1 | Bickel, Hammel & O'Connell (1975), *Science* — "Sex Bias in Graduate Admissions: Data from Berkeley" |
| 2 | Holland (1986), *JASA* — "Statistics and Causal Inference" |
| 3 | Miratrix (2013), *JRSSB* — "Adjusting treatment effect estimates by post-stratification in randomized experiments" |
| 4 | Lin (2013), *AOAS* — "Agnostic notes on regression adjustments to experimental data: Reexamining Freedman's critique" |
| 5 | Li, Ding & Rubin (2018), *PNAS* — "Asymptotic theory of rerandomization in treatment-control experiments" |
| 6 | Rosenbaum & Rubin (1983), *Biometrika* — "The central role of the propensity score in observational studies for causal effects" |
| 7 | Lunceford & Davidian (2004), *Statistics in Medicine* — "Stratification and weighting via the propensity score in estimation of causal treatment effects: a comparative study" |
| 8 | Angrist, Imbens & Rubin (1996), *JASA* — "Identification of causal effects using instrumental variables" |
| 9 | Imbens (2014), *Statistical Science* — "Instrumental Variables: An Econometrician's Perspective" |
| 10 | Ding & VanderWeele (2016), *Epidemiology* — "Sensitivity Analysis Without Assumptions" |
| 11 | Pearl (1995), *Biometrika* — "Causal diagrams for empirical research" |
| 12 | Frangakis & Rubin (2002), *Biometrics* — "Principal stratification in causal inference" |

So the reading list doubles as a second syllabus, in the field's own primary sources rather than
in textbook form: week 1's topic, "association and paradoxes," is read alongside the Berkeley
admissions data paper; week 2's "potential outcomes framework" alongside Holland's paper of that
name; and so on down the table, each week's method paired with the paper that introduced or
analyzed it.

## How the work in the course is structured

Beyond exams, the course is organized around four kinds of work, each assessed:

- **Weekly reading reports** on the papers above — a short (2–3 page) written report each week
  describing the paper and evaluating the work.
- **Two recorded presentations of published papers**, chosen by the student rather than assigned:
  each must relate to causal inference, be published after 2012, and at least one must be a
  journal paper (as opposed to a conference paper). A 20-minute recorded presentation is required
  for each.
- **Scribing**: each student signs up to scribe one lecture's notes, in LaTeX, in a shared
  Overleaf document, released within a few days of the lecture.
- **A group project**, done in groups of three, with a research presentation given in the last
  weeks of the semester and a final written report (15–20 pages).

The mix is deliberate: reading reports and paper presentations put the *literature* of causal
inference in front of the student every week, not just the textbook account of it, and the scribed
notes and group project put the student on the producing side of that literature rather than only
the consuming side.

## Exercises

None supplied. This chapter is the course's syllabus, not a problem set — the weekly deliverable
in this course is the reading report described above, on a paper assigned by the table, rather
than a worked exercise.

## Sources

- **Course description, prerequisites, textbooks** — `01-introduction.md` (from
  `stat256-syllabus.pdf`, berkeley-stat156, Fall 2024).
- **Course outline (topics by week) and the assessment structure** — `02-evaluation.md`, same
  source. Administrative detail present in that file but not reproduced here — office hours,
  contact emails, wellness resources, academic-integrity policy, the laptop policy, exact
  percentage weights and due dates — is exactly the kind of boilerplate these notes strip; consult
  the syllabus itself for it.
- **The reading list** — `03-reading-assignments.md`, same source.
- All three files are machine reconstructions of a PDF syllabus with no extractable text layer (see
  each file's header: `route: llm`, `fidelity: reconstructed`); treat exact wording, and any detail
  not cross-checked here, as approximate rather than a verbatim quotation of the syllabus.
- Referred to but not contained in the supplied material: the syllabus PDF itself, the course
  website (`stat156.berkeley.edu/fall-2024`), the two textbooks (Ding 2024; Hernán & Robins 2020),
  and every paper on the reading list above — none of their contents are given here, only their
  citations and the week each is assigned.

---

[← 9. Introduction to Causal Inference](09-introduction-to-causal-inference.md) · [Contents](index.md) · [11. Course Overview: Causal Inference →](11-course-overview-causal-inference.md)
