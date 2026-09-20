---
title: 4-30 Recitation
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-30-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-04-30-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4-30 Recitation

DG Lectures 19 & 20
QTLs & Human Genetics

---

## Announcements

- Pset 5 due this Thursday (5-1)
- Exam 2 next Tuesday (5-6)
  - 2 double-sided sheets of notes
- Office Hours next Monday instead of Tuesday
- No recitations or regular OHs after exam
- Project Presentations May 13 and 15 – all students will peer review

---

## Outline

- Quantitative Trait Loci
  - Simple genetic model (haploid, unlinked)
  - Genotype-phenotype interactions
    - Broad-sense and narrow-sense heritability, sources of variance
  - LOD scores
  - Bloom *et al.* 2013 & missing sources of heritability
- Human Genetics
  - Testing for SNP/phenotype associations
  - Linkage Disequilibrium
  - Variant Phasing
  - Hardy-Weinberg Equilibrium

---

## Genotype to Phenotype

- Phenotype: organisms observable characteristics or traits
  - Qualitative: dead/alive, tall/short
  - Quantitative: Growth rate, height, gene expression
- Quantitative Trait locus (loci) – a marker that is associated with a quantitative trait
  - eQTL (expression quantitative trait locus) – marker associated with gene expression
  - eQTLs are often SNPs (single nucleotide polymorphisms) in the population
    - Can be in *cis* (within ~Kbs on the same chromosome) or in *trans* (1+Mb away or on different chromosome)
    - Often cell-type specific

---

## Haploid, unlinked genetic model

- $N$ loci that each contribute equally ($1/N$) to the trait
- Haploid = organism has 1 copy of each allele
- Unlinked = loci are on different chromosomes or far enough apart on the same chromosome so crossing over (recombination) can always occur
  - Each locus is therefore inherited independently
- Child randomly inherits maternal or paternal copy

Effect Size:
- White loci: $0, 0, \dots, 0$
- Black loci: $1/N, 1/N, \dots, 1/N$

Binomial model of # of black alleles $x$ inherited:

$$p(x, N) = \binom{N}{x} (1 - .5)^{N-x} .5^x$$

Here $x$ is the phenotypic value from 0 (no alleles) to 1 (all black alleles):

$$E[x] = .5$$

$$\sigma_x^2 = .25 / N$$

---

## Situation is more complex if loci are linked

Genetic linkage causes marker correlation

Proximal genomic locations makes crossing over unlikely during meiosis

- Assumption that each allele is inherited independently no longer holds – models more complex than binomial needed to capture this dependence

---

## Genotype – Phenotype interactions

- $i$ – individual in $[1 \dots N]$
- $g_i$ – genotype of individual $i$
- $p_i$ – quantitative phenotype of individual $i$ (single trait)
- $e_i$ – environmental contribution to $p_i$

$$p_i = f(g_i) + e_i$$
Phenotype is a function of genotype plus an environmental component

$$E[e_i] = 0 \quad E[e^2] = \sigma_e^2$$
Environmental component is unbiased but introduces noise from genotype to phenotype

$$\sigma_p^2 = \sigma_g^2 + \sigma_e^2 + 2\sigma_{ge}^2 \quad \rightarrow \quad \sigma_p^2 = \sigma_g^2 + \sigma_e^2$$

Assume environment affects all genotypes equally -> $g$ and $e$ are independent and their covariance is 0

---

## All phenotypic variation

- **All phenotypic variation**
  - Environmental variation
  - Heritable genetic variation (Broad-sense heritability $H^2$)
    - Additive genetic variation (Narrow-sense heritability $h^2$)
    - Non-additive genetic variation
      - Dominance effects
      - Gene-gene interactions
      - Gene-environment interactions

---

## 2 types of heritability

- Broad-sense ($H^2$) and narrow-sense ($h^2$)
- Broad-sense
  - Fraction of phenotypic variance explained by genetic components
    $$H^2 = \frac{\sigma_g^2}{\sigma_p^2} = \frac{\sigma_p^2 - \sigma_e^2}{\sigma_p^2}$$
    ($\sigma_p^2 - \sigma_e^2$: Can be estimated from identical twins or clones; $\sigma_p^2$: Can be observed from all individuals in population)
  - The upper bound for phenotypic prediction by optimal arbitrary (not necessarily linear) model
- Narrow-sense
  - The upper bound for phenotypic prediction by *linear* model (= fraction of total phenotypic variance that is caused by the additive effects of genes)
  - Determines the resemblance of offspring to their parents and the population's evolutionary response to selection

---

## Narrow-sense heritability ($h^2$) is the regression (slope) of offspring on parents

- $h^2 \approx 0$
- $h^2 \approx \frac{1}{2}$
- $h^2 \approx 1$

- Regression slope is: $\text{Cov}(x,y)/\text{Variance}(x)$ or $\text{Cov}(\text{parents}, \text{offspring})/\text{Variance}(\text{parents})$
  - $x$ is the "mid-parent"
- The higher the slope, the better the offspring resemble their parents.
- In other words, the higher the heritability, the better the offspring trait values are predicted by parental trait values.

---

## Narrow-sense heritability: additive model of phenotype

- $g_{i,j}$ is a binary $\{0,1\}$ variable of QTL $j$ in individual $i$
- Each QTL in the genotype contributes independently & linearly to the phenotype:

$$f_a(g_i) = \sum_{j \in \text{QTL}} \beta_j g_{ij} + \beta_0$$

- $\beta_j$ is the effect of QTL $j$ on the phenotype (higher -> QTL has greater impact)
- For additive markers, children are expected to be the midpoint of their parents since they get an average of $\frac{1}{2}$ loci from each parent:

$$E[f_a(g_i)] = \frac{f_a(p_1)}{2} + \frac{f_a(p_2)}{2}$$

---

## Narrow-sense heritability: additive model of phenotype

$$f_a(g_i) = \sum_{j \in \text{QTL}} \beta_j g_{ij} + \beta_0$$

$$p_i = f_a(g_i) + e_i$$

$$\sigma_a^2 = \sigma_p^2 - \frac{1}{N} \sum_{i=1}^N (p_i - f_a(g_i))^2$$

- $\sigma_a^2$: Additive genetic variance
- $\sigma_p^2$: Total phenotypic variance
- $\frac{1}{N} \sum_{i=1}^N (p_i - f_a(g_i))^2$: Variance that remains after linear model – one source of "missing" heritability in studies

Narrow-sense heritability:

$$h^2 = \frac{\sigma_a^2}{\sigma_p^2}$$

---

## Using LOD scores to discover QTLs for a trait (e.g. gene expression)

$$LOD = \log_{10} \prod_{i=1}^N \frac{P(p_i \mid g_{ij}, \mu_0, \mu_1, \sigma)}{P(p_i \mid \mu, \sigma)}$$

LOD = Logarithm of the ODds
$i$ = individual

"Null" model: locus does not affect gene's expression, and the probability of expression value $p_i$ simply follows a $\text{Normal}(\mu, \sigma^2)$ distribution

"Alternative" model: locus affects a gene's expression (is a QTL), and there are different mean expression values $\mu_0$ and $\mu_1$ depending on which genotype is present at the locus (if $g_{ij}=0$ or $1$)

- If the alternative model (that the locus is a QTL for the gene) doesn't explain the expression values any better than the null model, the probability ratios are 1 and the LOD score is 0
  - If alternative model better explains the data, LOD score > 0
- If the locus is a QTL, the LOD score will get higher with increasing number of individuals ($N$) – with larger sample samples we have greater power to detect loci as being statistically significant QTLs. This is referred to as "power" – a study with too few people to determine statistical significance at some loci is "underpowered".

---

## Using LOD scores to discover QTLs for a trait (e.g. gene expression)

$$LOD = \log_{10} \prod_{i=1}^N \frac{P(p_i \mid g_{ij}, \mu_0, \mu_1, \sigma)}{P(p_i \mid \mu, \sigma)}$$

- How to determine if a LOD score is significant?
  - Permute genotypes (so the marker $g_{ij}$ and expression values are mixed up) 1000 times and compute LOD scores to get empirical null distribution
  - Determine the null LOD score that corresponds to FDR = 0.05
  - Use this threshold on unpermuted LOD scores to find QTLs for each gene
  - Since all loci are included in the permuted null distribution, no multiple hypothesis correction needed

- Fit a linear model to discovered QTLs to determine each QTL's contribution ($\beta_j$)

- Once this has been done to find the set of statistically significant QTLs from the first pass, you can repeat to find QTLs in the residuals from the existing model that may have been below the threshold in the first pass (3 times)

---

## Bloom *et al.* 2013: "Finding the sources of missing heritability in a yeast cross"

- 5-29 QTLs per trait (median of 12), although most QTLs have small effect size

QTL effect size: Absolute value of normalized difference in means between genotypes

---

## Bloom *et al.* 2013: "Finding the sources of missing heritability in a yeast cross"

- Good news: most additive heritability (narrow-sense) is explained by detected QTLs

---

## Bloom *et al.* 2013: "Finding the sources of missing heritability in a yeast cross"

- Bad news: There is still much heritability missing from our additive linear model

---

## Bloom *et al.* 2013: "Finding the sources of missing heritability in a yeast cross"

- What could cause the missing heritability?
  - Incorrect heritability estimates
  - Rare variants that the study is underpowered to detect
  - Structural variants (insertions or deletions – these studies typically only measure SNPs)
  - Epigenetic interactions
  - Epistatic effects
    - When the effect of a gene depends on the presence of one or more modifier genes (the genetic background)
    - Example: locus A and locus B each only cause a 5% decrease if one of the variants is present, but a 50% decrease if both are present
    - Since all pairwise interactions is too large of a search space ($100{,}000 \times 100{,}000$), can only consider all interactions that involve at least of the detected QTLs ($20 \times 100{,}000$)

---

## Human Genetics

- We want to find human variants (SNPs, etc.) that are associated with a particular phenotype (e.g. a disease)
- "Manhattan plot"
- We need a way to test whether a SNP is significantly associated with a phenotype:
  - Chi-squared test
    - Asymptotic approximation, so not appropriate if counts are small (should be at least 5 counts per category)
  - Fisher's exact test
    - An "exact" calculation (not asymptotic approximation), but involved factorials so computationally difficult when counts become large (but this is exactly when the Chi-square test is appropriate)

---

## Testing for SNP/phenotype association

- Testing for association between a SNP and a disease (or some other trait) – we are given the following counts:

| Allele | Cases | Controls | Total Counts |
| :--- | :--- | :--- | :--- |
| C | 62 | 80 | 142 |
| A | 108 | 250 | 358 |
| Total Counts | 170 | 330 | 500 |

- Calculate expected counts under null hypothesis that the proportion/ratio of cases to controls is the same regardless of whether an individual is C or A:
  - 1) calculate total proportion of cases regardless of A/C = $170/500 = 0.34$
  - 2) calculate what proportion of the 142 Cs should be cases according to the total proportion of cases = $142(0.34) = 48.28$, controls = $142(1 - 0.34) = 93.72$
  - 3) same for the As: what proportion of the 358 As should be cases/controls according to null model?
    for A individuals, expected cases = $358(0.34) = 121.72$, controls = $358(1 - 0.34) = 236.28$

---

## Testing for SNP/phenotype association

- Testing for association between a SNP and a disease (or some other trait) – we are given the following counts:

**Observed**
| Allele | Cases | Controls | Total Counts |
| :--- | :--- | :--- | :--- |
| C | 62 | 80 | 142 |
| A | 108 | 250 | 358 |
| Total Counts | 170 | 330 | 500 |

**Expected**
| Allele | Cases | Controls | Total Counts |
| :--- | :--- | :--- | :--- |
| C | 48.28 | 93.72 | 142 |
| A | 121.72 | 236.28 | 358 |
| Total Counts | 170 | 330 | 500 |

Using a Chi-squared test:

$$X^2 = \sum_{i=1}^n \frac{(O_i - E_i)^2}{E_i} = \frac{(62 - 48.28)^2}{48.28} + \frac{(80 - 93.72)^2}{93.72} + \frac{(108 - 121.72)^2}{121.72} + \frac{(250 - 236.28)^2}{236.28} = 8.25$$

$$df = (#\text{ rows} - 1)(#\text{ cols} - 1) = 1$$

---

---

[Up: contents](index.md) · [Testing for SNP/phenotype association →](02-testing-for-snp-phenotype-association.md)
