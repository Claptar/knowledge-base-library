---
title: P3 – Heritability (5 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/05-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# P3 – Heritability (5 points)

## (A) (3 points)
For 3A, many students simply copied from the lecture slides, which was accepted, but students should understand how to calculate these quantitites.

(i) Suppose there is a single locus in a haploid organism controlling a trait with a positive allele for which the phenotype is 1 and a neutral allele for which the phenotype is 0. Calculate $V_G$ for this trait in an infinite population of $F_1$ children from these two parents.

$$V_G = 0.5(1 - 0.5)^2 + 0.5(0 - 0.5)^2 = 0.25$$

(ii) Now, suppose there are three unlinked loci each with a positive allele contributing $\frac{1}{3}$ to the phenotype and neutral allele contributing 0 to the phenotype. Calculate $V_G$.

$$\mu_G = \frac{1}{8} \cdot 0 + \frac{3}{8} \cdot \frac{1}{3} + \frac{3}{8} \cdot \frac{2}{3} + \frac{1}{8} \cdot 1 = \frac{1}{2}$$

$$V_G = \left(\frac{1}{8}\right)\left(0 - \frac{1}{2}\right)^2 + \left(\frac{3}{8}\right)\left(\frac{1}{3} - \frac{1}{2}\right)^2 + \left(\frac{3}{8}\right)\left(\frac{2}{3} - \frac{1}{2}\right)^2 + \left(\frac{1}{8}\right)\left(1 - \frac{1}{2}\right)^2 = \frac{1}{12}$$

(iii) Generalize the previous results to calculate $V_G$ for $N$ unlinked loci contributing 0 or $\frac{1}{N}$ to the phenotype.
The variance for a single allele, which has 50% chance of contributing value 0 and 50% chance of contributing value 1, is (considering it as an independent Bernoulli trial):

$$\frac{1}{2}\left(0 - \frac{1}{2N}\right)^2 + \frac{1}{2}\left(\frac{1}{N} - \frac{1}{2N}\right)^2 = \frac{1}{(2N)^2}$$

Since the alleles are independent, we can add the variances for the $N$ alleles to get:

$$V_G = \frac{1}{4N}$$

How many possible values are there for the phenotype?
N+1 – the phenotype can take on the values 0 and all multiples of 1/N up to/including 1

**(B) (1 point)** You perform linear regression to predict a phenotypic trait ($y$) on a set of binary genotypic variables ($x_1, x_2, \dots, x_N$) for a model system. Show how the $R^2$ that results relates to the narrow sense heritability of the trait.
$R^2$ is equal to $h^2$ (narrow sense heritability). $R^2$ in a linear regression is defined as the regression sum of squares divided by the total sum of squares (sample variance).

In the case where the predictors are genotypic components, this regression is the same as the additive model covered in class. The numerator is therefore $\sigma_a^2$ and the denominator is $\sigma_p^2$, giving the same equation as narrow sense heritability.

**(C) (1 point)** Assume that all of the genetic components from part (a) are additive. Give the environmental contribution to the observed phenotype variance assuming that the covariance between the genetic and environmental components is zero.
$1 - R^2$

We were looking for a quantity relating to $R^2$, which wasn’t made clear in the instructions. Many students used the $\sigma_p^2 = \sigma_e^2 + \sigma_g^2$ formula and used the $1/4N$ term for the genotypic variance, which was accepted. We were looking for a ratio of the environmental contribution.

$$\frac{\sigma_e^2}{\sigma_p^2} = \frac{\sigma_p^2 - \sigma_a^2}{\sigma_p^2} = 1 - \frac{\sigma_a^2}{\sigma_p^2} = 1 - h^2 = 1 - R^2$$

---

[← P2 – Analysis of Chromatin Structure (5 points)](02-p2-analysis-of-chromatin-structure-5-points.md) · [Up: contents](index.md) · [P4 – Association Studies (5 points) →](04-p4-association-studies-5-points.md)
