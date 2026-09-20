---
title: Analysis of Genome Wide Association Studies (GWAS)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/20-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Analysis of Genome Wide Association Studies (GWAS)

### Lecture 20

David K. Gifford

Massachusetts Institute of Technology

---

## Today's Narrative Arc

1. We can discover human variants that are associated with a phenotype by studying the genotypes of case and control populations
   - **Approach 1** – Use allelic counts from SNP arrays (SNPs called from microarray data)
   - **Approach 2** – Use read counts from sequencing (multiple reads per variant per individual)
2. We can prioritize variants based upon their estimated importance
3. Follow up confirmation is important because correlation is not equivalent to causality

---

## Today's Computational Approaches

1. Contingency tables for allelic association tests and genotypic association tests.
2. Methods of testing - Chi-Square tests, Fisher's exact test
3. Likelihood based tests of case/control posterior genotypes

---

## Out of scope for today

1. Non-random genotyping failure
2. Methods to correct for population stratification
3. Structural variants (SVs) and copy number variations (CNVs)

---

### Allele Frequency

* **50%**
  * **High-frequency polymorphisms**
    * *Eg: many now known*
    * *HapMap*
    * *First generation arrays*
* **5%**
  * **Lower-frequency polymorphisms**
    * *Eg: CFTR delta 508*
    * *PCSK9 C679X*
    * *1000 Genomes Project*
    * *New arrays, imputation*
* **0.5%**
* **0.05%**
  * **Rare Mutations**
    * *Eg: most mendelian*
    * *MC4R, ABCA1*
    * *1q21.1 in SCZ*
    * *Direct sequencing*
    * *Array-based detection (CNV)*

*(Rarer Alleles, Stronger Effects)*

Mendelian traits are caused by a single gene

Courtesy of David Altshuler. Used with permission.

Slide courtesy of David Altshuler, HMS/Broad

---

Animation: Itsik Pe'er, Columbia

Time $\longrightarrow$

---

## Disease cases | Healthy control

---

## Disease cases | Healthy controls

Association between genotype and phenotype

---

## Age-related macular degeneration

Cohort – 2172 unrelated European descent individuals at least 60 years old

2004: Little known about cause of AMD

* **934 controls** (Normal Vision)
* **1238 cases** (Age-related Macular Degeneration)

Photographs are in the public domain.

---

## SNP rs1061170

1238 individuals with AMD and 934 controls
2172 individuals / 4333 alleles

| Allele | Cases (with AMD) | Controls (without AMD) | Total Alleles |
| :--- | :--- | :--- | :--- |
| C | 1522 (a) | 670 (b) | 2192 |
| T | 954 (c) | 1198 (d) | 2152 |
| Total Alleles | 2476 | 1868 | 4344 |

\$\$\chi^2 = \frac{(ad - bc)^2

---

[Up: contents](../index.md)

## Figures

Extracted from the original PDF. They are listed by the page they came from rather
than placed in the text: the conversion does not record where on the page each one
sat.

![Figure from page 1 of the original](20-slides/figures/p001-1.jpeg)

![Figure from page 5 of the original](20-slides/figures/p005-1.jpx)

![Figure from page 6 of the original](20-slides/figures/p006-1.jpeg)

![Figure from page 7 of the original](20-slides/figures/p007-1.jpeg)

![Figure from page 8 of the original](20-slides/figures/p008-1.jpeg)

![Figure from page 9 of the original](20-slides/figures/p009-1.jpeg)

![Figure from page 9 of the original](20-slides/figures/p009-2.jpeg)

![Figure from page 10 of the original](20-slides/figures/p010-1.jpeg)

![Figure from page 11 of the original](20-slides/figures/p011-1.jpeg)

![Figure from page 12 of the original](20-slides/figures/p012-1.jpeg)

![Figure from page 14 of the original](20-slides/figures/p014-1.jpeg)

![Figure from page 14 of the original](20-slides/figures/p014-2.jpeg)

![Figure from page 14 of the original](20-slides/figures/p014-3.jpeg)

![Figure from page 15 of the original](20-slides/figures/p015-1.jpeg)

![Figure from page 16 of the original](20-slides/figures/p016-1.jpeg)

![Figure from page 17 of the original](20-slides/figures/p017-1.jpeg)

![Figure from page 18 of the original](20-slides/figures/p018-1.jpeg)

![Figure from page 19 of the original](20-slides/figures/p019-1.jpeg)

![Figure from page 20 of the original](20-slides/figures/p020-1.jpeg)

![Figure from page 23 of the original](20-slides/figures/p023-1.png)

![Figure from page 24 of the original](20-slides/figures/p024-1.png)

![Figure from page 25 of the original](20-slides/figures/p025-1.png)

![Figure from page 26 of the original](20-slides/figures/p026-1.jpeg)

![Figure from page 27 of the original](20-slides/figures/p027-1.png)

![Figure from page 28 of the original](20-slides/figures/p028-1.jpeg)

![Figure from page 29 of the original](20-slides/figures/p029-1.png)

![Figure from page 30 of the original](20-slides/figures/p030-1.png)

![Figure from page 31 of the original](20-slides/figures/p031-1.png)

![Figure from page 32 of the original](20-slides/figures/p032-1.jpeg)

![Figure from page 33 of the original](20-slides/figures/p033-1.jpeg)

![Figure from page 34 of the original](20-slides/figures/p034-1.png)

![Figure from page 36 of the original](20-slides/figures/p036-1.jpeg)

![Figure from page 37 of the original](20-slides/figures/p037-1.png)

![Figure from page 38 of the original](20-slides/figures/p038-1.png)

![Figure from page 39 of the original](20-slides/figures/p039-1.jpeg)

![Figure from page 44 of the original](20-slides/figures/p044-1.png)

![Figure from page 45 of the original](20-slides/figures/p045-1.jpeg)

![Figure from page 46 of the original](20-slides/figures/p046-1.png)

![Figure from page 47 of the original](20-slides/figures/p047-1.png)

![Figure from page 48 of the original](20-slides/figures/p048-1.png)

![Figure from page 49 of the original](20-slides/figures/p049-1.png)

![Figure from page 50 of the original](20-slides/figures/p050-1.png)

![Figure from page 52 of the original](20-slides/figures/p052-1.jpeg)

![Figure from page 53 of the original](20-slides/figures/p053-1.jpeg)

![Figure from page 54 of the original](20-slides/figures/p054-1.jpeg)

![Figure from page 56 of the original](20-slides/figures/p056-1.jpeg)

![Figure from page 57 of the original](20-slides/figures/p057-1.jpeg)

![Figure from page 57 of the original](20-slides/figures/p057-2.jpeg)

![Figure from page 58 of the original](20-slides/figures/p058-1.jpeg)

![Figure from page 58 of the original](20-slides/figures/p058-2.jpeg)

![Figure from page 60 of the original](20-slides/figures/p060-1.jpeg)

