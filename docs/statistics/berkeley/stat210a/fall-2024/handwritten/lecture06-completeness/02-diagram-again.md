---
title: Diagram again
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture06-completeness.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture06-completeness.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture06-completeness.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture06-completeness.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Diagram again

```
η_2 ^
    |       s = 2
    |
    |                   (A) Full Rank       (B) Curved
    |                   //////                  (Minimal)
    |                  (//////)               _
    |                                        /
    |                       (C)             |
    |                       /               ~
    |                      /
    |                 γ   / Not minimal
    |                  * /  (Full-rank for s=1)
    |
    +----------------------------------------------------> η_1
```
(Within $\Xi$, represented as an oval region)

$T(X)$ definitely complete for (A)

Maybe not for (B), (C)

---

**Theorem** If $T(X)$ complete sufficient for $\mathcal{P}$ then $T(X)$ is minimal.

Game plan for completeness proofs: show two things are a.s. equal by showing they have = expectation.

**Proof** Assume $S(X)$ is minimal suff.

Let $\bar{T}(S(X)) = \mathbb{E}[T(X) \mid S(X)]$ (since $S$ suff.)

Claim: $\bar{T}(S(X)) \stackrel{\text{a.s.}}{=} T(X)$

We have $S(X) \stackrel{\text{a.s.}}{=} f(T(X))$ ($S$ minimal suff)

Let $g(t) = t - \bar{T}(f(t))$
$$\mathbb{E}_\theta[g(T(X))] = \mathbb{E}_\theta T(X) - \mathbb{E}_\theta[\bar{T}(S(X))]$$
$$= \mathbb{E}_\theta T(X) - \mathbb{E}_\theta[\mathbb{E}[T \mid S]]$$
$$= 0$$
$$\implies g(T(X)) \stackrel{\text{a.s.}}{=} 0 \quad \text{(completeness)}$$
$$\tag*{$\boxtimes$}$$

---

## Ancillarity

Two reasons to care about completeness:
1) Uniqueness of unbiased estimators using $T$
   $$\text{If } \mathbb{E}_\theta \delta_1(T) = \mathbb{E}_\theta \delta_2(T) = g(\theta), \ \forall \theta \in \Theta$$
   $$\text{Then } \mathbb{E}_\theta[\delta_1 - \delta_2] = 0 \implies \delta_1 \stackrel{\text{a.s.}}{=} \delta_2$$
   [We will explore this further next time]
2) Basu's theorem: neat way to show independence

**Def** $V(X)$ is **ancillary** for $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ if its distribution does not depend on $\theta$. ($V$ carries no info. about $\theta$)

### (Aside:) Conditionality Principle
If $V(X)$ is ancillary then all inference should be conditional on $V(X)$
[Will return to this in testing & CI unit]

---

## Basu's Theorem

**Theorem** (Basu)
If $T(X)$ is complete sufficient and $V(X)$ is ancillary for $\mathcal{P}$, then
$$V(X) \perp\!\!\!\perp T(X) \quad \text{for all } \theta \in \Theta$$

**Proof**
Want $\mathbb{P}(V \in A, T \in B) = \mathbb{P}(V \in A) \mathbb{P}_\theta(T \in B)$ all $A, B, \theta$

Let $q_A(T(X)) = \mathbb{P}(V \in A \mid T)$ (since $T$ suff.)
$$p_A = \mathbb{P}(V \in A) \quad \text{($V$ ancillary)}$$

$$\mathbb{E}_\theta[q_A(T) - p_A] = p_A - p_A = 0, \quad \forall \theta$$
$$\implies q_A(T) \stackrel{\text{a.s.}}{=} p_A \quad \forall \theta$$

$$\mathbb{P}_\theta(V \in A, T \in B) = \int q_A(t) \mathbf{1}\{t \in B\} \, dP_\theta^T(t)$$
$$= p_A \int \mathbf{1}\{t \in B\} \, dP_\theta^T(t)$$
$$= \mathbb{P}(V \in A) \mathbb{P}_\theta(T \in B) \tag*{$\boxtimes$}$$

---

## Using Basu's Theorem

Ancillarity, Completeness, Sufficiency are all properties wrt a family $\mathcal{P}$

Independence is a property of a **distribution**

If you can't verify the thm's hypotheses for one family, try a different family!

**Ex.** $X_1, \dots, X_n \stackrel{\text{iid}}{\sim} N(\mu, \sigma^2) \quad \mu \in \mathbb{R}, \ \sigma^2 > 0$

**Sample mean** $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$

**Sample variance** $S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$

Want to show $\bar{X} \perp\!\!\!\perp S^2$

But neither stat. is ancillary or sufficient in the full family with $\mu, \sigma^2$ unknown

To apply Basu, use family with $\sigma^2$ known:
$$\mathcal{P} = \{N(\mu, \sigma^2)^n : \mu \in \mathbb{R}\}$$

---

In $\mathcal{P}$, $\bar{X}$ is complete sufficient and $S^2$ is ancillary since
$$S^2 = \sum (Z_i - \bar{Z})^2 \quad \text{for } Z_i = X_i - \mu \stackrel{\text{iid}}{\sim} N(0, \sigma^2)$$
(not statistics but doesn't matter)

Therefore $\bar{X} \perp\!\!\!\perp S^2$

[Conclusion has nothing to do with "known" or "unknown" parameters]

---

[← Completeness](01-completeness.md) · [Up: contents](index.md)
