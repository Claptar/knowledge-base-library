---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7.91 / 20.490 / 6.874 / HST.506 7.36 / 20.390 / 6.802 C. Burge Lecture #9 Mar. 6, 2014

Modeling & Discovery of Sequence Motifs

1

###### Modeling & Discovery of Sequence Motifs

- Motif Discovery with Gibbs Sampling Algorithm

- Information Content of a Motif

- Parameter Estimation for Motif Models (+ others)

**Background for today:**

NBT Primers on Motifs, Motif Discovery. Z&B Ch. 6. Optional: Lawrence Gibbs paper, Bailey & Elkan MEME paper **For Tuesday:** NBT primer on HMMs, Z&B on HMMs (various pp.) Rabiner tutorial on HMMs

2

#### **What is a (biomolecular) sequence motif?**

A pattern common to a set of DNA, RNA or protein sequences that share a common biological property, such as functioning as binding sites for a particular protein

Ways of representing motifs

- Consensus sequence

- Regular expression

- Weight matrix/PSPM/PSSM

- More complicated models

3

#### **Where do motifs come from?**

   - Sequences of known common function

   - Cross-linking/pulldown experiments

   - in vitro binding / SELEX experiments

   - Multiple sequence alignments / comparative genomics

      - Why are they important?

- Identify proteins, DNAs or RNAs that have a specific property

- Can be used to infer which factors regulate which genes

- Important for efforts to model gene expression

4

#### **Examples of Protein Sequence Motifs**


© FUNPEC-RP. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Ericsson, A. O., L. O. Faria, et al. "TcZFP8, A Novel Member of the Trypanosoma Cruzi CCHC Zinc Finger Protein Family with Nuclear Localization." _Genetics and Molecular Research_ 5, no. 3 (2006): 553-63.

CX2CX4HX4C

###### Zinc finger (DNA binding)


Courtesy of the authors. License: CC-BY-NC. Source: Bentem, Van, Sergio de la Fuente, et al. "Phosphoproteomics Reveals Extensive inVivo Phosphorylation of Arabidopsis Proteins Involved in RNA Metabolism." _Nucleic Acids Research_ 34, no. 11 (2006): 3267-78.

Ericsson et al. Genet. Mol. Res. 2006

- Phosphorylation sites ( _Arabidopsis_ SRPK4)

de la Fuente van Bentem et al. NAR 2006

5

#### **Core Splicing Motifs (Human)**

- 5’ splice site

branch site


3’ splice site


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

6

Weight Matrix with Background Model 5’ splice site motif (+) Background (-) Con: C A G … G T **Pos Generic Pos -3 -2 -1 … +5 +6** A 0.25 A **0.3 0.6** 0.1 … 0.1 0.1 C 0.25 C **0.4** 0.1 0.0 … 0.1 0.2 G 0.25 G 0.2 0.2 **0.8 … 0.8** 0.2 T 0.25 T 0.1 0.1 0.1 … 0.0 **0.5** S = S1 S2 S3 S4 S5 S6 S7 S8 S9 P(S|+) = P-3(S1)P-2(S2)P-1(S3) ••• P5(S8)P6(S9) **Odds Ratio:** R = P(S|-) = Pbg(S1)Pbg(S2)Pbg(S3) ••• Pbg(S8)Pbg(S9) Background model homogenous, assumes independence

7

Ways to describe a motif Common motif adjectives: exact/precise _versus_ degenerate

- strong _versus_ weak (good _versus_ lousy)

high information content _versus_ low information content low entropy _versus_ high entropy

8

---

[Up: contents](index.md) · [Statistical (Shannon) Entropy →](02-statistical-shannon-entropy.md)
