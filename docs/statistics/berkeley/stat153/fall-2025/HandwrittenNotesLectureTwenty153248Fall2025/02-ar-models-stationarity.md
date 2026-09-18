---
title: AR models & Stationarity
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# AR models & Stationarity

$$AR(1): \quad y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t$$
$$\varepsilon_t \overset{\text{iid}}{\sim} N(0, \sigma^2)$$

Is this stationary?

$y_1 = \text{fixed at the observed value}$.

$$\prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma} \exp \left[ - \frac{(y_t - \phi_0 - \phi_1 y_{t-1})^2}{2\sigma^2} \right]$$

$$y_1$$
$$y_2 = \phi_0 + \phi_1 y_1 + \varepsilon_2$$
$$y_3 = \phi_0 + \phi_1 y_2 + \varepsilon_3 = \phi_0 + \phi_1(\phi_0 + \phi_1 y_1 + \varepsilon_2) + \varepsilon_3$$

---

$$= \phi_0(1 + \phi_1) + \phi_1^2 y_1 + \varepsilon_3 + \phi_1 \varepsilon_2$$

$$y_t = \phi_0(1 + \phi_1 + \dots + \phi_1^{t-2}) + \phi_1^{t-1} y_1 + \varepsilon_t + \phi_1 \varepsilon_{t-1} + \phi_1^2 \varepsilon_{t-2} + \dots + \phi_1^{t-2} \varepsilon_2$$

Suppose $|\phi_1| < 1$, then $y_t$ will be approximately equal to (at least for $t$ which are not small)

$$y_t = \phi_0(1 + \phi_1 + \phi_1^2 + \dots) + \varepsilon_t + \phi_1 \varepsilon_{t-1} + \phi_1^2 \varepsilon_{t-2} + \dots$$

$$y_t = \left( \frac{\phi_0}{1 - \phi_1} \right) + \sum_{j=0}^{\infty} \phi_1^j \varepsilon_{t-j}$$

$$y_t = \mu + \varepsilon_t + \theta_1 \varepsilon_{t-1} + \theta_2 \varepsilon_{t-2} + \dots + \theta_q \varepsilon_{t-q}$$
$$\theta_1 = \phi_1, \quad \theta_2 = \phi_1^2, \quad \dots, \quad \theta_q = \phi_1^q$$

$$\mathbb{E} \, y_t = \frac{\phi_0}{1 - \phi_1}$$

$$\operatorname{Cov}(y_t, y_{t+h}) = \frac{\sigma^2 \phi_1^{|h|}}{1 - \phi_1^2} \quad \text{CHECK}$$

$AR(1)$ **causal-stationary** when $|\phi_1| < 1$.

$$y_t = \frac{\phi_0}{1 - \phi_1} - \frac{\varepsilon_{t+1}}{\phi_1} - \frac{\varepsilon_{t+2}}{\phi_1^2} - \dots$$

---

When $|\phi_1| > 1$

$$y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t$$
$$y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t$$
$$\phi_1 y_{t-1} = -\phi_0 + y_t - \varepsilon_t$$
$$y_{t-1} = -\frac{\phi_0}{\phi_1} + \frac{y_t}{\phi_1} - \frac{\varepsilon_t}{\phi_1}$$

**CAUSAL STATIONARY** $AR(1) \iff |\phi_1| < 1$

---

---

[← Lecture Twenty](01-lecture-twenty.md) · [Up: contents](index.md) · [$AR(p)$ for $p \ge 1$ →](03-for.md)
