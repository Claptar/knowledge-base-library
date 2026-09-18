---
title: Completeness
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture06-completeness.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture06-completeness.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture06-completeness.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture06-completeness.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Completeness

### Outline

1) Completeness
2) Ancillarity
3) Basu's Theorem

---

**Def** $T(X)$ is complete for $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ if
$$\mathbb{E}_\theta f(T(X)) = 0 \quad \forall \theta \implies f(T) \overset{\text{a.s.}}{=} 0 \quad \forall \theta$$

[Name comes from a prior notion that $\mathcal{P}^T = \{P_\theta^T : \theta \in \Theta\}$ is "complete basis" w.r.t inner product $\langle f, P_\theta^T \rangle = \int f(t)\, dP_\theta^T(t)$ (see HW 3)]

**Ex.** (Cont'd) Laplace location family has minimal suff stat $S = (X_{(i)})_{i=1}^n$. Complete?

No: Let $M(S) = \text{median}(X)$
$$\bar{X}(S) = \frac{1}{n} \sum X_i$$

$$\mathbb{E}_\theta \bar{X} = \mathbb{E}_\theta M = \theta \quad (\text{by symmetry})$$
$$\mathbb{E}_\theta [\bar{X}(S) - M(S)] = 0 \quad \forall \theta$$

$S(X)$ still has "a lot of extra fluff"

---

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} \mathcal{U}[0, \theta] \quad \theta \in (0, \infty)$

$$p_\theta(x) = \prod_i \frac{1}{\theta} \mathbf{1}\{x_i \le \theta\} = \frac{1}{\theta^n} \mathbf{1}\{X_{(n)} \le \theta\}$$

$$\frac{p_\theta(x)}{p_\theta(y)} = \frac{\mathbf{1}\{x_{(n)} \le \theta\}}{\mathbf{1}\{y_{(n)} \le \theta\}}$$

$$\implies T(X) = X_{(n)} \text{ minimal suff.}$$

Find density of $T(X)$
$$\mathbb{P}_\theta(T \le t) = \left(\frac{t}{\theta} \wedge 1\right)^n = \left(\frac{t}{\theta}\right)^n \wedge 1$$
$$\implies p_\theta(t) = \frac{d}{dt} \mathbb{P}_\theta(T \le t) = n \frac{t^{n-1}}{\theta^n} \mathbf{1}\{t \le \theta\}$$

Suppose
$$0 = \mathbb{E}_\theta f(T) \quad \forall \theta > 0$$
$$= \frac{n}{\theta^n} \int_0^\theta f(t) t^{n-1}\, dt \quad \forall \theta > 0$$
$$\implies \int_0^\theta f(t) t^{n-1}\, dt = 0 \quad \forall \theta > 0$$
$$\implies f(t) t^{n-1} = 0 \quad \text{a.e. } t > 0$$

---

**Def** Assume $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$ has densities
$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$

If $T(X)$ satisfies no linear constraint $\left(\nexists\ \beta \ne 0, \alpha : \beta' T(X) \overset{\text{a.s.}}{=} \alpha\right)$ and $\Xi$ contains an open set, we say $\mathcal{P}$ is **full-rank**.

If $\mathcal{P}$ is not full-rank we say it is curved.

[Note: If $T(X)$ satisfies linear constraint, then $\mathcal{P}$ might still be full-rank for a lower-dim. sufficient statistic]

*Proof in Lehmann & Romano, Thm. 4.3.1*

**Theorem** If $\mathcal{P}$ is full rank then $T(X)$ is complete sufficient

Proof uses uniqueness of mgfs

---

**Proof** (Canonical form) $p_\eta(x) = e^{\eta' x - A(\eta)}$

Assume wlog $0 \in \Xi^\circ$, $A(0) = 0$

Suppose $\mathbb{P}_0(f(X) \ne 0) > 0 \quad (\iff \mathbb{P}_\eta(\cdot) > 0\ \forall \eta)$
and $\mathbb{E}_\eta f(X) = 0 \quad \forall\ \eta \in \Xi$

Write $f(x) = f^+(x) - f^-(x)$, for $f^+, f^- \ge 0$
$$\implies \mathbb{E}_\eta f^+(X) = \mathbb{E}_\eta f^-(X) \quad \forall \eta$$
$$\implies \int e^{\eta' x} f^+(x)\, d\mu(x) = \int e^{\eta' x} f^-(x)\, d\mu(x)$$

MGFs for r.v.s $Y^+ \sim f^+$, $Y^- \sim f^-$
(wlog $\int f^+ d\mu = \int f^- d\mu = 1$)

Uniqueness of MGFs $\implies Y^+ \overset{\mathcal{D}}{=} Y^- \implies f^+ \overset{\text{a.s.}}{=} f^-$

But $f^+(x) = f^-(x)$ only if $f(x) = 0$
$\blacksquare$

---

## Diagram again

$s=2$

- $\Xi_1$
- (A) Full Rank
- (B) Curved (Minimal)
- (C) Not minimal (Full-rank for $s=1$)

$T(X)$ definitely complete for (A)
Maybe not for (B), (C)

(Converse not true: could be complete suff for all 3)

---

**Theorem** If $T(X)$ complete sufficient for $\mathcal{P}$ then $T(X)$ is minimal

*Game plan for completeness proofs: show two things are a.s. equal by showing they have = expectation.*

**Proof** Assume $S(X)$ is minimal suff

Let $\bar{T}(S(X)) = \mathbb{E}_{\cancel{\theta}}[T(X) \mid S(X)]$ (since $S$ suff.)

Claim: $\bar{T}(S(X)) \overset{\text{a.s.}}{=} T(X)$

We have $S(X) \overset{\text{a.s.}}{=} f(T(X))$ ($S$ minimal suff)

Let $g(t) = t - \bar{T}(f(t))$

$$\mathbb{E}_\theta [g(T(X))] = \mathbb{E}_\theta T(X) - \mathbb{E}_{\cancel{\theta}}[\bar{T}(S(X))]$$
$$= \mathbb{E}_\theta T(X) - \mathbb{E}_\theta [\mathbb{E}[T \mid S]]$$
$$= 0$$
$$\implies g(T(X)) \overset{\text{a.s.}}{=} 0 \quad (\text{completeness})$$
$\blacksquare$

---

## Ancillarity

Two reasons to care about completeness:
1) Uniqueness of unbiased estimators using $T$
If $\mathbb{E}_\theta \delta_1(T) = \mathbb{E}_\theta \delta_2(T) = g(\theta), \ \forall \theta \in \Theta$
Then $\mathbb{E}_\theta[\delta_1 - \delta_2] = 0 \implies \delta_1 \overset{\text{a.s.}}{=} \delta_2$
[We will explore this further next time]
2) Basu's theorem: neat way to show independence

**Def** $V(X)$ is **ancillary** for $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ if its distribution does not depend on $\theta$. ($V$ carries no info. about $\theta$)

**(Aside:) Conditionality Principle**
If $V(X)$ is ancillary then all inference should be conditional on $V(X)$
[will return to this in testing & CI unit]

---

## Basu's Theorem

**Theorem (Basu)**
If $T(X)$ is complete sufficient and $V(X)$ is ancillary for $\mathcal{P}$, then
$$V(X) \perp\!\!\!\perp T(X) \quad \text{for all } \theta \in \Theta$$

**Proof**
Want $\mathbb{P}_\theta(V \in A, T \in B) = \mathbb{P}(V \in A) \mathbb{P}_\theta(T \in B)$ all $A, B, \theta$

Let
$$q_A(T(X)) = \mathbb{P}_{\cancel{\theta}}(V \in A \mid T) \quad (\text{T suff.})$$
$$p_A = \mathbb{P}_{\cancel{\theta}}(V \in A) \quad (\text{V ancillary})$$

$$\mathbb{E}_\theta [q_A(T) - p_A] = p_A - p_A = 0, \quad \forall \theta$$
$$\implies q_A(T) \overset{\text{a.s.}}{=} p_A \quad \forall \theta$$

$$\mathbb{P}_\theta(V \in A, T \in B) = \int_B q_A(t) \mathbf{1}\{t \in B\}\, dP_\theta^T(t)$$
$$= p_A \int \mathbf{1}\{t \in B\}\, dP_\theta^T(t)$$
$$= \mathbb{P}(V \in A) \mathbb{P}_\theta(T \in B) \quad \blacksquare$$

---

## Using Basu's Theorem

Ancillarity, Completeness, Sufficiency are all properties w.r.t a family $\mathcal{P}$

Independence is a property of a **distribution**

If you can't verify the thm's hypotheses for one family, try a different family!

**Ex.** $X_1, \dots, X_n \overset{\text{iid}}{\sim} \mathcal{N}(\mu, \sigma^2) \quad \mu \in \mathbb{R}, \sigma^2 > 0$

**Sample mean** $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$

**Sample variance** $S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2$

Want to show $\bar{X} \perp\!\!\!\perp S^2$

But neither stat. is ancillary or sufficient in the full family with $\mu, \sigma^2$ unknown.

To apply Basu, use family with $\sigma^2$ known:
$$\mathcal{P} = \{\mathcal{N}(\mu, \sigma^2)^n : \mu \in \mathbb{R}\}$$

---

In $\mathcal{P}$, $\bar{X}$ is complete sufficient and $S^2$ is ancillary since
$$S^2 = \sum (Z_i - \bar{Z})^2 \quad \text{for } Z_i = X_i - \mu \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$$
(not statistics, but doesn't matter)

Therefore $\bar{X} \perp\!\!\!\perp S^2$

[Conclusion has nothing to do with "known" or "unknown" parameters]

---

[Up: contents](../index.md)
