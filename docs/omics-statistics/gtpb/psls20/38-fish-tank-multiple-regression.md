---
title: "38. Fish Tank Multiple Regression"
course: "GTPB Psls20"
chapter: 38
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 38. Fish Tank Multiple Regression

## What this covers

This chapter sets up a multiple-regression exercise built around a poisoning experiment on fish. It
answers the question: once a simple regression of survival time on poison dose has been fit, how do
you check whether other measured variables — species and weight — also matter, and how do you build
and read a regression model that accounts for them together, including how they interact with dose?
It assumes a prior tutorial in this course already fit a simple linear regression of (log) survival
time on dose, and that the reader has met multiple regression, interaction terms and the analysis of
variance before.

## The fish tank experiment

Ninety-six fish — dojofish, goldfish and zebrafish — were each placed alone in a tank holding two
litres of water and dosed with a fixed amount (in mg) of the poison EI-43,064. For each fish, two
things were recorded:

- **Surv_time**: the number of minutes the fish survived after the poison was added — the measure
  of the fish's resistance to the poison.
- **Weight**: the fish's weight.

Together with the poison **dose** and the fish's **Species**, the goal is to study how dose relates
to survival time once weight and species are accounted for, using a multiple regression model.

Before any modelling, the raw data need tidying:

- the first column name needs capitalising;
- `Species` needs to be set as a factor;
- its levels, coded `0`, `1`, `2`, need recoding to `Dojofish`, `Goldfish`, `Zebrafish` (the
  suggested tool is `fct_recode`);
- a new variable `log.Surv_time` needs adding, since — as an earlier tutorial in the course already
  showed — survival time itself is not normally distributed, but its logarithm is.

## From a simple regression to a multiple one

A previous tutorial fit survival time (after log transformation) as a function of dose alone. That
model is silent on a real possibility: fish of the same species, or of similar weight, might react
to the poison in a similar way regardless of dose. If species and weight are associated with
survival time — and, on top of that, associated with dose itself — leaving them out of the model
risks attributing their effect to dose, or missing a real effect of dose that they are masking.

The way to check this before modelling is exploratory: look at the pairwise relationships between
dose, weight, species and (log) survival time, and at how weight and species relate to dose itself.
If dose, weight and species turn out not to be independent of each other, the model has to include
them jointly — and, because the exploration suggests they influence each other, the interactions
between them as well as their main effects.

## The multiple regression model

The exercise's own conclusion from the exploration step is that survival time is affected by more
than dose alone, and that dose, species and weight do not act independently: their effects on
survival time depend on one another. Fitting a model that treats them as independent contributions
would therefore misrepresent the data. What is needed is a model with:

- the three **main effects** — dose, species and weight — and
- the **interaction terms** between them, since the main effects are not expected to act in
  isolation.

Once such a model is fit, its assumptions need checking as with any regression, and its parameters
need interpreting. Because the model contains interactions, the recommended tool for interpretation
is a **Type III analysis of variance** (`car::Anova(..., type = "III")`), which is the appropriate
type of ANOVA when the model has interaction terms, alongside the usual `summary()` of the fitted
model.

## Exercises

All of the following are taken from the tutorial script; none is worked here.

1. **Tidy the data.** Starting from `poison.csv`:
   - capitalise the name of the first column;
   - set `Species` as a factor;
   - recode its levels `0`, `1`, `2` to `Dojofish`, `Goldfish`, `Zebrafish`;
   - add a variable `log.Surv_time`, the logarithm of survival time.

2. **Explore the data.**
   - Produce a pairwise plot of the variables (e.g. with `GGally::ggpairs`) and interpret the
     correlations with respect to survival time.
   - Plot log survival time against weight, colouring by species, and interpret the association.
   - Plot weight against dose, colouring by species, and interpret the association.
   - Plot log survival time against dose, colouring by species, and interpret the association.
   - Plot the relationship between log survival time and species, and interpret it.

3. **Fit and check a multiple regression model.**
   - Fit a multiple regression model for log survival time containing the main effects of dose,
     species and weight, together with their interaction terms.
   - Assess the model's assumptions.
   - Interpret the model's parameters, using a Type III analysis of variance
     (`car::Anova(..., type = "III")`) given the presence of interactions, together with
     `summary()` of the fitted model.
   - Formulate a conclusion about the association between dose and survival time, correcting for
     weight and species.

## Sources

- `01-fish-tank-dataset.md` — the experimental description, the tidying tasks, and the tutorial's
  stated goal (studying dose and survival time while correcting for weight and species).
- `02-data-exploration.md` — the rationale for moving to a multiple regression, the exploratory
  plotting tasks, the model-fitting and assumption-checking tasks, and the note on using a Type III
  ANOVA in the presence of interactions.
- Both files are exercise stubs (blank R code chunks) from the GTPB PSLS20 course's multiple
  regression tutorial (`Multiple_Regression_fish_half.Rmd`); no worked code, output or results are
  given in the source, and none is supplied here. The files refer to "previous tutorials" — the
  simple regression of survival time on dose, and the justification for the log transform — which
  were not part of the material supplied for this chapter.

---

[← 37. Multiple Regression and Confounding: FEV](37-multiple-regression-and-confounding-fev.md) · [Contents](index.md) · [39. KPNA2 Gene Expression Study →](39-kpna2-gene-expression-study.md)
