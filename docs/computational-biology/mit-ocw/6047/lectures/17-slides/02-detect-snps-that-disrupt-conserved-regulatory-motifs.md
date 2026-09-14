---
title: Detect SNPs that disrupt conserved regulatory motifs
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/17-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Detect SNPs that disrupt conserved regulatory motifs

**Source:** `lectures/17-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
© Source unknown. All rights reserved. This content is excluded from our Creative<br><!-- End of picture text -->

Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Functionally-associated SNPs enriched in states, constraint

• Prioritize candidates, increase resolution, disrupted motifs

13

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

   - <mark>Estimate fraction constrained: signal vs. background</mark>

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - Reading-frame conservation, codon-substitution frequency

   - Likelihood ratio framework: Estimating QCQN, scoring

   - Revise genes, read-through, excess constraint regions

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

   - Sense/anti-sense miRNAs, mature/star arm cooperation

14

###### **Estimating portion of the genome under constraint**

###### Constraint calculated over a **50mer**


<!-- Start of picture text -->
4 mammals  29 mammals<br>5% FDR  5% FDR<br> 0.6%    1.8%<br>detectable   detectable<br><!-- End of picture text -->

###### Constraint calculated over a **12mer**


<!-- Start of picture text -->
4 mammals  21 mammals<br>5% FDR  5% FDR<br> no signal   1.1%<br>detectable<br><!-- End of picture text -->

- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Or Zuk, Manuel Garber** 15

### **Estimating total fraction under constraint**


<!-- Start of picture text -->
Conservation<br><!-- End of picture text -->

   - © Source unknown. All rights reserved. This content is excluded from our Creative

   - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Actual distribution of conservation scores (Signal) vs. expected distribution if no constraint (Background).

- At any cutoff: true positives (TP) and false predictions (FP)

- Can’t **detect** all constrained elements since curves overlap

- But we can **estimate** the total amount of excess constraint by integrating over entire area between the two curves

16

### **Detection of evolutionarily constrained elements**


<!-- Start of picture text -->
Most new elements in<br>intronic/intergenic<br>regions<br>Highest enrichment<br>for coding transcripts<br><!-- End of picture text -->


<!-- Start of picture text -->
© Source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

17 **Excess positive/purifying selection Distribution of constraint**

17

## **Coverage depth higher in functional regions**


- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Challenges of low-coverage genomes: varying aligment depth Evidence of selection against deletions in functional regions

18

###### **Increase in power from HMRD to 29 mammals**

**ω ω π log-odds π log-odds (12mers) (50mers) (12mers) (50mers) 29 mammals 7.1/1.5/4.6 6.8/1.8/4.1 5.7/ 1.1/3.8 5.7/1.8/3.0 (HMRD) Human 4.2/0.0/0.0 5.3/0.1/0.3 4.5/0.0/0.0 5.1/0.6/1.7 Mouse Rat Dog Estimated / kmers detectable at 5% FDR / base pairs detectable at 5% FDR**

Small increase in estimate of genome percentage under constraint Dramatic increase in power to detect small constrained elements

**Manuel Garber, Or Zuk**

19

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

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

20

##### **Comparative genomics and evolutionary signatures**


      - © Source unknown. All rights reserved. This content is excluded from our Creative

      - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Comparative genomics can reveal functional elements**

   - For example:  exons are deeply conserved to mouse, chicken, fish

   - Many other elements are also strongly conserved: exons / regulatory?

- **Can we also pinpoint specific functions of each region?  Yes!** – Patterns of change distinguish different types of functional elements – Specific function  Selective pressures  Patterns of mutation/inse/del

- **Develop evolutionary signatures characteristic of each function**

21 **Stark** **_et al_ , Nature 2007**

### **Evolutionary signatures for diverse functions**


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Stark, Alexander et al. "Discovery of functional elements in 12 Drosophila genomes using evolutionary signatures." Nature 450, no. 7167 (2007): 219-232.

###### **Protein-coding genes**

- Codon Substitution Frequencies - Reading Frame Conservation

###### **RNA structures**

- Compensatory changes

- Silent G-U substitutions

###### **microRNAs**

- Shape of conservation profile

- Structural features: loops, pairs

- Relationship with 3’UTR motifs

**Regulatory motifs**

- Mutations preserve consensus

- Increased Branch Length Score

- Genome-wide conservation

**Stark et al, Nature 2007**

22

### **Implications for genome annotation / regulation**


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Stark, Alexander et al. "Discovery of functional elements in 12 Drosophila genomes using evolutionary signatures." Nature 450, no. 7167 (2007): 219-232.

**Novel protein-coding genes Revised gene annotations Unusual gene structures**

**Novel structural families Targeting, editing, stability Riboswitches in mammals**

**Novel/expanded miR families miR/miR* arm cooperation Sense/anti-sense miR switches**

**Novel regulatory motif** s **Regulatory motif instances TF/miRNA regulatory networks Single binding site resolution** 23 **Stark et al, Nature 2007**

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

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

24

### **Evolutionary signatures for protein-coding** **<u>genes</u>**

###### **Splice**

```
Dmel TGTTCATAAATAAA-----TTTACAACAGTTAGCTG-GTTAGCCAGGCGGAGTGTCTGCGCCCATTACCGTGCGGACGAGCATGT---GGCTCCAGCATCTTC
Dsec TGTCCATAAATAAA-----TTTACAACAGTTAGCTG-GTTAGCCAGGCGGAGTGTCTGCGCCCATTACCGTGCGGACGAGCATGT---GGCTCCAGCATCTTC
Dsim TGTCCATAAATAAA-----TTTACAACAGTTAGCTG-GTTAGCCAGGCGGAGTGTCTGCGCCCATTACCGTGCGGACGAGCATGT---GGCTCCAGCATCTTC
Dyak TGTCCATAAATAAA-----TTTACAACAGTTAGCTG-GTTAGCCAGGCGGAGTGCCTTCTACCATTACCGTGCGGACGAGCATGT---GGCTCCAGCATCTTC
Dere TGTCCATAAATAAA-----TTTACAACAGTTAGCTG-CTTAGCCATGCGGAGTGCCTCCTGCCATTGCCGTGCGGGCGAGCATGT---GGCTCCAGCATCTTT
Dana TGTCCATAAATAAA-----TCTACAACATTTAGCTG-GTTAGCCAGGCGGAGTGTCTGCGACCGTTCATG------CGGCCGTGA---GGCTCCATCATCTTA
Dpse TGTCCATAAATGAA-----TTTACAACATTTAGCTG-CTTAGCCAGGCGGAATGGCGCCGTCCGTTCCCGTGCATACGCCCGTGG---GGCTCCATCATTTTC
Dper TGTCCATAAATGAA-----TTTACAACATTTAGCTG-CTTAGCCAGGCGGAATGCCGCCGTCCGTTCCCGTGCATACGCCCGTGG---GGCTCCATTATTTTC
Dwil TGTTCATAAATGAA-----TTTACAACACTTAACTGAGTTAGCCAAGCCGAGTGCCGCCGGCCATTAGTATGCAAACGACCATGG---GGTTCCATTATCTTC
Dmoj TGATTATAAACGTAATGCTTTTATAACAATTAGCTG-GTTAGCCAAGCCGAGTGGCGCC------TGCCGTGCGTACGCCCCTGTCCCGGCTCCATCAGCTTT
Dvir TGTTTATAAAATTAATTCTTTTAAAACAATTAGCTG-GTTAGCCAGGCGGAATGGCGCC------GTCCGTGCGTGCGGCTCTGGCCCGGCTCCATCAGCTTC
Dgri TGTCTATAAAAATAATTCTTTTATGACACTTAACTG-ATTAGCCAGGCAGAGTGTCGCC------TGCCATGGGCACGACCCTGGCCGGGTTCCATCAGCTTT
          *****   *     * **  *** *** ***  ******* ** ** ** *  *  ** *     **    **    **    ** ****  *  **
```

Frame-shifting indels Periodic mutations Synonymous substs.

• **Same conservation levels, distinct patterns of divergence**

   - Gaps are multiples of three (preserve amino acid translation)

   - Mutations are largely 3-periodic (silent codon substitutions)

   - Specific triplets exchanged more frequently (conservative substs.)

   - Conservation boundaries are sharp (pinpoint individual splicing signals)

- **Evolutionary signatures of protein-coding selection**

25

###### Evolutionary signatures of protein-coding genes

|`thefat`|`cat sat`|
|---|---|
|Δ1`the atc`|`ats at`|
|Δ2`the tca`|`tsa t`|
|Δ3`the cat`|`sat`|


DNA insertions and deletions can either insert/remove AAs, or totally mangle the remainder of the protein (frameshift).

Some point mutations to the DNA sequence do not change its protein translation at all.

Natural selection tends to tolerate mutations with little/no effect on the protein.

26

###### Protein-coding sequences tolerate distinctive types of change


<!-- Start of picture text -->
protein-coding exon<br>conserved non-coding<br>sequence<br><!-- End of picture text -->


<!-- Start of picture text -->
synonymous<br>conservative<br>non-conservative<br>frame-shifted<br>three stop codons<br><!-- End of picture text -->

- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

27

**Substitution typical of protein-coding regions Substitution typical of intergenic regions**

**Known genes stand out**


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

28

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

   - Estimate fraction constrained: signal vs. background

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - <mark>Reading-frame conservation, codon-substitution frequency</mark>

   - – Likelihood ratio framework: Estimating QCQN, scoring

   - Revise genes, read-through, excess constraint regions

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

   - Sense/anti-sense miRNAs, mature/star arm cooperation

29

**RFC**

### **Signature 1:  Reading frame conservation**

**100% 100% 100% 100% 100% 100% 100% 100% 100%**  **100%**


**RFC 60% 55% 90% 40% 60% 100% 20% 30% 40%**

 **60%**

||Genes|Intergeni|c|Separation|
|---|---|---|---|---|
|Mutations|30%|58%||2-fold|
|Gaps|1.3%|14%||10-fold|
|Frameshifts|0.14%|10.2%||**75-fold**|


30

### **Reading Frame Conservation Test**

```
Scer    CTTCTAGATTTTCATCTT-GTCGATGTTCAAACAACGTGTTA-----TCAGAGAAACAGCTCTATGAGAAATCAGCTGATG
Scer_f1 123123123123123123-12312312312312312312312-----3123123123123123123123123123123123
```

**`Spar    TATTCATA-TCTCATCTTCATCAATGTTCAAACAGCGTGTTACAGACACAGAGAAACAGCTTC-TGAGAAGTCAGCCGGTG RFC Spar_f1 12312312-312312312312312312312312312312312312312312312312312312-31231231231231231`**  **`43% Spar_f2 23123123-123123123123123123123123123123123123123123123123123123-12312312312312312`**  **`34% Spar_f3 31231231-231231231231231231231231231231231231231231231231231231-23123123123123123`**  **`23%`** F ~~1~~ F ~~2~~ F1 F2 F3 100% 60% 100% 60% 100% 90% 100% 40% 100% 60% 100% 100% 100% 30% 100% 30% 100% 30% **100% 56%**

31

### **Revisiting gene content with RFC test**

||**Accept **|**Reject**|
|---|---|---|
|**~4000 named genes**|**99.9%**|**0.1%**|
|**~300 intergenic regions**|**1%**|**99%**|
|**2000 Hypothetical**<br>**ORFs**|**1500**|**500**|
|High sensitivity|and specificity||
|Example of a|rejected ORF||


32

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power – Detect constrained elements: nucleotides, windows, HMM

   - Estimate fraction constrained: signal vs. background

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - Reading-frame conservation, codon-substitution frequency

   - <mark>Likelihood ratio framework: Estimating Q</mark> C <mark>Q</mark> N <mark>, scoring</mark>

   - Revise genes, read-through, excess constraint regions

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

   - Sense/anti-sense miRNAs, mature/star arm cooperation

33


###### protein-coding exon

conserved non-coding sequence

###### <u>A method to distinguish these evolutionary signatures should:</u>

- **Quantify the distinctiveness of all 64**<sup>**2**</sup> **possible codon substitutions**

   - Synonymous: very frequent in protein-coding sequences

   - Nonsense: much more frequent in non-coding than coding regions

- **Model the phylogenetic relationship among the species**

   - Multiple apparent substitutions may be explained by one evolutionary event

- **Tolerate uncertainty in the input**

   - Unknown ancestral sequences

   - Alignment gaps, missing data

- **Report the [un]certainty of the result**

   - Quantify confidence that given alignment is protein-coding

   - Units: p-value, bits, decibans, etc.

34

#### Codon evolution can be modeled as a Bayesian network


<!-- Start of picture text -->
ATT  dmel<br>ATT  dsim<br>GTT  dsec<br>b<br>ATA  dyak<br>a<br><!-- End of picture text -->


Conditional probability distribution (CPD) giving, for all codons a & b,

Each site (codon alignment column) is treated independently.

Given the topology and CPDs, we can simulate evolution of an ancestral sequence.

Additionally given extant (leaf) sequences, the ancestral sequences can be inferred.

For _L_ leaves, CPDs total about parameters.

35

###### The Bayes net is parameterized as a continuous-time Markov process


Rate matrix _(_ **_Q_** )

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Branch lengths t

Each CPD is determined by a rate matrix shared throughout the tree and a branch-specific ‘time’ (branch length):


<u>Intuition: The branch lengths specify how much ‘time’ passed between any two nodes. The</u> rate matrix describes the relative frequencies of codon substitutions _per unit branch length_ . Synonymous substitutions have high rates and nonsense substitutions have low rates.

We can obtain maximum likelihood estimates of parameters using EM in training data.


36

### Example nucleotide (4x4) rate & substitution matrices

A **Q** = G C T


A    G    C    T


is the solution to the system of differential equations describing the Markov process model of evolution.


Analogy:

<u>Side note:  Jukes-Cantor and Kimura models are</u> set up so that the entries of e<sup>Qt</sup> have closed-form solutions.

solves the differential equation


37

The hairy math: how do we estimate **_Q_** ?

- Collect many alignments of known protein-coding sequences (training data)

- • Consider the probability of the training data as a function of **_<u>Q</u>_**


Still computed using Felsenstein algorithm

- Choose the **_Q_** that maximizes that probability:


Note: **_Q_** represents thousands of parameters

- Maximization strategies: expectation-maximization; gradient ascent; simulated annealing; spectral decomposition; others

- Branch lengths can also be optimized in the same way (simultaneously)

- • Non-coding model estimated similarly, with random non-coding regions as training data.

38

###### Given this generative model of codon evolution:


Rate matrix _(_ **_Q_** )

Branch lengths t

- © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

We can compute the probability of any given alignment, marginalizing over all possible ancestral sequences, using Felsenstein’s pruning algorithm.


###### protein-coding exon


###### conserved non-coding sequence


If I simulate alignments randomly according to the model, I’ll get this <u>exact alignment once every 10</u><sup>117</sup> samples

39

###### Now suppose we’ve estimated <u>two rate matrices:</u>


###### **_Q_** _C_ estimated from known coding regions


###### **_Q_** _N_ estimated from noncoding regions

- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### These specify different rates of codon substitution, which in turn lead to different probabilities of any given alignment:


40


This alignment is 10<sup>35</sup> times more probable under the coding model than the non-coding model.


This alignment is 10<sup>21</sup> times less probable under the coding model than the non-coding model.


This **likelihood ratio**

is our measure of confidence that

the alignment is protein-coding.

41

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

   - Estimate fraction constrained: signal vs. background

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - Reading-frame conservation, codon-substitution frequency

   - Likelihood ratio framework: Estimating QCQN, scoring

   - <mark>Revise genes, read-through, excess constraint regions</mark>

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

   - Sense/anti-sense miRNAs, mature/star arm cooperation

42

## Evolutionary signatures can predict new genes and exons


Protein-Coding Evolutionary Signatures


SMCRF Viterbi decoding

Targeted validation full-length cDNA


_Evolutionary signatures built into a semi-Markov conditional random field to predict proteincoding exons_


<!-- Start of picture text -->
43<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Stark, Alexander et al. "Discovery of functional elements in 12 Drosophila genomes using evolutionary signatures." Nature 450, no. 7167 (2007): 219-232.

43

### **New protein-coding genes**


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

New genes supported by Illumina BodyAtlas transcripts Submitted to GENCODE for validation / manual curation

44

### **Translational read-through in flies and mammals**

###### **One of four novel candidates in the human genome: OPRL1 neurotransmitter**


**Protein-coding conservation**

**Stop codon read through**

**Continued protein-coding No more 2**<sup>**nd**</sup> **stop conservation codon conservation**

- **New mechanism of post-transcriptional regulation?**

   - Conserved in both mammals (4 candidates) and flies (350 candidates)

   - Strongly enriched for neurotransmitters, brain-expressed proteins, TF regulators

   - After correcting for gene length: TF enrichment remains

- **Evidence suggestive of regulatory control**

   - Read-through stop codon perfectly conserved in 93% of cases (24% at bkgrnd)

   - Upstream bases show increased conservation. Downstream is TGAC.

   - GCA triplet repeats

– Increased RNA secondary structure

**Lin** **_et al_ , Genome Research 2007** 45 **Jungreis** **_et al_ , in preparation**

**Discover of translational readthrough genes**


- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Discovery of 4 readthrough genes, abundant in many animal genomes

46

### **Overlapping selection in protein-coding exons**


rhombomere 4 expression rhombomere 2 expr. (Lampe _et al_ ., NAR 2008) (Tümpel PNAS 2008)

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. 10,000 overlapping synonymous constrained elements Roles in splicing, translation, regulation

47

### **Codon-specific measures of positive selection**


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Gene-wide vs. punctate regions of exons positive selection 48

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

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

49

### **New RNA structures and families**


### New structs fall in families, supported by evolut/energy


- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Ex: new struct in XIST long non-coding RNA Known function in X-chromosome inactivation Possible functional domain of XIST?

50

### **RNA families: orthologous/paralogous conservation**


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Example of new structural 3’UTR family in MAT2A gene likely role in detecting S-adeosyl-methionic (SAM) level

51

## **<mark>Computational challenge of miRNA discovery</mark>**

###### **60-100 true miRNAs**

**760,355 miRNA-like hairpins**


**A false positive rate of 0.5%**  **3800 spurious hairpins. Need 99.99% specificity (>5,000-fold enrichment)**

52

##### **Evolutionary signatures for microRNA genes**


**(1) Conservation profile**

- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### **miRNAs show characteristic conservation properties**

53

##### **Distinguishing true miRNAs from random hairpins**


<!-- Start of picture text -->
Evolutionary features  Feature performance<br>Enrichment<br>Total<br>(1)<br>(2)<br>(3)<br>Structural features<br>(4)<br>(5)<br><!-- End of picture text -->


<!-- Start of picture text -->
Structural features<br>(4)<br>(5)<br>(6)<br><!-- End of picture text -->

**Combination of features: > 4,500-fold enrichment**

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

54

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

   - Estimate fraction constrained: signal vs. background

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - Reading-frame conservation, codon-substitution frequency

   - Likelihood ratio framework: Estimating QCQN, scoring

   - Revise genes, read-through, excess constraint regions

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

– Sense/anti-sense miRNAs, mature/star arm cooperation

55

### **miRNA detection using many decision trees**

MFE<3?

- **For each tree:**


<!-- Start of picture text -->
<br>yes  no<br>ProfileCorr<8  StrConsIndx>3<br>yes  no  yes  no<br>NOT  miRNA  NOT  #Loops>2<br>yes  no<br>Stability>4  NOT<br>yes  no<br>NOT  #Loops<5<br>yes  no<br>miRNA  NOT<br><!-- End of picture text -->

- Randomly select:

   - Subset of features to base classification on

   - Subset of +/- training examples

   - Remainder of testing examples

- Use to train a decision tree classifier:

   - Select a feature and cutoff at each level

   - Continue with feature/cutoff at next level

   - (…)

- Evaluate performance on test set:

   - Push each element down the decision tree

   - Leaf label gives classification decision

- **To combine trees:**

   - Average prediction class across trees

   - Report class with maximum # of votes

56

### **Random Forests: Combine many decision trees**


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

• **Many decision trees:**

– Each can select cutoffs and direction of cutoff

– Each feature can be reused multiple times

– Used serially (AND) and in parallel (OR)

• **Ensemble classifier**

– Bagging: model averaging, combines predictions

– Can take median of predictions

• **Advantages: Robustness, Feature importance**

57

**Evidence 1: Novel miRNAs match sequencing reads**


<!-- Start of picture text -->
348 reads<br>16 reads<br><!-- End of picture text -->

**Ruby, Bartel, Lai**

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

58

**Evidence 2: Genomic properties typical of miRNAs**


- **Novel miRNAs in introns of known genes**

- **Preference for + strand, transcription factors**


- **Genomic clustering with novel / known miRNAs**

- **Same family, common origin / same precursor**

   - © Source unknown. All rights reserved. This content is excluded from our Creative

   - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

59

**Two ‘dubious’ protein-coding** **<u>genes are in fact miRNAs</u>**

###### **Two novel miRNAs overlap exons (5’UTR and coding!)**


   - © Source unknown. All rights reserved. This content is excluded from our Creative

   - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Both CG31044 and CG33311 were independently rejected as** **_dubious_ based on their non-protein-coding conservation patterns (Lin** **_et al._ )**

- **Novel miRNA genes provide explanation for their transcripts, as their precursor miRNA**

60

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint** – Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

   - Estimate fraction constrained: signal vs. background

- **Evolutionary signatures: focus on pattern of change** – Different functions  Characteristic patterns of evolution

- **Signatures of protein-coding genes**

   - Reading-frame conservation, codon-substitution frequency

   - Likelihood ratio framework: Estimating QCQN, scoring

   - Revise genes, read-through, excess constraint regions

- **Signatures of microRNA genes**

   - Structural and evolutionary features of microRNAs

   - Combining features: decision trees, random forests

   - <mark>Sense/anti-sense miRNAs, mature/star arm cooperation</mark>

61

### **Surprise 1: microRNA & microRNA* function**


<!-- Start of picture text -->
Drosophila Hox<br><!-- End of picture text -->

      - © Source unknown. All rights reserved. This content is excluded from our Creative

      - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Both hairpin arms of a microRNA can be functional** – High scores, abundant processing, conserved targets

   - Hox miRNAs miR-10 and miR-iab-4 as master Hox regulators

62 **Stark** **_et al_ , Genome Research 2007**

### **Evidence of miR-iab-4 anti-sense (AS) function**


<!-- Start of picture text -->
Highly conserved Hox targets<br>anti-<br>sense  sense<br><!-- End of picture text -->

- © Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Stark, Alexander et al. "A single Hox locus in Drosophila produces functional microRNAs from opposite DNA strands." Genes & development 22, no. 1 (2008): 8-13.

- **A single miRNA locus transcribed from both strands**

- • **The two transcripts show distinct expression domains (mutually exclusive)**

- • **Both processed to mature miRNAs: mir-iab-4, miR-iab-4AS (anti-sense)**

63

### **miR-iab-4AS leads to homeotic transformations**


<!-- Start of picture text -->
wing<br>w/bristles<br>Sensory bristles<br>haltere<br>wing  haltere<br>WT<br>wing<br>sense  Antisense<br><!-- End of picture text -->


<!-- Start of picture text -->
Note: C,D,E same magnification<br><!-- End of picture text -->

- © Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Stark, Alexander et al. "A single Hox locus in Drosophila produces functional microRNAs from opposite DNA strands." Genes & development 22, no. 1 (2008): 8-13.

- **Mis-expression of mir-iab-4S & AS: alteres**  **wings homeotic transform.**

- • **Stronger phenotype for AS miRNA**

- **Sense/anti-sense pairs as general building blocks for miRNA regulation**

- • **10 sense/anti-sense miRNAs in mouse**

**Stark** **_et al_ , Genes&Development 2008**

64

### **Comparative genomics I: Evolutionary signatures**

- **Nucleotide conservation: evolutionary constraint**

   - Purifying selection, neutral branch length, discovery power

   - Detect constrained elements: nucleotides, windows, HMM

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

65

**Mammalian constraint matches Human SNPs**


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

66 Human SNPs match mammalian-wide twofold constraint

### **Mammalian constraint matches Human SNPs**


- © Source unknown. All rights reserved. This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Genome-wide agreement of selection and polymorphisms 67

67

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Human constraint outside conserved regions →](03-human-constraint-outside-conserved-regions.md)
