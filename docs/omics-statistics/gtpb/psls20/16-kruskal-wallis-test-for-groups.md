---
title: "16. Kruskal-Wallis Test for Groups"
course: "GTPB Psls20"
chapter: 16
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Kruskal-Wallis Test for Groups

## What this covers

This chapter sets up a practical exercise on comparing more than two groups when the assumptions
behind ANOVA cannot be relied on. It assumes the reader already has one-way ANOVA and the idea of a
hypothesis test in hand, and is meeting the rank-based alternative — the Kruskal-Wallis test — as
something to *apply* to a real dataset rather than to derive. The source material for this chapter
is the exercise brief itself; the worked solution and the test's mechanics live in a linked notebook
that was not supplied (see Sources).

## The setting: does fertilizer type affect lettuce growth?

The exercise is framed around a question from agriculture: growers want a high yield of crops, and
one route to more leaf weight is fertilizer. The study compares three fertilizer-related treatments:

- **biochar**
- **compost**
- **cobc** — a combination of biochar and compost

To test whether any of these help, researchers grew lettuce plants in a greenhouse, with pots filled
with one of four soil types:

- soil only (**control**)
- soil supplemented with biochar (**refoak**)
- soil supplemented with compost (**compost**)
- soil supplemented with both biochar and compost (**cobc**)

This gives a **one-way, four-group design**: a single factor (soil treatment) with four levels, and
the response is the freshweight of the lettuce plant. The dataset, `freshweight_lettuce.txt`,
records the freshweight of 28 lettuce plants across the four groups.

## Why Kruskal-Wallis rather than ANOVA

The exercise is explicitly placed under "non-parametric, multigroup analysis." A one-way ANOVA
answers the same kind of question — does the group mean differ across more than two groups? — but
it leans on assumptions (normally distributed residuals, equal variances) that a small dataset like
this one may not support. The Kruskal-Wallis test is the rank-based analogue: it asks whether the
four groups' *distributions* differ, using the ranks of the freshweight values rather than the raw
measurements, and so does not require normality. The exercise gives the practical motivation for
reaching for it — a four-group comparison on a modest sample — without walking through the test
statistic's construction; that derivation is not part of the supplied material.

## The research question

The concrete question the researchers want answered is whether **one or more of the treatments**
(refoak, compost, cobc) shifts lettuce growth relative to control — i.e., whether soil treatment has
any effect at all on freshweight, before asking which treatment is responsible.

## Exercises

Working from the `freshweight_lettuce.txt` dataset (28 lettuce plants, one of four soil treatments
each: control, refoak, compost, cobc):

1. State the null and alternative hypotheses for testing whether soil treatment affects lettuce
   freshweight.
2. Explain why a rank-based test such as Kruskal-Wallis is a reasonable choice for this design and
   sample size, rather than a one-way ANOVA.
3. Carry out the Kruskal-Wallis test on the four groups and state your conclusion about whether the
   treatments affect growth.

## Sources

- Notes: `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/09_kruskalWallis/09_kruskalWallis.md`
  (GTPB "Practical Statistics for the Life Sciences" 2020, day 3, non-parametric multigroup exercise).
- Referred to but not supplied as input: the worked exercise notebook
  `Kruskal_Wallis_lettuce_plants_half.html` and the data file `freshweight_lettuce.txt`, both linked
  from the notes but not included in the material given for this chapter.

---

[← 15. Wilcoxon-Mann-Whitney Rank Test](15-wilcoxon-mann-whitney-rank-test.md) · [Contents](index.md) · [17. Categorical Data Analysis →](17-categorical-data-analysis.md)
