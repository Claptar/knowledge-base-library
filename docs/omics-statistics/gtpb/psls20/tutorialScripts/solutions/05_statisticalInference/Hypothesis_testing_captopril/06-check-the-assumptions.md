---
title: Check the assumptions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Check the assumptions

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

The paired t-test has 2 assumptions:

1. The observations are independent of each other (in both groups)
2. The data (SBPb and SBPa) must be normally distributed (in both groups)

Additionally, we must check if the variances are similar for both groups.
If so, we can use a t-test with a pooled variance (see theory).
If not, we must rely on the Welch t-test, which can deal with
unequal variances.

The first assumption is met (same concept as for question 1).
We must first check if the `SBPa` values are also normally distributed.

```r
captopril %>%
  ggplot(aes(sample=SBPa)) +
  geom_qq() +
  geom_qq_line()
```

Again, we can see that all of the data lies nicely around the quantile-quantile
line. As such, we may conclude that our data is normally distributed.

For the third assumption, we must compare the within-group
variability of both groups. We can do this visually with the boxplots.

```r
captopril %>%
  select(SBPb,SBPa) %>%
  gather(type,bp) %>%
  ggplot(aes(x=type,y=bp,fill=type)) +
  scale_fill_brewer(palette="RdGy") +
  theme_bw() +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter(width = 0.2) +
  ggtitle("Boxplot of different blood pressure measures") +
  ylab("blood pressure (mmHg)") + stat_summary(fun.y=mean, geom="point", shape=5, size=3, color="black", fill="black")
```

As a measure of variability, we may take the height
of each boxplot's box. This is the interval between
the 25% and 75% quantile. Here we can see that this
interval, as well as the length of the whiskers, is
approximately equal for both groups. When the sample
sizes are small (as is the case here, we speak about deviation
from equality if one height is more than 2 or 3 times
larger/smaller than that of the other group.

As all three assumptions are met we may continue with
performing the unpaired two-sample t-test.

As such, we will now perform a `paired` t-test.

```r
output2 <- t.test(captopril$SBPb,captopril$SBPa, paired = TRUE)
output2
```

Clearly, by correctly stating that the data is paired,
we have gained a lot of statistical power for rejecting
the null hypothesis that the true mdifferenc in means is
equal to 0. The p-value (p = `r round(unname(output2$p.value),5)`) has now become
extremely significant. Note that the 95% CI has become
narrower!

** Conclusion **

We may conclude that, on the 5% significance level, the mean
SBP levels of patients before captopril treatment is
extremely significantly (p = `r round(unname(output2$p.value),5)`) higher than the mean
SBP levels of patients after captopril treatment. The SBP levels
are on average `r round(unname(output2$estimate),2)` mmHg
higher before treatment than after treatment (95% CI [`r round(output2$conf.int[c(1,2)],2)`]).

### One-sample t-test on the difference

On final thing; performing a paired two-sample t-test is
analogous to performing a one-sample t-test on the difference
between both groups.

This can be easily seen from the output of the paired two-sample
t-test. The alternative hypothesis $HA$ there states that
the "true difference in means is not equal to 0". So internally,
R will actually perform a one-sample t-test on the difference, and
check whether or not the true mean difference is equal to 0.
We can also set this up manually.

```r
bp_diff <- captopril %>%
  mutate(bp_diff = SBPb-SBPa) %>%
  select(bp_diff)

t.test(bp_diff,mu=0)
```

Indeed, the output is completely analogous to that
of the paired two-sample t-test.

---

[← Question 2](05-question-2.md) · [Up: contents](index.md)
