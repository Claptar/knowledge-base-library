---
title: "25. Exploring the FEV Dataset"
course: "GTPB Psls20"
chapter: 25
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 25. Exploring the FEV Dataset

## What this covers

This chapter works through a single data-exploration exercise built around one dataset:
measurements of lung function, age, height, gender and smoking status for a group of children. The
question it poses is a modest one — does the data, looked at with nothing more than plots, suggest
that smoking affects how much air a child can forcibly exhale? — and it deliberately stops short of
answering that with a model, since the modelling machinery needed to answer it properly is covered
later in the same week of the course. It assumes the reader can already import a dataset into R,
tell which of its columns should be treated as categorical rather than numeric, and produce a basic
plot; the point of the exercise is the sequence of exploratory decisions, not the code that
implements them.

## The FEV dataset

FEV — forced expiratory volume — is a measure of how much air a person can exhale, in litres,
during a forced breath. The dataset records the FEV of 606 children between the ages of 6 and 17,
along with four other pieces of information about each child: their age, their height, their
gender, and — the variable the whole exercise is organised around — whether they are a smoker or a
non-smoker.

The motivating question is whether smoking has an effect on the FEV of children. Answering that
properly needs a model that can separate the effect of smoking from the effects of the other
recorded variables, and that model is introduced later in the course. Here the task is only to
explore the raw data closely enough to form an expectation of what such a model ought to find.

## Tidying the data before exploring it

Two columns need attention before any plot is worth making.

`gender` and `smoking` arrive as unstructured values but are really categories, not numbers or
free text, so both should be recoded as factors — that is what lets later summaries and plots group
by them rather than treating them as continuous measurements.

`height` is recorded in inches. The exercise's own reasoning for changing this is about the
audience rather than the data: for a mainly Portuguese/Belgian audience, inches are not an
intuitive unit, so a new column, `height_cm`, is added with height converted to centimetres.
Neither recoding changes what the data says — both just put it in a form that is easier to read
and to group by.

## From one plot to a fuller picture

The first plot the exercise asks for is deliberately narrow: show only the FEV values, split by
the two smoking categories, choosing a plot type suited to a continuous measurement broken down by
a two-level category. The exercise does not prescribe which chart to use — that choice, and how
readable and informative the result is, is left to the reader — but it does ask a pointed
follow-up question: did the result match what you expected?

That question sets up the second half of the exercise. The suggestion is that a plot of FEV against
smoking status alone may be misleading — "there is something else going on in the data" — and that
a more accurate picture comes from bringing more of the recorded variables (age, height, gender)
into the same visualization rather than looking at smoking in isolation. The exercise does not say
what that fuller picture turns out to be; it asks the reader to build a visualization that
describes the data as well as possible, using everything that has been recorded, and to judge for
themselves whether it changes the story told by the single-variable plot.

## Exercises

The source poses these as a single guided walkthrough; restated here as discrete tasks, in the
same order, without the code.

1. Load whatever packages are needed to import, tidy and plot a dataset in R, then import the FEV
   dataset and take a first look at it.
2. Decide which of `gender` and `smoking` should be recoded as factors, and recode them.
3. Add a `height_cm` column that expresses height in centimetres instead of inches.
4. Choose a plot type and produce a plot of FEV against smoking status alone. Before looking at it,
   decide what result you expect — then check whether the plot matches that expectation.
5. Using more of the recorded variables (age, height and gender, as well as smoking), produce a
   visualization that gives a more complete account of what is associated with FEV than the
   smoking-only plot did. Aim for the best description of the data you can manage.

## Sources

- Notes: `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_FEV.md`
  (GTPB PSLS20, Tutorial 1.4 "Exploring the FEV dataset", converted from the course's
  `Data_exploration_FEV.Rmd`, CC BY 4.0). No slide deck or lecture transcript was supplied for this
  material — the source is the tutorial exercise sheet itself.
- The code cells in the source are blank template placeholders (`...`), left for the student to
  fill in as part of the exercise; they carry no worked content of their own and so are not
  reproduced here.
- The source's own reference to "all three required steps to analyse such a dataset" — the
  modelling techniques this exploration is a preliminary to — is noted above but is not itself part
  of this material.

---

[← 24. Visualizing Paired Data](24-visualizing-paired-data.md) · [Contents](index.md) · [26. The NHANES Dataset →](26-the-nhanes-dataset.md)
