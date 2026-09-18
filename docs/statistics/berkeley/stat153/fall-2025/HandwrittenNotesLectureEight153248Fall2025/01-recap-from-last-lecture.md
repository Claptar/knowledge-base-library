---
title: Recap from last lecture
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Recap from last lecture

$$y_t = \beta_0 + \beta_1 \cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t$$
$$\begin{matrix} y_1, \dots, y_n & \quad & \downarrow \qquad t = 1, \dots, n \\ & & \text{main} \\ & & \text{parameters} \end{matrix} \qquad \epsilon_t \overset{iid}{\sim} N(0, \sigma^2)$$

$$RSS(f) = \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n \left[y_t - \beta_0 - \beta_1 \cos 2\pi f t - \beta_2 \sin 2\pi f t\right]^2$$

We can restrict $f$ to $[0, 0.5]$

$$\left[ \begin{array}{l} \text{Take a grid of } f\text{-values.} \\ \text{Compute } RSS(f) \\ \text{Minimize to obtain } \hat{f}. \end{array} \right.$$

For efficient computation, we need a more explicit expression for $RSS(f)$.

Fourier Frequencies: $f \in [0, 0.5]$
($nf$ must be an integer)

$$\begin{cases} \{0, \frac{1}{n}, \frac{2}{n}, \frac{3}{n}, \dots, \frac{n-1}{2n}\} & \text{if } n \text{ is odd} \\ \{0, \frac{1}{n}, \frac{2}{n}, \frac{3}{n}, \dots, \frac{n/2}{n}\} & \text{if } n \text{ is even} \end{cases}$$

**LAST CLASS, we derived**

$RSS(f) =$
when $f$ is a Fourier frequency & $0 < f < \frac{1}{2}$

---

$$\sum_{t=1}^n (y_t - \bar{y})^2 - \frac{2}{n} \left(\sum_{t=1}^n y_t \cos 2\pi f t\right)^2 - \frac{2}{n} \left(\sum_{t=1}^n y_t \sin 2\pi f t\right)^2$$

$$y \cdot \cos = \sum_{t=1}^n y_t \cos 2\pi f t$$
$$y \cdot \sin = \sum_{t=1}^n y_t \sin 2\pi f t$$

$$RSS(f) = \sum_{t=1}^n (y_t - \bar{y})^2 - \frac{2}{n} \left[(y \cdot \cos)^2 + (y \cdot \sin)^2\right]$$

$$I(f) = \frac{1}{n} \left\{(y \cdot \cos)^2 + (y \cdot \sin)^2\right\} \quad \begin{array}{l} 0 < f < \frac{1}{2} \\ f \text{ is a} \\ \text{Fourier frequency} \end{array}$$

$$RSS(f) = \sum_{t=1}^n (y_t - \bar{y})^2 - 2\, I(f)$$

$\downarrow$ **Periodogram**

$$\text{Minimizing } RSS(f) \text{ over Fourier frequencies} \iff \text{Maximizing } I(f) \text{ over Fourier frequencies}$$

$$I(f) = \frac{1}{n} \left[(y \cdot \cos)^2 + (y \cdot \sin)^2\right]$$

$$[e^{i\theta} = \cos\theta + i\sin\theta]$$

$$\sum_{t=1}^n y_t e^{-2\pi i f t} = y \cdot e^{2\pi i f t}$$

---

$$I(f) = \frac{1}{n} \left| y \cdot e^{2\pi i f t} \right|^2$$
$$\begin{array}{ll} \text{Real part:} & y \cdot \cos \\ \text{Imaginary part:} & -\, y \cdot \sin \end{array}$$

**Dot product between complex vectors:**
$$a = (a_1, \dots, a_n) \qquad b = (b_1, \dots, b_n)$$
$$a \cdot b = \langle a, b \rangle = \sum_{j=1}^n a_j \, \overline{b_j} \to \begin{array}{l} \text{complex} \\ \text{conjugate} \\ \text{of } b_j \end{array}$$

$$y \cdot e^{2\pi i f t} = \sum_{t=1}^n y_t e^{-2\pi i f t}$$

**Periodogram:** $I(f) = \frac{1}{n} \left| y \cdot e^{2\pi i f t} \right|^2$

## DFT (Discrete Fourier Transform)

Data $y_0, y_1, \dots, y_{n-1}$ (often represented by the vector $y$)

DFT:
$$b_j = \sum_{t=0}^{n-1} y_t \exp\left(-2\pi i \frac{j}{n} t\right) = y \cdot \exp\left(2\pi i \frac{j}{n} t\right)$$
$\uparrow$
represents the Fourier frequency $\frac{j}{n}$

---

$$y = (y_0, \dots, y_{n-1})$$
$$u^j = (\exp(2\pi i \frac{j}{n} t), \, t = 0, 1, \dots, n-1)$$
$\hookrightarrow$ Data coming from the complex sinusoid of frequency $\frac{j}{n}$.

$$b_j = y \cdot u^j = \langle y, u^j \rangle$$

---

[Up: contents](index.md) · [Indexing starting at 0 vs 1 →](02-indexing-starting-at-0-vs-1.md)
