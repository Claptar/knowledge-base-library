---
title: Proof of IDFT
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/HandwrittenNotesLectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`HandwrittenNotesLectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureEight153248Fall2025.pdf) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Proof of IDFT

We use **orthogonality of complex sinusoid vectors.**
$$u^j = (\exp(2\pi i \frac{j}{n} t), \, t = 0, 1, \dots, n-1) \qquad j = 0, 1, \dots, n-1$$
$$= (1, \, \exp(2\pi i \frac{j}{n}(1)), \, \exp(2\pi i \frac{j}{n}(2)), \dots, \exp(2\pi i \frac{j}{n}(n-1)))$$

$$b_j = \langle y, u^j \rangle \to \text{Defn of DFT}$$

**FACT:** $u^0, u^1, \dots, u^{n-1}$ satisfy:

$$\langle u^j, u^k \rangle = \begin{cases} 0 & \text{if } j \neq k \\ n & \text{if } j = k \end{cases}$$

$$\exp(2\pi i f t)$$
$$u^0, u^1, \dots, u^{n-1} \to \text{vectors of length } n$$
$$\text{orthogonal & constant length}$$

$$\Downarrow$$
they form a basis for all vectors of length $n$.
$$\Downarrow$$
every vector can be written as a linear combination of $u^0, u^1, \dots, u^{n-1}$

---

$$y = a_0 u^0 + a_1 u^1 + \dots + a_{n-1} u^{n-1}$$

Take inner product on both sides with $u^j$:
$$\begin{aligned}
\langle y, u^j \rangle &= a_0 \langle u^0, u^j \rangle + a_1 \langle u^1, u^j \rangle \\
&\quad + \dots + a_{n-1} \langle u^{n-1}, u^j \rangle \\
&= a_j \langle u^j, u^j \rangle = a_j n
\end{aligned}$$

$$\implies a_j = \frac{1}{n} \langle y, u^j \rangle = \frac{b_j}{n}$$

We proved:
$$y = \frac{b_0}{n} u^0 + \frac{b_1}{n} u^1 + \dots + \frac{b_{n-1}}{n} u^{n-1}$$
$$\implies y_t = \frac{b_0}{n} u_t^0 + \frac{b_1}{n} u_t^1 + \dots + \frac{b_{n-1}}{n} u_t^{n-1}$$

$$y_t = \frac{1}{n} \sum_{j=0}^{n-1} b_j \exp\left(2\pi i \frac{j}{n} t\right) \to \textbf{Inverse DFT}$$

$$\begin{array}{ccc} \text{Data} & \longrightarrow & \text{DFT} \\ \substack{\text{\textbf{TIME}} \\ \text{\textbf{DOMAIN}} \\ \text{\textbf{ANALYSIS}}} & & \substack{\text{Modeling} \\ b_j} \\ y_t & & \end{array} \quad \begin{pmatrix} \text{\textbf{FREQUENCY}} \\ \text{\textbf{DOMAIN}} \\ \text{\textbf{ANALYSIS}} \end{pmatrix}$$

---

[← More on DFT](03-more-on-dft.md) · [Up: contents](index.md)
