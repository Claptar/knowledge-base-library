---
title: "19. ANOVA on the Lettuce Dataset"
course: "GTPB Psls20"
chapter: 19
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 19. ANOVA on the Lettuce Dataset

## What this covers

This chapter works through a single applied exercise: testing, with a one-way ANOVA, whether soil
treatment affects the growth of lettuce plants in a fertiliser trial. It assumes the reader already
knows what a one-way ANOVA tests — whether the mean of a continuous outcome differs across more
than two groups defined by one categorical factor — since the source is a hands-on tutorial script,
not a theory lecture. The chapter follows the tutorial as far as it goes: setting up the applied
question, loading and preparing the data, and laying out the steps of the analysis. It stops where
the tutorial itself stops, at the point where the student is asked to do the modelling, the
assumption checks and the test.

## The fertiliser trial

Higher crop yield is a persistent goal in agriculture, and for lettuce, plants with more leaves —
or, more precisely, a higher total leaf weight — are what growers and consumers want. One route to
that is fertiliser, and there is a growing preference for natural fertilisers such as compost over
synthetic ones. Near Ghent, an agricultural and fisheries research institute has been testing a
newer natural fertiliser called biochar: a residual product of pyrolysis, the process of burning
biomass under controlled conditions (such as high pressure) to produce energy. Biochar behaves
similarly to charcoal but has some useful extra properties — it helps soil retain water, and it has
a positive effect on the soil microbiome.

The researchers wanted to know whether biochar, compost, or a combination of the two changes how
lettuce plants grow, relative to untreated soil. They grew lettuce in a greenhouse in pots filled
with one of four soil treatments:

1. soil only (control)
2. soil supplemented with biochar (labelled `refoak` in the data)
3. soil supplemented with compost (`compost`)
4. soil supplemented with both biochar and compost (`cobc`)

The response variable is freshweight, in grams, recorded for 28 lettuce plants — 7 under each of
the four treatments, so the design is balanced. Because there are four groups rather than two, the
natural first test is an omnibus one-way ANOVA: does treatment have *any* effect at all, before
asking which specific treatments differ. If the ANOVA says yes, the plan is to follow it with a
post-hoc test (Tukey's test) to work out which pairs of treatments are actually different from each
other.

## Loading and preparing the data

The tutorial's own code loads the data straight from the course's dataset repository and does two
small but necessary pieces of housekeeping before any modelling can happen.

```r
library(tidyverse)

lettuce <- read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/freshweight_lettuce.txt")

glimpse(lettuce)
```

`glimpse` is there to check that the import worked as expected — the right number of rows and
columns, and each column read as a sensible type. That check matters here in particular because
`treatment` is a categorical grouping variable, and `read_csv` has no way of knowing that: left
alone, it will read the treatment labels as plain character strings. R's modelling functions need
the grouping variable encoded as a factor to treat the four labels as group levels rather than as
arbitrary text, so the tutorial converts it explicitly:

```r
lettuce <- lettuce %>%
  mutate(treatment = as.factor(treatment))
```

With that done, a quick tally checks that the design really is balanced as described:

```r
lettuce %>%
  count(treatment)
```

This should return seven plants per treatment; if it does not, that is a sign either the import
went wrong or the trial was not run as described, and either way it changes how the later ANOVA
should be interpreted — an unbalanced design is more sensitive to violations of the equal-variance
assumption than a balanced one.

## Before modelling: look at the data

Before fitting anything, the tutorial asks for a plot of freshweight by treatment — boxplots are
the natural choice for a continuous outcome split by a categorical group — and for that plot to be
interpreted before moving on. That step is worth taking seriously rather than skipping past: a
boxplot gives an informal first look at whether the group medians look different, how much the
groups overlap, and whether the spread of freshweight looks roughly similar across the four
treatments — a rough, visual preview of the homogeneity-of-variance assumption that the formal
ANOVA will need checked properly before its result can be trusted.

## Exercises

Using `lettuce` as prepared above (freshweight in grams for 28 lettuce plants, 7 per treatment:
control, biochar, compost, and biochar-plus-compost):

1. Make a plot of freshweight against treatment and interpret it: do the groups look different,
   and does the spread of freshweight look similar across treatments?
2. Decide how to model these data — what statistical model fits this design of one continuous
   response and one categorical factor with four levels?
3. Translate the research question ("does soil treatment change lettuce growth?") into a statement
   about the parameters of that model.
4. Check whatever assumptions the model chosen in (2) requires before it can be trusted.
5. If those assumptions are satisfied, fit the model.
6. If the model shows an overall treatment effect, follow up with a post-hoc test (Tukey's test) to
   work out which specific treatments differ from each other.

## Sources

- Notes: `ANOVA_lettuce_plants_half.md`, the tutorial exercise script "Tutorial 7.1: ANOVA in the
  lettuce dataset" from GTPB "Practical Statistics for the Life Sciences" (2020) —
  [source](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/07_ANOVA/ANOVA_lettuce_plants_half.Rmd),
  CC BY 4.0. All of the applied motivation, the data-loading code, and the numbered task list above
  come from this script.
- No slide deck and no lecture transcript were supplied for this chapter.
- The dataset file itself, `freshweight_lettuce.txt`, is referenced and loaded by URL in the script
  but was not included in the supplied material, so no actual results, plots, model fit, or test
  outcome appear in this chapter — the source is a "half" version of the tutorial, meant to be
  completed by the student, and the chapter follows it exactly that far.

---

[← 18. One-Way ANOVA on Cuckoo Eggs](18-one-way-anova-on-cuckoo-eggs.md) · [Contents](index.md) · [20. ANOVA on the NHANES Dataset →](20-anova-on-the-nhanes-dataset.md)
