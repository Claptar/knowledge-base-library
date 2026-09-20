---
title: "73. Stationary MA and AR Processes"
course: "Berkeley Stat 153 Fall 2024"
chapter: 73
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 73. Stationary MA and AR Processes

## What this covers

This chapter introduces (weak) stationarity for a time series and works out the two basic
building blocks of linear time series models: the moving-average process $MA(q)$ and the
autoregressive process $AR(p)$. It answers, for each of them, when the model actually has a
stationary solution, and shows the algebraic device — the backshift operator — that makes the
general $AR(p)$ case tractable. It assumes familiarity with expectation, variance and covariance
of sums of independent random variables, and with i.i.d. Gaussian noise $\varepsilon_t$.

## Stationarity

A time series $y_t$ is (weakly, or covariance-) stationary if none of its first two moments
depend on where you look in time:

- $\mathbb{E}\,y_t$ does not change with $t$,
- $\operatorname{var}(y_t)$ does not change with $t$,
- $\operatorname{Cov}(y_t, y_{t+h})$ does not change with $t$, for each fixed lag $h$.

The third condition is the interesting one: it says the correlation between two observations can
depend on how far apart they are, but not on when they occurred. That function of $h$ alone,
$$\gamma(h) = \operatorname{Cov}(y_t, y_{t+h}),$$
is the **autocovariance function**, and $\rho(h) = \gamma(h)/\gamma(0)$ is the
**autocorrelation function (ACF)**.

## Moving-average processes

The simplest way to build a stationary series out of white noise
$\varepsilon_t \overset{\text{iid}}{\sim} N(0,\sigma^2)$ is to add up a fixed, finite window of
it. The order-1 case,
$$y_t = \mu + \varepsilon_t + \theta\varepsilon_{t-1} \qquad \text{for all } t,$$
is the $MA(1)$ model, with three parameters $\mu,\theta,\sigma$. The idea generalizes to a window
of length $q+1$:
$$y_t = \mu + \varepsilon_t + \theta_1\varepsilon_{t-1} + \theta_2\varepsilon_{t-2} + \cdots +
\theta_q \varepsilon_{t-q}, \qquad MA(q).$$

(The notes cite Slutzky's *"Summation of Random Causes"* at exactly this point, without further
discussion — see Sources.)

Because $y_t$ is a fixed linear combination of a fixed set of i.i.d. shocks, its moments never
depend on $t$: $MA(q)$ is automatically stationary. For $MA(1)$,
$$\mathbb{E}\,y_t = \mu, \qquad \operatorname{var}(y_t) = \sigma^2(1+\theta^2).$$
For the covariance, only the shocks the two observations have in common survive:
$$\operatorname{Cov}(y_t,y_{t+1}) = \operatorname{Cov}(\varepsilon_t + \theta\varepsilon_{t-1},\
\varepsilon_{t+1}+\theta\varepsilon_t) = \operatorname{Cov}(\varepsilon_t,\theta\varepsilon_t) =
\theta\sigma^2,$$
because $\varepsilon_{t-1}$ and $\varepsilon_{t+1}$ do not appear anywhere in the other bracket.
Two steps apart, nothing overlaps at all:
$$\operatorname{Cov}(y_t,y_{t+2}) = \operatorname{Cov}(\varepsilon_t+\theta\varepsilon_{t-1},\
\varepsilon_{t+2}+\theta\varepsilon_{t+1}) = 0,$$
and the same reasoning gives $\operatorname{Cov}(y_t,y_{t+h})=0$ for every $h\ge 2$. So
$$\gamma(h) = \begin{cases} \sigma^2(1+\theta^2) & h=0 \\ \theta\sigma^2 & |h|=1 \\ 0 &
|h|>1\end{cases}, \qquad \rho(h) = \begin{cases}1 & h=0\\ \dfrac{\theta}{1+\theta^2} & |h|=1\\ 0 &
|h|>1.\end{cases}$$

The same "shared shocks only" argument is what makes $MA(q)$ stationary with $\gamma(h)=0$ once
$|h|>q$: $y_t$ and $y_{t+h}$ are built from disjoint sets of $\varepsilon$'s as soon as the window
of length $q+1$ no longer overlaps between the two.

## Autoregressive processes: is $AR(1)$ stationary?

$MA(q)$ is stationary by construction. The autoregressive model is not obviously so, and working
out when it is turns out to be the main content of the lecture. Consider
$$y_t = \phi_0 + \phi_1 y_{t-1} + \varepsilon_t, \qquad \varepsilon_t \overset{\text{iid}}{\sim}
N(0,\sigma^2), \qquad AR(1),$$
started from a fixed observed value $y_1$. Substituting the recursion into itself,
$$y_2 = \phi_0 + \phi_1 y_1 + \varepsilon_2,$$
$$y_3 = \phi_0 + \phi_1 y_2 + \varepsilon_3 = \phi_0(1+\phi_1) + \phi_1^2 y_1 + \varepsilon_3 +
\phi_1\varepsilon_2,$$
and in general
$$y_t = \phi_0\left(1+\phi_1+\cdots+\phi_1^{t-2}\right) + \phi_1^{t-1}y_1 + \varepsilon_t +
\phi_1\varepsilon_{t-1} + \cdots + \phi_1^{t-2}\varepsilon_2.$$

Run from a fixed starting value, this process is *not* stationary as it stands: the coefficient
of $y_1$ and the number of noise terms both change with $t$, so for instance
$\operatorname{var}(y_2)\ne\operatorname{var}(y_3)$ in general. But if $|\phi_1|<1$, the term
$\phi_1^{t-1}y_1$ decays geometrically and the partial sum $1+\phi_1+\cdots+\phi_1^{t-2}$ tends to
the geometric series $1/(1-\phi_1)$: the memory of the fixed starting point washes out. For $t$
not too small,
$$y_t \approx \frac{\phi_0}{1-\phi_1} + \varepsilon_t + \phi_1\varepsilon_{t-1} +
\phi_1^2\varepsilon_{t-2} + \cdots = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty
\phi_1^j \varepsilon_{t-j}.$$

This limit is exactly stationary — it is what the recursion would settle into if it had been
running since the infinite past — and it is a moving average of infinite order: matching it
against the $MA(q)$ form with $\theta_j=\phi_1^j$ shows that an $AR(1)$ with $|\phi_1|<1$ *is* an
(infinite) moving average. This is the **causal stationary solution**: $y_t$ is written using
only present and past noise. Its moments follow the same "shared shocks" computation as for
$MA(q)$:
$$\mathbb{E}\,y_t = \frac{\phi_0}{1-\phi_1}, \qquad \operatorname{Cov}(y_t,y_{t+h}) =
\sigma^2\sum_{j=0}^\infty \phi_1^j\phi_1^{j+h} = \frac{\sigma^2\phi_1^{|h|}}{1-\phi_1^2}.$$

**$AR(1)$ has a causal stationary solution exactly when $|\phi_1|<1$.**

### What happens when $|\phi_1|>1$

The recursion can also be solved in the other time direction. Rearranging
$$y_t = \phi_0+\phi_1y_{t-1}+\varepsilon_t \quad\Longrightarrow\quad y_{t-1} =
-\frac{\phi_0}{\phi_1} + \frac{y_t}{\phi_1} - \frac{\varepsilon_t}{\phi_1}$$
expresses $y_{t-1}$ in terms of $y_t$ instead of the reverse — the same shape of recursion, but
with $1/\phi_1$ in place of $\phi_1$. If $|\phi_1|>1$ then $|1/\phi_1|<1$, so running *this*
recursion the same way as before (iterating in the backward time direction, letting the
influence of a fixed far-future value vanish) produces a stationary solution built from *future*
noise:
$$y_t = \frac{\phi_0}{1-\phi_1} - \frac{\varepsilon_{t+1}}{\phi_1} -
\frac{\varepsilon_{t+2}}{\phi_1^2} - \cdots.$$

So $AR(1)$ has a stationary solution whenever $\phi_1 \ne \pm 1$ — but only the $|\phi_1|<1$
solution is *causal*, i.e. expressible using the present and the past alone. That is why
"causal stationary $AR(1)$" is reserved for $|\phi_1|<1$: it is the version usable for
forecasting, since forecasting the future from the past requires the model not to secretly
depend on the future.

## The backshift operator

Writing out substitutions like the ones above becomes unwieldy for $AR(p)$ with $p>1$, so it
helps to have notation for "shift back in time." Define the **backshift operator** $B$ by
$$By_t = y_{t-1}, \qquad B^2y_t = B(By_t) = By_{t-1} = y_{t-2}, \qquad B^ky_t = y_{t-k},$$
with $B^0=I$ the identity, and negative powers shifting forward: $B^{-3}y_t=y_{t+3}$. It is
linear, so for instance $(B+2B^3)y_t = y_{t-1}+2y_{t-3}$.

The general $AR(p)$ model,
$$y_t = \phi_0+\phi_1y_{t-1}+\cdots+\phi_py_{t-p}+\varepsilon_t,$$
rearranges to
$$y_t - \phi_1By_t-\phi_2B^2y_t-\cdots-\phi_pB^py_t = \phi_0+\varepsilon_t \quad\Longrightarrow\quad
(I-\phi_1B-\cdots-\phi_pB^p)y_t=\phi_0+\varepsilon_t.$$
Writing $\phi(z) = 1-\phi_1z-\phi_2z^2-\cdots-\phi_pz^p$ for the **AR polynomial**, this reads
$$\phi(B)\,y_t = \phi_0+\varepsilon_t.$$

For $AR(1)$, $\phi(B)=I-\phi_1B$, and "dividing" through recovers the earlier computation purely
formally: since $\dfrac{1}{1-\phi_1z} = 1+\phi_1z+(\phi_1z)^2+\cdots$ as a power series,
$$y_t = \frac{1}{I-\phi_1B}(\phi_0+\varepsilon_t) = (I+\phi_1B+\phi_1^2B^2+\cdots)(\phi_0+
\varepsilon_t) = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty\phi_1^j\varepsilon_{t-j},$$
the same causal stationary solution as before, now obtained by inverting the operator $\phi(B)$
rather than substituting the recursion into itself.

## $AR(2)$, and the general condition for $AR(p)$

The same trick handles $AR(2)$:
$$y_t = \phi_0+\phi_1y_{t-1}+\phi_2y_{t-2}+\varepsilon_t, \qquad \phi(z)=1-\phi_1z-\phi_2z^2,
\qquad \phi(B)y_t=\phi_0+\varepsilon_t.$$
Factor the AR polynomial, $\phi(z) = (1-a_1z)(1-a_2z)$, where $1/a_1,1/a_2$ are its roots. Then
$$y_t = \frac{1}{(I-a_1B)(I-a_2B)}(\phi_0+\varepsilon_t) = (I+a_1B+a_1^2B^2+\cdots)
(I+a_2B+a_2^2B^2+\cdots)(\phi_0+\varepsilon_t),$$
each factor a geometric series exactly as in the $AR(1)$ case, provided each one converges.
Multiplying the two series out gives a general linear process
$$y_t = \mu+\sum_{j=0}^\infty\psi_j\varepsilon_{t-j}, \qquad \mu = \phi_0\sum_{j=0}^\infty\psi_j,
\qquad \psi_0=1,\ \ \psi_1=a_1+a_2,\ \ \psi_2 = a_1^2+a_1a_2+a_2^2,\ \dots$$
(each $\psi_j$ is the coefficient of $B^j$ in the product of the two geometric series). This is a
genuine stationary solution precisely when **both** geometric series converge, i.e. when $a_1$
and $a_2$ both have modulus strictly less than $1$.

The pattern is the general one. For $AR(p)$,
$$y_t = \phi_0+\phi_1y_{t-1}+\cdots+\phi_py_{t-p}+\varepsilon_t, \qquad \phi(z) =
1-\phi_1z-\cdots-\phi_pz^p,$$
factor $\phi(z)$ into its $p$ roots $1/a_1,\dots,1/a_p$ and invert $\phi(B)$ one factor at a time,
exactly as for $AR(2)$. **$AR(p)$ has a causal stationary solution iff $|a_j|<1$ for every $j$** —
equivalently, every root $1/a_j$ of the AR polynomial has modulus strictly greater than $1$.
Setting $p=1$ recovers the earlier condition: the $AR(1)$ polynomial $1-\phi_1z$ has its single
root at $1/\phi_1$, with $a_1=\phi_1$, so $|a_1|<1$ is exactly $|\phi_1|<1$.

## Sources

All material in this chapter comes from one set of handwritten lecture notes — no slide deck,
transcript, or exercise set was supplied for this lecture.

- Berkeley STAT 153 (Fall 2025), *Lecture Twenty*, handwritten notes:
  [`HandwrittenNotesLectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/HandwrittenNotesLectureTwenty153248Fall2025.pdf)
  (CC BY 4.0). The notes were reconstructed from a scanned PDF with no text layer by a model, and
  the conversion flags every equation as unverified.
  - `01-lecture-twenty.md` — stationarity, $MA(1)$ and $MA(q)$, their mean, variance and ACF.
  - `02-ar-models-stationarity.md` — $AR(1)$, the recursive substitution, the causal-stationary
    condition $|\phi_1|<1$, and the non-causal solution when $|\phi_1|>1$.
  - `03-for.md` ("$AR(p)$ for $p\ge1$") — the backshift operator, $AR(p)$ in operator form, the
    $AR(2)$ factorization, and the general causal-stationarity condition on the roots of the AR
    polynomial.
- The notes cite Slutzky's paper *"Summation of Random Causes"* immediately after introducing
  $MA(1)$, evidently as motivation for the moving-average model, but do not discuss its content
  further; it is not reconstructed here beyond the citation.

---

[← 72. Ridge Regression as Bayesian Inference](72-ridge-regression-as-bayesian-inference.md) · [Contents](index.md) · [75. $MA(q)$ models →](75-ma-q-models.md)
