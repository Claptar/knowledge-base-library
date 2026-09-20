---
title: "10. Course Description and Program"
course: "StatOmics Sga21"
chapter: 10
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Course Description and Program

## What this covers

This chapter is the course's own front matter: what the Statistical Genomics Analysis (SGA)
course is about, who it is for, and how its sessions are organised into modules. It assumes
nothing about proteomics or RNA-sequencing — that material starts in the modules described below
— but does assume the general statistics and R background listed under Prerequisites.

## Scope

High-throughput 'omics studies generate large, complex datasets, and this course is built around
the statistical concepts needed to interpret them correctly: preprocessing, quantification, and
differential analysis. Two technologies carry the material throughout — shotgun proteomics, and
(bulk and single-cell) RNA-sequencing. Experimental design runs through both: the course covers
how to design a statistically efficient experiment, and how the design shapes the model used on
the resulting data, introducing concepts such as blocking as a consequence of design rather than
an afterthought. All computation uses free, open-source tools in R/Bioconductor.

The source page opens with a workflow diagram (`wpGraph.jpeg`) situating the course among
preprocessing, quantification and differential analysis; the image itself is not part of the
converted material, so it is not reproduced here.

## Audience and prerequisites

The course targets biologists and bioinformaticians with a particular interest in differential
analysis of quantitative 'omics data.

It assumes a basic statistics course covering data exploration and descriptive statistics, and
statistical modelling and inference: linear models, confidence intervals, t-tests, F-tests, ANOVA,
and the chi-squared test. Two online refreshers are pointed to for this material: an
English-language course at `gtpb.github.io/PSLS20` and a Dutch-language one at
`statomics.github.io/statistiekCursusNotas`.

It also expects some programming ability in R. A primer and a data-visualisation course, both
hosted on Ghent University's Dodona platform, are given as a starting point for students who need
to pick this up (`R` Basics and `R` Data Exploration).

## Software

Everything runs in R, version 4.1.1 or later, with RStudio recommended. The course repository
supplies a single installation script that pulls in every package used later in the course:

```
source("https://raw.githubusercontent.com/statOmics/SGA21/master/install.R")
```

Anyone who cannot get a local installation working can fall back to a cloud RStudio instance with
the packages pre-installed — offered for the duration of the course, not for routine use.

## Structure of the course

The programme runs in a recap plus three modules, moving from a shared statistical toolbox
(linear models) into two 'omics technologies that both quantify abundance from high-throughput
measurements, then into a technology — single-cell RNA-seq — where the unit of measurement
changes from a bulk sample to a single cell.

### Recap: linear models (week 1)

A lecture recapping the general linear model, paired with a tutorial that applies multiple
regression to the KPNA2 dataset. This is the statistical base the rest of the course builds on.

### Module I: proteomics data analysis (weeks 1-5)

- **Bioinformatics for proteomics** — an introductory lecture (with an accompanying video) and
  tutorials on peptide/protein identification.
- **Preprocessing and analysis of simple designs (week 3)** — a lecture on preprocessing
  quantification data, a matching tutorial, and a wrap-up on peptide-based models for robust
  summarisation.
- **Statistical inference and analysis of factorial designs (weeks 3-4)** — a lecture on
  differential abundance analysis, a tutorial on experimental design, and a wrap-up on blocking.
- **Advanced and reading material** — technical details on inference after summarisation,
  stage-wise testing, and three papers: Sticker et al. (2020) on robust summarisation and
  inference in label-free quantification, Ludger Goeminne's PhD-introduction background chapter on
  proteomics data analysis, and Van den Berge et al. (2017), the stageR stage-wise testing paper.
- **Worked solutions** — the CPTAC study, a 6x6 cancer design, a mouse study, and a heart study,
  each solved in an accompanying wrap-up or dedicated page.

### Module II: bulk RNA-sequencing

- **Introduction to sequencing technology, raw data and preprocessing**, with a shell-script
  tutorial for preprocessing raw RNA-seq data and a recommended review ("RNA Sequencing Data: A
  Hitchhiker's Guide to Expression Analysis").
- **Working with count data and generalized linear models**, including a tutorial that analyses
  bike-sharing count data as a warm-up before fitting a GLM to a single gene.
- **Analysis of RNA-seq data**: the four major challenges in analysing RNA-seq datasets, plus a
  page arguing for using offsets rather than scaling the counts directly.
- **Technical topics in bulk RNA-seq differential expression analysis.**

### Module III: single-cell RNA-sequencing

General concepts and the analysis workflow for single-cell RNA-seq data, covering the
variance-stabilising transformation for a Poisson random variable, an external explainer on UMAP,
and a simulation study of post-selection inference — the problem of testing on the same data used
to select which genes or clusters to test. These are tied together in a reproducible workflow on
the Macosko Drop-seq dataset.

## Instructors and license

The course is taught by Koen Van den Berge, Lieven Clement, and Lennart Martens.

The course material is licensed CC BY-NC-SA 4.0 (Creative Commons
Attribution-NonCommercial-ShareAlike): reuse must give attribution, may not be commercial, and any
derivative must carry the same licence.

## Sources

- Course description: `docs/omics-statistics/statomics/sga21/home/01-course-description.md`,
  converted from `index.Rmd` in the statOmics/SGA21 GitHub repository (commit `0ad787d`).
- Detailed program: `docs/omics-statistics/statomics/sga21/home/02-detailed-program.md`, converted
  from the same `index.Rmd`.
- Named but not contained in these two pages, and not covered by this chapter: the individual
  lecture slide decks, tutorials, and shell scripts linked from the detailed program, the three
  papers cited (Sticker et al. 2020; Van den Berge et al. 2017; Goeminne's background chapter), and
  the `wpGraph.jpeg` workflow diagram referenced but not embedded in the converted page.

---

[← 9. Illumina Next-Generation Sequencing Overview](09-illumina-next-generation-sequencing-overview.md) · [Contents](index.md) · [11. Course Description →](11-course-description.md)
