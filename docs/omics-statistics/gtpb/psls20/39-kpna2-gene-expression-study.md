---
title: "39. KPNA2 Gene Expression Study"
course: "GTPB Psls20"
chapter: 39
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 39. KPNA2 Gene Expression Study

## What this covers

This chapter works through a single applied exercise: does the expression of the *KPNA2* gene in
breast tumours depend on histologic grade and on lymph-node status, and does the grade effect look
different in the two node groups? It assumes you can already fit and read off a multiple linear
regression with categorical predictors, including a model containing an interaction term — the
exercise is the application of that machinery to a real dataset, not an introduction to it.

## The study

Histologic grade is an established prognostic marker in breast cancer. The tutorial's own framing
is that researchers wanted to know whether histologic grade is reflected in gene expression, and
whether expression profiles could in turn be used to sharpen histologic grading. The gene singled
out here is *KPNA2*, which is known to be associated with poor prognosis in breast cancer.

The patients in the dataset are not classified on grade alone: each patient is also recorded as
having lymph nodes that were either unaffected (coded `0`) or surgically removed (coded `1`). So
there are two categorical factors in play, not one, and the tutorial's own hint is that they may
not act independently: it explicitly raises the possibility that "the differential expression
associated with histological grade is different in patients that have unaffected lymph nodes and
patients for which the lymph nodes had to be removed" — that is, an interaction between grade and
node status, on top of whatever main effects either has on its own.

## The data

The dataset (`kpna2.txt`) is read directly from the course repository as a tab-separated file. It
records, per patient, the *KPNA2* expression measurement together with histologic grade and node
status. Grade and node are stored as numeric codes in the raw file, so the first step the source
calls for is converting both to factors before they are used in a model — otherwise R would treat
them as ordinary numbers rather than groups.

The source's own next step is a graphical exploration of the data before any model is fit — a plot
that should show whether grade and node status look associated with expression at all, and whether
the association with grade looks different across the two node groups. The source leaves this plot
itself as an empty code cell for the reader to produce; nothing in the material says what the plot
actually shows, so no reading of it is given here either.

## Setting up the model

Because the design has two categorical factors and the study explicitly asks whether one factor's
effect depends on the level of the other, the model to specify has to be able to represent three
things at once: a main effect of grade, a main effect of node status, and — if the data support it
— an interaction between the two, capturing exactly the "effect modification" the background
paragraph describes. Deciding which of those terms belong in the model, and what each fitted
parameter then means in terms of *KPNA2* expression, grade and node status, is the first task below.

## Exercises

Based on `multipleRegression_KPNA2_half.md`, GTPB PSLS20, exercise 3 ("Breastcancer Gene Expression
Study: KPNA2 gene").

1. Import the `kpna2` dataset and convert the `grade` and `node` variables to factors.
2. Explore the data graphically. Does the plot suggest an association between *KPNA2* expression
   and grade, between expression and node status, and does the grade effect look different between
   the two node groups?
3. Specify a multiple regression model for *KPNA2* expression in terms of grade and node status,
   and interpret each parameter of the model.
4. Formulate the research questions this study is asking.
5. Translate each research question into a null and an alternative hypothesis, carry out the
   corresponding hypothesis tests, and calculate the relevant confidence intervals.
6. State your conclusions in terms of the original research question.

## Sources

- `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/08_multipleRegression/multipleRegression_KPNA2_half.md`
  — the sole input for this chapter. It is a converted tutorial exercise (CC BY 4.0, from the GTPB
  PSLS20 course repository, `08_multipleRegression/multipleRegression_KPNA2_half.Rmd`), not a
  lecture: there is no accompanying slide deck or transcript for this item, and the file itself is
  the "half" version of the tutorial — a template with some R code already filled in (the data
  import) and other cells left blank for the reader to complete (converting variables to factors,
  producing the exploratory plot, fitting the model).
- The general multiple-regression machinery this exercise applies — how to specify a model with
  categorical predictors and an interaction term, and how to read off and test its parameters — is
  assumed prior knowledge from earlier in the course's multiple-regression material, which was not
  supplied as input to this chapter.

---

[← 38. Fish Tank Multiple Regression](38-fish-tank-multiple-regression.md) · [Contents](index.md) · [40. Base R Cheat Sheet →](40-base-r-cheat-sheet.md)
