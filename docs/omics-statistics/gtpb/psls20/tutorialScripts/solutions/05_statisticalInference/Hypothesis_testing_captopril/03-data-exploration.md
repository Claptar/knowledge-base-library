---
title: Data exploration
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data exploration

**Source:** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Before we start delving into the data in order to solve
our research hypothese, it is always a good idea to first
have a look at the data. Our dataset looks like this;

```r
head(captopril)
```

We have 15 patients, for which we have measure the systolic
blood pressure and diastolyic blood pressure, before and after
treatment with the captopril drug.

We can visualize the entire dataframe in an informative way
with boxplots;

```r
captopril %>%
  gather(type,bp,-id) %>%
  ggplot(aes(x=type,y=bp,fill=type)) +
  scale_fill_brewer(palette="RdGy") +
  theme_bw() +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter(width = 0.2) +
  ggtitle("Boxplot of different blood pressure measures") +
  ylab("blood pressure (mmHg)") + stat_summary(fun.y=mean, geom="point", shape=5, size=3, color="black", fill="black")
```

Clearly, it seems that on average the measurements
after treatment are lower than those before treatment.
But is this difference **significant**? To answer this
question, we will need to perform hypothesis tests.
Let's start of with question 1.

---

[← Import the data](02-import-the-data.md) · [Up: contents](index.md) · [Question 1 →](04-question-1.md)
