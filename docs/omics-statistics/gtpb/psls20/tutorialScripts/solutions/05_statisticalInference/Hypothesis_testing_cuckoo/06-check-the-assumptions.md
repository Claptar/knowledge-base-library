---
title: Check the assumptions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Check the assumptions

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

1. The observations are independent of each other (in both groups)
2. The data (length) must be normally distributed (in both groups)

Additionally, we should check if the variability within both
groups is similar or not (in the lattter case we should use
a Welch t-test).

3. The variability within both groups is similar

The first assumption is met, as we may assume that there are no
specific patterns of correlation randomly selected nests.

To check the normality assumption, we will use QQ plots.

```r
Cuckoo %>%
  ggplot(aes(sample=length)) +
  geom_qq() +
  geom_qq_line() +
  facet_grid(~type)
```

There seem to be no clear deviations from normality.

The third assumption seems to be met based on our
visualization with the boxplots. As all assumptions are met,
we may proceed with the analysis.

---

[← Data exploration](05-data-exploration.md) · [Up: contents](index.md) · [Two-sample t-test (unpaired) →](07-two-sample-t-test-unpaired.md)
