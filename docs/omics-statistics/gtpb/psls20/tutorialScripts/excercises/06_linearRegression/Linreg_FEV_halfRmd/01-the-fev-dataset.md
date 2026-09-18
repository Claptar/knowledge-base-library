---
title: The FEV dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The FEV dataset

As an exercise on linear regression, we will analyse the FEV dataset.

The FEV, which is an acronym for forced expiratory volume,
is a measure of how much air a person can exhale (in litres)
during  a forced breath. In this dataset, the FEV of 606 children,
between the ages of 6 and 17, were measured. The dataset
also provides additional information on these children:
their `age`, their `height`, their `gender` and, most
importantly, whether the child is a smoker or a non-smoker.

The overarching goal of this experiment was to find out whether or not
smoking has an effect on the FEV of children.

## Load the required libraries

```r
library(tidyverse)
```

## Import the data

```r
fev <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/fev.txt")
head(fev)
```

## Tidy the data

There are a few things in the formatting of the
data that can be improved upon:

1. Both the `gender` and `smoking` can be transformed to
factors.
2. The `height` variable is written in inches. Assuming that
this audience is mainly Portuguese/Belgian, inches are hard to
interpret. Let's add a new column, `height_cm`, with the values
converted to centimeters using the `mutate` function.

```r
```

## Data Exploration

Explore the data. Visualise the FEV for smokers versus non-smokers:

```r
```

Did you expect these results? Can you explain what we observe (and why)?
Additionally, can you provide an even better visualisation of the data, taking
into account more useful explanatory variables with respect
to the FEV?

```r
```

---

[Up: contents](index.md) · [Analysis →](02-analysis.md)
