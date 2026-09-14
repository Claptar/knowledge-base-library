---
title: 1 Why Bayesian computation is difficult
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-computation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Why Bayesian computation is difficult

**Source:** [`reader/bayes-computation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

We have seen simple examples of hierarchical Bayesian models, but one great advantage of Bayesian models is the way they allow us to model complex relationships between many quantities of interest. When performing inference on these quantities, however, the computations required can be difficult.

The primary difficulty in calculating the Bayesian posterior <span class="math display">\\$$ \\lambda(\\theta \\mid x) = \\frac{\\lambda(\\theta) p\_\\theta(x)}{\\int\_{\\Theta} \\lambda(\\zeta)p\_\\zeta(x)\\,d\\zeta}, \\$$</span> is that the denominator, an integral over a possibly high-dimensional parameter space, can be very difficult to calculate. In our discussion so far we have mostly ignored the denominator, which is only a normalizing constant in <span class="math inline">\$\\theta\$</span>, because in problems with simple conjugate priors, or more generally in cases with only one or two parameters, the normalization is very easy. However, it is only in rare special cases that we can derive a nice closed form expression for this integral; in most cases, it requires involved calculations. By contrast, even in more complex problems the numerator is relatively easy to calculate.

Much of the work done by Bayesian statisticians is in coming up with efficient ways to calculate posterior probabilities, or sample from the posterior, when we can efficiently compute the numerator but need more help with the denominator. The most common by far is **Markov chain Monte Carlo** (MCMC), a general strategy for sampling from computationally difficult distributions, where the analyst devises a method for sampling a sequence of random variables <span class="math inline">\$\\theta^{(0)},\\theta^{(1)},\\ldots,\$</span> whose distribution converges to the posterior distribution, then uses a well-chosen subset of the <span class="math inline">\$\\theta^{(t)}\$</span> variables (for large enough <span class="math inline">\$t\$</span>) as a proxy for a sample from the posterior.

---

[← Markov Chain Monte Carlo](01-markov-chain-monte-carlo.md) · [Up: contents](index.md) · [2 Markov chains →](03-2-markov-chains.md)
