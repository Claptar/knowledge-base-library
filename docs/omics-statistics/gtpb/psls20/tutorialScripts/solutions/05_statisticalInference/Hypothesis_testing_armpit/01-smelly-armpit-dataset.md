---
title: Smelly armpit dataset
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/05_statisticalInference/Hypothesis_testing_armpit.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Smelly armpit dataset

In this tutorial, we perform a hypothesis test on the
"smelly armpit" dataset.

Smelly armpits are not caused by sweat, itself. The smell is caused by specific micro-organisms belonging to the group of *Corynebacterium spp.* that metabolise sweat.
Another group of abundant bacteria are the *Staphylococcus spp.*, these bacteria do not metabolise sweat in smelly compounds.

The CMET-groep at Ghent University does research to on transplanting the armpit microbiome to save people with smelly armpits.

- Proposed Therapy:
  	1. Remove armpit-microbiome with antibiotics
    2. Influence armpit microbiome with microbial transplant (https://youtu.be/9RIFyqLXdVw)

- Experiment:

    - 20 students with smelly armpits are attributed to one of two treatment groups
    - placebo (only antibiotics)
    - transplant (antibiotica followed by microbial transplant).
    - The microbiome is sampled 6 weeks upon the treatment
    - The relative abundance of *Staphylococcus spp.* on *Corynebacterium spp.* +
      *Staphylococcus spp.* in the microbiome is measured via DGGE (*Denaturing Gradient
      Gel Electrophoresis*).

## Goal

The overarching goal of this research was to assess if the relative abundance
*Staphylococcus spp.*
in the microbiome of the armpit is affected by transplanting the microbiome.
To this end the researchers randomized patients to two treatment:
A treatment with antibiotics only and a treatment with
antibiotics and a microbial transplant.

In the tutorial on hypotheses testing we will use a formal statistical test to generalize the results from the sample to that of the population.

Load the libraries

```r
library(tidyverse)
```

## Import the dataset

```r
ap <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/armpit.csv")
```

```r
glimpse(ap)
```

## Data visualization

It is always a good idea to first have a quick look at the raw data;

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
Staphylococcus spp. But is this difference **significant**?

We can test this with an unpaired, two-sample t-test.
But before we can start the analysis, we must check if
all assumptions to perform a t-test are met.

---

[Up: contents](index.md) · [Check the assumptions →](02-check-the-assumptions.md)
