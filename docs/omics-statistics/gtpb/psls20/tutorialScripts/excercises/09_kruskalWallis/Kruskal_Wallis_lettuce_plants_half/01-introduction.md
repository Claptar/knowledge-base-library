---
title: Introduction
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

In a previous tutorial, we analysed the dataset on
lettuce plants with ANOVA (see ANOVA_lettuce_plants_half.rmd in chapter 7).
However, it was not clear if all the assumptions of ANOVA were met.
Indeed, with only 7 values per group, it is very hard to assess
the assumptions of normality and equal variances.

Therefore, we will re-analyse the dataset by using the
non-parametric alternative to ANOVA, the Kruskal-Wallis test,
which is the alternative of ANOVA if the assumptions are not met.

## The lettuce dataset

The researcher want to find out if biochar, compost and
a combination of both biochar and compost have an influence
on the growth of lettuce plants. To this end, they grew up
lettuce plants in a greenhouse. The pots were filled with
one of four soil types;

1. Soil only (control)
2. Soil supplemented with biochar (refoak)
3. Soil supplemented with compost (compost)
4. Soil supplemented with both biochar and compost (cobc)

The dataset `freshweight_lettuce.txt` contains the freshweight
(in grams) for 28 lettuce plants (7 per condition). The researchers
want to use an ANOVA test to find out whether or not there is an
effect of one or more of the treatments on the growth of lettuce
plants. If so, they will use a post-hoc test (Tuckey test) to find
which specific treatments have an effect.

Load the required libraries

```r
library(tidyverse)
```

## Data import

```r
lettuce <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/freshweight_lettuce.txt")
```

Take a glimpse at the data

```r
glimpse(lettuce)
```

## Data tidying

```r
## set treatment to factor
## ...
```

## Data exploration

```r
## Count the number of observations per treatment

```

Now let's make a boxplot displaying the freshweight
of each treatment condition:

```r
# ...
```

Interpret the visualization!

In the analysis in chapter 7 (ANOVA_lettuce_plants_half.rmd file),
we accepted the assumptions for analyzing the data with an ANOVA.
However, it was not clear if all the assumptions of ANOVA were met.
Indeed, with only 7 values per group, it is very hard to assess
the assumptions of normality and equal variances.

Therefore, we will re-analyse the dataset by using the
non-parametric alternative to ANOVA: the Kruskal-Wallis test.

## Kruskal-Wallis rank test

### Hypotheses

Formulate a correct null and alternative hypothesis for the Kruskal-Wallis test in this analysis.

### Analysis

```r
#set.seed(1)
#kw <- kruskal_test(...)
#kw
```

Interpret the results!

---

[Up: contents](index.md) · [Post-hoc analysis →](02-post-hoc-analysis.md)
