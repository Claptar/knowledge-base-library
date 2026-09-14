---
title: Conclusion
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conclusion

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

We may conclude that, on the 5% significance level, the mean
length of eggs fostered by the European robin in extremely
significantly higher (p = `r round(output$p.value,8)`) than the mean
length of eggs fostered by the Eurasian wren. The eggs
fostered by the European wren are on average
`r round(unname(output$estimate[1])-unname(output$estimate[2]),2)` mm longer
(95% CI [`r round(output$conf.int[c(1,2)],2)`]).

---

[← Two-sample t-test (unpaired)](07-two-sample-t-test-unpaired.md) · [Up: contents](index.md)
