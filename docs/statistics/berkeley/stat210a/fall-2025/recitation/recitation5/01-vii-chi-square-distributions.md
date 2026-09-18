---
title: VII Chi-Square Distributions
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation5.pdf
source_file: sources/berkeley-stat210a/fall-2025/recitation/recitation5.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`recitation/recitation5.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation/recitation5.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# VII Chi-Square Distributions

- A random variable $Y$ is called chi-square distribution with degree of freedom $k$ and is denoted by $\mathcal{X}^2(k)$ if one of the following equivalent conditions holds:

  (i) $Y \overset{d}{=} Z_1^2 + \cdots + Z_k^2$, where $Z_i \overset{iid}{\sim} N(0, 1)$.

  (ii) $Y \sim \text{Gamma}\left(\frac{k}{2}, 2\right)$

  (iii) The probability density function of $Y$ is
  $$p_Y(y) = \frac{1}{\Gamma\left(\frac{k}{2}\right) 2^{\frac{k}{2}}} \times y^{\frac{k}{2}-1} e^{-\frac{y}{2}}, \quad y > 0$$

  (iv) The moment generating function of $Y$ is
  $$M_Y(u) = (1-2u)^{-\frac{k}{2}}, \quad u < \frac{1}{2}$$

- A random variable $Y$ is called **non-central** chi-square distribution with degree of freedom $k$ and **non-centrality parameter $\delta > 0$** and is denoted by $\mathcal{X}^2(k; \delta)$ if one of the following equivalent conditions holds:

  (i) $Y \overset{d}{=} Z_1^2 + \cdots + Z_k^2$, where $Z_i \sim N(\mu_i, 1)$ and $\sum_{i=1}^k \mu_i^2 = \delta$

  (ii) $Y \overset{d}{=} V + Z^2$, where $V \sim \mathcal{X}^2(k-1)$ and $Z \sim N(\mu, 1)$ are independent and $\mu^2 = \delta$.

  (iii) The moment generating function of $Y$ is
  $$M_Y(u) = (1-2u)^{-\frac{k}{2}} \times \exp\left(\frac{\delta u}{1-2u}\right), \quad u < \frac{1}{2}$$

* $\mathbb{E}[Y] = k + \delta$, $\text{Var}(Y) = 2k + 4\delta$

* Suppose $Z \sim N_d(\mu, I)$ and $A$ is a symmetric matrix satisfying $A^2 = A$, $\text{tr}(A) = k$, and $\mu^T A \mu = \delta$. Then, $Z^T A Z \sim \mathcal{X}^2(k; \delta)$.

(pf) Consider the spectral decomposition of $A$:
$$A = PDP^T,$$
where $P$ is an orthogonal matrix ($PP^T = I = P^T P$) and $D$ is a diagonal matrix, $D = \text{diag}(\lambda_i)$.

Since $A^2 = A$, $\lambda_i = 0$ or $1$ for $i=1, \dots, d$.

Also, since $\text{tr}(A) = k$,
$$|\{i : \lambda_i = 1\}| = k.$$

WLOG, let $\lambda_1 = \cdots = \lambda_k = 1$ and $\lambda_{k+1} = \cdots = \lambda_d = 0$.

Note that
$$Z^T A Z = Z^T P D P^T Z = \sum_{i=1}^d \lambda_i (P^T Z)_i^2 = \sum_{i=1}^k (P^T Z)_i^2.$$

Because
$$P^T Z \sim N_d(P^T \mu, I) \quad \text{and}$$
$$\sum_{i=1}^k (P^T \mu)_i^2 = \mu^T P D P^T \mu = \mu^T A \mu = \delta,$$
we can derive that
$$Z^T A Z \sim \mathcal{X}^2(k; \delta).$$
$\square$

## VIII t distributions

- A random variable $Y$ is called $t$ distribution with degree of freedom $k$ and is denoted by $t(k)$ if
$$Y \overset{d}{=} \frac{Z}{\sqrt{V/k}},$$
where $Z \sim N(0, 1)$ and $V \sim \mathcal{X}^2(k)$ are independent

- A random variable $Y$ is called **non-central** $t$ distribution with degree of freedom $k$ and **non-centrality parameter $\delta > 0$** and is denoted by $t(k; \delta)$ if
$$Y \overset{d}{=} \frac{Z}{\sqrt{V/k}},$$
where $Z \sim N(\delta, 1)$ and $V \sim \mathcal{X}^2(k)$ are independent

## IX F distributions

- A random variable $Y$ is called $F$ distribution with degree of freedom $k_1$ and $k_2$ and is denoted by $F(k_1, k_2)$ if
$$Y \overset{d}{=} \frac{V_1 / k_1}{V_2 / k_2},$$
where $V_1 \sim \mathcal{X}^2(k_1)$ and $V_2 \sim \mathcal{X}^2(k_2)$ are independent

- A random variable $Y$ is called **non-central** $F$ distribution with degree of freedom $k_1$ and $k_2$ and **non-centrality parameter $\delta > 0$** and is denoted by $F(k_1, k_2; \delta)$ if
$$Y \overset{d}{=} \frac{V_1 / k_1}{V_2 / k_2},$$
where $V_1 \sim \mathcal{X}^2(k_1; \delta)$ and $V_2 \sim \mathcal{X}^2(k_2)$ are independent.

---

[Up: contents](index.md) · [VII Example →](02-vii-example.md)
