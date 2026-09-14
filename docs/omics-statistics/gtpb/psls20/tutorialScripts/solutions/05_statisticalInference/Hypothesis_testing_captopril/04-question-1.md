---
title: Question 1
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Question 1

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Is the average systolic blood pressure (SBP)
before captopril treatment higher tahn 149 mmHg?

Yesterday, we used the NHANES dataset to set up a reference
interval, i.e. an interval that is expected to hold 95% of
the SBP values of healthy individuals. We found the interval
of [93;149] mmHg.

To test the effect of the captopril on diseased individuals
(patients), we need to find a group of patients that have
elevated SBP levels, higher than 149 mmHg.Therefore, we want
to test whether or not the provided patients have an SBP level
that is greater than 149 mmHg. To test this, we will perform a
one-sample t-test, which will tell us if the average SBPb of
our patients is significantly greater thatn 149 mmHg on the 5%
significance level.

** important **

Before we can perform a t-test, we must check that the required
assumptions are met!


1. The observations are independent of each other
2. The data (SBPb) must be normally distributed

For the first assumption requires us to think about the data.
Are there any underlying correlation structures (that we know of)
in the data? For instance, if all the 15 subjects are members of
the same family, we expect that the data will give us a good
representation of the underlying population of interest, i.e.,
all past, present and future patients with elevated SBP levels.

In this dataset, we have no reason to believe that this
assumption was violated; we may we have assume 15 unrelated,
"random"  patients with elevated SBP levels.

We can assess the second assumption with a quantile-quantile plot.

```r
captopril %>%
  ggplot(aes(sample=SBPb)) +
  geom_qq() +
  geom_qq_line()
```

We can see that all of the data lies nicely around the quantile-quantile
line (black line). As such, we may conclude that our data is normally distributed.

As such, we may proceed with our analysis. Here, we will
test if mean SBPb is significantly higher than 149 mmHg.

More specifically, we will test the null hypothesis;

$H0:$ the mean SBPb is equal to 149 mmHg

versus the alternative hypothesis;

$HA:$ the mean SBPb is greater than 149 mmHg

```r
output1 <- t.test(captopril$SBPb,mu=149,alternative = "greater",conf.level = 0.95)
output1
```

When writing a conclusion on your research hypothesis,
it is very important to be precise and concise, yet complete.

An example of such a conclusion for our research question
is given below:

The mean SBP of patients before treatment with captopril
is significantly higher (p=`r round(unname(output1$p.value),5)`) than the
upper bound of the reference interval (147 mmHg) on the 5% signifcance level.
The mean SBPb equals `r round(unname(output1$estimate),2)` mmHg with
a 95% confidence interval of [`r round(output1$conf.int[c(1,2)],2)`]).

As we have seen in the theory class, the 95% confidence
interval can be interpreted as;

With 95% confidence we can state that the interval
[`r round(output1$conf.int[c(1,2)],2)`]
contains the true average of SBP of diseased patient before
treatment with captopril.

---

[← Data exploration](03-data-exploration.md) · [Up: contents](index.md) · [Question 2 →](05-question-2.md)
