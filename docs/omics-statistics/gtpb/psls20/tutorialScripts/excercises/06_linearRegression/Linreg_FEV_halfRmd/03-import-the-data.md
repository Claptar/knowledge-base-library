---
title: Import the data
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Import the data

**Source:** [`tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
fev <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/fev.txt")
head(fev)
```

---

[← Load the required libraries](02-load-the-required-libraries.md) · [Up: contents](index.md) · [Tidy the data →](04-tidy-the-data.md)
