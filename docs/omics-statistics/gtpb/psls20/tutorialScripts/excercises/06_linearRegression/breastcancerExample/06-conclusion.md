---
title: Conclusion
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conclusion

**Source:** [`tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/breastcancerExample.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

There is an extremely significant negative association between the S100A8 gene expression and that of ESR1 ($p<<0.001$).

A patient with an ESR1 expression that is 2 times the expression of that of another patient will on average have an  S100A8 expression that is `r round(2^-lm2$coef[2]
,2)` times lower (95\% CI [`r paste(sort(round(2^-confint(lm2)[2,],2)),collapse=",")`]).

---

[← Model](05-model.md) · [Up: contents](index.md)
