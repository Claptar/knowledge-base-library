---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture06-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture06-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture06-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture06-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

9/14/23

1) Convex Loss
2) Rao-Blackwell Theorem
3) UMVU Estimators
4) Examples

---

## Unbiased Estimation

**Recall** strategies to choose an estimator

1) Summarize risk by a scalar (avg or sup)
2) Restrict to a smaller class of estimators

**Today:** Unbiased estimation

Require $\mathbb{E}_\theta \delta(X) = g(\theta)$ (estimand), $\forall \theta \in \Theta$

If we have complete sufficient stat $T(X)$,
- there is **at most** one unbiased $\delta^*(T(X))$
  (If $\mathbb{E}_\theta \delta_1(T) = \mathbb{E}_\theta \delta_2(T) = g(\theta) \quad \forall \theta$ then $\delta_1 \stackrel{\text{a.s.}}{=} \delta_2$)
- if it exists, it **uniformly minimizes risk** for any convex loss function

---

## Convex Loss Functions

**Recall** $f(x)$ is **convex** if, for all $x_1, x_2$, all $\gamma \in [0, 1]$

$$f(\gamma x_1 + (1-\gamma)x_2) \le \gamma f(x_1) + (1-\gamma) f(x_2)$$

strictly convex if $<$

**Thm** (Jensen) If $f$ convex then
$$f(\mathbb{E} X) \le \mathbb{E} f(X) \quad \text{for any r.v. } X$$
$f$ strictly convex then $<$ unless $X \stackrel{\text{a.s.}}{=} c$

**Convex Loss** $L(\theta, d)$ means convex **in** $d$

**Ex.**
$$\begin{aligned}
L(\theta, d) &= (g(\theta) - d)^2 \\
MSE(\theta; \delta) &= \mathbb{E}_\theta \left[ (g(\theta) - \delta(X))^2 \right] \\
&= \text{Bias}_\theta^2(\delta) + \text{Var}_\theta(\delta) \\
&= \text{Var}_\theta(T) \quad \text{if } \delta \text{ unbiased}
\end{aligned}$$

Convex losses penalize us for making the estimator too noisy

---

## Rao-Blackwell Theorem

Recipe to improve any $\delta(X)$ that violates the **suff. principle.**

**Theorem** (Rao-Blackwell)

Assume $T(X)$ sufficient, $\delta(X)$ estimator

Let $\bar{\delta}(T(X)) = \mathbb{E} [\delta(X) \mid T(X)]$ (no $\theta$)

If $L(\theta, \delta)$ convex then $R(\theta; \bar{\delta}) \le R(\theta; \delta)$

If strictly convex then $R(\theta; \bar{\delta}) < R(\theta; \delta)$
unless $\delta(X) \stackrel{\text{a.s.}}{=} \bar{\delta}(T(X))$ for all $\theta$

**Proof**
$$\begin{aligned}
R(\theta; \bar{\delta}) &= \mathbb{E}_\theta \left[ L(\theta, \mathbb{E}[\delta \mid T]) \right] \\
&\le \mathbb{E}_\theta \mathbb{E} \left[ L(\theta; \delta) \mid T \right] \\
&= R(\theta; \delta)
\end{aligned}$$
$<$ if strictly, unless $\delta \stackrel{\text{a.s.}}{=} \bar{\delta}$ $\quad \boxtimes$

$\bar{\delta}(T)$ called the **Rao-Blackwellization** of $\delta(X)$

---

## UMVU Estimators

Not all estimands have unbiased estimators:

**Def** We say $g(\theta)$ is **U-estimable** if $\exists\ \delta(X)$ with $\mathbb{E}_\theta \delta = g(\theta)\ \forall \theta$

**Def** $\delta(X)$ is **uniform minimum variance unbiased** (UMVU) if for any unbiased $\tilde{\delta}$,
$$\text{Var}_\theta(\delta(X)) \le \text{Var}_\theta(\tilde{\delta}(X)) \quad \forall \theta \in \Theta$$

**Theorem** For model $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$, assume:
i) $T(X)$ complete suff
ii) $g(\theta)$ U-estimable

Then there exists a unique estimator of the form $\delta^*(T(X))$, which
1) is UMVU and minimizes
2) uniformly minimizes risk among all unbiased estimators

---

## Proof

"All Rao-Blackwellizations lead to $\delta^*$"

**Existence**
Take any $\delta_0$ unbiased for $g(\theta)$
Let $\delta^*(T) = \mathbb{E} [\delta_0 \mid T]$ (no $\theta$)
$$\mathbb{E}_\theta \delta^* = \mathbb{E}_\theta \left[ \mathbb{E}[\delta_0 \mid T] \right] = \mathbb{E}_\theta \delta_0 = g(\theta)$$

**Uniqueness**
If $\delta(T)$ unbiased then
$$\mathbb{E}_\theta [\delta^*(T) - \delta(T)] = 0 \quad \forall \theta \in \Theta$$
$$\implies \delta^*(T) \stackrel{\text{a.s.}}{=} \delta(T) \quad (\text{completeness})$$

**Optimality wrt any convex loss**
Suppose $\delta(X)$ unbiased,
let $\bar{\delta}(T) = \mathbb{E}[X \mid T] \stackrel{\text{a.s.}}{=} \delta^*(T)$ (uniqueness)

Rao-Blackwell:
$$R(\theta; \delta^*) = R(\theta; \bar{\delta}) \le R(\theta; \delta)$$
Hence,
$$MSE(\theta; \delta^*) \le MSE(\theta; \delta)$$
$$\text{Var}_\theta(\delta^*) \le \text{Var}_\theta(\delta)$$
So, $\delta^*$ UMVU $\quad \boxtimes$

---

---

[Up: contents](index.md) · [Finding the UMVUE →](02-finding-the-umvue.md)
