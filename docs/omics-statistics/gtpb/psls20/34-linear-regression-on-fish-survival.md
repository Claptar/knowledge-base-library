---
title: "34. Linear Regression on Fish Survival"
course: "GTPB Psls20"
chapter: 34
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 34. Linear Regression on Fish Survival

## What this covers

This chapter walks through a tutorial exercise: fitting a simple linear regression to see whether
the dose of a poison predicts how long a fish survives it. It assumes you already have simple
linear regression from the lecture — fitting a line by least squares, and reading its intercept
and slope — and adds the practice of applying that model to a real, slightly untidy dataset in R,
checking its assumptions, and writing a conclusion tied to the research question, rather than any
new theory.

## The fish tank experiment

96 fish — dojofish, goldfish and zebrafish — were each placed alone in a tank holding two litres
of water and a measured dose (in mg) of poison EI-43,064. Two things were then recorded for every
fish:

- `Surv_time` — how many minutes the fish survived after the poison was added, and
- its weight.

The species each fish belonged to was also noted. The raw data is a single CSV (`poison.csv`),
read directly from the course's GitHub repository with `read_csv()`.

The research goal is to describe the relationship between poison dose and survival time with a
linear regression model.

## Why simple regression, and not the full model

Dose is not the only thing in the data that plausibly affects how long a fish survives — its
species and its weight are recorded for exactly this reason, since a heavier fish or a hardier
species might tolerate the same dose differently. A model that accounted for all of them at once
would be a multiple regression, but multiple regression had not yet been covered in the lecture at
this point in the course. So the tutorial deliberately restricts itself to a single predictor —
dose alone — to get comfortable with the mechanics of simple linear regression: fitting it,
checking it, and reading its two parameters, before multiple regression is introduced later to
bring the other variables back in.

## Getting the data into usable shape

Before any modelling, the raw table needs the same kind of tidying that shows up throughout this
course: `Species` is stored as a bare number (0, 1, 2) rather than a proper label, and the first
column name needs capitalising to match the convention used elsewhere. Converting `Species` to a
factor and relabelling its three levels as `Dojofish`, `Goldfish` and `Zebrafish` — the tutorial's
own hint points at `fct_recode` for the relabelling — turns the column from a number a model would
happily average into the three-way grouping variable it actually is.

## The workflow the tutorial follows

1. **Import** the data from the CSV and inspect it.
2. **Tidy** it: fix the column name and turn `Species` into a properly labelled factor.
3. **Explore** it: count how many fish there are of each species, think about which of the
   recorded variables could plausibly affect survival, and plot survival time against dose.
4. **Fit** a simple linear regression of survival time on dose alone, restricting to a single
   predictor for the reason above.
5. **Check** the model's remaining assumptions before trusting it.
6. **Interpret** the two fitted parameters — intercept and slope — and translate the fit back into
   an answer to the research question.

## Exercises

Working from the fish tank dataset described above (96 fish; `Surv_time` in minutes; poison dose
in mg; `Species` coded 0/1/2 for dojofish/goldfish/zebrafish; weight also recorded):

1. Tidy the imported data: capitalise the first column's name, convert `Species` to a factor, and
   recode its levels from `0`, `1`, `2` to `Dojofish`, `Goldfish` and `Zebrafish`.
2. How many fish are there of each species?
3. Which of the recorded variables might plausibly influence survival time? Produce a suitable
   plot showing the association between dose and survival time.
4. Fit a simple linear regression of survival time on dose, and check whatever assumptions of the
   model still need verifying.
5. Interpret the fitted model's parameters — both the intercept and the slope.
6. Write a conclusion, in terms of the original research question, that states what the fitted
   model says about the relationship between poison dose and fish survival.

## Sources

- Tutorial notes: `tutorialScripts/excercises/06_linearRegression/Linreg_continuous_fish_poison_half.Rmd`
  (GTPB PSLS20 course, Tutorial 6.3, "Linear regression (continuous) on the fish tank dataset") —
  the experimental description, the stated research goal, the data-import URL, and all the
  exercise steps (data tidying, data exploration, model fitting, assumption checking, parameter
  interpretation, conclusion) come from this file.
- The file's own R code chunks — for loading libraries, importing the data, tidying it, exploring
  it, and modelling it — are left blank in the source; they are the student's task to complete, not
  material the course supplied, so no R code is reproduced here.
- No slide deck or lecture transcript was supplied for this tutorial. The simple linear regression
  theory it applies (least-squares fitting, the interpretation of an intercept and a slope, and the
  model's assumptions) is referred to as already covered "in the lecture" but is not contained in
  this file; neither is the `fct_recode` function the tutorial names as a hint for relabelling
  `Species`.

---

[← 33. Kruskal-Wallis and Pairwise Wilcoxon Tests](33-kruskal-wallis-and-pairwise-wilcoxon-tests.md) · [Contents](index.md) · [35. Linear Regression on the FEV Dataset →](35-linear-regression-on-the-fev-dataset.md)
