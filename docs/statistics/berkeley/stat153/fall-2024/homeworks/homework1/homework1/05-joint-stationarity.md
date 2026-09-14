---
title: Joint stationarity
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework1/homework1.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Joint stationarity

**Source:** [`homeworks/homework1/homework1.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

\def\eqd{\overset{d}{=}}

Notions of joint stationarity, between two time series, can be defined in an
analogous way to how we defined stationarity in lecture. We say that two time
series $x_t$, $t = 1,2,3,\dots$ and $y_t$, $t = 1,2,3,\dots$ are *strongly
jointly stationary* provided that:
\begin{multline*}
(x_{s_1}, x_{s_2}, \dots, x_{s_k}, y_{t_1}, y_{t_2}, \dots, y_{t_\ell})
\eqd (x_{s_1+h}, x_{s_2+h}, \dots, x_{s_k+h}, y_{t_1+h}, y_{t_2+h}, \dots,
y_{t_\ell+h}), \\ \text{for all $k,\ell \geq 1$, all $s_1,\dots,s_k$ and
$t_1,\dots,t_\ell$, and all $h$}.
\end{multline*}
Here $\eqd$ means equality in distribution. In other words, any collection of
variates from the two sequences has the same joint distribution after we shift
the time indices forward or backwards in time. Meanwhile, we say that $x_t$,
$t = 1,2,3,\dots$ and $y_t$, $t = 1,2,3,\dots$ are *weakly jointly stationary*
or simply *jointly stationary* provided that each series is stationary, and:
$$
\gamma_{xy}(s,t) = \gamma_{xy}(s+h, t+h), \quad \text{for all $s,t,h$}.
$$
Here $\gamma_{xy}$ is the cross-covariance function between $x,y$. In other
words, the cross-covariance function must be invariant to shifts forward or
backwards in time, and is only a function of the lag $h = s-t$. For jointly
stationary series, we can hence abbreviate their cross-covariance function by
$\gamma_{xy}(h)$.

14. (2 pts)
Give an example of two time series that are weakly jointly stationary but not
strongly jointly stationary.

15. (3 pts)
If $x_t$, $t = 1,2,3,\dots$ and $y_t$, $t = 1,2,3,\dots$ form a *joint Gaussian
process*, which means that any collection $(x_{s_1}, x_{s_2}, \dots, x_{s_k},
y_{t_1}, y_{t_2}, \dots, y_{t_\ell})$ of variates along the series has a
multivariate Gaussian distribution, then prove that weak joint stationarity
implies strong joint stationarity.

16. (3 pts)
Write down explicit formulas that shows how to estimate the cross-covariance
and cross-correlation function of two finite time series $x_t$, $t = 1,\dots,n$
and $y_t$, $t = 1,\dots,n$, under the assumption of joint stationarity. Hint:
these should be entirely analogous to the *sample auto-covariance and sample
auto-correlation functions* that we covered in lecture.

17. (4 pts)
Following the code used in the lecture notes from week 2 ("Measures of
dependence and stationarity"), use the `ccf()` function to compute and plot
the sample cross-correlation function between Covid-19 cases and deaths,
separately, for each of Florida, Georgia, New York, Pennsylvania, and Texas.
(The lecture code does this for California.) Comment on what you find: do the
cross-correlation patterns look similar across different states?

    Also, follow the lecture code to plot the case and death signals together,
on the same plot, for each state (the lecture code provides a way to do this so
that they are scaled dynamically to attain the same min and max, and hence look
nice when plotted together). Comment on whether the estimated cross-correlation
patterns agree with what you see visually between the case and death signals.

---

[← Stationarity](04-stationarity.md) · [Up: contents](index.md)
