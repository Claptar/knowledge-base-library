---
title: Sufficiency
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture04-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Sufficiency

9/5/2023

### Outline

1) Review
2) Sufficiency
3) Factorization Theorem

---

### Motivation: Coin flipping

Suppose $X_1, \dots, X_n \overset{\text{iid}}{\sim} \text{Bernoulli}(\theta)$

$\Rightarrow X \sim \prod_i \theta^{X_i}(1-\theta)^{1-X_i}$ on $\{0, 1\}^n$

Then $T(X) = \sum X_i \sim \text{Binom}(n, \theta)$

$= \theta^t (1-\theta)^{n-t} \binom{n}{t}$ on $\{0, \dots, n\}$

$(X_1, \dots, X_n) \to T(X)$ is throwing away data. How do we justify this?

In exp. fam. lingo, $T(X)$ is the "sufficient statistic" for $X$. Today we'll see why we call it that.

### Definition

Let $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ be a statistical model for data $X$. $T(X)$ is **sufficient** for $\mathcal{P}$ if $P_\theta(X \mid T)$ does not depend on $\theta$.

### Example (cont'd)

$$P_\theta(X = x \mid T = t) = \frac{P_\theta(X = x, \, T = t)}{P_\theta(T = t)}$$

$$= \frac{\theta^{\sum x_i} (1-\theta)^{n - \sum x_i} \mathbf{1}\{\sum x_i = t\}}{\theta^t (1-\theta)^{n-t} \binom{n}{t}}$$

$$= \mathbf{1}\{\sum x_i = t\} / \binom{n}{t}$$

So given $T(X) = t$, $X$ is uniform on all seq.s with $\sum x_i = t$.

---

## Factorization Theorem

Often, we can identify sufficient stats by inspecting the density.

### Theorem (Factorization Theorem)

Let $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ be a model with densities $p_\theta(x)$ wrt common measure $\mu$.

$T(X)$ is sufficient iff there exist $g_\theta(t)$, $h(x)$ with

$$p_\theta(x) = g_\theta(T(x)) \, h(x)$$

for $\mu$-almost-every $x$ : $\mu(\{x : p_\theta(x) \neq g_\theta(T(x)) \cdot h(x)\}) = 0$

[Avoids counterexamples from changing $p_{\theta_0}(x_0)$ some $\theta_0, x_0$]

Rigorous proof in Keener 6.4

---

### **Proof (discrete $\mathcal{X}$):** Assume wlog $\mu = #$ on $\mathcal{X}$

$(\Leftarrow)$

$$P_\theta(X = x \mid T = t) = \frac{P_\theta(X = x, \, T(x) = t)}{P_\theta(T(x) = t)}$$

$$= \frac{g_\theta(t) \, h(x) \, \mathbf{1}\{T(x) = t\}}{\sum_{T(z) = t} g_\theta(t) \, h(z)}$$

$(\Rightarrow)$ Assume $T(x)$ sufficient.

Take $g_\theta(t) = \sum_{T(x) = t} p_\theta(x)$

$$= P_\theta(T(X) = t)$$

For any $\theta_0 \in \Theta$, let

$$h(x) = p_{\theta_0}(x) \Big/ \sum_{T(z) = T(x)} p_{\theta_0}(z)$$

$$= P_{\theta_0}(X = x \mid T(X) = T(x))$$
$$\hspace{1.5cm} \nwarrow \text{no dep. on } \theta$$

Then,

$$g_\theta(T(x)) \, h(x) = P_\theta(T = T(x)) \, P(X = x \mid T = T(x))$$

$$= P_\theta(X = x) \quad \square$$

---

## Interpretations of Sufficiency

$X$ is informative about $\theta$ only because its distribution depends on $\theta$.

We can think of the data as being generated in two stages:

1) Generate $T$ : distribution dep. on $\theta$
2) Generate $X \mid T$ : does not dep. on $\theta$

### Sufficiency Principle

If $T(X)$ is sufficient for $\mathcal{P}$ then any statistical procedure should depend on $X$ only through $T(X)$

In fact, we could throw away $X$ and generate a new $\tilde{X} \sim P(X \mid T)$ (no $\theta$) and it would be just as good as $X$ since $\tilde{X} \sim P_\theta$

In graphical model form:

$\theta \xrightarrow{\text{Step 1}} T(X) \xrightarrow{\text{Step 2}} X$

$\text{Fake Step 2} \searrow \tilde{X}$

- From $T(X) \to X$: No reason to pay any attention
- From $\tilde{X}$: Just as good as $X$

---

## Examples

### **Ex.** Exponential Families

$$p_\theta(x) = \underbrace{e^{\eta(\theta)' T(x) - B(\theta)}}_{g_\theta(T(x))} \underbrace{h(x)}_{h(x)}$$

### **Ex.** Uniform location family

\$\$X_1, \dots, X_n \overset{\text{iid}}{\sim} U

---

[Up: contents](../index.md)
