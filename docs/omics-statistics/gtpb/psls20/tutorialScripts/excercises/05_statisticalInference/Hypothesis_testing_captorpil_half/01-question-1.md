---
title: Question 1
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_captorpil_half.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Question 1

In this second tutorial, we will see some basics
in hypothesis testing and more specifically on
t-tests. As an example, we will work with the
captopril dataset that we explored in the tutorial on data exploration.

We will work around these two research questions;

1) Is the average systolic blood pressure
before captopril treatment (SBPb) higher than 149 mmHg?

2) Is the average SBP before captopril treatment
significantly different from the average SBP after
captopril treatment?

First, we will load the required R libraries:

```r
```

## Import the data

```r
captopril <- ...
```

## Data exploration

**Note:** you may copy the results from the data exploration tutorial.

Before we start with hypothesis testing, it is crucial to first explore the data.

```r
```

We have 15 patients, for which we have measured the systolic
blood pressure and diastolyic blood pressure, before and after
treatment with the captopril drug.

Visualize the data in an informative way (see tutorial of yesterday)

```r
```

Interpret the plot!

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

### Assess the assumptions

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

### Hypothesis test

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

[Up: contents](index.md) · [Question 2 →](02-question-2.md)
