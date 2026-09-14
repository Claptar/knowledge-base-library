---
title: Example Chromatin State Annotation
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/11-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Example Chromatin State Annotation

**Source:** `lectures/11-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Use Baum Welch to learn hidden states and their annotations

- Learned states correspond to known functional elements

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ernst, Jason and Manolis Kellis. "Discovery and characterization of chromatin states for systematic annotation of the human genome." Nature Biotechnology 28, no. 8 (2010): 817-825.

- _De novo_ discovery of major types of chromatin

61

#### **Model complexity matches that of genome**

• Handful of repressed states capture vast majority of genome

   - Only 1% of genome split in 14 promoter states

- © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Modeling power well distributed where needed

62

###### **Apply genome wide to classify chromatin states** **_de novo_**


<!-- Start of picture text -->
1  2  3  4<br>5  6  7  8  9<br>10  11  12  13  14  15<br>16  17  18  19  20  21  22  X  Y<br>16  17<br>© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Source: Ernst, Jason and Manolis Kellis. "Discovery and characterization of chromatin states for<br>systematic annotation of the human genome." Nature Biotechnology 28, no. 8 (2010): 817-825.<br><!-- End of picture text -->

0

2

10

**Now what? Interpret these states biologically**

63

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

– Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Chromatin state characterization: Functional/positional enrichment

- 4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

- – Capturing dependencies and state-conditional mark independence

- 5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

- – Defining activity profiles for linking enhancer regulatory networks

- (Future: Chromatin states to interpret disease-associated variants)

64

State definitions  State Enrichments 65

© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Ernst, Jason and Manolis Kellis. "Discovery and characterization of chromatin states for systematic annotation of the human genome." Nature Biotechnology 28, no. 8 (2010): 817-825.

65

<mark>Functional enrichments enable annotation of 51 distinct states</mark>

66

© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Ernst, Jason and Manolis Kellis. "Discovery and characterization of chromatin states for systematic annotation of the human genome." Nature Biotechnology 28, no. 8 (2010): 817-825.

66

###### Application of ChromHMM to 41 chromatin marks in CD4+ T-cells (Barski’07, Wang’08)


<!-- Start of picture text -->
Transcribed states<br><!-- End of picture text -->


<!-- Start of picture text -->
Active Intergenic<br><!-- End of picture text -->


67

67

###### **Functional properties of discovered chromatin states**

**State 28: 112-fold ZNF enrich**

|**GO Category**|**State 3**|**State 4**|**State 5**|**State 6**|**State 7**|**State 8**||
|---|---|---|---|---|---|---|---|
|Cell Cycle<br>Phase|2.10<br>(2x10<sup>-7</sup>)|0.57<br>(1)|1.61<br>(0.001)|1.45<br>(1)|<br>1.15 (1)|1.51 (1)|**State 27**|
|Embryonic<br>Development|<sup>1.24 (1)</sup><br>|2.82<br>(9x10<sup>-23</sup>)|<sup>1.07 (1)</sup>|0.85 (1)|0.54 (1)|1.00 (1)||
|Chromatin|1.20 (1)|0.48 (1)<br>|2.2<br>(1.4x10<sup>-7</sup>)|<sup>1.64 (1)</sup>|0.85 (1)|0.85 (1)||
|Response to<br>DNA Damage<br>Stimulus|1.20 (1)|0.35 (1)|1.55<br>(0.074)|2.13<br>(6.5x10<sup>-11</sup>)|<br>1.97<br>(1.0x10<sup>-4</sup>)|<br>0.84 (1)||
|RNA<br>|<sup>049 1</sup>|<sup>026 1</sup>|<sup>131 1</sup>|1.91|2.64|<br>2.45||
|Processing|<sup>. ()</sup>|<sup>. ()</sup>|<sup>. ()</sup>|(4.2x10<sup>-11</sup>)|(8.7x10<sup>-24</sup>)|(3.0x10<sup>-4</sup>)||
|T cell<br>Activation|0.77 (1)|0.88 (1)|1.27 (1)|0.70 (1)|0.79 (1)|4.72<br>(2x10<sup>-7</sup>)||


“The achievement of the repressed state by wild-type KAP1 involves <u>decreased recruitment of</u> **RNA polymerase II** , reduced levels of histone **H3 K9 acteylation** and **H3K4 methylation** , an increase in **histone occupancy** , enrichment of **trimethyl histone H3K9** , **H3K36** , and **histone H4K20** …” MCB 2006.

**Promoter state**  **gene GO function**


<!-- Start of picture text -->
Transcription End State<br>State 30<br>29<br>34<br>35<br>42<br><!-- End of picture text -->


<!-- Start of picture text -->
ZNF repressed state recovery<br><!-- End of picture text -->


<!-- Start of picture text -->
TF binding  Motif enrichment<br>promoters<br>enhancers<br><!-- End of picture text -->


**Distinct types of repression - Chrom bands / HDAC resp - Repeat family / composition**


<!-- Start of picture text -->
State 10kb away predictive of expr.<br><!-- End of picture text -->

**Promoter vs. enhancer regulation**

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

68

##### **Applications to genome annotation**

###### **Long intergenic non-coding RNAs/lincRNAs**

###### **New protein-coding genes**


<!-- Start of picture text -->
lincRNAs<br><!-- End of picture text -->


<!-- Start of picture text -->
Known coding<br><!-- End of picture text -->


<!-- Start of picture text -->
Evolutionary CSF score  <br>Chromatin signature:  Evolutionary signature:<br>promoter / transcribed  not protein-coding<br><!-- End of picture text -->


<!-- Start of picture text -->
In promoter(short)/low-expr states<br><!-- End of picture text -->


<!-- Start of picture text -->
Bing Ren, Eddy Rubin<br><!-- End of picture text -->


<!-- Start of picture text -->
Assign candidate functions to intergenic SNPs<br>from genome-wide association studies<br><!-- End of picture text -->

###### **New developmental enhancer regions**

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

69

###### **Discovery power for promoters, transcripts**


<!-- Start of picture text -->
True Positive Rate<br><!-- End of picture text -->


<!-- Start of picture text -->
TSS<br><!-- End of picture text -->


<!-- Start of picture text -->
False Positive Rate<br><!-- End of picture text -->


<!-- Start of picture text -->
Transcribed genes<br><!-- End of picture text -->


<!-- Start of picture text -->
False Positive Rate<br><!-- End of picture text -->

   - © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Significantly outperforms single-marks

- Similar power to supervised learning approach

- CAGE experiments give possible upper bound

70

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Promoter, transcribed, intergenic, repressed, repetitive states

- 4. Model complexity: selecting the number of states/marks – Capturing dependencies. State-conditional mark independence

   - Selecting the number of states, selecting number of marks

5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

– Defining activity profiles for linking enhancer regulatory networks

(Future: Chromatin states to interpret disease-associated variants)

71

**State-conditional mark independence** Do hidden states actually capture dependencies between marks?

72

###### **Pairwise Expected vs. Observed Mark Co-Occurence**

Each point = one pair of chromatin marks 41x41 pairs plotted X-axis: F(mark1)*F(mark2) Y-axis: F(mark1 & mark2) Diagonal: independence Off-diag: dependence

 Marks become conditionally independent  Model captures dependencies

**_pi_** emission prob _k_ for mark **_i qi,j_** freq w/ which marks **_i_** and **_j_** co-occur

_<mark>P</mark> i_ Test each pair of chromatin marks _<mark>p</mark> j_ ? _qi,j=pi*pj_

Multi-variate HMM emits entire vector of marks at a time Model assumes mark independence _*conditional*_ upon state In fact, it specifically seeks to _*capture*_ these dependencies

73

###### **Test conditional independence for each state**


<!-- Start of picture text -->
Promoter states<br>Transcribed states<br><!-- End of picture text -->


74

74

###### **Non-independence reveals cases of model violation**


- **Repetitive states show more dependencies**

- **Conditional independence does not hold**

75

###### **As more states are added, dependencies captured**


- **With only 5 states in HMM, not enough power to distinguish different properties**

- **Dependencies remain**

- **As model complexity increases, states learned become more precise**

- **Dependencies captured**

76

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Promoter, transcribed, intergenic, repressed, repetitive states

- 4. Model complexity: selecting the number of states/marks – Capturing dependencies. State-conditional mark independence

   - <mark>Selecting the number of states, selecting number of marks</mark>

5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

– Defining activity profiles for linking enhancer regulatory networks

(Future: Chromatin states to interpret disease-associated variants)

77

###### **Comparison of BIC Score vs. Number of States for Random and Nested Initialization**

###### Step 1: Learn a larger model that captures ‘all’ relevant states

Step 2: Prune down model greedily eliminating least informative states

Step 3: Select arbitrary cutoff based on biological interpretation Result: a 51-state model that captures most biology in least complexity

• Standard model selection criteria fail due to genome complexity: more states always preferred • Instead: Start w/complex model, keep informative states, prune redundant states. Pick cutoff

78

**Recovery of 79-state model in random vs. nested initialization**


**Random Initialization** (states appear & disappear)

**Selected 51-state model**

**Nested Initialization** (states consistly recoverd)


###### **Nested initialization approach:**

- **First pass:** learn models of increasing complexity

- **Second pass:** form nested set of emission parameter initializations by greedily removing states from best BIC model found

- **Nested models criteria:**

- Maximize sum of correlation of emission vectors with nested model

- Models learned in parallel

79

###### Functional recovery with increasing numbers of states


Simple Repeat state

Transcription End State

Zinc Finger state

- Red: Maximum fold functional enrichment for corresponding biological category

- Blue: Percent of that functional category that overlaps regions annotated to this state

- Top plot: Correlation of emission parameter vector for that state to closest state

80

Chromatin state recovery with increasing numbers of marks **Which states are well-recovered? Precisely what mistakes are made?**

Increasing numbers of marks (greedy)


**Precisely what mistakes are made?** (for a given subset of 11 ENCODE marks)

###### State Inferred with subset of marks


###### **State confusion matrix with 11 ENCODE marks**

© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Ernst, Jason and Manolis Kellis. "Discovery and characterization of chromatin states for systematic annotation of the human genome." Nature Biotechnology 28, no. 8 (2010): 817-825.

**Recovery of states with increasing number of marks**

81

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

   - Promoter, transcribed, intergenic, repressed, repetitive states

4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

– Capturing dependencies and state-conditional mark independence

5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

– Defining activity profiles for linking enhancer regulatory networks

(Future: Chromatin states to interpret disease-associated variants)

82

###### **ENCODE: Study nine marks in nine human cell lines**

###### **<u>9 human cell types</u>**

###### **<u>9 marks</u>**

|**H3K4me1**|**HUVEC**|Umbilical vein endothelial|
|---|---|---|
|**H3K4me2**<br>|**NHEK**|Keratinocytes|
|**H3K4me3**<br>**H3K27ac**|**GM12878**|Lymphoblastoid|
|<br>**H3K9ac**|**K562**<br>x|Myelogenous leukemia|
|**H3K27me3**|**HepG2**<br>|Liver carcinoma|
|**H4K20me1**|**NHLF**|Normal human lung fibroblast|
|**H3K36me3**|**HMEC**|Mammary epithelial cell|
|**CTCF**<br>|**HSMM**|Skeletal muscle myoblasts|
|**+WCE**<br>**+RNA**|**H1**|Embryonic|
||**Brad Bernst**|**ein ENCODE Chromatin Group**|


How to learn single set of chromatin states?

###### **81 Chromatin Mark Tracks**

###### **(2**<sup>**81**</sup> **combinations)**

© Brad Bernstein. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Ernst et al, _Nature_ 2011 83

######

###### **Solution 1: Learn independent models and cluster**


**<u>Basic approach:</u>**

Promoter

- **a) Train a k-state model in each cell type independently**

Candidate enhancer

- **b) Cluster models learned independently**

Insulator

Transcribed

- **c) Merge clusters and reapply to each cell type**

Repressive

Repetitive

**<u>How to cluster</u>**

- **a) Using emission probability matrix: most similar definitions**

- **b) Using genome annotation: posterior probability decoding**

84

###### **Joint learning of states across multiple cell types**


Cell type 1

Cell type 2

Cell type 3

Cell type 4

Cell type 5

Cell type 6

Cell type 7

Cell type 8

Cell type 9

###### **Solution 2: Stacking**

- Learns each combination of activity as a separate state

- Ex: ES-specific enhancers: enhancer marks in ES, no marks in other cell types


(…)

Cell type 1 Cell type 2 Cell type 9 **Solution 3: Concatenation**

- Requires that profiled marks are the same (or treat as missing data)

- Ensures common state definitions across cell types

85

###### **Joint learning with different subsets of marks (Solution 3)**


<!-- Start of picture text -->
Missing  Missing<br>(…)<br>Missing<br>Missing<br>Cell type 1  Cell type 2  Cell type 9<br><!-- End of picture text -->

**Option (a) Treat missing tracks as missing data**

- EM framework allows for unspecified data points

- As long as pairwise relationship observed in some cell type

- **Option (b) Chromatin mark imputation**

- Explicitly predict max-likelihood chromatin track for missing data

- Less powerful if ultimate goal is chromatin state learning

86

###### **ENCODE: Study nine marks in nine human cell lines**

###### **<u>9 human cell types</u>**

###### **<u>9 marks</u>**

|**H3K4me1**|**HUVEC**|Umbilical vein endothelial|
|---|---|---|
|**H3K4me2**<br>|**NHEK**|Keratinocytes|
|**H3K4me3**<br>**H3K27**|**GM12878**|Lymphoblastoid|
|**ac**<br>**H3K9ac**|**K562**<br>x|Myelogenous leukemia|
|**H3K27me3**|**HepG2**<br>|Liver carcinoma|
|**H4K20me1**|**NHLF**|Normal human lung fibroblast|
|**H3K36me3**|**HMEC**|Mammary epithelial cell|
|**CTCF**<br>|**HSMM**|Skeletal muscle myoblasts|
|**+WCE**<br>**+RNA**|**H1**|Embryonic|


###### **81 Chromatin Mark Tracks**

**(2**<sup>**81**</sup> **combinations)**

- **Concatenation approach:**

- **Learned jointly across cell types**

- **State definitions are common**

- **State locations are dynamic**

###### **Brad Bernstein ENCODE Chromatin Group**

© Brad Bernstein. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Ernst et al, _Nature_ 201 87

###### **Chromatin states dynamics across nine cell types**


<!-- Start of picture text -->
Predicted<br>linking<br>Correlated<br>activity<br>© Brad Bernstein. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

- **Single annotation track for each cell type**

- **Summarize cell-type activity at a glance**

• **Can study 9-cell activity pattern across**

88

###### **Epigenomic mapping across 100+ tissues/cell types**

###### **_Diverse tissues and cells_**

###### **_Diverse epigenomic assays_**


**x**

Courtesy of NIH Roadmap Epigenomics Mapping Consortium. Used with permission.

**Adult tissues and cells** (brain, muscle, heart, digestive, skin, adipose, lung, blood…) **Fetal tissues** (brain, skeletal muscle, heart, digestive, lung, cord blood…) **ES cells, iPS, differentiated cells**

Courtesy of Broad Communications. Used with permission.

###### **Histone modifications**

- **H3K4me3, H3K4me1, H3K36me3**

- **H3K27me3, H3K9me3, H3K27/9ac**

- **+20 more**

**Open chromatin** :

(meso/endo/ectoderm, neural, mesench…)

- **DNA accessibility**

- **DNA methylation** :


- **WGBS, RRBS, MRE/MeDIP**

- **Gene expression**

   - **RNA-seq, Exon Arrays**

89

###### **States show distinct mCpG, DNase, Tx, Ac profiles**


<!-- Start of picture text -->
Ali Moussavi<br><!-- End of picture text -->


Ali Moussavi **0% 100% Closed Open DNA methylation DNA accessibility** (WGBS, 37 epigenomes) (DNaseI, 53 epigenomes

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**TssA** vs. **TssBiv** : diff. activity, both open, both unmethylated! **Enh** vs. **ReprPC** : diff. activity, both intermediate DNase/Methyl **Tx** : Methylated, closed, actively transcribed  Distinct modes of repression: **H3K27me3** vs. **DNAme** vs. **Het**

90

###### **Chromosomal ‘domains’ from chromatin state usage**


© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330.

• **State usage**  **gene density, lamina, cytogenetic bands** 91 • **Quies/ZNF/het | gene rich/poor, each active/repressed**

#### **H3K4me1 phylogeny reveals common biology**


© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330.

Wouter Meuleman

Grouping of ES, immune, brain, muscle, heart, smooth muscle, fetal

•

92

###### **Cells/Tissues at extremes of epigenomic variation**


**H3K4me1 MDS**

© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330.

- **ES/Immune/IMR90 most extreme**

- **ES:**  **Biv,**  **Enh/Tx/TssFlnk/PCwk**

- **Immune:**  **TssA,**  **TxWk**

- • **IMR90:**  **ReprPC,**  **Quies** Misha Bilenky, Wouter Meuleman

93

###### **Chromatin state annotations across 127 epigenomes**


© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330. Reveal epigenomic variability: enh/prom/tx/repr/het Anshul Kundaje 94

94

###### **State switching: active/inactive, mostly keep identity**


###### Anshul Kundaje / Wouter Meuleman


© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330.

• **Most variable: Enhancers. Least: TssA/Tx/Quies** • **State switching: Active (1-7)**  **Inactive (10-15)** • **Exception: Dyadic regions: enhancer**  **promoter**

95

###### **Chromatin state changes during differentiation Classify cells TSS-proximal TSS-distal**

######


   - © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Epigenomic features can predict directionality:** AUC 78%

- • **TSS-proximal** : (1) Loss of Het/ZNF. (2) Gain of TxWk, Quies • **TSS-distal** : Bivalent, PCrepressed  Enhancer, Tx, TssFlnk

96

###### **Epigenome imputation by exploiting mark correlations**

**Observed Imputed**

      - © Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Two types of features**

   - Other marks + context in same tissue

   - Same mark in ‘closest’ tissues

- **Impute missing datasets** – Predict DNase, marks @ 25bp res

   - Predict RNA-Seq @ 25 bp res

   - Predict DNA methylation @ 1bp res


<!-- Start of picture text -->
Jason Ernst<br><!-- End of picture text -->

97

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

- Promoter, transcribed, intergenic, repressed, repetitive states

- 4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

- – Capturing dependencies and state-conditional mark independence

- 5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

- <mark>Defining activity profiles for linking enhancer regulatory networks</mark>

- (Future: Chromatin states to interpret disease-associated variants)

98

###### **5. Correlation-based links of enhancer networks**

Regulators  Enhancers  Target genes

99

###### **Chromatin state annotations across 127 epigenomes**


Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330.

Reveal epigenomic variability: enh/prom/tx/repr/het

Anshul Kundaje 100

###### **2.3M enhancer regions**  **only ~200 activity patterns**


<!-- Start of picture text -->
immune<br>dev/morph<br>muscle<br>morph<br>learning  <3  kidney<br>smooth<br>liver<br>Wouter Meuleman  muscle<br><!-- End of picture text -->

© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330.

101

###### **Introducing multi-cell activity profiles**


<!-- Start of picture text -->
Gene  Chromatin  Active TF motif  TF regulator  Dip-aligned<br>expression  States  enrichment  expression  motif biases<br>HUVEC<br>NHEK<br>GM12878<br>K562<br>HepG2<br>NHLF<br>HMEC<br>HSMM<br>H1<br><!-- End of picture text -->

###### **Link enhancers to target genes**

ON Active enhancer Motif enrichment TF On Motif aligned TF Off Flat profile OFF Repressed Motif depletion

102

###### **Activity-based linking of enhancers to target genes**

###### Finding correct target of enhancer in divergently transcribed genes


<!-- Start of picture text -->
?  ?<br>HMEC state<br>IRF6  C1orf107<br>expression  -0.7  H3K27ac signal  -1.1  expression<br>-1.7  1.2<br>-1.6  0.0<br>-1.7  -1.3<br>0.9  0.5<br>-1.6  -0.1<br>-1.6  0.1<br>4.2  0.4<br>3.7  0.3<br><!-- End of picture text -->

© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Compute correlations between gene expression levels and enhancer associated histone modification signals

103

###### Visualizing 10,000s predicted enhancer-gene links


© Source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Overlapping regulatory units, both few and many

- • Both upstream and downstream elements linked

• Enhancers correlate with sequence constraint

104

###### **Chromatin dynamics: linking enhancer networks**

TFs  enhancers  target genes

105

###### **Introducing multi-cell activity profiles**


<!-- Start of picture text -->
Gene  Chromatin  Active TF motif  TF regulator  Dip-aligned<br>expression  States  enrichment  expression  motif biases<br>HUVEC<br>NHEK<br>GM12878<br>K562<br>HepG2<br>NHLF<br>HMEC<br>HSMM<br>H1<br>Link TFs to target enhancers<br>Predict activators vs. repressors<br>ON  Active enhancer  Motif enrichment  TF On  Motif aligned<br>TF Off  Flat profile<br>OFF  Repressed  Motif depletion<br><!-- End of picture text -->

106

###### **Coordinated activity reveals activators/repressors**

###### **Activity signatures for each TF**

###### **Enhancer activity**


<!-- Start of picture text -->
Ex1: Oct4 predicted activator  Ex2: Gfi1 repressor of<br>of embryonic stem (ES) cells  K562/GM cells<br><!-- End of picture text -->

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ernst, Jason et al. "Mapping and analysis of chromatin state dynamics in nine human cell types." Nature 473, no.7345 (2011): 43-49.

107 • Enhancer networks: Regulator  enhancer  target gene

107

###### **Regulatory motifs predicted to drive enhancer modules**

###### **Pouya Kheradpour**

© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative

Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330. • **Activator and repressor motifs consistent with tissues**

108

###### **Causal motifs supported by dips & enhancer assays**


<!-- Start of picture text -->
Tarjei Mikkelsen<br><!-- End of picture text -->

Predicted causal HNF motifs (that also showed dips) in HepG2 enhancers

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ernst, Jason et al. "Mapping and analysis of chromatin state dynamics in nine human cell types." Nature 473, no.7345 (2011): 43-49.

**Dip evidence of TF binding Enhancer activity halved (nucleosome displacement) by single-motif disruption**

 **Motifs bound by TF, contribute to enhancers** 109

109

###### **Goals for today: Computational Epigenomics**

1. Introduction to Epigenomics – Overview of epigenomics, Diversity of Chromatin modifications

   - Antibodies, ChIP-Seq, data generation projects, raw data

2. Primary data processing: Read mapping, Peak calling – Read mapping: Hashing, Suffix Trees, Burrows-Wheeler Transform

– Quality Control, Cross-correlation, Peak calling, IDR (similar to FDR)

3. Discovery and characterization of chromatin states

   - A multi-variate HMM for chromatin combinatorics

   - Promoter, transcribed, intergenic, repressed, repetitive states

4. Model complexity: selecting the number of states/marks – Selecting the number of states, selecting number of marks

– Capturing dependencies and state-conditional mark independence

5. Learning chromatin states jointly across multiple cell types – Stacking vs. concatenation approach for joint multi-cell type learning

– Defining activity profiles for linking enhancer regulatory networks

(Future: Chromatin states to interpret disease-associated variants)

110

#### **Interpreting disease-association signals**

**Interpret variants using reference states - Chromatin states: Enhancers, promoters, motifs - Enrichment in individual loci, across 1000s of SNPs in T1D**


**CATGACTG CATGCCTG GWAS Genotype**

**Disease mQTLs MWAS Epigenome**

###### **Epigenome changes in disease**

**- Molecular phenotypic changes in patients vs. controls - Small variation in brain methylomes, mostly genotype-driven - 1000s of brain-specific enhancers increase methylation in Alzheimer’s**

111

###### **<mark>GWAS hits in enhancers of relevant cell types</mark>**

© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roadmap Epigenomics Consortium et al. "Integrative analysis of 111 reference human epigenomes." Nature 518, no. 7539 (2015): 317-330.

112


<!-- Start of picture text -->
Linking traits to their relevant cell/tissue types<br>ES<br>Liver<br>Brain<br>Digestive<br>Heart<br>T cells  B cells<br><!-- End of picture text -->

113

###### **HaploReg: systematic mining of GWAS variants**


###### Courtesy of the authors. License: CC BY-NC.

Source: Ward, Lucas D. and Manolis Kellis. "HaploReg: a resource for exploring chromatin states, conservation, and regulatory motif alterations within sets of genetically linked variants." Nucleic Acids Research 40, no. D1 (2012): D930-D934.

- **Start with any list of SNPs or select a GWA study**

   - Mine ENCODE and Roadmap epigenomics data for hits

   - Hundreds of assays, dozens of cells, conservation, motifs

   - Report significant overlaps and link to info/browser

- **Try it out: http://compbio.mit.edu/HaploReg** Ward, Kellis NAR 2011

114

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Transition matrix akl](16-transition-matrix-akl.md) · [Up: contents](index.md)
