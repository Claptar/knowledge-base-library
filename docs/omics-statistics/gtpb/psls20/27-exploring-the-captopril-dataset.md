---
title: "27. Exploring the Captopril Dataset"
course: "GTPB Psls20"
chapter: 27
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 27. Exploring the Captopril Dataset

## What this covers

This chapter works through a short tutorial on exploring **paired data**: systolic and diastolic
blood-pressure readings taken twice on the same fifteen hypertensive patients, once before and
once after they were given the drug captopril. It covers how to reshape a table of paired
measurements into the long form that `ggplot2` expects, why the barplot-with-error-bars that
papers commonly use is a poor way to display such data, and what a summary of paired measurements
should actually capture. It assumes basic familiarity with R and the tidyverse — data frames,
`dplyr` verbs such as `group_by` and `summarize_at`, and `ggplot2`.

## The captopril dataset

Fifteen patients with hypertension each contribute four numbers: systolic blood pressure before
captopril, systolic blood pressure after, diastolic blood pressure before, and diastolic blood
pressure after. The important structural fact is in the word *paired*: these are not four
independent groups of measurements, but two repeated measurements (before/after) on each of two
quantities (systolic/diastolic), taken on the *same* fifteen people. Any summary of the data that
throws away which "before" belongs with which "after" — for a given patient — throws away exactly
the information the pairing was designed to give.

The tutorial starts by loading the tidyverse and importing the `captopril` table, then taking a
first look at it (`head`, or similar). The template leaves both of those steps for the reader to
fill in, so no code for them is shown here.

## Reshaping wide to long

Once `captopril` is a data frame with one row per patient and four measurement columns, most
`ggplot2` recipes want the opposite shape: one row per (patient, measurement) pair, with a column
naming *which* measurement it is and a column holding its value. `gather` does this reshaping:

```r
captopril %>%
  gather(type, bp, -id)
```

Every column except `id` is gathered into two new columns: `type` (which of the four measures —
systolic/diastolic, before/after — the row records) and `bp` (the numeric value). This is the
shape used for both the plotting and the summarizing that follow.

## Visualizing the four groups: barplot with error bars

The obvious plot to reach for is a barplot of the mean of each of the four measurement types, with
error bars showing one standard error above and below the mean:

```r
captopril %>%
  gather(type, bp, -id) %>%
  group_by(type) %>%
     summarize_at("bp",
               list(mean=~mean(.,na.rm=TRUE),
                    sd=~sd(.,na.rm=TRUE),
                    n=function(x) x%>%is.na%>%`!`%>%sum)) %>%
  mutate(se=sd/sqrt(n)) %>%
  ggplot(aes(x=type,y=mean,fill=type)) +
  scale_fill_brewer(palette="RdGy") +
  theme_bw() +
  geom_bar(stat="identity") +
  geom_errorbar(aes(ymin=mean-se, ymax=mean+se),width=.2) +
  ggtitle("Barplot of different blood pressure measures") +
  ylab("blood pressure (mmHg)")
```

`summarize_at` computes, for each `type`, the mean, the standard deviation, and $n$ — the count of
non-missing values, obtained by negating `is.na` and summing. From these, the standard error is

$$SE = \frac{s}{\sqrt{n}}.$$

`geom_bar(stat="identity")` then draws one bar per type at the pre-computed mean, and
`geom_errorbar` adds the whisker from $\text{mean} - SE$ to $\text{mean} + SE$.

## Why the barplot is not the right picture

This plot is common in papers, but it is a poor summary of the data. A bar's height encodes only
one number, the mean; the error bar adds a second, the standard error of that mean. Neither says
anything about how the fifteen underlying values are actually distributed — whether they cluster
tightly around the mean or are spread widely, whether there are outliers, whether the distribution
is symmetric. It is possible to overlay the raw values as points on top of the bars, which restores
the individual values, but even that still does not give a summary measure of spread such as the
interquartile range. The lecture's own conclusion is that it is usually more informative to show
the underlying values as *raw* as possible, rather than collapsing them to a mean and an error bar
before plotting anything at all.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A bar with an error whisker next to the scatter of individual values it summarizes">
  <line x1="20" y1="190" x2="150" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="190" y1="190" x2="320" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <rect x="70" y="100" width="40" height="90" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="90" y1="85" x2="90" y2="115" stroke="currentColor" stroke-width="1.5"/>
  <line x1="82" y1="85" x2="98" y2="85" stroke="currentColor" stroke-width="1.5"/>
  <line x1="82" y1="115" x2="98" y2="115" stroke="currentColor" stroke-width="1.5"/>
  <text x="90" y="207" text-anchor="middle" font-size="12" fill="currentColor">barplot</text>
  <text x="150" y="90" text-anchor="end" font-size="11" fill="currentColor">mean &#177; SE</text>
  <line x1="190" y1="100" x2="320" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
  <circle cx="248" cy="70" r="3" fill="currentColor"/>
  <circle cx="258" cy="82" r="3" fill="currentColor"/>
  <circle cx="252" cy="92" r="3" fill="currentColor"/>
  <circle cx="262" cy="98" r="3" fill="currentColor"/>
  <circle cx="245" cy="104" r="3" fill="currentColor"/>
  <circle cx="256" cy="108" r="3" fill="currentColor"/>
  <circle cx="266" cy="115" r="3" fill="currentColor"/>
  <circle cx="250" cy="122" r="3" fill="currentColor"/>
  <circle cx="260" cy="130" r="3" fill="currentColor"/>
  <circle cx="244" cy="138" r="3" fill="currentColor"/>
  <circle cx="264" cy="145" r="3" fill="currentColor"/>
  <circle cx="252" cy="155" r="3" fill="currentColor"/>
  <circle cx="258" cy="163" r="3" fill="currentColor"/>
  <circle cx="247" cy="170" r="3" fill="currentColor"/>
  <circle cx="261" cy="176" r="3" fill="currentColor"/>
  <text x="255" y="207" text-anchor="middle" font-size="12" fill="currentColor">15 raw values</text>
</svg>
<figcaption>The bar and its whisker encode only the mean and standard error of one measurement
type. The dashed line marks that same mean sitting among the fifteen individual patient values it
was computed from — spread, shape and outliers the bar cannot show.</figcaption>
</figure>

## Descriptive statistics for paired data

Because the four measurement types are not independent groups but two repeated measurements on
the same fifteen people, a useful set of summary statistics has to reflect that pairing rather than
treat "systolic before", "systolic after", and so on as four unrelated samples. Summarizing each
column on its own — as the barplot above effectively does — discards the information that a
particular "before" and "after" value belong to the same patient, which is exactly the information
a paired design is collected to preserve.

## Exercises

Rewritten from the tutorial's own prompts; none are solved here.

1. Import the `captopril` dataset into R and take a first look at its structure (this step is left
   blank in the tutorial template).
2. Having seen why a barplot of the four means with standard-error whiskers is not very
   informative, propose a better way to visualize the captopril data, and write the code for it.
3. Write a code chunk that computes summary statistics for the captopril data that are useful
   precisely *because* the measurements are paired within each patient.

## Sources

- All of the above is from the single supplied file: `Tutorial 1.3: Exploring the captopril
  dataset`, GTPB PSLS20, *Data Exploration* tutorial exercise
  (`tutorialScripts/excercises/04_DataExploration/DataExplorationCaptoprilMinimalExample.Rmd`,
  CC BY 4.0).
- No slide deck or lecture transcript was supplied for this tutorial, and no problem set beyond the
  two prompts embedded in the file itself.
- The file refers to, but does not itself contain: the `captopril` data file (imported by code the
  template leaves blank), and the accompanying *Data Exploration* lecture that this tutorial
  practises.

---

[← 26. The NHANES Dataset](26-the-nhanes-dataset.md) · [Contents](index.md) · [28. Exploring the Fish Tank Dataset →](28-exploring-the-fish-tank-dataset.md)
