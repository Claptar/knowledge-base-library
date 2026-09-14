---
title: Data Exploration
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data Exploration

**Source:** [`tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_armpit_LC.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

A crucial first step in a data analysis is to visualize and to explore the raw data.


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
Staphylococcus spp. But is this difference statistically  *significant* so that we can generalized what we observe in the sample to the population?

We can test this with an unpaired, two-sample t-test, which falsifies the null hypothesis that there is on average no difference in relative abundance of *Staphylococcus* in the armpit microbiome between the transplant and the placebo group against the alternative hypothesis that there is a difference in average abundance of *Staphyloccocus* in the armpit microbiome between the transplant and placebo treatment.

But, before we can start the analysis, we must check if
all assumptions to perform a t-test are met.

## Check the assumptions

1. The observations are independent both within and between groups.  This has to be garanteed by the design.
2. The data (rel) are normally distributed in each of the groups
3. The variability within both groups is similar.

To check the normality assumption, we will use QQ plots.

```r
ap %>%
  ggplot(aes(sample=rel)) +
  geom_qq() +
  geom_qq_line() +
  facet_grid(cols = vars(trt))
```

We can see that the data is nicely scattered around the quantile-quantile
line (black line). As such, we may conclude that the our data are approximately normally distributed.

For the third assumption, we must compare the within-group
variability of both groups. We can do this visually based on the boxplots. The size of the box in the boxplot is the interquartile range, an nonparametric estimator of the variability of the data.
In the plot we observe that the boxes are fairly equal in size indicating that  the box size is
approximately equal for groups.

For small sample sizes the variability estimation is not very precise and the differences in box sizes have to be more than 2 or 3 times larger in one of the groups before there is an indication for the deviation of equality of means. If the variability would not have been equal, we might have resorted the Welch modified T-test.

As all three assumptions are met we may continue with
performing the unpaired two-sample t-test with equal variances.

---

[← Import the dataset](03-import-the-dataset.md) · [Up: contents](index.md) · [Assess the research question with the two-sample t-test →](05-assess-the-research-question-with-the-two-sample-t-test.md)
