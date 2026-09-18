---
title: More Nonlinear Regression Models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureNine153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# More Nonlinear Regression Models

### (1) Two or more sinusoids

$$y_t = \beta_0 + \beta_{11} \cos 2\pi f_1 t + \beta_{12} \sin 2\pi f_1 t + \beta_{21} \cos 2\pi f_2 t + \beta_{22} \sin 2\pi f_2 t + \varepsilon_t$$

$$\boxed{f_1, f_2}$$

$$RSS(f_1, f_2) = \operatorname{argmin}_\beta \|y - X_{f_1, f_2} \beta\|^2$$

$$X = \begin{bmatrix} 1 & \cos 2\pi f_1 t & \sin 2\pi f_1 t & \cos 2\pi f_2 t & \sin 2\pi f_2 t \\ \vdots & & & & \end{bmatrix}$$

$$(\hat{f}_1, \hat{f}_2) = \operatorname{argmin}_{f_1, f_2} RSS(f_1, f_2)$$

$$\text{posterior}(f_1, f_2) \propto \left(\frac{1}{RSS(f_1, f_2)}\right)^{\frac{n-5}{2}} |X_{f_1, f_2}^T X_{f_1, f_2}|^{-1/2} I\left(0 < f_1, f_2 < \frac{1}{2}\right)$$

(1) Restrict both $f_1$ & $f_2 \in (0, \frac{1}{2})$ to Fourier frequencies

(2) Take another possibly denser grid for both $f_1$ & $f_2$.

---

If $f_1$ & $f_2$ are distinct Fourier frequencies in $(0, \frac{1}{2})$ (e.g. $f_1 = \frac{j_1}{n}$, $f_2 = \frac{j_2}{n}$, $j_1 \neq j_2$)

$$RSS(f_1, f_2) = \sum_{t=0}^{n-1} (y_t - \bar{y})^2 - 2 I(f_1) - 2 I(f_2)$$

$\to$ happens because of orthogonality of sinusoids at Fourier frequencies.

$$X_{f_1, f_2}^T X_{f_1, f_2} = \begin{bmatrix} n & & & & \\ & \frac{n}{2} & & 0 & \\ & & \frac{n}{2} & & \\ & 0 & & \frac{n}{2} & \\ & & & & \frac{n}{2} \end{bmatrix}$$

$RSS(f_1, f_2)$ is minimized when $f_1$ & $f_2$ are the top two maximizers of the periodogram:

$$I\left(\frac{1}{n}\right), I\left(\frac{2}{n}\right), \dots, I(\quad)$$

$$I\left(\frac{10}{n}\right) : \hat{f}_1 = \frac{10}{n}$$
$$I\left(\frac{8}{n}\right) : \hat{f}_2 = \frac{8}{n}$$

## Change of Slope Model

### (1) $y_t = \beta_0 + \beta_1 t + \beta_2 (t - c)_+ + \varepsilon_t$

$$RSS(c)$$

---

### (2) $y_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ + \beta_3 (t - c_2)_+ + \varepsilon_t$

$$\begin{array}{ccc}
\text{slope } \beta_1 & \beta_1 + \beta_2 & \beta_1 + \beta_2 + \beta_3 \\
\hline
& c_1 & c_2
\end{array}$$

$$\boxed{RSS(c_1, c_2)}$$

### (3) $c_1, c_2, c_3$
$$RSS(c_1, c_2, c_3)$$

$$y_t = \beta_0 + \beta_1 t + \beta_2 (t - 2)_+^{\downarrow} + \beta_3 (t - 3)_+^{\downarrow} + \dots + \beta_{n-1} (t - (n-1))_+ + \varepsilon_t$$

$$\longrightarrow \text{High-dimensional Linear Regression Model}$$

$$\boxed{RSS = 0} \quad \boxed{\textbf{Regularized}} \text{ Estimation}$$

(1) minimize $\left[ \text{Least squares} + \text{penalty} \right]$

---

(2) $\beta_0, \beta_1, \beta_2, \dots, \beta_{n-1} \stackrel{iid}{\sim} \text{Unif}(-C, C)$
more informative
$\text{Unif}(-\tau, \tau)$
for some $\boxed{\tau}$

---

[← Introduction](01-introduction.md) · [Up: contents](index.md)
