---
title: Data visualization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data visualization

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

It is always a good idea to first have a quick look at the raw data;

```r
ap %>% ggplot(aes(x=trt,y=rel,fill=trt)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter") +
  ylab("relative abundance (%)") +
  xlab("treatment group") +
  stat_summary(fun.y=mean, geom="point", shape=5, size=3, color="black", fill="black")
```

We clearly see that, on average, the subjects who had a
microbial transplant have a higher relative abundance of
Staphylococcus spp. But is this difference **significant**?

We can test this with an unpaired, two-sample t-test.
But before we can start the analysis, we must check if
all assumptions to perform a t-test are met.

---

[← Import the dataset](03-import-the-dataset.md) · [Up: contents](index.md) · [Check the assumptions →](05-check-the-assumptions.md)
