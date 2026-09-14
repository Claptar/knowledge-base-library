---
title: 'Tutorial 8.1: Multiple regression on the fish tank dataset'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Tutorial 8.1: Multiple regression on the fish tank dataset

**Source:** [`tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

As an exercise on multiple regression, we will analyse
the fish tank dataset.

# Fish tank dataset

In this experiments 96 fish (dojofish, goldfish and zebrafish)
were placed separately in a tank with two liters of water and
a certain dose (in mg) of a certain poison EI-43,064. The resistance
of the fish a against the poison was measured as the amount of
minutes the fish survived upon adding the poison (Surv_time, in
minutes). Additionally, the weightt of each fish was measured.

# Goal

In this tutorial, we will study the association between dose and
survival time, while correcting for weight and species, by using
a multiple regression model.

Read the required libraries

```r
library(tidyverse)
```

# Import the data

```r
poison <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/poison.csv")
```

# Data tidying

```r
head(poison)
```

We can see a couple of things in the data that can
be improved upon:

1. Capitalize the fist column name
2. Set the Species column as a factor
3. Change the speciec factor levels from 0, 1 and 2 to
Dojofish, Goldfish and Zebrafish. Hint: use the fct_recode
function.
4. Add the variable log.Surv_time: we already saw in previous
tutorials that this transfromation is required to obtain
normally distributed data.

```r
```

# Data exploration

In a previous tutorial, we already studied the effect of
dose on (the logarithm of) suvival time. There, we did not
account for the fact that fish of the same species and/or
fish of similar weight will probably reacht similarly to
the poison.

When we expect the data more closely, we see that these
factors do indeed matter.

```r
library(GGally)
#poison %>%  select(-survival) %>% ggpairs()
```

Interpret the correlations with respect to the survival time.

Some additional visualizations:

- Plot the log survival time in function of weigth.
Add species as a color.

```r
```

Interpret the observed association.

- Plot the fish weights in function of dose, color on species.

```r
```

Interpret the observed association.

- Plot the log of survival time in function of dose, color on species.

```r
```

Interpret the observed association.

- Plot the relationship between log survival time and species.

```r
```

Interpret the observed association.

The researchers assume, based on the data exploration, that
there are multiple variables other than the dose of the poison
that affect the survival time of the fishes.

In addition, it seems that the main effects (i.e. dose, species and
weight) influence each other. As such, we must construct a multiple
regression model that contains all main effects as well as the interaction terms.


# Multiple regression model

Fit the multiple regression model with all the main effects:

```r
```

# Assess the model assumptions

```r
```

# Interpret the model parameters

```r
library(car)
#Anova(..., type = "III") ## type three in presence of important interactions
#summary(...)
```


# Conclusion

Formulate a conclusion.

---

[Up: contents](../../../index.md)
