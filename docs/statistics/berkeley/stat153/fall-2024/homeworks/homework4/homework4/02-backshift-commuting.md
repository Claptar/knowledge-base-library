---
title: Backshift commuting
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework4/homework4.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework4/homework4.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Backshift commuting

**Source:** [`homeworks/homework4/homework4.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework4/homework4.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

1. (1 pt)
Let $B$ denote the backshift operator. Given any integers $k,\ell \geq 0$,
explain why $B^k B^\ell = B^\ell B^k$.

2. (2 pts)
Using Q1, if $\phi_1,\dots,\phi_k$ and $\varphi_1,\dots,\varphi_\ell$ are any
coefficients, show that
$$
(1 + \phi_1 B + \cdots + \phi_k B^k)
(1 + \varphi_1 B + \cdots + \varphi_\ell B^\ell) =
(1 + \varphi_1 B + \cdots + \varphi_\ell B^\ell)
(1 + \phi_1 B + \cdots + \phi_k B^k)
$$

3. (2 pts)
Verify the result in Q2 with a small code example.

4. (3 pts)
Using Q2, show that we can write a SARIMA model equivalently as
$$
\phi(B) \Phi(B^s) \nabla^d \nabla_s^D x_t =
\theta(B) \Theta(B^s) w_t
$$
and
$$
\Phi(B^s) \phi(B) \nabla_s^D \nabla^d x_t =
\Theta(B^s) \theta(B) w_t.
$$

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Long-range ARIMA →](03-long-range-arima.md)
