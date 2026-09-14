---
title: The Poisson distribution
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# The Poisson distribution

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

- The Poisson distribution is a typical count distribution that is generally popular and fairly easy to work with. It is defined by a single parameter: its mean $\mu$. For a Poisson distributed random variable $Y_i$ with observations $i \in \{1, \ldots, n\}$, its variance is equal to its mean. That is, if $Y_i \sim Poi(\mu)$, then $E(Y_i) = Var(Y_i) = \mu$.
 - This immediately shows an important feature of count data: the **mean-variance relationship**. Indeed, in count data, the variance will always be a function of the mean.
 - This is quite intuitive. Consider the following example. You have two bird cages, where in one bird cage there are $10$ birds, while in the other there are $100$ birds. You let a sample of people count the number of birds in either one of the cages. It seems unlikely that a person in front of the 10-bird cage would come up with an estimate of $5$, while it seems quite likely that someone in front of the 100-bird cage would come up with an estimate of $95$. Even though the difference from the true value is the same, the exact value has an impact on the plausible deviation around it.

```r
set.seed(11)
y1 <- rpois(n=500, lambda=10)
y2 <- rpois(n=500, lambda=100)

par(mfrow = c(1,2))
hist(y1, main="Poisson(10)", breaks=40)
hist(y2, main="Poisson(100)", breaks=40)
```

## The Poisson distribution in RNA-seq

 - In RNA-seq, technical replicates represent different aliquots of the same sample being sequenced repeatedly. The underlying true expression of a gene can hence safely be assumed to be equal across these technical replicates.
 - [Marioni *et al.* (2008)](https://genome.cshlp.org/content/18/9/1509) have shown that, for most genes, the distribution of observed gene expression counts across technical replicates follow a Poisson distribution. A small proportion of genes ($\sim 0.5\%$) do not follow this Poisson model, however, and actually show evidence for *'extra-Poisson variation'*.

```r

---

[← A function for captioning and referencing images](01-a-function-for-captioning-and-referencing-images.md) · [Up: contents](index.md) · [All defaults →](03-all-defaults.md)
