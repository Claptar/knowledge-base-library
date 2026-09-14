---
title: Tidy the data
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Tidy the data

**Source:** [`tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← Import the data](03-import-the-data.md) · [Up: contents](index.md) · [Data Exploration →](05-data-exploration.md)
