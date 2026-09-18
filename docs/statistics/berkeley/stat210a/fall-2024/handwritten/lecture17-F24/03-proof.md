---
title: Proof
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture17-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Proof

Assume $\phi$ any unbiased test

**Step 1:** $\mathbb{E}_{\theta, \lambda} |\phi(X)| \le 1 < \infty \quad \forall (\theta, \lambda) \in \Omega$
$\overset{(\text{Keener Thm 2.4})}{\Rightarrow} \mathbb{E}_{\theta, \lambda} \phi(X)$ infinitely diff. on $\Omega$, can diff. under $\int$
$\phi$ unbiased $\Rightarrow \mathbb{E}_{\theta_0, \lambda} [\phi(X)] = \alpha \quad \forall (\theta_0, \lambda) \in \Omega$

**Step 2: Boundary submodel:** $\mathcal{P}_{\theta_0} = \{ P_{\theta_0, \lambda} : (\theta_0, \lambda) \in \Omega \}$
$$P_{\theta_0, \lambda}(x) = e^{\lambda' U(x) - A(\theta_0, \lambda)} \cdot \frac{e^{\theta_0 T(x)}}{h(x)}$$
$\mathcal{P}_{\theta_0}$ is full-rank, $s$-param exp. fam, $U(X)$ comp. suff.

Let $f(u) = \mathbb{E}_{\theta_0} [\phi(X) \mid U(X) = u] - \alpha$
$$\mathbb{E}_{\theta_0, \lambda} [f(U(X))] = \mathbb{E}_{\theta_0, \lambda} [\phi(X)] - \alpha = 0 \quad \forall \lambda$$
$$\Rightarrow f(u) \overset{\text{a.s.}}{=} 0$$
$$\Rightarrow \mathbb{E}_{\theta_0} [\phi(X) \mid U(X) = u] = 0 \quad \forall u$$

**Two-sided case:**
$$\begin{aligned}
g(u) &= \frac{d}{d\theta} \mathbb{E}_{\theta_0} [\phi \mid U = u] \\
&= \mathbb{E}_{\theta_0} [(T - \mathbb{E}_{\theta_0}[T \mid U]) \phi \mid U] \\
&= \mathbb{E}_{\theta_0} [T(\phi - \alpha) \mid U]
\end{aligned}$$
$$\mathbb{E}_{\theta_0, \lambda} g(U) = \mathbb{E}_{\theta_0, \lambda} [T(\phi - \alpha)] = \frac{\partial}{\partial \theta} \beta_\phi(\theta_0) = 0 \, \forall \lambda$$
$$\Rightarrow \frac{d}{d\theta} \mathbb{E}_{\theta_0} [\phi \mid U] \overset{\text{a.s.}}{=} 0 \quad (\text{cond'l power has derivative } 0 \text{ at } \theta_0)$$

---

**Step 3:** For any value $u$, the conditional model is
$$q_\theta(t \mid u) = e^{\theta t - B_u(\theta)} g(t, u), \quad \text{1-param. exp. fam}$$

In one- / two-sided case, we have shown $\psi(t; u)$ is UMP / UMPU in $\mathcal{Q}_u$

Let $\bar{\phi}(t; u) = \mathbb{E}[\phi(X) \mid T(X) = t, U(X) = u]$
$$\begin{aligned}
\mathbb{E}_{\theta_0} [\bar{\phi}(T; u) \mid U = u] &= \mathbb{E}_{\theta_0} [\phi(X) \mid U(X) = u] \\
&= \alpha \quad \text{if } \theta = \theta_0
\end{aligned}$$
$\Rightarrow \bar{\phi}(\cdot; u)$ is a (cond'l) test of $H_0$ vs. $H_1$ in $\mathcal{Q}_u$ with $\text{power} = \alpha$ at boundary (or $\theta \le \theta_0$)

**One-sided case:**
$\psi(t; u)$ is the UMP test of $\theta = \theta_0$ vs $\theta > \theta_0$ in $\mathcal{Q}_u$, which is a 1-param. exp. fam.

**Two-sided case:**
$\psi(t; u)$ is the UMP test of $\theta = \theta_0$ vs. $\theta \ne \theta_0$ among tests with $\text{power} = \alpha$, $\frac{d}{d\theta} \text{power} = 0$ @ $\theta_0$
(Keener Thm 12.22, main thm. for two-sided tests)

In either case $\psi$ has higher **cond.** power than $\bar{\phi}$, a.s.

---

For $(\theta, \lambda) \in \Omega_1$:
$$\begin{aligned}
\mathbb{E}_{\theta, \lambda} [\phi(X)] &= \mathbb{E}_{\theta, \lambda} [ \, \mathbb{E}_\theta [ \, \bar{\phi}(T; U) \mid U \, ] \, ] \\
&\le \mathbb{E}_{\theta, \lambda} [ \, \mathbb{E}_\theta [ \, \psi(T; U) \mid U \, ] \, ] \\
&= \mathbb{E}_{\theta, \lambda} [\phi^*(X)]
\end{aligned}$$

---

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} N(\mu, \sigma^2) \qquad \sigma^2 > 0 \quad \text{unknown}$

$H_0 : \mu = 0 \quad \text{vs.} \quad H_1 : \mu \ne 0$

$$p_{\mu, \sigma^2}(x) = e^{\overbrace{\frac{\mu}{\sigma^2}}^\theta \overbrace{\sum X_i}^{T = \bar{X}} - \overbrace{\frac{1}{2\sigma^2}}^\lambda \overbrace{\sum X_i^2}^{u = \|X\|^2} - \frac{n\mu^2}{2\sigma^2}} \cdot \left(\frac{1}{2\pi\sigma^2}\right)^{n/2}$$

Optimal test rejects when $\bar{X}$ is extreme given $\|X\|$

If $\mu = 0$, $p$ is rotationally symmetric
$$\Rightarrow X / \|X\|^2 = u \overset{H_0}{\sim} \text{Unif}\left(\sqrt{u} \cdot S^{n-1}\right)$$
$$\left(\Leftrightarrow \frac{X}{\|X\|} \overset{H_0}{\sim} \text{Unif}(S^{n-1}), \quad \text{indep. of } \|X\|\right)$$

Optimal test rejects when $\frac{\bar{X}}{\|X\|}$ extreme (marginally)

Could stop here & simulate

---

## Geometric Picture ($n = 2$)

```
          X₂ ^
             |                   /  X₁ = X₂ line
             |                  /
             |            ..---/-..
             |         .-'    /    '-.  largest values of X̄
             |       .'      /        '.
             |      /       * X         \  Conditioning set:
             |     ;       /             ; ||X||² = u
             |    |       /               |
             |    |      /                |
             |----|-----*-----------------|----> X₁
             |    |    1_n                |
             |     ;                     ;
             |      \                   /
             | smallest'                 '
             | values of X̄'.-       -.'
             |               ''---''
             |                  /
             |                 /
```

---

## $t$-statistic

Above test rejects for
* conditionally extreme $\bar{X}$ given $\|X\|^2$
* OR marginally extreme $\frac{\bar{X}}{\|X\|} \quad (\perp\!\!\!\perp \|X\|^2)$ (equiv.)

**Equivalent:** reject for marginally extreme
$$T = \frac{\sqrt{n} \, \bar{X}}{\sqrt{S^2}}, \qquad \text{where}$$
$$\begin{aligned}
S^2 &= \frac{1}{n-1} \sum (X_i - \bar{X})^2 \qquad \text{(sample variance)} \\
&= \frac{1}{n-1} \left( \sum X_i^2 - 2\bar{X}\sum X_i + n\bar{X}^2 \right) \\
&= \frac{1}{n-1} \left( \|X\|^2 - n\bar{X}^2 \right)
\end{aligned}$$

$$\Rightarrow T = \sqrt{n-1} \cdot \frac{\sqrt{n} \, \bar{X}}{\sqrt{\|X\|^2 - n\bar{X}^2}} = \sqrt{n-1} \cdot \frac{R}{\sqrt{1 - R^2}}$$
$$r \mapsto \frac{r}{\sqrt{1-r^2}} : \quad \text{strictly increasing}$$

for
$$R = \frac{\sqrt{n} \, \bar{X}}{\|X\|} = \frac{1}{\sqrt{n}} \mathbf{1}_n \cdot \frac{X}{\|X\|} = \cos \sphericalangle(\mathbf{1}_n, X)$$
$$\text{(unit vectors)}$$
$$f\left(\frac{X}{\|X\|}\right) \Rightarrow \perp\!\!\!\perp \|X\|$$

---

## Geometric Picture

$$T = \frac{\sqrt{n} \, \bar{X}}{\sqrt{S^2}} = \frac{\|\operatorname{Proj}_{\mathbf{1}_n} X\|}{\|\operatorname{Proj}_{\mathbf{1}_n}^\perp X\|} \cdot \sqrt{n-1} \operatorname{sgn}(\bar{X})$$

```
          X₂ ^
             |                  /  X₁ = X₂ line
             |            ..---/-..
             |         .-'    /|   '-.
             |       .'      / |      '.
             |      /       /  |        \  √(n-1) S² = ||Proj_{1_n}^⟂ X||
             |     ;  |√n X̄|   * X       ;
             |    | = ||Proj_{1_n} X||    |
             |    |    /                  |
             |----|---*-------------------|----> X₁
             |    |  1_n \ ∢(1, X)        |
             |     ;      \              ;
             |      \      \            /
             |       '.     \         .'
             |         '-.   \     .-'
             |            ''---/--''
             |                /
```

Next major theme: ratios of projections

---

---

[← Theorem](02-theorem.md) · [Up: contents](index.md) · [Permutation Tests →](04-permutation-tests.md)
