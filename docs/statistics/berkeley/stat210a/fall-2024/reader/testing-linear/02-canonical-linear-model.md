---
title: Canonical Linear Model
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-linear.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-linear.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Canonical Linear Model

**Source:** [`reader/testing-linear.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-linear.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Assume $Z = \begin{pmatrix} Z_1 \\ Z_2 \end{pmatrix} \sim N\left(\begin{pmatrix} \mu \\ 0 \end{pmatrix}, \sigma^2 I_d\right)$, $d = d_0 + d_1$, $\mu \in \mathbb{R}^{d_0}$, $\sigma^2 > 0$

Test $H_0: \mu = 0$ vs $H_1: \mu \neq 0$ (or possibly one-sided if $d_0 = 1$)

Exponential Family:

$$f(z) = f(z_0, z_1) = \frac{1}{(2\pi\sigma^2)^{d/2}} \exp\left(-\frac{\|z_1\|^2 + \|z_0 - \mu\|^2}{2\sigma^2}\right)$$

### Case 1: $\sigma^2$ Known

Condition on $Z_1$, reject for large/small/extreme $Z_0$

$Z_0 \sim N(\mu, \sigma^2 I_{d_0})$

$\chi^2$ test: Reject for large $\|Z_0\|^2$

t-test: If $d_0 = 1$, reject for large $|Z_0|$

### Case 2: $\sigma^2$ Unknown

Condition on $Z_1$, $\|Z_1\|^2$, $\|Z_0\|^2$ sufficient

Reject for large/small/extreme $Z_0$

Reject for large $\frac{\|Z_0\|^2/d_0}{\|Z_1\|^2/d_1} \sim F_{d_0,d_1}$ under $H_0$

F-test: $d_0 > 1$, Reject for conditionally large $\|Z_0\|^2$

Reject for large $\frac{\|Z_0\|^2/d_0}{\|Z_1\|^2/d_1} \sim F_{d_0,d_1}$

t-test: $d_0 = 1$, Reject for conditionally large $|Z_0|$

Reject for large $\frac{|Z_0|}{\sqrt{\|Z_1\|^2/d_1}} \sim t_{d_1}$

Here, $\frac{\|Z_1\|^2}{d_1}$ functioning as estimator of $\sigma^2$:
$\mathbb{E}[\frac{\|Z_1\|^2}{d_1}] = \sigma^2$, $\text{Var}(\frac{\|Z_1\|^2}{d_1}) = \frac{2\sigma^4}{d_1}$

General case: $Z \sim N(\mu, \sigma^2 I_d)$, $\mu \not\in \mathbb{R}^{d_0} \times \{0\}^{d_1}$

Translate problem:

$Z_0 \sim N_{d_0}(\mu_0, \sigma^2 I_{d_0})$
$Z_1 \sim N_{d_1}(\mu_1, \sigma^2 I_{d_1})$

Can do some tests with $Z - \mu_1$ replacing $Z$

Invert:
$1-\alpha$ CI: $\mu_0 \in Z_0 \pm \sigma t_{d_1,1-\alpha/2} \sqrt{\frac{\|Z_1 - \mu_1\|^2}{d_1}}$

$1-\alpha$ confidence ellipsoid: $\|\mu_0 - Z_0\|^2 \leq \frac{d_0}{d_1} \|Z_1 - \mu_1\|^2 F_{d_0,d_1,1-\alpha}$

$1-\alpha$ prediction interval: $Z_{\text{new}} \in Z_0 \pm \sigma t_{d_1,1-\alpha/2} \sqrt{1 + \frac{\|Z_1 - \mu_1\|^2}{d_1}}$

---

[← t and F Distributions](01-t-and-f-distributions.md) · [Up: contents](index.md) · [General Linear Model →](03-general-linear-model.md)
