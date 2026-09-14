---
title: Peak Calling
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Peak Calling

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Continuous signal  Intervals

40

## **Peak calling: detect regions of enrichment**


   - © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

   - **Goal:** Transform read counts into **normalized intensity signal Steps:**

1. Estimate fragment-length _f_ using strand cross-correlation analysis

      2. Extend each read from 5’ to 3’ direction to fragment length _f_

3. Sum intensity for each base in ‘extended reads’ from both strands

   4. Perform same operation on input-DNA control data (correct for sequencing depth differences)

5. Calculate enrichment ratio value for every position in the genome

**Result:** Enrichment fold difference for ChIP / control signal

41

## **Peak calling: identify discrete intervals**


Courtesy of the authors. License: CC BY. Source: Wilbanks, Elizabeth G. and Marc T. Facciotti. "Evaluation of algorithm performance in ChIP-seq peak detection." PLOS ONE 5, no. 7 (2010): e11471.

42

## **Peak calling thresholds**

###### **Poisson p-value thresholds**

- Read count model: Locally-adjusted’ Poisson distribution 𝑥 exp −𝜆𝑙𝑜𝑐𝑎𝑙

- 𝑃 𝑐𝑜𝑢𝑛𝑡= 𝑥=<sup>𝜆𝑙𝑜𝑐𝑎𝑙</sup> 𝑥!

- λlocal = max(λBG, [λ1k,] λ5k, λ10k) estimated from control data • Poisson _p_ -value = 𝑃 𝑐𝑜𝑢𝑛𝑡≥𝑥

   - _q_ -value : Multiple hypothesis correction

**Peaks:** Genomic locations that pass a user-defined _p_ -value (e.g. 1e-5) or _q_ -value (e.g. 0.01) threshold

###### **Empirical False discovery rates**

   - Swap ChIP and input-DNA tracks

      - Recompute _p_ -values

- At each _p_ -value, eFDR = Number of control peaks / Number of ChIPpeaks

   - Use an FDR threshold to call peaks

43

## **Issues with peak calling thresholds**

Cannot set a universal threshold for empirical FDRs and p-values

- Depends on ChIP and input sequencing depth

   - Depends on binding ubiquity of factor

###### **(at FDR = 1% cutoff)**

- Stronger antibodies get an advantage

FDRs quite unstable

- Small changes in threshold => massive changes in peak numbers

Difficult to compare results across peak callers with a fixed threshold

- Different methods to compute eFDR or q- values

###### **# peaks called by SPP**

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

44

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

- Antibodies, ChIP-Seq, data generation projects, raw data

- 2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

- – Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

- 3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Promoter, transcribed, intergenic, repressed, repetitive states

- 4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

- – Capturing dependencies and state-conditional mark independence

- 5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

- – Defining activity profiles for linking enhancer regulatory networks

- (Future: Chromatin states to interpret disease-associated variants)

45

---

[← Cross-correlation analysis](10-cross-correlation-analysis.md) · [Up: contents](index.md) · [Selecting meaningful peaks using reproducibility →](12-selecting-meaningful-peaks-using-reproducibility.md)
