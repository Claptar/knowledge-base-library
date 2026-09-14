---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework2.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework2.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework2.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework2.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

The natural parameter space for any exponential family (meaning the set of all parameters $\eta$ that give normalizable densities) is a convex subset of $\mathbb{R}^s$.

**Problem 3** (Expectation of an increasing function).

1.  Assume $X\sim P$ is a real-valued random variable. Show that if $f(x)$ and $g(x)$ are non-decreasing functions of $x$, then $$\text{Cov}(f(X),g(X)) \geq 0$$ **Hint**: first show $\mathbb{E}\left[(f(X_1)-f(X_2))(g(X_1)-g(X_2))\right] = 2\text{Cov}(f(X_1),g(X_1))$, where $X_1,X_2\overset{\text{i.i.d.}}{\sim}P$.

2.  Let $p_\eta(x)$ be a one-parameter canonical exponential family with non-decreasing sufficient statistic $T(x)$, where $x\in\mathcal{X}\subseteq \mathbb{R}$: $$p_\eta(x) = e^{\eta T(x) - A(\eta)}h(x).$$ Let $\psi(x)$ be any non-decreasing bounded function. Show that, for $\eta\in\Xi_1^\circ$, the interior of the natural parameter space, $\frac{d}{d \eta}\mathbb{E}_{\eta}[\psi(X)] \geq 0$.

    **Hint**: find an expression for $\frac{d}{d \eta} \mathbb{E}_{\eta}[\psi(X)]$ by using methods akin to the ones we used in class to derive the differential identities. You may assume it is justified to differentiate under the integral sign.

3.  Conclude that $X$ is stochastically increasing in $\eta$; that is, show $\mathbb{P}_\eta(X \leq c)$ is non-increasing in $\eta$, for every $c \in \mathbb{R}$.

---

[← Moral](02-moral.md) · [Up: contents](index.md) · [Moral →](04-moral.md)
