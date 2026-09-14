---
title: Markov Chain Monte Carlo (MCMC)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/hierarchical-bayes.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/hierarchical-bayes.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Markov Chain Monte Carlo (MCMC)

**Source:** [`reader/hierarchical-bayes.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/hierarchical-bayes.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Hierarchical models are very flexible, but often create big computational headaches:

$$
\pi(\theta|x) = \frac{p(x|\theta)\pi(\theta)}{\int p(x|\theta)\pi(\theta)d\theta}
$$

Numerator is usually nice, denominator often intractable.

Computational strategy: Set up a Markov chain with stationary distribution $\pi(\theta|x)$, run it to get approximate samples from $\pi(\theta|x)$.

### Definition of Markov Chain

A stationary Markov chain with transition kernel $Q(y|x)$ and initial distribution $\pi_0(x)$ is a sequence of r.v.'s $X_0, X_1, \ldots$ where $X_0 \sim \pi_0$ and:

$$
P(X_{t+1} \in A | X_t, \ldots, X_0) = P(X_{t+1} \in A | X_t) = \int_A Q(y|X_t) dy
$$

Marginal distribution of $X_t$:

$$
\pi_t(y) = P(X_t \in A) = \int Q(y|x)\pi_{t-1}(x) dx
$$

This is a directed graphical model: $X_0 \to X_1 \to X_2 \to \cdots$

If $\pi(y) = \int Q(y|x)\pi(x) dx$, we say $\pi$ is a stationary distribution for $Q$.

A sufficient condition is detailed balance:

$$
\pi(x)Q(y|x) = \pi(y)Q(x|y)
$$

$$
\int_y Q(y|x)\pi(x) dx = \int_y \pi(y)Q(x|y) dy = \pi(y)
$$

A Markov chain with detailed balance is called reversible: $X_{t-1} | X_t \sim X_{t+1} | X_t$ if $\pi_t = \pi$.

### Theory

If a Markov chain with stationary distribution $\pi$ is:

1. Irreducible: $\forall x,y, \exists n: P(X_n = y | X_0 = x) > 0$
2. Aperiodic: $\forall x, \gcd\{n > 0: P(X_n = x | X_0 = x) > 0\} = 1$

Then $\pi_t \to \pi$ in TV distance, regardless of $\pi_0$ (chain "forgets" $\pi_0$).

Strategy: Find $Q$ with stationary distribution $\pi(\theta|x)$, start at any $X_0$, run chain for a long time, then $X_t$ is approximately a sample from posterior for large $t$.

---

[← Hierarchical Bayes](01-hierarchical-bayes.md) · [Up: contents](index.md) · [Gibbs Sampler →](03-gibbs-sampler.md)
