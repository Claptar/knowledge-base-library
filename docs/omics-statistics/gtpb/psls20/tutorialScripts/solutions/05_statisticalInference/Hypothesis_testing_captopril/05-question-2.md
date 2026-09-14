---
title: Question 2
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Question 2

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Is the average SBP before captopril treatment
different from the average SBP after captopril treatment?

As the data is paired, there will be a strong correlation between the BP values
before and after treatment of each individual patient. We can show this
with a scatterplot.

```r
captopril %>%
  ggplot(aes(x=SBPb,y=SBPa)) +
  geom_point() +
  ggtitle("correlation between SBPb and SBPa") +
  ylab("SBPa (mmHg)") +
  xlab("SBPb (mmHg)")
```

We clearly see that if a patient's SBPb value is high, its
SBPa value will be comparatively high as well.

---

[← Question 1](04-question-1.md) · [Up: contents](index.md) · [Check the assumptions →](06-check-the-assumptions.md)
