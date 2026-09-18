---
title: A Quick Guide to Conducting a Simulation Study
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/simulation_tutorial_miratrix.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/simulation_tutorial_miratrix.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# A Quick Guide to Conducting a Simulation Study

Luke Miratrix

2017-04-18 17:59:53

## Overview

The code in this document is a series of case studies of simple simulation studies where we examine such things
as the behavior of the simple difference-in-means for detecting treatment effect in a randomized experiment.

The primary purpose of this document is to illustrate how one might generate functions to conduct a
simulation given a specific set of parameters, and then build on such functions to explore a range of parameter
settings in what we would call multi-factor simulation experiments.

This script shows how you can streamline this using a few useful R functions in order to get nice and tidy
code with nice and tidy simulation results.

The first simulation study presented looks at the $t$-test under violations of the normality assumption. The
second is, essentially, a power analysis. Here we have a single estimator and we are evaluating how it works in
a variety of cicumstances. In the third simulation we compare different estimators via simulation by showing
a simulation comparing the mean, trimmed mean and median for estimating the center of a distribution.

This script relies on the **tidyverse** package, which needs to be loaded.

```r
library( tidyverse )
```

We use methods from the “tidyverse” for cleaner code and some nice shortcuts. (see the R for Data Science
textbook for more on this).

**Technical note**: This script was compiled from a simple .R file. If you are reading the raw file you will
notice some “#+” which indicate directives to R code blocks (chunks) in the knitr (R markdown) world.
This impacts how the code is run and displayed when turning the R file into a pdf to read. The comments
beginning with “#'” are interpreted as markdown when the document is complied in RStudio as a notebook
via knitr:spin() to make the pretty tutorial pdf.

## Simulation 1: the performance of the $t$-test

We will start with a simulation study to examine the coverage of the lowly one-sample $t$-test. *Coverage* is the
chance of a confidence interval capturing the true parameter value. Let’s first look at our test on some fake
data:

```r
# make fake data
dat = rnorm( 10, mean=3, sd=1 )

# conduct the test
tt = t.test( dat )
tt
```

```
##
## 	One Sample t-test
##
## data:  dat
## t = 10.134, df = 9, p-value = 3.202e-06
## alternative hypothesis: true mean is not equal to 0
##
```

---

[Up: contents](../index.md)
