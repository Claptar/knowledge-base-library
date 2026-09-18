---
title: Lecture Twenty
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Lecture Twenty

**Stationarity:** $\mathbb{E} \, y_t$ does not change with time $t$
$\operatorname{var} \, y_t$ also does not change with $t$
$\operatorname{Cov}(y_t, y_{t+h})$ also does not change with $t$ (for fixed $h$)

**Eg:** $\varepsilon_t \overset{\text{iid}}{\sim} N(0, \sigma^2)$

$$y_t = \mu + \varepsilon_t + \theta \varepsilon_{t-1} \quad \text{all } t$$

$\mu, \theta, \sigma$

$MA(1)$
moving average

Slutzky
'Summation of Random Causes'

$$\varepsilon_0, \, \varepsilon_1, \, \varepsilon_2, \, \varepsilon_3, \, \dots$$

$$y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \dots + \theta_q \varepsilon_{t-q}$$
$$MA(q)$$

$$\mathbb{E} \, y_t = \mu$$
$$\operatorname{var}(y_t) = \sigma^2(1 + \theta^2)$$
$$\begin{aligned}
\operatorname{Cov}(y_t, y_{t+1}) &= \operatorname{Cov}(\mu + \varepsilon_t + \theta \varepsilon_{t-1}, \, \mu + \varepsilon_{t+1} + \theta \varepsilon_t) \\
&= \operatorname{Cov}(\varepsilon_t, \, \theta \varepsilon_t) \\
&= \theta \sigma^2
\end{aligned}$$

---

$$\begin{aligned}
\operatorname{Cov}(y_t, y_{t+2}) &= \operatorname{Cov}(\mu + \varepsilon_t + \theta \varepsilon_{t-1}, \, \mu + \varepsilon_{t+2} + \theta \varepsilon_{t+1}) \\
&= 0
\end{aligned}$$

$$\operatorname{Cov}(y_t, y_{t+h}) = 0 \quad \text{for } h \ge 2$$

$$\gamma(h) = \begin{cases}
\sigma^2(1 + \theta^2) & \text{if } h = 0 \\
\theta \sigma^2 & \text{if } |h| = 1 \\
0 & \text{if } |h| > 1
\end{cases}$$

ACF:
$$\rho(h) = \frac{\gamma(h)}{\gamma(0)} = \begin{cases}
1 & \text{if } h = 0 \\
\frac{\theta}{1 + \theta^2} & \text{if } |h| = 1 \\
0 & \text{if } |h| > 1
\end{cases}$$

---

---

[Up: contents](index.md) · [AR models & Stationarity →](02-ar-models-stationarity.md)
