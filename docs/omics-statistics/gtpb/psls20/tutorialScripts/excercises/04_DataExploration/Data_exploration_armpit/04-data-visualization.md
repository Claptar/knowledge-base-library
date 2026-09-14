---
title: Data visualization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data visualization

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

A crucial first step in a data analysis is to visualize and to explore the raw
data.

First, try to make a histogram of the data. Fill in the
missing parts in the chunk of code below to get a good-looking
visualization:

```r
ap %>%
  ggplot(aes(x=...,fill=...)) + ## fill in the correct values for x and fill
  geom_histogram() +
  facet_grid(rows = vars(...)) + ## fill in to put the histograms for both treatment conditions in a separate row
  theme_bw() +
  xlab("relative abundance (%)")
```

Based on this plot, it seems that the relative abundace
is higher for subjects who had the transplants.
However, given the small sample size the histograms
are not optimally informative. A better option for these data would be to
show the data in a boxplot:

```r
ap %>%  ggplot(aes(x=...,y=...,fill=...)) +
```

What do you observe?

## Descriptive statistics

Here, we will generate some informative descriptive statistics
for the dataset.

We first summarize the data and calculate the mean, standard
deviation, number of observations and standard error and store the
result in an object apRelSum via 'apRelSum<-`

1. We pipe the `ap` dataframe to the group_by function to group
the data by treatment trt `group_by(trt)`
2. We pipe the result to the `summarize_at` function to summarize
the "rel" variable and calculate the mean, standard deviation and
the number of observations
3. We pipe the result to the `mutate` function to make a new
variable in the data frame that is named `se` for which we calculate the
standard error

```r
## Use the instructions from above to generate the summary statistics
...
```

This concludes the data exploration. Tomorrow, we will
learn how to formally test whether the observed
difference is statistically **significant**.

---

[← Goal](03-goal.md) · [Up: contents](index.md)
