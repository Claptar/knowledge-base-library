---
title: Confidence Sequences
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html
source_file: sources/berkeley-stat158/spring-2026/27-sequential-analysis/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Confidence Sequences

**Source:** [`27-sequential-analysis/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/27-sequential-analysis/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Confidence Sequences

***Confidence sequences*** <span class="citation" cites="waudby-smith2024">Waudby-Smith et al. (<a href="#/references" role="doc-biblioref" onclick="">2024</a>)</span> — the sequential analogue of CIs

> Valid at **all** sample sizes, no matter when you peek

<span class="math display">\\$$ \\mathsf{P}\\!\\left(\\forall\\, n \\in \\{0, 1, \\ldots\\} : \\mu \\in \\bar C\_n(X)\\right) \\geq 1 - \\alpha \\$$</span> <span class="math display">\\$$ \\forall\\, n \\in \\{0, 1, \\ldots\\},\\quad \\mathsf{P}\\!\\left(\\mu \\in \\dot C\_n(X)\\right) \\geq 1 - \\alpha \\$$</span>

## Illustration: A Simple Experiment

We consider a simple randomized experiment:

| Parameter | Value | Description |
|----|----|----|
| <span class="math inline">\$n\$</span> | 1000 | Total samples |
| <span class="math inline">\$p\_0\$</span> | 0.4 | Mean under control |
| <span class="math inline">\$p\_1\$</span> | 0.6 | Mean under treatment |
| <span class="math inline">\$e\$</span> | 0.5 | Propensity score |
| <span class="math inline">\$\\tau = p\_1 - p\_0\$</span> | **0.2** | True ATE |

The IPW estimator is <span class="math inline">\$\\phi\_i = \\frac{Z\_i Y\_i}{e} - \\frac{(1-Z\_i)Y\_i}{1-e}\$</span>

## We Use the Robbins Confidence Sequence

**robbins\_confseq**

Show robbins\_confseq

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
library(ggplot2)
library(patchwork)

running_sd <- function(x) {
  n  <- seq_along(x)
  M2 <- numeric(length(x))
  mu <- cumsum(x) / n
  for (t in 2:length(x)) {
    d     <- x[t] - mu[t - 1]
    M2[t] <- M2[t - 1] + d * (x[t] - mu[t])
  }
  sqrt(pmax(M2 / pmax(n - 1, 1), 1e-10))
}

robbins_confseq <- function(x, alpha = 0.05, rho = 1) {
  n      <- seq_along(x)
  mu_hat <- cumsum(x) / n
  s_n    <- running_sd(x)
  radius <- s_n * sqrt(
    (2 * (n * rho^2 + 1) / (n^2 * rho^2)) *
    log(sqrt(n * rho^2 + 1) / alpha)
  )
  data.frame(lower = mu_hat - radius, upper = mu_hat + radius)
}
```

- The math is not incredibly important, but it is here for future reference.
- <span class="math inline">\$\\rho\$</span> parameter changes how fast the width converges (tradeoff)
- Fun fact: Herbert Robbins invented Stochastic Gradient Descent!

## Confidence Sequences vs. CLT CI

Show simulation code

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}

---

[← Use in Industry and Research](06-use-in-industry-and-research.md) · [Up: contents](index.md) · [--- Parameters --- →](08-----parameters.md)
