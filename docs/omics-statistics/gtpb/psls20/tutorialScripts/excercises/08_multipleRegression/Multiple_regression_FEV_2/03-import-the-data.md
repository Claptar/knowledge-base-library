---
title: Import the data
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the data

**Source:** [`tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
fev <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/fev.txt")
```

```r
head(fev)
```

---

[← Load the required libraries](02-load-the-required-libraries.md) · [Up: contents](index.md) · [Data tidying →](04-data-tidying.md)
