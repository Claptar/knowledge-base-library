---
title: Lecture THIRTEEN
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureThirteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureThirteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureThirteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureThirteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture THIRTEEN

$$y_t = \beta_0 + \beta_1(t-1)_+ + \beta_2(t-2)_+ + \dots + \beta_{n-1}(t-(n-1))_+ + \varepsilon_t$$

$$\beta_0, \beta_1 \overset{\text{i.i.d.}}{\sim} N(0, C) \quad \text{or} \quad \text{Unif}(-C, C), \quad \beta_2, \dots, \beta_{n-1} \overset{\text{i.i.d.}}{\sim} N(0, \tau^2)$$

$$\log \tau \sim \text{Unif}(-C, C), \quad \log \sigma \sim \text{Unif}(-C, C)$$

$$\beta, \sigma, \tau$$
$$\beta_0, \beta_1, \dots, \beta_{n-1}$$

What is the posterior?

$$\beta \mid \underset{n \times 1}{\text{data}}, \sigma, \tau \sim N\left(\left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}, \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1}\right)$$

posterior of $\beta$ when $\sigma, \tau$ are fixed

Here

$$Q = \begin{bmatrix}
C & & & 0 \\
& C & & \\
& & \tau^2 & & \\
0 & & & & \tau^2
\end{bmatrix}$$

$$Q^{-1} = \begin{bmatrix}
1/C & & & 0 \\
& 1/C & & \\
& & 1/\tau^2 & & \\
0 & & & & 1/\tau^2
\end{bmatrix} \approx \begin{bmatrix}
0 & & & 0 \\
& 0 & & \\
& & 1/\tau^2 & & \\
0 & & & & 1/\tau^2
\end{bmatrix} = \frac{1}{\tau^2} J$$

$$J = \begin{bmatrix}
0 & & & 0 \\
& 0 & & \\
& & 1 & & \\
0 & & & & 1
\end{bmatrix}$$

---

$$\beta \mid \underset{\tau, \sigma}{\text{data}} \sim N\left(\left(\frac{X^T X}{\sigma^2} + \frac{J}{\tau^2}\right)^{-1} \frac{X^T y}{\sigma^2}, \left(\frac{X^T X}{\sigma^2} + \frac{J}{\tau^2}\right)^{-1}\right)$$

$$= N\left(\left(X^T X + \frac{\sigma^2}{\tau^2} J\right)^{-1} X^T y, \, \sigma^2 \left(X^T X + \frac{\sigma^2}{\tau^2} J\right)^{-1}\right)$$

Ridge Regression:

$$\|y - X \beta\|^2 + \lambda \sum_{j=2}^{n-1} \beta_j^2$$

$$\hat{\beta}_{\text{ridge}}(\lambda) = (X^T X + \lambda J)^{-1} X^T y$$

$$= \text{posterior mean of } \beta \mid \underset{\sigma, \tau}{\text{data}}$$
$$\text{provided } \lambda = \frac{\sigma^2}{\tau^2}.$$

$\beta \mid \sigma, \tau, \text{data}$

$$f(\sigma, \tau \mid \text{data}) \propto \frac{\sigma^{-n - 1} \tau^{-1}}{\sqrt{\det Q}} \sqrt{\det\left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1}} \exp\left(-\frac{y^T y}{2\sigma^2}\right) \exp\left(\frac{y^T X \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} X^T y}{2\sigma^2}\right)$$

$$Q = \text{diag}(C, C, \tau^2, \dots, \tau^2) \implies Q^{-1} \approx J/\tau^2$$
$$\det Q = C^2 (\tau^2)^{n-2} \propto (\tau^2)^{n-2}$$

Evaluate the posterior of $(\tau, \sigma)$ over a grid of values of $(\tau, \sigma)$.

(1) Generate posterior samples of $\tau, \sigma$

---

(2) Generate $\beta$ given $\tau, \sigma$.

Most cases:

(a) $f(\tau, \sigma \mid \text{data})$ prefers $\tau$ which are not too large. (AVOID OVERFITTING)

$\tau = 0.5$
$\sigma = 2$
$f(0.5, 2 \mid \text{data}) = 17$
$f(0.05, 2 \mid \text{data}) = 25$

(b) $f(\tau, \sigma \mid \text{data})$ prefers $\tau$ which are not too small. (AVOID UNDERFITTING)

$$f(\tau, \sigma \mid \text{data}) \propto f(\text{data} \mid \tau, \sigma) f(\tau, \sigma)$$

$$f(\tau, \sigma) \propto \frac{1}{\tau \sigma}$$
$$\log \tau \sim \text{Unif}(-C, C)$$
$$\log \sigma \sim \text{Unif}(-C, C)$$
Uninformative

$$f(\text{data} \mid \tau, \sigma)$$

Likelihood: $f(\text{data} \mid \beta, \sigma) = \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^n \exp\left(-\frac{\|y - X \beta\|^2}{2\sigma^2}\right)$

$$f(\text{data} \mid \tau, \sigma) = \int f(\text{data} \mid \beta, \sigma, \tau) f(\beta \mid \tau, \sigma) \, d\beta$$

---

Integrated Likelihood (Marginal Likelihood)

$$f(\text{data} \mid \tau, \sigma)$$
Integrated Likelihood

$$f(\text{data} \mid \beta, \sigma)$$
Original likelihood $\downarrow$ will be large for values of $\beta$ which lead to overfitting

$$f(\text{data} \mid \tau, \sigma) = \int f(\text{data} \mid \beta, \sigma) f(\beta \mid \tau) \, d\beta$$

(1) $\tau$ large: $N(0, \tau^2) \quad \frac{1}{\sqrt{2\pi}\tau} \exp\left(-\frac{\beta_i^2}{2\tau^2}\right)$
$\rightarrow$ usually will be small.

(2) $\tau$ small: $N(0, \tau^2)$
$\rightarrow f(\text{data} \mid \tau, \sigma)$ will be small.

**Slightly Different Prior**

$$\tau, \sigma$$

---

Reparametrize $\tau = \sigma \times \gamma$

Change the prior to
$$\log \tau, \log \sigma \overset{\text{i.i.d.}}{\sim} \text{Unif}(-C, C)$$
$$\downarrow \text{CHANGE}$$
$$\log \gamma, \log \sigma \overset{\text{i.i.d.}}{\sim} \text{Unif}(-C, C)$$

allows tractable integration of $\sigma$ in $f(\sigma, \gamma \mid \text{data})$.

Ridge: $\lambda = \frac{\sigma^2}{\tau^2}, \quad \tau = \sigma \times \gamma$.

$$\lambda = \frac{1}{\gamma^2} \quad \text{or} \quad \gamma = \frac{1}{\sqrt{\lambda}}$$

Posterior: $(\beta, \sigma, \gamma)$

$$\beta \mid \text{data}, \sigma, \gamma \sim N\left(\left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1} \frac{X^T y}{\sigma^2}, \left(\frac{X^T X}{\sigma^2} + Q^{-1}\right)^{-1}\right)$$

$$Q = \begin{bmatrix}
C & & & 0 \\
& C & & \\
& & \sigma^2 \gamma^2 & & \\
0 & & & & \sigma^2 \gamma^2
\end{bmatrix}$$

$$f(\sigma, \gamma \mid \text{data})$$

---

$$\gamma \mid \text{data}$$

$$f(\gamma \mid \text{data}) = \frac{\gamma^{-n+1} |X^T X + \gamma^{-2} J|^{-1/2}}{\left(y^T y - y^T X (X^T X + \gamma^{-2} J)^{-1} X^T y\right)^{\frac{n}{2} - 1}}$$

$$\sigma \mid \gamma, \text{data}$$

$$\frac{1}{\sigma^2} \mid \text{data}, \gamma \sim \text{Gamma}\left(\frac{n}{2} - 1, \, \frac{y^T y - y^T X (X^T X + \gamma^{-2} J)^{-1} X^T y}{2}\right)$$

(1) First take a grid for $\gamma$ & compute posterior samples for $\gamma$.
(2) For each $\gamma$ sample, generate $\sigma$.
(3) Given $\gamma$ & $\sigma$, generate $\beta$.

## VARIANCE MODELS (SPECTRAL ANALYSIS)

ALL THE MODELS we studied so far are examples of **mean** models.

e.g.:
$$y_t = \beta_0 + \beta_1(t-1)_+ + \beta_2(t-2)_+ + \dots + \beta_{n-1}(t-(n-1))_+ + \varepsilon_t$$

$$\sum [y_t - (\dots)]^2 + \lambda \sum \beta_j^2$$
or $\lambda \sum |\beta_j|$

---

$$y_t = \mu_t + \varepsilon_t$$

$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{j=2}^{n-1} ((\mu_j - \mu_{j-1}) - (\mu_{j-1} - \mu_{j-2}))^2$$

$$\sum_{t=1}^n (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} |(\mu_t - \mu_{t-1}) - (\mu_{t-1} - \mu_{t-2})|$$

Data: $y_1, \dots, y_n$
Model: $y_t \overset{\text{independent}}{\sim} N(\mu_t, \sigma^2)$
Goal: To estimate the means $\mu_1, \dots, \mu_n$
Estimate: Assume smoothness.

$$\sum (y_t - \mu_t)^2 + \lambda \sum_{t=2}^{n-1} ((\mu_t - \mu_{t-1}) - (\mu_{t-1} - \mu_{t-2}))^2$$

THIS IS AN EXAMPLE OF A MEAN MODEL

In Contrast, Variance Model example:
$$y_1, \dots, y_n$$
$$[y_t \overset{\text{independent}}{\sim} N(0, \sigma_t^2)], \quad t = 1, \dots, n$$

---

$\alpha_t$ vs. $t$

$$\sigma_t = \exp(\alpha_t)$$
$$y_t \overset{\text{independent}}{\sim} N(0, \sigma_t^2)$$

$\rightarrow$ Variance model.

---

[Up: contents](index.md)
