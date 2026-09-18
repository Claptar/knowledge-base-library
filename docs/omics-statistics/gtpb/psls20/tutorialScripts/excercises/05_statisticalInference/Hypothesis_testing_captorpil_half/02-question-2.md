---
title: Question 2
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Question 2

Is the average SBP before captopril treatment is different from the
average SBP after captopril treatment?

The data are paired data; each patient's BP values were measured twice.
Therefore, there will be a strong correlation between the BP values before and
after treatment of each individual patient. We can show this
with a scatterplot.

```r
# Create scatterplot
```

We clearly see that if a patient's SBPb value is high, its
SBPa value will be comparatively high as well.

As such, we will now need to perform a paired two-sample t-test. First, we must
check the assumptions.

## Check the assumptions

State the assumptions that you have to check and include the diagnostic plots to assess the assumption.

## Hypothesis test

If all assumptions are met, we may continue with
performing the paired two-sample t-test.

```r
output2 <- t.test(...,..., paired = ...,data=)
output2
```

Formulate a conclusion bases on the output

## One-sample t-test on the difference

Performing a paired two-sample t-test is
analogous to performing a one-sample t-test on the difference
between both groups.

This can be spotted in the output of the paired two-sample
t-test. The alternative hypothesis HA there states that
the "true difference in means is not equal to 0". So internally,
R will actually perform a one-sample t-test on the difference, and
check whether or not the true mean difference is equal to 0.
We can also set this up manually.

```r
captopril %>%
  mutate(bp_diff = ...) %>%
  t.test(...,mu=...)
```

Indeed, the output is completely analogous to that
of the paired two-sample t-test.

---

[← Question 1](01-question-1.md) · [Up: contents](index.md)
