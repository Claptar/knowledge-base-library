---
title: Data exploration
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_Regression_fish_half.Rmd) — gtpb-psls20, licensed CC BY 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

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

## Multiple regression model

Fit the multiple regression model with all the main effects:

```r
```

## Assess the model assumptions

```r
```

## Interpret the model parameters

```r
library(car)
#Anova(..., type = "III") ## type three in presence of important interactions
#summary(...)
```

## Conclusion

Formulate a conclusion.

---

[← Fish tank dataset](01-fish-tank-dataset.md) · [Up: contents](index.md)
