---
title: 'Challenge I: Choice of modeling assumptions'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Challenge I: Choice of modeling assumptions

When working with a GLM, as part of the choices of modeling assumptions, we need to pick an appropriate distribution for the expression counts. Below we perform some exploratory analyses to investigate.

```r
y <- assays(se)$counts[1,]
hist(y, breaks = 40,
     xlab = "Gene expression",
     xaxt = "n", yaxt = "n",
     main = "Data for the first gene")
axis(1, at = seq(200, 1200, by=200))
axis(2, at = 0:3)

# Mean-variance trend within each experimental condition
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

# note phi = 1 / size
y2 <- rnbinom(n=1e5, mu=alpha / (beta), size=alpha)


plot(density(y1))
lines(density(y2), col="steelblue")
```

---

[← Experimental design, data import and data exploration](02-experimental-design-data-import-and-data-exploration.md) · [Up: contents](index.md) · [Challenge II: Normalization →](04-challenge-ii-normalization.md)
