---
title: Data Import with the readr R package
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Import with the readr R package

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_NHANES.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
library(readr)
```

Let's try reading in some data. We will begin by
reading in the `NHANES.csv` dataset.

```r
NHANES <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/NHANES.csv")
```

```r
head(NHANES) ## take a look at the first rows of the dataset
```

```r
tail(NHANES) ## take a look at the last rows of the dataset
```

```r
#knitr::kable(NHANES[c(1,4,5,6,7,8),c(1,3,4,7,17,20,21,25)],format = "markdown")
NHANES[c(1,4,5,6,7,8),c(1,3,4,7,17,20,21,25)] ## take a look at a subset of the dataset
```

## Take a `glimpse()` at your data

The glimpse function allows us to (obviously) take
a first, informative glimpse at our data. The function
is part of the `dplyr`, which we will explore in much
more detail below!

```r
dplyr::glimpse(NHANES[,1:10])

---

[← The NHANES dataset](01-the-nhanes-dataset.md) · [Up: contents](index.md) · [or glimpse(NHANES) to see all the variables in the dataset →](03-or-glimpse-nhanes-to-see-all-the-variables-in-the-dataset.md)
