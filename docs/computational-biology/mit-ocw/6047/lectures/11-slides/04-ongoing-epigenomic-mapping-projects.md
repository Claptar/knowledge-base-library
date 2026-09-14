---
title: Ongoing epigenomic mapping projects
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ongoing epigenomic mapping projects

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Mapping multiple modifications

- In multiple cell types

- In multiple individuals

- In multiple species

•First wave published

•Lots more in pipeline

•Time for analysis!

- In multiple conditions

- With multiple antibodies

- Across the whole genome

10

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

- Antibodies, ChIP-Seq, data generation projects, raw data

- 2. Primary data processing: Read mapping, Peak calling

   - Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

   - – Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

   - Promoter, transcribed, intergenic, repressed, repetitive states

4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

– Capturing dependencies and state-conditional mark independence

5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

– Defining activity profiles for linking enhancer regulatory networks

(Future: Chromatin states to interpret disease-associated variants)

11

#### **ChIP-seq review**

###### **(Chromatin immunoprecipitation followed by sequencing)**


<!-- Start of picture text -->
antibody<br><!-- End of picture text -->


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Park, Peter J. "ChIP–seq: advantages and challenges of a maturing technology." Nature Reviews Genetics 10, no. 10 (2009): 669-680.

© Illumina, Inc. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Lefrançois, Philippe et al. "Efficient yeast ChIP-Seq using multiplex short-read DNA sequencing." BMC genomics 10, no. 1 (2009): 1.

Bar-coded multiplexed sequencing

12

#### ChIP-chip and ChIP-Seq technology overview


<!-- Start of picture text -->
or modification<br>Image adapted from Wikipedia<br><!-- End of picture text -->

Modification-specific antibodies  Chromatin Immuno-Precipitation followed by:  ChIP-chip: array hybridization 13 ChIP-Seq: Massively Parallel Next-gen Sequencing

#### ChIP-Seq Histone Modifications: What the

#### raw data looks like


- Each sequence tag is 30 base pairs long

- Tags are mapped to unique positions in the ~3 billion base reference genome

- Number of reads depends on sequencing depth. Typically on the order of 10 million mapped reads.

14

###### **Summarize multiple marks into chromatin states**


###### **Chromatin state track summary**


© WashU Epigenome Browser. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

WashU Epigenome Browser **_ChromHMM: multi-variate hidden Markov model_**

15

---

[← 100s of histone tail modifications](03-100s-of-histone-tail-modifications.md) · [Up: contents](index.md) · [Mapping millions of short reads to the genome →](05-mapping-millions-of-short-reads-to-the-genome.md)
