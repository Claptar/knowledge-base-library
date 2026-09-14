---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/17-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

6.047/6.878/HST.507 Computational Biology: Genomes, Networks, Evolution

**Lecture 17 Comparative genomics I: Genome annotation using evolutionary signatures**

1

### **Module V: Comparative genomics and evolution**

- Today: Whole-genome comparative genomics

   - Evolutionary signatures for systematic genome annotation

- Next week: Phylogenetics and Phylogenomics

   - Distance-based and model-based phylogenetics approaches

   - Gene trees and species trees, reconciliation, coalescence

- Computational foundations:

   - Evolutionary rates and models of evolution

   - Dynamic programming on two-dimensional tree structures

   - Synteny-based alignment, genome assembly

2

### **Key goal: Evolution preserves functional elements**

||Gal4|
|---|---|
||Gal10<br>Gal1|
|<br> <br> <br> <br> <br>`Scer`<br>`Spar`<br>`Smik`<br>`Sbay`<br> <br>GAL1|`Scer   TTATATTGAATTTTCAAAAATTCTTACTTTTTTTTTGGATGGACGCAAAGAAGTTTAATAATCATATTACATGGCATTACCACCATATACA`<br>`Spar   CTATGTTGATCTTTTCAGAATTTTT-CACTATATTAAGATGGGTGCAAAGAAGTGTGATTATTATATTACATCGCTTTCCTATCATACACA`<br>`Smik   GTATATTGAATTTTTCAGTTTTTTTTCACTATCTTCAAGGTTATGTAAAAAA-TGTCAAGATAATATTACATTTCGTTACTATCATACACA`<br>`Sbay   TTTTTTTGATTTCTTTAGTTTTCTTTCTTTAACTTCAAAATTATAAAAGAAAGTGTAGTCACATCATGCTATCT-GTCACTATCACATATA`<br>`* * ****  * *  *   ** ** *  *   **           **  ** * *    *    **   **    *  * * ** * * *`<br>`TATCCATATCTAATCTTACTTATATGTTGT-GGAAAT-GTAAAGAGCCCCATTATCTTAGCCTAAAAAAACC--TTCTCTTTGGAACTTTCAGTAATACG`<br>`TATCCATATCTAGTCTTACTTATATGTTGT-GAGAGT-GTTGATAACCCCAGTATCTTAACCCAAGAAAGCC--TT-TCTATGAAACTTGAACTG-TACG`<br>`TACCGATGTCTAGTCTTACTTATATGTTAC-GGGAATTGTTGGTAATCCCAGTCTCCCAGATCAAAAAAGGT--CTTTCTATGGAGCTTTG-CTA-TATG`<br>`TAGATATTTCTGATCTTTCTTATATATTATAGAGAGATGCCAATAAACGTGCTACCTCGAACAAAAGAAGGGGATTTTCTGTAGGGCTTTCCCTATTTTG`<br>`**   ** ***  **** ******* **   *  *   *     *  *    *  *       **  **      * *** *    ***    *  *  *`<br>0<br>**TBP**<br>**GAL4**<br>**GAL4**<br>**GAL4**|
|`Scer`<br>`Spar`<br>`Smik`<br>`Sbay`<br> <br>|`CTTAACTGCTCATTGC-----TATATTGAAGTA`**`CGG`**`ATTAGAAGCCG`**`CCG`**`AG`**`CGG`**`GCGACAGCCCT`**`CCG`**`A`**`CGG`**`AAGACTCTCCT`**`CCG`**`TGCGTCCTCGTCT`<br>`CTAAACTGCTCATTGC-----AATATTGAAGTA`**`CGG`**`ATCAGAAGCCG`**`CCG`**`AG`**`CGG`**`ACGACAGCCCT`**`CCG`**`A`**`CGG`**`AATATTCCCCT`**`CCG`**`TGCGTCGCCGTCT`<br>`TTTAGCTGTTCAAG--------ATATTGAAATA`**`CGG`**`ATGAGAAGCCG`**`CCG`**`AA`**`CGG`**`ACGACAATTCC`**`CCG`**`A`**`CGG`**`AACATTCTCCT`**`CCG`**`CGCGGCGTCCTCT`<br>`TCTTATTGTCCATTACTTCGCAATGTTGAAATA`**`CGG`**`ATCAGAAGCTG`**`CCG`**`AC`**`CGG`**`ATGACAGTACT`**`CCG`**`G`**`CGG`**`AAAACTGTCCT`**`CCG`**`TGCGAAGTCGTCT`<br>`**  **`~~`** ***** ******* ****** ***** ***`~~`****   *`~~`*** *****`~~`* *`~~`****** ***`~~`* ***`<br>  <br>**GAL4**|
|`Scer`<br>`Spar`<br>`Smik`<br>`Sbay`<br>|`TCACCGG-TCGCGTTCCTGAAACGCAGATGTGCCT`**`CGC`**`GCCGCACTGCT`**`CCG`**`AACAATAAAGATTCTACAA-----TACTAGCTTTT--ATGGTTATGAA`<br>`TCGTCGGGTTGTGTCCCTTAA-CATCGATGTACCT`**`CGC`**`GCCGCCCTGCT`**`CCG`**`AACAATAAGGATTCTACAAGAAA-TACTTGTTTTTTTATGGTTATGAC`<br>`ACGTTGG-TCGCGTCCCTGAA-CATAGGTACGGCT`**`CGC`**`ACCACCGTGGT`**`CCG`**`AACTATAATACTGGCATAAAGAGGTACTAATTTCT--ACGGTGATGCC`<br>`GTG-CGGATCACGTCCCTGAT-TACTGAAGCGTCT`**`CGC`**`CCCGCCATACC`**`CCG`**`AACAATGCAAATGCAAGAACAAA-TGCCTGTAGTG--GCAGTTATGGT`<br>`** *   ** *** *      *`~~`***** **`~~`*  *`~~`****** **`~~`*   * **     * *             ** ***`<br>**MIG1**|
|`Scer`|`GAGGA-AAAATTGGCAGTAA----CCTGGCCCCACAAACCTT-CAAATTAACGAATCAAATTAACAACCATA-GGATGATAATGCGA------TTAG--T`|
|`Spar`<br>`Smik`<br>`Sbay`<br>|`AGGAACAAAATAAGCAGCCC----ACTGACCCCATATACCTTTCAAACTATTGAATCAAATTGGCCAGCATA-TGGTAATAGTACAG------TTAG--G`<br>`CAACGCAAAATAAACAGTCC----CCCGGCCCCACATACCTT-CAAATCGATGCGTAAAACTGGCTAGCATA-GAATTTTGGTAGCAA-AATATTAG--G`<br>`GAACGTGAAATGACAATTCCTTGCCCCT-CCCCAATATACTTTGTTCCGTGTACAGCACACTGGATAGAACAATGATGGGGTTGCGGTCAAGCCTACTCG`<br>`****    *         *`~~`*****     ***`~~`* * *    *  * *    *     *           **`|
||<br>**TBP**<br>**MIG1**|
|`Scer`<br>`Spar`<br>`Smik`|`TTTTTAGCCTTATTTCTGGGGTAATTAATCAGCGAAGCG--ATGATTTTT-GATCTATTAACAGATATATAAATGGAAAAGCTGCATAACCAC-----TT`<br>`GTTTT--TCTTATTCCTGAGACAATTCATCCGCAAAAAATAATGGTTTTT-GGTCTATTAGCAAACATATAAATGCAAAAGTTGCATAGCCAC-----TT`<br>`TTCTCA--CCTTTCTCTGTGATAATTCATCACCGAAATG--ATGGTTTA--GGACTATTAGCAAACATATAAATGCAAAAGTCGCAGAGATCA-----AT`|
|`Sbay`<br>|`TTTTCCGTTTTACTTCTGTAGTGGCTCAT--GCAGAAAGTAATGGTTTTCTGTTCCTTTTGCAAACATATAAATATGAAAGTAAGATCGCCTCAATTGTA`<br>`* *      *    ***       * **   *  *`~~`*** ***`~~`*  *  **  ** *`~~`********`~~`****    *`|
|`Scer`<br>`Spar`<br>`Smik`<br>`Sbay`|`TAACTAATACTTTCAACATTTTCAGT--TTGTATTACTT-CTTATTCAAAT----GTCATAAAAGTATCAACA-AAAAATTGTTAATATACCTCTATACT`<br>`TAAATAC-ATTTGCTCCTCCAAGATT--TTTAATTTCGT-TTTGTTTTATT----GTCATGGAAATATTAACA-ACAAGTAGTTAATATACATCTATACT`<br>`TCATTCC-ATTCGAACCTTTGAGACTAATTATATTTAGTACTAGTTTTCTTTGGAGTTATAGAAATACCAAAA-AAAAATAGTCAGTATCTATACATACA`<br>`TAGTTTTTCTTTATTCCGTTTGTACTTCTTAGATTTGTTATTTCCGGTTTTACTTTGTCTCCAATTATCAAAACATCAATAACAAGTATTCAACATTTGT`|
|<br> <br>`Scer`<br>`Spar`<br>`Smik`<br>`Sbay`<br> <br>We|<br>`*   *     *     *      * *  **  ***   *  *        *        *  ** **  ** * *  * *    * ***       *`<br>`TTAA-CGTCAAGGA---GAAAAAACTATA`<br>`TTAT-CGTCAAGGAAA-GAACAAACTATA`<br>`TCGTTCATCAAGAA----AAAAAACTA..`<br>`TTATCCCAAAAAAACAACAACAACATATA`<br>`*    *   **  *    ** **  **`<br>GAL1<br>Factor footprint<br>can ‘read’ evolution to revealfunctional elements|
|<br>Yeast (Kellis et|<br>Conservation island<br>al, Nature 2003), Mammals (Xie, Nature 2005), Fly (Stark et al, Nature 07)|


3

###### **Comparative Genomics**


<!-- Start of picture text -->
Lecture 17<br>Using evolution to study genomes<br>(Today):<br><!-- End of picture text -->


Evolution Genomics **Lectures 18-19 Using genomics to study evolution (Thursday):**

4

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power – Detect constrained elements: nucleotides, windows, HMM

   - Estimate fraction constrained: signal vs. background

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - Reading-frame conservation, codon-substitution frequency

   - Likelihood ratio framework: Estimating QCQN, scoring

   - Revise genes, read-through, excess constraint regions

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

   - Sense/anti-sense miRNAs, mature/star arm cooperation

- **Measuring selection within the human lineage**

5

### **Comparative genomics for genome annotation**

###### **29 mammals**


###### **12 flies**


###### **17 fungi**


<!-- Start of picture text -->
9 Yeasts<br>P<br>N<br>P<br>P<br>8 Candida  P<br>N<br>P<br>P<br>Post-duplication<br>Pre-dup<br>Diploid<br>Haploid<br><!-- End of picture text -->

      - © Source unknown. All rights reserved. This content is excluded from our Creative

      - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Compare related species to discover functional elmts**

- **Evolution process: random mutation, natural selection** – Non-functional regions: accumulate mutations, kept

   - Functional regions: accumulate mutations, decrease fitness

   - Evolutionary time: less fit organisms & their genes thin out

6

### **Power of many closely related: total branch length**


      - © Source unknown. All rights reserved. This content is excluded from our Creative

      - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **More branch length**  **more events**  **more power** – Goal: functional vs. non-functional based on # of mutations

   - Very close distances: no mutations in either region

   - Sufficient distance: ability to distinguish increases

   - Very far distances: functional regions no longer conserved

- **Many closely related species >> few distantly related** – For same total branch length: prefer many close species

   - Functional regions conserved for each pair of species

   - Non-functional regions accumulate noise **independently**

   - Analogy: recording a concert with multiple microphones

7

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power <mark>– Detect constrained elements: nucleotides, windows, HMM</mark>

   - Estimate fraction constrained: signal vs. background

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - Reading-frame conservation, codon-substitution frequency

   - Likelihood ratio framework: Estimating QCQN, scoring

   - Revise genes, read-through, excess constraint regions

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

   - Sense/anti-sense miRNAs, mature/star arm cooperation

8

##### **Genome-wide alignments reveal orthologous segments**


Courtesy of Don Gilbert. Used with permission.


<!-- Start of picture text -->
100 genes<br><!-- End of picture text -->

   - © Source unknown. All rights reserved. This content is excluded from our Creative

   - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Genome-wide alignments span entire genome**

- **Comparative identification of functional elements**

9

##### **Comparative genomics and evolutionary signatures**


      - © Source unknown. All rights reserved. This content is excluded from our Creative

      - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Comparative genomics can reveal functional elements**

   - For example:  exons are deeply conserved to mouse, chicken, fish

   - Many other elements are also strongly conserved: exons / regulatory?

- **Develop methods for estimating the level of constraint**

   - Count the number of edit operations, number of substitutions and gaps

   - Estimate the number of mutations (including estimate of back-mutations)

   - Incorporate information about neighborhood: conservation ‘windows’

   - Estimate the probability of a constrained ‘hidden state’: HMMs next week

   - Use phylogeny to estimate tree mutation rate, or ‘rejected substitutions’

   - Allow different portions of the tree to have different rates: phylogenetics

10

### **Detecting rates and patterns of selection (ω/π)**

**<u>Estimating intensity of constraint (</u>** <u></u> **<u>):</u>**

- Probabilistic model of substitution rate

- Maximum Likelihood (ML) estimation of 

   - Report rate ω

   - Report log odds score that non-neutral

- Window-based vs. sitewise application

###### **<u>Detect unusual substitution pattern (π):</u>**

- •Probabilistic model of stationary distribution that is different from background.


###### **Neutral sequence**


###### **Decreased rate ω**

|**0       0     0.8     0.5   0.6     3.2      0      0**|
|---|
|Constrained sequence|


- •ML estimator () of this vector

   - Report PWM for each k-mer in genome.

   - Report log odds score that non-neutral

**Manuel Garber, Or Zuk, Xiaohui Xie**


###### **Unusual patterns π**

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<sup>11</sup>

### **Measuring constraint at individual nucleotides**

**NRSF motif**

   - © Source unknown. All rights reserved. This content is excluded from our Creative

   - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Reveal individual transcription factor binding sites**

- **Within motif instances reveal position-specific bias**

• **More species: motif consensus directly revealed**

12

---

[Up: contents](index.md) · [Detect SNPs that disrupt conserved regulatory motifs →](02-detect-snps-that-disrupt-conserved-regulatory-motifs.md)
