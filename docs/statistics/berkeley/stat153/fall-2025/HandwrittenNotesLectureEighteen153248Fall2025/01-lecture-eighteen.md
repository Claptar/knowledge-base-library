---
title: Lecture Eighteen
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEighteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureEighteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureEighteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEighteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Eighteen

Last lecture: Estimation in $AR(1)$

$$y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t, \quad \varepsilon_t \overset{\text{iid}}{\sim} N(0, \sigma^2)$$
$$t = 2, \dots, n$$

(1) Likelihood:
$$\prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(y_t - \phi_0 - \phi_1 y_{t-1})^2}{2\sigma^2} \right)$$

$$f_{y_2, \dots, y_n \mid y_1}^\theta$$

Conditional MLE or least squares

$AR(p)$:
$$y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \varepsilon_t$$
$$t = p+1, \dots, n$$

Conditional likelihood:
$$\prod_{t=p+1}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(y_t - \phi_0 - \dots - \phi_p y_{t-p})^2}{2\sigma^2} \right)$$

Two implementation methods:

(a) Create $\underset{(n-p)\times 1}{y}$ & $\underset{(n-p)\times (p+1)}{X}$ & use OLS: `sm.OLS(y, X).fit()`

(b) `AutoReg(y, p=1 \text{ or } 2 \text{ etc})`

$\to$ Identical parameter estimates of $\phi_0, \phi_1, \dots, \phi_p$

$\to$ For $\sigma$, method (a): $\hat{\sigma} = \sqrt{\frac{\text{RSS}}{(n-p)-(p+1)}}$

---

method (b): $\hat{\sigma} = \sqrt{\frac{\text{RSS}}{n-p}}$

$\to$ $t$ vs $z$

(2) $AR(1)$:
$$y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t,$$
$$t = 2, \dots, n$$
$$t = 1, 0, -1, \dots$$

Assume $|\phi_1| < 1$

$$y_1 = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty \phi_1^j \varepsilon_{1-j}$$
$$\sim N\left(\frac{\phi_0}{1-\phi_1}, \frac{\sigma^2}{1-\phi_1^2}\right)$$

Likelihood:
$$\left\{ \frac{\sqrt{1-\phi_1^2}}{\sqrt{2\pi}\sigma} \exp\left[ -\frac{\left(y_1 - \frac{\phi_0}{1-\phi_1}\right)^2 (1-\phi_1^2)}{2\sigma^2} \right] \right\}$$
$$\times \prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(y_t - \phi_0 - \phi_1 y_{t-1})^2}{2\sigma^2} \right)$$

$\longrightarrow$ Full likelihood / Unconditional, $|\phi_1| < 1$

`AutoReg` does not have an option to use this complicated likelihood.

$\to$ `arima` (function in `statsmodels`)

---

$y_1, \dots, y_p$

How are predictions & standard errors calculated?

$$y_1, \dots, y_n$$

$$\hat{y}_{n+1}(\theta) = \phi_0 + \phi_1 y_n + \dots + \phi_p y_{n+1-p}$$

$\theta = (\phi_0, \dots, \phi_p)$

$$\hat{y}_{n+1}(\hat{\theta}) = \mathbb{E}(y_{n+1} \mid y_1, \dots, y_n, \theta)$$

$$\hat{y}_{n+2}(\theta) = \mathbb{E}(y_{n+2} \mid y_1, \dots, y_n, \theta)$$
$$= \mathbb{E}\left[ \phi_0 + \phi_1 y_{n+1} + \phi_2 y_n + \dots + \phi_p y_{n+2-p} \mid y_1, \dots, y_n, \theta \right]$$
$$= \phi_0 + \phi_1 \underbrace{\mathbb{E}(y_{n+1} \mid y_1, \dots, y_n, \theta)}_{\hat{y}_{n+1}(\theta)} + \phi_2 y_n + \dots + \phi_p y_{n+2-p}$$

$$\hat{y}_{n+k}(\theta) = \phi_0 + \phi_1 \hat{y}_{n+k-1}(\theta) + \phi_2 \hat{y}_{n+k-2}(\theta) + \dots + \phi_p \hat{y}_{n+k-p}(\theta)$$
$$k = 1, 2, \dots$$

Recursion

$$\mathbb{E}(y_{n+k} \mid y_1, \dots, y_n, \theta)$$

$$\hat{y}_j(\theta) = y_j \quad \text{for } j \le n$$

$$y_1, \dots, y_n$$

---

## Standard Errors corresponding to predictions

$$\operatorname{var}\left(y_{n+k} \mid \underset{\theta}{y_1, \dots, y_n}\right) \quad k=1, 2, \dots$$

$$\operatorname{var}\left(y_{n+1} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$
$$= \operatorname{var}\left( \phi_0 + \phi_1 y_n + \phi_2 y_{n-1} + \dots + \phi_p y_{n+1-p} + \varepsilon_{n+1} \mid \underset{\theta}{y_1, \dots, y_n} \right)$$
$$= \operatorname{var}\left( \varepsilon_{n+1} \mid \underset{\theta}{y_1, \dots, y_n} \right) = \sigma^2$$

$$\operatorname{var}\left(y_{n+2} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$
$$= \operatorname{var}\left( \phi_0 + \phi_1 y_{n+1} + \phi_2 y_n + \dots + \phi_p y_{n+2-p} + \varepsilon_{n+2} \mid \underset{\theta}{y_1, \dots, y_n} \right)$$
$$= \operatorname{var}\left( \phi_1 y_{n+1} + \varepsilon_{n+2} \mid \underset{\theta}{y_1, \dots, y_n} \right)$$

$$\operatorname{var}\left(y_{n+k} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$

$$\operatorname{Cov}\left( \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k} \end{pmatrix} \;\middle|\; \underset{\theta}{y_1, \dots, y_n} \right) = \Gamma_k(\theta)$$

---

---

[Up: contents](index.md) · [Covariance Matrices →](02-covariance-matrices.md)
