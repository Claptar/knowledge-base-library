---
title: Lecture 7
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 7

### ChIP-seq Analysis
### Irreproducible Discovery Rate (IDR) Analysis

Foundations of Computational Systems Biology
David K. Gifford

---

## Transcription factors regulate gene expression

© Emw on wikipedia. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Transcription factors are proteins that bind to specific DNA sequences and act as molecular switches (Pit1 shown)**

**Humans have ~2000 gene regulators.**

---

## Gene Regulation: DNA -> RNA -> Protein

Regulators Gene

mRNA

Protein

**What are the gene regulators that control gene expression?**
**At what genes do these regulators operate?**

---

## Gene regulatory networks provide key insight into cellular function

Transcriptional regulatory network information will:

- **reveal how cellular processes are connected and coordinated**
- **suggest new strategies to manipulate phenotypes and combat disease**

Courtesy of Richard Young. Used with permission.

---

## ChIP-seq data reveals where TFs bind to the genome

Regulators Gene

mRNA
ChIP-seq data
Protein

---

## ChIP-seq protocol

- Crosslink proteins to binding sites in living cells
- Harvest cells and fragment DNA
- Enrich for protein-bound DNA fragments with antibodies $\longrightarrow$ Sequence ChIP DNA
- $\longrightarrow$ Sequence whole cell extract (WCE) DNA (control)

---

## A binding event produces a distribution of reads around its site

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Kharchenko, Peter V., Michael Y. Tolstorukov, et al. "Design and Analysis of ChIP-seq Experiments for DNA-binding Proteins." Nature biotechnology 26, no. 12 (2008): 1351-9.

---

## Data from two binding events
### mES cell Oct4 ChIP Seq

Sox2

---

## The spatial distribution of reads can be used to improve spatial resolution of prediction and de-convolve joint binding events

**ChIP-Seq reads are independently generated from a set of spatially discrete binding events**

---

## GPS addresses the challenges in ChIP-Seq analysis

- **ChIP DNA are randomly fragmented** $\Longrightarrow$ **Model the spatial distribution of the reads**
- **Mixture of Reads from different events** $\Longrightarrow$ **Construct a mixture model**

Courtesy of Wang and Zhang. Licensed CC-BY.
Source: Wang, Xi, and Xuegong Zhang. "Pinpointing Transcription Factor Binding Sites from ChIP-seq Data with SeqSite." BMC Systems Biology 5, no. Suppl 2 (2011): S3.

---

## GPS estimates the spatial distribution of the reads

+ strand
- strand
Location with respect to binding site

---

## GPS estimates the spatial distribution of the reads

$$p(r_i | b_j) = p(r_i | z_{ij} = 1) = \text{emp}((-1)^{S_i}(r_i - b_j))$$

$r_i$: a read at position $r_i$
$b_j$: a binding event at position $b_j$
$\text{emp}(d)$: the empirical spatial distribution
$S_i = 0$ for forward strand
$= 1$ for reverse strand

---

---

[Up: contents](index.md) · [GPS probabilistically models ChIP-Seq read spatial distribution using a mixture model →](02-gps-probabilistically-models-chip-seq-read-spatial-distribut.md)
