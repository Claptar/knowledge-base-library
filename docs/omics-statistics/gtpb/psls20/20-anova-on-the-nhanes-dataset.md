---
title: "20. ANOVA on the NHANES Dataset"
course: "GTPB Psls20"
chapter: 20
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 20. ANOVA on the NHANES Dataset

## What this covers

This chapter is a single applied exercise, not a new piece of theory: it asks whether systolic
blood pressure differs across categories of self-reported general health in a real survey
dataset, and leaves the reader to set up, check and complete a one-way ANOVA for it. It assumes
the reader already has the machinery from the ANOVA lecture — the F-test for comparing several
group means, and the assumptions of normality and constant variance within groups that make
the test valid — and is now being asked to apply that machinery to data that may not cooperate.

## The dataset

The exercise uses NHANES, the National Health and Nutrition Examination Survey, which has
collected physical, demographic, nutritional and life-style data on the U.S. population since
1960. The slice used here is the cycle collected between 2009 and 2012, covering about 10,000
civilians.

Two columns of that dataset are relevant:

- `HealthGen` — a participant's self-reported general health, recorded only for participants
  aged 12 or older, as a factor with five ordered levels: Excellent, Vgood, Good, Fair, Poor.
- `BPSys1` — a measured systolic blood pressure value.

## The question

The research question is whether mean systolic blood pressure (`BPSys1`) is the same across the
five self-reported health categories (`HealthGen`). This is exactly the shape of question ANOVA
is for: one continuous response, one categorical explanatory variable with more than two levels,
and a comparison of means across the groups it defines — to be carried out only if the
assumptions the test needs turn out to hold.

## Exercises

The dataset needs some preparation before the comparison can be made. Before answering the
questions below:

- Filter out subjects with missing (`NA`) values for `HealthGen` or `BPSys1`.
- Set `HealthGen` to a factor and relevel it from Poor through Excellent, so that plots and
  output display the categories in their natural order rather than alphabetically.

Then, working from a plot of `BPSys1` against `HealthGen`:

1. What do you observe from the data exploration?
2. How will you model the data?
3. Translate the research question into a null and an alternative hypothesis.
4. Which test will you use to assess the research hypothesis?
5. Formulate the assumptions of the test, and assess them using diagnostic plots.
6. If all the assumptions needed to perform the test are met, complete the analysis and
   formulate a proper conclusion. If the assumptions are not met, can you think of concepts
   discussed in the theory that could be used to tackle this issue?

## Sources

- Notes: `tutorialScripts/excercises/07_ANOVA/ANOVA_NHANES_half.md` (GTPB PSLS20, CC BY 4.0) —
  the full content of this chapter. The source is an R Markdown exercise sheet with the code
  chunks left blank for the student to fill in (a "half" version); no worked solution or
  numerical answer is supplied, so none is given here.
- No slides or transcript accompanied this tutorial in the supplied material.

---

[← 19. ANOVA on the Lettuce Dataset](19-anova-on-the-lettuce-dataset.md) · [Contents](index.md) · [21. One-Way ANOVA Worked Example →](21-one-way-anova-worked-example.md)
