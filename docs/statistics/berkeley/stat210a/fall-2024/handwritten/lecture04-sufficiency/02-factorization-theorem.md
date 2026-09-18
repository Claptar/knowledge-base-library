---
title: Factorization Theorem
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-sufficiency.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture04-sufficiency.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture04-sufficiency.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture04-sufficiency.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Factorization Theorem

Usually, we can recognize sufficient stats by inspecting the density.

**Theorem (Factorization Theorem)**

Let $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ be a model with densities $p_\theta(x)$ wrt common measure $\mu$.

$T(X)$ is sufficient iff there exist $g_\theta(t)$, $h(x) \ge 0$ with

$$p_\theta(x) = g_\theta(T(x)) \, h(x) \quad (\text{for } \mu\text{-a.e. } x)$$

**Note** we could absorb $h$ into $\mu$ as density
(define new base measure $\nu$, $\nu(A) = \int_A h(x) d\mu(x)$)
$\implies \mathcal{P}$ has densities $p_\theta(x) = g_\theta(T(x))$ wrt $\nu$

**Interp**: after changing base measure, density depends on $x$ only through $T(x)$

(Can't absorb $g_\theta(T(x))$ into $\mu$: depends on $\theta$)

---

**Proof (discrete $\mathcal{X}$)**: Assume wlog $\mu = #$ on $\mathcal{X}$

$(\Leftarrow)$ $P_\theta(X = x \mid T = t) = \frac{P_\theta(X = x, \, T(X) = t)}{P_\theta(T(X) = t)}$

$$= \frac{g_\theta(t) \, h(x) \, \mathbf{1}\{T(x) = t\}}{\sum_{T(z)=t} g_\theta(t) \, h(z)}$$

$(\Rightarrow)$ Assume $T(X)$ sufficient, let
$g_\theta(t) = P_\theta(T(X) = t)$
$h(x) = P(X = x \mid T(X) = T(x))$ (no dep. on $\theta$)

$\implies g_\theta(T(x)) \, h(x) = P_\theta(T(X) = T(x) \text{ and } X = x)$
$= P_\theta(X = x) = p_\theta(x)$ $\quad \square$

Proof similar for general densities
- careful about conditioning in cts spaces

---

## Examples

**Ex.** Normal location family

$$X_1, \dots, X_n \stackrel{iid}{\sim} N(\theta, 1) = \frac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2/2}$$

$$p_\theta(x) = (2\pi)^{-n/2} \prod_{i=1}^n e^{-(x_i-\theta)^2/2}$$

$$= e^{\theta \sum x_i - n\theta^2/2} \cdot \frac{e^{-\sum x_i^2/2}}{(2\pi)^{n/2}} \quad (\text{collect factors with no dep. on } \theta)$$

$\implies \sum X_i$ is sufficient

**Ex.** Poisson family

$$X_1, \dots, X_n \stackrel{iid}{\sim} \text{Pois}(\theta) = \frac{\theta^x e^{-\theta}}{x!} \quad \text{for } x = 0, 1, 2, \dots$$

$$p_\theta(x) = \prod_{i=1}^n \frac{\theta^{x_i} e^{-\theta}}{x_i!} = \theta^{\sum x_i} e^{-n\theta} \cdot \frac{1}{\prod x_i!}$$

$\implies \sum X_i$ is sufficient

These two examples have something important in common!
(next lecture)

**Ex.** Uniform location family

$$X_1, \dots, X_n \stackrel{iid}{\sim} U[\theta, \theta + 1] = \mathbf{1}\{\theta \le x \le \theta + 1\}$$

$$p_\theta(x) = \prod_{i=1}^n \mathbf{1}\{\theta \le x_i \le \theta + 1\}$$

$$= \mathbf{1}\{\theta \le X_{(1)}\} \, \mathbf{1}\{X_{(n)} \le \theta + 1\}$$

$\implies (X_{(1)}, X_{(n)})$ is sufficient.

---

## Interpretations of Sufficiency

$X$ is informative about $\theta$ only because its distribution depends on $\theta$.

We can think of the data as being generated in two stages:
1) Generate $T$: distribution dep. on $\theta$
2) Generate $X \mid T$: does not dep on $\theta$

### Sufficiency Principle

If $T(X)$ is sufficient for $\mathcal{P}$ then any statistical procedure should depend on $X$ only through $T(X)$

In fact, we could throw away $X$ and generate a new $\tilde{X} \sim P(X \mid T)$ (no $\theta$) and it would be just as good as $X$ since $\tilde{X} \sim P_\theta$

In graphical model form:

* Step 1: $\theta \longrightarrow T(X)$
* Step 2: $T(X) \longrightarrow X$ (No reason to pay any attention)
* Fake step 2: $T(X) \longrightarrow \tilde{X}$ (Just as good as $X$)

---

## Order Statistics

For $x_1, \dots, x_n \in \mathbb{R}$, define order statistics
$\min_i x_i = X_{(1)} \le X_{(2)} \le \dots \le X_{(n)} = \max_i X_i$

**Ex** (iid sampling on $\mathbb{R}$) $X_1, \dots, X_n \stackrel{iid}{\sim} P_\theta$,
any model $\mathcal{P} = \{P_\theta^n : \theta \in \Theta\}$ on $\mathcal{X} \subseteq \mathbb{R}$

$P_\theta^n$ invariant to perm.s of $X = (X_1, \dots, X_n)$
$\implies$ All permutations of $x$ are equally likely
$\implies$ Order statistics $S(X) = (X_{(i)})_{i=1}^n$ sufficient

$X \mapsto S(X)$ forgets orig. ordering of observations

---

## Empirical Distribution

Order statistics depend on total ordering of $\mathcal{X}$
What about more general sample space?

Define **Dirac measure** $\delta_x(A) = \mathbf{1}\{x \in A\}$

**Empirical distribution** $\hat{P}_n(\cdot) = \frac{1}{n} \sum_{i=1}^n \delta_{X_i}(\cdot)$
random measure on $\mathcal{X}$, determined by sample

For example, $\hat{P}_n(A) = \frac{3}{5}$

**Ex** (iid sampling) $X_1, \dots, X_n \stackrel{iid}{\sim} P_\theta$
any model $\mathcal{P} = \{P_\theta^n : \theta \in \Theta\}$ on any $\mathcal{X}$

$\hat{P}_n$ is sufficient

$X \mapsto \hat{P}_n$ records which values observed, how many times

---

## Minimal Sufficiency

Consider $X_1, \dots, X_n \stackrel{iid}{\sim} N(\theta, 1)$

$T(X) = \sum X_i$ sufficient
$\bar{X} = \frac{1}{n} \sum X_i$ also
$S(X) = (X_{(1)}, \dots, X_{(n)})$ too
$X = (X_1, \dots, X_n)$ too

Which can be recovered from which others?

```
      X  <------- these can be compressed further
     / \
    /   \
   v     v
  |     S(X) <--- these can be compressed further
  |      / \
  v     v   v
\sum X_i <-> \bar{X} <--- These are the most compressed.
                          Are they as compressed as possible?
```

---

**Prop** If $T(X)$ is sufficient and $T(X) = f(S(X))$ then $S(X)$ is sufficient

**Proof**: $p_\theta(x) = g_\theta(T(x)) \, h(x) = (g_\theta \circ f)(S(x)) \, h(x) \quad \square$

**Definition**: $T(X)$ is **minimal sufficient** if
1) $T(X)$ is sufficient
2) For any other sufficient $S(X)$, $T(X) = f(S(X))$ for some $f$ (a.s. in $\mathcal{P}$)

So, no matter how many more suff. stats we add to our diagram, they will all have arrows pointing to $\sum X_i$

---

---

[← Sufficiency](01-sufficiency.md) · [Up: contents](index.md) · [Recognizing minimal sufficiency →](03-recognizing-minimal-sufficiency.md)
