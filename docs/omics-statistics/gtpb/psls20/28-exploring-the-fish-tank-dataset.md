---
title: "28. Exploring the Fish Tank Dataset"
course: "GTPB Psls20"
chapter: 28
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 28. Exploring the Fish Tank Dataset

## What this covers

This chapter works through the exploratory step of a multiple-regression exercise, using a
dataset on fish and a poison. Before any model is fitted, the question is which predictors — dose,
weight, species — actually look related to the outcome, and whether they look related to *each
other* in a way that will complicate a simple additive model. It assumes the reader already knows
what a multiple regression model with interaction terms is, and can read a scatterplot matrix and
a boxplot; it does not derive or fit the regression itself, only the reasoning that decides what
the model needs to contain.

## The experiment behind the data

96 fish — dojofish, goldfish and zebrafish — were each placed alone in a tank with two litres of
water and a dose (in mg) of the poison EI-43,064. Two outcomes were recorded per fish: how long it
survived after the poison was added (`Surv_time`, in minutes) and its weight. The goal of the
exercise is to study the association between dose and survival time *while correcting for weight
and species*, which is exactly the situation multiple regression is for: dose is the predictor of
interest, and weight and species are variables that need to be accounted for before dose's effect
can be read off cleanly.

## Getting the data into shape

Before any plotting, the raw table needs four small fixes, all standard tidying rather than
anything statistical:

- capitalise the `species` column name to `Species`;
- set `Species` as a factor rather than a bare number;
- recode the factor's numeric levels to names — `0` is Dojofish, `1` is Goldfish, `2` is Zebrafish;
- add a new column `log.Surv_time`, the natural log of survival time.

The log transform is not new here: an earlier tutorial (not part of this chapter's material)
already established that survival time needs this transformation to be approximately normally
distributed. Every plot and every model from this point on uses `log.Surv_time`, not the raw
survival time.

## Reading the pairwise plot

The first move is a pairwise plot of all the variables together (`ggpairs`), which is a fast way
to see, in one picture, every two-way relationship the model might need to represent. It shows:

- survival time is strongly associated with dose, with species, and with weight;
- there is a strong positive association between log survival time and weight;
- that association is not perfectly straight — for low weights, the slope of log survival time on
  weight seems to flatten;
- the weights are not equally distributed across the different doses;
- there is an association between species and weight.

The last two points matter as much as the first three. If weight, dose and species are entangled
with each other, then a model that only looks at each one's marginal relationship with survival
time risks attributing one variable's effect to another.

## Weight, species, and survival

Plotting log survival time against weight, with points coloured by species, confirms the strong
weight relationship seen in the pairwise plot — but it also shows that weight itself differs by
species. So "heavier fish survive longer" and "some species are heavier than others" are both true
at once, and a model that ignores species when looking at weight (or vice versa) would be
confounding the two.

The same entanglement shows up from the other side: plotting weight against dose (as a boxplot with
the individual fish jittered on top) shows that the doses were not administered to fish of evenly
matched weight — some doses (for instance 1.9 mg) happened, apparently by chance, to be given to
fish that were somewhat heavier or lighter than average. That is exactly the kind of accidental
imbalance a designed experiment tries to avoid, and it is a second reason weight has to be in the
model rather than set aside.

## Dose, species, and survival

Plotting log survival time against dose, coloured by species, with a separate linear fit per
species, shows a clear linear relationship between dose and log survival time overall — but the
intercept of that linear relationship differs by species. Plotting log survival time against
species alone (boxplot) confirms directly that log survival time differs across species.

Put together, dose predicts survival, weight predicts survival, species predicts survival, and
weight and dose are each entangled with species. None of these relationships can safely be read in
isolation.

## What the exploration decides

Based on this picture, the researchers judge that the effect of dose on survival varies between
species — not just the baseline survival level, but how strongly dose moves it. That is a claim
about a slope changing across groups, which an additive model (one dose coefficient shared by every
species) cannot represent; it calls for an **interaction term between dose and species**. The same
reasoning is extended to weight: since weight's relationship to survival also plausibly differs by
species, the planned model includes a **weight-by-species interaction** as well.

This is where the exploratory part of the exercise stops. The actual fitting of that model —
`log.Surv_time` regressed on dose, species, weight, and the two interactions — is the next step in
the exercise but is not part of the material behind this chapter.

## Sources

Both source files convert the same R Markdown tutorial script, `tutorialScripts/excercises/08_multipleRegression/fish_tank_explore.Rmd`
from the GTPB PSLS20 course (licensed CC BY 4.0):

- Dataset description, experimental setup, and the four tidying steps (renaming, factor recoding,
  log transform) — `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore/01-fish-tank-dataset.md`.
- The pairwise plot, the weight/species/dose exploratory plots and their stated interpretations,
  and the resulting decision to include the dose-by-species and weight-by-species interactions —
  `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/08_multipleRegression/fish_tank_explore/02-data-exploration.md`.

No slide deck, transcript, or separate exercise set was supplied for this chapter. The earlier
tutorial that established the need for the log transformation, and the actual fitting of the
interaction model that this exploration sets up, are referred to in the material but not contained
in it.

---

[← 27. Exploring the Captopril Dataset](27-exploring-the-captopril-dataset.md) · [Contents](index.md) · [29. Checking t-test Assumptions →](29-checking-t-test-assumptions.md)
