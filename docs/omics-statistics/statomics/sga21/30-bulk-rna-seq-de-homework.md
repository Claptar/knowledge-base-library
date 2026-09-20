---
title: "30. Bulk RNA-seq DE Homework"
course: "StatOmics Sga21"
chapter: 30
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 30. Bulk RNA-seq DE Homework

## What this covers

This chapter works through a homework assignment that extends the default bulk RNA-seq
differential-expression (DE) pipeline built in the RNA-seq analysis intro lecture. It assumes you
already have that pipeline in hand — count data loaded into `edgeR`, a design matrix with a
treatment factor and a blocking factor, TMM normalization via `calcNormFactors`, and a fitted
negative-binomial GLM tested against a contrast. The assignment pokes at three separate pieces of
that pipeline in turn: the contrast itself, the blocking term, and the normalization step.

## The contrast under study

Every part of the assignment is fit to the same comparison: **DPN treatment versus control at
48 hours.** Whatever design terms are added or removed, and however the counts are normalized,
this is the one contrast whose test statistics and DE-gene calls get compared across the different
versions of the analysis.

## What changes between the parts

**Default analysis.** The starting point is the pipeline exactly as built in the intro lecture:
`edgeR`, default TMM normalization, and a design that includes a `patient` term alongside the
treatment factor.

**Removing the blocking term.** The design's `patient` term is there to absorb between-patient
variability that is not the effect of interest — that is what "blocking on patient" means here.
The assignment asks you to drop it and refit the same DPN-vs-control-at-48h contrast, then compare
the two fits two ways: how many genes are called DE, and how the *full* distribution of p-values
across all genes looks under each design, not only the fraction that clears a significance
threshold. The second comparison is the more informative one — a change in the DE-gene count could
come from a shift in power spread across the whole gene list, or from a change concentrated in a
handful of genes, and only the full p-value histogram distinguishes the two.

**Replacing TMM with full-quantile normalization.** The default pipeline normalizes with TMM,
applied through `edgeR`'s `calcNormFactors`. This part of the assignment asks you to build a
different normalization from scratch — full-quantile (FQ) normalization — and see what it changes.
Three things go with implementing it:

- writing `FQnorm` yourself and applying it to the count matrix in place of TMM;
- checking what the normalization actually did, by comparing per-sample densities of
  `log1p`-transformed counts before and after FQ normalization, and asking whether it makes the
  samples' distributions more or less alike;
- refitting the DPN-vs-control-at-48h contrast on the FQ-normalized counts — and, because those
  counts are already normalized, dropping the `calcNormFactors` step this time, since running TMM
  on top of FQ-normalized data would normalize the data twice.

Finally, at a fixed 5% FDR threshold, the DE gene list from the TMM-normalized analysis and the DE
gene list from the FQ-normalized analysis are compared against each other.

## Exercises

1. **Default `edgeR` analysis.** Using the pipeline from the RNA-seq analysis intro lecture, analyze
   the dataset with `edgeR`. Focus throughout on the contrast comparing DPN treatment to control
   at 48h.

2. **Impact of blocking.** Refit the same contrast with the `patient` term removed from the design
   (i.e., without blocking on patient). Assess the difference in the number of DE genes between the
   two models, and compare the p-value distributions between them.

3. **Full-quantile normalization.**
   a. Implement a function `FQnorm` that carries out full-quantile normalization of a count matrix,
      and apply it to the data.
   b. Compare the distributions of `log1p`-transformed counts — per sample, using the `density`
      function — before and after FQ normalization. What is the impact of FQ normalization on the
      differences in distribution between samples?
   c. Repeat the `edgeR` analysis using the FQ-normalized counts as input, this time omitting the
      `calcNormFactors` step, since the data have already been normalized.
   d. At a 5% FDR threshold, compare the list of DE genes obtained with TMM normalization to the
      list obtained with FQ normalization — for example, using a Venn diagram.

## Sources

- StatOmics SGA21, homework sheet `sequencing_hw.md` (converted from `sequencing_hw.Rmd`,
  CC BY-NC-SA 4.0) — all three assignment parts ("Default `edgeR` analysis", "Impact of blocking",
  "Analyze dataset using full-quantile normalization") and their code stubs.
- The homework refers to, but does not itself contain, the "RNA-seq analysis intro lecture" that
  supplies the default `edgeR` code and the dataset (its design, treatment/time levels, and the
  `patient` blocking factor). Neither the dataset nor that lecture's code was supplied with this
  homework file.

---

[← 29. Poisson GLMs for Count Data](29-poisson-glms-for-count-data.md) · [Contents](index.md) · [31. Sequencing Technology and Preprocessing →](31-sequencing-technology-and-preprocessing.md)
