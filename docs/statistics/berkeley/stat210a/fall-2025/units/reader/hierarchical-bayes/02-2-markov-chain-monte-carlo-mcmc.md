---
title: 2 Markov Chain Monte Carlo (MCMC)
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hierarchical-bayes.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/hierarchical-bayes.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hierarchical-bayes.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Markov Chain Monte Carlo (MCMC)

Hierarchical models are very flexible, but often create big computational headaches:

$$
\pi(\theta|x) = \frac{p(x|\theta)\pi(\theta)}{\int p(x|\theta)\pi(\theta)d\theta}
$$

Numerator is usually nice, denominator often intractable.

Computational strategy: Set up a Markov chain with stationary distribution $\pi(\theta|x)$, run it to get approximate samples from $\pi(\theta|x)$.

## 2.1 Definition of Markov Chain {.anchored number="2.1" anchor-id="definition-of-markov-chain"}

A stationary Markov chain with transition kernel $Q(y|x)$ and initial distribution $\pi_0(x)$ is a sequence of r.v.’s $X_0, X_1, \ldots$ where $X_0 \sim \pi_0$ and:

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

## 2.2 Theory {.anchored number="2.2" anchor-id="theory"}

If a Markov chain with stationary distribution $\pi$ is:

1.  Irreducible: $\forall x,y, \exists n: P(X_n = y | X_0 = x) > 0$
2.  Aperiodic: $\forall x, \gcd\{n > 0: P(X_n = x | X_0 = x) > 0\} = 1$

Then $\pi_t \to \pi$ in TV distance, regardless of $\pi_0$ (chain “forgets” $\pi_0$).

Strategy: Find $Q$ with stationary distribution $\pi(\theta|x)$, start at any $X_0$, run chain for a long time, then $X_t$ is approximately a sample from posterior for large $t$.

---

[← 1 Hierarchical Bayes](01-1-hierarchical-bayes.md) · [Up: contents](index.md) · [3 Gibbs Sampler →](03-3-gibbs-sampler.md)
