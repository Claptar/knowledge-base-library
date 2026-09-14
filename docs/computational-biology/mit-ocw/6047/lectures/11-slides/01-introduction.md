---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

6.047/6.878/HST.507 Computational Biology: Genomes, Networks, Evolution

###### **Lecture 11 - Epigenomics** read mapping – peak calling – multivariate HMMs

1

###### **Module III: Epigenomics and gene regulation**

- Computational Foundations – L10: Gibbs Sampling: between EM and Viterbi training – L11: Rapid linear-time sub-string matching – L11: Multivariate HMMs

– L12: Post-transcriptional regulation

- Biological frontiers: – L10: Regulatory motif discovery, TF binding – L11: Epigenomics, chromatin states, differentiation

   - L12: Post-transcriptional regulation

2

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics

   - Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Promoter, transcribed, intergenic, repressed, repetitive states

- 4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

- – Capturing dependencies and state-conditional mark independence

- 5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

- – Defining activity profiles for linking enhancer regulatory networks

- (Future: Chromatin states to interpret disease-associated variants)

3

---

[Up: contents](index.md) · [One Genome – Many Cell Types →](02-one-genome-many-cell-types.md)
