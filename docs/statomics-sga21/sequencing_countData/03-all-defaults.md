---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/marioniFigs_cropped.png")
```

## Relative uncertainty for Poisson distributed random variables

Take a minute to consider the following question:

 - Suppose that we have a solid tumor sample from a cancer patient, as well as a sample of surrounding healthy tissue. For each sample, we have three technical replicates at our disposal. Let $Y_{grt}$ denote the observed gene expression values of gene $g$ in replicate $r \in \{1,2,3\}$ from tissue $t \in \{0,1\}$, where $t=0$ denotes healthy tissue and $t=1$ denotes tumoral tissue.
 - We then know that the random variables $Y_{gr0}$ and $Y_{gr1}$ follow a Poisson distribution, and we would estimate its mean as $\bar{Y}_{g0} = \frac{1}{3} \sum_{r=1}^3 Y_{gr0}$ and $\bar{Y}_{g1} = \frac{1}{3} \sum_{r=1}^3 Y_{gr1}$, respectively.
 - Similar, for another gene $k$, we observe $Y_{krt}$, and estimate $\bar{Y}_{k0}$ and $\bar{Y}_{k1}$ correspondingly.
 - Now suppose that $\beta_{k} = \bar{Y}_{k1} / \bar{Y}_{k0} = 5$, but also $\beta_g = \bar{Y}_{g1} / \bar{Y}_{g0} = 5$, i.e., the two genes have the same average expression ratio (also often called a fold-change) across samples. However, they are differently expressed as $\bar{Y}_{k1} = 100$, and $\bar{Y}_{g1} = 10$ (making $\bar{Y}_{k0} = 20$, and $\bar{Y}_{g0} = 2$).
 - For which of the two genes is the uncertainty on the expression ratio the highest? In other words, do we trust $\beta_k$ more or do we trust $\beta_g$ more?

 ---

Let's approximate the uncertainty in $\beta_g$ and $\beta_k$ using simulation:

```r
N <- 1e3
beta_g <- beta_k <- vector(length=N)
for(ii in 1:N){
  ygr1 <- rpois(n=3, lambda=10)
  ygr0 <- rpois(n=3, lambda=2)
  ykr1 <- rpois(n=3, lambda=100)
  ykr0 <- rpois(n=3, lambda=20)
  beta_g[ii] <- mean(ygr1) / mean(ygr0)
  beta_k[ii] <- mean(ykr1) / mean(ykr0)
}

par(mfrow=c(1,2), mar=c(4,2,3,1))
hist(beta_g, breaks=seq(0,50,by=1), xlim=c(0,50))
hist(beta_k, breaks=seq(0,50,by=1), xlim=c(0,50))
```

 ---

 We clearly see that the uncertainty on $\beta_k$ is much lower than on $\beta_g$. Even though the variance on the counts of gene $k$ is higher, since its mean is higher and it is distributed as a Poisson variable. How do we explain this?

 - We may explain this by considering the relative uncertainty on the mean. Relative uncertainty may be defined as the coefficient of variation $CV = \frac{\sigma}{\mu}$ (this is, the standard deviation divided by the mean). Indeed, the CV describes the relative deviation of the distribution relative to its mean, where a low CV indicates low dispersion with respect to the mean.
 - Calculating the CV shows that **the relative uncertainty for gene $k$ than for gene $g$, even though the variance on the raw counts is higher for gene $k$ than for gene $g$**.
 - This lower relative uncertainty on the mean then propagates further to a lower uncertainty on the fold-change. This basic result will be essential for understanding the results of a differential expression analysis!

```r
sqrt(100)/100 #CV for gene k

sqrt(10)/10 #CV for gene g
```

---

[← The Poisson distribution](02-the-poisson-distribution.md) · [Up: contents](index.md) · [Modeling count data: Generalized linear models →](04-modeling-count-data-generalized-linear-models.md)
