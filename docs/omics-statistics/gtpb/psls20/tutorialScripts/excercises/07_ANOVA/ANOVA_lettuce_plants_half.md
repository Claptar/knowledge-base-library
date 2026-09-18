---
title: 'Tutorial 7.1: ANOVA in the lettuce dataset'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Tutorial 7.1: ANOVA in the lettuce dataset

In agriculture, it is important to have a high yield
of crops. For lettuce plants, plants with many leaves are known to be preferred by the consumers.

One way to increase the number of leaves (or better, total
leaf weight) is by using a fertilizer. Recently, there is
a tendency to rely more on natural fertilizers, such as compost.
Near Ghent, the institute of research for agriculture and fishery is testing new, natural fertilization methods. One of these new fertilizers is called biochar. Biochar is a residual product from pyrolysis, a process in which biomass is burned under specific conditions (such as high pressure) in order to produce energy. Biochar is similar to charcoal, but has some very useful properties, such as retaining water in the soil. It also has a positive influence on the soil microbiome.

## The lettuce dataset

The researcher hypothesize that biochar, compost and
a combination of both biochar and compost can have a different influence
on the growth of lettuce plants. To this end, they grew up
lettuce plants in a greenhouse. The pots were filled with
one of four soil types;

1. Soil only (control)
2. Soil supplemented with biochar (refoak)
3. Soil supplemented with compost (compost)
4. Soil supplemented with both biochar and compost (cobc)

The dataset `freshweight_lettuce.txt` contains the freshweight
(in grams) for 28 lettuce plants (7 per condition). The researchers
want to use an ANOVA test to assess if the treatments have a different effect on the growth of lettuce
plants. If so, they will use a post-hoc test (Tuckey test) to discover which specific treatments have an effect.

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

```r
## treatment to factor
lettuce <- lettuce %>%
  mutate(treatment = as.factor(treatment))
```

## Data exploration

```r
## Count the number of observations per treatment
lettuce %>%
  count(treatment)
```

Make a plots to explore the data
```r
#...
```

Interpret the boxplots!

1. How will you model the data.
2. Translate the research question into parameters of the model.
3. Check the assumptions.
4. If the assumptions are fulfilled you can fit model
5. Further assess differences between the treatments in a posthoc analysis if applicable.

---

[Up: contents](../../../index.md)
