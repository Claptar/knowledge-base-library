---
title: Data visualization
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/DataExplorationCaptoprilMinimalExample.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/04_DataExploration/DataExplorationCaptoprilMinimalExample.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data visualization

**Source:** [`tutorialScripts/excercises/04_DataExploration/DataExplorationCaptoprilMinimalExample.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/DataExplorationCaptoprilMinimalExample.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

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

---

[← Import the data](02-import-the-data.md) · [Up: contents](index.md) · [Descriptive statistics →](04-descriptive-statistics.md)
