---
title: Sample
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd
source_file: sources/gtpb-psls20/theory/02-concepts.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Sample

**Source:** [`theory/02-concepts.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/02-concepts.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- In real studies we typically do not know the distribution in the population.

- Due to financial and logistic reasons we can almost never study the entire population.

- The population parameters (e.g. mean IQ, variance of IQ)  can therefore not be obtained without error.

- Only as small subset of the population can be studied: the *sample*
- Sample according to a structured design: select **subject completely at random from the population** so that every subject has an equal probability to end up in the sample $\rightarrow$ **Representative sample**.

- The sample $x_1, x_2, . . . , x_{n}$ can be considered to be $n$ realisations of the same random variable $X$, for subjects $i = 1,2,...,n$.

- The distribution in the population is unknown and has to be estimated.

- If we can assume that the studied characteristic follows a particular distribution (e.g. a normal distribution $N(\mu,\sigma^2)$ then we only have to estimate the population parameters (e.g $\mu$ and $\sigma^2$) based on the sample.

- We refer to them as estimates and denote them by $\hat \mu$ and $\hat \sigma^2$.

---

## NHANES example

- Gender in the population
- Select $n=10000$ subjects at random from the American population.
- Once the random individuals are sampled from the population we have observed $n$ realisations of the random variable $X$.

- *Convention*: Observed values $\rightarrow$ are denoted with a small letter $x$.

- $x$ is a particular value measured/observed in a conducted experiment and no longer an unknown variable.

## In summary

  - Unknown values of the studied population characteristic for 1 to $n$ subjects in a sample are random variables: $X_1, \ldots, X_n$
  - We have to reason on this in order to understand how the observations, estimates and conclusions of a study can change from sample to sample.
  - In a sample we observe the realised outcomes $x_1, x_2, \dots, x_n$: e.g. the observed genders or the observed direct cholesterol levels of the subjects in the sample.

---

---

[← Describing the population](06-describing-the-population.md) · [Up: contents](index.md) · [Gender Example →](08-gender-example.md)
