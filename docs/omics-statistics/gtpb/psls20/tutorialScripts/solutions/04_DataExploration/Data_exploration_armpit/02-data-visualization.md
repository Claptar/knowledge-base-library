---
title: Data visualization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_armpit.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Data visualization

It is always a good idea to first have a quick look at the raw
data.

First, try to make a histogram of the data. Fill in the
missing parts in the chunk of code below to get a good-looking
visualization:

```r
ap %>%
  ggplot(aes(x=rel,fill=trt)) + # fill in the correct values for x and fill
  geom_histogram() +
  facet_grid(rows = vars(trt)) + # fill in to put the histograms for both treatment conditions in a separate row
  theme_bw() +
  xlab("relative abundance (%)")
```

Based on this plot, it seems that the relative abundace
is higher for subjects who had the transplants.
However, given the small sample size the histograms
are not optimally informative. A better option would be to
show the data in a boxplot:

```r
ap %>%  ggplot(aes(x=trt,y=rel,fill=trt)) +
  geom_boxplot(outlier.shape=NA) +
  geom_point(position="jitter") +
  ylab("relative abundance (%)") +
  xlab("treatment group") +
  stat_summary(fun.y=mean, geom="point", shape=5, size=3, color="black", fill="black")
```

We clearly see that, on average, the subjects who had a
microbial transplant have a higher relative abundance of
Staphylococcus spp. In the tutorial on hypothesis testing, we will learn how to formally test
whether the observed difference is statistically
**significant**.

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

[← Smelly armpit dataset](01-smelly-armpit-dataset.md) · [Up: contents](index.md)
