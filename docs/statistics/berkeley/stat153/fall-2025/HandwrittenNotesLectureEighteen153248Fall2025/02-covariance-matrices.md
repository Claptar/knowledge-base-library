---
title: Covariance Matrices
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEighteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureEighteen153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureEighteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEighteen153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Covariance Matrices

$Y$: random variable $\mathbb{E}Y$, $\operatorname{var} Y$

$Y_1, \dots, Y_p$: $p$-random variables

$\underset{p \times 1}{Y} = \begin{pmatrix} Y_1 \\ \vdots \\ Y_p \end{pmatrix}$: Random vector

$$\mathbb{E}Y = \begin{pmatrix} \mathbb{E}Y_1 \\ \vdots \\ \mathbb{E}Y_p \end{pmatrix} : p \times 1$$

$$\underset{p \times p \text{ matrix}}{\operatorname{Cov}(Y)} = \begin{bmatrix} & & \\ & \cdot & \\ & & \end{bmatrix} \to \operatorname{Cov}(Y_i, Y_j)$$

(1) $\mathbb{E}(AY + b) = A(\mathbb{E}Y) + b$

(2) $\operatorname{Cov}(AY + b) = A(\operatorname{Cov} Y)A^T$

(3) $\operatorname{Cov}(AY + b, BW + d) = A \operatorname{Cov}(Y, W) B^T$

$\underset{p \times 1}{Y}$: random vector, $\underset{q \times 1}{W}$: another random vector

$\underset{p \times q}{\operatorname{Cov}(Y, W)}$ with $(i,j)^{\text{th}}$ entry $\operatorname{Cov}(Y_i, W_j)$

---

$$\operatorname{var}\left(y_{n+k} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$

$$\operatorname{Cov}\left( \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k} \end{pmatrix} \;\middle|\; \underset{\theta}{y_1, \dots, y_n} \right) = \underset{k \times k \text{ covariance matrix}}{\Gamma_k(\theta)}$$

$$\Gamma_1(\theta) = \operatorname{Cov}\left(y_{n+1} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$
$$= \operatorname{var}\left(y_{n+1} \mid \underset{\theta}{y_1, \dots, y_n}\right) = \sigma^2$$

$$[\sigma^2] \qquad \begin{bmatrix} \\ \end{bmatrix}_{2 \times 2} \qquad \begin{bmatrix} \\ \end{bmatrix}_{3 \times 3}$$

$$\Gamma_k(\theta) = \operatorname{Cov}\left( \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k} \end{pmatrix} \;\middle|\; \underset{\theta}{y_1, \dots, y_n} \right)$$

$(i,j)^{\text{th}}$ entry is $\operatorname{Cov}\left(y_{n+i}, y_{n+j} \mid \underset{\theta}{y_1, \dots, y_n}\right)$

$$\operatorname{Cov}\begin{pmatrix} y_{n+1} \\ y_{n+2} \\ y_{n+3} \end{pmatrix} = \begin{bmatrix} \operatorname{Cov}\begin{pmatrix} y_{n+1} \\ y_{n+2} \end{pmatrix} \\ \end{bmatrix}$$

$$= \begin{bmatrix}
\Gamma_{k-1}(\theta) & \vline & \gamma_k(\theta) \\
\hline
\gamma_k^T(\theta) & \vline & \cdot
\end{bmatrix}_{k \times k}$$

$$\gamma_k(\theta) = \operatorname{Cov}\left( \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k-1} \end{pmatrix}, y_{n+k} \;\middle|\; \underset{\theta}{y_1, \dots, y_n} \right)$$

---

$$= \operatorname{Cov}\left( \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k-1} \end{pmatrix}, \phi_0 + \phi_1 y_{n+k-1} + \phi_2 y_{n+k-2} + \dots + \phi_p y_{n+k-p} + \varepsilon_{n+k} \;\middle|\; \underset{\theta}{y_1, \dots, y_n} \right)$$

$$\downarrow$$
$$a_1 y_{n+1} + a_2 y_{n+2} + \dots + a_{k-1} y_{n+k-1}$$

---

$$\operatorname{var}\left(y_{n+1} \mid \underset{\theta}{y_1, \dots, y_n}\right) = \sigma^2$$

$$\operatorname{var}\left(y_{n+2} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$
$$= \operatorname{var}\left( \phi_0 + \phi_1 y_{n+1} + \phi_2 y_n + \dots + \varepsilon_{n+2} \mid \underset{\theta}{y_1, \dots, y_n} \right)$$
$$= \operatorname{var}\left( \phi_1 y_{n+1} + \varepsilon_{n+2} \mid \underset{\theta}{y_1, \dots, y_n} \right)$$
$$= \phi_1^2 \sigma^2 + \sigma^2$$

$$\operatorname{var}\left(y_{n+3} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$
$$= \operatorname{var}\left( \phi_1 y_{n+2} + \phi_2 y_{n+1} + \varepsilon_{n+3} \mid \underset{\theta}{y_1, \dots, y_n} \right)$$

---

$$\operatorname{Cov}\left( \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k-1} \end{pmatrix}, a_1 y_{n+1} + \dots + a_{k-1} y_{n+k-1} \;\middle|\; \underset{\theta}{y_1, \dots, y_n} \right)$$
$$a^T \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k-1} \end{pmatrix}$$
$$= \Gamma_{k-1}(\theta) a$$

---

$$\operatorname{Cov}(AY + b, BW + c) = A \operatorname{Cov}(Y, W) B^T$$

$$\Gamma_k(\theta) = \begin{bmatrix}
\Gamma_{k-1}(\theta) & \vline & \Gamma_{k-1}(\theta) a \\
\hline
a^T \Gamma_{k-1}(\theta) & \vline & \boxed{\phantom{x}}
\end{bmatrix}$$

$$\operatorname{var}\left(y_{n+k} \mid \underset{\theta}{y_1, \dots, y_n}\right)$$
$$= \operatorname{var}\left( \underbrace{\phi_1 y_{n+k-1} + \dots + \phi_p y_{n+k-p}}_{a^T \begin{pmatrix} y_{n+1} \\ \vdots \\ y_{n+k-1} \end{pmatrix}} + \varepsilon_{n+k} \;\middle|\; \underset{\theta}{y_1, \dots, y_n} \right)$$
$$= \sigma^2 + a^T \Gamma_{k-1}(\theta) a$$

$$\Gamma_k(\theta) = \begin{bmatrix}
\Gamma_{k-1}(\theta) & \vline & \Gamma_{k-1}(\theta) a \\
\hline
a^T \Gamma_{k-1}(\theta) & \vline & a^T \Gamma_{k-1}(\theta) a + \sigma^2
\end{bmatrix}$$

(1) $\Gamma_1(\theta) = \sigma^2$

(2) For each $k = 2, 3, \dots$
Calculate $a$ depending on $k, p$ & $\phi_1 \dots \phi_p$
$$\Gamma_k(\theta) = \begin{bmatrix}
\Gamma_{k-1}(\theta) & \Gamma_{k-1}(\theta) a \\
a^T \Gamma_{k-1}(\theta) & a^T \Gamma_{k-1}(\theta) a + \sigma^2
\end{bmatrix}$$

---

[← Lecture Eighteen](01-lecture-eighteen.md) · [Up: contents](index.md)
