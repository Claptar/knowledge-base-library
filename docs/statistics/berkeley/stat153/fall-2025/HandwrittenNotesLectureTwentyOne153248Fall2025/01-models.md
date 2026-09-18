---
title: $MA(q)$ models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyOne153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwentyOne153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwentyOne153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwentyOne153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# $MA(q)$ models

$$y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q}, \quad t = \dots, -3, -2, -1, 0, \dots$$

$\{\varepsilon_t\} \overset{i.i.d.}{\sim} N(0, \sigma^2)$

$q = 1$:

$$y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} \leftarrow \text{Slutzky 1937 Summation of Random Causes}$$

$$\begin{aligned}
\theta_1 = 0 &\to y_t \overset{i.i.d.}{\sim} N(\mu, \sigma^2) \\
\theta_1 > 0 &\to \text{positive correlation between } y_t \text{ & } y_{t+1} \\
\theta_1 < 0 &\to \text{negative correlation between } y_t \text{ & } y_{t+1}
\end{aligned}$$

$$\operatorname{Corr}(y_t, y_{t+1}) = \frac{\theta_1}{1 + \theta_1^2}$$

$$\operatorname{Corr}(y_t, y_{t+h}) = 0 \quad \text{for } h \ge 2$$

---

| **Sample ACF** | **Theoretical ACF for a stationary Time Series Model** |
| :--- | :--- |
| $y_1, \dots, y_n$
$\text{Sample ACF}(h) =$ Sample correlation between $y_t$ & $y_{t+h}$
$= \begin{pmatrix} (y_1, y_{1+h}) \\ (y_2, y_{2+h}) \\ \vdots \\ (y_{n-h}, y_n) \end{pmatrix}$ | $\rho(h) = \operatorname{Corr}(y_t, y_{t+h})$
$\to$ cannot depend on $t$ |

---

$(a_1, b_1), \dots, (a_m, b_m)$

$$\text{Correlation} = \frac{\sum_{i=1}^m (a_i - \bar{a})(b_i - \bar{b})}{\sqrt{\sum_{i=1}^m (a_i - \bar{a})^2 \sum_{i=1}^m (b_i - \bar{b})^2}}$$

$m = n - h$
$a_i = y_i$
$b_i = y_{i+h}$

$\bar{a} = \frac{1}{n-h} \sum_{i=1}^{n-h} y_i \approx \bar{y}$, $\quad \bar{b} = \frac{1}{n-h} \sum_{i=1}^{n-h} y_{i+h} \approx \bar{y}$

$$\frac{\sum_{t=1}^{n-h} (y_t - \bar{y})(y_{t+h} - \bar{y})}{\sqrt{\sum_{t=1}^{n-h} (y_t - \bar{y})^2 \sum_{t=1}^{n-h} (y_{t+h} - \bar{y})^2}}$$

Replace by $\sum_{t=1}^n (y_t - \bar{y})^2$

$$\text{Sample ACF}(h) = \frac{\sum_{t=1}^{n-h} (y_t - \bar{y})(y_{t+h} - \bar{y})}{\sqrt{\sum_{t=1}^n (y_t - \bar{y})^2 \sum_{t=1}^n (y_t - \bar{y})^2}}$$

$$= \frac{\sum_{t=1}^{n-h} (y_t - \bar{y})(y_{t+h} - \bar{y})}{\sum_{t=1}^n (y_t - \bar{y})^2} = \hat{\rho}(h) \longrightarrow \text{Calculated from Data}$$

---

Stationary Model: $\rho(h)$ : ACF of the model

**$MA(1)$ model:** $y_t = \mu + \varepsilon_t + \theta \varepsilon_{t-1}$

$$\rho(h) = \begin{cases} 1 & \text{if } h = 0 \\ \frac{\theta}{1 + \theta^2} & \text{if } |h| = 1 \\ 0 & \text{if } |h| \ge 2 \end{cases}$$

$\to$ looks like $MA(1)$

**$MA(q)$ model:** $y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \dots + \theta_q \varepsilon_{t-q}$
$\downarrow$
**ALWAYS CAUSAL & STATIONARY**

$$\to \rho(h) = \begin{cases} \text{something} & \text{if } |h| \le q \\ 0 & \text{if } |h| > q \end{cases}$$

---

---

[Up: contents](index.md) · [$MA(1)$ vs $AR(1)$ →](02-vs.md)
