---
title: Data exploration
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data exploration

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_cuckoo.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

How many birds do we have for each type?

```r
Cuckoo %>%
  count(type)
```

Visualize the data

```r
Cuckoo %>%
  ggplot(aes(x=type,y=length,fill=type)) +
  geom_boxplot() +
  theme_bw() +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter(width = 0.2) +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  ggtitle("Boxplot of the length of eggs per type") +
  ylab("length (mm)") +
  stat_summary(fun.y=mean, geom="point", shape=5, size=3, color="black", fill="black")
```

We clearly see that, on average, the eggs laid in the
nest of the European robin (type=4) are larger than those
laid in the nest of the Eurasian wren. But is this difference **significant**?

We can test this with an unpaired, two-sample t-test.
Buu before we can start the analysis, we must check if
all assumptions to perform a t-test are met.

---

[← Data tidying](04-data-tidying.md) · [Up: contents](index.md) · [Check the assumptions →](06-check-the-assumptions.md)
