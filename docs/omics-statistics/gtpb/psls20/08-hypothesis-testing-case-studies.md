---
title: "8. Hypothesis-Testing Case Studies"
course: "GTPB Psls20"
chapter: 8
source: "https://github.com/GTPB/PSLS20"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [GTPB Psls20](https://github.com/GTPB/PSLS20), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Hypothesis-Testing Case Studies

## What this covers

This is the introduction to the second day of tutorials, which hands over from the ideas of
hypothesis testing to practice on real data. It does not introduce any new theory itself: it
assumes the reader already has the basic machinery of a hypothesis test (a null and an
alternative hypothesis, a test statistic, a p-value) and instead lays out four small, real
datasets, each chosen to force a different experimental-design question — paired measurements,
two independent groups, and more than two groups — before the reader works through the
corresponding exercise on each one.

## Why the design of the experiment comes before the test

The point of walking through four datasets rather than one is that the right test is not a free
choice: it is forced by how the data were collected. Before running any test, the question to ask
is "were these measurements taken on the same units, or on different ones, and how many groups is
one comparing?" The four cases below are built to make that question unavoidable.

## The captopril dataset: a paired design

Fifteen patients with elevated blood pressure each contribute four numbers: systolic and
diastolic pressure, measured on the same patient before and after treatment with the drug
captopril. Because "before" and "after" are two measurements on the *same* fifteen people rather
than on two separate groups of people, the two sets of numbers are not independent of one
another — a patient who starts with high pressure tends to still have relatively high pressure
after treatment, even if the drug works. This is what a paired design means, and recognising it
is the first hurdle the tutorial exercise on this dataset is built around.

## The armpit dataset: two independent groups

The motivating biology: body odour is not caused by sweat itself but by bacteria that metabolise
it, chiefly *Corynebacterium* species; a second common group, *Staphylococcus* species, does not
produce the smelly compounds. A research group at Ghent University transplants the armpit
microbiome as a possible treatment for smelly armpits, and tested it by splitting volunteers into
two separate groups — one given a placebo, one given a microbiome transplant — and comparing the
average relative abundance of *Staphylococcus* between them afterwards. Unlike the captopril
case, these are two distinct sets of people, not one set measured twice, so the comparison is
between two independent samples rather than paired ones.

## The shrimps dataset: two independent groups, a different question

Two groups of 18 shrimp samples (100 g each) were raised under different conditions: a control
medium and a medium polluted with PCBs (compounds that are common in coolants and accumulate
readily in shrimp adipose tissue). The question is whether the growth condition affects the PCB
concentration found in the tissue. The design is structurally the same as the armpit case — two
independent groups compared on one measured quantity — even though the biological question is
unrelated, which is the point: the same design produces the same kind of test regardless of the
subject matter.

## The cuckoo dataset: more than two groups

The common cuckoo does not build its own nest; it lays its eggs in the nest of a "foster parent"
species, and has done so long enough (this has been documented since the 1892 observation that egg
type varies by location, and an experiment from 1940 showed cuckoos return to the same nesting
area and foster species year on year) that geographically separated cuckoo subspecies have evolved
whose eggs mimic the eggs of their particular foster species. The dataset records 120 cuckoo eggs
drawn from randomly selected foster nests, and the question is whether the *type* of foster parent
affects the average length of the cuckoo egg. Because there are more than two foster-parent
categories being compared at once, this case is structurally different again from the armpit and
shrimp examples: it is a comparison across several groups rather than a comparison between two.

## Exercises

The lecture material handed to this tutorial session is only the description of the four
datasets above; the worksheets themselves (one `.Rmd` exercise per dataset, each with its own
data file) are referenced by URL but were not part of the material supplied for this chapter, so
they are not reproduced here. For reference, the four exercises are:

- Captopril (paired design)
- Armpit microbiome (two independent groups)
- Shrimps and PCB exposure (two independent groups)
- Cuckoo eggs and foster species (more than two groups)

## Sources

- `docs/omics-statistics/gtpb/psls20/tutorialScripts/excercises/05_statisticalInference/05_statisticlInference.md`
  — the sole supplied source for this chapter, an introductory note (not a slide deck or a
  transcript) for the second day of the "Practical Statistics for the Life Sciences" (PSLS20)
  course, describing the captopril, armpit, shrimps and cuckoo datasets used in the day's
  hypothesis-testing tutorials.
- The note itself links out to four `.Rmd` exercise files and four data files (captopril, armpit,
  shrimps, Cuckoo), hosted in the course's GitHub repository (`GTPB/PSLS20`). None of these were
  supplied as input to this chapter, so their content — the actual test procedures, R code and
  worked answers — is not covered here.

---

[← 7. The Two-Sample T-Test](07-the-two-sample-t-test.md) · [Contents](index.md) · [9. Simple Linear Regression →](09-simple-linear-regression.md)
