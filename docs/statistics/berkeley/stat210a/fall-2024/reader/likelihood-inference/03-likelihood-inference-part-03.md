---
title: Likelihood inference Part 03 —
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/likelihood-inference.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/likelihood-inference.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Likelihood inference Part 03 —

**Source:** [`reader/likelihood-inference.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/likelihood-inference.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Test $H_0: \theta = \theta_0$ vs $H_1: \theta \neq \theta_0$

We can bypass quadratic approximation entirely by using score as test stat:

$\nabla \ell_n(\theta_0; X) \sim N(0, nJ(\theta_0))$
or $J_n^{-1/2}(\theta_0)\nabla \ell_n(\theta_0; X) \stackrel{\cdot}{\sim} N_d(0, I_d)$

So we can reject $H_0: \theta = \theta_0$ if
$\|\hat{J}_n^{-1/2}(\theta_0)\nabla \ell_n(\theta_0; X)\|^2 > \chi^2_{d,1-\alpha}$

$\nabla \ell_n(\theta_0; X)^T \hat{J}_n^{-1}(\theta_0) \nabla \ell_n(\theta_0; X) \sim \chi^2_d$

Can do 1-sided tests

### Remarks
- No quadratic approx, no MLE
- No need to estimate Fisher info at $\theta_0$
- Can be generalized to case with nuisance params
- Typically estimate via MLE on $\Theta_0$

### Score Test is Invariant to Reparameterization

Assume $\Theta \subset \mathbb{R}^d$, $\eta = g(\theta)$, $\Psi = g(\Theta)$

$q_\eta(x) = p_{g^{-1}(\eta)}(x)$

$\ell_\eta(x) = \log q_\eta(x) = \ell_\theta(x)$

$\nabla_\eta \ell_\eta(x) = \nabla_\theta \ell_\theta(x) \cdot \nabla g^{-1}(\eta)$

$J_\eta(\eta) = J_\theta(g^{-1}(\eta)) \cdot \nabla g^{-1}(\eta) \cdot \nabla g^{-1}(\eta)^T$

So $\nabla_\eta \ell_\eta(x)^T J_\eta^{-1}(\eta) \nabla_\eta \ell_\eta(x) = \nabla_\theta \ell_\theta(x)^T J_\theta^{-1}(\theta) \nabla_\theta \ell_\theta(x)$

if $\eta_0 = g(\theta_0)$

### Example: 1-Parameter Exponential Family

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} e^{\eta T(x) - A(\eta)} h(x)$

$\nabla \ell_n(\eta; X) = \sum T(X_i) - n\mu(\eta)$

$\ell_n''(\eta; X) = -n\text{Var}_\eta[T(X)]$

$\hat{\eta}_n = \text{MLE} = A'^{-1}(\bar{T})$

$\frac{\sum T(X_i) - n\mu(\eta_0)}{\sqrt{n\text{Var}_{\eta_0}[T(X)]}} \sim N(0,1)$

### Example: $X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} \text{Laplace}(\theta, 2\sqrt{2})$

Test $H_0: \theta = 0$ vs $H_1: \theta \neq 0$ (two-tailed)

$\ell_n(\theta; X) = \sum |X_i - \theta| - n\log(4\sqrt{2})$

$\nabla \ell_n(\theta; X) = \sum \text{sgn}(\theta - X_i) = \sum [\mathbb{I}(X_i < \theta) - \mathbb{I}(X_i > \theta)]$

$\nabla \ell_n(0; X) = \sum [\mathbb{I}(X_i < 0) - \mathbb{I}(X_i > 0)] = \sum \text{sgn}(-X_i)$

$J_n(0) = n/2$

$\sqrt{2/n} \sum \text{sgn}(-X_i) \sim N(0,1)$ (sign test)

Note: this test is the exact NP/UMP test for $H_0: \theta = 0$ vs $H_0: |\theta| = \epsilon$ for $\epsilon > 0$

Intuition: Maximize power for nearby alternatives since we'll have power for $\theta \gg 0$

More generally, one-sided score test is almost UMP for nearby alternatives

$p_\theta(x) \approx p_0(x)[1 + \epsilon \ell'_0(X)]$ for small $\epsilon > 0$

### Example: Pearson's $\chi^2$ Test (Goodness of Fit)

$N = (N_1, \ldots, N_d) \sim \text{Multi}(n, \pi)$, $\pi_i \geq 0$, $\sum \pi_i = 1$

$\ell_n(\pi; N) = \sum N_i \log \pi_i$

Note $\mathbb{E}[\pi] = 1$ so this is a full rank $d-1$ parameter exp family e.g.
$T_j = \mathbb{I}(\text{category} = j)$, $j=1,\ldots,d-1$

$\nabla \ell_n(\pi; N) = (N_1/\pi_1, \ldots, N_d/\pi_d)^T - n1_d$

$\hat{\pi} = \text{MLE} = (N_1/n, \ldots, N_d/n)$

$J_n(\pi) = n[\text{diag}(\pi_1^{-1}, \ldots, \pi_d^{-1})

---

[← Wald-Type Confidence Regions](02-wald-type-confidence-regions.md) · [Up: contents](index.md)
