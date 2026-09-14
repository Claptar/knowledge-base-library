---
title: Goal
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Goal

**Source:** [`tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

In this tutorial, we will study the association between dose and
survival time, while correcting for weight and species, by using
a multiple regression model.

Read the required libraries

```r
library(readr)
library(dplyr)
library(tidyverse)
library(ggplot2)
library(car)
```

---

[← Fish tank dataset](01-fish-tank-dataset.md) · [Up: contents](index.md) · [Import the data →](03-import-the-data.md)
