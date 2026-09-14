---
title: Causality testing
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Causality testing

**Source:** `lectures/20-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

71

## Modeling complex Human diseases

- Three possible models:

1. Independent Associations


<!-- Start of picture text -->
G M<br>X<br>D<br><!-- End of picture text -->

2. Causal Pathway Model

**G**


<!-- Start of picture text -->
M<br><!-- End of picture text -->

**D**

3. Interaction Model

**G** Genotype **M** Methylation **D** Disease


<!-- Start of picture text -->
G M<br>D<br><!-- End of picture text -->

72

## (1) Independent Associations


<!-- Start of picture text -->
G M<br>X<br>D<br><!-- End of picture text -->

- Association between Factor A and Disease

- Association between Factor B and Disease

- No association between Factor A and Factor B

- Example: 2 independent risk genes

**G** Factor A **X** Factor B

**Y** Disease D

73

## (2) Causal Pathway Models

- Is the a direct link between risk factor (A) and disease (D)?

**A**

**D**

- Does the risk factor’s (!) effect on disease (D) depend on an intermediate step (B)?

**A**

**B**

**D**

- To test:

   - A is associated with B and D

   - B is associated with D

   - A is not associated with D when controlling for B

**G** Factor A

- Note: A **MUST** come before B temporally

**X** Factor B **D** Disease D

74

   - (2) Causal Pathway Models

- In reality its a little of both; !’s affect on D is partially _mediated_ through B


<!-- Start of picture text -->
A  B D<br><!-- End of picture text -->

**A B**

- To test:

   - A is associated with B and D

   - B is associated with D

   - The effect size of A on D is decreased  when controlling for B

   - Note: A **MUST** come before B temporally

**A** Factor A

- Example: _CR1_ effect on cognitive decline

**B** Factor B **D** Disease D

75

## (3) Interaction Models

- Factor B’s effect on D is different depending on value for factor !


<!-- Start of picture text -->
B B B<br>(A = AA)  (A = Aa)  (A = aa)<br>D<br><!-- End of picture text -->

- To test:

   - A + B + A*B  D, if estimate for A*B is significant then

   - Stratify by levels of A

- Example:

   - ! drug’s effect is different depending on genotype

   - More to come<

76

## Application to 12 AD GWAS loci

|**Gene**|**locus**|<br>**reference**|**Published**<br>**AD**|**AD**|**NP**|
|---|---|---|---|---|---|
|ABCA7|rs3764650|Hollingsworth 2010|5.0x10<sup>-21</sup>|0.747|0.187|
|APOE|<br>Anyε4|||1.2x10<sup>-13</sup>|<br>1.8x10<sup>-23</sup>|
|BIN1|rs744373|Seshadri 2010|1.6x10<sup>-11</sup>|0.204|0.480|
|CD2AP|rs9349407|Naj 2011/Hollingsworth 2011|8.6x10<sup>-9</sup>|0.445|0.221|
|CD33|rs3865444|Naj 2011/Hollingsworth 2012|1.6x10<sup>-9</sup>|0.133|0.123|
|CLU|rs11136000|Lambert 2009/Harold 2009|7.5x10<sup>-9</sup>|0.762|0.649|
|CR1|rs6656401|Lambert 2009|3.7x10<sup>-9</sup>|0.0009|0.057|
|EPHA1|rs11767557|Naj 2011/Hollingsworth 2011|6.0x10<sup>-10</sup>|0.562|0.391|
|MS4A4A|rs4938933|Naj 2011|1.7x10<sup>-9</sup>|0.792|0.567|
|MS4A6A|rs610932|Hollingsworth 2010|1.2x10<sup>-16</sup>|0.534|0.820|
|MTHFD1L|rs11754661|Naj 2010|1.9x10<sup>-10</sup>|0.126|0.934|
|PICALM|rs3851179|Harold 2009|1.9x10<sup>-8</sup>|0.382|0.171|


77

## CR1: Causal pathway model

###### Risk Factors

Pathology

Clinical

Disease

**Genetic** _CR1_

**AD specific Cognitive Alzheimer’s** Neuritic Plaque **Decline disease** Neurofibulary Tangles ?

- _CR1_ first associated with AD in 2009

- Original associated variant is in an intron, no clear function

- Unclear how _CR1_ locus influences AD susceptibility mechanistically

- Questions:

   - Is the effect only on AD?

   - Is there a broader effect on cognitive decline?

   - Is there an association with AD pathology?

   - Does it go through pathology to have an effect of cognitive decline?

78

## _CR1_ (rs6656401)

###### _CR1_  Pathology

TT


<!-- Start of picture text -->
0.85<br>0.8<br>0.75<br>0.7<br>CR1   Global Cognitive<br>0.65  Decline<br>0.6<br>0.55<br>0.5<br>0.45<br>0.4<br>Neuritic Plaque  Neurofibillary Tangles<br>p=0.008 p=0.10<br><!-- End of picture text -->

AT/AA (risk allele)


<!-- Start of picture text -->
p=0.0008<br><!-- End of picture text -->

Pathology  Global Cognitive Decline p < 0.0001

time

79

##### **Genetic + Epigenetic variation in !lzheimer’s**


<!-- Start of picture text -->
Gen ome Epigenome  Phenotype<br>meQTL<br>1 Classification<br>2<br>MWAS<br>Epigenome<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Methylation variation in 723 AD patients & controls**

###### **Relate to genotype and AD variation**


###### **_Methylation >> SNPs Enhancers >> promoters_**


**Estimate causal M roles: regression of meQTL effects reduces M**  **D**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

80

### **Goal: Personalized and Predictive Medicine**

1. Intro to Epidemiology: basis of human disease

2. Genetic Epidemiology:

– Genetic basis: GWAS and screening

– Interpreting GWAS with functional genomics

– Calculating functional enrichments for GWAS loci

3. Molecular epidemiology

– meQTLs: Genotype-Epigenome association (cis-/trans-) – EWAS: Epigenome-Disease association

4. Resolving Causality

– Statistical: Mendelian Randomization

– Application to genotype + methylation in AD

5. Systems Genomics and Epigenomics of disease – Beyond single loci: polygenic risk prediction models

– Sub-threshold loci and somatic heterogeneity in cancer

81

Beyond top-scoring hits: 1000s of variants of weak effect cluster in cell type specific enhancers

82

##### **Rank-based functional testing of weak associations**

**Enrichment peaks at 10,000s of SNPs down the rank list, even after LD pruning!**

   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Rank all SNPs based on GWAS signal strength**

- • **Functional enrichment for cell types and states**

83

### **Weak-effect T1D hits in 50k T-cell enhancers**


<!-- Start of picture text -->
enhancers<br><!-- End of picture text -->


<!-- Start of picture text -->
CD4+ T-cells<br>T-cells<br>B-cells<br>Other cell types<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

• **LD-pruning (CEU r**<sup>**2**</sup> **>.2): 50k**  **41k independ. loci**

84

## **Cell type specificity stronger for enhancers enhancers promoters**


<!-- Start of picture text -->
promoters<br>CD4+ T-cells<br>T-cells<br>B-cells<br>Other cell types<br>transcribed<br>© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br><!-- End of picture text -->

• **T/B-cells also enriched for promoters, transcribed** 85 • **Enhancer enrichment much more cell type specific**

###### **T1D/RA-enriched enhancers spread across genome**


   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw. mit.edu/help/faq-fair-use/.

- **High concentration of loci in MHC, high overlap**

• **Yet: many distinct regions, 1000s of distinct loci**

86

## **Implications for genetic predisposition: polygenic models for risk prediction**

87

### Basic setup of polygenic risk prediction studies


<!-- Start of picture text -->
Case-control cohort w/<br>Target cohort:<br>genotype + phenotype<br>genotyped individuals<br>(no phenotypes)<br>Training cohort Testing cohort<br>(power matters) (power matters) (power limited to one<br>individual at a time)<br>Selection of SNPs<br>1 2<br>Estimation of effects Apply predictor Apply predictor w/<br>Evaluate accuracy estimated confidence<br>Ranking<br><!-- End of picture text -->

- Applications 1: 1 (testing cohort) – Understand total heritability captured in common variants

   - Understand disease “architecture”: number of SNPs

   - Recognize functional classes associated with weak genetic associations

- Applications 2: 2 (new individuals)

   - Provide health recommendations at the individual level

   - Prioritize high-risk individuals for subsequent testing at population level

88

## How many SNPs to include in model?


<!-- Start of picture text -->
pi0:Proportion of markers with no effect<br>‘only 5% matter’<br><!-- End of picture text -->

- ‘only 5% matter’

Dudridge PLoS Genetics 2013 Purcell Nature 2009 Schizophrenia risk prediction

‘only 10% matter’ (but still can’t tell Which ones until ‘all matter’ Full rank list)

###### inclusion threshold

   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- It depends on:

   - Architecture: Fraction of SNPs that are estimated to be functional

   - Power: Number of individuals in cohort, i.e. ability to rank correctly

- It only peaks at 5% (≈1-pi0) when sufficient power to rank – Large fraction of associated markers are hidden within non-significant SNPs

• For pi0=0.90, still need to include all SNPs to maximize predictive power

89

## Application to pleiotropy and common risk

**Trait 1 (schizophrenia) Trait 2 (bipolar disorder) Case-control cohort w/ Case-control cohort w/ genotype + phenotype genotype + phenotype**

**Selection of SNPs Estimation of effects Apply predictor Evaluate accuracy Ranking**

- Ability to assess common genetic risk

   - Are the highly-ranked SNPs for one study relevant to a different study?

   - Is there a shared genetic architecture between seemingly unrelated traits?

- First use showed schizophrenia and bipolar disorder common risk – Schizophrenia-ranked SNPs in one cohort<

      - < are predictive of bipolar disorder diagnosis

   - < but not predictive of unrelated (cardiovascular) traits

90

### Important points/caveats for risk prediction

- Always limited by genetic component

   - Environment, random effects play big role for most traits

- Mendelian=deterministic vs. common variants=prob.ic

   - Only a first screen for individuals at risk

- Limited by discovery power

   - Cohort size limits discriminative power and ranking ability

- Limited by genotyped SNPvs vs. all SNPs

   - Selection pushes fitness-reducing variants to lower freq

   - Genotyped SNPs selected to be common

- Even if SNPs are correctly identified, their effects are not

   - Winner’s curse: over-estimate above-threshold true effect

- Training and testing cohort non-independence

   - Relatives, cryptic relatedness, population stratification inflate est. 91

91

### **Goal: Personalized and Predictive Medicine**

1. Intro to Epidemiology: basis of human disease

2. Genetic Epidemiology:

– Genetic basis: GWAS and screening

– Interpreting GWAS with functional genomics

– Calculating functional enrichments for GWAS loci

3. Molecular epidemiology

– meQTLs: Genotype-Epigenome association (cis-/trans-) – EWAS: Epigenome-Disease association

4. Resolving Causality

– Statistical: Mendelian Randomization

– Application to genotype + methylation in AD

5. Systems Genomics and Epigenomics of disease

– Beyond single loci: polygenic risk prediction models

<mark>– Sub-threshold loci and somatic heterogeneity in cance</mark> r

92

###### **_This talk: From loci to mechanisms_**

###### **_Building a reference map of the regulatory genome_**

**Enhancers Promoters Transcribed Repressed Regions** : Enhancers, promoters, transcribed, repressed **Cell types** : Predict tissues and cell types of epigenomic activity **Target genes** : Link variants to their target genes using eQTLs, activity, Hi-C **Nucleotides** : Regulatory consequence of mutation: Conservation, PWMs **Regulators** : Upstream regulators whose activity is disrupted by mutation

**_Application to GWAS, hidden heritability, and Cancer_ GWAS CATGCCTG** • 93% top hits non-coding  Mechanism? Cell type? **hits CGTGTCTA** • Lie in haplotype blocks  Causal variant(s)? **‘Hidden’ CATGCCTG** • Many variants, small effects  Pathway-level burden/load **heritability CGTGTCTA** • Many false positives  Prioritize w/ regulatory annotations

**Cancer CATGCCTG**<sup>•</sup> Loss of function  Protein-coding variants, convergence **mutations CATCCCTG** • Gain of function  Regulatory variants, heterogeneity

93

###### **Characterizing sub-threshold variants in heart arrhythmia**


- © source unknown. All rights reserved.This content is excluded from our Creative

- Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


###### **_Focus on sub-threshold variants (e.g. rs1743292 P=10_**<sup>**_-4.2_**</sup> **_)_**

From Arking, D. E., Pulit, S. L., Crotti, L., Harst, P. V., Munroe, P. B., Koopmann, T. T., . . . Newton-Cheh, C. (2014). Genetic association study of QT interval highlights role for calcium myocardial repolarization. Nature Genetics Nat Genet, 46(8), 826-836. Used with permission.

- **_Trait: QRS/QT interval_**

- (1) Large cohorts, (2) many known hits

- (3) well-characterized tissue drivers

94

###### **Enhancers overlapping GWAS loci share functional properties**


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**_Train machine learning model to prioritize sub-threshold loci_**

95

##### Functional evidence for sub-threshold target genes


**_Human genetics_**


**_Zebrafish phenotypes_**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**_Mouse phenotypes_**

96

#### **Experimental validation of 11 sub-threshold loci**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### **_9 of 11 tested loci show allelic activity, chromatin interactions_**

97

##### **Functional evidence for rs1743292 causality (P=10**<sup>**-4.2**</sup> **)**


###### **_Enhancer 4C links to target gene promoters_**

**_Heart enhancer activity_**


###### **_Motif disruption_**

**_Allelic DNase in multiple individuals_**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**_Allelic enha-_** 98 **_ncer activity_**

##### **Target gene impact on heart conduction**

###### Optical voltage mapping

ventricle

atrium

transmembrane voltage (ventricle)

zebrafish embryo hearts voltage-sensitive fluorescent dye


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

###### **_Detection and validation of a new cardiac locus_**

99

###### **What would we need to discover rs1743292 without epigenomics?**

**rs1743292** Minor allele frequency: 0.134 Effect size: -0.5773 +/- 0.17 msec With 68,900 individuals: 12.8% power to discover at p<5x10<sup>-8</sup>

- rs1743292 has similar effect sizes as many genome-wide significant variants

- Many GWAS variants discovered due to **winner’s curse** : often only have 5- 20% power to discover

- Combining epigenomics and GWAS can:

   1. Confirm existing GWAS loci are real

   2. Discover new sub-threshold loci with weak effect sizes, low power

To reach 80% power to discover rs1743292 at p<5x10<sup>-8</sup> , we need **146,700** individuals!

100

### **Goal: Personalized and Predictive Medicine**

1. Intro to Epidemiology: basis of human disease 2. Genetic Epidemiology:

   - Genetic basis: GWAS and screening

- Interpreting GWAS with functional genomics

- – Calculating functional enrichments for GWAS loci

- 3. Molecular epidemiology

– meQTLs: Genotype-Epigenome association (cis-/trans-) – EWAS: Epigenome-Disease association 4. Resolving Causality

   - Statistical: Mendelian Randomization

- Application to genotype + methylation in AD

- 5. Systems Genomics and Epigenomics of disease – Beyond single loci: polygenic risk prediction models

   - Sub-threshold loci and <mark>somatic heterogeneity in cancer</mark>

101

###### **_This talk: From loci to mechanisms_**

###### **_Building a reference map of the regulatory genome_**

**Enhancers**

**Promoters Transcribed**

**Repressed**


**Regions** : Enhancers, promoters, transcribed, repressed **Cell types** : Predict tissues and cell types of epigenomic activity **Target genes** : Link variants to their target genes using eQTLs, activity, Hi-C **Nucleotides** : Regulatory consequence of mutation: Conservation, PWMs **Regulators** : Upstream regulators whose activity is disrupted by mutation

**_Application to GWAS, hidden heritability, and Cancer_ GWAS CATGCCTG** • 93% top hits non-coding  Mechanism? Cell type? **hits CGTGTCTA** • Lie in haplotype blocks  Causal variant(s)? **‘Hidden’ CATGCCTG** • Many variants, small effects  Pathway-level burden/load **heritability CGTGTCTA** • Many false positives  Prioritize w/ regulatory annotations **Cancer CATGCCTG** • Loss of function  Protein-coding variants, convergence **mutations CATCCCTG** • Gain of function  Regulatory variants, heterogeneity

102

###### **Regulatory convergence of dispersed driver mutations**


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **Common mutations in regulatory plexus of each gene Richard Sallari** 103

###### **Cancer genes are more likely to be up-regulated**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Richard Sallari**<sup>104</sup>

###### **Dysregulated genes show dispersed non-coding mutations**


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Dysregulated genes are enriched for plexus mutations at all distances.

**Richard Sallari**<sup>105</sup>

###### **Non-coding mutations enriched in promoters / enhancers active in other cell types**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Disruptive mutations in ‘low’ elements are enriched in enhancers and promoters in other tissues **Richard Sallari**

106

##### **Statistical model for excess of rare/somatic variants**


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- • **Correct for region-, state-, tumor-specific rate variation**

107

##### **Convergence in immune, signaling, mitoch. functions**


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

• **Pathway-level convergence, hierarchical model**

108

##### **Non-coding drivers of prostate cancer dysregulation**


###### **_Regulatory mutations reveal new cancer driver genes_**

###### **_Convergence in immune, signaling,_**

###### **_mitochondrial functions_**


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- **_Convergence in inositol phosphate metabolism PLCB4 overexpression in PC3 prostate cancer adjacent to PTEN, PIK3CA, known cancer genes_**<sup>**_reduces Erk/Akt activity, synergistic with PTEN_**</sup> 109

### Personal genomics tomorrow: Already 100,000s of complete genomes

- Health, disease, quantitative traits:

   - Genomics regions  disease mechanism, drug targets

   - Protein-coding  cracking regulatory code, variation

   - Single genes  systems, gene interactions, pathways

- Human ancestry:

   - Resolve all of human ancestral relationships

   - Complete history of all migrations, selective events

   - Resolve common inheritance vs. trait association

- What’s missing is the computation

   - New algorithms,  machine learning, dimensionality reduction

   - Individualized treatment from 1000s genes, genome

   - Understand missing heritability

   - Reveal co-evolution between genes/elements

   - Correct for modulating effects in GWAS

110

## **Challenge ahead: From research to clinic**

1. Systematic medical genotyping / sequencing

   - Currently a curiosity, future: medical practice

2. Systematic medical molecular profiling

   - Functional genomics in relevant cell types

3. Systematic perturbation studies for validation

   - 1000s of regulatory predictions x 100s cell types

4. Systematic repurposing of approved drugs

   - Systems-biology view of drug response

5. Genomics of drug response in clinical trials

   - Personalized drug prescription and combinations

6. Partnerships:  academia, industry, hospitals

   - Interdisciplinary training in each of the instituttions

111

### **Summary: Personalized & Predictive Medicine**

1. Intro to Epidemiology: basis of human disease

2. Genetic Epidemiology:

- Genetic basis: GWAS and screening

- Interpreting GWAS with functional genomics

- Calculating functional enrichments for GWAS loci

3. Molecular epidemiology

– meQTLs: Genotype-Epigenome association (cis-/trans-) – EWAS: Epigenome-Disease association

4. Resolving Causality

   - Statistical: Mendelian Randomization

   - Application to genotype + methylation in AD

5. Systems Genomics and Epigenomics of disease

   - Beyond single loci: polygenic risk prediction models

– Sub-threshold loci and somatic heterogeneity in cancer

112

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← eWAS](09-ewas.md) · [Up: contents](index.md)
