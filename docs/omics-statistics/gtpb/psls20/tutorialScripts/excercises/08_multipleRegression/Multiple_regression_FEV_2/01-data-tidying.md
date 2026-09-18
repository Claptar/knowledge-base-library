---
title: Data tidying
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Data tidying

As an exercise on multiple regression, we will analyse
the FEV dataset.

### The FEV dataset

The FEV, which is an acronym for forced expiratory volume,
is a measure of how much air a person can exhale (in liters)
during  a forced breath. In this dataset, the FEV of 606 children,
between the ages of 6 and 17, were measured. The dataset
also provides additional information on these children:
their `age`, their `height`, their `gender` and, most
importantly, whether the child is a smoker or a non-smoker.

The goal of this experiment was to find out whether or not
smoking has an effect on the FEV of children.

## Load the required libraries

```r
library(tidyverse)
library(GGally)
```

## Import the data

```r
fev <- read_tsv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/fev.txt")
```

```r
head(fev)
```

There are a few things in the formatting of the
data that can be improved upon:

1. Both the `gender` and `smoking` can be transformed to
factors.
2. The `height` variable is written in inches. Assuming that
this audience is mainly Portuguese/Belgian, inches are hard to
interpret. Let's add a new column, `height_cm`, with the values
converted to centimeters

```r
fev <- fev %>%
  mutate(gender = as.factor(gender)) %>%
  mutate(smoking = as.factor(smoking)) %>%
  mutate(height_cm = height*2.54)

head(fev)
```

That's better!

### Data exploration

```r
fev$height
```

```r
fev %>% mutate(lfev=log(fev)) %>% dplyr::select(smoking,gender,age,height_cm,lfev) %>% ggpairs()
```

```r
plot(log(fev$fev)~fev$age)
```

There a very strong associations between
- age and height
- age and FEV
- heigth and FEV
- gender and height
- gender and FEV
- ...

Remember the "Data_exploration_FEV.Rmd" file? There, we
saw that plotting the FEV in function of smoking status
only, it appeared that the FEV was higher for smokers.

```r
fev %>%
  ggplot(aes(x=smoking,y=age,fill=smoking)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(width = 0.2, size = 0.1, position = position_jitterdodge()) +
  theme_bw() +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  ggtitle("Boxplot of FEV versus smoking") +
  ylab("fev (l)") +
  xlab("smoking status")
```

```r
plot(fev$age~fev$height_cm)
```

However, if we "corrected" the visualization for a child's
age and/or heigth and/or gender, this completely changed the picture.

Let's again make a nice plot where we make a boxplot of the FEV
in function of age (as factor), stratified on gender (facet)
and colored based on the smoking status.

```r
fev %>%
  ggplot(aes(x=as.factor(age),y=fev,fill=smoking)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(width = 0.2, size = 0.1, position = position_jitterdodge()) +
  theme_bw() +
  scale_fill_manual(values=c("dimgrey","firebrick")) +
  ggtitle("Boxplot of FEV versus smoking, stratified on age and gender") +
  ylab("fev (l)") +
  xlab("age (years)") +
  facet_grid(rows = vars(gender))
```

---

[Up: contents](index.md) · [Analysis →](02-analysis.md)
