---
title: Sample mean
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-one-parameter.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-one-parameter.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Sample mean

**Source:** [`reader/testing-one-parameter.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-one-parameter.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

c.alpha <- quantile(rowSums(Z), 1-alpha)
power[,t1.ix+1] <- sapply(theta.grid, function(th) mean(rowSums(Z+th)>c.alpha))

matplot(theta.grid, power, col=c("black","blue","red","darkgreen","purple"), lty=c(2,2,2,1,1), lwd=c(1,1,1,2,2), type="l", xlab=expression(theta), ylab="Power", main = "Power for various test statistics (Laplace)")
grid()
abline(h=c(0,alpha,1),lty=3)
abline(v=0,lty=3)
axis(2,at=alpha,labels = expression(alpha))
legend("bottomright",legend=c(expression(Sigma[i] *T[2](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X[i])), expression(Sigma[i] *T[1](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X[i])), expression(Sigma[i] *T[0.2](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X[i])), expression(S[0](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/X)), expression(Sigma[i] *X[i])), lty=c(2,2,2,1,1), lwd=c(1,1,1,2,2), col=c("black","blue","red","darkgreen","purple"))
```


### The sign test as a nonparametric test

The test based on the binomial statistic $S_0(X)$ (or $B(X)$) is called the *sign test*, and is generally an appealing test for a *nonparametric* testing problem. Suppose $X_1,\ldots,X_n \simiid F$, where $F$ represents an unknown cdf for their distribution. Assume for simplicity that $F$ is continuous and strictly increasing on its support, so that the median $\theta(F) = F^{-1}(1/2)$ is well-defined, and consider testing $H_0:\; \theta(F) \leq 0$ vs $H_1:\; \theta(F) > 0$.

Then $B(X) \sim \text{Binom}(n, 1-F(0))$, where the probability parameter $1-F(0)$ is no more than $1/2$ if $H_0$ is true, but strictly greater than $1/2$ if $H_1$ is true. Then the test that rejects when $S(X)$ is above the upper $1-\alpha$ quantile of the $\text{Binom}(n,1/2)$ distribution (randomizing at the boundary if desired) is level-$\alpha$ on $H_0$.

---

[← One-sided testing](02-one-sided-testing.md) · [Up: contents](index.md) · [Two-sided alternatives →](04-two-sided-alternatives.md)
