---
title: Data tidying
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data tidying

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

For this exercise, we only care about the European robin
and the Eurasian wren. Therefore, we can remove the observations
of the other types. In addition, it seems that the `tpye`
column rather than a factor. Let's fix this:

```r
Cuckoo <- Cuckoo %>%
  filter(type %in% c("4","6")) %>%
  mutate(type = as.factor(type))
```

---

[← Import the data](03-import-the-data.md) · [Up: contents](index.md) · [Data exploration →](05-data-exploration.md)
