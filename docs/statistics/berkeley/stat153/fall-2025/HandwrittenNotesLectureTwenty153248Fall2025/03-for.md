---
title: $AR(p)$ for $p \ge 1$
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwenty153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# $AR(p)$ for $p \ge 1$

$$y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \varepsilon_t$$

$y_1, y_2 \qquad y_3, y_4, \dots$

**BACKSHIFT TRICK**

---

## BACKSHIFT OPERATOR

$$B y_t = y_{t-1}$$
$$B^2 y_t = B(B y_t) = B y_{t-1} = y_{t-2}$$
$$B^k y_t = y_{t-k}, \qquad B^{-3} y_t = y_{t+3}$$

$$B^0 y_t = y_t$$
$$B^0 = I$$

$$(B + 2 B^3) y_t = y_{t-1} + 2 y_{t-3}$$

---

## $AR(p)$ model using Backshift Notation:

$$y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \varepsilon_t$$

$$y_t - \phi_1 y_{t-1} - \phi_2 y_{t-2} - \dots - \phi_p y_{t-p} = \phi_0 + \varepsilon_t$$

$$y_t - \phi_1 B y_t - \phi_2 B^2 y_t - \dots - \phi_p B^p y_t = \phi_0 + \varepsilon_t$$

$$(I - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p) y_t = \phi_0 + \varepsilon_t$$

$\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p :$ AR polynomial

$$\phi(B) y_t = \phi_0 + \varepsilon_t \to AR(p) \text{ model}$$

**$AR(1)$:** $\phi(B) = I - \phi_1 B$

$$\phi(z) = 1 - \phi_1 z$$

$$(I - \phi_1 B) y_t = \phi_0 + \varepsilon_t$$

$$y_t = \left(\frac{1}{I - \phi_1 B}\right) (\phi_0 + \varepsilon_t)$$

$$\frac{1}{1 - \phi_1 z} = 1 + \phi_1 z + (\phi_1 z)^2 + (\phi_1 z)^3 + \dots$$

$$= (I + \phi_1 B + \phi_1^2 B^2 + \phi_1^3 B^3 + \dots)(\phi_0 + \varepsilon_t)$$
$$= (I + \phi_1 B + \phi_1^2 B^2 + \dots)\phi_0 + (I + \phi_1 B + \phi_1^2 B^2 + \dots)\varepsilon_t$$

---

$$= \phi_0(1 + \phi_1 + \phi_1^2 + \dots) + \varepsilon_t + \phi_1 \varepsilon_{t-1} + \phi_1^2 \varepsilon_{t-2} + \dots$$

$$y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^{\infty} \phi_1^j \varepsilon_{t-j} \longleftrightarrow y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t$$

---

## $AR(2)$

$$y_t = \phi_0 + \phi_1 y_{t-1} + \phi_2 y_{t-2} + \varepsilon_t$$

$$\phi(z) = 1 - \phi_1 z - \phi_2 z^2$$

$$\phi(B) y_t = \phi_0 + \varepsilon_t$$

$$\Rightarrow y_t = \frac{1}{\phi(B)} (\phi_0 + \varepsilon_t)$$

$$= \left( \frac{1}{I - \phi_1 B - \phi_2 B^2} \right) (\phi_0 + \varepsilon_t)$$

$$\phi(z) = 1 - \phi_1 z - \phi_2 z^2 = (1 - a_1 z)(1 - a_2 z)$$

$\frac{1}{a_1}, \frac{1}{a_2}$ denote roots of $\phi(z)$.

$$= \frac{1}{(I - a_1 B)(I - a_2 B)} (\phi_0 + \varepsilon_t)$$

$$= (I + a_1 B + a_1^2 B^2 + a_1^3 B^3 + \dots)(I + a_2 B + a_2^2 B^2 + \dots)(\phi_0 + \varepsilon_t)$$

---

$$= \mu + \sum_{j=0}^{\infty} \psi_j \varepsilon_{t-j} \quad \text{for some } \{\psi_j\}.$$
$$\mu = \phi_0 \sum_{j=0}^{\infty} \psi_j$$

$$\psi_1 = a_1 + a_2$$
$$\psi_2 = a_1^2 + a_2^2 + a_1 a_2$$
$$\psi_3 =$$

**Need:** $a_1, a_2$ to have moduli strictly smaller than $1$.

---

**$AR(1)$:** $y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t$
When does it have a causal stationary solution?
$$|\phi_1| < 1$$

**$AR(p)$:** $y_t = \phi_0 + \phi_1 y_{t-1} + \dots + \phi_p y_{t-p} + \varepsilon_t$
When does it have a causal stationary solution?
AR polynomial: $1 - \phi_1 z - \phi_2 z^2 - \dots - \phi_p z^p$.
Calculate roots of the polynomial: $\frac{1}{a_1}, \dots, \frac{1}{a_p}$
**Check:** $|a_j| < 1$ for every $j$

**Note:** When $p = 1$, AR polynomial $1 - \phi_1 z$
$$\text{root}: \frac{1}{\phi_1} \qquad a_1 = \phi_1$$

$$\frac{1}{I - a_1 B} = I + a_1 B + (a_1 B)^2 + \dots$$

---

$$\frac{1}{I - a_2 B} = I + a_2 B + (a_2 B)^2 + \dots$$

$$\{I + a_1 B + (a_1 B)^2 + \dots\}\{I + a_2 B + (a_2 B)^2 + \dots\}$$
$$= I + (a_1 + a_2)B + (a_1^2 + a_1 a_2 + a_2^2)B^2 + (\qquad)B^3 + \dots$$
$$= (I + \psi_1 B + \psi_2 B^2 + \psi_3 B^3 + \dots)(\phi_0 + \varepsilon_t)$$
$$\psi_0 = 1$$

$$\sum_{j=0}^{\infty} \psi_j \varepsilon_{t-j}$$

$$\phi_0 \sum \psi_j$$

---

[← AR models & Stationarity](02-ar-models-stationarity.md) · [Up: contents](index.md)
