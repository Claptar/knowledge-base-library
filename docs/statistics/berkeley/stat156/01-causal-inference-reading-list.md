---
title: "1. Causal Inference Reading List"
course: "Berkeley Stat 156 Fall 2024"
chapter: 1
source: "https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf"
licence: "CC BY-NC 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 156 Fall 2024](https://github.com/berkeley-stat156/fall-2024/blob/bbfe05b00bcc6fcbcf3140ad89cda2c5b36ed75e/HW3.pdf), licensed CC BY-NC 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Causal Inference Reading List

## What this covers

This chapter is not a lecture but a reading list: the schedule of research papers that the
graduate-credit track of the course ("256") reads and reports on across the semester, one paper
per week, alongside the rubric used to grade those reports. It assumes nothing beyond ordinary
familiarity with a course syllabus, and it does not explain the content of any paper on the list
— only the title, authors, venue and due date are supplied, and the papers themselves are the
actual reading.

## The assignment

Students on the 256 track read one research paper each week and submit a 2-3 page,
double-spaced report evaluating it, through Gradescope. Each report is graded on four things:

- correct identification of the research question the paper addresses
- an accurate summary of the method the paper uses
- a clear summary of the paper's key results
- a thoughtful overall evaluation — of the work's significance, novelty, and relevance

## The reading list

The papers are assigned in this order, one due date apart:

| Due date | Reading |
| --- | --- |
| 9/10/24 | Bickel et al. 1975, *Science* — Sex Bias in Graduate Admissions: Data from Berkeley |
| 9/17/24 | Holland 1986, *JASA* — Statistics and Causal Inference |
| 9/24/24 | Miratrix 2013, *JRSSB* — Adjusting treatment effect estimates by post-stratification in randomized experiments |
| 10/01/24 | Lin 2013, *AOAS* — Agnostic notes on regression adjustments to experimental data: reexamining Freedman's critique |
| 10/08/24 | Li, Ding and Rubin 2018, *PNAS* — Asymptotic theory of rerandomization in treatment-control experiments |
| 10/15/24 | Rosenbaum and Rubin 1983, *Biometrika* — The central role of the propensity score in observational studies for causal effects |
| 10/22/24 | Lunceford and Davidian 2004, *Statistics in Medicine* — Stratification and weighting via the propensity score in estimation of causal treatment effects: a comparative study |
| 10/29/24 | Angrist, Imbens and Rubin 1996, *JASA* — Identification of causal effects using instrumental variables |
| 11/5/24 | Imbens 2014, *Statistical Science* — Instrumental variables: an econometrician's perspective |
| 11/12/24 | Ding and VanderWeele 2016, *Epidemiology* — Sensitivity analysis without assumptions |
| 11/19/24 | Pearl 1995, *Biometrika* — Causal diagrams for empirical research |
| 11/26/24 | Frangakis and Rubin 2002, *Biometrics* — Principal stratification in causal inference |

## Reading the list as a syllabus

The titles alone lay out an arc through causal inference, and it is worth noticing the arc before
starting on any one paper, since it is why the papers sit in this order rather than another.

**An example, then a framework.** The list opens with an applied case — sex bias in Berkeley
graduate admissions — before moving to Holland's statement of statistics and causal inference as
a formal subject. The ordering puts the applied question that motivates the field ahead of the
framework used to answer it.

**Randomized experiments: how to adjust, and how to design.** Three consecutive papers concern
randomized experiments specifically: adjusting treatment-effect estimates by post-stratification
(Miratrix), regression adjustment to experimental data (Lin), and the design-stage question of
rerandomization (Li, Ding and Rubin). Read together, they cover both ends of a randomized trial —
how the treatment is assigned, and how the resulting data is analyzed.

**Observational studies: the propensity score.** The next pair turns to settings where treatment
is not randomized. Rosenbaum and Rubin's paper is the one that establishes the propensity score's
central role in observational studies; Lunceford and Davidian's is a comparative study of ways to
use it — stratification and weighting.

**Instrumental variables.** Angrist, Imbens and Rubin's paper on identifying causal effects with
instrumental variables is followed by Imbens's own later perspective on the same tool, from an
econometrician's point of view — the method, then a retrospective view of it.

**Beyond adjustment.** The list closes with three papers that each address a different way the
simple randomized/observational picture can break down: sensitivity analysis for when an
assumption (e.g., no unmeasured confounding) cannot be verified (Ding and VanderWeele), causal
diagrams as a formal language for encoding assumptions about a causal structure (Pearl), and
principal stratification for handling a post-treatment variable such as non-compliance
(Frangakis and Rubin).

## Sources

This chapter is drawn entirely from the reading-assignments page supplied as notes:
`statistics/berkeley/stat156/fall-2024/assignments.md` (converted from `assignments.qmd`,
CC BY-NC 4.0). No slides, transcript, or exercises were supplied for this entry. The page itself
supplies only the grading rubric and the list of papers with their titles, venues, authors and due
dates — it does not contain the papers' content, so this chapter maps the reading list rather than
explaining any paper on it. The papers themselves, linked from the source page, are the actual
reading.

---

[Contents](index.md) · [4. Confounding, Backdoor Paths, M-Bias →](04-confounding-backdoor-paths-m-bias.md)
