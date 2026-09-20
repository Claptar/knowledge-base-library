---
title: "23. Smelly Armpit Data Exploration"
course: "GTPB Psls20"
chapter: 23
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 23. Smelly Armpit Data Exploration

## What this covers

A hypothesis test comes with assumptions, and you don't get to skip checking them just because the
test itself is the interesting part. This chapter works through the "smelly armpit" dataset — a
small randomized experiment on the armpit microbiome — as an exercise in *data exploration*: what
to plot, what to compute, and what question each of those answers, before any formal test is run.
It assumes you can manipulate a data frame with `dplyr`-style piping (`group_by`, `summarize`,
`mutate`) and that you know roughly what a two-sample comparison of means is trying to do; the test
itself is deferred to the next tutorial.

## The experiment behind the data

A smelly armpit is not caused by sweat itself. Sweat is odourless; the smell comes from specific
bacteria that metabolise it into smelly compounds, chiefly *Corynebacterium spp.* A second group of
bacteria, *Staphylococcus spp.*, is also abundant in the armpit microbiome but does *not* turn sweat
into odour. So the balance between the two genera is a plausible handle on how smelly an armpit is:
the more the microbiome is dominated by *Staphylococcus* relative to *Corynebacterium*, the less
odour-producing capacity it has.

A research group at Ghent University (the CMET group) tested whether that balance can be shifted on
purpose, as a therapy for smelly armpits:

1. wipe out the existing armpit microbiome with antibiotics;
2. reintroduce a different microbiome by microbial transplant.

The experiment: 20 students with smelly armpits were randomized into two treatment arms — a
*placebo* arm (antibiotics only) and a *transplant* arm (antibiotics followed by a microbial
transplant). Six weeks after treatment, the armpit microbiome was sampled and the relative abundance
of *Staphylococcus spp.* — its share of *Staphylococcus spp.* plus *Corynebacterium spp.* — was
measured by DGGE (Denaturing Gradient Gel Electrophoresis). The question the researchers wanted
answered: does the transplant shift that relative abundance, compared with antibiotics alone?

<figure>
<svg viewBox="0 0 420 240" role="img" aria-label="Randomized two-arm design of the armpit-microbiome transplant experiment, sampled at six weeks">
  <defs>
    <marker id="arrow-armpit" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="140" y="10" width="140" height="34" fill="none" stroke="currentColor"/>
  <text x="210" y="27" text-anchor="middle" font-size="12" fill="currentColor">20 students,</text>
  <text x="210" y="40" text-anchor="middle" font-size="12" fill="currentColor">smelly armpits</text>

  <line x1="210" y1="44" x2="210" y2="68" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-armpit)"/>
  <text x="226" y="60" font-size="11" fill="currentColor">randomize</text>

  <line x1="210" y1="70" x2="100" y2="102" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-armpit)"/>
  <line x1="210" y1="70" x2="320" y2="102" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-armpit)"/>

  <rect x="20" y="104" width="160" height="40" fill="none" stroke="currentColor"/>
  <text x="100" y="121" text-anchor="middle" font-size="11" fill="currentColor">placebo:</text>
  <text x="100" y="136" text-anchor="middle" font-size="11" fill="currentColor">antibiotics only</text>

  <rect x="240" y="104" width="160" height="40" fill="none" stroke="currentColor"/>
  <text x="320" y="121" text-anchor="middle" font-size="11" fill="currentColor">transplant:</text>
  <text x="320" y="136" text-anchor="middle" font-size="11" fill="currentColor">antibiotics + transplant</text>

  <line x1="100" y1="144" x2="210" y2="182" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-armpit)"/>
  <line x1="320" y1="144" x2="210" y2="182" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-armpit)"/>

  <rect x="80" y="186" width="260" height="40" fill="none" stroke="currentColor"/>
  <text x="210" y="203" text-anchor="middle" font-size="11" fill="currentColor">6 weeks later: DGGE measurement</text>
  <text x="210" y="218" text-anchor="middle" font-size="11" fill="currentColor">of relative Staphylococcus abundance</text>
</svg>
<figcaption>Twenty students with smelly armpits were randomized to antibiotics alone or antibiotics
followed by a microbial transplant. Six weeks later, the relative abundance of
<em>Staphylococcus spp.</em> in the armpit microbiome was measured by DGGE — this is the "rel"
variable, recorded alongside the treatment group "trt".</figcaption>
</figure>

## Why explore the data before testing it

The formal comparison of the two groups is left to the next tutorial, but it comes with a cost: to
be valid, a standard two-sample test needs

1. the data within each treatment group to be roughly normally distributed, and
2. the two groups to have roughly the same variance.

These are not things you assume and hope; they are things you check, and the way you check them is
exploration — plotting the data and summarizing it numerically — *before* the test is run. If either
assumption looks badly wrong, that is information the downstream analysis needs, not something to
discover after the fact. Mastering that exploration step, on this dataset, is the point of the
tutorial.

## Looking at the shape: histograms and boxplots

The first plot to make is a histogram of the relative abundance (`rel`), with one row per treatment
group (`trt`) so the two distributions sit directly above one another for comparison. From that plot
it looks like relative abundance is higher in the students who received the transplant.

But with only 20 students split across two arms — about ten per group — a histogram is a genuinely
noisy way to see a distribution's shape: each bar is counting very few points, and where the bin
edges happen to fall can make the same data look lumpy or smooth. A boxplot is a better choice at
this sample size, because it summarizes the data directly (median, interquartile range, whiskers)
rather than routing it through an arbitrary binning. Plotting relative abundance against treatment
as a boxplot is what to look at instead — and what to look *for* is whether the two boxes overlap,
whether their spreads (box heights) are comparable, which speaks directly to the equal-variance
assumption, and whether either group shows a skew or an outlier that would threaten the
normality assumption.

## Turning the picture into numbers

A plot gives a qualitative read; the exploration also needs numbers that the next tutorial's test
will actually use. For each treatment group, compute:

- the **mean** relative abundance,
- the **standard deviation**, a measure of spread within the group — this is the number that
  directly checks the equal-variance assumption between the two groups,
- **n**, the number of observations in the group, and
- the **standard error of the mean**,
$$SE = \frac{s}{\sqrt{n}},$$
  which will set the scale of uncertainty for whatever comparison of the two group means comes next.

The natural pipeline for this is the one the tutorial sets up: group the data by treatment
(`group_by(trt)`), summarize the `rel` variable within each group to get the mean, standard
deviation and count, then add a derived column for the standard error from those. Nothing here is
new statistics — it is the same three numbers (mean, spread, sample size) that any exploration of a
grouped variable needs, made specific to this dataset.

## Exercises

The dataset is a data frame `ap` with (at least) a treatment column `trt` (placebo vs. transplant)
and a relative-abundance column `rel`.

1. Load the dataset into `ap` and inspect it with `glimpse()`. What are the variables, and what type
   is each one held as?
2. Plot a histogram of `rel`, coloured by `trt`, with the two treatment groups shown as separate rows
   (one histogram per group, stacked vertically). What does the plot suggest about the effect of the
   transplant?
3. Explain, given the sample size, why a boxplot might be more informative here than a histogram, and
   produce one: relative abundance on one axis, treatment group on the other, coloured by treatment.
   What do you observe?
4. Group the data by treatment and compute, for each group, the mean, standard deviation and number
   of observations of `rel`; then add a column for the standard error of the mean. Which of the two
   assumptions listed above (normality within groups, equal variance across groups) does each of
   these numbers or plots speak to?

## Sources

- Both parts of this chapter are drawn from the GTPB PSLS20 tutorial *Data exploration: armpit
  microbiome*, converted from `Data_exploration_armpit.Rmd` (CC BY 4.0):
  - the dataset and experimental design —
    [`01-smelly-armpit-dataset.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd)
  - the visualization and descriptive-statistics workflow —
    [`02-data-visualization.md`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/04_DataExploration/Data_exploration_armpit.Rmd)
- The source is itself a fill-in-the-blank R exercise: the code that actually loads `ap`, the exact
  `ggplot` calls for the histogram and boxplot, and the `summarize_at`/`mutate` pipeline for the
  descriptive statistics are left as blanks for the student to complete, so no filled-in code or
  solved output is reproduced here — see the Exercises section above for the tasks themselves.
- The tutorial links to a video on the proposed microbial-transplant therapy
  (`https://youtu.be/9RIFyqLXdVw`) without summarizing it; that content is not included here.
- The formal test of the treatment effect, and its own assumption checks, are deferred by the source
  to a following tutorial on hypothesis testing, which was not supplied.

---

[← 22. Breast Cancer Dataset](22-breast-cancer-dataset.md) · [Contents](index.md) · [24. Visualizing Paired Data →](24-visualizing-paired-data.md)
