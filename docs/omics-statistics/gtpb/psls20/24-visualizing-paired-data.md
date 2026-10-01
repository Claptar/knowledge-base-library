---
title: "24. Visualizing Paired Data"
course: "GTPB Psls20"
chapter: 24
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 24. Visualizing Paired Data

## What this covers

This chapter works through a single worked dataset — 15 hypertensive patients whose systolic and
diastolic blood pressure were measured **before and after** a dose of captopril — to answer a
narrower question than "how do I plot this": *how should I visualize and summarize data that come
in matched pairs*, and why does the obvious first plot (a bar chart of group means) actively hide
the thing that matters? It assumes basic comfort with R/tidyverse (reshaping a data frame, piping,
`ggplot2`) and with elementary descriptive statistics (mean, standard deviation, standard error),
of the kind built up in the course's earlier exploration tutorial on the armpit-microbiome data.

## The captopril dataset

Fifteen patients with hypertension each contribute four numbers: systolic blood pressure before
treatment, systolic blood pressure after treatment, diastolic blood pressure before, and diastolic
blood pressure after. The design is **paired**: the "before" and "after" readings for a given
patient are not two independent samples, they are two measurements on the *same* person. That
matters for every choice that follows — which plot to draw, which summary to compute, and later,
which test to run.

The raw table is one row per patient with one column per measurement type — "wide" format. To
summarize or plot by measurement type it is reshaped to "long" format, one row per
patient–measurement-type combination, with a `type` column recording which of the four
measurements it is and a `bp` column holding the value. In the tidyverse this is what `gather`
does: `captopril %>% gather(type, bp, -id)` keeps `id` fixed and stacks the other four columns into
`type`/`bp` pairs. Grouping and summarizing by measurement type, or faceting a plot by it, both
need the data in this shape.

## Why the bar chart is not enough

A natural first plot groups the long-format data by `type`, computes the mean, standard deviation
and standard error of each group, and draws a bar per type with an error bar of $\pm 1$ SE. This is
the plot most commonly seen in papers, and it is a poor one here, for a reason that has nothing to
do with captopril specifically: **a bar plus an error bar is only two numbers**, the mean and the
spread of the mean. It says nothing about

- the shape of the underlying distribution — is it symmetric, skewed, bimodal?
- the spread of the *raw* values, e.g. the interquartile range, as opposed to the standard error
  of the mean;
- and, specific to this dataset, **which "before" value belongs to which "after" value**. Even
  overlaying the raw points on the bars would not fix this last point: a cloud of 15 "before" dots
  and a cloud of 15 "after" dots still does not show which dot in one cloud is paired with which
  dot in the other.

That third failure is the one worth dwelling on, because it is invisible unless you go looking for
it: two datasets can have identical bar charts — identical means, identical standard errors — while
one shows every patient's blood pressure falling by the same amount and the other shows half the
patients rising and half falling by twice as much, so that the changes cancel in the mean. A bar
chart of group means cannot tell these apart.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Illustrative line plot connecting each patient's before and after reading, showing individual change that a bar chart of the two group means cannot show">
  <line x1="40" y1="20" x2="40" y2="190" stroke="currentColor" stroke-width="1" opacity="0.4"/>
  <text x="18" y="18" font-size="12" fill="currentColor">bp</text>
  <text x="90" y="205" text-anchor="middle" font-size="12" fill="currentColor">before</text>
  <text x="230" y="205" text-anchor="middle" font-size="12" fill="currentColor">after</text>
  <line x1="90" y1="60" x2="230" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="80" x2="230" y2="120" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="100" x2="230" y2="150" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="130" x2="230" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="150" x2="230" y2="90" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <circle cx="90" cy="60" r="3" fill="currentColor"/>
  <circle cx="90" cy="80" r="3" fill="currentColor"/>
  <circle cx="90" cy="100" r="3" fill="currentColor"/>
  <circle cx="90" cy="130" r="3" fill="currentColor"/>
  <circle cx="90" cy="150" r="3" fill="currentColor"/>
  <circle cx="230" cy="110" r="3" fill="currentColor"/>
  <circle cx="230" cy="120" r="3" fill="currentColor"/>
  <circle cx="230" cy="150" r="3" fill="currentColor"/>
  <circle cx="230" cy="170" r="3" fill="currentColor"/>
  <circle cx="230" cy="90" r="3" fill="currentColor"/>
</svg>
<figcaption>Each line joins one patient's before and after reading (schematic, not the actual
captopril values). Four fall, one rises (dashed). A bar chart of the two column means would show
only two heights, and could not distinguish this pattern from one in which every patient changed
identically, or one in which rises and falls happened to cancel in the average.</figcaption>
</figure>

## Showing the pairing: a line per patient

If the plot is meant to show a treatment effect, it should show the *change*, not just the two
group locations. The direct fix is to draw one line per patient connecting their "before" point to
their "after" point — in `ggplot2`, `geom_line(aes(group = id))` on top of the before/after points
achieves this: each patient becomes a slope rather than two disconnected dots, and the eye reads
the direction and size of each individual's change directly, along with how consistent that change
is across patients.

## Reducing the pair to one number: the difference

An alternative to plotting both values per patient is to collapse each pair into a single
per-patient number, the difference `after − before`. This throws away the absolute level and keeps
only the change, which is usually exactly the quantity of interest when the question is "did the
treatment do anything". A boxplot or histogram of these 15 differences shows the distribution of
individual effects directly — including any patients whose blood pressure moved the "wrong" way —
in a way neither the bar chart nor the two raw clouds of points did.

This reduction also sets up the question the tutorial poses next: **to which value should the
average difference be compared, to decide whether captopril had an effect, and why?** If the drug
did nothing, a patient's "after" reading should differ from their "before" reading only by
measurement noise, so the *differences* should be centred on zero, not on the baseline mean or any
other reference. Zero is therefore the natural benchmark, and comparing the observed average
difference to zero is exactly what the paired test introduced in the later tutorial on statistical
inference formalizes.

## Checking the normality assumption with a QQ-plot

That upcoming paired test relies on an assumption: that the per-patient differences are
approximately normally distributed. Before trusting the test, the tutorial checks this
graphically with a **QQ-plot**, which plots the sorted observed differences against the quantiles
a normal distribution would predict at the same ranks. Points falling close to a straight line are
consistent with normality; systematic curvature or points peeling away at the ends are evidence
against it. For the systolic blood pressure differences here, the tutorial reports no large
deviation from the line — the differences look approximately normal, so the paired test's
assumption is not obviously violated.

## Descriptive statistics, twice

The same `gather` → `group_by` → `summarize_at` pattern used for the bar chart — computing mean,
standard deviation, sample size (`n`, counting non-missing values) and standard error
($\text{se} = \text{sd}/\sqrt{n}$) for each of the four measurement types — is worth keeping even
after abandoning the bar chart itself: as a table, these numbers are a legitimate compact summary,
they are only a poor *plot*.

It is worth computing the same four numbers a second time for the systolic difference alone,
separately from the four raw measurement types. The mean of the differences is the estimated
average treatment effect; its standard deviation describes how much that effect varies from patient
to patient, i.e. how consistent captopril's effect was across the 15 people in the study — a
question the means of the raw "before" and "after" columns, taken separately, cannot answer.

## Wrap-up

For paired data, the tutorial's own conclusion is the one to keep: report the paired line plot and
a boxplot (or histogram) of the differences, and drop the bar chart of group means from any
write-up — it hides exactly the structure, the pairing, that makes the data worth having.

## Exercises

1. The tutorial's own barplot code produces a bar per blood-pressure type with $\pm 1$ standard
   error bars. Explain concretely what this plot fails to show about the captopril data, then
   design and produce a more informative visualization of the same four measurement types.
2. Produce a plot that makes the pairing in the data visible — that each "before" and "after"
   reading belongs to the same patient. (Hint used in the tutorial: `geom_line(aes(group = id))`.)
3. Compute, for each patient, the difference between their "after" and "before" systolic blood
   pressure, and plot the distribution of these 15 differences.
4. To assess whether captopril had an effect, to which value should the average difference be
   compared? Justify the choice.
5. Produce a QQ-plot of the systolic blood pressure differences and assess whether the normality
   assumption needed for the paired test (covered in the later inference tutorial) looks
   reasonable.
6. Compute descriptive statistics — mean, standard deviation, sample size and standard error — for
   each of the four blood pressure measurements (systolic/diastolic, before/after).
7. Compute the same descriptive statistics for the systolic blood pressure difference, and use them
   to comment on the size and consistency of captopril's effect across the 15 patients.

## Sources

- `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/04_DataExploration/Data_exploration_captopril.md`
  — GTPB PSLS20, Tutorial 1.3 "Exploring the captopril dataset" (CC BY 4.0), converted from the
  course's `Data_exploration_captopril.Rmd`. All of the above — the dataset description, the
  barplot critique, the paired line plot hint, the difference-score question, the QQ-plot check
  and its stated result, and the descriptive-statistics steps — is drawn from this file.
- No slide deck or spoken transcript was supplied for this session; the tutorial is a
  self-contained R Markdown exercise sheet.
- The tutorial refers to, but does not itself contain, an earlier exploration tutorial on the
  "armpit" microbiome dataset, pointed to as the place to look for the descriptive-statistics
  pattern (`gather` → `group_by` → `summarize_at`) reused here, and to a later tutorial on
  statistical inference where the paired test for the systolic blood pressure difference is
  actually carried out. Neither is part of the material supplied for this chapter.

---

[← 23. Smelly Armpit Data Exploration](23-smelly-armpit-data-exploration.md) · [Contents](index.md) · [25. Exploring the FEV Dataset →](25-exploring-the-fev-dataset.md)
