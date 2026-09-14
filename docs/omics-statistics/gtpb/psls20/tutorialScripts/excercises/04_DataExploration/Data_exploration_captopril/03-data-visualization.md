---
title: Data visualization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data visualization

**Source:** [`tutorialScripts/excercises/04_DataExploration/Data_exploration_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Let's say we now first want to visualize the data.
One possibility to easily visualize the four types
of blood pressure values is by adopting the `gather`
function from tidyverse. It will reshape the dataframe,
such that we have have a single variable `type`, which
points at one of the four blood pressure types, and `bp`,
which points at the actual value for each type
for each patient.

```r
captopril %>%
  gather(type,bp,-id)
```

## Barplot

A barplot is a plot that you will commonly find in papers.
The code for generating such a barplot is provided below:

```r
captopril %>%
  gather(type,bp,-id) %>%
  group_by(type) %>%
     summarize_at("bp",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n)) %>%
  ggplot(aes(x=type,y=mean,fill=type)) +
  scale_fill_brewer(palette="RdGy") +
  theme_bw() +
  geom_bar(stat="identity") +
  geom_errorbar(aes(ymin=mean-se, ymax=mean+se),width=.2) +
  ggtitle("Barplot of different blood pressure measures") +
  ylab("blood pressure (mmHg)")
```

A barplot, however, is not very informative. The height of the
bars only provides us with information of the mean blood pressure.
However, we don't see the actual underlying values, so we for
instance don't have any information on the spread of the data.
It is usually more informative to represent to underlying
values as _raw_ as possible. Note that it is possible to add the
raw data on the barplot, but we still would not see any measures
of the spread, such as the interquartile range.

Based on this critisism, can you think of a better
visualization strategy for the captopril data?

Go ahead and try out alternative strategies for generating
the most informative plot you can think of. In addition,
you may use the plethora of ggplot functionalities
to make it look good as well!

```r
## Generate an informative plot of the captopril data
...
```

After generating the plot, make sure to interpret
the visualization thoroughly. This may greatly improve
our understanding of the data, which will aid the following
data analysis.

## Paired data
An important feature of this dataset is that it contains
paired data; for each patient, we have blood pressure values
(systolic and diastolic) before and after treatment with
captopril.

It is likely that your previous visualizition does not show
that the data is paired. Can you think of a plot that shows this
information?

**Hint:** Try to use `geom_line(aes(group = id))` for
visualizing the paired data in the chunk of code below

```r
```


As an alternative to looking at the paired data, we may think
of the data in terms of the difference between the `after`
measurement and the `before` measurement.

Can you visualize the difference between the systolic
blood pressure levels before and after captopril treatment?

```r
captopril %>%
  mutate(bp_diff = ...) %>%
  ...
```

In order to assess the effect of captopril, to which
value should you compare the difference? Why?

## Assumption: Normal distribution of the blood pressure differences

In the tutorial on statistical inference we will assess if the systolic blood pressure before and after administering captopril is on average different.
The statistical test for paired data relies on the assumption that the systolic blood pressure differences are normally distributed.
We can check this with a QQ-plot:

```r
captopril %>%
  mutate(bp_diff = ...) %>%
  ...
```

The plot shows no large deviations of the straight line indicating that the data are approximately normally distributed.

#Descriptive statistics

Descriptive statistics for all blood pressure measurements are found below.
Have a look at the exploration of the armpit data
to generate useful summary statistics.

```r
captopril %>%
  gather(type,bp,-id) %>%
  ...
```

It is also very useful to calculate the descriptive statistics for the systolic bloodpressure difference because we can assess the effect size of administering captopril for every patient.

```r
captopril %>%
  ...
```

---

[← Import the data](02-import-the-data.md) · [Up: contents](index.md) · [Wrap-up →](04-wrap-up.md)
