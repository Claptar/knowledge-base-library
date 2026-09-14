---
title: Age-­‐related macular degeneraOon
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Age-­‐related macular degeneraOon

**Source:** `lectures/20-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Cohort – 2172 unrelated European descent individuals at least 60 years old

2004: LiQle known about cause of AMD

**934 controls**


**1238 cases**


Photographs are in the public domain.

Computa(onal   Analysis   of   QTLs

9

SNP rs1061170 1238 individuals with AMD and 934 controls 2172 individuals / 4333 alleles


X<sup>2</sup> = 279 Df = (2 rows-­‐1)x(2 columns-­‐1) = 1

P-­‐value = 1.2 x 10<sup>-­‐62</sup>

Computa(onal   Analysis   of   QTLs

10

##### ConOngency Tables – χ<sup>2</sup> test


<!-- Start of picture text -->
2<br>n<br>( a + b )( a + c ) ( O i − E i )<br>E 1 =<br>X 2 = ∑<br>( a + b + c + d ) i =1 Ei<br><!-- End of picture text -->

###### Df = (2 rows-­‐1)x(2 columns-­‐1) = 1

Computa(onal   Analysis   of   QTLs

11

##### ConOngency Tables – Fisher’s   Exact Test


<!-- Start of picture text -->
! $! $<br>a + b c + d<br>a c<br>##" &&%##" &&%<br>p =<br>! $<br>a + b + c + d<br>a + c<br>##" &&%<br><!-- End of picture text -->

Sum all probabiliOes for observed and all more extreme values with same marginal totals to compute probability of null hypothesis

Computa(onal   Analysis   of   QTLs

12

##### Does the affected or control group exhibit PopulaOon StraOficaOon?

- PopulaOon straOficaOon is when subpopulaOons exhibit allelic variaOon because of ancestry

- Can cause false posiOves in an associaOon study if there are SNP   differences in the case and control populaOon structures

- Control for this arOfact by tesOng control SNPs   for general elevaOon in χ<sup>2</sup> distribuOon between cases and controls

Computa(onal   Analysis   of   QTLs

13

Age-­‐related macular degeneraOo 2004: LiQle known about cause of AMD


2006: Three genes (5 common variants)

###### Together explain >50% of risk


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Maller, Julian, Sarah George, et al. "Common Variation in Three Genes, Including a Noncoding Variant in CFH, Strongly Influences Risk of Age-related Macular Degeneration." _Nature Genetics_ 38, no. 9 (2006): 1055-9.

Photographs are in the public domain.

RelaOve risk ploQed as a funcOon of the geneOc load of the five variants that influence risk of AMD. Two variants are in the CFH gene on chromosome 1: Y402H and rs1410996. Another common variant (A69S) is in hypotheOcal gene LOC387715 on chromosome 10. Two relaOvely rare variants are observed in the C2 and BF genes on chromosome 6. We find no evidence for interacOon between any of these variants, suggesOng an independent mode of acOon.

Edwards et al, Klein   et al, Haines et al _<u>Science</u>_ (2005); JakobsdoRr et al, _<u>AJHG</u>_ (2005); Gold et al _<u>Nature Gene-cs</u>_ (2006), Maller, George, Purcell,   Fagerness,   Altshuler, Daly, Seddon,   Nature GeneOcs (2006)

14

###### Computa(onal   Analysis   of   QTLs


- Courtesy of Macmillan Publishers Limited. Used with permission.

Source: Burton, Paul R., David G. Clayton, et al. "Genome-wide Association Study of 14,000 Cases of

Seven Common Diseases and 3,000 Shared Controls." _Nature_ 447, no. 7145 (2007): 661-78.

Nature   Vol 447|7 June 2007| doi:10.1038/nature05911

Computa(onal   Analysis   of   QTLs

15

##### Linkage Disequilibrium (LD) between two loci L1 and L2 in gametes

At locus L1

pA probability L1 is A qa probability L1 is a At locus L2

pB probability L2 is B qb probability L2 is b


D = Measure of linkage disequilibrium = 0 when L1 and L2 are in equilibrium

D=PABPab -­‐ PAbPaB

r<sup>2</sup> = D<sup>2</sup> / (pAqapBqb)

r is [0,1]   and is the correlaOon coefficient between allelic states in L1 and L2

Computa(onal   Analysis   of   QTLs

16

## r<sup>2</sup> from human chromosome 22


Computa(onal   Analysis   of   QTLs

17

##### LD organizes the genome into haplotype blocks


Human genome 5q31 region (associated with Inflammatory Bowel Disease)

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

18

##### The length of haplotype blocks vs Ome


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

20

#### **Variant Phasing**

1. Phasing assigns alleles to their parental chromosome

2. Set of ordered alleles along a chromosome is a haplotype

3. Known   haplotypes can assist with phasing

4. Phasing is criOcal for understanding the funcOonal status of genes with more than one important SNPs   (are the non-­‐ reference alleles on different chromosome? If so, the gene may not be funcOonal)

5. New   long read sequencing technologies phase variants in observed reads

Computa(onal   Analysis   of   QTLs

21

#### **Today’s NarraBve Arc**

1. We can discover human variants that are associated with a phenotype by studying the genotypes of case and control populaOons

   - Approach 1 – Use allelic counts from SNP   arrays (SNPs   called from microarray data)

   - **Approach 2 – Use read counts from sequencing (mulBple   reads per variant   per   individual)**

2. We can prioriOze variants based upon their esOmated importance

3. Follow up confirmaOon is important because correlaOon is not equivalent to causality

Computa(onal   Analysis   of   QTLs

22

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

23


<!-- Start of picture text -->
23<br><!-- End of picture text -->

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

24 Computa(onal   Analysis   of   QTLs


<!-- Start of picture text -->
24<br><!-- End of picture text -->

Computa(onal   Analysis   of   QTLs

25

© source unknown. All rights reserved. This content is excluded from our Creative 25 Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

26

© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

27

##### Genome Analysis Tool Kit (GATK)

Courtesy of the Broad Institute. Used with permission. The most recent best practices can be found at this website: https://www.broadinstitute.org/gatk/guide/best-practices.

Computa(onal   Analysis   of   QTLs

28

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

29


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

30

Courtesy of the Broad Institute. Used with permission. The most recent best practices can be found at this website: https://www.broadinstitute.org/gatk/guide/best-practices.

Computa(onal   Analysis   of   QTLs

31

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

32


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

33


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

ComputaOona Analysi o QTLs

34

#### CompuOng genotypes


<!-- Start of picture text -->
1 = P ( G )<br>∑<br>G ∈{ AA , AC ,..., TT }<br><!-- End of picture text -->

Given the reads we observe we wish to compute P(Gp) at a SNP for a populaOon p (p could be cases or controls)

Computa(onal   Analysis   of   QTLs

35

#### Joint esOmaOon of genotype frequencies


Computa(onal   Analysis   of   QTLs

36

Compute Bayesian posterior genotype frequencies (G) for each individual from their reads (D)

_G=H1,H2_

Computa(onal   Analysis   of   QTLs

37

#### Haploid likelihood considers the probability of errors

<mark>[</mark> _<mark>D</mark> j_ <mark>is a single read]</mark>

Computa(onal   Analysis   of   QTLs

38

#### Joint esOmaOon of genotype frequencies


Computa(onal   Analysis   of   QTLs

39

#### EM can be used to improve the esOmate of P(Gp)


<!-- Start of picture text -->
t<br>1 n ) ( )<br>P ( Di | Gp ) P ( Gp<br>P ( G ) ( t +1)<br>p ∑ ' ' ' t<br>= n ( )<br>i =1 ∑ P ( D i | Gp ) P ( Gp )<br>'<br>Gp<br><!-- End of picture text -->

Computa(onal   Analysis   of   QTLs

40

#### TesOng for associaOons

Assume a reference allele (A) and a single non-­‐reference allele (a)

ψ = _P_ ( _A_ ) (1−ψ) = _P_ ( _a_ ) ε0 = _P_ ( _AA_ ) ε1 = _P_ ( _Aa_ ) ε2 = _P_ ( _aa_ )

Computa(onal   Analysis   of   QTLs

41

TesOng for Hardy Weinberg Equilibrium (HWE) When a populaOon is in HWE we can compute genotypic frequencies from allelic frequencies We can test for HWE as follows –


<!-- Start of picture text -->
P ( D |ε0,ε1,ε2 )<br>T 3 = 2log<br>P ( D | (1−ψ) 2 ,2ψ(1−ψ),ψ 2 )<br><!-- End of picture text -->

Computa(onal   Analysis   of   QTLs

42

#### TesOng for associaOons


[1] and [2] are cases and controls. Do not use T2 when populaOon is in HWE as it will be underpowered (too many DOF)

[1] [1] [2] [2] [2]) _P_ <u>(</u> _D_<sup>[1]</sup> <u>|ε0</u> ,ε1 ,ε2[1]) _P_ <u>(</u> _D_ [2] <u>|ε0</u> ,ε1 ,ε2 _T_ 2 = 2log _P_ ( _D_ |ε0,ε1,ε2 )

43 Computa(onal   Analysis   of   QTLs


Computa(onal   Analysis   of   QTLs

44

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Computa(onal   Analysis   of   QTLs

45


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

46 Computa(onal   Analysis   of   QTLs


Computa(onal   Analysis   of   QTLs

47

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

48 Computa(onal   Analysis   of   QTLs


49 Computa(onal   Analysis   of   QTLs


Computa(onal   Analysis   of   QTLs

50

#### **Today’s NarraBve Arc**

1. We can discover human variants that are associated with a phenotype by studying the genotypes of case and control populaOons

   - Approach 1 – Use allelic counts from SNP   arrays (SNPs   called from microarray data)

   - Approach 2 – Use read counts from sequencing (mulOple reads per variant per individual)

**2. We can prioriBze   variants   based upon their   esBmated importance**

3. Follow up confirmaOon is important because correlaOon is not equivalent to causality

Computa(onal   Analysis   of   QTLs

51


© Macmillan Publishers Limited. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Weedon, Michael N., Inês Cebola, et al. "Recessive Mutations in a Distal PTF1A

Enhancer Cause Isolated Pancreatic Agenesis." _Nature Genetics_ (2013).

Computa(onal   Analysis   of   QTLs

52

##### IdenOficaOon of possible funcOonal variants

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Weedon, Michael N., Inês Cebola, et al. "Recessive Mutations in a Distal PTF1A Enhancer

Cause Isolated Pancreatic Agenesis." _Nature Genetics_ (2013).

Computa(onal   Analysis   of   QTLs

53

##### AssociaOon of variants with pedigrees

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Weedon, Michael N., Inês Cebola, et al. "Recessive Mutations in a Distal PTF1A Enhancer

Cause Isolated Pancreatic Agenesis." _Nature Genetics_ (2013).

Computa(onal   Analysis   of   QTLs

54

#### **Today’s NarraBve Arc**

1. We can discover human variants that are associated with a phenotype by studying the genotypes of case and control populaOons

   - Approach 1 – Use allelic counts from SNP   arrays (SNPs   called from microarray data)

   - Approach 2 – Use read counts from sequencing (mulOple reads per variant per individual)

2. We can prioriOze variants based upon their esOmated importance

**3. Follow up confirmaBon is important because correlaBon is not equivalent   to causality**

Computa(onal   Analysis   of   QTLs

55

##### ConfirmaOon of variant funcOon

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Weedon, Michael N., Inês Cebola, et al. "Recessive Mutations in a Distal PTF1A Enhancer Cause Isolated Pancreatic Agenesis." _Nature Genetics_ (2013).

Computa(onal   Analysis   of   QTLs

56


© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Roberts, Nicholas J., Joshua T. Vogelstein, et al. "The Predictive Capacity of Personal Genome Sequencing." _Science Translational Medicine_ 4, no. 133 (2012): 133ra58.


Computa(onal   Analysis   of   QTLs

57


- © American Association for the Advancement of Science. All rights reserved. This content is excluded

- from our Creative Commons license. For more information, see<sup>http://ocw.mit.edu/help/faq-fair-use/.</sup> Source: Roberts, Nicholas J., Joshua T. Vogelstein, et al. "The Predictive Capacity of Personal Genome Sequencing." _Science Translational Medicine_ 4, no. 133 (2012): 133ra58.


Computa(onal   Analysis   of   QTLs

58

# **FIN**

59 Computa(onal   Analysis   of   QTLs


MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Analysis of Genome Wide AssociaBon Studies (GWAS) Lecture 20](01-analysis-of-genome-wide-associabon-studies-gwas-lecture-20.md) · [Up: contents](index.md)
