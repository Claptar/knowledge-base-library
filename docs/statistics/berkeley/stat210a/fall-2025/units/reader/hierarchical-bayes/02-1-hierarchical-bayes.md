---
title: 1 Hierarchical Bayes
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Hierarchical Bayes

**Source:** [`units/reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

The full power of Bayes is realized in large, complex problems with repeat structure, allowing us to pool information across many observations.

### <span class="header-section-number">1.1</span> Example: Predicting Batting Averages {.anchored number="1.1" anchor-id="example-predicting-batting-averages"}

Predict a batter’s true batting average from <span class="math inline">\$n\_i\$</span> at-bats, <span class="math inline">\$X\_i\$</span> hits: <span class="math inline">\$X\_i\|\\theta\_i \\sim \\text{Binom}(n\_i, \\theta\_i)\$</span>

Pool info across players <span class="math inline">\$i=1,\\ldots,m\$</span> via hierarchical model:

<span class="math display">\\$$ \\begin{aligned} \\alpha, \\beta &\\sim \\pi\_0(\\alpha, \\beta) \\quad \\text{(hyperprior)} \\\\ \\theta\_i\|\\alpha, \\beta &\\sim \\text{Beta}(\\alpha, \\beta), \\quad i=1,\\ldots,m \\\\ X\_i\|\\theta\_i, n\_i &\\sim \\text{Binom}(n\_i, \\theta\_i), \\quad i=1,\\ldots,m \\end{aligned} \\$$</span>

<span class="math display">\\$$ \\mathbb{E}\[\\theta\_i\|X$$ = \\mathbb{E}$$\\mathbb{E}\[\\theta\_i\|X, \\alpha, \\beta$$\|X\] = \\mathbb{E}\\left$$\\frac{\\alpha + X\_i}{\\alpha + \\beta + n\_i}\|X\\right$$ \\\]</span>

Use all <span class="math inline">\$X\_1,\\ldots,X\_m\$</span> to learn a good prior on <span class="math inline">\$\\theta\_i\$</span>.

Note: There is always an equivalent model where we marginalize over <span class="math inline">\$\\alpha, \\beta\$</span> and just write a more complicated prior on <span class="math inline">\$\\theta\$</span>. The hierarchical version may give better intuition or computational strategies.

### <span class="header-section-number">1.2</span> Gaussian Hierarchical Model {.anchored number="1.2" anchor-id="gaussian-hierarchical-model"}

<span class="math display">\\$$ \\begin{aligned} \\theta\_i &\\sim N(\\mu, \\tau^2), \\quad i=1,\\ldots,d \\\\ X\_i\|\\theta\_i &\\sim N(\\theta\_i, \\sigma^2), \\quad i=1,\\ldots,d \\end{aligned} \\$$</span>

Posterior mean:

<span class="math display">\\$$ \\mathbb{E}\[\\theta\_i\|X$$ = \\mathbb{E}$$\\mathbb{E}\[\\theta\_i\|X, \\mu, \\tau^2$$\|X\] = \\mathbb{E}\\left$$\\frac{\\tau^2}{\\tau^2 + \\sigma^2}X\_i + \\frac{\\sigma^2}{\\tau^2 + \\sigma^2}\\mu\|X\\right$$ \\\]</span>

Linear shrinkage estimator: Bayes optimal shrinkage estimated from data.

Likelihood for <span class="math inline">\$\\mu, \\tau^2\$</span> (marginalizing over <span class="math inline">\$\\theta\_i\$</span>):

<span class="math display">\\$$ \\begin{aligned} X\_i\|\\mu, \\tau^2 &\\sim N(\\mu, \\tau^2 + \\sigma^2) \\\\ \\bar{X} &\\sim N(\\mu, \\frac{\\tau^2 + \\sigma^2}{n}) \\\\ S^2 = \\frac{1}{n-1}\\sum\_{i=1}^n (X\_i - \\bar{X})^2 &\\sim \\frac{\\tau^2 + \\sigma^2}{n-1}\\chi^2\_{n-1} \\end{aligned} \\$$</span>

Define <span class="math inline">\$B = \\tau^2 + \\sigma^2\$</span> (amount of shrinkage):

<span class="math display">\\$$ \\delta(x) = \\mathbb{E}\[\\mathbb{E}\[\\theta\_i\|X, B$$\|X\] = \\mathbb{E}\\left$$\\frac{B - \\sigma^2}{B}X\_i + \\frac{\\sigma^2}{B}\\bar{X}\|X\\right$$ \\\]</span>

Estimated from entire data set:

<span class="math display">\\$$ \\begin{aligned} \\bar{X} &\\sim N(\\mu, \\frac{B}{n}) \\\\ (n-1)S^2 &\\sim B\\chi^2\_{n-1} \\end{aligned} \\$$</span>

Conjugate prior (scale mixture):

<span class="math display">\\$$ \\pi(B\|\\lambda, \\nu) \\propto B^{-\\nu/2-2}\\exp(-\\frac{\\lambda}{2B}) \\$$</span>

<span class="math display">\\$$ B\|X \\sim \\text{InvGamma}\\left(\\frac{n+\\nu}{2}, \\frac{\\lambda + (n-1)S^2}{2}\\right) \\$$</span>

<span class="math display">\\$$ \\mathbb{E}\\left\[\\frac{1}{B}\|X\\right$$ = \\frac{n+\\nu}{\\lambda + (n-1)S^2} \\\]</span>

<span class="math display">\\$$ \\delta\_i(x) = \\frac{(n-3)S^2}{(n-1)S^2 + \\lambda}X\_i + \\frac{\\lambda + 2S^2}{(n-1)S^2 + \\lambda}\\bar{X} \\$$</span>

Pseudo-data: <span class="math inline">\$\\nu, \\lambda\$</span> with <span class="math inline">\$\\nu \\approx 2, \\lambda \\approx \\nu\\sigma^2\$</span>

Might want to truncate prior to <span class="math inline">\$$$\\sigma^2, \\infty)\$</span> if <span class="math inline">\$\\lambda\$</span> small.

### <span class="header-section-number">1.3</span> Graphical Form {.anchored number="1.3" anchor-id="graphical-form"}

For hyperparameters <span class="math inline">\$\\alpha, \\beta\$</span>:

         α, β
        /  |  \
       θ₁  θ₂  θ₃
       |   |   |
       X₁  X₂  X₃

These are the distributions associated with a factor for each vertex in a DAG <span class="math inline">\$(V,E)\$</span>:

<span class="math display">\\\[ p(z) = \\prod\_{i=1}^{\|V\|} p(z\_i\|z\_{\\text{pa}(i)}) \\$$</span>

For this model:

<span class="math display">\\$$ p(\\alpha, \\beta, \\theta\_1,\\ldots,\\theta\_m, X\_1,\\ldots,X\_m) = p(\\alpha, \\beta)\\prod\_{i=1}^m p(\\theta\_i\|\\alpha, \\beta)p(X\_i\|\\theta\_i) \\$$</span>

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Markov Chain Monte Carlo (MCMC) →](03-2-markov-chain-monte-carlo-mcmc.md)
