---
title: "40. Proteomics Software Setup"
course: "StatOmics Sga21"
chapter: 40
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 40. Proteomics Software Setup

## What this covers

This short chapter is not a lecture on statistics — it is the course's software setup page for the
Proteomics Data Analysis 2021 (PDA21) module, telling a participant what to install before the
sessions on quantitative proteomics data analysis can be followed hands-on. It assumes nothing
beyond having a computer to install software on; it does not introduce any statistical concept.

## R, RStudio, and the analysis package

The course's computational work is done in R, through RStudio, using a Bioconductor package built
for the course: **msqrob2**. Three things need to be in place before a session:

1. **R**, version 4.1 or higher, from CRAN.
2. **RStudio**, the desktop interface for R.
3. **msqrob2**, installed through Bioconductor's package manager rather than `install.packages`,
   since it is a Bioconductor package:

```r
if(!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager")
}
BiocManager::install("msqrob2")
```

`msqrob2` is the package that fits the models used later in the course to test for differential
protein and peptide abundance from mass-spectrometry-based proteomics data; installing it here is
what makes those later analyses runnable.

## Optional: a graphical interface

Participants who prefer a point-and-click interface over writing R code can additionally install
**msqrob2gui**, a Shiny app wrapped around `msqrob2`. It depends on the `remotes` package to pull
the app itself from GitHub rather than from Bioconductor's own repository:

```r
if(!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager")
}
if(!requireNamespace("remotes", quietly = TRUE)) {
  BiocManager::install("remotes")
}
BiocManager::install("statomics/msqrob2gui")
```

This is an alternative front end to the same package, not a separate analysis tool — anything done
through the GUI is msqrob2 underneath.

## Checking the installation

The course supplies a short worked check: load a built-in example dataset (`pe`), collapse its
peptide-level measurements into protein-level ones, fit an `msqrob2` model of protein abundance
against experimental condition, and print the fitted coefficient for the first protein.

```r
library(msqrob2)
data(pe)
pe <- aggregateFeatures(pe, i = "peptide", fcol = "Proteins", name = "protein")
pe <- msqrob(pe, i = "protein", formula = ~condition, modelColumnName = "rlm")
getCoef(rowData(pe[["protein"]])$rlm[[1]])
```

Running this end to end — feature aggregation, then model fitting, then coefficient extraction —
and getting output rather than an error is the intended sanity check that the local installation is
ready for the course.

## Avoiding installation altogether

For anyone who would rather not install R, RStudio and the packages locally, the course offers a
pre-built alternative: an RStudio interface running inside an R Docker container that already has
the Bioconductor proteomics packages installed, launched through a hosted Binder instance built
from one of the course's GitHub repositories. This trades local setup for a browser-based session
with the same environment already configured.

## Sources

- `docs/omics-statistics/statomics/sga21/software.md` — the course's "2. Software for Proteomics
  Data Analysis 2021 (PDA21)" page, converted from `software.Rmd` in the statOmics/SGA21 repository
  (commit `0ad787d`), licensed CC BY-NC-SA 4.0.
- No slides, transcript or exercises were supplied for this chapter; it covers only what that
  software-setup page contains.

---

[← 39. Variance-Stabilizing Transformation for Poisson Counts](39-variance-stabilizing-transformation-for-poisson-counts.md) · [Contents](index.md) · [41. Stage-wise Omnibus and Post-hoc Testing →](41-stage-wise-omnibus-and-post-hoc-testing.md)
