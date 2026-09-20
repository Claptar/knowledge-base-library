---
title: "31. Hypothesis Testing on the Cuckoo Data"
course: "GTPB Psls20"
chapter: 31
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 31. Hypothesis Testing on the Cuckoo Data

## What this covers

This chapter works through a single tutorial exercise: a hypothesis test comparing the length of
cuckoo eggs raised by two different host ("foster") species. It assumes the reader already has the
two-sample $t$-test — its null and alternative hypotheses, its assumptions, and how to read a
diagnostic plot for them — since that machinery is what the exercise asks you to apply, not what it
teaches. What this tutorial adds is the practical step in between: deciding *which* test question a
multi-group dataset actually poses, and preparing the data so that the test is testing what you
think it is.

## The cuckoo dataset

The common cuckoo does not build its own nest. It lays its eggs in another bird's nest and lets
that species raise the chick. This has been known since 1892, and a 1940 study showed something
more specific: a cuckoo returns to the same nesting area every year and always parasitises the same
foster species. Over generations this produced geographically distinct cuckoo subspecies, each with
eggs that mimic the eggs of *their* particular foster species as closely as possible.

The dataset records 120 cuckoo eggs, sampled from randomly selected foster nests. For each egg it
gives:

- `length` — the egg length, in mm
- `type` — the foster species, coded `1`–`6`: meadow pipit, tree pipit, dunnock, European robin,
  white wagtail, Eurasian wren

The research question is whether the foster species has an effect on egg length — consistent with
the mimicry story above, different foster species should be associated with different mean egg
lengths.

## One test, or many?

A $t$-test compares the means of exactly two groups. Here there are six. Two ways to get from "six
groups" down to something a $t$-test can answer:

1. **Run every pairwise comparison.** Six groups give $\binom{6}{2} = 15$ pairs, so 15 separate
   $t$-tests.
2. **Run a single ANOVA** across all six groups at once.

The tutorial notes that the second approach is more efficient and has higher statistical power, and
defers it to the chapter on ANOVA. This exercise instead does the simplest possible version of
option 1: a single pairwise comparison, between the European robin (`type=4`) and the Eurasian wren
(`type=6`), leaving the full six-group analysis to a later tutorial on the same dataset.

## Preparing the comparison

Two things have to happen to the raw data before a two-sample test makes sense on it.

**Subsetting.** Since only the robin/wren comparison is being made, every other foster type is
filtered out:

```r
Cuckoo <- Cuckoo %>%
  filter(type %in% c("4","6")) %>%
  mutate(type = as.factor(type))
```

**Recoding `type` as a factor.** The `type` column is stored as the numeric codes `1`–`6`, but it
does not represent a quantity — it names a species. Left as a number, software would treat `type=6`
as three times `type=2`, which is meaningless here; a two-sample test needs it as a categorical
grouping variable with exactly two levels, `4` and `6`. Hence the explicit `as.factor(type)` above.

With the data subset and `type` correctly typed, the tutorial then asks you to check the group
sizes (how many robin eggs, how many wren eggs) and to look at the distribution of `length` in each
group before running any test — the usual order of operations: explore first, then test.

## Exercises

Using the two-group cuckoo subset above (European robin, `type=4`, vs Eurasian wren, `type=6`):

1. What do you observe, having tabulated the group sizes and visualised the two distributions of
   egg `length`?
2. How will you model the data?
3. Translate the research question into a null and an alternative hypothesis.
4. Which test will you use to assess the research hypothesis?
5. Formulate the assumptions of the test, and assess them using diagnostic plots.
6. If the assumptions for the test hold, complete the analysis and formulate a proper conclusion.

## Sources

- Tutorial exercise sheet: *Tutorial 2.4: Hypothesis testing on the cuckoo dataset*, GTPB PSLS20,
  `tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_cuckoo_half.Rmd` (converted
  copy at `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/05_statisticalInference/Hypothesis_testing_cuckoo_half.md`
  in the knowledge-base-library).
- No slide deck or lecture transcript was supplied for this tutorial; the code chunks for loading
  libraries, importing the data, the first data-exploration step, and the visualisation step are
  blank in the source (left for the student to fill in), so they are not reproduced here as worked
  code. The ANOVA treatment of all six foster species that this tutorial defers to is likewise not
  contained in this source and is not covered in this chapter.

---

[← 30. One-Sample and Paired t-Tests](30-one-sample-and-paired-t-tests.md) · [Contents](index.md) · [32. Hypothesis Testing: The Shrimps Dataset →](32-hypothesis-testing-the-shrimps-dataset.md)
