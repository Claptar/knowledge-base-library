---
title: 1 Frequentist motivation for a Bayes Estimator
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Frequentist motivation for a Bayes Estimator

1.  [Course Reader](../introduction/index.md)
2.  [Bayes Estimation](index.md)

## Bayes Estimation {#bayes-estimation .title}

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

### 1 Frequentist motivation for a Bayes Estimator {.anchored number="1" anchor-id="frequentist-motivation-for-a-bayes-estimator"}

We will motivate Bayes estimation first as a strategy for selecting an estimator in the setting of [Lecture 2](../estimation/index.md). Recall that, when we discussed possible strategies for choosing between different admissible estimators, we suggested using the *average-case risk* to reduce the risk function to a scalar summary. This average must be taken with respect to some measure $\Lambda$ on the parameter space $\Theta$, which we will call the *prior*.

That is, for an estimator $\delta$ we can define the average-case or *Bayes risk* with respect to $\Lambda$:

$$
r_\Lambda(\delta) = \int_\Theta R(\theta; \delta)\,d\Lambda(\theta).
$$

 An estimator $\delta_\Lambda$ that minimizes the Bayes risk is called a *Bayes estimator*. If $\Lambda(\Theta) = \infty$, we call the prior *improper*, and otherwise we assume $\Lambda$ is normalized so that $\Lambda(\Theta) = 1$. Then, $\Lambda$ is a probability measure; in that case we call it *proper*, and the integral can be rewritten as an expectation

$$
r_\Lambda(\delta) = \EE_{\theta \sim \Lambda}[R(\theta; \delta)] = \EE[L(\theta, \delta(X))],
$$

 where the last expectation is taken with respect to the *joint distribution* where $\theta \sim \Lambda$ and $X \mid \theta \sim P_\theta$. The key to finding a Bayes estimator is to calculate the conditional distribution of $\theta$ given $X$, which we call the *posterior*.

The prior will commonly be represented by a density $\lambda(\theta)$, giving the joint density $\lambda(\theta)p_\theta(x)$. Then the marginal distribution of $X$ is $q(x) = \int_\Theta p_\theta(x)\lambda(\theta)\,d\theta$, and the posterior density is given by Bayes’ rule:

$$
\lambda(\theta \mid x) = \frac{\lambda(\theta) p_\theta(x)}{q(x)}.
$$

The names “prior” and “posterior” evoke a natural epistemic interpretation that the prior represents our subjective beliefs about $\theta$ before we observe the data, and the posterior our beliefs afterward. But nothing about the mathematical formulation of the problem requires that we endorse these interpretations: even if we are dogmatic frequentists, or if we are using a $\Lambda$ that doesn’t really correspond to anyone’s subjective prior beliefs, the expectation still makes sense as a mathematically equivalent expression to the average-case risk.

---

[Up: contents](index.md) · [2 Bayes estimator →](02-2-bayes-estimator.md)
