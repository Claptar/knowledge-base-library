---
title: Molecular Epidemiology
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Molecular Epidemiology

**Source:** `lectures/20-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Molecular Biomarkers of disease state:** Gene expression, DNA methylation, chromatin in specific cell types

44

###### Genetic and epigenetic data in 750 Alzheimer’s patients/controls

**MAP Memory and Aging Project + ROS Religious Order Study**

chr2


<!-- Start of picture text -->
meQTL−linked CpG r^2<br>meQTL SNP r^2<br>Dorsolateral PFC SNP AAF586<br>Genotype<br>439<br>(1M SNPs<br>293<br>Genotype<br>x700 ind.)<br>146<br>(De Jager)<br>0<br>3' 5<br>241,400,000 241,500,000 241,600,000 241,700,000 241,800,000 241,900,000 242,000,000 242,100,000 242,200,000 242,300,000<br>BRN.MID.FRNTL E073<br>BRN.ANG.GYR E067<br>BRN.ANT.CAUD E068<br>. BRN.CING.GYR E069<br>BRN.HIPP.MID E071<br>Brain BRN.INF.TMP E072<br>BRN.SUB.NIG E074<br>LIV.ADLT E066<br>BLD.CD14.PC E029<br>Liver BLD.CD4.MPC E037<br>Blood BLD.CD4.CD25M.CD45RA.NPC E039LNG.IMR90 E017<br>Lung GI.STMC.MUS E111<br>GI SKIN.PEN.FRSK.FIB.01 E055MUS.TRNK.FET E089<br>Skin  BONE.OSTEO E129<br>Muscle Genes(+)<br>Bone<br>Genes(−)<br>241,400,000 241,500,000 241,600,000 241,700,000 241,800,000 241,900,000 242,000,000 242,100,000 242,200,000 242,300,000<br>5' 3<br>Mean Methylation<br>Methylation<br>Normalized Methylation<br>(450k probes<br>. x 700 ind)<br>Reference<br>(De Jager)<br>Chromatin<br>Methylation StdDev<br>states  meQTL−linked CpG r^2<br><!-- End of picture text -->

**Reference (De Jager) Chromatin** Methylation StdDev **states** meQTL−linked CpG r^2 **(Bernstein)** © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. 750 subjects, initially cognitively normal, Alzheimer’s diagnosed by pathology. (Bennett)<sup>45</sup>

## Data Matrices – An example scenario

###### n=750 individuals

###### n=750 individuals


<!-- Start of picture text -->
Methylation<br><!-- End of picture text -->

Genotype


<!-- Start of picture text -->
E<br>environment<br><!-- End of picture text -->


<!-- Start of picture text -->
cause<br>D<br>G  M  Alzheimer<br>genotype<br>methylation effects disease<br><!-- End of picture text -->

###### n=750 individuals

n=750 individuals

Phenotype “Environment” (Disease)

**M** - Illumina Methylation 450k array, 450,000 probes targeting CpGs genome-wide.

- **G** - Affy SNP arrays, imputed against CEU thousand genomes reference panel, yielding 12m SNPs.

**E** - Clinical covariates that might mask the variation due to our phenotype, e.g. gender, smoking, age or sample batch.

**P** - Phenotype of interest, sometimes measured with multiple markers (clinical Alz. diagnosis vs. pathology Alz. diagnosis vs. count of neuritic plaques).

**n** -> number of individuals in cohort.

46

EWAS: Capturing variability in the Epigenome attributable to disease

**C E Experimental, Technical Environment** Cell type mixtures, Age, Education Batch effects, Other Gender, etc. Unknown Confounders **Known & ICA Known variable inferred variable correction correction X G meQTL Genotype Epigenome D** (~60K DNA methylation 5M Common **Phenotype** CpGs) Variants !lzheimer’s Disease **EWAS** Hundreds of AD associated loci, enriched in enhancers and relevant pathways

47

### Excluding discovered and known covariates

Infer covariates using ICA, compare to known, exclude both.

Strongest effects:

- **Plate (batch)**

- **Cell mixture**

- Bisulfite conversion

- Gender

- Age

Variance explained:

- Known: 25%

- Inferred: 35%

- Together: 40%

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

48

## **C E confounders**


<!-- Start of picture text -->
environment<br>cause<br>D<br>G  M<br>genotype Disease<br>methylation effects<br><!-- End of picture text -->

GenotypeMethylation **Discovering mQTLs Methylation Quantitative Trait Loci**

49

## _cis_ -meQTLs

- n=750<sup>**Use linear models to identify**</sup><sup>**_cis_-meQTLs w/in some genomic window.**</sup>


<!-- Start of picture text -->
n=750  n=750<br>M<br>G<br>000<br>000,<br>=450,000<br>m<br>12,<br>g=<br><!-- End of picture text -->

   - For methyl mark mi and SNP gj: mi = β0 + β1(gj) + ε

- Given several predictors: is additional predictor increasing accuracy more than complexity introduced?

- Likelihood ratio testing paradigm: predict methylation with and without genotype (only works for nested models)

- Null hypothesis H0: β1=0: Additional model complexity doesn’t explain a significant portion of variation in response

###### **<u>Test using F statistic:</u>**

- p is the number of parameters in LM1

LM1: mi = β0 + ε LM2: mi = β0 + β1(gj) + ε

- q is the number of parameters in LM2

- n is the sample size

- RSS: Residual sum of squares

- β: parameters to learn. ε: residual error term. Under null hypothesis: ( (RSSLM1 – RSSLM2<sup>) / (q – p) ) / ( RSS</sup> LM2<sup>/ (n – q) )</sup> Is distributed as F distribution with (q-p, n-q) degrees of freedom

- If F statistic significant: reject null: This p-value is what we report in a meQTL study

- Otherwise, no meQTL: i.e. RSSLM1 – RSSLM2 too small vs. increase in model complexity

50

## _cis_ -meQTLs


<!-- Start of picture text -->
n n<br>M<br>G<br>000<br>000,<br>=450,000<br>m<br>12,<br>g=<br><!-- End of picture text -->

Alternative methods of detection:

- Permutation:

   - Correlate methylation and genotype.

   - For i in 1 -> nperm:

      - Permute genotypes

      - Correlate methylation and genotype

   - Generate empirical p-value from permuted correlations

- LMM: Linear mixed models.

51

**Most epigenomic variability is genotype-driven Manhattan plot of 450,000 methylation probes**


<!-- Start of picture text -->
1  2<br>rs7924341 cg20132549 −1847 rs17836662 cg10853533 −44352<br>1<br>3  0.0 0.5 1.0 1.5 2.0 −0.5 4  0.5 1.5<br>Adjusted MA Dosage Adjusted MA Dosage<br>2<br>−0.5 0.5 1.5 −0.5 0.5 1.5<br>3  4<br>Adjusted MA Dosage Adjusted MA Dosage<br>0.85<br>0.6<br>0.75<br>0.4<br>Adjusted Methylation Adjusted Methylation<br>0.2 0.65<br>0.72<br>0.30<br>0.68<br>0.20<br>0.64<br>Adjusted Methylation Adjusted Methylation<br>0.10<br>0.60<br><!-- End of picture text -->


<!-- Start of picture text -->
0<br><!-- End of picture text -->

- Chromosome and genomic position

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


• Genome-wide significance at <mark>p<3x10</mark><sup>-10</sup> . • Prune for probes disrupted by SNP.

- 140,000 CpGs associated with genotype at 1% FDR

- 55,000 at Bonferroni-corrected P-value of 10<sup>-2</sup>

52

### Scaling of discovery power with individuals


   - © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- Number of meQTLs continues to increase linearly

- Weak-effect meQTLs: median R<sup>2</sup> <0.1 after 400 indiv.

53

### **Goal: Personalized and Predictive Medicine**

1. Intro to Epidemiology: basis of human disease

2. Genetic Epidemiology:

– Genetic basis: GWAS and screening

– Interpreting GWAS with functional genomics

– Calculating functional enrichments for GWAS loci

3. Molecular epidemiology

– meQTLs: Genotype-Epigenome association (cis-/trans-) <mark>– EWAS: Epigenome-Disease association</mark>

4. Resolving Causality

– Statistical: Mendelian Randomization

– Application to genotype + methylation in AD

5. Systems Genomics and Epigenomics of disease

– Beyond single loci: polygenic risk prediction models

– Sub-threshold loci and somatic heterogeneity in cancer

54

## **C E confounders**


**environment**


**cause G M D genotype methylation effects Disease**

---

[← Three lines of linking evidence](05-three-lines-of-linking-evidence.md) · [Up: contents](index.md) · [MethylationDisease →](07-methylation-disease.md)
