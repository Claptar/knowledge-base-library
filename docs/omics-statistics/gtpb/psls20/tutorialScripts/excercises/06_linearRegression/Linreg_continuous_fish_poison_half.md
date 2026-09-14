---
title: 'Tutorial 6.3: Linear regression (continuous) on the fish tank dataset'
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_continuous_fish_poison_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/06_linearRegression/Linreg_continuous_fish_poison_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Tutorial 6.3: Linear regression (continuous) on the fish tank dataset

**Source:** [`tutorialScripts/excercises/06_linearRegression/Linreg_continuous_fish_poison_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/06_linearRegression/Linreg_continuous_fish_poison_half.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

As an exercise on linear regression, we will analyse
the fish tank dataset.

# Fish tank dataset

In this experiment, 96 fish (dojofish, goldfish and zebrafish)
were placed separately in a tank with two litres of water and
a certain dose (in mg) of a certain poison EI-43,064. The resistance
of the fish a against the poison was measured as the amount of
minutes the fish survived upon adding the poison (Surv_time, in
minutes). Additionally, the weight of each fish was measured.

# Goal

The research goal is to study the association between the dose of
the poison that was administered to the fish and their
survival time by using a linear regression model.


Read the required libraries

```r
library(tidyverse)
```

# Import the data

```r
poison <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/poison.csv")
```

# Data tidying

We can see a couple of things in the data that can
be improved upon:

1. Capitalise the fist column name
2. Set the Species column as a factor
3. Change the species factor levels from 0, 1 and 2 to
Dojofish, Goldfish and Zebrafish. Hint: use the fct_recode
function.

```r
```

# Data Exploration and Descriptive Statistics

Explore the data, there are multiple variables in the dataset.

How many fish do we have per species?

```r
```


Which variables might influence survival.

Make a suitable visualisation of the association between
the dose and the survival time.

```r
```


# Modelling the data

In principle we have multiple variables that can affect the survival.
We have not seen in the lecture how to model the response based on multiple predictors.
In order to get familiar with simple linear regression

1. Check the remaining assumptions

2. Interpret the model parameters of the linear model

3. Interpret the results, both for the intercept as well as for the slope

4. Write a conclusion that answers the research hypothesis.

---

[Up: contents](../../../index.md)
