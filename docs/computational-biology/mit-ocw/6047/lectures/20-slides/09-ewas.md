---
title: eWAS
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# eWAS

**Source:** `lectures/20-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### n

n

Link methylationphenotype (~cis-eQTLs): Phenotype • linear models and hypothesis testing (Disease) • Predict phenotype using methylation

n

Methylation

“Environment”

Problem:

variance due to phenotype probably very small (unless your phenotype is cancer)  Needle in a haystack

Control for other sources of variance to make the variance due to the phenotype stand out.

LM1: AD = β0 + β2(gender) + ε LM2: AD = β0 + β1(mj) + β2(gender) ε

If phenotype is !lzheimer’s (!D), gender incorporates more variance into your M matrix than does AD.

57

## eWAS


<!-- Start of picture text -->
n n<br>Might have many environmental<br>Phenotype<br>variables to control for.<br>(Disease)<br>n<br>“Environment”<br>Methylation<br>LM1: AD = β0 + β2(gender) + β3(age) + β4(education) + < + ε<br>LM2: AD = β0 + β1(mj) + β2(gender) + β3(age) + β4(education) + < + ε<br>p=10<br>e=15<br>m=450,000<br><!-- End of picture text -->

58

## eWAS

###### **Need to account for variance due to genotype as well.**


<!-- Start of picture text -->
n<br><!-- End of picture text -->


<!-- Start of picture text -->
n n n<br>Phenotype<br>(Disease)<br>n<br>“Environment”<br>Methylation<br>Genotype<br>p=10<br>e=15<br>g=12,000,000 m=450,000<br><!-- End of picture text -->

59

Role of enhancers vs. promoters in !lzheimer’s disease association

60

###### **Enhancers are hemi-methylated and highly variable**


<!-- Start of picture text -->
Promoters show<br>least variable<br>methylation<br>Enhancers show<br>most variable<br>methylation<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

• **Highly distinct signatures for promoters vs. enhancers**

- **Enhancers hemi-methylated in each person (not bimodal)**

Methylation level

Methylation level

61

SNP-associated CpGs in enhancers, not promoters


<!-- Start of picture text -->
TSS flanking<br>* Enhancers Repressed<br>*<br>*<br>*<br>*<br>* * *<br>* * *<br>TxEnh<br>*<br>*<br>Transcribed<br>Promoters<br>*<br>2<br>.5<br><!-- End of picture text -->

• Promoter methylation less affected by genetics • Enhancer methylation highly genotype-driven

• TSS-flanking and repressed regions also genetic

62

## AD-associated probes in distal enhancers


<!-- Start of picture text -->
Enhancers<br>Promoters<br><!-- End of picture text -->

   - © source unknown. All rights reserved. This content is excluded from our Creative

   - Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- After cleaning with known and inferred covariates.

- Distal and transcribed enhancers enriched.

- Proximal regulators (promoters) depleted.

63

##### **ICA covariate correction cleans up enhancer signal**

**Before: Orange** : Enrichment of enhancer probes for association with the real phenotype. **Grey** : Enrichment of enhancer probes for a scrambled phenotype.

**After:** ( **After** conditioning on 7 surrogate variables discovered with ICA.)


<!-- Start of picture text -->
Empirical p=0.06<br><!-- End of picture text -->


<!-- Start of picture text -->
Empirical p<.0001<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

64

## AD predictive power highest in enhancers


<!-- Start of picture text -->
Top predictive<br>enhancers<br>features are:<br>methylome<br>• Enhancer<br>promoters methylation<br>•  A<br>All SNPs ll methyl.<br>•  TSS, Het<br>• Genetics<br>(incl. APOE)<br>•  Causality?<br>• Common<br>pathways?<br>APO E<br><!-- End of picture text -->

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

65

##### **AD prediction reveals likely biological pathways**


<!-- Start of picture text -->
AUC using pathway feature selection; p= 1.922e−11<br>NRSF<br>All probes, ranked by AD assoc. P-value<br>ELK1<br>All probes, ranked by AD assoc. P-value<br>CTCF<br>Non−significant pathways Significant pathways<br>© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Enriched regulatory motifs<br>suggest potential pathways<br>HEB/Tcf12: proliferating neural and progenitor cells<br>GATA: cell growth, blood, cell development<br>TLX1/NFIC: Neuronal cell fates   Mouse AD models  66<br>0.75<br>0.70<br>0.65<br>0.60<br><!-- End of picture text -->

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

– Sub-threshold loci and somatic heterogeneity in cancer

67

### **Risk factor causality w/ instrumental variables**

**C E**

**confounders environment**


<!-- Start of picture text -->
causes<br>G  X Y<br>instrument<br>outcome<br>risk factor<br>effects<br><!-- End of picture text -->

If XY are correlated, possible scenarios are: • XY • XY • XUY<sup>To distinguish, need</sup> controlled random experiment

- Is risk factor X causing disease Y (or a consequence)? – E.g. alcohol addiction, smoking, blood cholesterol, fever, stress  Randomized experiment, with and without X: feasibility? ethics?

- **G**  **randomized experiment** (e.g. random Mendelian inheritance), as only some subjects have genotype

- G ( **i.v.** )must be correlated with Y **_but only through X_** i.e. if X known, G gives no additional information about Y

68

## In silico thought experiment

###### **p=3.847832e−05**

###### **p=2.946466e−35**


<!-- Start of picture text -->
CC<br>Small but significant<br>effect due to Alz<br>CA<br>Same effect due to Alz,<br>but with larger effect due<br>to genotype. AD<br>AD<br>nonAD<br>nonAD<br>0 200 400 600 800<br>0 200 400 600 800<br>Subjects<br>Subjects<br>© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Hemi-methylation associated with meQTL<br>yields a p-value that’s 30 orders of<br>magnitude lower for the AD phenotype.<br>1.0 1.0<br>0.8 0.8<br>0.6n n 0.6<br>oi oi<br>at at<br>yl yl<br>h h<br>et et<br>M M<br>0.4 0.4<br>0.2 0.2<br>0.0 0.0<br><!-- End of picture text -->

69

## Mendelian randomization approach

**Account for variance due to genotype, how much does methylation add?**


<!-- Start of picture text -->
With variability<br>due to<br>genotype and<br>environmental<br>covariates<br>removed, the<br>effect due to<br>E + G + M = P VS E + G = P phenotype<br>should become<br>more<br>prevalent.<br>From G, include probe-specific<br>terms for cis-meQTLs, as well as<br>including trans-meQTLs in all<br>comparisons.<br><!-- End of picture text -->

70

---

[← eWAS](08-ewas.md) · [Up: contents](index.md) · [Causality testing →](10-causality-testing.md)
