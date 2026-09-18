---
title: Introduction
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_captopril.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

In this second tutorial, we will see some basics
in hypothesis testing and more specifically on
t-tests. As an example, we will work with the
captopril dataset that we explored yesterday.

We will work around these three research questions;

1) Is the average systolic blood pressure
before captopril treatment (SBPb) higher than 149 mmHg?

2) Is the average SBP before captopril treatment
significantly different from the average SBP after
captopril treatment?

First, we will load the required R libraries:

```r
library(tidyverse)
```

## Import the data

```r
captopril <- read.table("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/captopril.txt", header = TRUE, sep = ",")
```

## Data exploration

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

[Up: contents](index.md) · [Question 1 →](02-question-1.md)
