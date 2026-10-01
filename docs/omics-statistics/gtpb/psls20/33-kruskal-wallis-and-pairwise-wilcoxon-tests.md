---
title: "33. Kruskal-Wallis and Pairwise Wilcoxon Tests"
course: "GTPB Psls20"
chapter: 33
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 33. Kruskal-Wallis and Pairwise Wilcoxon Tests

## What this covers

This chapter works through a single lab exercise: re-analysing a dataset on lettuce growth,
previously analysed with a one-way ANOVA, using the Kruskal-Wallis test, followed by a post-hoc
pairwise comparison. It assumes you already know what the Kruskal-Wallis test is and why it is the
rank-based counterpart to one-way ANOVA, what the Wilcoxon rank-sum test and its "probabilistic
index" interpretation are, and how to correct a family of p-values for multiple testing (e.g. with
the Bonferroni method) — none of that machinery is derived here, only applied. It also assumes the
earlier ANOVA analysis of the same dataset, referred to in the source material as "chapter 7".

## The lettuce experiment

A greenhouse experiment grew lettuce plants in four soil conditions:

1. soil only (control),
2. soil with biochar (`refoak`),
3. soil with compost (`compost`),
4. soil with both biochar and compost (`cobc`).

Seven plants were grown per condition, 28 in total, and the response recorded is each plant's fresh
weight in grams. The dataset (`freshweight_lettuce.txt`) has one row per plant and is read directly
from the course's repository. The original question — does any treatment change lettuce growth,
and if so, which one — was addressed in an earlier tutorial with a one-way ANOVA followed by a
Tukey post-hoc test.

## Why redo it without ANOVA

A one-way ANOVA rests on its residuals being approximately normal with equal variance across the
four groups. With only seven values per group there is very little basis for judging whether either
assumption actually holds: a departure from normality in a sample of seven is nearly impossible to
tell apart from ordinary sampling variation. The Kruskal-Wallis test sidesteps this — it works on
the ranks of the freshweights rather than the raw values, and is the standard alternative to
one-way ANOVA when the ANOVA assumptions cannot be established.

## Structure of the analysis

The exercise follows the same shape as the earlier ANOVA one:

- import the data and inspect it (`glimpse`),
- tidy it — in particular, make sure `treatment` is stored as a factor with the right four levels,
- explore it — count the observations per treatment and plot freshweight by treatment as a boxplot,
- state the hypotheses the Kruskal-Wallis test is testing here,
- run the test and interpret the result.

## Post-hoc: which treatments differ

A significant Kruskal-Wallis result only says that the four treatments are not all identical; it
does not say which ones differ. The follow-up here is a **pairwise Wilcoxon rank-sum test**, run
once for each of the six pairs of treatments. Because six tests are being read together rather than
one, the resulting p-values need to be corrected for multiple testing (Bonferroni, via
`p.adjust()`) before they are interpreted.

One way to get there, and the way the tutorial's own code builds it, is to enumerate the pairs
directly:

```r
treatments <- levels(lettuce$treatment)
freshweight <- lettuce$freshweight

pvalues <- combn(treatments, 2, function(x){
  test <- wilcox_test(freshweight ~ treatment,
                       subset(lettuce, treatment %in% x),
                       distribution = 'exact')
  pvalue(test)
})

pvalues_bonf <- p.adjust(pvalues, method = 'bonferroni')
names(pvalues_bonf) <- combn(levels(lettuce$treatment), 2, paste, collapse = "_VS_")
pvalues_bonf
```

`combn(treatments, 2, ...)` walks through all $\binom{4}{2} = 6$ unordered pairs of treatments,
runs an exact Wilcoxon test on each pair's subset of the data, and collects the six p-values before
they are Bonferroni-adjusted and labelled by which two treatments they compare.

As the analysis does not assume a location shift between two treatments, the tutorial has us read
the result as a probabilistic index instead, rather than as a difference in location.

## Exercises

These are the tasks the tutorial sets, in order; none is solved here.

1. **Data preparation.** Load `tidyverse`, read `freshweight_lettuce.txt` into `lettuce`, and check
   its structure with `glimpse()`. Convert the `treatment` column to a factor. Count how many
   observations there are per treatment, and produce a boxplot of `freshweight` by `treatment`.
   What does the boxplot suggest about the four treatments?

2. **Kruskal-Wallis test.** State a correct null and alternative hypothesis for the Kruskal-Wallis
   test on this dataset. Run the test (e.g. with `kruskal_test()`) and interpret the result.

3. **Post-hoc hypotheses.** State a correct null and alternative hypothesis for the pairwise
   Wilcoxon post-hoc analysis.

4. **Post-hoc test.** Run the pairwise Wilcoxon rank-sum test across the four treatments
   (`pairwise.wilcox.test()`, or the pair-by-pair construction shown above), correcting the
   resulting p-values for multiple testing. What do you observe?

5. **Effect size.** From the analysis above, extract the point estimates of the probabilistic
   index for each pair of treatments, and interpret them.

6. **Conclusion.** Write a conclusion that answers the researchers' original question: does
   biochar, compost, or their combination affect lettuce growth, and if so, how?

## Sources

- Both sections are drawn from the converted tutorial script `Kruskal_Wallis_lettuce_plants_half.Rmd`
  (GTPB PSLS20, licensed CC BY 4.0):
  - Background, dataset description and the Kruskal-Wallis exercise:
    [`01-introduction.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd)
  - Post-hoc pairwise Wilcoxon exercise:
    [`02-post-hoc-analysis.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/09_kruskalWallis/Kruskal_Wallis_lettuce_plants_half.Rmd)
- No slides or lecture transcript were supplied for this chapter.
- The source refers to an earlier ANOVA analysis of the same dataset ("chapter 7",
  `ANOVA_lettuce_plants_half.rmd`), which was not among the supplied inputs.

---

[← 32. Hypothesis Testing: The Shrimps Dataset](32-hypothesis-testing-the-shrimps-dataset.md) · [Contents](index.md) · [34. Linear Regression on Fish Survival →](34-linear-regression-on-fish-survival.md)
