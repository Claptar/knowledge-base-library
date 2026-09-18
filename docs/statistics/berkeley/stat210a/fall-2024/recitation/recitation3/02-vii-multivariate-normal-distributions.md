---
title: VII Multivariate normal distributions
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/recitation/recitation3.pdf
source_file: sources/berkeley-stat210a/fall-2024/recitation/recitation3.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`recitation/recitation3.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/recitation/recitation3.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# VII Multivariate normal distributions

## Equivalent definitions

### 1 $Z: n\text{-dimensional random variable}$
We say $Z \sim N_n(0, I_n)$ if
$$Z = (Z_1, \dots, Z_n)^T, \quad \text{where } Z_i \overset{iid}{\sim} N(0, 1)$$
*(Note: $0 = (0, \dots, 0)^T$, $I_n$ is $n \times n$ identity matrix)*

### 2 $X: n\text{-dimensional random variable}$
We say $X \sim N_n(\mu, \Sigma)$ if
*(where $\mu \in \mathbb{R}^n$, $\Sigma$ is an $n \times n$ positive semi-definite matrix)*

(i) $X = A Z + \mu$, where $Z \sim N(0, I_n)$ and $A A^T = \Sigma$

(ii) $X = \Sigma^{\frac{1}{2}} Z + \mu$, where $Z \sim N(0, I_n)$

(iii) $M_X(u) = \exp\{\mu^T u + \frac{1}{2} u^T \Sigma u\}$ for $u \in \mathbb{R}^n$
*(moment generating function of $X$)*

if $\Sigma$ is invertible

(iv) $p_X(x) = |2\pi \Sigma|^{-\frac{1}{2}} \exp\left\{-\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu)\right\}$ for $x \in \mathbb{R}^n$

---

## Properties

* Suppose $X \sim N(\mu, \Sigma)$.
For a $m \times n$ matrix $A$ and $b \in \mathbb{R}^m$,
$$A X + b \sim N(A\mu + b, A\Sigma A^T)$$

$$\begin{pmatrix}
X = \Sigma^{\frac{1}{2}} Z + \mu, \quad \text{where } Z \sim N(0, I_n) \\
A X + b = A \Sigma^{\frac{1}{2}} Z + (A\mu + b) \\
(A \Sigma^{\frac{1}{2}})(A \Sigma^{\frac{1}{2}})^T = A \Sigma A^T

* If $\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \sim N\left(\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}\right)$
and $\operatorname{cov}(X_1, X_2) = \Sigma_{12} = 0$,
then $X_1$ and $X_2$ are independent.

In other words, if $X_1$ and $X_2$ are jointly normal and $\operatorname{Cov}(X_1, X_2) = 0$, then they are independent.

$$\begin{pmatrix}
M_{X_1, X_2}(u_1, u_2) \\
= \exp\left[\begin{pmatrix} \mu_1^T & \mu_2^T \end{pmatrix} \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} + \frac{1}{2} \begin{pmatrix} u_1^T & u_2^T \end{pmatrix} \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix} \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}\right] \\
= \exp\left\{\mu_1^T u_1 + \frac{1}{2} u_1^T \Sigma_{11} u_1\right\} \\
\quad \times \exp\left\{\mu_2^T u_2 + \frac{1}{2} u_2^T \Sigma_{22} u_2\right\}
*(using $\Sigma_{12} = 0$, $\Sigma_{21} = 0$)*

* Suppose $X \sim N(\mu, \Sigma)$
For matrices $A$ and $B$, if $\operatorname{Cov}(AX, BX) = 0$,
then $AX$ and $BX$ are independent.

$$\left(\begin{pmatrix} AX \\ BX \end{pmatrix} = \begin{pmatrix} A \\ B \end{pmatrix} X \Rightarrow \text{jointly normal}\right)$$

* If $\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \sim N\left(\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}\right)$,
then $X_1 \sim N(\mu_1, \Sigma_{11})$

$$\begin{pmatrix}
X_1 = \begin{pmatrix} I & 0 \end{pmatrix} \begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \\
\Rightarrow X_1 \sim N\left(\begin{pmatrix} I & 0 \end{pmatrix}\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \begin{pmatrix} I & 0 \end{pmatrix} \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix} \begin{pmatrix} I \\ 0 \end{pmatrix}\right)

* If $\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \sim N\left(\begin{pmatrix} \mu_1 \\ \mu_2 \end{pmatrix}, \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}\right)$
and $\begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix}$ is invertible,
then $X_2 \mid X_1 = x_1 \sim N(\mu_2 + \Sigma_{21}\Sigma_{11}^{-1}(x_1 - \mu_1), \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})$

$$\begin{pmatrix}
\begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix} : \text{positive definite} \\
\Rightarrow \Sigma_{11} : \text{positive definite} \\
\Rightarrow \Sigma_{11} : \text{invertible} \\
\begin{pmatrix} X_1 - \mu_1 \\ X_2 - \mu_2 - \Sigma_{21}\Sigma_{11}^{-1}(X_1 - \mu_1) \end{pmatrix} = \begin{pmatrix} I & 0 \\ -\Sigma_{21}\Sigma_{11}^{-1} & I \end{pmatrix} \begin{pmatrix} X_1 - \mu_1 \\ X_2 - \mu_2 \end{pmatrix} \\
\begin{pmatrix} I & 0 \\ -\Sigma_{21}\Sigma_{11}^{-1} & I \end{pmatrix} \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{pmatrix} \begin{pmatrix} I & 0 \\ -\Sigma_{21}\Sigma_{11}^{-1} & I \end{pmatrix}^T \\
= \begin{pmatrix} \Sigma_{11} & 0 \\ 0 & \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12} \end{pmatrix}

$$\begin{pmatrix}
\Rightarrow X_1 - \mu_1 \text{ and } X_2 - \mu_2 - \Sigma_{21}\Sigma_{11}^{-1}(X_1 - \mu_1) \\
\text{are independent} \\
\Rightarrow X_2 - \mu_2 - \Sigma_{21}\Sigma_{11}^{-1}(X_1 - \mu_1) \mid X_1 = x_1 \\
\sim N(0, \Sigma_{22} - \Sigma_{21}\Sigma_{11}^{-1}\Sigma_{12})

* If $X \sim N_k(\mu, \Sigma)$ and $\Sigma$ is invertible, then
$$(X - \mu)^T \Sigma^{-1} (X - \mu) \sim \chi^2(k)$$

$$\begin{pmatrix}
X = \Sigma^{\frac{1}{2}} Z + \mu, \quad \text{where } Z \sim N_k(0, I) \\
(X - \mu)^T \Sigma^{-1} (X - \mu) = Z^T Z \\
= Z_1^2 + \dots + Z_k^2 \sim \chi^2(k)

---

[← VII Some matrix algebra](01-vii-some-matrix-algebra.md) · [Up: contents](index.md)
