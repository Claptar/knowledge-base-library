---
title: Bayesian Inference for Simple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureFour153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Bayesian Inference for Simple Linear Regression

$(x_1, y_1), \dots, (x_n, y_n)$

$y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad \varepsilon_i \overset{iid}{\sim} N(0, \sigma^2)$

$y_i \overset{ind}{\sim} N(\beta_0 + \beta_1 x_i, \sigma^2)$

$$Likelihood: \prod_{i=1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left[-\frac{1}{2\sigma^2}(y_i - \beta_0 - \beta_1 x_i)^2\right]$$

$$\propto \sigma^{-n} \exp\left[-\frac{1}{2\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2\right]$$

$$= \sigma^{-n} \exp\left[-\frac{S(\beta_0, \beta_1)}{2\sigma^2}\right]$$

$$\text{prior}: \beta_0, \beta_1, \log\sigma \overset{iid}{\sim} \text{Unif}(-C, C) \quad (\text{think of } C = \infty)$$

$$f_{\beta_0, \beta_1, \sigma}(\beta_0, \beta_1, \sigma) = \frac{I\{-C < \beta_0 < C\}}{2C} \frac{I\{-C < \beta_1 < C\}}{2C} \frac{I\{e^{-C} < \sigma < e^C\}}{2C\sigma}$$

$$\left(\log \sigma \sim \text{Unif}(-C, C) \Rightarrow \sigma \sim \dots\right)$$

$$\propto \frac{I\{-C < \beta_0, \beta_1, \log\sigma < C\}}{\sigma}$$

$$\underset{(\beta_0, \beta_1, \sigma)}{\text{posterior}} \propto \underset{(\beta_0, \beta_1, \sigma)}{\text{prior}} \times Likelihood(\beta_0, \beta_1, \sigma)$$

$$\propto \frac{I\{-C < \beta_0, \beta_1, \log\sigma < C\}}{\sigma} \left(\frac{1}{\sigma}\right)^n \exp\left(-\frac{S(\beta_0, \beta_1)}{2\sigma^2}\right)$$

---

$$= I\{-C < \beta_0, \beta_1, \log\sigma < C\} \left(\frac{1}{\sigma}\right)^{n+1} \exp\left(-\frac{S(\beta_0, \beta_1)}{2\sigma^2}\right)$$

Integrate this to get marginal densities of the variables separately.

$\beta_0, \beta_1$: main parameters
$\sigma$: nuisance parameters

$$f_{\beta_0, \beta_1 | data}(\beta_0, \beta_1) = \int_{-\infty}^\infty f_{\beta_0, \beta_1, \sigma | data}(\beta_0, \beta_1, \sigma) \, d\sigma \rightarrow \text{\textbf{LAW OF TOTAL PROBABILITY}}$$

$$\propto I\{-C < \beta_0, \beta_1 < C\} \int_{e^{-C}}^{e^C} \left(\frac{1}{\sigma}\right)^{n+1} \exp\left(-\frac{S(\beta_0, \beta_1)}{2\sigma^2}\right) d\sigma$$

$$\approx I\{-C < \beta_0, \beta_1 < C\} \int_0^\infty \left(\frac{1}{\sigma}\right)^{n+1} \exp\left(-\frac{S(\beta_0, \beta_1)}{2\sigma^2}\right) d\sigma$$

$$s = \frac{\sigma}{\sqrt{S(\beta_0, \beta_1)}}$$

$$= I\{-C < \beta_0, \beta_1 < C\} \int_0^\infty \left(\frac{1}{s}\right)^{n+1} (S(\beta_0, \beta_1))^{-\frac{n+1}{2}} \exp\left[-\frac{1}{2s^2}\right] \sqrt{S(\beta_0, \beta_1)} \, ds$$

$$= I\{-C < \beta_0, \beta_1 < C\} (S(\beta_0, \beta_1))^{-\frac{n}{2}} \int_0^\infty \left(\frac{1}{s}\right)^{n+1} \exp\left(-\frac{1}{2s^2}\right) ds$$

$$\propto I\{-C < \beta_0, \beta_1 < C\} \left[\frac{1}{S(\beta_0, \beta_1)}\right]^{\frac{n}{2}}$$

---

$$f_{\beta_0, \beta_1 | data}(\beta_0, \beta_1) \propto I\{-C < \beta_0, \beta_1 < C\} \left[\frac{1}{S(\beta_0, \beta_1)}\right]^{\frac{n}{2}}$$

$$\text{\textbf{Posterior mode}}: \text{Least squares estimator: } \hat{\beta}_0, \hat{\beta}_1$$

$$\propto I\{-C < \beta_0, \beta_1 < C\} \left[\frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)}\right]^{\frac{n}{2}}$$

**Claim**: Posterior is concentrated around the least squares estimator $\hat{\beta}_0, \hat{\beta}_1$.

(a) If $S(\beta_0, \beta_1) = (1.1) \, S(\hat{\beta}_0, \hat{\beta}_1)$,
then posterior at $(\beta_0, \beta_1)$: $\left(\frac{1}{1.1}\right)^{\frac{n}{2}}$

(b) If $S(\beta_0, \beta_1) = (1.01) \, S(\hat{\beta}_0, \hat{\beta}_1)$
posterior: $\left(\frac{1}{1.01}\right)^{\frac{n}{2}}$

**Conclude**: Bayesian inference with $\beta_0, \beta_1, \log\sigma \sim \text{Unif}(-C, C)$ is also based on the least squares estimators $\hat{\beta}_0, \hat{\beta}_1$. Posterior typically is highly concentrated: $\left[\frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)}\right]^{\frac{n}{2}}$

---

Posterior $\propto \left[\frac{S(\hat{\beta}_0, \hat{\beta}_1)}{S(\beta_0, \beta_1)}\right]^{\frac{n}{2}} \quad \{ \text{\textbf{t-density}} \}$

---

[Up: contents](index.md) · [Multiple Linear Regression →](02-multiple-linear-regression.md)
