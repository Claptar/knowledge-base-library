---
title: Completeness
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture06-completeness.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture06-completeness.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture06-completeness.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture06-completeness.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Completeness

## Outline
1) Completeness
2) Ancillarity
3) Basu's Theorem

---

**Def** $T(X)$ is complete for $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ if
$$\mathbb{E}_\theta f(T(X)) = 0 \quad \forall \theta$$
$$\implies f(T) \stackrel{a.s.}{=} 0 \quad \forall \theta$$

[Name comes from a prior notion that $\mathcal{P}^T = \{P_\theta^T : \theta \in \Theta\}$ is "complete basis" wrt inner product $\langle f, P_\theta^T \rangle = \int f(t) \, dP_\theta^T(t)$ (see HW 3)]

**Ex.** (Cont'd) Laplace location family has minimal suff stat. $S = (X_{(i)})_{i=1}^n$. Complete?

No: Let $M(S) = \text{median}(X)$
$$\bar{X}(S) = \frac{1}{n} \sum X_i$$

$$\mathbb{E}_\theta \bar{X} = \mathbb{E}_\theta M = \theta \quad \text{(by symmetry)}$$

$$\mathbb{E}_\theta [\bar{X}(S) - M(S)] = 0 \quad \forall \theta$$

$S(X)$ still has "a lot of extra fluff"

---

**Ex.** $X_1, \dots, X_n \stackrel{\text{iid}}{\sim} U[0, \theta] \quad \theta \in (0, \infty)$

Can show $T(X) = X_{(n)}$ min. suff. Complete?

Find density of $T(X)$:
$$P_\theta(T \le t) = \left(\frac{t}{\theta} \wedge 1\right)^n = \left(\frac{t}{\theta}\right)^n \wedge 1$$
$$\implies p_\theta(t) = \frac{d}{dt} P_\theta(T \le t)$$
$$= n \frac{t^{n-1}}{\theta^n} \mathbf{1}\{t \le \theta\}$$

Suppose $0 = \mathbb{E}_\theta f(T) \quad \forall \theta > 0$
$$= \frac{n}{\theta^n} \int_0^\theta f(t) t^{n-1} \, dt \quad \forall \theta > 0$$
$$\implies \int_0^\theta f(t) t^{n-1} \, dt = 0 \quad \forall \theta > 0$$
$$\implies f(t) t^{n-1} = 0 \quad \text{a.e. } t > 0$$

---

**Def** Assume $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$ has densities
$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$$

If $T(X)$ satisfies no linear constraint $\left(\nexists\ \beta \ne 0, \alpha : \beta' T(X) \stackrel{\text{a.s.}}{=} \alpha\right)$ and $\Xi$ contains an open set, we say $\mathcal{P}$ is **full-rank**.

If $\mathcal{P}$ is not full-rank we say it is curved.

[Note: If $T(x)$ satisfies linear constraint, then $\mathcal{P}$ might still be full-rank for a lower-dim. sufficient statistic]

Proof in Lehmann & Romano, Thm. 4.3.1

**Theorem** If $\mathcal{P}$ is full rank then $T(X)$ is complete sufficient.

**Proof idea** wlog $T(X) = X$, $p_\eta(x) = e^{\eta' x - A(\eta)}$, $0 \in \Xi^\circ$ (interior)

Write $f(x) = f^+(x) - f^-(x)$, for $f^+, f^- \ge 0$
$$\int e^{\eta' x} f^+(x) \, d\mu(x) = \int e^{\eta' x} f^-(x) \, d\mu(x)$$

$$\text{MGF for } Y^+ \sim \frac{f^+(x)}{\int f^+ d\mu} \qquad \text{MGF for } Y^- \sim \frac{f^-(x)}{\int f^- d\mu}$$

$$\text{Uniqueness of MGFs} \implies Y^+ \stackrel{\mathcal{D}}{=} Y^- \implies f^+ \stackrel{\text{a.s.}}{=} f^-$$

---

---

[Up: contents](index.md) · [Diagram again →](02-diagram-again.md)
