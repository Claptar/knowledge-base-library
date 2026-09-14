---
title: '"True" Fisher information'
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/asymptotics.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/asymptotics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# "True" Fisher information

**Source:** [`reader/asymptotics.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/asymptotics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

sigma <- sqrt(colMeans(sigma.hat^2))
hist(beta.hat[,2], freq=FALSE, breaks=50, main = expression(paste("Simulated distribution of ", hat(beta)[1])), xlab=expression(hat(beta)[1]))
curve(dnorm(x, mean = beta[2], sd = sigma[2]), add=TRUE)

hist((beta.hat[,2] - beta[2])/sigma.hat[,2], freq=FALSE, breaks=30, main = expression(paste("Simulated distribution of ", Z[1] == (hat(beta)[1]-beta[1])/hat(sigma)[1])), xlab=expression(Z[1]))
curve(dnorm(x), add=TRUE)
```

These results about the MLE apply far beyond logistic regression, to a wide variety of other models. To begin to prove them, however, we will need to be more precise about what we mean by $\hat\beta$ approximately following a normal distribution, or by the estimator $\hat\Sigma$ being approximately equal to the estimand $\Sigma(\beta)$.

---

[← Introduction to Asymptotic Theory](01-introduction-to-asymptotic-theory.md) · [Up: contents](index.md) · [Convergence →](03-convergence.md)
