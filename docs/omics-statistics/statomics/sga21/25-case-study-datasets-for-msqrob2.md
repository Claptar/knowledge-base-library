---
title: "25. Case-Study Datasets for msqrob2"
course: "StatOmics Sga21"
chapter: 25
source: "https://github.com/statOmics/SGA21"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [StatOmics Sga21](https://github.com/statOmics/SGA21), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 25. Case-Study Datasets for msqrob2

## What this covers

This chapter sets up two real datasets used to practice a full differential-expression workflow
in quantitative proteomics with `msqrob2`, on the simplest possible experimental design: two
groups to compare. It assumes the reader already has the machinery from earlier chapters — peptide
quantification, log-transformation, and the robust-regression summarization model that `msqrob2`
fits to turn peptide intensities into a protein-level fold change and test statistic — and is now
asking the practical question that comes right after building a pipeline: **how do you know the
pipeline is telling the truth?**

## Why a spike-in experiment, specifically

Any differential-analysis pipeline can be run on real biological data and will return some list of
"significant" proteins, but a real biological sample gives no way to check whether that list is
right, because the true fold changes are unknown. A **spike-in experiment** fixes this by
constructing a dataset where the ground truth is set by the experimenter rather than estimated:
known proteins are added to a background at known, different concentrations across the groups
being compared, so the analyst can check the pipeline's output against an answer that is already
known before the data are collected.

- Any spiked-in protein has a *known*, non-zero true fold change between the two groups.
- Every background protein has a true fold change of zero — it wasn't touched, so any statistical
  significance found on it is a false positive.

This is exactly the design behind the CPTAC dataset below, and it is why the workflow is checked
on it before being trusted on data without a known answer.

## The CPTAC spike-in dataset

The case study is a subset of Study 6 of the Clinical Proteomic Technology Assessment for Cancer
(CPTAC). The Sigma Universal Protein Standard mixture 1 (UPS1) — 48 human proteins — was spiked
into a background of *Saccharomyces cerevisiae* strain BY4741, at two different concentrations:

- **6A**: 0.25 fmol UPS1 protein/μL
- **6B**: 0.74 fmol UPS1 protein/μL

So the comparison "6A vs 6B" has a known answer built in: the 48 UPS1 (human) proteins have a real,
non-zero fold change between the two spike-in levels, while the yeast proteins making up the
background are the same in both groups and should show *no* fold change. A pipeline that recovers
the spiked proteins as differential and leaves the yeast proteins alone is behaving correctly; one
that flags yeast proteins as differential is producing false positives that a real experiment,
without this scaffolding, would hide.

The subset used here is restricted to one instrument and site — LTQ-Orbitrap W at site 56 — with
three replicates at each of the two spike-in concentrations. The raw files were searched with
MaxQuant version 1.5.2.8, with search settings as described in the original methods paper.

Two ways to obtain the data:

- The raw instrument files, from the CPTAC data portal (Study 6).
- The MaxQuant search output (`peptides.txt`), from a data archive; participants working in
  R/Rmarkdown can instead import it directly from the web within their script and skip the
  download.

The analysis itself is run either through the `msqrob2gui` Shiny app or through an Rmarkdown
script, both built around the `msqrob2` package.

## The breast cancer dataset

The second case study has no built-in ground truth — it is a real clinical comparison, used to
practice the same workflow on data where the analyst does not already know the answer. Eighteen
oestrogen-receptor-positive breast cancer tissue samples, from patients treated with tamoxifen upon
recurrence, were assessed by LC-MS (LTQ-Orbitrap, MaxQuant version 1.4.1.2, searched against the
2012-09 human canonical proteome). Nine patients had a good outcome and nine a poor outcome.

Three versions of the `peptides.txt` output are provided for this same cohort, at three different
sample sizes:

- 3 vs 3
- 6 vs 6
- 9 vs 9

## Exercises

1. Using the CPTAC 6A vs 6B data and either the GUI or the Rmarkdown script, run through the
   analysis workflow step by step, making sure you understand what each step is doing. Since the
   true fold change is known for both the spiked-in (UPS1) proteins and the yeast background
   proteins, check the output against that known answer — what do you observe?

2. Repeat the same analysis using median summarization in place of robust summarization. How do the
   results compare to the robust summarization, and why?

## Sources

- Notes: `docs/omics-statistics/statomics/sga21/pda_tutorialPreprocessing.md` (statOmics SGA21
  course, "2. Preprocessing and statistical analysis with msqrob2 for experiments with simple
  designs", sections 2.1–2.3) — the entire chapter is drawn from this file; no slides or transcript
  were supplied for this session.
- Referred to but not contained in the supplied material: the `msqrob2` Bioconductor package and
  its methods papers (Goeminne et al. 2016; Goeminne et al. 2020; Sticker et al. 2020); the CPTAC
  Study 6 raw data and original description; the GUI walkthrough (`cptac_robust_gui.html`) and
  Rmarkdown script (`cptac_robust.html`) that the exercises are run in; the `peptides.txt` files for
  both datasets.

---

[← 24. Experimental Design and Blocking](24-experimental-design-and-blocking.md) · [Contents](index.md) · [26. Mass Spectrometry-Based Proteomics →](26-mass-spectrometry-based-proteomics.md)
