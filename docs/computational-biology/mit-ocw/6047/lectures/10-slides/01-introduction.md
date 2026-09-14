---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/10-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

6.047/6.878 Computational Biology: Genomes, Networks, Evolution

#### **Lecture 10 Regulatory motif discovery and target identification**

1

###### **Module III: Epigenomics and gene regulation**

- Computational Foundations – L10: Gibbs Sampling: between EM and Viterbi training – L11: Rapid linear-time sub-string matching – L11: Multivariate HMMs

– L12: Post-transcriptional regulation

- Biological frontiers: – L10: Regulatory motif discovery, TF binding – L11: Epigenomics, chromatin states, differentiation

   - L12: Post-transcriptional regulation

2

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo

2. Expectation maximization: Motif matrixpositions – E step: Estimate motif positions Zij from motif matrix

– M step: Find max-likelihood motif from all positions Zij

3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

- More likely to find global maximum, easy to implement

- 4. Evolutionary signatures for _de novo_ motif discovery – Genome-wide conservation scores, motif extension

- – Validation of discovered motifs: functional datasets

5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score

– Foreground vs. background. Real vs. control motifs.

3

###### **Regulatory motif discovery**


<!-- Start of picture text -->
GAL1<br>Gal4  Gal4<br>Mig1<br>ATGACTAAATCTCATTCAGAAGAA<br>CGG  CCG  CGG  CCG  CCCCW<br><!-- End of picture text -->

- Regulatory motifs

   - Genes are turned on / off in response to changing environments

   - No direct addressing:  subroutines (genes) contain sequence tags (motifs)

   - Specialized proteins (transcription factors) recognize these tags

- What makes motif discovery hard?

   - Motifs are short (6-8 bp), sometimes degenerate

   - Can contain any set of nucleotides (no ATG or other rules)

   - Act at variable distances upstream (or downstream) of target gene

4

###### **The regulatory code: All about regulatory motifs**


**5’-UTR**

**3’-UTR**

**Enhancer regions Promoter motifs Splicing signals Motifs at RNA level Where in the body? When in time? Which variants? Which subsets?**

- The parts list:  ~20-30k genes

   - Protein-coding genes, RNA genes (tRNA, microRNA, snRNA)

- The circuitry:  constructs controlling gene usage – Enhancers, promoters, splicing, post-transcriptional motifs

- The regulatory code, complications:

   - Combinatorial coding of ‘unique tags’

      - Data-centric encoding of addresses

   - Overlaid with ‘memory’ marks

      - Large-scale on/off states

   - Modulation of the large-scale coding

      - Post-transcriptional and post-translational information

- Today: discovering motifs in co-regulated promoters and _de novo_ motif discovery & target identification

5

**TFs use DNA-binding domains to recognize specific DNA sequences in the genome**


DNA-binding domain of _Engrailed_


<!-- Start of picture text -->
“Logo” or  “motif”<br>TAATTA<br><!-- End of picture text -->


<!-- Start of picture text -->
TAATTA  CACGTG<br>AGATAAGA<br>TCATTA<br><!-- End of picture text -->

Courtesy of Elsevier, Inc., http://www.sciencedirect.com. Used with permission. Source: Berger, Michael F. et al. "Variation in homeodomain DNA binding revealed by high-resolution analysis of sequence preferences." Cell 133, no. 7 (2008): 1266-1276.

6

###### **Disrupted motif at the heart of FTO obesity locus**


###### **_Strongest association with obesity_**

###### **_C-to-T disruption of AT-rich regulatory motif_**


**Lean**

**Obese**

**_Restoring motif restores thermogenesis_**

Courtesy of Manolis Kellis. Used with permission.

7

###### **Regulator structure**  **recognized motifs**

- Proteins ‘feel’ DNA

   - Read chemical properties of bases

   - Do NOT open DNA (no base complementarity)

- 3D Topology dictates specificity

   - Fully constrained positions:  every atom matters

   - “Ambiguous / degenerate” positions  loosely contacted

- Other types of recognition

   - MicroRNAs: complementarity

   - Nucleosomes: GC content

   - RNAs: structure/seqn combination


© Garland Publishing. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

8

###### **Motifs summarize TF sequence specificity**


- Summarize information

- Integrate many positions

- Measure of information


- Distinguish motif vs. motif instance

- Assumptions:

   - Independence

   - Fixed spacing

9

###### **Experimental factor-centric discovery of motifs**


Courtesy of the authors. Used with permission. Source: Ray, Partha, and Rebekah R. White. "Aptamers For targeted drug delivery." Pharmaceuticals 3, no. 6 (2010): 1761-1778.


© Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http:// ocw.mit.edu/help/faq-fair-use/. Source: Liu, Xiao et al. "DIP-chip: rapid and accurate determination of DNA-binding specificity." Genome Research 15, no. 3 (2005): 421-427.


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/ help/faq-fair-use/.

**SELEX (Systematic Evolution of Ligands by Exponential Enrichment; Klug & Famulok, 1994)**

**DIP-Chip (DNAimmunoprecipitatio n with microarray detection; Liu et al., 2005)**

**PBMs (Protein binding microarrays; Mukherjee, 2004) Double stranded DNA arrays**

10

###### **Approaches to regulatory motif discovery**

- Expectation Maximization (e.g. MEME)

   - Iteratively refine positions / motif profile

###### Regionbased motif discovery

- Gibbs Sampling (e.g. AlignACE)

   - Iteratively sample positions / motif profile

- Enumeration with wildcards (e.g. Weeder) – Allows global enrichment/background score

- Peak-height correlation (e.g. MatrixREDUCE) – Alternative to cutoff-based approach

Genomewide

- Conservation-based discovery (e.g. MCS) – Genome-wide score, up-/down-stream bias

- Protein Domains (e.g. PBMs, SELEX)

   - In vitro motif identification, seq-/array-based

_In vitro_ / _trans_

11

###### **Motifs are not limited to DNA sequences**

- Splicing Signals at the RNA level

   - Splice junctions

   - – Exonic Splicing Enhancers (ESE)

– Exonic Splicing Surpressors (ESS)

- Domains and epitopes at the Protein level

   - Glycosylation sites

   - Kinase targets

   - Targetting signals

   - MHC binding specificities

- Recurring patterns at the physiological level – Expression patterns during the cell cycle

   - Heart beat patterns predicting cardiac arrest

      - Final project in previous year, now used in Boston hospitals!

   - Any probabilistic recurring pattern

12

---

[Up: contents](index.md) · [Challenges in regulatory genomics →](02-challenges-in-regulatory-genomics.md)
