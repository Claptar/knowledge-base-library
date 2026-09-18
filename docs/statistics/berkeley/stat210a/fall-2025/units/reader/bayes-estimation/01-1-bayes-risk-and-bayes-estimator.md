---
title: 1 Bayes Risk and Bayes Estimator
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/bayes-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Bayes Risk and Bayes Estimator

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
\DeclareMathOperator*{\maxz}{minimize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
$$

## 1 Bayes Risk and Bayes Estimator {.anchored number="1" anchor-id="bayes-risk-and-bayes-estimator"}

### 1.1 Definitions {.anchored number="1.1" anchor-id="definitions"}

The Bayes risk is the average case risk:

$$
r(\pi, \delta) = \EE_\pi[R(\theta, \delta)] = \int R(\theta, \delta) \,d\pi(\theta)
$$

where $\pi(\theta)$ is a probability measure (for now, we assume it’s proper; later we will allow it to be improper).

Note: $\pi$ and $\delta$ are functionally equivalent for average risk, which makes sense even if we don’t believe $\pi$.

$$
r(\pi, \delta) = \EE_\pi[\EE_\theta[L(\theta, \delta(X))]] = \EE[L(\theta, \delta(X))]
$$

where $(\theta, X) \sim p(\theta, x) = p(x|\theta)\pi(\theta)$

An estimator $\delta$ minimizing $r_\text{Bayes}(\delta)$ is called a Bayes estimator. It depends on $\pi$ and $L$.

$$
\delta_\pi = \argmin_\delta \EE[L(\theta, \delta(X))]
$$

### 1.2 Prior and Posterior {.anchored number="1.2" anchor-id="prior-and-posterior"}

- The usual interpretation of $\pi$ is the prior belief about $\theta$ before seeing the data.
- The conditional distribution $\pi(\theta|X)$ is called the posterior distribution (belief after seeing the data).

Densities: - Prior: $\pi(\theta)$ - Likelihood: $p(x|\theta)$ - Joint density: $p(\theta, x) = \pi(\theta)p(x|\theta)$ - Marginal density: $q(x) = \int p(\theta, x) \,d\theta$ - Posterior density: $\pi(\theta|x) = \frac{p(\theta, x)}{q(x)}$

The Bayes estimator depends on the posterior:

$$
\delta_\pi(x) = \argmin_d \EE[L(\theta, d)|X=x] = \argmin_d \int L(\theta, d) \pi(\theta|x) \,d\theta
$$

### 1.3 Theorem: Characterization of Bayes Estimators {.anchored number="1.3" anchor-id="theorem-characterization-of-bayes-estimators"}

Suppose $X \sim p_\theta(x)$ and $\delta_\pi(x) = \delta(x)$ for some function $\delta$. Then $\delta$ is Bayes with respect to $\pi$ if and only if $\delta(x) \in \argmin_d \EE[L(\theta, d)|X=x]$ for almost every $x$.

Proof: 1. Let $\delta'$ be any other estimator. 2. $r(\pi, \delta') = \int \EE[L(\theta, \delta'(X))|X=x] q(x) \,dx$ 3. $r(\pi, \delta) = \int \EE[L(\theta, \delta(X))|X=x] q(x) \,dx$ 4. Define $E_x(d) = \EE[L(\theta, d)|X=x]$ 5. If $\delta(x) \in \argmin_d E_x(d)$, then $E_x(\delta(x)) \leq E_x(\delta'(x))$ for all $x$ 6. This implies $r(\pi, \delta) \leq r(\pi, \delta')$

## 2 Special Cases and Examples {.anchored number="2" anchor-id="special-cases-and-examples"}

### 2.1 Squared Error Loss {.anchored number="2.1" anchor-id="squared-error-loss"}

If $L(\theta, d) = (\theta - d)^2$, then the Bayes estimator is the posterior mean:

$$
\delta_\pi(x) = \EE[\theta|X=x]
$$

Proof:

$$
\begin{aligned}
\EE[(\theta - d)^2|X=x] &= \EE[\theta^2|X=x] - 2d\EE[\theta|X=x] + d^2 \\
&= \Var(\theta|X=x) + (\EE[\theta|X=x] - d)^2 + \EE[\theta|X=x]^2 - 2d\EE[\theta|X=x] + d^2
\end{aligned}
$$

The minimum occurs when $d = \EE[\theta|X=x]$.

### 2.2 Weighted Squared Error {.anchored number="2.2" anchor-id="weighted-squared-error"}

For $L(\theta, d) = w(\theta)(\theta - d)^2$ (e.g., squared relative error), the Bayes estimator is:

$$
\delta_\pi(x) = \frac{\EE[w(\theta)\theta|X=x]}{\EE[w(\theta)|X=x]}
$$

---

[Up: contents](index.md) · [3 Examples →](02-3-examples.md)
