---
title: "32. Hypothesis Testing: The Shrimps Dataset"
course: "GTPB Psls20"
chapter: 32
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 32. Hypothesis Testing: The Shrimps Dataset

## What this covers

This is a tutorial exercise, not a lecture: it asks you to decide, and carry out, the hypothesis
test for whether a growth condition changes a measured concentration in two independent groups. It
assumes you already have the general machinery of hypothesis testing from earlier in the course —
how to explore a dataset, state a null and alternative hypothesis, pick a test for comparing two
groups, and read the diagnostic plots that check a test's assumptions. What is new here is applying
that machinery to a concrete dataset, PCB concentrations in shrimp adipose tissue, end to end.

## The shrimps dataset

Polychlorinated biphenyls (PCBs) are compounds often present in coolants, and they accumulate
readily in the adipose tissue of shrimps. In this experiment, two groups of 18 shrimp samples (each
of 100 grams) were cultivated under different conditions: one group in a control condition, and the
other in a medium polluted with PCBs. The outcome measured on every sample is the PCB concentration
in the adipose tissue, in picograms per gram (pg/g).

The research question is whether the growth condition — control versus PCB-polluted medium — has an
effect on PCB concentration in the adipose tissue.

## Exercises

Work through the following, building an analysis that weaves together the data exploration, the
plots and the results into a single coherent argument.

1. Explore the data. What do you observe?

2. How will you model the data?

3. Translate the research question into a null hypothesis and an alternative hypothesis.

4. Which test will you use to assess the research hypothesis?

5. State the assumptions of that test, and assess them using diagnostic plots.

6. If the assumptions needed to perform the test hold, complete the analysis and formulate a proper
   conclusion.

## Sources

- Tutorial exercise sheet: *Tutorial 2.3: Hypothesis testing on the shrimps dataset*, GTPB PSLS20,
  `tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_shrimps_half.Rmd`
  (licensed CC BY 4.0). No slides, transcript or worked solution were supplied alongside this
  exercise sheet — the chapter reproduces only the dataset description and the questions as given.

---

[← 31. Hypothesis Testing on the Cuckoo Data](31-hypothesis-testing-on-the-cuckoo-data.md) · [Contents](index.md) · [33. Kruskal-Wallis and Pairwise Wilcoxon Tests →](33-kruskal-wallis-and-pairwise-wilcoxon-tests.md)
