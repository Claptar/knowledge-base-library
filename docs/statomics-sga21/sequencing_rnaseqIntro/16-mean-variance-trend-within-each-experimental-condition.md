---
title: Mean-variance trend within each experimental condition
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Mean-variance trend within each experimental condition

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

cont24ID <- which(treatment == "Control" & time == "24h")
DPN24ID <- which(treatment == "DPN" & time == "24h")
OHT24ID <- which(treatment == "OHT" & time == "24h")
cont48ID <- which(treatment == "Control" & time == "48h")
DPN48ID <- which(treatment == "DPN" & time == "48h")
OHT48ID <- which(treatment == "OHT" & time == "48h")
idList <- list(cont24ID, DPN24ID, OHT24ID,
               cont48ID, DPN48ID, OHT48ID)
names(idList) <- paste0(rep(levels(treatment),2), rep(levels(time), each=3))

par(mfrow=c(3,2), mar=c(2,2,2,1))
for(kk in 1:length(idList)){
  # extract counts for each condition
  curCounts <- assays(se)$counts[,idList[[kk]]]
  plot(x = rowMeans(curCounts)+1,
       y = rowVars(curCounts)+1,
       pch = 16, cex=1/2,
       xlab = "Mean", ylab="Variance",
       main = names(idList)[kk],
       log="xy")
  abline(0,1, col="red")
  lw1 <- loess((rowVars(curCounts)+1) ~ (rowMeans(curCounts)+1), span=1/4, lwd=3)
  oo <- order(rowMeans(curCounts)+1)
  lines(rowMeans(curCounts)[oo]+1, lw1$fitted[oo], col="orange")

  smoothScatter(x = log1p(rowMeans(curCounts)),
       y = log1p(rowVars(curCounts)),
       pch = 16, cex=1/2,
       xlab = "Mean", ylab="Variance")
  abline(0,1, col="red")
  lines(log(rowMeans(curCounts)[oo]+1), log(lw1$fitted[oo]+1), col="orange")
}
```

 - Having data on thousands of genes provides the opportunity to empirically assess the mean-variance relationship.
 - It is clear that the data is overdispersed with respect to the Poisson distribution (red $y=x$ line). There also seems to be a quadratic trend of the variance as a function of the mean. This has motivated the **negative binomial distribution as the most popular choice to model (bulk) RNA-seq gene expression data**.

 ---

 - The negative binomial distribution is also referred to as the Gamma-Poisson distribution as it can be formulated as such. Indeed, if
 $$
 \lambda \sim \Gamma(\alpha, \beta) \\
 Y | \lambda \sim Poi(\lambda),
 $$
 then this is equivalent to
 $$ Y \sim NB(\mu = \alpha / \beta, \phi = 1/\alpha). $$
 - This can be shown analytically, but is considered out of the scope of this course. Below, we show it empirically using simulation.
 - This theoretical result has got some practical consequences. The Gamma-Poisson formulation makes it clear why we can sum technical replicates as the sum of Poisson random variables is again a Poisson random variable.
 - The Poisson statement can thus be considered as capturing technical variation, while the Gamma statement can be considered to capture biological variation, i.e., variation in the mean expression across biological replicates.

```r
alpha <- 20
beta <- 10
lambda <- rgamma(n = 1e5, shape = alpha, rate = beta)
y1 <- rpois(n = 1e5, lambda = lambda)

---

[← Challenge I: Choice of modeling assumptions](15-challenge-i-choice-of-modeling-assumptions.md) · [Up: contents](index.md) · [note phi = 1 / size →](17-note-phi-1-size.md)
