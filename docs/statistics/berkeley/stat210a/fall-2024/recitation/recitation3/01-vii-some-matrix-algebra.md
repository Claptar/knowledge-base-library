---
title: VII Some matrix algebra
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/recitation/recitation3.pdf
source_file: sources/berkeley-stat210a/fall-2024/recitation/recitation3.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`recitation/recitation3.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/recitation/recitation3.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# VII Some matrix algebra

## 1 Spectral decomposition

$A$: (real) symmetric $n \times n$ matrix

$\Rightarrow \exists$ $n \times n$ orthogonal matrix $P$ ($P P^T = I = P P^T$) and $n \times n$ diagonal matrix $D$ s.t.
$$A = P D P^T$$

If we write $P = \begin{pmatrix} \mid & & \mid \\ v_1 & \cdots & v_n \\ \mid & & \mid \end{pmatrix}$ and $D = \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix}$,

(i) $\{v_1, \dots, v_n\}$: orthonormal vectors

(ii) $v_i$ is an eigenvector of $A$ and $\lambda_i$ is a corresponding eigenvalue of $A$.

$$\begin{pmatrix}
A = P D P^T \Rightarrow A P = P D \\
\Rightarrow A \begin{pmatrix} \mid & & \mid \\ v_1 & \cdots & v_n \\ \mid & & \mid \end{pmatrix} = \begin{pmatrix} \mid & & \mid \\ v_1 & \cdots & v_n \\ \mid & & \mid \end{pmatrix} \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix} \\
\Rightarrow \begin{pmatrix} \mid & & \mid \\ A v_1 & \cdots & A v_n \\ \mid & & \mid \end{pmatrix} = \begin{pmatrix} \mid & & \mid \\ \lambda_1 v_1 & \cdots & \lambda_n v_n \\ \mid & & \mid \end{pmatrix}
\end{pmatrix}$$

(iii) $A = P D P^T = \begin{pmatrix} \mid & & \mid \\ v_1 & \cdots & v_n \\ \mid & & \mid \end{pmatrix} \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix} \begin{pmatrix} \text{---} & v_1^T & \text{---} \\ & \vdots & \\ \text{---} & v_n^T & \text{---} \end{pmatrix}$
$$= \sum_{i=1}^n \lambda_i v_i v_i^T$$

## 2 Positive semidefinite matrices and positive definite matrices

$A$: symmetric $n \times n$ matrix
$$\left( A = P D P^T \quad \left[ \begin{aligned} P &= \begin{pmatrix} \mid & & \mid \\ v_1 & \cdots & v_n \\ \mid & & \mid \end{pmatrix} : \text{orthogonal matrix} \\ D &= \begin{pmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{pmatrix} : \text{diagonal matrix} \end{aligned} \right. \right)$$

(i) We say $A$ is positive semidefinite if
$$x^T A x \ge 0 \quad \text{for all } x \in \mathbb{R}^n$$

* All eigenvalues are nonnegative
$$\left(0 \le v_i^T A v_i = \lambda_i \quad \text{for } i = 1, \dots, n\right)$$

* $\exists B: n \times n \text{ matrix s.t. } A = B B^T$
$$(B = P D^{\frac{1}{2}}, \text{ where } D^{\frac{1}{2}} = \begin{pmatrix} \lambda_1^{\frac{1}{2}} & & 0 \\ & \ddots & \\ 0 & & \lambda_n^{\frac{1}{2}} \end{pmatrix})$$

* $\exists C: n \times n \text{ symmetric matrix s.t. } A = C^2$
$$(C = P D^{\frac{1}{2}} P^T)$$
We sometime write $C$ as $A^{\frac{1}{2}}$

(ii) We say $A$ is positive definite if
$$x^T A x > 0 \quad \text{for all } x \in \mathbb{R}^n$$

* All eigenvalues are positive
$$\left(0 < v_i^T A v_i = \lambda_i \quad \text{for } i = 1, \dots, n\right)$$

* $A$ is invertible
$$(A^{-1} = P D^{-1} P^T)$$

* $\exists B: n \times n \text{ invertible matrix s.t. } A = B B^T$
$$(B = P D^{\frac{1}{2}}, \text{ where } D^{\frac{1}{2}} = \begin{pmatrix} \lambda_1^{\frac{1}{2}} & & 0 \\ & \ddots & \\ 0 & & \lambda_n^{\frac{1}{2}} \end{pmatrix})$$

* $\exists C: n \times n \text{ invertible symmetric matrix s.t. } A = C^2$
$$(C = P D^{\frac{1}{2}} P^T)$$

---

---

[Up: contents](index.md) · [VII Multivariate normal distributions →](02-vii-multivariate-normal-distributions.md)
