---
title: Introduction
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/20-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

MIT 6.047/6.878/HST.507 - Computational Biology: Genomes, Networks, Evolution

**Lecture 20** Personal genomics, disease epigenomics, systems approaches to disease Predictive Medicine Molecular Epidemiology Mendelian Randomization Polygenic Risk Prediction Models

1

## Personal genomics today: 23 and We **Recombination breakpoints**

**Dad’s mom**

**Me vs. my brother**

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


**My dad**


**Mom’s dad**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

**Systems: genes**  **combinations**  **pathways**

**Genomics: Regions**  **mechanisms**  **drugs**

2

### **Goal: Personalized and Predictive Medicine**

<mark>1. Intro to Epidemiology: basis of human disease</mark>

2. Genetic Epidemiology:

   - Genetic basis: GWAS and screening

   - Interpreting GWAS with functional genomics

- Calculating functional enrichments for GWAS loci

- 3. Molecular epidemiology

   - meQTLs: Genotype-Epigenome association (cis-/trans-)

- EWAS: Epigenome-Disease association

- 4. Resolving Causality

   - Statistical: Mendelian Randomization

- Application to genotype + methylation in AD

- 5. Systems Genomics and Epigenomics of disease – Beyond single loci: polygenic risk prediction models

   - Sub-threshold loci and somatic heterogeneity in cancer

3


<!-- Start of picture text -->
C E<br>confounders environment<br>syndrome<br>causes<br>G X D S<br>epigenome disease symptoms<br>genome<br>biomarkers<br>effects<br><!-- End of picture text -->

Epidemiology The study of the

**patterns** , **causes** , and **effects** of health and disease conditions in defined populations

4

### **Epidemiology: Definitions and terms**

- **Morbidity** level: how sick an individual is

- **Incidence** : # of **_new_** cases / # people / time period

- • **Prevalence** : Total # of cases in population • **Attributable risk** : rate in exposed vs. not exposed • **Population burden** : yrs of potential life lost (YPLL), quality-/disability-adjusted life year (QALY/DALY)

- • **Syndrome:** Co-occurring signs (observed), symptomes (reported), and other phenomena; (often hard to establish causality / risk factors)

- **Prevention challenge:** Determine disease, cause, understand whether, when, and how to intervene

5

## **Determining disease causes: study design**

- **Principles of experimental design**

   - **Control** : comparison to baseline, placebo effect

   - **Randomization** : Difficult to achieve, ensure mixing

   - **Replication** : control variability in initial sample

   - **Grouping** : understand variation between subgroups

   - **Orthogonality** : all combinations of factors/treatments

   - **Combinatorics** : factorial design _n_ x _n_ x _n_ x < x _n_ table

- **Challenge of human subjects**

   - Legal and ethical constraints, Review boards

   - Randomization by instrumental variables

   - Clinical trials: blind (patient), double-blind (doctor too)

6

### **Goal: Personalized and Predictive Medicine**

1. Intro to Epidemiology: basis of human disease

2. Genetic Epidemiology:

– Genetic basis: GWAS and screening

– Interpreting GWAS with functional genomics

– Calculating functional enrichments for GWAS loci

3. Molecular epidemiology

– meQTLs: Genotype-Epigenome association (cis-/trans-)

– EWAS: Epigenome-Disease association

4. Resolving Causality

– Statistical: Mendelian Randomization

- Application to genotype + methylation in AD

5. Systems Genomics and Epigenomics of disease

– Beyond single loci: polygenic risk prediction models

– Sub-threshold loci and somatic heterogeneity in cancer

7


<!-- Start of picture text -->
C E<br>confounders environment<br>causes<br>G X D S<br>epigenome disease symptoms<br>genome<br>biomarkers<br>effects<br>Genetic Epidemiology<br><!-- End of picture text -->

Genetic factors contributing to disease

8

## **Genome-wide association studies (GWAS)**


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Mccarthy, M. I., Abecasis, G. R., Cardon, L. R., Goldstein, D. B., Little, J., Ioannidis, J. P., & Hirschhorn, J. N. (2008). "Genome-wide association studies for complex traits: Consensus, uncertainty and challenges." Nat Rev Genet Nature Reviews Genetics, 9(5), 356-369.

- Identify regions that co-vary with the disease

- Risk allele G more frequent in patients, A in controls

- But: large regions co-inherited  find causal variant

- Genetics does not specify cell type or process

9

### **All disease-associated genotypes from GWAS**


Courtesy of Burdett T (EBI), Hall PN (NHGRI), Hastings E (EBI), Hindorff LA (NHGRI), Junkins HA (NHGRI),

- Klemm AK (NHGRI), MacArthur J (EBI), Manolio TA (NHGRI), Morales J (EBI), Parkinson H (EBI) and Welter D (EBI).The NHGRI-EBI Catalog of published genome-wide association studies. Available at: www.ebi.ac.uk/gwas. Used with Permission. • **1000s of studies, each with 1000s of individuals** – Increasing power, meta-analyses reveal additional loci – More loci expected, only fraction of heritability explained

10

### **More loci on the way: GWAS growth continues**


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

• When to design custom chip: continuously update • http://www.genome.gov/admin/gwascatalog.txt

11

### **Decreasing cost of whole-genome sequencing**


Image by Wetterstrand KA. DNA Sequencing Costs: Data from the NHGRI Genome Sequencing Program (GSP) Available at: www.genome.gov/sequencingcosts. Image in the public domain.

- Simply genotype all known variants at >0.1% freq

• Or: sequence complete diploid genome of everyone

12

## **Genetic epidemiology: What to test**

- **Family risk alleles** , inherited with common trait

   - Specific genes, specific variants, family history

- Monogenic, **actionable** , protein-coding mutations – Most understood, highest impact, easiest to interpret

- **All coding** SNPs with known disease association – What if not druggable / treatable? Want/need know?

- • **All** coding/non-coding **associations** from GWAS – Thousands of significant associations (1350 on 6/2012)

- • **All common** SNPs, regardless of association – HapMap and 1000 Genomes capture common variants

- **Genome** : all SNPs, CNVs, rare/private mutations

13

## **Predictive medicine: When to screen**

- **Diagnostic testing:** after symptoms, confirm a hypothesis, distinguish between possibilities

- **Predictive risk:** before symptoms even manifest

- **Newborn** : heel pick, store, for early treatment

- • **Pre-natal testing:** ulstrasound, maternal serum vs. n eedles, probes, chorionic villus sampling

- **Pre-conception testing:** common/rare disorders

- **Carrier testing** : specific mutation in family history

- **Genetics vs. biomarkers :** cause vs. consequence?

14

### **Goal: Personalized and Predictive Medicine**

1. Intro to Epidemiology: basis of human disease 2. Genetic Epidemiology: – Genetic basis: GWAS and screening

– Interpreting GWAS with functional genomics – Calculating functional enrichments for GWAS loci 3. Molecular epidemiology

– meQTLs: Genotype-Epigenome association (cis-/trans-) – EWAS: Epigenome-Disease association 4. Resolving Causality

– Statistical: Mendelian Randomization – Application to genotype + methylation in AD 5. Systems Genomics and Epigenomics of disease – Beyond single loci: polygenic risk prediction models – Sub-threshold loci and somatic heterogeneity in cancer

15

**Interpreting disease associations** Functional genomics of GWAS

16

### **Interpreting disease-association signals**

**(1) Interpret variants using Epigenomics**

   - **Chromatin states: Enhancers, promoters, motifs**

- **Enrichment in individual loci, across 1000s of SNPs in T1D**


**CATGACTG CATGCCTG GWAS G enotype Disease**

> **mQTLs Epigenome MWAS (2) Epigenome changes in disease**

- Intermediate molecular phenotypes associated with disease

   - Variation in brain methylomes of Alzheimer’s patients

17

##### **Complex disease: strong non-coding component**

**Monogenic / Mendelian Disease**

**Polygenic / Complex Disease**

**Coding Non-coding**

**Human Genetic Mutation Database April 2010 release**

**Catalog of GWAS studies Hindorff et al. PNAS 2009**

Slide credit: Benjamin Raby

18

##### **Genomic medicine: challenge and promises**

GWAS: simple χ<sup>2</sup> statistical test

1. The promise of genetics

   - Disease mechanism

   - New target genes

   - New therapeutics

   - Personalized medicine


2. The challenge

   - **90+% disease hits non-coding**

   - Cell type of action not known

   - Causal variant not known

Courtesy of Macmillan Publishers Limited. Used with permission Source: Hillmer, A. M., Brockschmidt, F. F., Hanneken, S., Eigelshoven, S., Steffens, M., Flaquer, A., . . . Nöthen, M. M. (2008). "Susceptibility variants for male-pattern baldness on chromosome 20p11." Nature Genetics Nat Genet, 40(11), 1279-1281. doi:10.1038/ng.228

- Mechanism not known

Hillmer Nature Genetics 2008

19

##### **Genomic medicine: challenge and promises**


Courtesy of NIH Roadmap Epigenomics Mapping Consortium. Used with permission.

3. The remedy

- Annotation of non-coding genome (ENCODE/Roadmap)

- Linking of enhancers to r egulators and target genes

- New methods for utilizing them

###### Roadmap Epigenomics, Nature 2015


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Ernst, J. et al. (2011). Mapping and analysis of chromatin state dynamics in nine human cell types. Nature, 473(7345), 43-49.

4. The deliverables

   - Relevant cell type

   - Target genes

   - Causal variant

   - Upstream regulator

   - Relevant pathways

   - Intermediate phenotypes

Ernst, Nature 2011

20

###### **_This talk: From loci to mechanisms_**

###### **_Building a reference map of the regulatory genome_**

###### **Enhancers**

**Promoters Transcribed**

**Repressed**


**Regions** : Enhancers, promoters, transcribed, repressed **Cell types** : Predict tissues and cell types of epigenomic activity **Target genes** : Link variants to their target genes using eQTLs, activity, Hi-C **Nucleotides** : Regulatory consequence of mutation: Conservation, PWMs **Regulators** : Upstream regulators whose activity is disrupted by mutation

###### **_Application to GWAS, hidden heritability, and Cancer_**

- **GWAS CATGCCTG** • 93% top hits non-coding  Mechanism? Cell type? **hits CGTGTCTA** • Lie in haplotype blocks  Causal variant(s)?

**‘Hidden’ CATGCCTG heritability CGTGTCTA Cancer CATGCCTG mutations CATCCCTG**

- Many variants, small effects  Pathway-level burden/load • Many false positives  Prioritize w/ regulatory annotations • Loss of function  Protein-coding variants, convergence • Gain of function  Regulatory variants, heterogeneity

21

##### **Dissecting non-coding genetic associations**


<!-- Start of picture text -->
4. Upstream regulator(s)<br>TF<br>TF TF<br>2. Target gene(s)<br>1. Tissue/cell type(s)<br>GWAS region<br>SNPs<br>3. Causal nucleotide(s) 5. Cellular phenotypes 6. Organismal phenotypes<br><!-- End of picture text -->

1. Establish relevant **tissue/cell type**

2. Establish downstream **target** gene(s)

3. Establishing **causal** nucleotide variant

4. Establish upstream **regulator** causality

5. Establish **cellular** phenotypic consequences

6. Establish **organismal** phenotypic consequences

22

---

[Up: contents](index.md) · [Using epigenomic maps to predict disease-relevant tissues →](02-using-epigenomic-maps-to-predict-disease-relevant-tissues.md)
