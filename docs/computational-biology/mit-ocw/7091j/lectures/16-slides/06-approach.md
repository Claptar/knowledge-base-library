---
title: Approach
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/16-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/16-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Approach

### mRNA levels do not predict protein levels

1,000 fold range of protein concentrations

$R^2 = 0.22$, $R_s = 0.46$

Protein expression levels (molecules/cell, log-scale base 10)
mRNA expression levels (arbitrary units, log-scale base 10)

© Royal Society of Chemistry. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.
Source: de Sousa Abreu, Raquel, Luiz O. Penalva, et al. "Global Signatures of Protein and mRNA Expression Levels." *Molecular Biosystems* 5, no. 12 (2009): 1512-26.
Raquel de Sousa Abreu, Luiz Penalva, Edward Marcotte and Christine Vogel, *Mol. BioSyst.*, 2009 DOI: 10.1039/b908315d

| | SpectrumMill | msInspect | msBID | NSAF | RPKM | Microarray |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SpectrumMill** | - | 0.91 (0.92) | 0.91 (0.91) | 0.90 (0.90) | 0.49 (0.51) | 0.36 (0.40) |
| **msInspect** | 0.91 (0.92) | - | 0.89 (0.91) | 0.87 (0.88) | 0.51 (0.53) | 0.40 (0.44) |
| **msBID** | 0.91 (0.91) | 0.89 (0.91) | - | 0.84 (0.89) | 0.54 (0.54) | 0.41 (0.42) |
| **NSAF** | 0.90 (0.90) | 0.87 (0.88) | 0.84 (0.89) | - | 0.51 (0.53) | 0.42 (0.44) |

Source: Ning, Kang, Damian Fermin, et al. "Comparative Analysis of Different Label-free Mass Spectrometry Based Protein Abundance Estimates and Their Correlation with RNA-Seq Gene Expression Data." *Journal of Proteome Research* 11, no. 4 (2012): 2261-71.
Kang Ning, Damian Fermin, and Alexey I. Nesvizhskii *J Proteome Res.* 2012 April 6; 11(4): 2261–2271.

---

## L18 Chromatin and DNase-seq Analysis

**Mutant**

**Wild-type**

Sequence Analysis

---

## Move upstream of transcription

Network integration

Epigenomic Data & Sequence Analysis

Interactome

DNA-binding proteins

mRNA

---

## 'Omic data don't agree

Toxic Compound, Mutation, Environmental Change

---

## Genetic vs. Expression Data

| Perturbation | Differentially expressed genes | Genetic hits | Number of overlapping genes |
| :--- | :--- | :--- | :--- |
| **Growth arrest (Hydroxyurea)** | 59 | 86 | 0 |
| **DNA damage (MMS)** | 198 | 1448 | 43 |
| **Protein biosynthesis block (Cycloheximide)** | 20 | 164 | 0 |
| **ER stress (Tunicamycin)** | 200 | 127 | 5 |
| **ATP synthesis block (Arsenic)** | 828 | 50 | 9 |
| **Fatty acid metabolism (oleate)** | 269 | 103 | 9 |
| **Gene inactivation (24 datasets, median shown)** | 27 | 130 | 0 |

Bridging high-throughput genetic and transcriptional data reveals cellular responses to alpha-synuclein toxicity
*Nature Genetics* Published online: 22 February 2009

---

---

[← A Bayesian Networks Approach for Predicting Protein-Protein Interactions from Genomic Data](05-a-bayesian-networks-approach-for-predicting-protein-protein.md) · [Up: contents](index.md) · [For 156 perturbations →](07-for-156-perturbations.md)
