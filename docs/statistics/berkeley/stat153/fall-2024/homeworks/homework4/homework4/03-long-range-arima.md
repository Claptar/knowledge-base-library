---
title: Long-range ARIMA
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework4/homework4.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework4/homework4.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Long-range ARIMA

**Source:** [`homeworks/homework4/homework4.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework4/homework4.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

5. (1 pt)
Let $\nabla = 1 - B$ denote the difference operator. Suppose that $\nabla x_t
= 0$ for all $t$. Prove that $x_t$ must be a constant sequence.

6. (2 pts)
Suppose that $\nabla x_t = u$ for all $t$, where $u$ is an arbitrary constant.
Prove that $x_t$ must be a linear function of $t$, of the form $x_t = a + bt$.

7. (3 pts)
Suppose that $\nabla x_t = u + vt$ for all $t$, where $u,v$ are again arbitrary
constants. Prove that $x_t$ must be a quadratic function of $t$, of the form
$x_t = a + bt + ct^2$.

8. (1 pt)
Using Q6 and Q7, prove that if $\nabla^2 x_t = u$ for all $t$, where $u$ is a
constant, then $x_t$ must be a quadratic function of $t$.

9. (4 pts)
Consider an ARMA(1,1) model:
$$
(1 - \phi B) x_t = (1 + \theta B) w_t.
$$
Suppose that our estimates pass the "unit root test", $|\hat\phi|, |\hat\theta|
< 1$, which we will assume implicitly henceforth. Unravel the forecast iteration
described in lecture to show that the forecast $\hat{x}_{t+h | t}$ from this
ARMA model approaches zero as $h \to \infty$.

10. (2 pts)
Consider an ARMA(1,1) model, with intercept:
$$
(1 - \phi B) x_t = c + (1 + \theta B) w_t.
$$
Unravel the forecast iteration to show that $\hat{x}_{t+h | t}$ approaches a
nonzero constant as $h \to \infty$.

11. (Bonus)
Now consider the extension to ARIMA($1,d,1$):
$$
(1 - \phi B) \nabla^d x_t = c + (1 + \theta B) w_t.
$$
Use Q5--Q10 to argue the following:
- If $c = 0$ and $d = 1$, then $\hat{x}_{t+h | t}$ approaches a constant as $h
  \to \infty$.
- If $c = 0$ and $d = 2$, then $\hat{x}_{t+h | t}$ approaches a linear trend as
  $h \to \infty$.
- If $c \not= 0$ and $d = 1$, then $\hat{x}_{t+h | t}$ approaches a linear trend
  as $h \to \infty$.
- If $c \not= 0$ and $d = 2$, then $\hat{x}_{t+h | t}$ approaches a quadratic
  trend as $h \to \infty$.

---

[← Backshift commuting](02-backshift-commuting.md) · [Up: contents](index.md) · [Time series CV →](04-time-series-cv.md)
