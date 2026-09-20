---
title: "37. Multiple Regression and Confounding: FEV"
course: "GTPB Psls20"
chapter: 37
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 37. Multiple Regression and Confounding: FEV

## What this covers

A second worked exercise in multiple regression, set up as a self-contained analysis for the
reader to carry out rather than one that is walked through. It assumes the reader already has
multiple linear regression — fitting a model with several predictors, reading a coefficient as an
effect "holding the other variables fixed," and the idea of a **confounder**, a third variable
associated with both the predictor of interest and the outcome that can create or hide an
association between them. The question this exercise poses is a clean instance of exactly that
problem: an apparent effect of smoking on lung function that has to be checked against the other
things that differ between the smokers and non-smokers in the sample.

## The FEV dataset and the question

FEV — forced expiratory volume — is a measure of how much air a person can exhale, in litres,
during a forced breath. The dataset records the FEV of 606 children aged 6 to 17, together with
each child's `age`, `height`, `gender`, and, most importantly, whether the child is a smoker or a
non-smoker.

The question the exercise sets is whether smoking has an effect on the FEV of children — but with
a qualification that is the whole point of doing this as a multiple regression rather than a
two-group comparison: **accounting for potential confounders**. Smokers and non-smokers in a
sample of children are not otherwise identical groups — age and height, in particular, both affect
lung volume directly and are very likely to differ between smokers and non-smokers (a child who
smokes is more likely to be older) — so a raw comparison of FEV between the two groups risks
attributing to smoking an effect that is really driven by age or height. Untangling that is what
the regression model, with smoking status alongside the other recorded variables, is for.

## Exercises

The dataset and goal above are the setup for the following tasks. Carry out each step and record
what it shows before moving to the next.

1. Import the FEV dataset and tidy it as needed for analysis (in particular, make sure that
   categorical variables such as gender and smoking status are represented as such, not as
   numbers).
2. Explore the data: visualize the (unadjusted) association between smoking and FEV, and then
   examine `age`, `height`, and `gender` as potential confounders of that association — how does
   each of them relate both to smoking status and to FEV?
3. Fit a regression model for FEV that includes smoking status together with the variables
   identified as potential confounders, and interpret the coefficient on smoking status in that
   model.
4. State a conclusion: does smoking have an effect on the FEV of children once age, height, and
   gender are accounted for, and how does that conclusion compare with what the raw, unadjusted
   comparison in step 2 suggested?

## Sources

This chapter is built entirely from the converted tutorial notes for this exercise; no slide deck
or lecture transcript was supplied for it, and no worked solution is included in the source.

- Dataset description ("The FEV dataset") and the stated goal: `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_half_2.md`.
- The same file's section headings — `Load libraries and import the data`, `Data tidying`, `Data
  exploration` (with the instruction to "visualize the effect of smoking on the FEV" and "assess
  all potential confounders"), `Data analysis`, and `Conclusion` — give the structure of the
  exercise reproduced above; the source itself contains no code, output, or discussion under any
  of these headings beyond that one sentence of instruction, so no worked figures, model output,
  or numerical results were available to report.

---

[← 36. Confounding and Multiple Regression](36-confounding-and-multiple-regression.md) · [Contents](index.md) · [38. Fish Tank Multiple Regression →](38-fish-tank-multiple-regression.md)
