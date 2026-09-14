---
title: Data visualization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data visualization

**Source:** [`tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/04_DataExploration/Data_exploration_captopril.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

One straightforward possibility to visualize the four types
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

A Barplot is a plot that you will commonly find in papers.

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

A barplot, however, is not very informative. The height of the bars
only provides us with information of the mean blood pressure.
However, we don't see the actual underlying values, so we for
instance don't have any information on the spread of the data.
It is usually more informative to represent to underlying
values as _raw_ as possible. Boxplots are ideal for this!

Note that it is possible to add the raw data on
the barplot, but we still would not see any measures of the
spread, such as the interquartile range.

## Boxplot

With the boxplot, we get a lot of useful information.
We immediately see multiple features of the spread of
the data, such as the median, the 25% and 75% quantiles
and outliers. Since we only have 15 raw values (patients),
we can easily add them to the plot without getting messy.

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


In terms of interpretation, we can see that the median
systolic and diastolic blood pressure values are lower
after treatment with captopril than before. If we want to
have visual inference on the mean values (cfr. class on t-test),
we can add them to the plot `stat_summary` function.

## Paired data
An important feature of this dataset is that it contains
paired data; for each patient, we have blood pressure values
(systolic and diastolic) before and after treatment with
captopril.

We first plot the systolic blood pressure measurements.
We make a plot with the data points for the two systolic blood pressure measurements in the patient id.

```r
captopril %>%
  gather(type,bp,-id) %>%
  filter(type%in%c("SBPa","SBPb")) %>%
  ggplot(aes(x=id,y=bp,color=type)) +
  geom_point() +
  scale_color_manual(values = c("darkgreen","red"))
```

We see that for all patients, the systolic blood
pressure is lower after captopril treatment than before.
Note that we could not see this from the boxplot, directly.

Another good way to visualise the paired data is by using a line plot that is grouped
by subject. Note, that we make a factor of the type and that we choose order of
the levels so that the level "b" before becomes before the level "a". Otherwise
the after measurements will appear first in the plot.

```r
captopril %>%
  gather(type,bp,-id) %>%
  mutate(type=factor(type,levels=c("SBPb","SBPa","DBPb","DBPa"))) %>%
  filter(type%in%c("SBPa","SBPb")) %>%
  ggplot(aes(x=type,y=bp)) +
  geom_line(aes(group = id)) +
  geom_point()
```

```r
captopril %>%
  gather(type,bp,-id) %>%
  mutate(type=factor(type,levels=c("SBPb","SBPa","DBPb","DBPa"))) %>%
  filter(type%in%c("DBPa","DBPb")) %>%
  ggplot(aes(x=type,y=bp)) +
  geom_line(aes(group = id)) +
  geom_point()
```

Analogously, we may immediately difference the `after` measurement from the
`before` measurement because we have paired data.

```r
captopril %>%
  mutate(bp_diff = SBPa-SBPb) %>%
  ggplot(aes(x="",y=bp_diff)) +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter(width = 0.2) +
  ggtitle("Boxplot of the difference in blood pressure") +
  ylab("blood pressure difference (mmHg)") + stat_summary(fun.y=mean, geom="point", shape=5, size=3, color="black", fill="black") +
  theme_bw()+
  ylim(-40,10) +
  geom_hline(yintercept = 0, color="red") # adds horizontal line to plot
```

The mean difference is lower than zero. It seems
that on average the captopril treatment has lowered
the blood pressure by about 20 mmHg.

## Assumptions: QQ-plot

In the tutorial on hypothesis testing we will assess if this difference is statistically significant.
We will introduce a statistical test that relies on the assumption that the differences are normally distributed.
We can check this with a QQ-plot:

```r
captopril %>%
  mutate(bp_diff = SBPa-SBPb) %>%
  select(bp_diff) %>%
  ggplot(aes(sample=bp_diff)) +
  geom_qq() +
  geom_qq_line()
```

The plot shows no large deviations of the straight line indicating that the data are approximately normally distributed.

#Descriptive statistics

Descriptive statistics for all blood pressure measurements are found below.

```r
captopril %>%
  gather(type,bp,-id) %>%
  group_by(type) %>%
     summarize_at("bp",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum))%>%
  mutate(se=sd/sqrt(n))
```

It is also very useful to calculate the descriptive statistics for the systolic blood pressure difference because we can assess the effect size of administering captopril for every patient.

```r
captopril %>%
  mutate(bp_diff = SBPa-SBPb) %>%
     summarize_at("bp_diff",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n))
```

---

[← Import the data](02-import-the-data.md) · [Up: contents](index.md) · [Wrap-up →](04-wrap-up.md)
