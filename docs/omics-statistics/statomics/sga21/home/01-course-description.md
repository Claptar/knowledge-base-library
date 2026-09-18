---
title: Course Description
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/index.Rmd
source_file: sources/statomics-sga21/index.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`index.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/index.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Course Description

```r
knitr::include_graphics("./figures/wpGraph.jpeg")
```

High-throughput 'omics studies generate ever larger datasets and, as a consequence, complex data interpretation challenges. This course focusses on statistical concepts involved in preprocessing, quantification and differential analysis of high-throughput 'omics data. The core focus will be on shotgun proteomics and (bulk and single-cell) RNA-sequencing. Experimental design is essential to allow for correct interpretation in all 'omics studies, and we will cover how to design a statistically efficient experiment, as well as discuss the impact experimental design has on how we model 'omics data, introducing concepts such as blocking. The course will rely exclusively on free and user-friendly open-source tools in R/Bioconductor. We hope that this will provide a solid basis for beginners, but will also bring new perspectives to those already familiar with standard data analysis workflows for proteomics and next-generation sequencing applications.

## Target Audience

This course is oriented towards biologists and bioinformaticians with a particular interest in differential analysis for quantitative 'omics data.

## GitHub repository

All source and data files for this course are available on the accompanying [GitHub repository](https://github.com/statOmics/SGA21).

## Prerequisites

The prerequisites for the Statistical Genomics Analysis course are the successful completion of a basic course of statistics that covers topics on data exploration and descriptive statistics, statistical modeling, and inference: linear models, confidence intervals, t-tests, F-tests, anova, chi-squared test.
The basis concepts may be revisited in the online course at https://gtpb.github.io/PSLS20/ (English) and in https://statomics.github.io/statistiekCursusNotas/ (Dutch).

In addition, knowledge of programming in `R` is preferred. A primer to `R` and Data visualization in `R` can be found at:

 - `R` Basics: https://dodona.ugent.be/nl/courses/335/
 - `R` Data Exploration: https://dodona.ugent.be/nl/courses/345/

## Software

- Participants are required to bring their own laptop with [R](https://www.r-project.org/) version 4.1.1 or greater.

- We also recommend to also install the latest version of [RStudio](https://www.rstudio.com/products/rstudio/download/).

- Installation script: to install all required packages, please copy and paste this line of code in your R console.

```
source("https://raw.githubusercontent.com/statOmics/SGA21/master/install.R")
```

- Participants who have issues with the installation of the R/Rstudio can use an Rstudio instance in the cloud with all packages installed for the course in the mean time. Note, that this is instance is not for routine use.

[![Binder](http://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/statOmics/SGA21/binder?urlpath=rstudio)

---

[Up: contents](index.md) · [Detailed Program →](02-detailed-program.md)
