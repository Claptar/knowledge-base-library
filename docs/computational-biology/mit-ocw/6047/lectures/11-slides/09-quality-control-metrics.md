---
title: Quality control metrics
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Quality control metrics

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

ChIP vs. Input DNA Read quality Mappability Library complexity

26

## **ENCODE uniform processing pipeline)**


<!-- Start of picture text -->
Mapped reads<br>Uniform Peak Calling Pipeline  Signal Generation<br>(read extension and mappability correction)<br>Good   reproducibility Poor reproducibility<br>Segmentation<br>Rep1<br>IDR Processing, Quality control and Blacklist Filtering<br>ChromHMM/Segway<br>Self Organising Maps<br>Motif Discovery  Co-association  Signal Aggregation<br>analysis  over elements<br>Rep2<br><!-- End of picture text -->

© sources unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

27

## **QC1: Use of input DNA as control dataset**


<!-- Start of picture text -->
signal<br>background<br><!-- End of picture text -->

      - © sources unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Challenge:**

   - Even without antibody: Reads are **<u>not</u>** uniformly scattered

- **Sources of bias in input dataset scatter:**

   - Non-uniform fragmentation of the genome

   - Open chromatin fragmented more easily than closed regions

   - Repetitive sequences over-collapsed in the assembled genome.

- **How to control for these biases:**

   - Remove portion of DNA sample before ChIP step

   - Carry out control experiment without an antibody (input DNA)

   - Fragment input DNA, sequence reads, map, use as background

28

##### **QC2: Read-level sequencing quality score Q>10**

###### **Read quality histograms**

###### High quality reads


average base score per position

- Each column is a color-coded histogram

- Encodes fraction of all mapped reads that have base score Q (y-axis) at each position (xaxis)

- Darker blue = higher density

###### Low quality reads


- Read quality tends to drop towards the ends of reads

- Low average per base score implies greater probabilty of mismappings.

- Typically, reject reads whose average score Q < 10

29

#### **QC3: Fraction of short reads mapped >50%**

**Reads can map to:**

- exactly one location (uniquely mapping)

- • multiple locations (repetitive or multi-mapping)

- • no locations (unmappable)

###### **Dealing with multiply-mapping reads:**

unique

GACT multiple **ACCT** none **TTTT**

GACTACCTTTACCT

   - Conservative approach: do not assign to any location

   - Probabilistic approach: assign fractionally to all locations

   - Sampling approach: pick one location at random, averages across many reads

   - • EM approach: map according to density, estimated from unambiguous reads

   - Pair-end approach: use paired end read to resolve ambiguities in repeat reads

- **Absence of reads in a region could be due to:**

   - No assembly coverage in that region (e.g. peri-centromeric region)

   - Too many reads mapping to this location (e.g. repetitive element)

   - No activity observed in this location (e.g. inactive / quiescent / dead regions)

- **Dealing with mappability biases:**

   - ‘Black-listed’ regions, promiscuous across many datasets

   - ‘White-listed’ regions, for which at least some dataset has unique reads

   - Treat unmappable regions as missing data, distinguish from ‘empty’ regions

30

##### **QC4: Library complexity: non-redundant fraction**

###### **Library complexity**


<!-- Start of picture text -->
M1<br>M1/M2 should be large<br>M2<br>1  2  3  5  7  9  11<br>No. of duplicates<br>No. of distinct reads<br><!-- End of picture text -->

- © sources unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**How many distinct uniquely mapping read? How many duplicates?**

If your sample does not contain sufficient DNA and/or you over-sequence, you will simply be repeatedly sequencing PCR duplicates of a restricted pool of distinct DNA fragments. This is known a **low-complexity library** and is not desirable.

- **Histogram of no. of duplicates**

- Non-redundant fraction (NRF) =   No. of ‘distinct’ unique-mapping reads No. of unique-mapping reads

• NRF should be > 0.8 when 10M < #reads < 80M unique-mapping reads

31

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

- Antibodies, ChIP-Seq, data generation projects, raw data

- 2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

- – Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

- 3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

   - Promoter, transcribed, intergenic, repressed, repetitive states

4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

– Capturing dependencies and state-conditional mark independence

5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

– Defining activity profiles for linking enhancer regulatory networks

(Future: Chromatin states to interpret disease-associated variants)

32

---

[← Searching for an Exact Match](08-searching-for-an-exact-match.md) · [Up: contents](index.md) · [Cross-correlation analysis →](10-cross-correlation-analysis.md)
