---
title: Fish tank dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Fish tank dataset

As an exercise on multiple regression, we will analyse
the fish tank dataset.

In this experiments 96 fish (dojofish, goldfish and zebrafish)
were placed separately in a tank with two liters of water and
a certain dose (in mg) of a certain poison EI-43,064. The resistance
of the fish a against the poison was measured as the amount of
minutes the fish survived upon adding the poison (Surv_time, in
minutes). Additionally, the weightt of each fish was measured.

## Goal

In this tutorial, we will study the association between dose and
survival time, while correcting for weight and species, by using
a multiple regression model.

Read the required libraries

```r
library(tidyverse)
```

## Import the data

```r
poison <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/poison.csv")
```

## Data tidying

```r
head(poison)
```

We can see a couple of things in the data that can
be improved upon:

1. Capitalize the fist column name
2. Set the Species column as a factor
3. Change the speciec factor levels from 0, 1 and 2 to
Dojofish, Goldfish and Zebrafish. Hint: use the fct_recode
function.
4. Add the variable log.Surv_time: we already saw in previous
tutorials that this transfromation is required to obtain
normally distributed data.

```r
```

---

[Up: contents](index.md) · [Data exploration →](02-data-exploration.md)
