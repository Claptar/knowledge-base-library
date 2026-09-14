---
title: Stationarity
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework1/homework1.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Stationarity

**Source:** [`homeworks/homework1/homework1.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

8. (3 pts)
Compute the mean, variance, auto-covariance, and auto-correlation functions for
the process
$$
x_t = w_t w_{t-1},
$$
where each $w_t \sim N(0, \sigma^2)$, independently. Is $x_t$, $t = 1,2,3,\dots$
stationary?

9. (3 pts)
Repeat the same calculations in Q8, but where each $w_t \sim N(\mu, \sigma^2)$,
independently, for $\mu \not= 0$. Is $x_t$, $t = 1,2,3,\dots$ stationary?

10. (3 pts)
Simulate the processes from Q8 (with $\mu = 0$) and Q9 (with $\mu \not= 0$),
yielding two time series of length 200, and plot the results. Compute the sample
mean and sample variance for each one (to be clear, this is just a sample mean of
all data, over all time, and similarly for the variance), and check that these
are close to the population mean and variance from Q8 and Q9. Also compute and
plot the sample auto-correlation function using `acf()`, and check again that it
agrees with the population auto-correlation function from Q8 and Q9.

11. (2 pts)
Give an example of a weakly stationary process that is not strongly stationary.

12. (Bonus)
A function $\kappa$ is said to be *positive semidefinite* (PSD) provided that
$$
\sum_{i,j=1}^n a_i a_j \kappa(t_i - t_j) \geq 0, \quad \text{for all $n \geq 1$,
all $a_1,\dots,a_n$, and all $t_1,\dots,t_n$}.
$$
Prove that if $x_t$, $t = 1,2,3,\dots$ is stationary, and $\gamma_x(h)$ is its
auto-covariance function (as a function of lag $h$), then $\gamma_x$ is PSD.
You may use whatever elementary probability and/or linear algebra facts that you
would like, as long as you state clearly what you are using.

13. (Bonus)
Prove moreover that the sample auto-covariance function $\hat\gamma_x$ defined
in lecture is also PSD.

---

[← Random walks](03-random-walks.md) · [Up: contents](index.md) · [Joint stationarity →](05-joint-stationarity.md)
