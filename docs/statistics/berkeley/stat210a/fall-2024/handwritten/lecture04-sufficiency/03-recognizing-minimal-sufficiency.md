---
title: Recognizing minimal sufficiency
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-sufficiency.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture04-sufficiency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-sufficiency.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-sufficiency.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Recognizing minimal sufficiency

Assume $\mathcal{P}$ has densities $p_\theta$, sample space $\mathcal{X}$
Define equivalence relation on $\mathcal{X}$:

$$x \equiv_\mathcal{P} y \quad \text{if} \quad \frac{p_\theta(x)}{p_\theta(y)} \text{ doesn't depend on } \theta$$

**Note** any sufficient statistic $T$ can only collapse together equivalent values: if $T(x) = T(y) = t$

$$\frac{p_\theta(x)}{p_\theta(y)} = \frac{P_\theta(X = x, \, T(X) = t)}{P_\theta(X = y, \, T(X) = t)} = \frac{P(X = x \mid T(X) = t)}{P(X = y \mid T(X) = t)}$$

So, for any sufficient stat $T(X)$, $\quad T(x) = T(y) \implies x \equiv_\mathcal{P} y$

---

For minimal sufficient stats, the reverse implication also holds:

**Theorem (Bahadur)** $T(X)$ is minimal sufficient if

$$x \equiv_\mathcal{P} y \iff T(x) = T(y)$$

**Interp**: a minimal sufficient stat. collapses the sample space into exactly these equiv. classes.

**Proof**: First show $T(X)$ sufficient:
For any $x$ with $T(x) = t$, we have

$$P_\theta(X = x \mid T(X) = t) = \frac{p_\theta(x)}{\sum_{z : T(z)=t} p_\theta(z)} = \frac{1}{\sum_{z : T(z)=t} p_\theta(z) / p_\theta(x)}$$

which doesn't depend on $\theta$ because $T(z) = t = T(x) \implies p_\theta(z) / p_\theta(x)$ doesn't depend on $\theta$

Next assume $S(X)$ sufficient. If $S(x) = S(y) = s$ then $x \equiv_\mathcal{P} y$ so $T(x) = T(y)$. Set $f(s) = T(x)$.
Any other $z$ with $S(z) = s$ has
$z \equiv_\mathcal{P} x \implies T(z) = T(x) = f(s) = f(S(z))$. $\quad \square$

---

## (Log-) Likelihood functions

### Definition

Assume $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ has densities $p_\theta(x)$

The **likelihood function** is the (random) function

$$\text{Lik}(\theta; X) = p_\theta(x)$$

- As a function of $\theta$
- data $X$ determines which function
- function of $x$ with parameter $\theta$

The **log-likelihood function** is its $\log$:

$$\ell(\theta; X) = \log \text{Lik}(\theta; X)$$

**Note** if $x \equiv_\mathcal{P} y$ is same as saying
$\ell(\theta; x) - \ell(\theta; y) = \frac{p_\theta(x)}{p_\theta(y)}$ is **constant**

---

**Ex** Laplace location family

$$X_1, \dots, X_n \stackrel{iid}{\sim} p_\theta^{(1)}(x) = \frac{1}{2} e^{-|x-\theta|}$$

$$\ell(\theta; x) = - \sum_{i=1}^n |x_i - \theta| - n \log 2$$

Piecewise linear in $\theta$, knots at $x_{(i)}$

On $[x_{(k)}, x_{(k+1)}]$,
$\text{Slope} = n - 2k$

$$\ell(\theta; x) = \ell(\theta; y) + \text{const} \iff X, Y \text{ same order statistics}$$

$\implies$ order stats are minimal suff.

---

[← Factorization Theorem](02-factorization-theorem.md) · [Up: contents](index.md)
