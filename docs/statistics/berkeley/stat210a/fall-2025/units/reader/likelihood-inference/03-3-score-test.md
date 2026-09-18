---
title: 3 Score Test
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/likelihood-inference.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/likelihood-inference.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 3 Score Test

Test $H_0: \theta = \theta_0$ vs $H_1: \theta \neq \theta_0$

We can bypass quadratic approximation entirely by using score as test stat:

$\nabla \ell_n(\theta_0; X) \sim N(0, nJ(\theta_0))$ or $J_n^{-1/2}(\theta_0)\nabla \ell_n(\theta_0; X) \stackrel{\cdot}{\sim} N_d(0, I_d)$

So we can reject $H_0: \theta = \theta_0$ if $\|\hat{J}_n^{-1/2}(\theta_0)\nabla \ell_n(\theta_0; X)\|^2 > \chi^2_{d,1-\alpha}$

$\nabla \ell_n(\theta_0; X)^T \hat{J}_n^{-1}(\theta_0) \nabla \ell_n(\theta_0; X) \sim \chi^2_d$

Can do 1-sided tests

## 3.1 Remarks {.anchored number="3.1" anchor-id="remarks-1"}

- No quadratic approx, no MLE
- No need to estimate Fisher info at $\theta_0$
- Can be generalized to case with nuisance params
- Typically estimate via MLE on $\Theta_0$

## 3.2 Score Test is Invariant to Reparameterization {.anchored number="3.2" anchor-id="score-test-is-invariant-to-reparameterization"}

Assume $\Theta \subset \mathbb{R}^d$, $\eta = g(\theta)$, $\Psi = g(\Theta)$

$q_\eta(x) = p_{g^{-1}(\eta)}(x)$

$\ell_\eta(x) = \log q_\eta(x) = \ell_\theta(x)$

$\nabla_\eta \ell_\eta(x) = \nabla_\theta \ell_\theta(x) \cdot \nabla g^{-1}(\eta)$

$J_\eta(\eta) = J_\theta(g^{-1}(\eta)) \cdot \nabla g^{-1}(\eta) \cdot \nabla g^{-1}(\eta)^T$

So $\nabla_\eta \ell_\eta(x)^T J_\eta^{-1}(\eta) \nabla_\eta \ell_\eta(x) = \nabla_\theta \ell_\theta(x)^T J_\theta^{-1}(\theta) \nabla_\theta \ell_\theta(x)$

if $\eta_0 = g(\theta_0)$

## 3.3 Example: 1-Parameter Exponential Family {.anchored number="3.3" anchor-id="example-1-parameter-exponential-family"}

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} e^{\eta T(x) - A(\eta)} h(x)$

$\nabla \ell_n(\eta; X) = \sum T(X_i) - n\mu(\eta)$

$\ell_n''(\eta; X) = -n\text{Var}_\eta[T(X)]$

$\hat{\eta}_n = \text{MLE} = A'^{-1}(\bar{T})$

$\frac{\sum T(X_i) - n\mu(\eta_0)}{\sqrt{n\text{Var}_{\eta_0}[T(X)]}} \sim N(0,1)$

## 3.4 Example: $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} \text{Laplace}(\theta, 2\sqrt{2})$ {#example-math96 .anchored number="3.4" anchor-id="example-x_1-ldots-x_n-stackreltextiidsim-textlaplacetheta-2sqrt2"}

Test $H_0: \theta = 0$ vs $H_1: \theta \neq 0$ (two-tailed)

$\ell_n(\theta; X) = \sum |X_i - \theta| - n\log(4\sqrt{2})$

$\nabla \ell_n(\theta; X) = \sum \text{sgn}(\theta - X_i) = \sum [\mathbb{I}(X_i < \theta) - \mathbb{I}(X_i > \theta)]$

$\nabla \ell_n(0; X) = \sum [\mathbb{I}(X_i < 0) - \mathbb{I}(X_i > 0)] = \sum \text{sgn}(-X_i)$

$J_n(0) = n/2$

$\sqrt{2/n} \sum \text{sgn}(-X_i) \sim N(0,1)$ (sign test)

Note: this test is the exact NP/UMP test for $H_0: \theta = 0$ vs $H_0: |\theta| = \epsilon$ for $\epsilon > 0$

Intuition: Maximize power for nearby alternatives since we’ll have power for $\theta \gg 0$

More generally, one-sided score test is almost UMP for nearby alternatives

$p_\theta(x) \approx p_0(x)[1 + \epsilon \ell'_0(X)]$ for small $\epsilon > 0$

## 3.5 Example: Pearson’s $\chi^2$ Test (Goodness of Fit) {#example-pearsons-math110-test-goodness-of-fit .anchored number="3.5" anchor-id="example-pearsons-chi2-test-goodness-of-fit"}

$N = (N_1, \ldots, N_d) \sim \text{Multi}(n, \pi)$, $\pi_i \geq 0$, $\sum \pi_i = 1$

$\ell_n(\pi; N) = \sum N_i \log \pi_i$

Note $\mathbb{E}[\pi] = 1$ so this is a full rank $d-1$ parameter exp family e.g. $T_j = \mathbb{I}(\text{category} = j)$, $j=1,\ldots,d-1$

$\nabla \ell_n(\pi; N) = (N_1/\pi_1, \ldots, N_d/\pi_d)^T - n1_d$

$\hat{\pi} = \text{MLE} = (N_1/n, \ldots, N_d/n)$

\$J\_n() = n[(\_1^{-1}, , \_d^{-1})

---

[← 2 Wald-Type Confidence Regions](02-2-wald-type-confidence-regions.md) · [Up: contents](index.md)
