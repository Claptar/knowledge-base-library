---
title: Analysis of Genome Wide AssociaBon Studies (GWAS) Lecture 20
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/20-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Analysis of Genome Wide AssociaBon Studies (GWAS) Lecture 20

**Source:** `lectures/20-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##### <u>David K. Gifford</u>

MassachuseQs InsOtute of Technology


1

Computa(onal   Analysis   of   QTLs

#### **Today’s NarraBve Arc**

1. We can discover human variants that are associated with a phenotype by studying the genotypes of case and control populaOons

   - **Approach 1 – Use allelic counts from SNP arrays (SNPs   called from microarray data)**

   - Approach 2 – Use read counts from sequencing (mulOple reads per variant per individual)

2. We can prioriOze variants based upon their esOmated importance

3. Follow up confirmaOon is important because correlaOon is not equivalent to causality

2

Computa(onal   Analysis   of   QTLs

#### **Today’s ComputaBonal Approaches**

1. ConOngency tables for allelic associaOon tests and genotypic associaOon tests.

2. Methods of tesOng -­‐ Chi-­‐Square tests, Fisher’s   exact test

3. Likelihood based tests of case/control posterior genotypes

Computa(onal   Analysis   of   QTLs

3

#### **Out of   scope   for   today**

1. Non-­‐random   genotyping failure

2. Methods to correct for populaOon straOficaOon

3. Structural variants (SVs) and copy number variaOons (CNVs)

Computa(onal   Analysis   of   QTLs

4

Mendelian traits are caused by a single gene

Courtesy of David Altshuler. Used with permission.

Slide courtesy of David Altshuler, HMS/Broad

AnimaOon: Itsik Pe’er, Columbia ComputaOonal   Analysis   of   QTLs


Computa(onal   Analysis   of   QTLs

Disease cases Healthy control


<!-- Start of picture text -->
6<br><!-- End of picture text -->


7


Computa(onal   Analysis   of   QTLs **Disease cases Healthy controls**

Computa(onal   Analysis   of   QTLs

8

---

[Up: contents](index.md) · [Age-­‐related macular degeneraOon →](02-age--related-macular-degeneraoon.md)
