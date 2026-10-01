---
title: "Carilli 2026 — Genetic Interrogation of Expression Regulation"
paper: "summary"
source: "https://thesis.library.caltech.edu/18729/"
licence: "CC BY-NC-ND 4.0 — no adaptation permitted, not reproduced"
written: "2026-10-02"
---

> **Summary of a thesis.** Maria T. Carilli. "Genetic Interrogation of Expression Regulation." PhD thesis, California Institute of Technology, Pasadena, California, 2026. Defended May 18, 2026. ([original](https://thesis.library.caltech.edu/18729/)). Rights: CC BY-NC-ND 4.0 — no adaptation permitted, not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Genetic Interrogation of Expression Regulation

## What this covers

A Caltech PhD thesis in computational biology developing stochastic models of transcription and a
genetic framework for cis versus trans gene regulation, combined to map regulatory differences
across eight genetically diverse founder mouse strains, eight tissues, and tens of thousands of
genes.

## The question

GWAS link genetic variants to disease and traits, but most significant variants sit in noncoding
DNA whose function is opaque. The usual intermediate step, linking variants to gene expression
(eQTL studies), is largely restricted to variants near a gene (cis), because testing all distal
(trans) candidates against all genes in all cell types is computationally and statistically
prohibitive — and even a successful eQTL hit says nothing about which cellular process
(transcription, splicing, degradation) a variant disturbs, since it rests on mean expression alone.
The thesis targets three linked problems: establishing that trans regulation exists for a gene
without an exhaustive variant search, resolving regulation at single-cell and tissue resolution,
and moving past mean expression to identify which biophysical process a genetic difference affects.

## The approach

Single-cell RNA counts are modeled as outcomes of stochastic (chemical master equation) processes
of transcription, splicing and degradation, rather than measurements collapsed to a per-gene mean;
fitting such models to the full count distribution recovers kinetic parameters — burst size,
splicing rate, degradation/export rate — invisible to mean-based differential expression. Since
most such models lack closed-form solutions, the thesis builds neural-network approximators
(kernel weight regression) fast enough for genome-wide use, and embeds the same likelihoods in a
variational-autoencoder architecture (biVI) to scale to modern datasets. Separately, it develops a
coordinate-geometry and regression framework, applied to homozygous parental strains and their F1
hybrids, testing whether an expression difference is cis or trans regulated without identifying the
causal variant. An earlier chapter applies a related idea to dimensionality reduction: contrasting
the variance structure of target and background data via a Rayleigh quotient ("rhoPCA") recovers
signal that comparing means, or standard PCA, misses. The final chapters combine these pieces,
applying the cis/trans test to fitted biophysical parameters across eight founder mouse strains.

## What it found

**Chapter II** reformulates contrastive PCA as a generalized eigenvalue (Rayleigh quotient)
problem, avoiding the original's non-physical negative variances and tunable contrast parameter. On
a mouse kidney dataset it recovered known sex-biased expression patterns and ran orders of
magnitude faster than standard contrastive PCA as sample/feature counts grew; an extension handles
longitudinal data.

**Chapter III** shows fitting chemical master equation models (via the authors' Monod package) to
scRNA-seq distributions surfaces changes invisible to mean expression. In a radiation-recovery
dataset, 380 genes showed a significant change in a kinetic parameter but not in mean mature
expression, versus 157 the reverse and 127 both; comparing minimal transcription models across
cortical cell types showed consistent differences in best-fitting model, suggesting real biological
variety in mechanism.

**Chapter IV** develops kernel weight regression networks approximating the joint nascent/mature
distribution these models predict. The fastest variant was about eight times faster than a
moderately fine numerical solver at comparable accuracy, and nearly an order of magnitude more
accurate than a coarser, similarly fast solver; a second variant trades accuracy for further speed.

**Chapter V** embeds the same likelihoods in a scVI-style variational autoencoder (biVI), learning
cell-type structure and per-gene kinetic parameters jointly. On mouse cortex data it recovered
marker-gene-specific parameter differences and, via Bayes-factor testing, found hundreds of genes
per cell subclass differing significantly in burst size or degradation rate with no corresponding
mean-expression difference — changes a standard pipeline would miss.

**Chapter VI** introduces a transformed coordinate system for parent/hybrid expression ratios, with
binomial and GLM-based tests, assigning cis/trans regulation from cross data without a tunable
threshold. Reapplied to two published datasets, it revised the original calls substantially: one
dataset's 57,253 reported trans-regulated genes fell to 39,063, and another's 478 cis-assigned
genes rose to 877. Estimating "proportion cis" from a regression slope, rather than the
geometrically correct angle, can be off by up to 57% in relative terms.

**Chapter VII** applies the biophysical models and cis/trans test jointly to eight founder mouse
strains across eight tissues (92 cell types, 30,763 genes) — called the largest analysis of
single-cell biophysical mechanism the author knows of. Cis regulation dominates differences in
burst size, splicing rate and export rate (52.2%, 52.8%, 62% of assignments), with trans next most
common; patterns vary by strain, tissue and cell type, and genes such as *Ptprd* show strain- and
cell-type-specific signatures in cortical neurons.

**Chapter VIII** closes by reviewing the arc from Mendel to genome-scale single-cell biophysics,
reflecting that simple, few-parameter models, not large ones, most changed the author's own
assumptions about a regulatory process during the PhD.

## Limits and context

The thesis cautions against over-reading its own tests: rejecting a "purely cis" or "purely trans"
null shows only that the alternative cannot be the sole explanation, not that it is true, and
comparing "significant" gene counts across cell types with very different nuclei numbers risks
mistaking low statistical power for absence of regulation. Chapter VII calls its splicing model
deliberately simple relative to what longer-read sequencing could support, an experimental rather
than theoretical limitation. More broadly, it argues against analyzing single-cell data via
heuristic summaries (fold-change on means) detached from a model of how the data were generated,
framing this as a tension between an "algorithmic modeling" and "stochastic data modeling" culture
in genomics, and offers this work as a genome-scale argument for the latter.

## Citation

Maria T. Carilli. *Genetic Interrogation of Expression Regulation.* PhD thesis, California
Institute of Technology, Pasadena, California, 2026. Defended May 18, 2026. Available at
<https://thesis.library.caltech.edu/18729/>.
