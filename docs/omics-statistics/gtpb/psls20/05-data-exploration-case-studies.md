---
title: "5. Data Exploration Case Studies"
course: "GTPB Psls20"
chapter: 5
source: "https://github.com/GTPB/PSLS20.git"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [GTPB Psls20](https://github.com/GTPB/PSLS20.git), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Data Exploration Case Studies

## What this covers

This chapter introduces the four data sets used on the first day of practical work in the
course, each built around a different real study and each chosen to teach a different habit or
hazard of exploratory data analysis: importing and tidying a large survey (NHANES), comparing two
independent groups (the armpit microbiome experiment), handling a paired design (the captopril
trial), and recognising a confounder (the FEV study). It assumes only that the reader is about to
start analysing data in R and has not yet seen any of the four data sets; it does not assume any
statistical test has been covered yet — the point of this stage is to look at the data before
testing anything.

## Why explore data before testing anything

Across a data-analysis pipeline, "getting familiar with the dataset" is always the first step,
before any hypothesis test is chosen or run. In practice this means: importing the data into R,
tidying it into a usable shape, wrangling it (recoding, filtering, joining, summarising) into the
variables the question actually needs, and visualising it to see the patterns, the outliers and
the structure of the design before committing to an analysis. The four data sets below are used,
in turn, to practise these steps and to introduce three recurring structures in real experiments:
independent groups, paired measurements, and confounding.

## The NHANES survey

The National Health and Nutrition Examination Survey (NHANES) has collected data on the US
population since 1960. The tutorial uses the wave collected between 2009 and 2012, covering
10,000 US civilians, with a large number of physical, demographic, nutritional and lifestyle
variables recorded per person. Because it is large and varied, it is the data set used to learn
the mechanics of exploration itself: import, tidying, wrangling and visualisation in R, without yet
asking a specific research question of it.

## The armpit microbiome experiment

Body odour from armpits is not caused by sweat itself but by micro-organisms that metabolise
sweat into smelly compounds. *Corynebacterium* spp. do this; *Staphylococcus* spp., another
abundant group in the armpit microbiome, do not.

The CMET group at Ghent University is investigating whether transplanting the armpit microbiome
can help people with smelly armpits. They ran an experiment on two independent groups of
volunteers: one treated with a placebo, the other given a microbiome transplant. The question the
data should answer is whether the relative abundance of *Staphylococcus* spp. differs between the
two groups.

Structurally, this is the simplest comparison: two independent groups, one continuous outcome. The
tutorial deliberately withholds the worked-example scaffolding used for NHANES and asks the reader
to apply the same exploratory skills unaided.

## The captopril trial

The captopril data set records a small experiment on 15 patients with elevated blood pressure.
Each patient contributes four measurements: systolic and diastolic blood pressure, each taken
before and after being treated with the drug captopril.

The structural point of this data set is that the four measurements per patient are not four
independent observations — before and after are the *same* patient, measured twice. Exploring data
like this means keeping the pairing intact (e.g., plotting each patient's before/after change),
rather than treating the "before" group and "after" group as if they were two independent samples.

## The FEV study

Forced expiratory volume (FEV) is the amount of air, in litres, a person can exhale during a
forced breath. The data set records FEV for 606 children aged 6 to 17, along with each child's
age, height, gender, and whether they smoke. The motivating question is whether smoking affects
the FEV of children.

This is the data set used to introduce confounding: smoking is not handed out at random among the
children — smokers in the sample tend to be older, and older children have larger lungs regardless
of smoking. A naive comparison of FEV between smokers and non-smokers is therefore contaminated by
age (and height), and exploring the data means checking, before any test, how smoking status
relates to the other recorded variables and not just to the outcome.

## The four data sets side by side

| Data set | What is measured | Design it illustrates |
| --- | --- | --- |
| NHANES | physical, demographic, nutritional, lifestyle variables, 10,000 people | large-scale import/tidy/wrangle/visualise practice |
| Armpit microbiome | relative abundance of *Staphylococcus* spp. | two independent groups (placebo vs. transplant) |
| Captopril | systolic and diastolic blood pressure, before/after | paired measurements on the same 15 patients |
| FEV | forced expiratory volume, plus age, height, gender, smoking | a confounded comparison (smoking, confounded by age/height) |

## Exercises

The course's own tutorial tasks, as set out in the instructions:

1. Using the NHANES data, practise importing, tidying, wrangling and visualising the data set in
   R, as a first pass before any formal analysis.
2. Using the armpit microbiome data, and applying the same exploratory skills as for NHANES without
   further guidance, explore whether the relative abundance of *Staphylococcus* spp. differs
   between the placebo group and the microbiome-transplant group.
3. Using the captopril data, explore the paired before/after blood-pressure measurements for the
   15 patients, keeping the pairing between each patient's two measurements intact.
4. Using the FEV data, explore whether smoking is associated with FEV in children, and consider
   what role age, height and gender might play as confounders of that association.

## Sources

- Notes: `tutorialScripts/excercises/04_DataExploration/04_instructions.md` (GTPB PSLS20, "Practical
  Statistics for the Life Sciences (2020)", CC BY 4.0) — the full content of this chapter, including
  all four data-set descriptions and the tutorial goals in the Exercises section.
- No slides or transcript were supplied for this session.
- The instructions reference, but do not themselves contain, the four exercise notebooks
  (`Data_exploration_NHANES.Rmd`, `Data_exploration_armpit.Rmd`, `Data_exploration_captopril.Rmd`,
  `Data_exploration_FEV.Rmd`) and their data files (`NHANES.csv`, `armpit.csv`, `captopril.txt`,
  `fev.txt`), hosted in the GTPB/PSLS20 GitHub repository — these were not supplied as input.

---

[← 4. Describing and Relating Quantitative Data](04-describing-and-relating-quantitative-data.md) · [Contents](index.md) · [6. The Logic of Statistical Inference →](06-the-logic-of-statistical-inference.md)
