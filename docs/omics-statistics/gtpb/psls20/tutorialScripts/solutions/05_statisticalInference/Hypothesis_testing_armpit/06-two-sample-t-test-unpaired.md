---
title: Two-sample t-test (unpaired)
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Two-sample t-test (unpaired)

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
placebo_rel <- ap %>%
  filter(trt=="placebo") %>%
  pull(rel)

transplant_rel <- ap %>%
  filter(trt=="transplant") %>%
  pull(rel)

output <- t.test(placebo_rel,transplant_rel,conf.level = 0.95,var.equal = TRUE)
output
```

---

[← Check the assumptions](05-check-the-assumptions.md) · [Up: contents](index.md) · [Conclusion →](07-conclusion.md)
