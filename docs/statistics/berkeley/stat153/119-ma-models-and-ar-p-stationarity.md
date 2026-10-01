---
title: "119. MA Models and AR(p) Stationarity"
course: "Berkeley Stat 153"
chapter: 119
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 119. MA Models and AR(p) Stationarity

## What this covers

This chapter answers two questions from the same lecture: what a Moving Average model is and why
every $\text{MA}(q)$ model is automatically stationary, and how to turn the *implicit* AR(1) /
AR($p$) difference equation into an explicit, causal, stationary formula for $y_t$ — first by
direct recursive substitution, then by the much faster backshift-operator trick that is the only
method that scales to AR($p$). It assumes the reader already has the definitions of a stationary
process, the autocovariance function (ACVF) and autocorrelation function (ACF), and has met the
AR(1) model as an implicit difference equation fit in practice with `AutoReg`.

## Recap: stationarity, ACVF and ACF

A time series $\{y_t\}$ is **stationary** if none of the following depend on $t$: the mean
$\mathbb{E}y_t$, the variance $\text{var}(y_t)$, and the covariance $\text{cov}(y_t, y_{t+h})$ for
each fixed $h$. For a stationary series the **autocovariance function** (ACVF) is
$$\gamma(h) := \text{cov}(y_t, y_{t+h}),$$
which by stationarity satisfies $\gamma(-h) = \gamma(h)$, and $\gamma(0)$ is just
$\text{var}(y_t)$. The **autocorrelation function** (ACF) is the normalized version
$$\rho(h) = \frac{\gamma(h)}{\gamma(0)}.$$

## Moving Average models

An important class of stationary models is the **Moving Average** models. For an integer
$q \ge 1$, the $\text{MA}(q)$ model is
$$y_t = \mu + \epsilon_t + \theta_1\epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \cdots + \theta_q \epsilon_{t-q}, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2),$$
with $q+2$ unknown parameters $\mu, \theta_1, \dots, \theta_q, \sigma$ estimated from the data.

Slutzky, who introduced the model in "The Summation of Random Causes as the Source of Cyclic
Processes" (*Econometrica*, 1937), described it exactly this way: the $\epsilon_t$ are independent
random "causes," and the observation $y_t$ at time $t$ is a *consequence* that pools together the
causes at times $t, t-1,\dots,t-q$, weighted by $\theta_1,\dots,\theta_q$. Because $y_t$ and
$y_{t+1}$ share some of the same underlying causes whenever $q\ge 1$, successive observations end
up correlated — that sharing is the entire mechanism behind an MA model's autocorrelation.

### Why MA(1) is stationary

Take $q=1$: $y_t = \mu + \epsilon_t + \theta_1\epsilon_{t-1}$. Every $\text{MA}(q)$ model is
stationary; here is the argument for $\text{MA}(1)$ (the general $q$ case is the same argument
with more terms, and is left as an exercise in the lecture). The mean is $\mathbb{E}y_t = \mu$,
constant in $t$. The variance is
$$\text{var}(y_t) = \text{var}(\epsilon_t + \theta_1\epsilon_{t-1}) = \sigma^2 + \theta_1^2\sigma^2,$$
also constant. For the covariance, $y_t$ and $y_{t+1}$ share the term $\epsilon_t$:
$$\text{cov}(y_t, y_{t+1}) = \text{cov}(\epsilon_t + \theta_1\epsilon_{t-1},\ \epsilon_{t+1} + \theta_1\epsilon_t) = \text{cov}(\epsilon_t, \theta_1\epsilon_t) = \theta_1\sigma^2,$$
using independence of the $\epsilon_t$'s to kill every other cross term. But $y_t$ and $y_{t+2}$
share **no** $\epsilon$'s at all:
$$\text{cov}(y_t, y_{t+2}) = \text{cov}(\epsilon_t + \theta_1\epsilon_{t-1},\ \epsilon_{t+2} + \theta_1\epsilon_{t+1}) = 0,$$
and the same argument gives $\text{cov}(y_t, y_{t+h}) = 0$ for every $h \ge 2$. None of these
depend on $t$, so $\text{MA}(1)$ is stationary, with
$$\gamma(h) = \begin{cases} \sigma^2(1+\theta_1^2) & h = 0 \\ \sigma^2\theta_1 & |h|=1 \\ 0 & |h| > 1\end{cases}
\qquad
\rho(h) = \begin{cases} 1 & h=0 \\ \dfrac{\theta_1}{1+\theta_1^2} & h = 1 \\ 0 & h > 1.\end{cases}$$

The pattern to notice: an $\text{MA}(q)$ model's autocorrelation cuts off exactly at lag $q$,
because that is exactly the largest lag at which $y_t$ and $y_{t+h}$ can still share an
$\epsilon$.

## Making AR(1) explicit: recursive substitution

Contrast this with the $\text{AR}(1)$ model, $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$. This is
an **implicit** equation — $y$ appears on both sides — so before a mean, variance or covariance
can even be computed, an explicit formula for $y_t$ in terms of the $\epsilon$'s alone is needed.

One way to get it is to substitute the same equation for $y_{t-1}$, then for $y_{t-2}$, and so on:
$$y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t = \phi_0(1+\phi_1) + \phi_1^2 y_{t-2} + \epsilon_t + \phi_1\epsilon_{t-1} = \cdots$$
After $M+1$ substitutions,
$$y_t = \phi_0\sum_{j=0}^M \phi_1^j + \phi_1^{M+1}y_{t-M-1} + \sum_{j=0}^M \phi_1^j \epsilon_{t-j},$$
an identity true for every $M \ge 0$ and every $\phi_0,\phi_1$ — but the right side still contains
a $y$-value.

**If $|\phi_1| < 1$**, then $\phi_1^{M+1} \to 0$, the geometric sum $\sum_{j=0}^M \phi_1^j \to
1/(1-\phi_1)$, and the partial sum of $\epsilon$'s converges (because $|\phi_1|^j$ decays).
Letting $M\to\infty$ removes the $y_{t-M-1}$ term entirely, leaving a formula with no $y$ on the
right:
$$y_t = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}.$$
This is well defined exactly when $|\phi_1|<1$, and one can check it satisfies the original AR(1)
equation. It is stationary (recall from the previous lecture: $\mathbb{E}y_t = \phi_0/(1-\phi_1)$
and $\text{cov}(y_t,y_{t+h}) = \sigma^2\phi_1^{|h|}/(1-\phi_1^2)$), and it expresses $y_t$ purely
in terms of present and past noise $\epsilon_t,\epsilon_{t-1},\dots$ — this is what **causal**
means. One consequence: $\epsilon_t$ is independent of every past $y$-value
$y_{t-1},y_{t-2},\dots$, because those depend only on $\epsilon_{t-1},\epsilon_{t-2},\dots$.

**If $|\phi_1| > 1$**, the substitution above never converges going into the past, but running the
recursion the *other* way — solving for $y_t$ in terms of $y_{t+1}$ and recursing into the
*future* — does converge, because now it is $1/\phi_1$ that is small:
$$y_t = -\frac{\phi_0}{\phi_1} + \frac{1}{\phi_1}y_{t+1} - \frac{\epsilon_{t+1}}{\phi_1}
\ \Longrightarrow\
y_t = \frac{\phi_0}{1-\phi_1} - \sum_{j=1}^\infty \frac{\epsilon_{t+j}}{\phi_1^j}$$
after the same kind of repeated substitution and limit. This is also a genuine stationary solution
of the AR(1) equation, but it is **non-causal**: $y_t$ depends on *future* noise
$\epsilon_{t+1},\epsilon_{t+2},\dots$, and $\epsilon_t$ is *not* independent of the past $y$'s.

**If $|\phi_1| = 1$**, neither recursion converges in either direction, and there is in fact no
stationary solution to the AR(1) equation at all.

So for AR(1): a causal stationary solution exists precisely when $|\phi_1| < 1$; a stationary
solution of any kind (necessarily non-causal) exists only when $|\phi_1| > 1$; and at
$|\phi_1| = 1$ there is none.

## What this means for fitting: `AutoReg` and three cases

In practice, AR(1) is fit with the `AutoReg` function from `statsmodels`, which maximizes the
conditional likelihood
$$\prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(y_t-\phi_0-\phi_1y_{t-1})^2}{2\sigma^2}\right),$$
i.e. it fixes $y_1$ at its observed value and assumes each $\epsilon_t$ is independent of the past
$y_{t-1},\dots,y_1$. This is a different model from the causal stationary AR(1) solution derived
above, whose likelihood carries an extra factor for $y_1$:
$$\frac{\sqrt{1-\phi_1^2}}{\sqrt{2\pi}\sigma}\exp\left(-\frac{1-\phi_1^2}{2\sigma^2}\left(y_1-\frac{\phi_0}{1-\phi_1}\right)^2\right)\times\prod_{t=2}^n \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(y_t-\phi_0-\phi_1y_{t-1})^2}{2\sigma^2}\right).$$
Depending on the fitted $\hat\phi_1$, three things can happen.

**Case 1: $|\hat\phi_1| > 1$.** Common when fitting AR(1) directly to raw economic data (GDP,
GNP). The fitted conditional model is very different from the true non-causal stationary AR(1)
solution (recall that in the non-causal solution $\epsilon_t$ becomes dependent on the past
$y$'s — a poor match for what `AutoReg` assumes). The fitted model is far from stationary, and
forecasts explode as the horizon grows.

**Case 2: $|\hat\phi_1| < 1$.** Also common, often after preprocessing economic data (logging,
then differencing once or twice). The fitted conditional model is technically still
non-stationary and distinct from the causal stationary model, but the discrepancy is minimal and
the two behave alike, for three reasons: (a) the true likelihood differs from the fitted one only
by the extra factor involving $y_1$, which barely matters once $n$ is large; (b) recursing the
fitted equation from $t$ back to $2$ leaves a term $\phi_1^{t-1}y_1$ that decays rapidly since
$|\phi_1|<1$, so for $t$ not too small the two representations nearly coincide; (c) forecasts from
both models are computed identically, since both rely only on the independence of $\epsilon_t$
from the past $y$'s. So when $|\hat\phi_1|<1$, it is standard practice to treat the `AutoReg` fit
as if it were the causal stationary AR(1) model.

**Case 3: $|\hat\phi_1| = 1$.** Both $\hat\phi_1=1$ and $\hat\phi_1=-1$ are non-stationary
boundary cases. $\hat\phi_1=-1$ almost never arises (it would need data oscillating wildly from
one point to the next). $\hat\phi_1=1$ (a "unit root") is common; it rewrites the equation as
$y_t - y_{t-1} = \phi_0+\epsilon_t$, which suggests fitting models to the *differenced* series
$y_t-y_{t-1}$ instead. `AutoReg` rarely returns exactly $\hat\phi_1=1$ but can get close to it;
predictions under $\hat\phi_1=1$ grow linearly, which suits many trending datasets reasonably
well.

Restricting to causal models, then, stationarity corresponds exactly to $|\phi_1|<1$ — the
mathematically valid stationary solution at $|\phi_1|>1$ is non-causal and does not match what
`AutoReg` fits.

## Backshift notation

Let $B$ be the **backshift operator**: $By_t = y_{t-1}$, $B^2y_t = y_{t-2}$, and so on (likewise
for $\epsilon_t$). Let $I$ be the identity, $Iy_t = y_t$. Polynomials in $B$ act termwise, e.g.
$$(I + B + 3B^2)y_t = y_t + y_{t-1} + 3y_{t-2}.$$
More generally $f(B)$ makes sense for any polynomial $f(z)$, and the notation even extends to
negative powers, which shift **forward**: $B^{-1}y_t = y_{t+1}$, and
$(B^3+9B^{-2})y_t = y_{t-3}+9y_{t+2}$.

In this notation, the $\text{AR}(p)$ equation $y_t=\phi_0+\phi_1y_{t-1}+\cdots+\phi_py_{t-p}+\epsilon_t$
becomes
$$\phi(B)y_t = \phi_0+\epsilon_t, \qquad \phi(z) := 1-\phi_1z-\phi_2z^2-\cdots-\phi_pz^p,$$
the **AR polynomial**. Likewise the $\text{MA}(q)$ equation becomes simply
$$y_t = \theta(B)\epsilon_t, \qquad \theta(z) := 1+\theta_1z+\cdots+\theta_qz^q.$$

## Rederiving the causal AR(1) formula by backshift calculus

The recursive-substitution argument above is hard to redo for $p\ge 2$. Backshift notation gives a
shortcut that generalizes immediately. Write the AR(1) equation as $\phi(B)y_t=\phi_0+\epsilon_t$
with $\phi(z)=1-\phi_1z$, and *formally* divide:
$$y_t = \frac{1}{\phi(B)}(\phi_0+\epsilon_t).$$
Since $\dfrac{1}{1-\phi_1z} = 1+\phi_1z+\phi_1^2z^2+\cdots$ as a power series, substitute $B$ for
$z$:
$$y_t = (I+\phi_1B+\phi_1^2B^2+\cdots)(\phi_0+\epsilon_t) = (1+\phi_1+\phi_1^2+\cdots)\phi_0 + \sum_{j=0}^\infty\phi_1^j\epsilon_{t-j} = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty \phi_1^j\epsilon_{t-j},$$
recovering exactly the causal formula from before — this time in three lines rather than an
explicit induction. This trick, sometimes called **backshift calculus**, is what makes
$\text{AR}(p)$ tractable.

## AR(p): factoring the AR polynomial

For $\text{AR}(p)$, $\phi(B)y_t=\phi_0+\epsilon_t$ with AR polynomial
$\phi(z)=1-\phi_1z-\cdots-\phi_pz^p$. Formally solving for $y_t$ needs $1/\phi(B)$, and the way to
make sense of the reciprocal of a degree-$p$ polynomial is to **factor it into linear pieces**
first:
$$\phi(z) = (1-a_1z)\cdots(1-a_pz),$$
so that $a_1,\dots,a_p$ are the reciprocals of the roots of $\phi$ (the roots themselves are
$1/a_1,\dots,1/a_p$; some $a_i$ can be complex even though $\phi$'s coefficients are real). Then
$$y_t = \prod_{k=1}^p \frac{1}{1-a_kB}(\phi_0+\epsilon_t) = \prod_{k=1}^p\left(\sum_{j=0}^\infty a_k^jB^j\right)(\phi_0+\epsilon_t),$$
applying the same geometric-series trick to each factor. Multiplying out the product and
collecting terms gives a $p$-fold sum over $j_1,\dots,j_p$, and for these sums to converge at all
every $|a_i|<1$ is needed. Equivalently — since $a_i = 1/(\text{root}_i)$ — **every root of the AR
polynomial $\phi(z)$ must have modulus strictly greater than 1.** When that holds, collecting all
terms with $j_1+\cdots+j_p=j$ gives a representation
$$y_t = \mu + \sum_{j=0}^\infty \psi_j\epsilon_{t-j}$$
for some constants $\mu,\psi_1,\psi_2,\dots$: causal (only present/past $\epsilon$'s appear) and
stationary.

This can be made rigorous:

1. If every root of $\phi(z)$ has modulus $>1$, there is a **unique** causal stationary process
   satisfying the AR($p$) equation, of the form above.
2. If even one root has modulus $\le 1$, **no** causal stationary solution exists.
3. `AutoReg` actually fits the conditional model that fixes $y_1,\dots,y_p$ at their observed
   values and treats $\epsilon_t$ as independent of the past for $t>p$; when condition 1 holds,
   this behaves like the true causal stationary model, for the same reasons it did at $p=1$. The
   `AutoReg` output reports the moduli of the roots of the fitted AR polynomial, which is exactly
   how condition 1 is checked in practice.

## Choosing the order $p$: the sample PACF

Fitting an AR($p$) model requires first choosing $p$. The standard tool is the **sample partial
autocorrelation function** (sample PACF): for each lag $h\ge 1$,
$$\text{sample PACF}(h) := \hat\phi_h,\quad\text{the estimated coefficient on }y_{t-h}\text{ when AR}(h)\text{ is fit to the data.}$$
The rule of thumb: use the smallest $p$ for which $\text{sample PACF}(h)$ is negligible for every
$h>p$. This matches the heuristic used in Lab 9 for choosing $p$ by checking whether the
confidence interval for $\hat\phi_p$ from an AR($p$) fit contains zero — checking that is exactly
checking whether the sample PACF at lag $p$ is small. It can happen that $\text{sample PACF}(h)$ is
negligible for $h=1,\dots,11$ but not at $h=12$, in which case the right model is $\text{AR}(12)$,
not a smaller order.

Why the quantity $\hat\phi_h$ obtained this way deserves the name "partial autocorrelation" is
left for the next lecture.

## Sources

Lecture notes reconstructed from *Lecture Twenty*, STAT 153, UC Berkeley, Fall 2025 (Aditya
Guntuboyina, 6 November 2025), source PDF `LectureTwenty153248Fall2025.pdf`
(`berkeley-stat153/fall-2025`, CC BY 4.0). No separate slide deck or transcript was supplied for
this lecture — only these reconstructed notes, produced by a model reading a PDF with no text
layer; per the notes' own caveat, every displayed equation is unverified against the original and
should be checked there if precision matters.

- MA($q$) definition, Slutzky's motivation, and the MA(1) stationarity proof:
  `01-1-moving-average-ma-models.md`.
- Explicit solution of AR(1) by recursive substitution, the causal/non-causal split at
  $|\phi_1|=1$, and the `AutoReg`-fitting discussion (three cases):
  `02-2-stationarity-of-ar-1.md`.
- Backshift operator and polynomial notation for AR($p$)/MA($q$): `03-3-backshift-notation.md`.
- Backshift-calculus rederivation of the causal AR(1) formula:
  `04-4-causal-stationary-ar-1-formula-using-backshift.md`.
- AR($p$) polynomial factorization, the roots-modulus condition, and the three rigorous facts:
  `05-5-ar-p-for.md`.
- Sample PACF and order selection: `06-6-determination-of-the-order-of-ar.md`.

Referred to but not contained in these notes, and not otherwise supplied: the previous lecture's
derivation of the AR(1) mean/covariance formula (cited here as "recall from the previous
lecture"), the Lab 9 heuristic for order selection, and the explanation — promised for the next
lecture — of why $\hat\phi_h$ is called a *partial* autocorrelation.

---

[← 118. Bayesian View of Ridge Regression](118-bayesian-view-of-ridge-regression.md) · [Contents](index.md) · [120. Nonlinear Autoregression →](120-nonlinear-autoregression.md)
