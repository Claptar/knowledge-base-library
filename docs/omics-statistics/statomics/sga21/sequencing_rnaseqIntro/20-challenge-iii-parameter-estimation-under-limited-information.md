---
title: 'Challenge III: Parameter estimation (under limited information setting)'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Challenge III: Parameter estimation (under limited information setting)

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

There are two challenges to be overcome here:

 - First, we need to get the structure of our mean model right, this is, which covariates to include, and how to include them, such that we are capable of capturing important sources of variation in our experiment, in order to derive a correct interpretation of the data in terms of our research question.
 - Second, we need to be able to estimate the parameters of our model in an efficient way, while having limited information (i.e., we are often confronted with only a small number of replicates).

## Defining the model for the mean

Let's first check how the authors of the original study parameterized the mean model.

```r

---

[← All defaults](19-all-defaults.md) · [Up: contents](index.md) · [All defaults →](21-all-defaults.md)
