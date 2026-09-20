---
title: "11. Course Description"
course: "StatOmics Sga21"
chapter: 11
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Course Description

## What this covers

This chapter is the course description for Statistical Genomics Analysis (SGA), rather than a
lecture on a statistical method. It answers the orienting questions a student needs before the
technical chapters that follow: what the course is about, who it is for, what background it
assumes, and who teaches it. It assumes nothing beyond general interest in 'omics data analysis.

## Scope of the course

High-throughput 'omics studies generate ever larger datasets and, as a consequence, complex data
interpretation challenges. The course focuses on the statistical concepts involved in
preprocessing, quantification and differential analysis of high-throughput 'omics data. The core
material is built around two data types: shotgun proteomics, and (bulk and single-cell)
RNA-sequencing.

Experimental design is treated as essential to correct interpretation in any 'omics study. The
course covers how to design a statistically efficient experiment, and also how the choice of design
feeds back into how the data are modelled — introducing concepts such as blocking.

All of the course's practical work relies on free, open-source tools in R/Bioconductor. The stated
aim is to give beginners a solid basis while also giving those already familiar with standard
proteomics and next-generation-sequencing workflows a new perspective on them.

## Target audience

The course is oriented towards biologists and bioinformaticians with a particular interest in
differential analysis for quantitative 'omics data.

## Prerequisites

Two kinds of background are expected:

- **A basic statistics course**, covering data exploration and descriptive statistics, statistical
  modelling, and inference — specifically linear models, confidence intervals, t-tests, F-tests,
  ANOVA, and the chi-squared test. Students who need to revisit these basics are pointed to two
  online courses: an English-language course at
  [gtpb.github.io/PSLS20](https://gtpb.github.io/PSLS20/) and a Dutch-language one at
  [statomics.github.io/statistiekCursusNotas](https://statomics.github.io/statistiekCursusNotas/).
- **Programming in R**, which is preferred but taught from the basics if needed. Two primers are
  given: [R Basics](https://dodona.ugent.be/nl/courses/335/) and
  [R Data Exploration](https://dodona.ugent.be/nl/courses/345/), both hosted on Dodona.

## Lecturers

The course is taught by:

- [Koen Van den Berge](https://koenvandenberge.github.io/)
- [Lieven Clement](https://statomics.github.io/pages/about.html)

## Sources

- Course description page: `docs/omics-statistics/statomics/sga21/indexOldLinksMaterialsKoen/01-course-description.md`,
  converted from `indexOldLinksMaterialsKoen.Rmd` (statOmics/SGA21 repository, commit
  `0ad787d4cc2bb2f4636440840a8a923cf6c09839`), licensed CC BY-NC-SA 4.0.
- No slides, transcript or exercises were supplied for this chapter; the course description is the
  entirety of the source material. External links referenced by the course description (the PSLS20
  and statistiekCursusNotas prerequisite courses, and the Dodona R primers) are named but their
  content is not part of this chapter.

---

[← 10. Course Description and Program](10-course-description-and-program.md) · [Contents](index.md) · [12. Genomics: A Molecular Biology Primer →](12-genomics-a-molecular-biology-primer.md)
