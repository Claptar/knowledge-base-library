---
title: Descriptive statistics
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Descriptive statistics

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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
variable in the data frame `se` for which we calculate the
standard error

```r
apRelSum<-ap%>%
  group_by(trt)%>%
  summarize_at("rel",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))

apRelSum
```

This concludes the data exploration.

---

[← Data visualization](04-data-visualization.md) · [Up: contents](index.md)
