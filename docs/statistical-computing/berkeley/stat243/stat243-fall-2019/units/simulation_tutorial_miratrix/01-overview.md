---
title: Overview
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Overview

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The code in this document is a series of case studies of simple simulation studies where we examine such things as the behavior of the simple difference-in-means for detecting treatment effect in a randomized experiment.

The primary purpose of this document is to illustrate how one might generate functions to conduct a simulation given a specific set of parameters, and then build on such functions to explore a range of parameter settings in what we would call multi-factor simulation experiments.

This script shows how you can streamline this using a few useful R functions in order to get nice and tidy code with nice and tidy simulation results.

The first simulation study presented looks at the _t_ -test under violations of the normality assumption. The second is, essentially, a power analysis. Here we have a single estimator and we are evaluating how it works in a variety of cicumstances. In the third simulation we compare different estimators via simulation by showing a simulation comparing the mean, trimmed mean and median for estimating the center of a distribution.

This script relies on the `tidyverse` package, which needs to be loaded.

```
library(tidyverse)
```

We use methods from the “tidyverse” for cleaner code and some nice shortcuts. (see the R for Data Science textbook for more on this).

**Technical note** : This script was compiled from a simple `.R` file. If you are reading the raw file you will notice some “ `#+` ” which indicate directives to R code blocks (chunks) in the knitr (R markdown) world. This impacts how the code is run and displayed when turning the R file into a pdf to read. The comments beginning with “ `#'` ” are interpreted as markdown when the document is complied in RStudio as a notebook via `knitr:spin()` to make the pretty tutorial pdf.

---

[Up: contents](index.md) · [Simulation 1: the performance of the t -test →](02-simulation-1-the-performance-of-the-t--test.md)
