---
title: "80. Correlation, Random Walks, and Stationarity"
course: "Berkeley Stat 153"
chapter: 80
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 80. Correlation, Random Walks, and Stationarity

## What this covers

This chapter works through Homework 1 of Stat 153 (time series), which is built to sharpen four
ideas from the first two weeks of lecture rather than to introduce new ones: the gap between zero
correlation and independence, the random walk with drift as the course's first example of a
non-stationary process, the definitions of stationarity together with the auto-covariance and
auto-correlation functions, and how those definitions extend from one time series to a pair of
them. It assumes you already have the lecture's definitions of (weak and strict) stationarity, the
random walk model, and the sample auto-covariance/auto-correlation functions — those are *used*
here, not re-derived, and the exercises below are the course's own homework problems, not solved.

## Correlation versus independence

Independence of two random variables always forces zero covariance, but the converse is false in
general — a pair can be completely uncorrelated while still being strongly dependent. Exercises 1
and 3 ask you to build such counterexamples yourself, in two different settings.

There is one setting where the converse *does* hold: if $(X,Y)$ is **jointly** (multivariate)
Gaussian, then $\mathrm{Cov}(X,Y) = 0$ forces independence. Exercise 2 asks you to prove this.

Exercise 3 is the trap to notice: it asks for $X,Y$ that are each *marginally* Gaussian — $X$ is
Gaussian and $Y$ is Gaussian — and uncorrelated, but not independent. This looks like it should
contradict Exercise 2, unless you notice the difference between "$X$ is Gaussian and $Y$ is
Gaussian" and "$(X,Y)$ is jointly Gaussian": the pair need not be jointly Gaussian even when each
coordinate is, and the hint attached to the problem says exactly this.

## The random walk with drift

The random walk with drift is
$$
x_t = \delta + x_{t-1} + w_t, \qquad t = 1,2,3,\dots,
$$
with $w_t \sim N(0,\sigma^2)$ drawn independently across $t$. Lecture already established that this
process is not stationary — both its mean and its variance grow with $t$. The homework asks you to
make that precise in a different way: to work out how the *correlation* $\rho(t-1,t)$ between two
consecutive observations changes with $t$ (Exercise 4), and to say what that correlation converges
to as $t \to \infty$ and what that limit means about the process.

The remaining exercises build a hypothesis test out of this model. Because differencing the random
walk once, $w_t = x_t - x_{t-1}$, gives i.i.d.\ Gaussian increments with mean $\delta$, testing
$H_0: \delta = 0$ reduces to a standard one-sample test for whether the mean of a Gaussian population
is zero when the variance is unknown, applied to the increments rather than to $x_t$ itself
(Exercise 5). Exercises 6 and 7 ask you to check this by simulation: first a single random walk
with and without drift, then fifty repetitions used to trace out how the mean and standard
deviation of $x_t$ evolve across time.

## Stationarity and the auto-covariance function

Two products of Gaussian noise are used to probe the stationarity definitions directly:
$$
x_t = w_t w_{t-1},
$$
first with $w_t \sim N(0,\sigma^2)$ i.i.d.\ (Exercise 8), then with $w_t \sim N(\mu,\sigma^2)$
i.i.d.\ for $\mu \neq 0$ (Exercise 9). In each case the exercise asks for the mean, variance,
auto-covariance and auto-correlation functions of $x_t$, and then for a verdict on whether the
process is stationary — the point being that the two cases (zero-mean versus nonzero-mean noise)
do not behave the same way. Exercise 10 asks you to check the population calculations from 8 and 9
against simulation: sample mean, sample variance, and the sample auto-correlation function from
`acf()`, on a simulated series of length 200 for each case.

Exercise 11 asks for an example of a process that is weakly stationary — constant mean, and
auto-covariance depending only on lag — without being strongly (strictly) stationary, i.e. without
the full joint distribution of the series being shift-invariant.

The two bonus exercises turn to a structural property of the auto-covariance function. A function
$\kappa$ is **positive semidefinite (PSD)** if
$$
\sum_{i,j=1}^n a_i a_j\, \kappa(t_i - t_j) \geq 0, \qquad \text{for all } n \geq 1,\ \text{all }
a_1,\dots,a_n,\ \text{and all } t_1,\dots,t_n.
$$
Exercise 12 asks you to show that the auto-covariance function $\gamma_x(h)$ of any stationary
process is PSD, and Exercise 13 to show the same for the sample auto-covariance function
$\hat\gamma_x$ defined in lecture.

## Joint stationarity

The homework extends stationarity from one series to a pair, $x_t$ and $y_t$, $t = 1,2,3,\dots$,
by the same shift-invariance idea used for a single series. The two series are **strongly jointly
stationary** if every finite joint collection drawn from both series has a distribution unaffected
by shifting all the time indices by the same amount $h$:
$$
(x_{s_1}, \dots, x_{s_k}, y_{t_1}, \dots, y_{t_\ell}) \overset{d}{=}
(x_{s_1+h}, \dots, x_{s_k+h}, y_{t_1+h}, \dots, y_{t_\ell+h}),
$$
for all $k,\ell \geq 1$, all indices $s_1,\dots,s_k,\,t_1,\dots,t_\ell$, and all $h$.

They are **weakly jointly stationary** (or just *jointly stationary*) if each series is itself
stationary and the cross-covariance function is shift-invariant:
$$
\gamma_{xy}(s,t) = \gamma_{xy}(s+h,t+h), \qquad \text{for all } s,t,h,
$$
so that $\gamma_{xy}$ depends on $s,t$ only through the lag $h = s-t$, and can be written
$\gamma_{xy}(h)$.

Exercise 14 asks for a pair that is weakly but not strongly jointly stationary — the two-series
analogue of Exercise 11. Exercise 15 asks you to prove that if $x_t$ and $y_t$ form a **joint
Gaussian process** (every finite collection drawn from the two series is jointly Gaussian), then
weak joint stationarity upgrades to strong joint stationarity — the two-series analogue of how
Gaussianity controlled the correlation/independence question in Exercise 2. Exercise 16 asks you to
write down the sample cross-covariance and sample cross-correlation functions for two finite series
under joint stationarity, built the same way as the sample auto-covariance and auto-correlation
functions from lecture. Exercise 17 puts this to work on data: computing and plotting the sample
cross-correlation function (`ccf()`) between COVID-19 case and death counts, state by state, and
comparing the cross-correlation pattern against what the case and death curves look like plotted
together.

## Exercises

**Correlation and independence**

1. (3 pts) Give an example of two random variables that are uncorrelated but not independent.
   Prove both that they are uncorrelated and that they are not independent (for the latter, any
   property equivalent to independence may be used).
2. (2 pts) If $(X,Y)$ has a multivariate Gaussian distribution and $\mathrm{Cov}(X,Y) = 0$, show
   that $X$ and $Y$ are independent.
3. (3 pts) Give an example of two random variables $X,Y$ that are each marginally Gaussian and
   uncorrelated, but not independent. (Hint: $(X,Y)$ cannot be jointly Gaussian in such an example.)

**Random walks**

4. (2 pts) Let $x_t = \delta + x_{t-1} + w_t$, $t=1,2,3,\dots$, with $w_t \sim N(0,\sigma^2)$
   independent across $t$. Prove that $\rho(t-1,t) = \sqrt{\dfrac{t-1}{t}}$. What does this
   approach as $t \to \infty$, and how should that limit be interpreted?
5. (3 pts) Suppose $\delta$ and $\sigma^2$ in the model of Exercise 4 are both unknown. Devise a
   test statistic for $H_0: \delta = 0$, based on a standard test (from a previous course) for
   whether the mean of a Gaussian population is zero when the variance is unknown, given
   i.i.d.\ samples from that Gaussian. State the null distribution of your test statistic and how
   you would compute it in R (a base-R function name suffices).
6. (2 pts) Simulate a random walk of length 200 without drift ($\delta = 0$) and compute the test
   statistic from Exercise 5. Repeat with a large nonzero $\delta$ and report both values.
7. (4 pts) Simulate 50 random walks of length 200 each, with nonzero drift, and plot them together
   using transparent colouring, following the week 2 lecture code ("Measures of dependence and
   stationarity"). Compute and plot the sample mean $\hat\mu_t$ at each time $t$ across the 50
   repetitions as a dark line, and the sample standard deviation $\hat\sigma_t$ at each $t$, shown
   as dark dotted lines at $\hat\mu_t \pm \hat\sigma_t$. Describe what the plot shows.

**Stationarity**

8. (3 pts) For $x_t = w_t w_{t-1}$ with $w_t \sim N(0,\sigma^2)$ independent across $t$, compute
   the mean, variance, auto-covariance, and auto-correlation functions of $x_t$. Is $x_t$
   stationary?
9. (3 pts) Repeat Exercise 8 with $w_t \sim N(\mu,\sigma^2)$ independent across $t$, for
   $\mu \neq 0$. Is $x_t$ stationary?
10. (3 pts) Simulate the processes of Exercise 8 (with $\mu=0$) and Exercise 9 (with $\mu \neq 0$)
    as two series of length 200 and plot them. Compute the sample mean and sample variance of each
    (over all time) and compare with the population values from Exercises 8 and 9. Compute and plot
    the sample auto-correlation function with `acf()` and compare with the population
    auto-correlation function.
11. (2 pts) Give an example of a weakly stationary process that is not strongly stationary.
12. (Bonus) A function $\kappa$ is positive semidefinite (PSD) if
    $\sum_{i,j=1}^n a_i a_j \kappa(t_i-t_j) \geq 0$ for all $n \geq 1$, all $a_1,\dots,a_n$, and all
    $t_1,\dots,t_n$. Prove that if $x_t$ is stationary with auto-covariance function $\gamma_x(h)$,
    then $\gamma_x$ is PSD. State clearly any probability or linear-algebra facts you use.
13. (Bonus) Prove that the sample auto-covariance function $\hat\gamma_x$ defined in lecture is
    also PSD.

**Joint stationarity**

14. (2 pts) Give an example of two time series that are weakly jointly stationary but not strongly
    jointly stationary.
15. (3 pts) If $x_t$ and $y_t$ form a joint Gaussian process — every finite collection
    $(x_{s_1},\dots,x_{s_k},y_{t_1},\dots,y_{t_\ell})$ is multivariate Gaussian — prove that weak
    joint stationarity implies strong joint stationarity.
16. (3 pts) Write down explicit formulas for estimating the cross-covariance and cross-correlation
    functions of two finite time series $x_t, y_t$, $t=1,\dots,n$, under joint stationarity,
    analogous to the sample auto-covariance and sample auto-correlation functions from lecture.
17. (4 pts) Following the week 2 lecture code ("Measures of dependence and stationarity"), use
    `ccf()` to compute and plot the sample cross-correlation function between COVID-19 cases and
    deaths, separately, for Florida, Georgia, New York, Pennsylvania, and Texas. (The lecture code
    does this for California.) Comment on whether the cross-correlation pattern is similar across
    states. Also plot the case and death signals together for each state, dynamically rescaled to
    share the same min and max as in the lecture code, and comment on whether the visual pattern
    agrees with the estimated cross-correlation.

## Sources

- All exposition and exercises are from Berkeley Stat 153, Fall 2024, Homework 1
  (`homeworks/homework1/homework1.Rmd`, CC BY 4.0), as converted to markdown:
  [Introduction](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd)
  (Exercises 1–3), [Random walks](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd)
  (Exercises 4–7), [Stationarity](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd)
  (Exercises 8–13), and [Joint stationarity](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework1/homework1.Rmd)
  (Exercises 14–17, including the strong/weak joint stationarity definitions reproduced above,
  which appear verbatim in that file).
- No slides or lecture transcript were supplied for this chapter. The homework repeatedly points to
  material it does not itself contain: the lecture's definitions of stationarity and the random walk
  model (used but not restated in Exercise 4), the sample auto-covariance/auto-correlation functions
  "defined in lecture" (Exercises 12, 13, 16), and the "week 2 lecture notes" titled *Measures of
  dependence and stationarity*, whose R code for plotting simulated random walks (Exercise 7) and for
  computing `ccf()` on COVID-19 case/death data (Exercise 17) was not provided as input to this
  chapter.

---

[← 79. Homework Assignments Index](79-homework-assignments-index.md) · [Contents](index.md) · [81. Regression: Estimation and Evaluation →](81-regression-estimation-and-evaluation.md)
