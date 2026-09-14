---
title: Why Bayesian computation is difficult
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/bayes-computation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Why Bayesian computation is difficult

**Source:** [`reader/bayes-computation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/bayes-computation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We have seen simple examples of hierarchical Bayesian models, but one great advantage of Bayesian models is the way they allow us to model complex relationships between many quantities of interest. When performing inference on these quantities, however, the computations required can be difficult.

The primary difficulty in calculating the Bayesian posterior
$$
\lambda(\theta \mid x) = \frac{\lambda(\theta) p_\theta(x)}{\int_{\Theta} \lambda(\zeta)p_\zeta(x)\,d\zeta},
$$
is that the denominator, an integral over a possibly high-dimensional parameter space, can be very difficult to calculate. In our discussion so far we have mostly ignored the denominator, which is only a normalizing constant in $\theta$, because in problems with simple conjugate priors, or more generally in cases with only one or two parameters, the normalization is very easy. However, it is only in rare special cases that we can derive a nice closed form expression for this integral; in most cases, it requires involved calculations. By contrast, even in more complex problems the numerator is relatively easy to calculate.

Much of the work done by Bayesian statisticians is in coming up with efficient ways to calculate posterior probabilities, or sample from the posterior, when we can efficiently compute the numerator but need more help with the denominator. The most common by far is **Markov chain Monte Carlo** (MCMC), a general strategy for sampling from computationally difficult distributions, where the analyst devises a method for sampling a sequence of random variables $\theta^{(0)},\theta^{(1)},\ldots,$ whose distribution converges to the posterior distribution, then uses a well-chosen subset of the $\theta^{(t)}$ variables (for large enough $t$) as a proxy for a sample from the posterior.

---

[Up: contents](index.md) · [Markov chains →](02-markov-chains.md)
