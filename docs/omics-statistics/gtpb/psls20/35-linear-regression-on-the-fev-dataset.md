---
title: "35. Linear Regression on the FEV Dataset"
course: "GTPB Psls20"
chapter: 35
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 35. Linear Regression on the FEV Dataset

## What this covers

This chapter is a linear-regression exercise built on the FEV dataset: measurements of lung
function, age, height, gender and smoking status for 606 children. It reintroduces the same
dataset used to ask whether smoking affects lung function, then shows why that question cannot yet
be answered directly with a straight line through one predictor, and what narrower questions can be
asked instead while the necessary tool — multiple regression — waits for a later tutorial. It
assumes the reader can already fit and interpret a simple linear regression: check its assumptions,
read off and interpret an intercept and a slope, and test a hypothesis about the slope.

## The FEV dataset, again

FEV — forced expiratory volume — is a measure of how much air a person can exhale, in litres,
during a forced breath. The dataset records the FEV of 606 children between the ages of 6 and 17,
together with each child's `age`, `height`, `gender`, and whether they are a smoker or a
non-smoker. The overarching goal of the experiment is to find out whether or not smoking has an
effect on the FEV of children.

Two columns need attention before any model is fit to them. `gender` and `smoking` should be
recoded as factors rather than left as unstructured values, so that later summaries and models
group by them instead of treating them as free text or numbers. `height` is recorded in inches;
the exercise adds a second column, `height_cm`, converting to centimetres — reasoning that, for a
mainly Portuguese/Belgian audience, inches are not an intuitive unit. Neither change touches what
the data says, only how easy it is to read and to group by.

## Looking before modelling

Before fitting anything, the exercise asks for a plot of FEV split only by smoking status, and a
pointed question: did you expect this result, and can you explain what you observe? It then asks
for something more ambitious — a visualization that brings in more of the recorded variables
(age, height, gender) alongside smoking — and leaves open whether that richer picture changes the
story the single-variable plot told.

## Why not just regress FEV on smoking

Answering the overarching question properly means separating the effect of smoking from the
effects of age, height and gender, all at once — that is a model with several predictors, and the
tools for fitting one have not been covered yet. As the exercise puts it, that model is taken up
"in the tutorial on multiple regression," and the analysis returns to this dataset there.

In the meantime, four smaller questions are within reach, each involving only one predictor:

1. Is there a linear association between FEV and height, among non-smoking females?
2. Is there a linear association between FEV and age, among non-smoking females?
3. Is there a linear association between FEV and height, among non-smoking males?
4. Is there a linear association between FEV and age, among non-smoking males?

Restricting every question to non-smokers removes smoking status as a variable that could be
entangled with the height–FEV or age–FEV relationship; splitting the remaining children by gender
does the same for gender. What is left in each case is a single predictor and a single outcome,
measured within a group that is otherwise as uniform as the recorded variables allow — exactly the
setting a simple linear regression is built to handle, even though it cannot yet handle the
original three-or-four-predictor question.

## What each of the four analyses has to produce

The exercise lays out the same three-part recipe for all four questions:

1. Check the assumptions of the linear model, and analyse the data accordingly — that is, let what
   the checks show determine how the analysis proceeds, rather than fitting the model regardless.
2. Interpret the output, with particular attention to what the intercept and the slope mean in
   terms of FEV, height or age, and the group being studied.
3. Formulate a conclusion for the research hypothesis that question was asking about.

Only the predictor (height or age) and the subgroup (non-smoking females or non-smoking males)
change between the four; the recipe for going from data to conclusion is the same each time.

## Exercises

The source poses these as one guided script with blank code cells; restated here as discrete
tasks, in the same order, without the code.

1. Import the FEV dataset.
2. Decide which of `gender` and `smoking` should be recoded as factors, and recode them. Add a
   `height_cm` column expressing height in centimetres instead of inches.
3. Plot FEV against smoking status alone. Before looking at the result, decide what you expect it
   to show, then check whether it matches — and try to explain what you see.
4. Build a fuller visualization of the data that brings in age, height and gender as well as
   smoking, and judge whether it gives a more complete account of what is associated with FEV than
   the smoking-only plot did.
5. Restrict the data to non-smoking females. Check the assumptions of a linear model relating FEV
   to height in this group, fit the model, interpret the intercept and the slope, and state a
   conclusion about whether FEV and height are linearly associated.
6. Within the same non-smoking females, repeat exercise 5 with `age` in place of `height`.
7. Restrict the data to non-smoking males and repeat exercise 5 (FEV against height).
8. Within the same non-smoking males, repeat exercise 6 (FEV against age).

## Sources

- Notes: `tutorialScripts/excercises/06_linearRegression/Linreg_FEV_halfRmd/01-the-fev-dataset.md`
  and `.../02-analysis.md` (GTPB PSLS20, Tutorial 6.2 "Linear regression on the FEV dataset",
  converted from the course's `Linreg_FEV_halfRmd.Rmd`, CC BY 4.0).
- The code cells in the source are blank template placeholders, left for the student to fill in;
  they carry no worked content of their own and so are not reproduced here.
- No slide deck or lecture transcript was supplied for this material — the source is the tutorial
  exercise sheet itself, split into its two constituent pages.
- The source's own forward reference to "the tutorial on multiple regression," where the analysis
  "come[s] back to this dataset" to answer the smoking question properly, points to material not
  supplied here.

---

[← 34. Linear Regression on Fish Survival](34-linear-regression-on-fish-survival.md) · [Contents](index.md) · [36. Confounding and Multiple Regression →](36-confounding-and-multiple-regression.md)
