---
title: "9. Introduction to Causal Inference"
course: "Berkeley Stat 156 Fall 2024"
chapter: 9
source: "https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf"
licence: "CC BY-NC 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 156 Fall 2024](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf), licensed CC BY-NC 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Introduction to Causal Inference

## What this covers

This chapter is the course's own statement of what it is about and how it is built, not a lecture
on causal inference itself: it lays out the subject matter, the format, the prerequisites, and the
sequence of topics that the rest of the book follows. It assumes only the background the course
itself assumes — an introductory mathematical statistics course, and enough comfort with R to work
with data.

## The subject

The course is an introduction to **causal inference**, built on two related tools: the **potential
outcomes framework** and **causal diagrams**. Within that framework it covers randomized
experiments, observational studies, instrumental variables, and mediation analysis, with
applications drawn from medicine and public policy.

## Format

The course splits into two parts that are meant to reinforce each other: lectures present the
concepts and methods, and lab sections work through applications, derivations, and problems, most
often using R. So the theory (what a causal effect is, when it is identifiable) and the practice
(estimating it from data) are taught side by side rather than one after the other.

## Prerequisites

The course assumes Stat 135 (an equivalent course, or CS 189, can substitute with the instructor's
permission), and recommends Stat 151A. It also assumes working knowledge of R and LaTeX, since both
the homework and the write-ups use them.

## Texts

Readings are drawn mainly from two books:

- Ding, P. (2024), *A First Course in Causal Inference* (CRC Press) — an older version is free on
  arXiv.
- Robins, J., and Hernán, M. A. (2020), *Causal Inference: What If* (CRC Press) — free online.

## Roadmap for the semester

The course outline lays out the order in which the ideas are meant to build, week by week:

1. Association and paradoxes (week 1)
2. Potential outcomes framework (week 2)
3. Randomized experiments (weeks 2–3)
4. Unconfounded observational studies (weeks 4–6)
5. Instrumental variables (weeks 7–8)
6. Sensitivity analysis (week 9)
7. Negative controls (week 10)
8. Principal stratification and mediation (week 11)
9. Modern methods (week 12)

The shape of this sequence is itself an argument: it starts from the paradoxes that make plain
association misleading, introduces the potential-outcomes language needed to state a causal
question precisely, and only then asks how to answer that question — first when treatment is
randomized, then when it is not (unconfounded observational studies), then when even that fails and
an instrument, a sensitivity analysis, or a negative control is needed instead. Principal
stratification, mediation, and "modern methods" close the course as harder variants and extensions
of the same identification problem.

## Sources

This chapter reproduces the scope, format, prerequisites, texts, and course outline from the
Stat 156 (Fall 2024, UC Berkeley, Causal Inference, instructor Amanda Coston) syllabus:
`stat156-syllabus/01-introduction.md` (course description, format, prerequisites, textbooks) and
`stat156-syllabus/02-evaluation.md` (the Course Outline section). Administrative material in those
two files — grading weights and dates, office hours, contact details, academic-integrity and
wellness policy, and the no-laptop rule — is not lecture content and has been left out here.

---

[← 8. The Final Project](08-the-final-project.md) · [Contents](index.md) · [10. Causal Inference: Course Structure →](10-causal-inference-course-structure.md)
