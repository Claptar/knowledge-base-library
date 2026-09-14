---
title: Delta Method
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/asymptotics.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/asymptotics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Delta Method

**Source:** [`reader/asymptotics.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/asymptotics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Theorem (Delta Method):
If $\sqrt{n}(X_n - \mu) \xrightarrow{d} N(0, \sigma^2)$
$f(x)$ differentiable at $x = \mu$

Then $\sqrt{n}(f(X_n) - f(\mu)) \xrightarrow{d} N(0, [f'(\mu)]^2 \sigma^2)$

Instant: $X \sim N(\mu, \sigma^2/n) \implies f(X) \sim N(f(\mu), [f'(\mu)]^2 \sigma^2/n + o(1/n))$

Proof:
$f(X_n) = f(\mu) + f'(\mu)(X_n - \mu) + o(X_n - \mu)$
$\sqrt{n}(f(X_n) - f(\mu)) = f'(\mu)\sqrt{n}(X_n - \mu) + \sqrt{n}o(X_n - \mu)$
$N(0, \sigma^2) + 0 \xrightarrow{d} N(0, [f'(\mu)]^2 \sigma^2)$

Multivariate: $\sqrt{n}(X_n - \mu) \xrightarrow{d} N(0, \Sigma)$, $f: \mathbb{R}^d \to \mathbb{R}^k$
Derivative $Df(\mu)$ exists at $\mu$

Then $\sqrt{n}(f(X_n) - f(\mu)) \xrightarrow{d} N(0, Df(\mu) \Sigma Df(\mu)^T)$

$N(f(\mu), Df(\mu) \Sigma Df(\mu)^T/n + o(1/n))$ if $k=1$

### Example: Delta Method Application

$X_1, \ldots, X_n \sim \text{Unif}[0, \theta]$ iid
$Y_1, \ldots, Y_m \sim \text{Unif}[0, \theta]$ iid
$X, Y$ independent

For large $n, m$, what is the distribution of $T = \frac{\bar{X}}{\bar{Y}}$?

1. $\sqrt{n}(\bar{X} - \frac{\theta}{2}) \xrightarrow{d} N(0, \frac{\theta^2}{12})$ as $n \to \infty$
2. $\sqrt{m}(\bar{Y} - \frac{\theta}{2}) \xrightarrow{d} N(0, \frac{\theta^2}{12})$ as $m \to \infty$

$T_n = \frac{\bar{X}}{\bar{Y}} = \frac{\theta/2}{\theta/2} = 1 + O_p(n^{-1/2} + m^{-1/2})$

Let $f(x,y) = x/y$

$f_x'(\frac{\theta}{2}, \frac{\theta}{2}) = \frac{1}{\theta/2} = \frac{2}{\theta}$
$f_y'(\frac{\theta}{2}, \frac{\theta}{2}) = -\frac{\theta/2}{(\theta/2)^2} = -\frac{2}{\theta}$

$f'(\frac{\theta}{2}, \frac{\theta}{2}) = (\frac{2}{\theta}, -\frac{2}{\theta})$

$\sqrt{n}(T_n - 1) \xrightarrow{d} N(0, \frac{4}{\theta^2} \cdot \frac{\theta^2}{12} \cdot \frac{1}{n} + \frac{4}{\theta^2} \cdot \frac{\theta^2}{12} \cdot \frac{n}{m})$

$= N(0, \frac{1}{3n} + \frac{1}{3m})$

More accurate:
$\sqrt{n}(T_n - 1) \xrightarrow{d} N(0, \frac{4}{3}(1 + \frac{n}{m}))$

### What if $\mu = 0$?

3. What if $\mu_1 = \mu_2 = 0$? Conclusion still holds:
   $T_n = \frac{1 + O_p(n^{-1/2})}{1 + O_p(m^{-1/2})} = 1 + O_p(n^{-1/2} + m^{-1/2})$

Note: $\frac{1}{1 + n^{-1/2}} \to 1$ (continuous mapping)
Not Slutsky

So $n(T_n - 1)^2 \xrightarrow{d} \chi^2_1$ (continuous mapping)
Why not delta method?

In general, can do higher-order Taylor expansions for delta method if derivatives $\neq 0$:

$f(X_n) = f(\mu) + f'(\mu)(X_n - \mu) + \frac{1}{2}f''(\mu)(X_n - \mu)^2 + O_p(n^{-3/2})$

If $f'(\mu) = 0$, use second-order term:
$n(f(X_n) - f(\mu)) \xrightarrow{d} \frac{1}{2}f''(\mu)\chi^2_1$

---

[← Slutsky's Theorem](05-slutsky-s-theorem.md) · [Up: contents](index.md)
