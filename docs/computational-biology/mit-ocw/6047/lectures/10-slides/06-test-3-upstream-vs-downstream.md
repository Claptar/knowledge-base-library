---
title: 'Test 3: Upstream vs. Downstream'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Test 3: Upstream vs. Downstream

**Source:** `lectures/10-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
CGG-11-CCG<br>Downstream motifs?<br>Most<br>Patterns<br>Downstream Conservation<br>Upstream Conservation<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

53

###### **Conservation for TF motif discovery**

###### **1. Enumerate motif seeds**

**<mark>T G</mark> C** **_gap_ T** **<mark>A G</mark>**

   - Six non-degenerate characters with variable size gap in the middle

**2. Score seed motifs**

   - Use a conservation ratio corrected for composition and small counts to rank seed motifs

**3. Expand seed motifs**

**<mark>S R T G</mark> C** **<mark>Y</mark>** **_gap_** **<mark>W</mark> T** **<mark>A G R</mark>**

   - Use expanded nucleotide IUPAC alphabet to fill unspecified bases around seed using hill climbing

**4. Cluster to remove redundancy**

   - Using sequence similarity

**Kellis, Nature 2003**

54

###### **Learning motif degeneracy using evolution**


• Record frequency with which one sequence  is “replaced” by another in evolution

- Use this to find clusters of k-mers that correspond to a single motif

© Cold Spring Harbor Laboratory Press. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Tanay, Amos et al. "A global view of the selection forces in the evolution of yeast cis-regulation." Genome Research 14, no. 5 (2004): 829-834.

**Tanay, Genome Research 2004**

55

###### **Motif discovery overview**

1. Introduction to regulatory motifs / gene regulation – Two settings: co-regulated genes (EM,Gibbs), de novo

2. Expectation maximization: Motif matrixpositions – E step: Estimate motif positions Zij from motif matrix

– M step: Find max-likelihood motif from all positions Zij

3. Gibbs Sampling: Sample from joint (M,Zij) distribution – Sampling motif positions based on the Z vector

- More likely to find global maximum, easy to implement

- 4. Evolutionary signatures for _de novo_ motif discovery – Genome-wide conservation scores, motif extension

- <mark>Validation of discovered motifs: functional datasets</mark>

- 5. Evolutionary signatures for instance identification – Phylogenies, Branch length score  Confidence score

- – Foreground vs. background. Real vs. control motifs.

56

###### **Validation of the discovered motifs**

- Because genome-wide motif discovery is _de novo_ , we can use functional datasets for validation

   - Enrichment in co-regulated genes

   - Overlap with TF binding experiments

   - Enrichment in genes from the same complex

   - Positional biases with respect to transcription start

   - Upstream vs. downstream / inter vs. intra-genic bias

   - Similarity to known transcription factor motifs

- Each of these metrics can also be used for discovery

   - In general, split metrics into discovery vs. validation

   - As long as they are _independent_ !

   - Strategies that combine them all lose ability to validate

      - Directed experimental validation approaches are then needed

57

###### **Similarity to known motifs**

- If discovered motifs are real, we expect them to match motifs in large databases of known motifs

- We find this (significantly higher than with random motifs)

|**MCS**|**Discovered motif**|**Known**<br>**Factor**|
|---|---|---|
|46.8|**GGGCGG**R|SP-1|
|34.7|**GCCATnTT**g|YY1|
|32.7|**CACGTG**|MYC|
|31.2|G**ATTGGY**|NF-Y|
|30.8|**TGA**n**TCA**|AP-1|
|29.7|**GGGAGG**RR|MAZ|
|29.5|**TGACGTM**R|CREB|
|26.0|**CGGCCAT**YK|NF-MUE1|
|25.0|**TGACCTTG**|ERR|
|22.6|**CCGGAAR**Y|ELK-1|
|19.8|S**CGGAAG**Y|GABP|
|17.9|**CA**T**TTCC**K|STAT1|


- Why not perfect agreement?

###### **70/174 mammalian motifs**

- Many known motifs are not conserved

- Known motifs are biased; may have missed real motifs

|**MCS**|**Discovered motif**|**Known**<br>**Factor**|
|---|---|---|
|65.6|CTAATTAAA|en|
|57.3|TTKCAATTAA|repo|
|54.9|WATTRATTK|ara|
|54.4|AAATTTATGC<br>K|prd|
|51|GCAATAAA|vvl|
|46.7|DTAATTTRYN<br>R|Ubx|
|45.7|TGATTAAT|ap|
|43.1|YMATTAAAA|abd-A|
|41.2|AAACNNGTT||
|40|RATTKAATT||
|39.5|GCACGTGT|ftz|
|38.8|AACASCTG|br-Z3|


**35/145 fly motifs**

58

###### **Positional bias of motif matches**

• Motifs are involved in initiation of transcription

Motif matches biased versus TSS

– 10% of fly motifs

– 34% of mammalian motifs

Depletion of TF motifs in coding sequence

– 57% of fly motifs

Clustering of motif matches

– 19% of fly motifs

59

###### **Motifs have functional enrichments**


<!-- Start of picture text -->
Tissues<br><!-- End of picture text -->

For both fly (top) and mammals (bottom), motifs are enriched in genes expressed in specific tissues


<!-- Start of picture text -->
Motifs<br><!-- End of picture text -->


<!-- Start of picture text -->
2. Functional clusters emerge<br><!-- End of picture text -->

Reveals modules of cooperating motifs

###### **1. Most motifs avoided in ubiquitously expressed genes**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

60

**TF1**

**TF2 microRNA1**


**Motif instance identification How do we determine the functional binding sites of regulators?**

**Kheradpour, Stark, Roy, Kellis, Genome Research 2007**

61

###### **Experimental target identification: ChIP-chip/seq**

Limitations :

- Antibody availability

- Restricted to specific stages/tissues

- • Biological functionality of most binding sites unknown

- • Resolution can be limited (can’t usually identify the precise base pairs)


**Ren et al., 2000; Iyer et al., 2001 (ChIP-chip) Robertson et al., 2007  (ChIP-seq)**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

62

###### **Computational target identification**

• Single genome approaches using motif clustering (e.g. Berman 2002; Schroeder 2004; Philippakis 2006)

– Requires set of specific factors that act together

- Miss instances of motifs that may occur alone

- • Multi-genome approaches (phylogentic footprinting) (e.g. Moses 2004; Blanchette and Tompa 2002; Etwiller 2005; Lewis 2003)

   - Tend to either require absolute conservation or have a strict model of evolution

63

###### **Challenges in target identification**


      - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Simple case

   - Instance fully conserved in orthologous position near genes

- Motif turn-around/movement

   - Motif instance is not found in orthologous place due to birth/death or alignment errors

- Distal/missing matches

   - Due to sequencing/assembly errors or turnover

   - Distal instances can be difficult to assign to gene

64

#### **Computing Branch Length Score (BLS)**

**mutations**

**movement**

**missing short branches**

**Allows for:**

**BLS = 2.23sps (78%)**


<!-- Start of picture text -->
CTCF<br><!-- End of picture text -->

**1. Mutations permitted by motif degeneracy**

**2. Misalignment/movement of motifs within window (up to hundreds of nucleotides)**

**3. Missing motif in dense species tree**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

65

###### **Branch Length Score**  **Confidence**

1. Evaluate chance likelihood of a given score

- Sequence could also be conserved due to overlap with un-annotated element (e.g. non-coding RNA)

- 2. Account for differences in motif composition and length

   - For example, short motif more likely to be conserved by chance

66

###### **Branch Length Score**  **Confidence**


**1. Use motif-specific shuffled control motifs determine the expected number of instances at each BLS by chance alone or due to nonmotif conservation**

**2. Compute Confidence Score as fraction of instances over noise at a given BLS (=1 – false discovery rate)**

67

###### **Producing control motifs**


When evaluating the conservation, enrichment, etc, of motifs, it is useful to have a set of “control motifs”

**1**

###### **Original motif**

**Produce 100 shuffles of our original motif**


**Filter motifs, requiring they match the genome with about (+/- 20%) of our original motif Sort potential control motifs based on their similarity to other known motifs**

###### **Genome sequence**

**2**

**3**

**Known motifs**

**4**

**Cluster potential control motifs and take at most one from each cluster, in increasing order of similarity to known motifs**


68

###### **Computing enrichments: background vs. foreground**

- Background vs. forgeround

###### **Background (e.g. Intergenic):**

###### **Foreground (e.g. TF bound):**

      - co-regulated promoters vs. all genes

   - Bound by TF vs. other intergenic regions

   - • Enrichment: **_fraction of motif instances in foreground_** vs. **_fraction of bases in foreground_**

   - Correct for composition/conservation level: compute enrichmt w/control motifs

- #in foreground size of foreground 

- #in background size of background

   - Fraction of motif instances can be compared to **fraction of control motif instances in foreground**

   - A hypergeometric p-value can be computed (similar to χ<sup>2</sup> , but better for small numbers)

- #in foreground #control in foreground 

- #in background #control in background

###### **binomial confidence interval**


<!-- Start of picture text -->
0.0  1.0<br>fraction<br>use this<br><!-- End of picture text -->

- Fractions can be made more conservative using a binomial confidence interval

69

#### **Confidence selects for functional instances**


<!-- Start of picture text -->
Transcription factor motifs  MicroRNA motifs<br>3’UTR<br>3’UTR<br>Intron<br>Intron<br>CDS<br>CDS<br>5’UTR<br>5’UTR<br>Promoter<br>Promoter<br><!-- End of picture text -->

**1. Confidence selects for transcription factor motif instances in promoters and miRNA motifs in 3’ UTRs**

70

###### **Validation of discovered motif instances**

Use independent experimental evidence Look for functional biases / enrichments

71

#### **Confidence selects for functional instances**


<!-- Start of picture text -->
Strand Bias<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**1. Confidence selects for transcription factor motif instances in promoters and miRNA motifs in 3’ UTRs 2. miRNA motifs are found preferentially on the plus strand, whereas no such preference is found for TF motifs** 72

72

###### **Increased sensitivity using BLS**

Figure 3 B removed due to copyright restrictions. Source: Kheradpour, Pouya et al. "Reliable prediction of regulator targets using 12 Drosophila genomes." Genome Research 17, no. 12 (2007): 1919-1931.

73

#### **Intersection with CTCF ChIP-Seq regions**


<!-- Start of picture text -->
≥  50% of regions with a motif<br><!-- End of picture text -->


<!-- Start of picture text -->
ChIP data from Barski,  et al. ,  Cell  (2007)<br><!-- End of picture text -->

**ChIP-Seq and ChIP-Chip technologies allow for identifying binding sites of a motif experimentally**

- Conserved CTCF motif instances highly enriched in ChIP-Seq sites

- High enrichment does not require low sensitivity

- Many motif instances are verified


<!-- Start of picture text -->
50% motifs verified<br>50% confidence<br><!-- End of picture text -->

74

###### **Enrichment found for many factors**


**Mammals Flies**


75

###### **Enrichment increases in conserved bound regions**


**1. ChIP bound regions may not be conserved 2. For CTCF we also have binding data in mouse**

**3. Enrichment in intersection is dramatically higher**

**Human: Barski,** **_et al._ ,** **_Cell_ (2007) Mouse: Bernstein, unpublished**

76

## **More enrichment when binding**

## **conserved**


**1. ChIP bound regions may not be conserved**

**2. For CTCF we also have binding data in mouse**

**3. Enrichment in intersection is dramatically higher**

**4. Trend persists for other factors where we have multi-species ChIP data**

77

## **Comparing ChIP to Conservation**


###### **1. Motifs at 60% confidence and ChIP have similar enrichments (depletion for the repressor Snail) in the functional promoters**

**2. Enrichments persist even when you look at non-overlapping subsets**

**3. Intersection of two regions has strongest signal**

**4. Evolutionary and experimental evidence is complementary**

   - **ChIP includes species specific regions and differentiate tissues**

   - **Conserved instances include binding sites not seen in tissues surveyed**

**ChIP data from: Zeitlinger,** **_et al_ .,** **_G&D_ (2007); Sandmann,** **_et al,_ .** **_G&D_ (2007); Sandmann,** **_et al., Dev Cell_ (2006)**

78

#### **Fly regulatory network at 60% confidence**


**TFs: 67 of 83 (81%) 46k instances miRNAs: 49 of 67 (86%) 4k instances**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Several connections confirmed by literature (directly or indirectly) Global view of instances allows us to make network level observations:**

- **46% of targets were co-expressed with their factor in at least one tissue (P < 2 x 10**<sup>**-3**</sup> **)**

- **TFs were more targeted by TFs (P < 10**<sup>**-20**</sup> **) and by miRNAs (P < 5 x 10**<sup>**-5**</sup> **)**

- **TF in-degree associated with miRNA in-degree (high-high: P < 10**<sup>**-4**</sup> **; low-low P < 10**<sup>**-6**</sup> **)**

79

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

80

---

[← Test 2: Intergenic vs. Coding](05-test-2-intergenic-vs-coding.md) · [Up: contents](index.md) · [Challenges in regulatory genomics →](07-challenges-in-regulatory-genomics.md)
