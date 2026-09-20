---
title: "17. Standing Homework Conventions"
course: "Berkeley Stat 210A Fall 2024"
chapter: 17
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Standing Homework Conventions

## What this covers

The homework page in this course is not a lecture; it is the standing instructions that every
problem set is written against, restated nowhere else. The exercises in the chapters that follow
assume the reader already knows these conventions, so they are collected here once: what
measure-theoretic care can be skipped, what a submitted solution must look like, what counts as a
legitimate numerical method and how precise its output must be, and what "asymptotic" and
"limiting distribution" mean whenever a problem uses those words without further qualification.

## Measure-theoretic niceties

Problems may be answered without worrying about the measure-theoretic fine print: conditioning on
events of probability zero, the distinction between almost-sure equality and actual equality, and
"all functions" versus "all measurable functions" may all be treated informally — unless a problem
explicitly asks about one of these issues, in which case it must be addressed.

## Submission, code, and plots

Any code used to answer a question must be shown, and any plot must be readable: axis labels and,
where relevant, a legend are expected. Very hard-to-read code or plots lose points.

In fall 2026 this is spelled out further: homework is submitted electronically on Gradescope,
need not be typeset in LaTeX, and may be handwritten unless the problem requires code or figures,
so long as the writing is legible — illegible solutions lose points. Code may be written in any
common language (R, Python, Matlab are named explicitly); anything more exotic should be cleared
with the GSI first.

## Monte Carlo as a numerical method

Whenever a problem asks for something to be calculated numerically, Monte Carlo integration —
estimating an expectation by repeatedly sampling from an appropriate distribution and averaging —
is automatically an admissible method; no permission is needed to use it. What is expected instead
is judgment about how many samples to draw, calibrated to three different standards of precision:

- a single reported **number** should be correct to a few significant digits;
- a **comparison of two numbers** needs enough precision that the difference between them is
  actually meaningful, not swamped by Monte Carlo noise;
- a **plot of a smooth function** should look smooth — visible sampling jitter means too few draws.

## Asymptotics and limiting distributions

Unless a problem says otherwise, every asymptotic statement is a statement as $n \to \infty$.

A request for "the limiting distribution" of some quantity $X_n$ means more than showing that
$X_n$ converges in probability to a constant — that limit is degenerate and not what is wanted.
It means finding a centering sequence $a_n$ and a scaling sequence $b_n$ such that

$$b_n(X_n - a_n)$$

converges to a non-degenerate limiting distribution. Producing $a_n$ and $b_n$ is part of the
answer, not a detail to be assumed.

## Sources

- `homework.md`, fall 2024 and fall 2025 (identical standing text, the latter under a "Standing
  homework instructions" heading): measure-theoretic niceties, code and plots, Monte Carlo
  precision, and the asymptotic/limiting-distribution conventions.
- `homework.md`, fall 2026, "Standing homework instructions": repeats the same three conventions
  under "Other conventions" and "Monte Carlo methods", and adds the "Submission format"
  subsection (Gradescope, handwriting permitted, choice of programming language, checking exotic
  languages with the GSI) that is absent from the 2024 and 2025 pages.
- The assignments themselves (Homework 1 through 10 or 11, depending on the year) are omitted
  here as instructed; each is a chapter in its own right.

---

[← 16. Hierarchical Bayes](16-hierarchical-bayes.md) · [Contents](index.md) · [18. Hypothesis Testing and Neyman-Pearson →](18-hypothesis-testing-and-neyman-pearson.md)
