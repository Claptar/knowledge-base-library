---
title: 1 Why Bayesian computation is difficult
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-computation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/bayes-computation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Why Bayesian computation is difficult

1.  [Course Reader](../introduction/index.md)
2.  [Markov Chain Monte Carlo](index.md)

## Markov Chain Monte Carlo {#markov-chain-monte-carlo .title}

$$
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cP}{\mathcal{P}}
\newcommand{\cX}{\mathcal{X}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\td}{\,\textrm{d}}
\newcommand{\simiid}{\stackrel{\textrm{i.i.d.}}{\sim}}
\newcommand{\simind}{\stackrel{\textrm{ind.}}{\sim}}
\newcommand{\eqas}{\stackrel{\textrm{a.s.}}{=}}
\newcommand{\eqPas}{\stackrel{\cP\textrm{-a.s.}}{=}}
\newcommand{\eqmuas}{\stackrel{\mu\textrm{-a.s.}}{=}}
\newcommand{\eqD}{\stackrel{D}{=}}
\newcommand{\indep}{\perp\!\!\!\!\perp}
\DeclareMathOperator*{\minz}{minimize\;}
\DeclareMathOperator*{\maxz}{maximize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
\newcommand{\ep}{\varepsilon}
$$

## 1 Why Bayesian computation is difficult {number="1"}

We have seen simple examples of hierarchical Bayesian models, but one great advantage of Bayesian models is the way they allow us to model complex relationships between many quantities of interest. When performing inference on these quantities, however, the computations required can be difficult.

The primary difficulty in calculating the Bayesian posterior

$$
\lambda(\theta \mid x) = \frac{\lambda(\theta) p_\theta(x)}{\int_{\Theta} \lambda(\zeta)p_\zeta(x)\,d\zeta},
$$

 is that the denominator, an integral over a possibly high-dimensional parameter space, can be very difficult to calculate. In our discussion so far we have mostly ignored the denominator, which is only a normalizing constant in $\theta$, because in problems with simple conjugate priors, or more generally in cases with only one or two parameters, the normalization is very easy. However, it is only in rare special cases that we can derive a nice closed form expression for this integral; in most cases, it requires involved calculations. By contrast, even in more complex problems the numerator is relatively easy to calculate.

Much of the work done by Bayesian statisticians is in coming up with efficient ways to calculate posterior probabilities, or sample from the posterior, when we can efficiently compute the numerator but need more help with the denominator. The most common by far is **Markov chain Monte Carlo** (MCMC), a general strategy for sampling from computationally difficult distributions, where the analyst devises a method for sampling a sequence of random variables $\theta^{(0)},\theta^{(1)},\ldots,$ whose distribution converges to the posterior distribution, then uses a well-chosen subset of the $\theta^{(t)}$ variables (for large enough $t$) as a proxy for a sample from the posterior.

---

[Up: contents](index.md) · [2 Markov chains →](02-2-markov-chains.md)
