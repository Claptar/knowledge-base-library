---
title: Check the assumptions
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Check the assumptions

1. The observations are independent of each other (in both groups)
2. The data (rel) must be normally distributed (in both groups)

Additionally, we must check if the variances are similar for both groups.
If so, we can use a t-test with a pooled variance (see theory).
If not, we must rely on the Welch t-test, which can deal with
unequal variances.

The first assumption is met, as we may assume that there are no
specific patterns of correlation in our group of 20 randomly
select subjects. Note, however, that as we sample only in the
population of 'students', we will only be able to extrapolate
our findings to this group.

To check the normality assumption, we will use QQ plots.

```r
ap %>%
  ggplot(aes(sample=rel)) +
  geom_qq() +
  geom_qq_line() +
  facet_grid(cols = vars(trt))
```

We can see that all of the data lies nicely around the quantile-quantile
line (black line). As such, we may conclude that our data is normally distributed.

For the third assumption, we must compare the within-group
variability of both groups. We can do this visually:

```r
ap %>%  ggplot(aes(x=trt,y=rel)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter") +
  ylab("relative abundance (%)") +
  xlab("treatment group") +
  stat_summary(fun.y=mean, geom="point", shape=5, size=3, color="black", fill="black")
```

Here we can see that this interval, as well as the length of the whiskers,
is approximately equal for groups.

As all three assumptions are met we may continue with
performing the unpaired two-sample t-test.

## Two-sample t-test (unpaired)

```r
placebo_rel <- ap %>%
  filter(trt=="placebo") %>%
  pull(rel)

transplant_rel <- ap %>%
  filter(trt=="transplant") %>%
  pull(rel)

output <- t.test(placebo_rel,transplant_rel,conf.level = 0.95,var.equal = TRUE)
output
```

## Conclusion

We may conclude that, on the 5% significance level, the mean
relative abundance in subjects that had a placebo treatment is
significantly (p = `r round(output$p.value,5)`) lower than the mean relative
abundance in subjects that had a microbial transplant. The
relative abundances are on average
`r round( unname(output$estimate[2]) - unname(output$estimate[1]),2)` percent
(95% CI: [ `r round(output$conf.int[c(1,2)],2)` ]) lower with placebo
treatment than with the transplant.

---

[← Smelly armpit dataset](01-smelly-armpit-dataset.md) · [Up: contents](index.md)
