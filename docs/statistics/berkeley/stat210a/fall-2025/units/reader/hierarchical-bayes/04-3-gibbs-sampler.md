---
title: 3 Gibbs Sampler
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Gibbs Sampler

**Source:** [`units/reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

For parameter vector <span class="math inline">\$\\theta = (\\theta\_1, \\ldots, \\theta\_d)\$</span>:

Algorithm: 1. Initialize <span class="math inline">\$\\theta^{(0)}\$</span> 2. For <span class="math inline">\$t = 1, \\ldots, T\$</span>: For <span class="math inline">\$j = 1, \\ldots, d\$</span>: Sample <span class="math inline">\$\\theta\_j^{(t)} \\sim p(\\theta\_j \| \\theta\_{-j}^{(t-1)}, X)\$</span> Record <span class="math inline">\$\\theta^{(t)}\$</span>

Variations: - Update one random coordinate <span class="math inline">\$J \\sim \\text{Unif}(1,\\ldots,d)\$</span> - Update coordinates in random order

Advantage for hierarchical priors: only need to sample low-dimensional conditional distributions:

<span class="math display">\\$$ p(\\theta\_i \| \\theta\_{-i}, X, \\alpha) \\propto p(\\theta\_i \| \\theta\_{\\text{pa}(i)}) \\prod\_{j \\in \\text{ch}(i)} p(\\theta\_j \| \\theta\_i) \\$$</span>

Especially easy if using conjugate priors at all levels; often can be parallelized.

### <span class="header-section-number">3.1</span> Gibbs Stationarity {.anchored number="3.1" anchor-id="gibbs-stationarity"}

Claim: If <span class="math inline">\$\\pi\_t = \\pi(\\theta\|X)\$</span>, then <span class="math inline">\$\\pi\_{t+1} = \\pi(\\theta\|X)\$</span>.

Proof (sketch): Consider updating only one fixed coordinate <span class="math inline">\$j\$</span>: <span class="math inline">\$\\theta\_j^{(t+1)} \\sim p(\\theta\_j \| \\theta\_{-j}^{(t)}, X)\$</span> If <span class="math inline">\$\\theta^{(t)} \\sim \\pi(\\theta\|X)\$</span>, then <span class="math inline">\$\\theta^{(t+1)} \\sim \\pi(\\theta\|X)\$</span> Updating any coordinate preserves posterior distribution Updating coordinates in any order also does

In theory: Pick initialization and valid kernel <span class="math inline">\$Q\$</span>, sample long enough, get <span class="math inline">\$\\theta^{(t)} \\sim \\pi(\\theta\|X)\$</span> Do it again <span class="math inline">\$N\$</span> more times, get <span class="math inline">\$N\$</span> samples from <span class="math inline">\$\\pi(\\theta\|X)\$</span>

In practice: How do we know we’ve sampled long enough? - Plot <span class="math inline">\$\\theta\_i^{(t)}\$</span> vs <span class="math inline">\$t\$</span>, show how fast the MC mixes - Look for <span class="math inline">\$\\hat{R} = \\frac{\\text{between-chain variance}}{\\text{within-chain variance}} \\approx 1\$</span>

These methods are GOOD, NOT GREAT. Can be deceived, especially for bimodal posteriors.

Better approach: Burn-in then convergence. Estimate posterior based on <span class="math inline">\$\\theta^{(B+1)}, \\ldots, \\theta^{(B+N)}\$</span>

For function <span class="math inline">\$f(\\theta)\$</span>: <span class="math inline">\$\\hat{\\mu}\_f = \\frac{1}{N} \\sum\_{t=B+1}^{B+N} f(\\theta^{(t)})\$</span>

### <span class="header-section-number">3.2</span> Implementation Details Matter {.anchored number="3.2" anchor-id="implementation-details-matter"}

Example: <span class="math display">\\$$ \\begin{aligned} \\theta &\\sim N(0, 100) \\\\ X\_i \| \\theta &\\sim N(\\theta, 0.1^2), \\quad i=1,\\ldots,n \\end{aligned} \\$$</span>

Posterior: <span class="math inline">\$\\theta \| X \\sim N\\left(\\frac{\\bar{X}/0.01^2}{n/0.01^2 + 1/100}, \\frac{1}{n/0.01^2 + 1/100}\\right)\$</span>

Gibbs sampler: 1. <span class="math inline">\$\\mathbb{E}$$\\theta\|X$$ = 8.9, \\text{SD}(\\theta\|X) = 0.1\$</span> 2. <span class="math inline">\$\\theta^{(t+1)} \| X, \\theta^{(t)} \\sim N(8.9, 0.1^2)\$</span>

Gibbs takes a long time to mix.

Better parameterization: <span class="math display">\\$$ \\begin{aligned} B &= \\theta - \\bar{X} \\\\ \\theta &= B + \\bar{X} \\end{aligned} \\$$</span>

<span class="math inline">\$B\|X \\sim N(0, 0.1^2)\$</span>

Gibbs: Directly sampling from posterior

---

[← 2 Markov Chain Monte Carlo (MCMC)](03-2-markov-chain-monte-carlo-mcmc.md) · [Up: contents](index.md) · [4 Empirical Bayes →](05-4-empirical-bayes.md)
