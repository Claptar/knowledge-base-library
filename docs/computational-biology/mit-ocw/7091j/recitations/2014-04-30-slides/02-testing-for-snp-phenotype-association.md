---
title: Testing for SNP/phenotype association
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-30-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-04-30-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Testing for SNP/phenotype association

Chi-Square Distribution Table

| $df$ | $\chi^2_{.995}$ | $\chi^2_{.990}$ | $\chi^2_{.975}$ | $\chi^2_{.950}$ | $\chi^2_{.900}$ | $\chi^2_{.100}$ | $\chi^2_{.050}$ | $\chi^2_{.025}$ | $\chi^2_{.010}$ | $\chi^2_{.005}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.000 | 0.000 | 0.001 | 0.004 | 0.016 | 2.706 | 3.841 | 5.024 | 6.635 | 7.879 |
| 2 | 0.010 | 0.020 | 0.051 | 0.103 | 0.211 | 4.605 | 5.991 | 7.378 | 9.210 | 10.597 |
| 3 | 0.072 | 0.115 | 0.216 | 0.352 | 0.584 | 6.251 | 7.815 | 9.348 | 11.345 | 12.838 |
| 4 | 0.207 | 0.297 | 0.484 | 0.711 | 1.064 | 7.779 | 9.488 | 11.143 | 13.277 | 14.860 |
| 5 | 0.412 | 0.554 | 0.831 | 1.145 | 1.610 | 9.236 | 11.070 | 12.833 | 15.086 | 16.750 |
| 6 | 0.676 | 0.872 | 1.237 | 1.635 | 2.204 | 10.645 | 12.592 | 14.449 | 16.812 | 18.548 |
| 7 | 0.989 | 1.239 | 1.690 | 2.167 | 2.833 | 12.017 | 14.067 | 16.013 | 18.475 | 20.278 |
| 8 | 1.344 | 1.646 | 2.180 | 2.733 | 3.490 | 13.362 | 15.507 | 17.535 | 20.090 | 21.955 |
| 9 | 1.735 | 2.088 | 2.700 | 3.325 | 4.168 | 14.684 | 16.919 | 19.023 | 21.666 | 23.589 |
| 10 | 2.156 | 2.558 | 3.247 | 3.940 | 4.865 | 15.987 | 18.307 | 20.483 | 23.209 | 25.188 |

Since our statistic (8.25) is higher than the cut-off for $P = 0.005$, the P-value is less than 0.005

Using a Chi-squared test:

$$X^2 = \sum_{i=1}^n \frac{(O_i - E_i)^2}{E_i} = \frac{(62 - 48.28)^2}{48.28} + \frac{(80 - 93.72)^2}{93.72} + \frac{(108 - 121.72)^2}{121.72} + \frac{(250 - 236.28)^2}{236.28} = 8.25$$

$df = (#\text{ rows} - 1)(#\text{ cols} - 1) = 1$, and $P(X_1^2 \ge 8.25) = 0.0041$ so we reject $\text{H}_0$ (=>SNP is associated)

---

- Testing for association between a SNP and a disease (or some other trait) – we are given the following counts:

**Observed**
| Allele | Cases | Controls | Total Counts |
| :--- | :--- | :--- | :--- |
| C | 62 | 80 | 142 |
| A | 108 | 250 | 358 |
| Total Counts | 170 | 330 | 500 |

Fisher's Exact Test:

$$p = \frac{\binom{a+b}{a} \binom{c+d}{c}}{\binom{a+b+c+d}{a+c}}$$

Sum all probabilities for observed and all more extreme values with same marginal totals to compute probability of null hypothesis

Let our 1 degree of freedom be $a$, the number of cases with "C"

Upper-tail one-sided P-value:

$$\sum_{a=62}^{142} \frac{\binom{142}{a} \binom{358}{170-a}}{\binom{500}{170}} \approx .003$$

Since the expected count of $a$ (= Cases with C) was $\sim 48$, since $62 = 48 + 14$, the lower tail goes up to $48 - 14 = 34$. The two-sided P-value is:

$$\sum_{a=0}^{34} \frac{\binom{142}{a} \binom{358}{170-a}}{\binom{500}{170}} + \sum_{a=62}^{142} \frac{\binom{142}{a} \binom{358}{170-a}}{\binom{500}{170}} \approx .0047$$

---

## Human Genetics

After doing a Chi-square test and seeing that a SNP is significantly enriched in a disease population, we might believe that the SNP is linked to the disease. But **population structure** can confound these results (methods for correcting for this are beyond the scope of this class)

Test control SNPs (known to be unrelated to the disease) for high $X^2$ distribution between cases and controls, which would indicate population stratification

In $4^{\text{th}}$ generation, fraction of Ts in population = 4/14, but in diseased group = 4/6
But once we see the family tree, we see that the SNP at locus 1 is unrelated to the disease

---

## Linkage Disequilibrium

- Recombination during meiosis "shuffles" alleles between the homologous maternal and paternal chromosomes

Over time and after many crossover events have occurred, loci that are physically close together on the chromosome will tend to remain together, so the probability of two loci occurring together is a function of their distance along the chromosome

If a crossover event is equally likely to occur at any position along the chromosome, the probability that it will separate loci A and B is much smaller than A and C or B and C

We have so far generally assumed that inheriting a particular allele at one locus won't affect the probability of inheriting an allele at a different locus. Such loci are in **linkage equilibrium**.

Loci are considered in **linkage disequilibrium** if genotypes at two loci are not independent of one another (e.g. inheriting A at locus 1 influences probability of inheriting B at locus 2)

---

## Linkage Disequilibrium

- Measuring linkage disequilibrium: consider two loci A and B, where locus A has two possible alleles A and a, and locus B has two alleles B and b:
  - then gametes can have one of four possible combinations:

| Gamete | Frequency |
| :--- | :--- |
| AB | $p_{AB}$ |
| Ab | $p_{Ab}$ |
| aB | $p_{aB}$ |
| ab | $p_{ab}$ |

| Allele | Frequency |
| :--- | :--- |
| A | $p_A = p_{AB} + p_{Ab}$ |
| a | $p_a = p_{aB} + p_{ab}$ |
| B | $p_B = p_{aB} + p_{AB}$ |
| b | $p_b = p_{ab} + p_{Ab}$ |

- Then if alleles are randomly associated w/ one another, the frequencies of the four gametes should be the product of the allele frequencies:
  - ex. $p_{AB} = p_A p_B = (p_{AB} + p_{Ab})(p_{aB} + p_{AB})$

---

## Linkage Disequilibrium

| Gamete | Frequency |
| :--- | :--- |
| AB | $p_{AB}$ |
| Ab | $p_{Ab}$ |
| aB | $p_{aB}$ |
| ab | $p_{ab}$ |

| Allele | Frequency |
| :--- | :--- |
| A | $p_A = p_{AB} + p_{Ab}$ |
| a | $p_a = p_{aB} + p_{ab}$ |
| B | $p_B = p_{aB} + p_{AB}$ |
| b | $p_b = p_{ab} + p_{Ab}$ |

- If they are not randomly associated (and therefore in linkage disequilibrium) then there will be a deviation ($D$) in the expected frequencies:
  - $p_{AB} = p_A p_B + D$
  - $p_{Ab} = p_A p_b - D$
  - $p_{aB} = p_a p_B - D$
  - $p_{ab} = p_a p_b + D$
- Where $D$ is given by:
  - $D = p_{AB} p_{ab} - p_{Ab} p_{aB}$ ($D = 0 \Rightarrow$ no disequilibrium)
- AB and ab are the "coupling" gametes (AB on one parental chromosome, ab on the other), Ab and aB are the "repulsion" gametes (crossing over event must occur between the loci) – $D$ is the difference between these types.

---

## Variant Phasing

- To determine which genes are linked together (and therefore likely to be inherited together in the next generation), you need to figure out which alleles (which variant SNPs) are on the same chromosome = "phasing"
  - Why does this matter?
    - If you have 2 different mutations in the same copy of a gene (phased), the $2^{\text{nd}}$ copy (no mutations) may be enough for normal activity
    - If there's one mutation in each (unphased), both copies of the gene may be nonfunctional
- Often rely on family data (e.g. parents) to determine which "parental" chromosome segments were inherited together in the child
- Can be used to identify haplotypes = combinations of alleles at adjacent locations in a chromosome that are inherited together over many generations

Crossing over during meiosis:
- X, Y, and Z are "in phase" on this chromosome
- x, y, and z are "in phase" on this chromosome
- Due to crossing over, the phasing has changed

---

## Variant Phasing

Longer reads will help – two SNPs present in the same read are definitely on the same chromosome

---

## Hardy-Weinberg Equilibrium (HWE)

- Assume only two alleles: A and a
- If $P(\text{A}) = \psi =$ frequency of A in the population, and the population is in HWE, then:
  - $P(\text{AA}) = \psi^2$
  - $P(\text{Aa}) = 2\psi(1-\psi)$
  - $P(\text{aa}) = (1-\psi)^2$

| gamete | A ($\psi$) | a ($1-\psi$) |
| :--- | :--- | :--- |
| A ($\psi$) | AA ($\psi^2$) | Aa ($\psi(1-\psi)$) |
| a ($1-\psi$) | Aa ($\psi(1-\psi)$) | aa ($(1-\psi)^2$) |

- HWE states that allele and genotype frequencies in a population will be constant from generation to generation in the absence of other evolutionary forces; assuming the following:
  - random mating
  - population size is infinite
  - no migration, mutation or selection (so allele frequencies won't change)

---

## HWE and Likelihood ratio tests

- Testing whether a population is in HWE using a likelihood ratio test (LRT):
  - say we observe $N = 200$ individuals with the following genotypes: 25 aa, 90 Aa, 85 AA
  - is this population in HWE?
- Recall that the likelihood ratio is given by:

$$\lambda = \frac{P(\text{Data} \mid H_0)}{P(\text{Data} \mid H_1)}$$

($P(\text{Data} \mid H_0)$: likelihood of the data under the null model; $P(\text{Data} \mid H_1)$: likelihood of the data under the alternative model)

- Then the following test statistic is approximately Chi-square distributed:

$$-2 \ln(\lambda) \sim X_{df}^2$$

- $df = (#\text{ free parameters in } H_1) - (#\text{ free parameters in } H_0)$

---

## HWE and Likelihood ratio tests

- We observe $n = 200$ individuals with the following genotypes: 25 aa, 55 Aa, 120 AA
  - is this population in HWE?
- Here, under the unconstrained model $H_1$, the parameters are $p_{AA}$, $p_{Aa}$ and $p_{aa}$ ($df = 2$)
  - for this example: $p_{AA} = 120/200 = 0.6$, $p_{Aa} = 55/200 = 0.275$, $p_{aa} = 25/200 = 0.125$
- Under the constrained model $H_0$, we only need $p_A$ (fraction of A alleles in population) and if HWE holds:
  - $p_A = (2n_{AA} + n_{Aa})/2n = (2(120) + 55)/400 = 295/400 = 0.7375$
  - $p_{AA} = (p_A)^2 = (0.7375)^2 = 0.5439$
  - $p_{Aa} = 2p_A(1-p_A) = 0.3872$
  - $p_{aa} = (1-p_A)^2 = 0.0689$

could also do a Chi-square goodness of fit test with these probabilities $*$ n as the expected counts instead of LRT

---

## HWE and Likelihood ratio tests

- We observe $N = 200$ individuals with the following genotypes: 25 aa, 90 Aa, 85 AA
  - is this population in HWE?
- Therefore, our test statistic is:

$$-2 \ln(\lambda) = -2 \ln \frac{P(\text{Data} \mid p_A^2, 2p_A(1-p_A), (1-p_A)^2)}{P(\text{Data} \mid p_{AA}, p_{Aa}, p_{aa})}$$

$$= -2 \ln \frac{P(\text{Data} \mid 0.5439, 0.3872, 0.0689)}{P(\text{Data} \mid 0.6, 0.275, 0.125)}$$

- Note that $P(\text{Data} \mid H)$ follows a multinomial distribution (generalized binomial for more than 2 categories):

$$P(x_1, \dots, x_k; n, p_1, \dots, p_k) = \frac{n!}{x_1! \dots x_k!} p_1^{x_1} \dots p_k^{x_k}$$

So for example:

$$P(\text{Data} \mid H_1) = P(25, 90, 85; 200, 0.6, 0.275, 0.125) = \frac{200!}{25!90!85!} 0.6^{25} 0.275^{90} 0.125^{85}$$

Note that the factorials will drop out of LRT

---

## Likelihood Ratio Tests

- Can use a similar LRT to determine whether the data are better explained when treated as two subpopulations, like cases and controls:
  - $H_0$: $p_{AA}$, $p_{Aa}$ and $p_{aa}$ are sufficient to explain the data
  - $H_1$: we do better by considering two subpopulations:
    - $p_{AA}^1$, $p_{Aa}^1$ and $p_{aa}^1$ for subpopulation 1 ($D^1$)
    - $p_{AA}^2$, $p_{Aa}^2$ and $p_{aa}^2$ for subpopulation 2 ($D^2$)
- Then our test statistic $T$ is:

$$T = -2 \ln \frac{P(D \mid p_{AA}, p_{Aa}, p_{aa})}{P(D^1 \mid p_{AA}^1, p_{Aa}^1, p_{aa}^1) P(D^2 \mid p_{AA}^2, p_{Aa}^2, p_{aa}^2)}$$

- approx. Chi-square distributed with $df = 4 - 2 = 2$

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 4-30 Recitation](01-4-30-recitation.md) · [Up: contents](index.md)
