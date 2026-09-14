---
title: Two-sample t-test (unpaired)
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Two-sample t-test (unpaired)

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
length_4 <- Cuckoo %>%
  filter(type == "4") %>%
  pull(length)

length_6 <- Cuckoo %>%
  filter(type == "6") %>%
  pull(length)

output <- t.test(length_4,length_6,conf.level = 0.95,var.equal = TRUE)
output
```

---

[← Check the assumptions](06-check-the-assumptions.md) · [Up: contents](index.md) · [Conclusion →](08-conclusion.md)
