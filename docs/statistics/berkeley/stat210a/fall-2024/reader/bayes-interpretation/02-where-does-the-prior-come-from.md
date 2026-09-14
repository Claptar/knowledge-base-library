---
title: Where Does the Prior Come From?
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/bayes-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Where Does the Prior Come From?

**Source:** [`reader/bayes-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/bayes-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Bayesian rejoinder: Where does $P$ come from?

Four main sources for prior on $\theta$:

### Source 1: Subjective Beliefs

Pros:
- Brings all relevant info to bear
- Straightforward interpretation of posterior

Cons:
- Posterior is therefore subjective
- Embarrassing to write "I think" in abstract
- Hard if $\theta$ high-dimensional or $P$ nonparametric

Example: Flip coin 20 times, get 7 heads
- 0.5 probably a better estimate than 0.35
- My subjective prior on coins:

$$
\pi(\theta) \propto \theta^{10}(1-\theta)^{10}
$$

### Source 2: Objective or Vague Prior

Pros:
- Using default prior removes subjectivity

Cons:
- What does the posterior mean?

Examples:

1. Flat prior: $\pi(\theta) \propto 1$ on $[0,1]$
   - Indifference in $\theta$ parameterization
   - Often improper, e.g., $\pi(\theta) \propto 1$ on $\mathbb{R}$, but usually ok

2. $\theta \in \mathbb{R}$, flat prior on $\mathbb{R}$
   - $X|\theta \sim N(\theta, \sigma^2)$
   - $\pi(\theta|x) \propto p(x|\theta)$
   - $\mathbb{E}[\theta|x] = \bar{x}$, $\theta|x \sim N(\bar{x}, \frac{\sigma^2}{n})$

3. Jeffreys prior: $\pi(\theta) \propto \sqrt{I(\theta)}$
   - Higher density where $p_\theta$ changing faster
   - Invariant to parameterization (HW 5)

4. $X|\theta \sim \text{Binom}(n, \theta)$
   - $\pi(\theta) \propto \theta^{-1/2}(1-\theta)^{-1/2} = \text{Beta}(1/2, 1/2)$
   - $\theta \to 0$ or $1$ as $\theta \to 0$ or $1$

### Intersubjective Agreement

Data may effectively rule out most $\theta$ values, making posterior uncontroversial.

Example: $X \sim \text{Binom}(10^4, \theta)$, observe $X = 3000$
- SD $\approx \sqrt{n} = 10 \approx 0.005$
- Likelihood $\theta|X = 0.3$ outside $[0.29, 0.31]$
- All reasonable priors may be $\approx$ flat on $[0.29, 0.31]$
- $\pi(\theta|x) \propto \text{Lik}(\theta|x) \approx \exp(-\frac{(\theta - 0.3)^2}{2(0.005)^2})$
- $\theta|x \approx N(0.3, (0.005)^2)$ (HW 5)

Data swamps everyone's prior.

### Gaussian Sequence Model

$X|\theta \sim N(\theta, I_d)$, $\theta \in \mathbb{R}^d$

- Jeffreys prior is flat: $\pi(\theta) \propto 1$ on $\mathbb{R}^d$
- $\pi(\theta|x) \propto N(\theta|x, I_d)$, $\mathbb{E}[\theta|x] = x$
- Same as UMVU
- What about $\|\theta\|_1$? Recall:
  - $\hat{\mu} = \arg\min_d \|\theta - d\|_1 \Rightarrow \hat{\mu}_j = \text{sign}(x_j)(|x_j| - \lambda)_+$
  - Recall James-Stein: $\|\hat{\mu}\|_2^2 \leq \|x\|_2^2 - 2d\lambda + d\lambda^2$
  - $\text{MSE}(\theta) = \mathbb{E}[\|\hat{\mu} - \theta\|_2^2] = \text{Var}(\hat{\mu}) + \text{Bias}^2$
  - $\text{Var}(\hat{\mu}) \leq d$, $\text{Bias}^2 \leq d\lambda^2$

What went wrong? Examine Jeffreys prior:
- $P(\|\theta\|_2 \leq r) = \text{Vol}(\text{Ball of radius } r) \propto r^d$
- $P(\|\theta\|_2 \geq r) = 1 - cr^d$
- $P(\|\theta\|_2 \geq \gamma d^{1/2}) \approx 1$ for $\gamma < 1$

Grows rapidly. Prior expects $\|\theta\|$ to be huge.

### Source 3: Prior or Concurrent Experience

- May have many instances of same problem
- Assume true $\theta$ values drawn from a population
- Hierarchical Bayes / empirical Bayes
- Can be hard to choose right reference class

Example: Estimate batting average
- Player $i$ has $n_i$ at-bats, true batting avg $\theta_i$
- Hierarchical model (players $i=1,\ldots,m$):
  - Hyperparameter $\alpha, \beta \sim \pi_0(\alpha, \beta)$ (hyperprior)
  - $\theta_i|\alpha, \beta \sim \text{Beta}(\alpha, \beta)$
  - $X_i|\theta_i, n_i \sim \text{Binom}(n_i, \theta_i)$
- $\theta_i|X \sim \text{Beta}(\alpha + X_i, \beta + n_i - X_i)$
- $\mathbb{E}[\theta_i|X] = \frac{\alpha + X_i}{\alpha + \beta + n_i}$
- If $m$ large, $\alpha, \beta$ may be almost known
- Choice of $\pi_0$ doesn't matter much
- Reference class problem: which players to include?

### Flexibility of Bayes

Any $(\pi, P, L, g(\theta))$ defined straightforwardly:
$$
\delta(x) = \arg\min_d \int L(\theta, d) \pi(\theta|x) d\theta
$$

- Problem reduced to (possibly hard) computation
- Posterior is one-stop shop for all answers
- No need for:
  - Special family structure (exp fam, completeness)
  - Special estimator (U-estimable)
  - Convex or nice $L$
- Highly expressive modeling & estimation
- Caveat: Limited by ability to do computations (topic of next lecture)

### Source 4: Convenience Priors

- Choosing conjugate or other nice priors
- Much faster computations, esp. in high dim
- But what does the posterior mean?

Example:
- $X_i \stackrel{iid}{\sim} p$, $p$ unknown density on $\mathbb{R}$
- Estimand: $m =$ median$(p)$
- Estimator: $\delta(x) =$ median$(X)$
  - Good estimator: robust, nonparametric
  - Large $n$: $\delta(x) \sim N(m, \frac{1}{4np(m)^2})$
  - Not Bayes for any realistic prior

Bayes approach:
1. Define prior over $p$ (infinite dim)
2. Calculate posterior (horrific unless we pick special prior)
3. Return e.g., $\mathbb{E}[m|X]$

If it differs substantially from median$(X)$, do we trust it?

---

[← Interpretations of Probability](01-interpretations-of-probability.md) · [Up: contents](index.md) · [Gaussian Hierarchical Model →](03-gaussian-hierarchical-model.md)
