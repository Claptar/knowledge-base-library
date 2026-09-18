---
title: Outline
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture07-unbiased.pdf
source_file: sources/berkeley-stat210a/fall-2026/handwritten/lecture07-unbiased.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture07-unbiased.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/handwritten/lecture07-unbiased.pdf) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Outline

1) Convex Loss
2) Rao-Blackwell Theorem
3) UMVU Estimators
4) Examples

---

## Unbiased Estimation

**Recall** strategies to choose an estimator

1) Summarize risk by a scalar (avg or sup)
2) Restrict to a smaller class of estimators

**Today**: Unbiased estimation

Require $\mathbb{E}_\theta \delta(X) = g(\theta)$, $\forall \theta \in \Theta$ (where $g(\theta)$ is the estimand)

If we have complete sufficient stat $T(X)$,
* there is **at most** one unbiased $\delta^*(T(X))$
  (If $\mathbb{E}_\theta \delta_1(T) = \mathbb{E}_\theta \delta_2(T) = g(\theta)$ $\forall \theta$ then $\delta_1 \stackrel{a.s.}{=} \delta_2$)
* if it exists, it **uniformly minimizes** risk for any convex loss function

---

## Convex Loss Functions

**Recall** $f(x)$ is **convex** if, for all $x_1, x_2$, all $\gamma \in [0,1]$

$$f(\gamma x_1 + (1-\gamma) x_2) \le \gamma f(x_1) + (1-\gamma) f(x_2)$$

strictly convex if $<$

**$\underline{\text{Thm}}$** (Jensen) If $f$ convex then
$$f(\mathbb{E} X) \le \mathbb{E} f(X) \quad \text{for any r.v. } X$$
$f$ strictly convex then $<$ unless $X \stackrel{a.s.}{=} c$

**$\underline{\text{Convex Loss}}$** $L(\theta, d)$ means convex **in $d$**

**$\underline{\text{Ex.}}$** $L(\theta, d) = (g(\theta) - d)^2$
$$\begin{aligned}
MSE(\theta; \delta) &= \mathbb{E}_\theta [(g(\theta) - \delta(X))^2] \\
&= \text{Bias}_\theta^2(\delta) + \text{Var}_\theta(\delta) \\
&= \text{Var}_\theta(T) \quad \text{if } \delta \text{ unbiased}
\end{aligned}$$

Convex losses penalize us for making the estimator too noisy

---

## Rao-Blackwell Theorem

Recipe to improve any $\delta(X)$ that violates the suff. principle.

**$\underline{\text{Theorem}}$ (Rao-Blackwell)**
Assume $T(X)$ sufficient, $\delta(X)$ estimator
Let $\bar{\delta}(T(X)) = \mathbb{E}[\delta(X) \mid T(X)]$ (no $\theta$)

If \$L(\theta, \

---

[Up: contents](../index.md)
