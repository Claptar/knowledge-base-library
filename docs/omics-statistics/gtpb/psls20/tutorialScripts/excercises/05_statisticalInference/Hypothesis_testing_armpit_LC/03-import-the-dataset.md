---
title: Import the dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the dataset

**Source:** [`tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
#Load the libraries
library(tidyverse)
```

Import the data

```r
ap <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/armpit.csv")
```

```r
glimpse(ap)
```

---

[← Goal](02-goal.md) · [Up: contents](index.md) · [Data Exploration →](04-data-exploration.md)
