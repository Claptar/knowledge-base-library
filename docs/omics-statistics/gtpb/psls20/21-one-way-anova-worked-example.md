---
title: "21. One-Way ANOVA Worked Example"
course: "GTPB Psls20"
chapter: 21
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 21. One-Way ANOVA Worked Example

## What this covers

This chapter works through a single worked example of one-way analysis of variance (ANOVA):
does the dose of arachidonic acid given to rats change the mean level of prostacyclin in their
blood plasma? It assumes you can already fit a linear model in R with `lm()` and read a p-value
off it, and shows what changes when the explanatory variable has three groups instead of two, so
that a two-sample $t$-test no longer answers the question by itself.

## The experiment

Researchers gave each of 36 rats one of three doses of arachidonic acid — low, medium or high —
with 12 rats per dose, and measured the resulting prostacyclin concentration in blood plasma with
a fluorescence assay (ELOSA). This is a single factor, `dose`, with three levels; each rat
contributes one measurement, so the data are three independent groups of size 12 to be compared.

## Checking the model before testing it

Before any test, the data are plotted two ways: a boxplot of prostacyclin concentration by dose
group, with the individual measurements jittered on top, and a QQ-plot of the measurements within
each dose group separately. The boxplot shows how the three groups compare in location and spread;
the QQ-plots check that the data in each group are close to normally distributed, since the model
that follows assumes normality. Having looked at the plots, the three groups are treated as
approximately normal with a common variance $\sigma^2$ — the spread looks similar across groups —
but with three possibly different means:

$$
Y_i \mid \text{group } j \sim N(\mu_j,\sigma^2), \qquad j = 1,2,3.
$$

This is the one-way ANOVA model: one normal distribution per group, sharing a variance, differing
only in its mean.

## The question as a hypothesis about means

The scientific question — does arachidonic acid dose change the average prostacyclin level —
becomes a single hypothesis about the three group means $\mu_1,\mu_2,\mu_3$ (low, medium, high):

$$
H_0 : \mu_1 = \mu_2 = \mu_3
$$

against

$$
H_1 : \exists\, j,k \in \{1,2,3\} : \mu_j \neq \mu_k.
$$

$H_0$ says the dose has no effect on the mean level at all. $H_1$ only asserts that *some* pair of
doses differ, without saying which — this is why the test is called an omnibus test: it answers
"is there an effect anywhere among the groups?" in one shot, rather than comparing groups pair by
pair. Which groups actually differ, if any do, is a separate question, addressed only after the
omnibus test rejects $H_0$.

## Fitting the model and running the omnibus test

Because `dose` now has three levels rather than two, the same `lm()` model-fitting still applies —
dose enters as a factor, and the fitted model carries one mean per group — but the test of $H_0$
against $H_1$ comes from calling `anova()` on the fitted model rather than reading a single
coefficient's p-value:

```r
model1 <- lm(prostac ~ dose, data = prostacyclin)
anova(model1)
```

`anova()` runs the F-test of the omnibus hypothesis: it asks whether letting the three group means
differ explains significantly more of the variation in prostacyclin level than a single shared
mean would. In this example the test rejects $H_0$ decisively ($p < 0.001$): arachidonic acid dose
does change the average prostacyclin concentration in rats.

## After the omnibus test: which groups differ

Rejecting $H_0$ only establishes that at least one pair of the three means differs — not which
pair. The follow-up is a set of pairwise comparisons (low vs. medium, low vs. high, medium vs.
high), using Tukey's method to correct for the fact that three comparisons are now being tested
instead of one, since testing several pairs after one significant omnibus result would otherwise
inflate the chance of a false positive:

```r
library(multcomp)
model1.mcp <- glht(model1, linfct = mcp(dose = "Tukey"))
summary(model1.mcp)
confint(model1.mcp)
plot(model1.mcp)
```

`glht()` ("general linear hypotheses") together with `mcp(dose = "Tukey")` sets up exactly the
three pairwise contrasts among the dose levels. `summary()` reports a Tukey-adjusted p-value for
each pairwise difference, `confint()` gives Tukey-adjusted confidence intervals for the three mean
differences, and `plot()` displays those intervals against zero.

## Reading the result

- The high-dose group has a significantly higher average prostacyclin concentration than both the
  low-dose group and the medium-dose group (both comparisons $p < 0.001$).
- The difference between the medium-dose and low-dose groups is not significant.
- So the effect picked up by the omnibus F-test is driven by the high dose: moving from low to
  medium dose does not move the mean detectably, but moving to the high dose does.

All of the post-hoc p-values and confidence intervals above are corrected for multiple testing
using the Tukey method, since three comparisons were read off the same fitted model.

## Sources

- Worked exercise: `tutorialScripts/excercises/07_ANOVA/ANOVA_prostacyclin.md` (converted from
  `ANOVA_prostacyclin.Rmd`), course GTPB PSLS20, CC BY 4.0. The entire chapter is drawn from this
  single tutorial script — the R code, the model, the hypotheses, the stated conclusions and the
  post-hoc analysis all come from it directly. No slide deck or lecture transcript was supplied for
  this chapter, and the mechanics of how the F-test itself is built from a sum-of-squares
  decomposition are not covered in this source — the script uses `anova()` and `glht()` as tools
  and reports their output, without deriving what the functions compute internally.

---

[← 20. ANOVA on the NHANES Dataset](20-anova-on-the-nhanes-dataset.md) · [Contents](index.md) · [22. Breast Cancer Dataset →](22-breast-cancer-dataset.md)
