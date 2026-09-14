---
title: 'Moral 2: {#moral-2}'
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework3.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework3.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral 2: {#moral-2}

**Source:** [`homework/homework3.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework3.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

If $\mathcal{P}= \{P_\eta:\; \eta \in \Xi\}$ is a full-rank exponential family with natural parameter $\eta$, meaning $\Xi$ contains an open set, our result from class allows us to prove completeness of $T(X)$. But the converse is far from true: it is possible for $T$ to be complete if $\Xi$ is discrete, or even finite.

**Problem 4** (Ancillarity in location-scale families).

In a parameterized family where $\theta = (\zeta, \lambda)$, we say a statistic $T$ is *ancillary for $\zeta$* if its distribution is independent of $\zeta$; that is, if $T(X)$ is ancillary in the subfamily where $\lambda$ is known, for each possible value of $\lambda$.

Suppose that $X_1,\ldots,X_n\in \mathcal{X}=\mathbb{R}$ are an i.i.d. sample from a *location-scale family* $\mathcal{P}= \{F_{a,b}(x) = F((x-a)/b): \; a\in \mathbb{R}, b>0\}$, where $F(\cdot)$ is a known cumulative distribution function. The real numbers $a$ and $b$ are called the *location* and *scale* parameters respectively.

**Note:** It is *not* enough to prove ancillarity of the coordinates; the joint distribution of the statistic shouldn’t depend on the relevant parameter.

1.  Show that the vector of differences $\left(X_1 - X_i\right)_{i = 2}^n$ is ancillary for $a$.

2.  Show that the vector of ratios $\left(\frac{X_1 - a}{X_i - a}\right)_{i=2}^n$ is ancillary for $b$. (Note: this is only a statistic when $a$ is known).

3.  **Optional:** (Not graded, no extra points) Show that the vector of difference ratios $\left(\frac{X_1 - X_i}{X_2 - X_i}\right)_{i=3}^n$ is ancillary for $(a,b)$.

4.  Let $X_1,\ldots,X_n$ be mutually independent with $X_i \sim \text{Gamma}(k_i, \theta)$. Show that $X_+ = \sum_{i=1}^n X_i$ is independent of $(X_1,\ldots,X_n)/X_+$.

---

[← Moral 1: {#moral-1}](03-moral-1-moral-1.md) · [Up: contents](index.md) · [Moral: {#moral-3} →](05-moral-moral-3.md)
