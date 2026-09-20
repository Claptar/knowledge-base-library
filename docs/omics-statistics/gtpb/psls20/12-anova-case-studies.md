---
title: "12. ANOVA Case Studies"
course: "GTPB Psls20"
chapter: 12
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. ANOVA Case Studies

## What this covers

This chapter introduces three real datasets that the course used as case studies for one-way
ANOVA: a fertiliser trial on lettuce, a survey of cuckoo egg lengths across different foster-parent
bird species, and a national health survey. It assumes the reader already knows what a one-way
ANOVA tests — whether the mean of a continuous response differs across more than two groups defined
by a single categorical factor — since the supplied material only sets up the applied question each
dataset was meant to answer. The mechanics of the test itself, and the assumption checks that go
with it, were left to tutorial scripts that were not part of the supplied material (see Sources).

## Three studies, one question

All three studies share the same underlying structure: a continuous outcome measured on a number of
individuals, and a categorical grouping factor with more than two levels. That is exactly the
setting a one-way ANOVA is built for — asking whether the group means could plausibly be equal,
rather than comparing just two groups at a time as a $t$-test would.

### The lettuce freshweight dataset

The applied motivation is agricultural: a higher yield of crops, here measured as total leaf
weight, is desirable, and one route to it is fertiliser. The study compares three fertiliser
treatments — biochar, compost, and a combination of the two ("cobc") — against an untreated soil
control, so the grouping factor has four levels:

- soil only (control)
- soil supplemented with biochar (refoak)
- soil supplemented with compost (compost)
- soil supplemented with both biochar and compost (cobc)

The dataset `freshweight_lettuce.txt` records the freshweight of 28 lettuce plants grown under
these four soil treatments. The question the researchers want answered is whether one or more of
the treatments has an effect on the growth of lettuce plants — the standard "is there any group
difference at all" question a one-way ANOVA is designed to answer before any pairwise comparison is
attempted.

### The cuckoo egg dataset

The common cuckoo does not build its own nest — it lays its eggs in another bird species' nest,
relying on that species to raise its young. It has been known since 1892 that the type of cuckoo
egg differs by location, and a 1940 study showed why: cuckoos return to the same nesting area every
year and always pick the same foster species. Over generations this produced geographically
distinct cuckoo subspecies whose eggs have evolved to resemble those of their particular foster
species as closely as possible.

The dataset contains measurements on 120 cuckoo eggs, collected from randomly selected foster
nests. The question is whether the type of foster parent has an effect on the average length of the
cuckoo eggs laid in its nest — again a comparison of means across more than two groups (one per
foster species), which is why the design calls for ANOVA rather than a two-sample test.

### The NHANES blood pressure dataset

The National Health and Nutrition Examination Survey (NHANES) has collected data on the US
population since 1960. The tutorial uses the 2009–2012 wave, covering around 10,000 US civilians,
which records a large number of physical, demographic, nutritional and lifestyle variables.

The question posed here is whether mean systolic blood pressure (the column `BPSys1`) is equal
across the five self-reported health categories, "if the required assumptions are met" — the source
is explicit that checking the ANOVA assumptions is a prerequisite step before the test is applied
here, in a way it does not spell out for the other two datasets.

## Exercises

1. **Lettuce freshweight.** Using `freshweight_lettuce.txt` (freshweight of 28 lettuce plants,
   grown under four soil treatments: control, biochar, compost, and biochar-plus-compost), test
   whether one or more of the three fertiliser treatments has an effect on the growth of the
   plants relative to the control.
2. **Cuckoo eggs.** Using the cuckoo egg dataset (lengths of 120 eggs collected from the nests of
   different foster-parent bird species), test whether the type of foster parent has an effect on
   the average length of the cuckoo eggs.
3. **NHANES blood pressure.** Using the NHANES 2009–2012 data (systolic blood pressure, column
   `BPSys1`, for around 10,000 US civilians), first check whether the assumptions required for an
   ANOVA are met, then test whether mean systolic blood pressure is equal across the five
   self-reported health categories.

## Sources

- Notes: `07_ANOVA.md`, the tutorial overview page for day three of GTPB "Practical Statistics for
  the Life Sciences" (2020) —
  [source](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/07_ANOVA.md),
  CC BY 4.0. All three case-study descriptions above, including the cuckoo natural-history
  background and the NHANES description, come from this page.
- No slide deck and no lecture transcript were supplied for this chapter; the page above is itself
  a tutorial index, not a worked lecture.
- The page links out to three worked exercise scripts — `ANOVA_lettuce_plants_half.Rmd`,
  `ANOVA_cuckoo_half.Rmd`, and `ANOVA_NHANES_half.Rmd` — and their underlying data files
  (`freshweight_lettuce.txt`, `Cuckoo.txt`, `NHANES.csv`). These were referred to by the source but
  not included in the supplied material, so the actual ANOVA model, $F$-test and assumption checks
  (e.g. normality of residuals, homogeneity of variance) are not covered in this chapter.

---

[← 11. One-Way ANOVA and Post-Hoc Tests](11-one-way-anova-and-post-hoc-tests.md) · [Contents](index.md) · [13. Multiple Linear Regression →](13-multiple-linear-regression.md)
