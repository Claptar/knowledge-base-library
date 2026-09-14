---
title: Introduction
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd
source_file: sources/gtpb-psls20/theory/05-statisticalInference-twosampleT.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`theory/05-statisticalInference-twosampleT.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/05-statisticalInference-twosampleT.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(include = TRUE, comment = NA, echo = TRUE,
                      message = FALSE, warning = FALSE)
library(tidyverse)
```

#Smelly armpit example

- Smelly armpits are not caused by sweat, itself. The smell is caused by specific micro-organisms belonging to the group of *Corynebacterium spp.* that metabolise sweat.
Another group of abundant bacteria are the *Staphylococcus spp.*, these bacteria do not metabolise sweat in smelly compounds.

- The CMET-group at Ghent University does research to on transplanting the armpit microbiome to save people with smelly armpits.

- Proposed Therapy:
  	1. Remove armpit-microbiome with antibiotics
    2. Influence armpit microbiome with microbial  transplant (https://youtu.be/9RIFyqLXdVw)

- Experiment:

    - 20 subjects with smelly armpits are attributed to one of two treatment groups
    - placebo (only antibiotics)
    - transplant (antibiotica followed by microbial transplant).
    - The microbiome is sampled 6 weeks upon the treatment
    - The relative abundance of *Staphylococcus spp.* on *Corynebacterium spp.* + *Staphylococcus spp.* in the microbiome is measured via DGGE (*Denaturing Gradient Gel Electrophoresis*).

---

## Import the data

```r
ap<-read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/armpit.csv")
ap
```

## Data exploration

We plot the direct relative abundances in function of the treatment group. With the ggplot2 library we can easily build plots by adding layers.

```r
ap %>%  ggplot(aes(x=trt,y=rel)) + geom_boxplot(outlier.shape=NA) + geom_point(position="jitter")

ap %>% ggplot(aes(sample=rel)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~trt)
```

---

---

[Up: contents](index.md) · [Two sample T-test →](02-two-sample-t-test.md)
