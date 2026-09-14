---
title: Modeling approach
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Modeling approach

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Assume we have C unique molecules in the library and we obtain N sequencing reads

- The probability distribution of the number of times we sequence a particular molecule is binomial (individual success probability p=1/C, N trials in total)

- Assume Poisson sampling as a tractable approximation (rate λ = N/C)

- Finally, truncate the Poisson process: we only see events that happened between L and R times (we don’t know how many molecules were observed 0 times)

5

**See e.g. Cohen,** **_JASA_ (1954)**

### Estimating library complexity with a Poisson model

- For Poisson sampling, we can write the (truncated) distribution over xi, the times we sequence the i<sup>th</sup> molecule as:


- [ The probability is 0 if xi is less than L or greater than R ]

- • We can estimate the maximum likelihood rate parameter λ from a vector of observations **x**

6

### Maximum likelihood library size


- M unique sequences observed, maximum likelihood library size is


- Approximate solution


7

#### Poisson Library Complexity model 150 1000 Genome Datasets


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

8

#### Poisson Library Complexity model 150 1000 Genome Datasets

**Poisson** l **= Me** **~~a~~ n = Variance**

- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

9

Library complexity is the number of unique molecules in the “library” that is sampled by finite sequencing


<!-- Start of picture text -->
Sample DNA<br>Adapters<br>Ligation<br><!-- End of picture text -->

**Library Complexity = 4 Reads**


<!-- Start of picture text -->
Amplification<br><!-- End of picture text -->

**Sequencing**

**Image adapted from Mardis,** **_ARGHG_ (2008)**

10

Gamma sampling rates describe the entire population (library preparation)

Poisson sampling to form a smaller sample ( _sequencing_ )

Negative binomial distribution characterizes the resulting occurrence histogram


@ source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

11

##### The gamma distribution is a “conjugate prior” for the Poission distribution


12

##### Negative Binomial model for sequence occurrences

C – library complexity (latent, fit to observed data) N – number of reads

M – total number of unique sequences l= N/C

k -  dispersion (latent, fit to observed data)

Pr(xi | l, k)  = NegativeBinomial(xi | l, k) = NegativeBinomial(xi | n, p) p = l / (l + 1/k) n = 1/k

13

Simulation results show that the Gamma Possion works well for non-uniform libraries

- True library complexity: 1M unique molecules

- • Vary k (controls sampling rate variance)

- Given 100K reads (λ=0.1), assess estimates from both models

–k=0.1 Poisson: 0.93M GP: 0.96M –k=1 Poisson: 0.52M GP: 1.01M –k=10 Poisson: 0.12M GP: 1.10M –k=20 Poisson: 0.07M GP: 0.68M

95% unique 91% unique 70% unique 59% unique

14

###### Negative Binomial Library Complexity model 150 1000 Genome Datasets Data are “overdispersed” (variance greater than mean)


- © source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

15

##### Marginal value of additional sequencing

C – library complexity (latent – estimated) N – number of reads

M – number of unique sequences

M can be estimated by (1 – Poisson(0 | l)) * C M can be estimated by (1 – NegativeBinomial(0 | l, k)) * C

Assume we have r more reads s = (N + r) / N

Replace l by sl to estimate M’ achieved with r more reads

16

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Marginal utility of sequencing →](03-marginal-utility-of-sequencing.md)
