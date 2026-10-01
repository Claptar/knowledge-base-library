---
title: "18. One-Way ANOVA on Cuckoo Eggs"
course: "GTPB Psls20"
chapter: 18
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. One-Way ANOVA on Cuckoo Eggs

## What this covers

This chapter walks through a tutorial exercise: testing whether the average length of a common
cuckoo's egg depends on which bird species raised it. It assumes you already know how one-way
ANOVA works — that it partitions the variability in a measurement into a between-group and a
within-group component and tests whether the group means could plausibly be equal — and that you
have already compared two of these groups directly with a t-test. What this tutorial adds is the
step from *two* groups to *several at once*, and the discipline of checking a test's assumptions
before trusting its conclusion.

## Background: a bird that outsources its eggs

The common cuckoo does not build a nest of its own. Instead it lays its eggs in the nest of another
bird species, which then raises the cuckoo chick as if it were its own. This has been known since
1892, and a 1940 study showed something more specific: individual cuckoos return to the same
nesting area year after year, and each one always lays in nests belonging to the same host species
— its "foster parent."

Because a host bird is more likely to reject an egg that looks obviously foreign, this repeated
pairing between a cuckoo lineage and a host species has, over many generations, produced
geographically distinct cuckoo subspecies whose eggs have evolved to resemble those of their
particular foster parent as closely as possible. Egg length is one of the traits this mimicry could
act on.

## The dataset

The cuckoo dataset records, for 120 cuckoo eggs collected from randomly selected foster nests, two
variables:

- `length` — the egg's length, in mm
- `type` — the species of the foster parent, coded 1 through 6:

| Code | Foster species |
|---|---|
| 1 | Meadow pipit |
| 2 | Tree pipit |
| 3 | Dunnock |
| 4 | European robin |
| 5 | White wagtail |
| 6 | Eurasian wren |

`type` is a categorical variable stored as a number, so before it can be used as a grouping factor
in the analysis it has to be converted to a proper factor — otherwise a statistical package will
happily treat "1", "2", ... "6" as a quantity to average rather than as six separate labels.

## From one pair to all six groups

A companion tutorial asked the narrower question: is the average egg length in nests of the
European robin different from the average in nests of the Eurasian wren, answered with a two-sample
t-test. The question here is broader — does foster-parent species affect egg length *at all*,
across all six species simultaneously — and a t-test does not extend to that directly: running a
t-test on every pair of the six groups would mean six group means compared three ways at a time
across fifteen pairs, inflating the chance of a false positive well past the nominal significance
level. One-way ANOVA is the tool built for exactly this case: one categorical factor with more than
two levels, one continuous response, and a single test of whether all the group means are equal.

## The workflow the tutorial follows

The exercise is structured as a sequence of steps, each meant to be carried out and thought about
before moving to the next:

1. **Import the data** and look at its structure.
2. **Tidy it** — in particular, set `type` to a factor rather than a numeric code, so that later
   steps treat it as six groups rather than as a measurement.
3. **Explore it**: count how many eggs were recorded for each of the six foster species (an
   unbalanced design, with very different group sizes, behaves differently from a balanced one),
   and visualise the distribution of `length` within each group — for instance with boxplots or
   jittered points by `type`.
4. **State the model and the hypotheses.** Egg length is modelled as a group mean plus noise, one
   mean per foster species; the null hypothesis is that all six group means are equal, and the
   alternative is that at least one differs.
5. **Choose the test** — one-way ANOVA — and **state its assumptions** before applying it:
   independence of the observations, approximate normality of the residuals within each group, and
   roughly equal variance across groups. These are checked with diagnostic plots (e.g. a
   quantile-quantile plot of the residuals, and a plot of residuals against fitted group means),
   not assumed for free.
6. **Only if the assumptions hold**, run the test and translate the result back into a substantive
   conclusion about whether foster-parent species affects cuckoo egg length — and note what should
   be tried instead if an assumption fails.

## Exercises

Working from the cuckoo dataset described above (`length` in mm, `type` coded 1–6 as the six
foster-parent species):

1. Tabulate how many eggs were recorded for each of the six foster-parent species, and visualise
   the distribution of egg length within each group. What do you observe?
2. What statistical model is appropriate for this data?
3. Translate the researchers' question — does foster-parent species affect the average length of
   cuckoo eggs? — into a precise null and alternative hypothesis.
4. Which test should be used to assess this hypothesis, and why does the earlier pairwise t-test
   not suffice here?
5. State the assumptions required for that test, and assess each one using appropriate diagnostic
   plots.
6. If the assumptions hold, carry out the complete analysis and state a conclusion in terms of the
   original research question. If an assumption fails, say what you would do differently.

## Sources

- Tutorial notes: `tutorialScripts/excercises/07_ANOVA/ANOVA_cuckoo_half.Rmd` (GTPB PSLS20 course,
  Tutorial 7.2, "ANOVA on the cuckoo dataset") — the dataset description, the variable coding table,
  the stated goal, the six numbered exercise questions, and the section headings for the workflow
  (load libraries, import data, data exploration, data tidying, visualisation) all come from this
  file.
- The file's own code chunks for loading libraries, importing the data, exploring it, and
  visualising it are left blank in the source — they are the student's task to fill in, not
  material the lecture supplied, so no R code is reproduced here.
- No slide deck or lecture transcript was supplied for this tutorial. The one-way ANOVA theory this
  exercise applies (partitioning of variance, the F-test, the assumptions of independence,
  normality and homogeneity of variance) and the earlier pairwise t-test on the European robin and
  Eurasian wren groups that this tutorial extends are both referred to in the source but not
  contained in it.

---

[← 17. Categorical Data Analysis](17-categorical-data-analysis.md) · [Contents](index.md) · [19. ANOVA on the Lettuce Dataset →](19-anova-on-the-lettuce-dataset.md)
