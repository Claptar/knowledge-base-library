---
title: The Poisson distribution
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The Poisson distribution

```r
# A function for captioning and referencing images
fig <- local({
    i <- 0
    ref <- list()
    list(
        cap=function(refName, text) {
            i <<- i + 1
            ref[[refName]] <<- i
            paste("Figure ", i, ": ", text, sep="")
        },
        ref=function(refName) {
            ref[[refName]]
        })
})
```

```r
knitr::opts_chunk$set(echo = TRUE)
suppressPackageStartupMessages({
  library(knitr)
  library(rmarkdown)
  library(ggplot2)
})
```

In this lecture we will introduce the main principles of working with count data, and how to model these using generalized linear models (GLMs). We focus on introducing the concept of generalized linear models, and how to interpret its results. We touch briefly upon statistical inference, providing the main results rather than the theory behind it, such that they can be applied to genomics data analysis.

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
# All defaults
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

[Up: contents](index.md) · [Modeling count data: Generalized linear models →](02-modeling-count-data-generalized-linear-models.md)
