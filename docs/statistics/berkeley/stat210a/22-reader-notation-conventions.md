---
title: "22. Reader Notation Conventions"
course: "Berkeley Stat 210A Fall 2024"
chapter: 22
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 22. Reader Notation Conventions

## What this covers

This chapter is not a lecture but the notation key behind one: the LaTeX macro file that the
STAT 210A reader loads at the start of every set of notes, so that the same shorthand renders the
same way from one chapter to the next. Collecting it here means the rest of the reader can be read
without re-deriving what a symbol means the first time it appears. It assumes only familiarity with
basic set notation and the definition of a probability space.

## Sets, spaces, and number systems

The reader uses calligraphic letters as generic names for sets, sigma-algebras, and spaces that get
fixed once at the start of a chapter and then used silently:

- $\mathcal{B}$, $\mathcal{F}$ — a sigma-algebra (e.g. of Borel sets, or of a filtration).
- $\mathcal{N}$ — a family or class named in a given chapter.
- $\mathcal{P}$ — a class of probability measures on the underlying space. This is the notation a
  theoretical-statistics course needs constantly: a statistical model is a family $\mathcal{P}$ of
  candidate distributions, not a single one, and a claim is often only true for every $P$ in that
  family rather than for one fixed $P$.
- $\mathcal{X}$ — a sample space, the set an observation takes its values in.

Blackboard bold is reserved for the two standard number systems:

- $\mathbb{R}$ — the real numbers.
- $\mathbb{Z}$ — the integers.

## Expectation and probability

$\mathbb{E}$ and $\mathbb{P}$ are the expectation and probability operators, also in blackboard
bold, so that they read visually as "the same kind of object" as $\mathbb{R}$ and $\mathbb{Z}$
rather than as ordinary italic letters that could be confused with a variable named $E$ or $P$.

## Notions of equality

Ordinary equality is not enough once probability is in the picture, so the reader distinguishes
several weaker senses of "equal," each written as an equals sign with the qualifier stacked above
it:

- $\stackrel{\text{a.s.}}{=}$ — equal almost surely: equal outside a set of probability zero, under
  whatever probability measure is fixed by context.
- $\stackrel{\mathcal{P}\text{-a.s.}}{=}$ — equal $\mathcal{P}$-almost surely: equal almost surely
  under *every* $P$ in the model class $\mathcal{P}$, not just one of them. This is the notion that
  matters when a statement is meant to hold uniformly over an entire statistical model.
- $\stackrel{\mu\text{-a.s.}}{=}$ — equal almost everywhere with respect to a fixed measure $\mu$
  that need not be a probability measure.
- $\stackrel{D}{=}$ — equal in distribution: the two sides need not be equal as random variables at
  all, only have the same law.

## Independence and identical distribution

- $\perp\!\!\!\!\perp$ — independence, written as two crossed vertical bars rather than spelled
  out, since it appears inside displayed equations often enough to need its own symbol.
- $\stackrel{\text{i.i.d.}}{\sim}$ — distributed independently and identically as (used for a
  sequence of random variables sharing one law).
- $\stackrel{\text{ind.}}{\sim}$ — distributed independently as, without the identical part: each
  variable in the sequence may have its own law, but they remain independent.

## Calculus and optimization shorthand

- `\td`, rendered $\,\mathrm{d}$, inserts the small space conventionally placed before a
  differential, as in $\int f(x) \td x$, so integrals are typeset consistently across the reader
  without retyping the spacing command each time.
- `\argmin` and `\argmax` typeset $\operatorname*{argmin}$ and $\operatorname*{argmax}$ as proper
  math operators (upright, with subscripts stacking underneath rather than to the side), the way
  $\sup$ or $\lim$ behave, rather than as three italic letters.
- `\minz` and `\maxz` do the same for the "minimize" and "maximize" headings of an optimization
  display, e.g.
$$\operatorname*{minimize}_{x} \ f(x) \quad \text{subject to} \quad g(x) \le 0.$$

## Moments

- $\mathrm{Var}$, $\mathrm{Cov}$, $\mathrm{Corr}$ — variance, covariance, and correlation, set in
  upright (non-italic) type as is conventional for a named operator rather than a product of
  variables.

## Two versions of the macro file

The reader has been revised between offerings of the course. The fall-2026 version of the macro
file differs from the fall-2024 version in two small ways: it fixes a copy-paste slip in which
`\maxz` had been declared to print "minimize" (the same text as `\minz`) instead of "maximize," and
it adds one further macro, `\ep`, as shorthand for $\varepsilon$. Both versions otherwise define
the same set of symbols listed above.

## Sources

- `statistics/berkeley/stat210a/fall-2024/reader/latex-macros.md`, converted from
  `reader/latex-macros.tex` in the `berkeley-stat210a/fall-2024` repository (commit
  `812543bde50398a54db3044bf8ba7120189a4dfa`), CC BY 4.0.
- `statistics/berkeley/stat210a/fall-2026/reader/latex-macros.md`, converted from
  `reader/latex-macros.tex` in the `berkeley-stat210a/fall-2026` repository (commit
  `7dc8f80da94dff74532d9e3923afdb16a255262d`), CC BY 4.0 — the clearer of the two (fixes the
  `\maxz` typo and adds `\ep`), used as the primary source for the symbol list above.

No slides, transcript, or exercises were supplied for this item; the source is the macro file
itself, not a recorded lecture, so this chapter documents the notation rather than a topic.

---

[← 21. The James-Stein Estimator](21-the-james-stein-estimator.md) · [Contents](index.md) · [23. Measures, Integration, and Densities →](23-measures-integration-and-densities.md)
