---
title: 2 Confidence Regions
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/testing-interpretation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 2 Confidence Regions

Definition: $C: \cX \to \cP(\Theta)$ is a $1-\alpha$ confidence set for $g(\theta)$ if:

$$
\mathbb{P}_\theta(C(X) \ni g(\theta)) \geq 1-\alpha \quad \forall \theta \in \Theta
$$

We say $C(x)$ covers $g(\theta)$ if $C(x) \ni g(\theta)$

Coverage probability: $\mathbb{P}_\theta(C(X) \ni g(\theta))$

$\inf_\theta \mathbb{P}_\theta(C(X) \ni g(\theta))$ is confidence level

Note: $C(X)$ is random, not $g(\theta)$

Often misinterpreted as Bayesian guarantee Say “$C(x)$ has a 95% chance of covering” Not “$g(\theta)$ has a 95% chance of being in $C$” NEVER “95% chance $g(\theta) \in [0.5, 1.5]$” e.g.

## 2.1 Duality of Tests/Confidence Sets {.anchored number="2.1" anchor-id="duality-of-testsconfidence-sets"}

Suppose we have a level $\alpha$ test $\phi(\cdot, a)$ of $H_0: g(\theta) = a$ vs $H_1: g(\theta) \neq a$, $\forall a \in \Theta$

We can use it to make a confidence set for $g(\theta)$:

Let $C(X) = \{a: \phi(X, a) = 0\}$ (all non-rejected values of $a$)

Then $\mathbb{P}_\theta(C(X) \ni g(\theta)) = \mathbb{P}_\theta(\phi(X, g(\theta)) = 0) \geq 1-\alpha$

Alternatively, suppose $C(X)$ is a $1-\alpha$ confidence set for $g(\theta)$

We can use $C$ to construct a test $\phi$ of $H_0: g(\theta) = a$ vs $H_1: g(\theta) \neq a$:

$\phi(x) = 1\{a \notin C(x)\}$

For $\theta$ s.t. $g(\theta) = a$:

$$
\mathbb{E}_\theta[\phi(X)] = \mathbb{P}_\theta(a \notin C(X)) = \mathbb{P}_\theta(C(X) \not\ni g(\theta)) \leq \alpha
$$

This is called inverting a test.

## 2.2 Confidence Intervals/Bounds {.anchored number="2.2" anchor-id="confidence-intervalsbounds"}

If $C(X) = [C_L(X), C_U(X)]$, we say: - $C(X)$ is a confidence interval (CI) - $C_L(X)$ is a lower confidence bound (LCB) - $C_U(X)$ is an upper confidence bound (UCB)

We usually get LCB, UCB by inverting a one-sided test in appropriate direction Called uniformly most accurate (UMA) if test UMP

Get CI by inverting a two-sided test Called UMAU if test is UMPU

Example: $X \sim \text{Exp}(\theta)$, $n=1$, $\mathbb{E}[X] = \frac{1}{\theta}$, $\theta > 0$

CDF: $\mathbb{P}_\theta(X \leq x) = 1 - e^{-\theta x}$

LCB: Invert test for $H_0: \theta \leq \theta_0$ Solve $\alpha = 1 - \mathbb{P}_{\theta_0}(X \leq x) = e^{-\theta_0 x}$

$\theta_0 = -\frac{1}{x}\log(\alpha)$

$C_L(X) = -\frac{1}{X}\log(\alpha)$, $\mathbb{P}_\theta(\theta \geq C_L(X)) = 1-\alpha$

UCB: Similar $C_U(X) = -\frac{1}{X}\log(1-\alpha)$

Equal-tailed: Invert equal-tailed test of $H_0: \theta = \theta_0$

$\theta_0 e^{-\theta_0 x} = \frac{\alpha}{2}$, $1 - e^{-\theta_0 x} = 1 - \frac{\alpha}{2}$

$C(X) = [\frac{-\log(\alpha/2)}{X}, \frac{-\log(\alpha/2)}{X}]$

Similar for UMPU 2-sided test

---

[← 1 p-Values](01-1-p-values.md) · [Up: contents](index.md) · [3 Misinterpreting Hypothesis Tests →](03-3-misinterpreting-hypothesis-tests.md)
