---
title: Lecture 5
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture05-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture05-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture05-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture05-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture 5

9/12/2023

## Outline
1) Completeness
2) Ancillarity
3) Basu's Theorem

---

## Completeness

**Def** $T(X)$ is complete for $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$

if $\mathbb{E}_\theta f(T(X)) = 0 \quad \forall \theta$

$\implies f(T) \overset{\text{a.s.}}{=} 0 \quad \forall \theta$

[Name comes from a prior notion that $\mathcal{P}^T = \{P_\theta^T : \theta \in \Theta\}$ is "complete basis" wrt inner product $\langle f, P_\theta^T \rangle = \int f(t) \, dP_\theta^T(t)$ (see HW 3)]

**Ex.** (Cont'd) Laplace location family has minimal suff stat $S = (X_{(i)})_{i=1}^n$. Complete?

No: Let $M(S) = \text{median}(X)$
$$\bar{X}(S) = \frac{1}{n} \sum X_i$$

$$\mathbb{E}_\theta \bar{X} = \mathbb{E}_\theta M = \theta \quad (\text{by symmetry})$$

$$\mathbb{E}_\theta [\bar{X}(S) - M(S)] = 0 \quad \forall \theta$$

$S(X)$ still has "a lot of extra fluff"

---

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} \mathcal{U}[0, \theta] \quad \theta \in (0, \infty)$

Can show $T(X) = X_{(n)}$ min. suff. Complete?

Find density of $T(X)$:
$$\mathbb{P}_\theta(T \le t) = \left(\frac{t}{\theta} \wedge 1\right)^n = \left(\frac{t}{\theta}\right)^n \wedge 1$$
$$\implies p_\theta(t) = \frac{d}{dt} \mathbb{P}_\theta(T \le t)$$
$$= n \frac{t^{n-1}}{\theta^n} \mathbf{1}\{t \le \theta\}$$

Suppose $0 = \mathbb{E}_\theta f(T) \quad \forall \theta > 0$
$$= \frac{n}{\theta^n} \int_0^\theta f(t) t^{n-1} \, dt \quad \forall \theta > 0$$
$$\implies \int_0^\theta f(t) t^{n-1} \, dt = 0 \quad \forall \theta > 0$$
$$\implies f(t) t^{n-1} = 0 \quad \text{a.e. } t > 0$$

---

**Def** Assume $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$ has densities
$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$

If $T(X)$ satisfies no linear constraint ($\nexists\ \beta \ne 0, \alpha : \beta' T(X) \overset{\text{a.s.}}{=} \alpha$) and $\Xi$ contains an open set, we say $\mathcal{P}$ is **full-rank**.

If $\mathcal{P}$ is not full-rank we say it is curved.

[Note: If $T(x)$ satisfies linear constraint, then $\mathcal{P}$ might still be full-rank for a lower-dim. sufficient statistic]

**Theorem** If $\mathcal{P}$ is full rank then $T(X)$ is complete sufficient.

Proof in Lehmann & Romano, Thm. 4.3.1

**Proof idea** wlog $T(X) = X$, $p_\eta(x) = e^{\eta' x - A(\eta)}$, $0 \in \Xi^\circ$ (interior)

Write $f(x) = f^+(x) - f^-(x)$, for $f^+, f^- \ge 0$

$$\int e^{\eta' x} \underbrace{f^+(x) \, d\mu(x)}_{d\tilde{\nu}^+(x)} = \int e^{\eta' x} \underbrace{f^-(x) \, d\mu(x)}_{d\tilde{\nu}^-(x)} \quad \text{Both MGFs}$$

Uniqueness of MGFs $\implies f^+ = f^-$

---

$s = 2$

$\eta_2 \uparrow$ vs $\eta_1 \rightarrow$

In parameter space $\Xi$:
- Region (A) is a shaded disk labeled "Full Rank"
- Region (B) is a curved line labeled "Curved"
- Region (C) is a line segment labeled "Full-rank ($s=1$)"

---

**Theorem** If $T(X)$ complete sufficient for $\mathcal{P}$ then $T(X)$ is minimal.

Game plan for completeness proofs: show two things are a.s. equal by showing they have $=$ expectation.

**Proof** Assume $S(X)$ is minimal suff.

Let $\bar{T}(S(X)) = \mathbb{E}[T(X) \mid S(X)]$ (subscript $\theta$ crossed out: as $S$ suff.)

Claim: $\bar{T}(S(X)) \overset{\text{a.s.}}{=} T(X)$

We have $S(X) \overset{\text{a.s.}}{=} f(T(X))$ ($S$ minimal suff)

Let $g(t) = t - \bar{T}(f(t))$
$$\mathbb{E}_\theta [g(T(X))] = \mathbb{E}_\theta T(X) - \mathbb{E}_\theta [\bar{T}(S(X))]$$
\$\$= \mathbb{E}_\theta T(X) - \mathbb{E

---

[Up: contents](../index.md)
