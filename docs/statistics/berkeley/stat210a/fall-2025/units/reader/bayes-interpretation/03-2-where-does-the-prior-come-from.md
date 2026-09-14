---
title: 2 Where Does the Prior Come From?
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 2 Where Does the Prior Come From?

**Source:** [`units/reader/bayes-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Bayesian rejoinder: Where does <span class="math inline">\$P\$</span> come from?

Four main sources for prior on <span class="math inline">\$\\theta\$</span>:

### <span class="header-section-number">2.1</span> Source 1: Subjective Beliefs {.anchored number="2.1" anchor-id="source-1-subjective-beliefs"}

Pros: - Brings all relevant info to bear - Straightforward interpretation of posterior

Cons: - Posterior is therefore subjective - Embarrassing to write “I think” in abstract - Hard if <span class="math inline">\$\\theta\$</span> high-dimensional or <span class="math inline">\$P\$</span> nonparametric

Example: Flip coin 20 times, get 7 heads - 0.5 probably a better estimate than 0.35 - My subjective prior on coins:

<span class="math display">\\$$ \\pi(\\theta) \\propto \\theta^{10}(1-\\theta)^{10} \\$$</span>

### <span class="header-section-number">2.2</span> Source 2: Objective or Vague Prior {.anchored number="2.2" anchor-id="source-2-objective-or-vague-prior"}

Pros: - Using default prior removes subjectivity

Cons: - What does the posterior mean?

Examples:

1.  Flat prior: <span class="math inline">\$\\pi(\\theta) \\propto 1\$</span> on <span class="math inline">\$$$0,1$$\$</span>
    - Indifference in <span class="math inline">\$\\theta\$</span> parameterization
    - Often improper, e.g., <span class="math inline">\$\\pi(\\theta) \\propto 1\$</span> on <span class="math inline">\$\\mathbb{R}\$</span>, but usually ok
2.  <span class="math inline">\$\\theta \\in \\mathbb{R}\$</span>, flat prior on <span class="math inline">\$\\mathbb{R}\$</span>
    - <span class="math inline">\$X\|\\theta \\sim N(\\theta, \\sigma^2)\$</span>
    - <span class="math inline">\$\\pi(\\theta\|x) \\propto p(x\|\\theta)\$</span>
    - <span class="math inline">\$\\mathbb{E}$$\\theta\|x$$ = \\bar{x}\$</span>, <span class="math inline">\$\\theta\|x \\sim N(\\bar{x}, \\frac{\\sigma^2}{n})\$</span>
3.  Jeffreys prior: <span class="math inline">\$\\pi(\\theta) \\propto \\sqrt{I(\\theta)}\$</span>
    - Higher density where <span class="math inline">\$p\_\\theta\$</span> changing faster
    - Invariant to parameterization (HW 5)
4.  <span class="math inline">\$X\|\\theta \\sim \\text{Binom}(n, \\theta)\$</span>
    - <span class="math inline">\$\\pi(\\theta) \\propto \\theta^{-1/2}(1-\\theta)^{-1/2} = \\text{Beta}(1/2, 1/2)\$</span>
    - <span class="math inline">\$\\theta \\to 0\$</span> or <span class="math inline">\$1\$</span> as <span class="math inline">\$\\theta \\to 0\$</span> or <span class="math inline">\$1\$</span>

### <span class="header-section-number">2.3</span> Intersubjective Agreement {.anchored number="2.3" anchor-id="intersubjective-agreement"}

Data may effectively rule out most <span class="math inline">\$\\theta\$</span> values, making posterior uncontroversial.

Example: <span class="math inline">\$X \\sim \\text{Binom}(10^4, \\theta)\$</span>, observe <span class="math inline">\$X = 3000\$</span> - SD <span class="math inline">\$\\approx \\sqrt{n} = 10 \\approx 0.005\$</span> - Likelihood <span class="math inline">\$\\theta\|X = 0.3\$</span> outside <span class="math inline">\$$$0.29, 0.31$$\$</span> - All reasonable priors may be <span class="math inline">\$\\approx\$</span> flat on <span class="math inline">\$$$0.29, 0.31$$\$</span> - <span class="math inline">\$\\pi(\\theta\|x) \\propto \\text{Lik}(\\theta\|x) \\approx \\exp(-\\frac{(\\theta - 0.3)^2}{2(0.005)^2})\$</span> - <span class="math inline">\$\\theta\|x \\approx N(0.3, (0.005)^2)\$</span> (HW 5)

Data swamps everyone’s prior.

### <span class="header-section-number">2.4</span> Gaussian Sequence Model {.anchored number="2.4" anchor-id="gaussian-sequence-model"}

<span class="math inline">\$X\|\\theta \\sim N(\\theta, I\_d)\$</span>, <span class="math inline">\$\\theta \\in \\mathbb{R}^d\$</span>

- Jeffreys prior is flat: <span class="math inline">\$\\pi(\\theta) \\propto 1\$</span> on <span class="math inline">\$\\mathbb{R}^d\$</span>
- <span class="math inline">\$\\pi(\\theta\|x) \\propto N(\\theta\|x, I\_d)\$</span>, <span class="math inline">\$\\mathbb{E}$$\\theta\|x$$ = x\$</span>
- Same as UMVU
- What about <span class="math inline">\$\\\|\\theta\\\|\_1\$</span>? Recall:
  - <span class="math inline">\$\\hat{\\mu} = \\arg\\min\_d \\\|\\theta - d\\\|\_1 \\Rightarrow \\hat{\\mu}\_j = \\text{sign}(x\_j)(\|x\_j\| - \\lambda)\_+\$</span>
  - Recall James-Stein: <span class="math inline">\$\\\|\\hat{\\mu}\\\|\_2^2 \\leq \\\|x\\\|\_2^2 - 2d\\lambda + d\\lambda^2\$</span>
  - <span class="math inline">\$\\text{MSE}(\\theta) = \\mathbb{E}$$\\\|\\hat{\\mu} - \\theta\\\|\_2^2$$ = \\text{Var}(\\hat{\\mu}) + \\text{Bias}^2\$</span>
  - <span class="math inline">\$\\text{Var}(\\hat{\\mu}) \\leq d\$</span>, <span class="math inline">\$\\text{Bias}^2 \\leq d\\lambda^2\$</span>

What went wrong? Examine Jeffreys prior: - <span class="math inline">\$P(\\\|\\theta\\\|\_2 \\leq r) = \\text{Vol}(\\text{Ball of radius } r) \\propto r^d\$</span> - <span class="math inline">\$P(\\\|\\theta\\\|\_2 \\geq r) = 1 - cr^d\$</span> - <span class="math inline">\$P(\\\|\\theta\\\|\_2 \\geq \\gamma d^{1/2}) \\approx 1\$</span> for <span class="math inline">\$\\gamma &lt; 1\$</span>

Grows rapidly. Prior expects <span class="math inline">\$\\\|\\theta\\\|\$</span> to be huge.

### <span class="header-section-number">2.5</span> Source 3: Prior or Concurrent Experience {.anchored number="2.5" anchor-id="source-3-prior-or-concurrent-experience"}

- May have many instances of same problem
- Assume true <span class="math inline">\$\\theta\$</span> values drawn from a population
- Hierarchical Bayes / empirical Bayes
- Can be hard to choose right reference class

Example: Estimate batting average - Player <span class="math inline">\$i\$</span> has <span class="math inline">\$n\_i\$</span> at-bats, true batting avg <span class="math inline">\$\\theta\_i\$</span> - Hierarchical model (players <span class="math inline">\$i=1,\\ldots,m\$</span>): - Hyperparameter <span class="math inline">\$\\alpha, \\beta \\sim \\pi\_0(\\alpha, \\beta)\$</span> (hyperprior) - <span class="math inline">\$\\theta\_i\|\\alpha, \\beta \\sim \\text{Beta}(\\alpha, \\beta)\$</span> - <span class="math inline">\$X\_i\|\\theta\_i, n\_i \\sim \\text{Binom}(n\_i, \\theta\_i)\$</span> - <span class="math inline">\$\\theta\_i\|X \\sim \\text{Beta}(\\alpha + X\_i, \\beta + n\_i - X\_i)\$</span> - <span class="math inline">\$\\mathbb{E}$$\\theta\_i\|X$$ = \\frac{\\alpha + X\_i}{\\alpha + \\beta + n\_i}\$</span> - If <span class="math inline">\$m\$</span> large, <span class="math inline">\$\\alpha, \\beta\$</span> may be almost known - Choice of <span class="math inline">\$\\pi\_0\$</span> doesn’t matter much - Reference class problem: which players to include?

### <span class="header-section-number">2.6</span> Flexibility of Bayes {.anchored number="2.6" anchor-id="flexibility-of-bayes"}

Any <span class="math inline">\$(\\pi, P, L, g(\\theta))\$</span> defined straightforwardly: <span class="math display">\\$$ \\delta(x) = \\arg\\min\_d \\int L(\\theta, d) \\pi(\\theta\|x) d\\theta \\$$</span>

- Problem reduced to (possibly hard) computation
- Posterior is one-stop shop for all answers
- No need for:
  - Special family structure (exp fam, completeness)
  - Special estimator (U-estimable)
  - Convex or nice <span class="math inline">\$L\$</span>
- Highly expressive modeling & estimation
- Caveat: Limited by ability to do computations (topic of next lecture)

### <span class="header-section-number">2.7</span> Source 4: Convenience Priors {.anchored number="2.7" anchor-id="source-4-convenience-priors"}

- Choosing conjugate or other nice priors
- Much faster computations, esp. in high dim
- But what does the posterior mean?

Example: - <span class="math inline">\$X\_i \\stackrel{iid}{\\sim} p\$</span>, <span class="math inline">\$p\$</span> unknown density on <span class="math inline">\$\\mathbb{R}\$</span> - Estimand: <span class="math inline">\$m =\$</span> median<span class="math inline">\$(p)\$</span> - Estimator: <span class="math inline">\$\\delta(x) =\$</span> median<span class="math inline">\$(X)\$</span> - Good estimator: robust, nonparametric - Large <span class="math inline">\$n\$</span>: <span class="math inline">\$\\delta(x) \\sim N(m, \\frac{1}{4np(m)^2})\$</span> - Not Bayes for any realistic prior

Bayes approach: 1. Define prior over <span class="math inline">\$p\$</span> (infinite dim) 2. Calculate posterior (horrific unless we pick special prior) 3. Return e.g., <span class="math inline">\$\\mathbb{E}$$m\|X$$\$</span>

If it differs substantially from median<span class="math inline">\$(X)\$</span>, do we trust it?

---

[← 1 Interpretations of Probability](02-1-interpretations-of-probability.md) · [Up: contents](index.md) · [3 Gaussian Hierarchical Model →](04-3-gaussian-hierarchical-model.md)
