---
title: Conclusion
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conclusion

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

We may conclude that, on the 5% significance level, the mean
relative abundance in subjects that had a placebo treatment is
significantly (p = `r round(output$p.value,5)`) lower than the mean relative
abundance in subjects that had a microbial transplant. The
relative abundances are on average
`r round( unname(output$estimate[2]) - unname(output$estimate[1]),2)` percent
(95% CI: [ `r round(output$conf.int[c(1,2)],2)` ]) lower with placebo
treatment than with the transplant.

---

[← Two-sample t-test (unpaired)](06-two-sample-t-test-unpaired.md) · [Up: contents](index.md)
