---
title: Question 1
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Question 1

**Source:** [`tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Is the average systolic blood pressure (SBP)
before captopril treatment higher than 149 mmHg?

In the data exploration of the NHANES dataset we have set up a reference
interval, i.e. an interval that is expected to hold 95% of
the SBP values of healthy individuals. We found the interval
of [93;149] mmHg. (If you did not get to this point of the script
yet, don't worry!).

To test the effect of the captopril on subjects with hypertension
(patients), we need to find a group of patients that have
elevated SBP levels, higher than 149 mmHg.Therefore, we want
to test whether the patients in the captopril study indeed have on average a SBP level
that is greater than 149 mmHg.
We can assess this research hypothesis using a one sample t-test.

## Assess the assumptions

Before we can perform a t-test, we must check that the required
assumptions are met!

1. The observations are independent of each other
2. The data (SBPb) must be normally distributed


```r
... %>%
  ... +
  geom_qq() +
  geom_qq_line()
```

Interpret the qq-plot

If you feel comfortable with assuming normality based on the qq-plot,
you may proceed with the analysis.

## Hypothesis test

Here, we will
test if mean SBPb is significantly higher than 149 mmHg.

More specifically, we will test the null hypothesis;

H0: the mean SBPb is equal to 149 mmHg

versus the alternative hypothesis;

HA: the mean SBPb is greater than 149 mmHg

```r
output1 <- t.test(...,mu=...,alternative = ...,conf.level = ...,data=...)
output1
```

When writing a conclusion on your research hypothesis,
it is very important to be precise and concise, yet complete.
Formulate a proper conclusion.

---

[← Data exploration](03-data-exploration.md) · [Up: contents](index.md) · [Question 2 →](05-question-2.md)
