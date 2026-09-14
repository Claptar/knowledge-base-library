---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### 6.047/6.878/HST.507 Computational Biology: Genomes, Networks, Evolution

# **Lecture 2 Sequence Alignment and Dynamic Programming**

1

##### **Module 1: Aligning and modeling genomes**


- Module 1: Computational foundations

   - Dynamic programming: exploring exponential spaces in poly-time

   - Introduce Hidden Markov Models (HMMs): Central tool in CS

   - HMM algorithms: Decoding, evaluation, parsing, likelihood, scoring

- This week: Sequence alignment / comparative genomics – Local/global alignment: infer nucleotide-level evolutionary events

   - Database search: scan for regions that may have common ancestry

- Next week: Modeling genomes / exon / CpG island finding – Modeling class of elements, recognizing members of a class

   - Application to gene finding, conservation islands, CpG islands

2

#### **Genome-wide alignments reveal orthologous segments**


Courtesy of Don Gilbert. Used with permission.


<!-- Start of picture text -->
100 genes<br><!-- End of picture text -->

   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Genome-wide alignments span entire genome**

- **Comparative identification of functional elements**

3

#### **Comparative genomics reveals conserved regions**


- © source unknown. All rights reserved. This content is excluded from our Creative

Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Comparative genomics can reveal functional elements** – For example:  exons are deeply conserved to mouse, chicken, fish

   - Many other elements are also strongly conserved: exons / regulatory?

- **Develop methods for estimating the level of constraint**

   - Count the number of edit operations, number of substitutions and gaps

   - Estimate the number of mutations (including estimate of back-mutations)

   - Incorporate information about neighborhood: conservation ‘windows’

   - Estimate the probability of a constrained ‘hidden state’: HMMs next week

   - Use phylogeny to estimate tree mutation rate, or ‘rejected substitutions’

   - Allow different portions of the tree to have different rates: phylogenetics

4

---

[Up: contents](index.md) · [Evolutionary signatures for diverse functions →](02-evolutionary-signatures-for-diverse-functions.md)
