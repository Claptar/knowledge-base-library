---
title: 3 Markov Chain Monte Carlo {number="3"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 3 Markov Chain Monte Carlo {number="3"}

**Source:** [`reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/hierarchical-bayes.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

## <span class="header-section-number">3.1</span> Hierarchical Bayes {.anchored number="3.1" anchor-id="hierarchical-bayes"}

The full power of Bayes is realized in large, complex problems with repeat structure, allowing us to pool information across many observations.

### <span class="header-section-number">3.1.1</span> Example: Predicting Batting Averages {.anchored number="3.1.1" anchor-id="example-predicting-batting-averages"}

Predict a batter’s true batting average from <span class="math inline">\$n\_i\$</span> at-bats, <span class="math inline">\$X\_i\$</span> hits: <span class="math inline">\$X\_i\|\\theta\_i \\sim \\text{Binom}(n\_i, \\theta\_i)\$</span>

Pool info across players <span class="math inline">\$i=1,\\ldots,m\$</span> via hierarchical model:

<span class="math display">\\$$ \\begin{aligned} \\alpha, \\beta &\\sim \\pi\_0(\\alpha, \\beta) \\quad \\text{(hyperprior)} \\\\ \\theta\_i\|\\alpha, \\beta &\\sim \\text{Beta}(\\alpha, \\beta), \\quad i=1,\\ldots,m \\\\ X\_i\|\\theta\_i, n\_i &\\sim \\text{Binom}(n\_i, \\theta\_i), \\quad i=1,\\ldots,m \\end{aligned} \\$$</span>

<span class="math display">\\$$ \\mathbb{E}\[\\theta\_i\|X$$ = \\mathbb{E}$$\\mathbb{E}\[\\theta\_i\|X, \\alpha, \\beta$$\|X\] = \\mathbb{E}\\left$$\\frac{\\alpha + X\_i}{\\alpha + \\beta + n\_i}\|X\\right$$ \\\]</span>

Use all <span class="math inline">\$X\_1,\\ldots,X\_m\$</span> to learn a good prior on <span class="math inline">\$\\theta\_i\$</span>.

Note: There is always an equivalent model where we marginalize over <span class="math inline">\$\\alpha, \\beta\$</span> and just write a more complicated prior on <span class="math inline">\$\\theta\$</span>. The hierarchical version may give better intuition or computational strategies.

### <span class="header-section-number">3.1.2</span> Gaussian Hierarchical Model {.anchored number="3.1.2" anchor-id="gaussian-hierarchical-model"}

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

### <span class="header-section-number">3.1.3</span> Graphical Form {.anchored number="3.1.3" anchor-id="graphical-form"}

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

## <span class="header-section-number">3.2</span> Markov Chain Monte Carlo (MCMC) {.anchored number="3.2" anchor-id="markov-chain-monte-carlo-mcmc"}

Hierarchical models are very flexible, but often create big computational headaches:

<span class="math display">\\$$ \\pi(\\theta\|x) = \\frac{p(x\|\\theta)\\pi(\\theta)}{\\int p(x\|\\theta)\\pi(\\theta)d\\theta} \\$$</span>

Numerator is usually nice, denominator often intractable.

Computational strategy: Set up a Markov chain with stationary distribution <span class="math inline">\$\\pi(\\theta\|x)\$</span>, run it to get approximate samples from <span class="math inline">\$\\pi(\\theta\|x)\$</span>.

### <span class="header-section-number">3.2.1</span> Definition of Markov Chain {.anchored number="3.2.1" anchor-id="definition-of-markov-chain"}

A stationary Markov chain with transition kernel <span class="math inline">\$Q(y\|x)\$</span> and initial distribution <span class="math inline">\$\\pi\_0(x)\$</span> is a sequence of r.v.’s <span class="math inline">\$X\_0, X\_1, \\ldots\$</span> where <span class="math inline">\$X\_0 \\sim \\pi\_0\$</span> and:

<span class="math display">\\$$ P(X\_{t+1} \\in A \| X\_t, \\ldots, X\_0) = P(X\_{t+1} \\in A \| X\_t) = \\int\_A Q(y\|X\_t) dy \\$$</span>

Marginal distribution of <span class="math inline">\$X\_t\$</span>:

<span class="math display">\\$$ \\pi\_t(y) = P(X\_t \\in A) = \\int Q(y\|x)\\pi\_{t-1}(x) dx \\$$</span>

This is a directed graphical model: <span class="math inline">\$X\_0 \\to X\_1 \\to X\_2 \\to \\cdots\$</span>

If <span class="math inline">\$\\pi(y) = \\int Q(y\|x)\\pi(x) dx\$</span>, we say <span class="math inline">\$\\pi\$</span> is a stationary distribution for <span class="math inline">\$Q\$</span>.

A sufficient condition is detailed balance:

<span class="math display">\\$$ \\pi(x)Q(y\|x) = \\pi(y)Q(x\|y) \\$$</span>

<span class="math display">\\$$ \\int\_y Q(y\|x)\\pi(x) dx = \\int\_y \\pi(y)Q(x\|y) dy = \\pi(y) \\$$</span>

A Markov chain with detailed balance is called reversible: <span class="math inline">\$X\_{t-1} \| X\_t \\sim X\_{t+1} \| X\_t\$</span> if <span class="math inline">\$\\pi\_t = \\pi\$</span>.

### <span class="header-section-number">3.2.2</span> Theory {.anchored number="3.2.2" anchor-id="theory"}

If a Markov chain with stationary distribution <span class="math inline">\$\\pi\$</span> is:

1.  Irreducible: <span class="math inline">\$\\forall x,y, \\exists n: P(X\_n = y \| X\_0 = x) &gt; 0\$</span>
2.  Aperiodic: <span class="math inline">\$\\forall x, \\gcd\\{n &gt; 0: P(X\_n = x \| X\_0 = x) &gt; 0\\} = 1\$</span>

Then <span class="math inline">\$\\pi\_t \\to \\pi\$</span> in TV distance, regardless of <span class="math inline">\$\\pi\_0\$</span> (chain “forgets” <span class="math inline">\$\\pi\_0\$</span>).

Strategy: Find <span class="math inline">\$Q\$</span> with stationary distribution <span class="math inline">\$\\pi(\\theta\|x)\$</span>, start at any <span class="math inline">\$X\_0\$</span>, run chain for a long time, then <span class="math inline">\$X\_t\$</span> is approximately a sample from posterior for large <span class="math inline">\$t\$</span>.

## <span class="header-section-number">3.3</span> Gibbs Sampler {.anchored number="3.3" anchor-id="gibbs-sampler"}

For parameter vector <span class="math inline">\$\\theta = (\\theta\_1, \\ldots, \\theta\_d)\$</span>:

Algorithm: 1. Initialize <span class="math inline">\$\\theta^{(0)}\$</span> 2. For <span class="math inline">\$t = 1, \\ldots, T\$</span>: For <span class="math inline">\$j = 1, \\ldots, d\$</span>: Sample <span class="math inline">\$\\theta\_j^{(t)} \\sim p(\\theta\_j \| \\theta\_{-j}^{(t-1)}, X)\$</span> Record <span class="math inline">\$\\theta^{(t)}\$</span>

Variations: - Update one random coordinate <span class="math inline">\$J \\sim \\text{Unif}(1,\\ldots,d)\$</span> - Update coordinates in random order

Advantage for hierarchical priors: only need to sample low-dimensional conditional distributions:

<span class="math display">\\$$ p(\\theta\_i \| \\theta\_{-i}, X, \\alpha) \\propto p(\\theta\_i \| \\theta\_{\\text{pa}(i)}) \\prod\_{j \\in \\text{ch}(i)} p(\\theta\_j \| \\theta\_i) \\$$</span>

Especially easy if using conjugate priors at all levels; often can be parallelized.

### <span class="header-section-number">3.3.1</span> Gibbs Stationarity {.anchored number="3.3.1" anchor-id="gibbs-stationarity"}

Claim: If <span class="math inline">\$\\pi\_t = \\pi(\\theta\|X)\$</span>, then <span class="math inline">\$\\pi\_{t+1} = \\pi(\\theta\|X)\$</span>.

Proof (sketch): Consider updating only one fixed coordinate <span class="math inline">\$j\$</span>: <span class="math inline">\$\\theta\_j^{(t+1)} \\sim p(\\theta\_j \| \\theta\_{-j}^{(t)}, X)\$</span> If <span class="math inline">\$\\theta^{(t)} \\sim \\pi(\\theta\|X)\$</span>, then <span class="math inline">\$\\theta^{(t+1)} \\sim \\pi(\\theta\|X)\$</span> Updating any coordinate preserves posterior distribution Updating coordinates in any order also does

In theory: Pick initialization and valid kernel <span class="math inline">\$Q\$</span>, sample long enough, get <span class="math inline">\$\\theta^{(t)} \\sim \\pi(\\theta\|X)\$</span> Do it again <span class="math inline">\$N\$</span> more times, get <span class="math inline">\$N\$</span> samples from <span class="math inline">\$\\pi(\\theta\|X)\$</span>

In practice: How do we know we’ve sampled long enough? - Plot <span class="math inline">\$\\theta\_i^{(t)}\$</span> vs <span class="math inline">\$t\$</span>, show how fast the MC mixes - Look for <span class="math inline">\$\\hat{R} = \\frac{\\text{between-chain variance}}{\\text{within-chain variance}} \\approx 1\$</span>

These methods are GOOD, NOT GREAT. Can be deceived, especially for bimodal posteriors.

Better approach: Burn-in then convergence. Estimate posterior based on <span class="math inline">\$\\theta^{(B+1)}, \\ldots, \\theta^{(B+N)}\$</span>

For function <span class="math inline">\$f(\\theta)\$</span>: <span class="math inline">\$\\hat{\\mu}\_f = \\frac{1}{N} \\sum\_{t=B+1}^{B+N} f(\\theta^{(t)})\$</span>

### <span class="header-section-number">3.3.2</span> Implementation Details Matter {.anchored number="3.3.2" anchor-id="implementation-details-matter"}

Example: <span class="math display">\\$$ \\begin{aligned} \\theta &\\sim N(0, 100) \\\\ X\_i \| \\theta &\\sim N(\\theta, 0.1^2), \\quad i=1,\\ldots,n \\end{aligned} \\$$</span>

Posterior: <span class="math inline">\$\\theta \| X \\sim N\\left(\\frac{\\bar{X}/0.01^2}{n/0.01^2 + 1/100}, \\frac{1}{n/0.01^2 + 1/100}\\right)\$</span>

Gibbs sampler: 1. <span class="math inline">\$\\mathbb{E}$$\\theta\|X$$ = 8.9, \\text{SD}(\\theta\|X) = 0.1\$</span> 2. <span class="math inline">\$\\theta^{(t+1)} \| X, \\theta^{(t)} \\sim N(8.9, 0.1^2)\$</span>

Gibbs takes a long time to mix.

Better parameterization: <span class="math display">\\$$ \\begin{aligned} B &= \\theta - \\bar{X} \\\\ \\theta &= B + \\bar{X} \\end{aligned} \\$$</span>

<span class="math inline">\$B\|X \\sim N(0, 0.1^2)\$</span>

Gibbs: Directly sampling from posterior

## <span class="header-section-number">3.4</span> Empirical Bayes {.anchored number="3.4" anchor-id="empirical-bayes"}

Back to Gaussian hierarchical model:

<span class="math display">\\$$ \\begin{aligned} \\theta\_i &\\sim N(\\mu, \\tau^2) \\\\ X\_i \| \\theta\_i &\\sim N(\\theta\_i, \\sigma^2) \\end{aligned} \\$$</span>

<span class="math display">\\$$ \\mathbb{E}\[\\theta\_i \| X, B$$ = \\frac{B - \\sigma^2}{B}X\_i + \\frac{\\sigma^2}{B}\\bar{X}, \\quad B = \\tau^2 + \\sigma^2 \\\]</span>

For any reasonable prior: <span class="math inline">\$B \| X \\approx \\frac{1}{N}\\sum\_{i=1}^N (X\_i - \\bar{X})^2\$</span>

If prior doesn’t matter much, why use one? Could just estimate <span class="math inline">\$B\$</span> from data, however we want.

A minimax estimator is <span class="math inline">\$B = \\sigma^2 + \\frac{1}{N}\\sum\_{i=1}^N (X\_i - \\bar{X})^2\$</span>

Called Empirical Bayes: a hybrid approach in which hyperparameters are treated as fixed, others treated as random.

---

[← 2 Markov Chains {number="2"}](03-2-markov-chains-number-2.md) · [Up: contents](index.md)
