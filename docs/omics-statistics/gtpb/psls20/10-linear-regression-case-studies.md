---
title: "10. Linear Regression Case Studies"
course: "GTPB Psls20"
chapter: 10
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Linear Regression Case Studies

## What this covers

This chapter introduces the third day of practicals in the course: three linked tutorials that each apply a
linear regression model to a different dataset. It does not derive the linear regression model itself — that
belongs to the tutorial exercises each dataset points to — but it lays out the experimental question each
tutorial is built to answer, and what each dataset actually contains. It assumes the reader already knows what
a linear regression model is and is about to see it applied to real data.

## The day's three tutorials

On the third day of the course, three tutorials cover linear regression, each built on its own dataset: a
first dataset, the fish dataset, and the FEV dataset. Only the fish and FEV datasets are described in the
source material — the first is referenced only as a placeholder ("Add dataset 1"), with no data, exercise, or
description attached, so it is left out of what follows.

## The fish dataset: poison dose and survival time

Ninety-six fish — a mix of dojofish, goldfish and zebrafish — were each placed individually in a tank
containing two litres of water and a measured dose (in mg) of a poison, EI-43,064. For each fish, two
quantities were recorded:

- `Surv_time`: how many minutes the fish survived after the poison was added — its resistance to the poison
- the fish's weight

The question the tutorial studies is whether the dose of poison predicts how long a fish survives. Framed as
linear regression, dose (with weight available as an additional variable) predicts survival time. The
associated exercise script, `Linreg_continuous_fish_poison_half.Rmd`, works through fitting and interpreting
that model on the data in `poison.csv`.

## The FEV dataset: does smoking affect lung function in children?

FEV — forced expiratory volume — is a measure of how much air a person can exhale during a forced breath, and
is a standard measure of lung function. The dataset records the FEV of 606 children aged 6 to 17, together
with each child's age, height, gender, and smoking status (smoker or non-smoker).

The question the tutorial is built around is whether smoking has a measurable effect on FEV in children. That
is a linear regression question with one predictor of particular interest — smoking status — among several
other variables recorded for each child, fit on the data in `fev.txt`.

## Exercises

The source material points to two tutorial exercises, run as R Markdown scripts against the datasets above.
Neither exercise script was itself supplied for this chapter, so only what each is for is given here, not a
worked version of it:

1. **Fish poison tutorial.** Using the 96 fish and their measured poison dose and survival time (with weight
   available as an additional variable), fit and interpret a linear regression relating dose to survival time.
   Script: `Linreg_continuous_fish_poison_half.Rmd`. Data: `poison.csv`.

2. **FEV tutorial.** Using the FEV, age, height, gender and smoking status of 606 children, fit and interpret a
   linear regression that asks whether smoking status is associated with FEV. Data: `fev.txt`. No exercise
   script for this tutorial was given in the source.

## Sources

- All context above is drawn from the course's own overview page for this session: `06_linearRegression.md`
  (GTPB/PSLS20 `tutorialScripts/excercises/06_linearRegression/`, CC BY 4.0).
- The overview page referred to, but did not itself contain, the following files, which were not supplied to
  this chapter and so are not described any further than the overview page describes them:
  - the exercise for "dataset 1" — the source gives only the placeholder "Add dataset 1", with no dataset,
    exercise, or description attached
  - `Linreg_continuous_fish_poison_half.Rmd`, the R Markdown exercise script for the fish tutorial
  - `poison.csv`, the fish poison dataset itself
  - the exercise script for the FEV tutorial (the source lists no script, only the data file)
  - `fev.txt`, the FEV dataset itself
- No slides or transcript were supplied for this session; this chapter is built entirely from the tutorial
  overview page listed above.

---

[← 9. Simple Linear Regression](09-simple-linear-regression.md) · [Contents](index.md) · [11. One-Way ANOVA and Post-Hoc Tests →](11-one-way-anova-and-post-hoc-tests.md)
