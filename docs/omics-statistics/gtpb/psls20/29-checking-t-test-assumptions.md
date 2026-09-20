---
title: "29. Checking t-test Assumptions"
course: "GTPB Psls20"
chapter: 29
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 29. Checking t-test Assumptions

## What this covers

This chapter works through a single worked example — the "smelly armpit" microbial-transplant
experiment — to answer a practical question: before running a two-sample $t$-test on real data,
what has to be checked, and how? It assumes the reader already knows what a two-sample $t$-test
is and what null and alternative hypotheses are; the point here is the diagnostic work that has
to happen *before* the test is trusted, not the mechanics of the test itself.

## The experiment

Smelly armpits are not caused by sweat itself. The smell comes from specific micro-organisms in
the group *Corynebacterium spp.* that metabolise sweat into odorous compounds. A second group,
*Staphylococcus spp.*, is also abundant in the armpit microbiome but does not produce the smell.
A research group at Ghent University (the CMET group) investigated whether transplanting the
armpit microbiome could be used to treat people with smelly armpits, via a two-step therapy:

1. remove the existing armpit microbiome with antibiotics, then
2. influence the microbiome with a microbial transplant.

Twenty subjects with smelly armpits were randomized to one of two treatment groups:

- **placebo** — antibiotics only,
- **transplant** — antibiotics followed by a microbial transplant.

Six weeks after treatment, the microbiome was sampled and the relative abundance of
*Staphylococcus spp.* against *Corynebacterium spp.* + *Staphylococcus spp.* was measured by
denaturing gradient gel electrophoresis (DGGE). This relative abundance is the outcome variable.

The research question is whether transplanting the microbiome changes the relative abundance of
*Staphylococcus spp.* in the armpit. Framed as a hypothesis test, the null hypothesis is that
there is, on average, no difference in relative abundance between the transplant and placebo
groups; the alternative is that there is a difference. An unpaired, two-sample $t$-test is the
natural tool for this, because randomization gives two independent groups and the outcome is
a continuous relative abundance.

## Look at the data before testing anything

The first step, before any formal test, is to plot the raw data: a boxplot of relative abundance
by treatment group, with the individual observations jittered on top and the group means marked.
Visually, the subjects who received the microbial transplant have a higher relative abundance of
*Staphylococcus spp.* on average than the placebo group. But an apparent difference in a sample of
twenty is not by itself evidence about the population — that is exactly what the formal test is
for, and it is only trustworthy if its assumptions hold.

## Checking the assumptions of the two-sample $t$-test

A two-sample $t$-test rests on three assumptions, and each has to be checked against the specific
dataset before the test is run, not just asserted:

1. **Independence**, both within and between groups. This one is not checked from the data at
   all — it has to be guaranteed by the design. Here it follows from randomizing subjects to the
   two treatments and sampling each subject once.
2. **Normality** of the outcome within each group.
3. **Equal variability** (homoscedasticity) between the two groups.

**Checking normality.** The standard visual check is a quantile-quantile (QQ) plot for each
group: the sample's quantiles are plotted against the quantiles a normal distribution would
produce, together with a reference diagonal. If the data really are normal, the points should
scatter closely around that diagonal. In this dataset, the points in both groups' QQ plots sit
close to the reference line, which is read as the data being approximately normally distributed
in each group.

**Checking equal variability.** This is compared visually from the boxplots already drawn: the
size of the box (its height) is the interquartile range, a nonparametric estimate of spread that
does not depend on the normality assumption. If the two boxes are roughly the same size, the two
groups have roughly the same variability. Here the boxes for the two treatment groups are fairly
equal in size.

A caveat is attached to this second check: with only ten subjects per group, an interquartile
range is not estimated very precisely, so a small difference in box size is not good evidence of
unequal variance. The rule of thumb used here is that one box needs to be roughly two to three
times larger than the other before it counts as an indication of unequal variability. (Had that
been the case, the fix is not to abandon the $t$-test but to use its Welch-modified version, which
does not assume the two groups have equal variance.)

Since all three checks come out clean — independence by design, approximate normality in each
group, and comparable spread between groups — the unpaired two-sample $t$-test with equal
variances is the appropriate test to run on this data.

## Exercises

No problems were supplied with this material.

## Sources

- Dataset description, biological background, experimental design, research goal, and hypotheses
  from `01-smelly-armpit-dataset.md` (GTPB PSLS20, *Hypothesis_testing_armpit_LC*, "Smelly armpit
  dataset" and "Goal" sections).
- Data visualization and the three-assumption check (independence, normality via QQ plot, equal
  variability via boxplot interquartile range, and the Welch's-test caveat) from
  `02-data-exploration.md` (same source, "Data Exploration" and "Check the assumptions" sections).
- The material stops at the header "Assess the research question with the two-sample t-test": the
  actual test computation, its output, and the exercise inviting the reader to check the
  assumptions themselves ("Train yourself in checking the assumptions") are referenced by the
  source but were not included in what was supplied for this chapter, so they are not covered
  here. Likewise, a linked video on the microbial-transplant procedure is mentioned in the source
  but not part of the supplied material.

---

[← 28. Exploring the Fish Tank Dataset](28-exploring-the-fish-tank-dataset.md) · [Contents](index.md) · [30. One-Sample and Paired t-Tests →](30-one-sample-and-paired-t-tests.md)
