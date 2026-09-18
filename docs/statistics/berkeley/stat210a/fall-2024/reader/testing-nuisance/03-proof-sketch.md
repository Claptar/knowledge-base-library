---
title: Proof Sketch
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-nuisance.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-nuisance.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/testing-nuisance.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-nuisance.qmd) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Proof Sketch

1. Any unbiased test has $\mathbb{P}(\phi=1) \leq h(t,u)$ (continuity)
2. Power = 0 on boundary $\implies \mathbb{E}_{\theta_0}[T\phi] = \theta_0$ (UK complete sufficient on boundary sub-model)
3. $\phi$ optimal among all tests with conditional level $\alpha$ by reduction to univariate model

### Detailed Proof

Assume $\phi$ any unbiased test:

1. $\mathbb{E}_\theta[\phi] = \alpha + f(\theta)$, $f(\theta_0) = 0$, $f'(\theta_0) = 0$
   Keener Thm 12.4
2. $\mathbb{E}_\theta[\phi]$ infinitely diff on $\mathbb{R}^s$, can diff under $\int$
3. $\phi$ unbiased $\implies \mathbb{E}_\theta[T\phi] = \frac{\partial}{\partial \theta} \mathbb{E}_\theta[\phi] = \theta$

Step 1: Boundary sub-model $\cP_0 = \{p_{\theta_0, \lambda}: \lambda \in \mathbb{R}^r\}$

$p_{\theta_0, \lambda}(x) = e^{\lambda \cdot U(x) - A(\theta_0, \lambda)}h(x)$

$\cP_0$ is full rank $r$-param exp fam, $U(X)$ complete suff

Let $f(\lambda) = \mathbb{E}_{\theta_0, \lambda}[\phi(X) | U(X)] = \alpha$

$\mathbb{E}_{\theta_0, \lambda}[\phi(X) T(X) | U(X)] = \theta_0$ a.s.

$\mathbb{E}_{\theta_0, \lambda}[\phi(X) | U(X)] = \alpha$ a.s.

Two-sided: $\mathbb{E}_{\theta_0, \lambda}[g(U(X))\phi(X)] = \mathbb{E}_{\theta_0, \lambda}[T(X)\phi(X)] = \theta_0$

$\mathbb{E}_{\theta_0, \lambda}[g(U)\mathbb{E}_{\theta_0, \lambda}[\phi|U]] = \theta_0$

$\mathbb{E}_{\theta_0, \lambda}[g(U) \alpha] = \theta_0$

$\mathbb{E}_{\theta_0, \lambda}[g(U)] = \frac{\theta_0}{\alpha}$

One-sided: $\mathbb{E}_{\theta_0, \lambda}[\phi] = \alpha$ $\forall \lambda$

Steps 2-3: For any value $u$, the conditional model is:

$$p_\theta(t|u) = e^{\theta \cdot t} g(t,u)$$

1-param exp fam.

In one/two-sided case, we have shown $\psi(t,u)$ is UMP/UMPU in $\{p_\theta(\cdot|u)\}$

Let $g(t,u) = \mathbb{E}_{\theta_0}[\phi(X) | T(X)=t, U(X)=u] \leq 1$

$\mathbb{E}_{\theta_0}[\psi(T,U) | U] = \mathbb{E}_{\theta_0}[\phi(X) | U(X)=u]$

$\psi$ if $\theta > \theta_0$
$\phi(X)$ is a conditional test of $H_0$ vs $H_1$ in $\{p_\theta(\cdot|u)\}$ with power $\leq \alpha$ at boundary

One-sided case: For $\theta > \theta_0$
$\psi(t,u)$ is the UMP test of $\theta=\theta_0$ vs $\theta>\theta_0$
in $\{p_\theta(\cdot|u)\}$, which is a 1-param exp fam

Two-sided:
$\psi(t,u)$ is the UMP test of $\theta=\theta_0$ vs $\theta \neq \theta_0$
among tests with power $\alpha$ over $\theta=\theta_0$
Keener Thm 12.22 (main thm for two-sided tests)

In either case, $\psi$ has higher cond. power than $\phi$ a.s.

For $\theta \neq \theta_0$:

$$\mathbb{E}_\theta[\phi] = \mathbb{E}_\theta[\mathbb{E}[\phi(X) | T(X), U(X)]]$$
$$\leq \mathbb{E}_\theta[\mathbb{E}[\psi(T(X), U(X)) | T(X), U(X)]]$$
$$= \mathbb{E}_\theta[\psi]$$

### Example: Normal Mean with Unknown Variance

$X \sim N(\mu, \sigma^2)$, $\sigma^2>0$ unknown
$H_0: \mu=0$ vs $H_1: \mu \neq 0$

$T = \frac{\bar{X}}{\|X\|}$, $U = \|X\|^2$

Optimal test rejects when $\bar{X}$ is extreme given $\|X\|^2$

If $\mu=0$, $\frac{X}{\|X\|}$ is rotationally symmetric
$\frac{X}{\|X\|} \sim \text{Unif}(S^{n-1})$, $\frac{X}{\|X\|}$ indep of $\|X\|$

Optimal test rejects when $\frac{\bar{X}}{\|X\|}$ extreme (marginally)

Could stop here & simulate

#### Geometric Picture (n=2)

[Insert geometric picture here]

Above test rejects for:
- conditionally extreme $\bar{X}$ given $\|X\|^2$
OR
- marginally extreme $\frac{\bar{X}}{\|X\|}$

Fact: reject for marginally extreme $T$ where

$$T^2 = \frac{(\sum X_i)^2}{\sum X_i^2 - \frac{1}{n}(\sum X_i)^2} = \frac{n\bar{X}^2}{\|X\|^2 - n\bar{X}^2} = \frac{n\bar{X}^2}{S^2}$$

and $S^2 = \frac{1}{n-1}\sum (X_i - \bar{X})^2$

#### Geometric Picture

[Insert second geometric picture here]

$T^2 = \frac{\|\text{Proj}_\mathbf{1}X\|^2}{\|\text{Proj}_{\mathbf{1}^\perp}X\|^2} \cdot \frac{n-1}{n}$

Next major theme: ratios of projections

## Permutation Tests

Even if we don't get a UMPU test at the end, conditioning on null suff. stat. still helps

Example: $X_1, \ldots, X_n \sim \text{iid } P$, $Y_1, \ldots, Y_m \sim \text{iid } Q$
$H_0: P=Q$ vs $H_1: P \neq Q$

Under $H_0$: $P=Q$, $X_1, \ldots, X_n, Y_1, \ldots, Y_m \sim P$

Let $Z = (Z_1, \ldots, Z_{n+m}) = (X_1, \ldots, X_n, Y_1, \ldots, Y_m)$

Under $H_0$, $U = Z$ is complete sufficient

Let $S_{n+m}$ = Permutations on $n+m$ elements

$(X, Y) = (U_{\pi(1)}, \ldots, U_{\pi(n+m)})$ for $\pi \in S_{n+m}$

Thus for test stat $T$, if $P=Q$:

$$\mathbb{P}(T \geq t | U) = \frac{1}{(n+m)!}\sum_{\pi \in S_{n+m}} 1\{T(Z_{\pi(1)}, \ldots, Z_{\pi(n+m)}) \geq t\}$$

Monte Carlo test: In practice, we sample \$\pi_1, \ldots, \pi_B \sim

---

[← Theorem (Informal)](02-theorem-informal.md) · [Up: contents](index.md)
