---
title: Gibbs Sampler
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/hierarchical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/hierarchical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Gibbs Sampler

**Source:** [`reader/hierarchical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/hierarchical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

For parameter vector $\theta = (\theta_1, \ldots, \theta_d)$:

Algorithm:
1. Initialize $\theta^{(0)}$
2. For $t = 1, \ldots, T$:
   For $j = 1, \ldots, d$:
     Sample $\theta_j^{(t)} \sim p(\theta_j | \theta_{-j}^{(t-1)}, X)$
   Record $\theta^{(t)}$

Variations:
- Update one random coordinate $J \sim \text{Unif}(1,\ldots,d)$
- Update coordinates in random order

Advantage for hierarchical priors: only need to sample low-dimensional conditional distributions:

$$
p(\theta_i | \theta_{-i}, X, \alpha) \propto p(\theta_i | \theta_{\text{pa}(i)}) \prod_{j \in \text{ch}(i)} p(\theta_j | \theta_i)
$$

Especially easy if using conjugate priors at all levels; often can be parallelized.

### Gibbs Stationarity

Claim: If $\pi_t = \pi(\theta|X)$, then $\pi_{t+1} = \pi(\theta|X)$.

Proof (sketch):
Consider updating only one fixed coordinate $j$: $\theta_j^{(t+1)} \sim p(\theta_j | \theta_{-j}^{(t)}, X)$
If $\theta^{(t)} \sim \pi(\theta|X)$, then $\theta^{(t+1)} \sim \pi(\theta|X)$
Updating any coordinate preserves posterior distribution
Updating coordinates in any order also does

In theory: Pick initialization and valid kernel $Q$, sample long enough, get $\theta^{(t)} \sim \pi(\theta|X)$
Do it again $N$ more times, get $N$ samples from $\pi(\theta|X)$

In practice: How do we know we've sampled long enough?
- Plot $\theta_i^{(t)}$ vs $t$, show how fast the MC mixes
- Look for $\hat{R} = \frac{\text{between-chain variance}}{\text{within-chain variance}} \approx 1$

These methods are GOOD, NOT GREAT. Can be deceived, especially for bimodal posteriors.

Better approach: Burn-in then convergence. Estimate posterior based on $\theta^{(B+1)}, \ldots, \theta^{(B+N)}$

For function $f(\theta)$: $\hat{\mu}_f = \frac{1}{N} \sum_{t=B+1}^{B+N} f(\theta^{(t)})$

### Implementation Details Matter

Example:
$$
\begin{aligned}
\theta &\sim N(0, 100) \\
X_i | \theta &\sim N(\theta, 0.1^2), \quad i=1,\ldots,n
\end{aligned}
$$

Posterior: $\theta | X \sim N\left(\frac{\bar{X}/0.01^2}{n/0.01^2 + 1/100}, \frac{1}{n/0.01^2 + 1/100}\right)$

Gibbs sampler:
1. $\mathbb{E}[\theta|X] = 8.9, \text{SD}(\theta|X) = 0.1$
2. $\theta^{(t+1)} | X, \theta^{(t)} \sim N(8.9, 0.1^2)$

Gibbs takes a long time to mix.

Better parameterization:
$$
\begin{aligned}
B &= \theta - \bar{X} \\
\theta &= B + \bar{X}
\end{aligned}
$$

$B|X \sim N(0, 0.1^2)$

Gibbs: Directly sampling from posterior

---

[← Markov Chain Monte Carlo (MCMC)](02-markov-chain-monte-carlo-mcmc.md) · [Up: contents](index.md) · [Empirical Bayes →](04-empirical-bayes.md)
