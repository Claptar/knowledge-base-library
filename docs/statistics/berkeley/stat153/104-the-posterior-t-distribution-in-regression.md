---
title: "104. The Posterior t-Distribution in Regression"
course: "Berkeley Stat 153 Fall 2024"
chapter: 104
source: "https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 153 Fall 2024](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFive153248Fall2025.ipynb), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 104. The Posterior t-Distribution in Regression

## What this covers

In Bayesian multiple linear regression with a flat prior, what is the exact posterior distribution
of the coefficients $\beta_0,\dots,\beta_m$, and why does it turn out to be a multivariate
$t$-distribution rather than a normal one? This chapter derives that result from scratch, works out
the properties of the multivariate $t$-density it produces, and uses it to build credible intervals
for individual coefficients. It then turns to the natural next question — models where a parameter
enters nonlinearly — and works two examples of the same idea: a change-of-slope ("broken-stick")
regression and a sinusoidal model with unknown frequency. It assumes the ordinary least-squares
matrix formulation ($X$, $y$, $\hat\beta = (X^TX)^{-1}X^Ty$) and the flat-prior Bayesian setup for
linear regression from the preceding lecture.

## Setting up the Bayesian model

In multiple linear regression there is one response $y$ and $m$ covariates $x_1,\dots,x_m$, observed
on $n$ subjects: $(y_i, x_{i1},\dots,x_{im})$ for $i=1,\dots,n$. The model is

$$
y_i = \beta_0 + \beta_1 x_{i1} + \dots + \beta_m x_{im} + \epsilon_i, \qquad \epsilon_i \stackrel{\text{i.i.d}}{\sim} N(0,\sigma^2).
$$

For a Bayesian treatment we put a flat (improper) prior on the coefficients and on $\log\sigma$:

$$
\beta_0,\dots,\beta_m,\log\sigma \stackrel{\text{i.i.d}}{\sim} \text{unif}(-C,C)
$$

for a very large $C$. Combining this with the normal likelihood gives the joint posterior density

$$
f_{\beta,\sigma\mid\text{data}}(\beta,\sigma) \propto \sigma^{-n-1}\exp\left(-\frac{S(\beta)}{2\sigma^2}\right) I\{-C<\beta_0,\dots,\beta_m,\log\sigma<C\},
$$

where $S(\beta) := \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_{i1} - \dots - \beta_m x_{im})^2$ is the sum
of squares. (The extra $\sigma^{-1}$ beyond the usual $\sigma^{-n}$ from the likelihood comes from the
flat prior being on $\log\sigma$ rather than $\sigma$.)

## Marginalizing out $\sigma$

The posterior over the coefficients alone is obtained by integrating out $\sigma$:

$$
f_{\beta\mid\text{data}}(\beta) \propto I\{-C<\beta_j<C\}\int_{e^{-C}}^{e^{C}} \sigma^{-n-1}\exp\left(-\frac{S(\beta)}{2\sigma^2}\right)d\sigma
\;\approx\; \int_0^\infty \sigma^{-n-1}\exp\left(-\frac{S(\beta)}{2\sigma^2}\right)d\sigma,
$$

dropping the indicator as $C\to\infty$ (as in the linear-regression posterior derived earlier in the
course, the bound $C$ has essentially no effect). Substituting $\sigma = s\sqrt{S(\beta)}$ turns the
integral into

$$
\int_0^\infty \sigma^{-n-1}\exp\left(-\frac{S(\beta)}{2\sigma^2}\right)d\sigma
= \left(\frac{1}{S(\beta)}\right)^{n/2}\int_0^\infty s^{-n-1}\exp\left(-\frac{1}{2s^2}\right)ds,
$$

and the remaining integral over $s$ is a constant that does not depend on $\beta$. Hence

$$
f_{\beta\mid\text{data}}(\beta) \;\propto\; \left(\frac{1}{S(\beta)}\right)^{n/2} \;\propto\; \left(\frac{S(\hat\beta)}{S(\beta)}\right)^{n/2}, \tag{$*$}
$$

where $\hat\beta$ is the least-squares estimator (multiplying by the constant $S(\hat\beta)^{n/2}$
does not change the proportionality). It turns out that $(*)$ is exactly a multivariate $t$-density.
The rest of this chapter explains why, and what that buys us.

## Two facts about the sum of squares

Write the model in matrix form, $y = X\beta+\epsilon$, with

$$
y=\begin{pmatrix}y_1\\ \vdots\\ y_n\end{pmatrix},\quad
X=\begin{pmatrix}1&x_{11}&\dots&x_{1m}\\ \vdots& & &\vdots\\ 1&x_{n1}&\dots&x_{nm}\end{pmatrix},\quad
\beta=\begin{pmatrix}\beta_0\\ \vdots\\ \beta_m\end{pmatrix},
$$

so that $S(\beta) = \|y-X\beta\|^2$. Two facts about $S$ do all the work below.

**Fact 1 (normal equations).** The least-squares estimator is $\hat\beta = (X^TX)^{-1}X^Ty$. To see
this, expand $S(\beta) = y^Ty - \beta^TX^Ty - y^TX\beta + \beta^TX^TX\beta$ and differentiate:
$\nabla S(\beta) = 2X^Ty - 2X^TX\beta$. Setting this to zero at $\beta=\hat\beta$ gives
$X^TX\hat\beta = X^Ty$, i.e. $\hat\beta=(X^TX)^{-1}X^Ty$.

**Fact 2 (Pythagorean identity).** For every $\beta$,

$$
S(\beta) = S(\hat\beta) + (\beta-\hat\beta)^TX^TX(\beta-\hat\beta).
$$

*Proof.* Write $y - X\beta = (y-X\hat\beta) + (X\hat\beta - X\beta)$ and expand the squared norm:

$$
S(\beta) = \|y-X\hat\beta\|^2 + \|X\hat\beta-X\beta\|^2 + 2\langle y-X\hat\beta,\, X\hat\beta-X\beta\rangle.
$$

The cross term vanishes: $\langle y-X\hat\beta, X\hat\beta-X\beta\rangle = (\hat\beta-\beta)^TX^T(y-X\hat\beta)
= (\hat\beta-\beta)^T(X^Ty - X^TX\hat\beta) = 0$ by Fact 1. $\square$

Fact 2 says $S(\beta)$ is a paraboloid centred at $\hat\beta$ with curvature matrix $X^TX$ — exactly
the shape that will match a $t$-density.

## Identifying the posterior as a multivariate $t$

The multivariate $t$-density $t_p(\mu,\Sigma,\nu)$, for a $p\times 1$ location $\mu$, a $p\times p$
scale matrix $\Sigma$, and degrees of freedom $\nu>0$, is

$$
f(x) = \frac{\Gamma((\nu+p)/2)}{\Gamma(\nu/2)\,\nu^{p/2}\pi^{p/2}\sqrt{\det\Sigma}}\left[1+\frac{1}{\nu}(x-\mu)^T\Sigma^{-1}(x-\mu)\right]^{-(\nu+p)/2}
\;\propto\; \left[1+\frac{1}{\nu}(x-\mu)^T\Sigma^{-1}(x-\mu)\right]^{-(\nu+p)/2}. \tag{3}
$$

Now use Fact 2 to rewrite $(*)$:

$$
f_{\beta\mid\text{data}}(\beta) \propto \left(\frac{S(\hat\beta)}{S(\hat\beta)+(\beta-\hat\beta)^TX^TX(\beta-\hat\beta)}\right)^{n/2}
= \left(\frac{1}{1+(\beta-\hat\beta)^T\dfrac{X^TX}{S(\hat\beta)}(\beta-\hat\beta)}\right)^{n/2}.
$$

Matching this to (3) with $x=\beta$, $p=m+1$, $\mu=\hat\beta$, $\nu+p=n$, and $\Sigma^{-1}/\nu = X^TX/S(\hat\beta)$
gives $\nu=n-m-1$ and $\Sigma = \dfrac{S(\hat\beta)}{n-m-1}(X^TX)^{-1}$. So the posterior of the whole
coefficient vector is exactly a multivariate $t$:

$$
\beta_0,\dots,\beta_m\mid\text{data} \;\sim\; t_{m+1}\!\left(\hat\beta,\; \frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1},\; n-m-1\right). \tag{1}
$$

This is the central result: the posterior is centred at the least-squares estimate, its spread is
governed by the same $(X^TX)^{-1}$ that appears in the classical sampling covariance of $\hat\beta$,
and the degrees of freedom $n-m-1$ is the usual residual degrees of freedom.

## Properties of the multivariate $t$-density

**Connection to the normal.** The quadratic form $(x-\mu)^T\Sigma^{-1}(x-\mu)$ in (3) is the same one
that appears in the multivariate normal density $N_p(\mu,\Sigma)$. The precise link: if
$X\sim N_p(\mu,\Sigma)$ and $V\sim\chi^2_\nu$ are independent, then

$$
T := \mu + \frac{X-\mu}{\sqrt{V/\nu}} \;\sim\; t_p(\mu,\Sigma,\nu). \tag{4}
$$

So $t_p(\mu,\Sigma,\nu)$ is what you get by taking a normal vector and inflating its deviation from
the mean by a random factor $1/\sqrt{V/\nu}$ that is at least $1$ on average — the extra randomness
in that inflation factor is exactly what gives the $t$-distribution its heavier tails than the
normal. A proof of (4) is given below.

**Components and linear combinations are also $t$.** If $T\sim t_p(\mu,\Sigma,\nu)$ with components
$T_1,\dots,T_p$, then every linear combination $a_0+a^TT$ is univariate $t$. Using (4),

$$
a_0+a^TT = (a_0+a^T\mu) + \frac{(a_0+a^TX)-(a_0+a^T\mu)}{\sqrt{V/\nu}},
$$

and since $a_0+a^TX \sim N(a_0+a^T\mu,\, a^T\Sigma a)$, applying (4) again (now in one dimension) gives

$$
a_0+a^TT \sim t_1(a_0+a^T\mu,\, a^T\Sigma a,\, \nu).
$$

Taking $a$ to be a coordinate vector, each component satisfies $T_j\sim t_1(\mu_j,\Sigma(j,j),\nu)$,
where $\Sigma(j,j)$ is the $j$th diagonal entry of $\Sigma$. This is what makes the individual
$\beta_j$ posteriors tractable even though the joint posterior (1) is a $(m+1)$-dimensional object.

**Large $\nu$: $t$ looks normal.** When $\nu$ is large, $(x-\mu)^T\Sigma^{-1}(x-\mu)/\nu$ is small, so
using $1+z\approx e^z$ for small $z$,

$$
\left[1+\frac{1}{\nu}(x-\mu)^T\Sigma^{-1}(x-\mu)\right]^{-(\nu+p)/2} \approx \exp\left(-\frac{\nu+p}{2\nu}(x-\mu)^T\Sigma^{-1}(x-\mu)\right) \approx \exp\left(-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)\right),
$$

because $(\nu+p)/\nu\approx 1$. So $t_p(\mu,\Sigma,\nu)\approx N_p(\mu,\Sigma)$ for large $\nu$. In the
regression posterior (1), $\nu=n-m-1$, so whenever there is a reasonable amount of data relative to
the number of covariates, the exact $t$-posterior and the normal approximation

$$
t_{m+1}\!\left(\hat\beta,\frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1},\,n-m-1\right) \approx N_{m+1}\!\left(\hat\beta,\frac{S(\hat\beta)}{n-m-1}(X^TX)^{-1}\right)
$$

are close, and the extra machinery of this chapter matters most precisely when $n-m-1$ is small.

## Proof of the mixture representation (4)

Condition on $V=x$: since $T\mid V=x \sim N(\mu, \frac{\nu}{x}\Sigma)$,

$$
f_{T\mid V=x}(y) = \frac{1}{(2\pi)^{p/2}\sqrt{\det(\frac{\nu}{x}\Sigma)}}\exp\left(-\frac12(y-\mu)^T\left(\frac{\nu}{x}\Sigma\right)^{-1}(y-\mu)\right)
= \frac{x^{p/2}}{(2\pi)^{p/2}\nu^{p/2}\sqrt{\det\Sigma}}\exp\left(-\frac{x}{2\nu}(y-\mu)^T\Sigma^{-1}(y-\mu)\right),
$$

using $\det(\frac\nu x\Sigma) = (\nu/x)^p\det\Sigma$. Averaging over the $\chi^2_\nu$ density of $V$,
$f_V(x)\propto x^{\nu/2-1}e^{-x/2}$,

$$
f_T(y) = \int_0^\infty f_{T\mid V=x}(y)f_V(x)\,dx \;\propto\; \int_0^\infty x^{\frac{p+\nu}{2}-1}\exp\left(-\frac{x}{2}\left[1+\frac1\nu(y-\mu)^T\Sigma^{-1}(y-\mu)\right]\right)dx.
$$

Substituting $t = x\left[1+\frac1\nu(y-\mu)^T\Sigma^{-1}(y-\mu)\right]$ pulls the bracketed factor out
of a now-standard Gamma integral:

$$
f_T(y) \propto \frac{1}{\left[1+\frac1\nu(y-\mu)^T\Sigma^{-1}(y-\mu)\right]^{(\nu+p)/2}}\int_0^\infty t^{\frac{\nu+p}{2}-1}e^{-t/2}dt
\propto \left[1+\frac1\nu(y-\mu)^T\Sigma^{-1}(y-\mu)\right]^{-(\nu+p)/2},
$$

which is exactly (3). $\square$

## Back to regression: intervals for individual coefficients

Write $\hat\sigma^2 := S(\hat\beta)/(n-m-1)$, so that $\hat\sigma$ is the usual (frequentist) unbiased
estimator of $\sigma$ — it can also be justified directly as a Bayesian point estimator, which is the
content of a homework exercise. It is commonly called the **residual standard error**. With this
notation, (1) becomes

$$
\beta_0,\dots,\beta_m\mid\text{data} \sim t_{m+1}\!\left(\hat\beta,\,\hat\sigma^2(X^TX)^{-1},\,n-m-1\right). \tag{6}
$$

Because components of a multivariate $t$ are univariate $t$, each coefficient's posterior is

$$
\beta_j\mid\text{data} \;\sim\; t_1\!\left(\hat\beta_j,\, \hat\sigma^2(X^TX)^{j+1,j+1},\, n-m-1\right),
$$

where $(X^TX)^{j+1,j+1}$ is the $(j+1)$th diagonal entry of $(X^TX)^{-1}$ (the shift by one is because
$\beta_j$ is the $(j+1)$th entry of $\beta$, the $0$th entry being $\beta_0$). Equivalently,

$$
\frac{\beta_j-\hat\beta_j}{\hat\sigma\sqrt{(X^TX)^{j+1,j+1}}} \;\sim\; \text{standard } t \text{ with } n-m-1 \text{ degrees of freedom},
$$

and the quantity $\hat\sigma\sqrt{(X^TX)^{j+1,j+1}}$ is the **standard error** of $\beta_j$. Letting
$t_{n-m-1,\alpha/2}$ denote the point beyond which the $t_{n-m-1}$ distribution puts probability
$\alpha/2$, this pivot gives

$$
\mathbb P\!\left(\hat\beta_j - \hat\sigma\sqrt{(X^TX)^{j+1,j+1}}\,t_{n-m-1,\alpha/2} \;\le\; \beta_j \;\le\; \hat\beta_j + \hat\sigma\sqrt{(X^TX)^{j+1,j+1}}\,t_{n-m-1,\alpha/2} \;\middle|\; \text{data}\right) = 1-\alpha.
$$

The resulting interval is the $100(1-\alpha)\%$ **Bayesian credible interval** for $\beta_j$, and it
coincides exactly with the frequentist $100(1-\alpha)\%$ confidence interval — the two philosophies
give the same numbers here, even though they mean different things by the probability statement.
When $n-m-1$ is large, this reduces to the familiar normal-based interval, since (6) and its
components are then close to $N_{m+1}(\hat\beta,\hat\sigma^2(X^TX)^{-1})$ and
$N(\hat\beta_j,\hat\sigma^2(X^TX)^{j+1,j+1})$ respectively.

## Extending to nonlinear regression

Everything above assumed the covariates enter the model linearly, so that $y = X\beta+\epsilon$ for a
design matrix $X$ built purely from the data. The next class of models has a parameter that enters
*nonlinearly* — through the argument of a function rather than as a coefficient. If that nonlinear
parameter were known, the model would collapse back to ordinary linear regression; the difficulty is
that it is not known, and it cannot be profiled out algebraically the way $\beta$ can. The recipe used
for both examples below is the same: fix the nonlinear parameter, minimize the sum of squares over
the linear coefficients (that's a linear-regression problem, solved as above), and then search over
the nonlinear parameter to minimize the resulting residual sum of squares.

### Example: the sinusoidal model

A sinusoid is $s(t) = R\cos(2\pi ft+\phi)$, with amplitude $R$, frequency $f$, phase $\phi$, and
period $1/f$. Using $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$, it can be rewritten
as

$$
s(t) = A\cos(2\pi ft) + B\sin(2\pi ft), \qquad A=R\cos\phi,\ B=R\sin\phi,
$$

a form in which $A,B$ appear linearly — the reason this representation is preferred when $s(t)$ is
embedded in a regression model. When time is sampled at integers $t=1,\dots,n$, the frequency can
always be taken to lie in $[0,1/2]$ without loss of generality:

**Fact.** For every $f,\phi\in(-\infty,\infty)$ there exist $f_0\in[0,1/2]$ and $\phi_0$ with
$R\cos(2\pi ft+\phi) = R\cos(2\pi f_0t+\phi_0)$ for every integer $t$.

*Proof.* If $f<0$, use $\cos(2\pi ft+\phi)=\cos(2\pi(-f)t-\phi)$ and $-f\ge 0$. If $f\ge 1$, write
$f=[f]+(f-[f])$; since $\cos$ has period $2\pi$ and $[f]$ is an integer, $\cos(2\pi ft+\phi) =
\cos(2\pi(f-[f])t+\phi)$ with $0\le f-[f]<1$. If $f\in[1/2,1)$, use
$\cos(2\pi ft+\phi)=\cos(2\pi t - 2\pi(1-f)t+\phi)=\cos(2\pi(1-f)t-\phi)$ (valid since $t$ is an
integer), and $0<1-f\le 1/2$. Chaining these reduces any $f$ to some $f_0\in[0,1/2]$. $\square$

At the boundary $f=0$, $s(t)=R\cos\phi$ is constant; at $f=1/2$, $s(t)=R(-1)^t\cos\phi$ oscillates
maximally between $R\cos\phi$ and $-R\cos\phi$.

The sinusoidal regression model for a series $y_1,\dots,y_n$ is

$$
y_t = \beta_0+\beta_1\cos(2\pi ft)+\beta_2\sin(2\pi ft)+\epsilon_t, \qquad \epsilon_t\stackrel{\text{i.i.d}}{\sim}N(0,\sigma^2),
$$

with unknowns $\beta_0,\beta_1,\beta_2,\sigma,f$, and $f\in[0,1/2]$ unknown (as for the sunspots data
the course fits it to). If $f$ were known this is ordinary linear regression with design matrix

$$
X_f = \begin{pmatrix}1 & \cos(2\pi f\cdot 1) & \sin(2\pi f\cdot 1)\\ \vdots & \vdots & \vdots \\ 1 & \cos(2\pi f\cdot n) & \sin(2\pi f\cdot n)\end{pmatrix}.
$$

**MLE.** For fixed $f$, $S(\beta,f)=\|y-X_f\beta\|^2$ is minimized at $\hat\beta(f)=(X_f^TX_f)^{-1}X_f^Ty$,
giving $\text{RSS}(f) := S(\hat\beta(f),f) = \min_\beta S(\beta,f)$. Since
$\min_{\beta,f}S(\beta,f)=\min_f\text{RSS}(f)$, the MLE is found by: (1) grid the candidate frequencies
$f\in[0,1/2]$; (2) for each grid value, regress $y$ on $X_f$ and record $\text{RSS}(f)$; (3) take
$\hat f$ to minimize $\text{RSS}(f)$ over the grid; (4) take $\hat\beta,\hat\sigma$ from the ordinary
regression of $y$ on $X_{\hat f}$.

**Bayesian posterior for $f$.** Uncertainty quantification for $\hat f$ is awkward classically, so the
course turns to the Bayesian route instead, with independent priors
$\beta_0,\beta_1,\beta_2,\log\sigma\sim\text{unif}(-C,C)$ and $f\sim\text{unif}[0,1/2]$. Dropping the
$C$-indicators as before, the joint posterior is

$$
\text{posterior}(\beta,f,\sigma) \propto \sigma^{-n-1}\exp\left(-\frac{S(\beta,f)}{2\sigma^2}\right) I\{\sigma>0\}I\{0\le f\le 1/2\}.
$$

To get the marginal posterior of $f$ — the parameter of real interest — integrate out $\beta$ and
$\sigma$. First, using the Pythagorean identity applied to $S(\beta,f)$ (in $\beta$, for fixed $f$),
the inner integral over $\beta$ is the normalizing constant of a $p$-dimensional normal density
($p=3$ here):

$$
\int\exp\left(-\frac{S(\beta,f)}{2\sigma^2}\right)d\beta = \exp\left(-\frac{\text{RSS}(f)}{2\sigma^2}\right)(2\pi)^{p/2}\sigma^p\,|X_f^TX_f|^{-1/2}.
$$

Substituting this in and integrating over $\sigma$ exactly as in the marginalization step earlier in
this chapter — except that the extra factor $\sigma^p$ shifts the power of $\sigma$ from $-n-1$ to
$-n+p-1$, which is the same computation with $n$ replaced by $n-p$ — gives

$$
\text{posterior}(f) \;\propto\; I\{0\le f\le 1/2\}\;|X_f^TX_f|^{-1/2}\,\text{RSS}(f)^{-(n-p)/2}.
$$

The dominant term is $\text{RSS}(f)^{-(n-p)/2}$: it is largest at the MLE $\hat f$, and the exponent
$n-p$ controls how tightly the posterior concentrates there — tighter as $n$ grows. This posterior is
evaluated numerically over a grid of $f\in(0,1/2)$; the endpoints $f=0,1/2$ must be excluded because
there $X_f$ loses full column rank and $|X_f^TX_f|^{-1/2}$ blows up.

### Example: change-of-slope ("broken-stick") regression

A second nonlinear model changes the slope of a straight line at an unknown time $c$:

$$
y_t = \beta_0+\beta_1t+\beta_2\,\text{ReLU}(t-c)+\epsilon_t, \qquad \epsilon_t\stackrel{\text{i.i.d}}{\sim}N(0,\sigma^2),
$$

where $\text{ReLU}(t-c)=(t-c)_+=(t-c)I\{t>c\}=\max(t-c,0)$ is the positive-part (ramp) function. For
$t\le c$ the slope of the mean function is $\beta_1$; for $t>c$ it becomes $\beta_1+\beta_2$ — hence
"change of slope", or "broken-stick regression", for the shape of the resulting piecewise-linear
curve.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A piecewise-linear mean function with a kink at time c, changing slope from beta 1 to beta 1 plus beta 2">
  <line x1="30" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1"/>
  <line x1="30" y1="170" x2="30" y2="20" stroke="currentColor" stroke-width="1"/>
  <line x1="45" y1="150" x2="160" y2="95" stroke="currentColor" stroke-width="2"/>
  <line x1="160" y1="95" x2="280" y2="35" stroke="currentColor" stroke-width="2"/>
  <line x1="160" y1="170" x2="160" y2="95" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="160" y="185" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="100" y="140" text-anchor="middle" font-size="12" fill="currentColor">slope &#946;&#8321;</text>
  <text x="225" y="55" text-anchor="middle" font-size="12" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;</text>
  <text x="300" y="185" text-anchor="middle" font-size="12" fill="currentColor">t</text>
</svg>
<figcaption>The change-of-slope model: a straight line with slope $\beta_1$ that kinks at the unknown
time $c$ and continues with slope $\beta_1+\beta_2$.</figcaption>
</figure>

The unknown parameters are $c,\beta_0,\beta_1,\beta_2,\sigma$; it is $c$ that makes the model
nonlinear. If $c$ were known, this is again ordinary linear regression, $y=X_c\beta+\epsilon$, with

$$
X_c = \begin{pmatrix}1&1&\text{ReLU}(1-c)\\ 1&2&\text{ReLU}(2-c)\\ \vdots&\vdots&\vdots\\ 1&n&\text{ReLU}(n-c)\end{pmatrix}, \qquad \beta=\begin{pmatrix}\beta_0\\\beta_1\\\beta_2\end{pmatrix}.
$$

Least squares again minimizes $S(\beta,c) = \|y-X_c\beta\|^2$ over all four unknowns
$\beta_0,\beta_1,\beta_2,c$. Exactly as in the sinusoidal case, fixing $c$ turns this into an ordinary
linear-regression problem, minimized (by Fact 1 above) at

$$
\hat\beta_c := (X_c^TX_c)^{-1}X_c^Ty.
$$

The source material breaks off at this formula. The natural continuation — following exactly the
same recipe carried through in full for the frequency $f$ above — would be to record
$\text{RSS}(c) = S(\hat\beta_c,c)$, grid the candidate values of $c$, and take $\hat c$ to be the grid
value minimizing $\text{RSS}(c)$; this is not spelled out in the lecture material supplied here.

## Sources

- Derivation of the Bayesian posterior for $\beta$ via marginalizing out $\sigma$ (the flat-prior
  model, the $\sigma^{-n-1}$ joint posterior, and the integral leading to $(*)$): STAT 153/248,
  UC Berkeley, Fall 2026, Lecture Five, §1 ("Bayesian Inference for Linear Regression" through
  §1.2), Aditya Guntuboyina, 10 September 2026.
- Matrix notation, Fact 1 (normal equations) and Fact 2 (Pythagorean identity), and the matching of
  the posterior to the multivariate $t$-density giving (1): same source, §1.2, and cross-checked
  against Fall 2025, Lecture Five, part 1 ("1 Posterior $t$-density in Multiple Linear Regression"),
  11 September 2025, which states result (1) without re-deriving it ("In the last lecture, we saw
  the following formula...") — the Fall 2026 notes supply the derivation the Fall 2025 notes assume.
- Definition and properties of the multivariate $t$-density $t_p(\mu,\Sigma,\nu)$ (mixture
  representation, components/linear combinations also $t$, large-$\nu$ normal approximation):
  Fall 2025, Lecture Five, part 2 ("2 $t$-density"), matching Fall 2026 §1.1 essentially verbatim.
  Both cite Wikipedia's article on the multivariate $t$-distribution as their source for the density
  formula.
- Proof of the mixture representation (4): Fall 2025, Lecture Five, part 4 ("4 Proof of (4)").
- Credible intervals for individual $\beta_j$, the residual standard error $\hat\sigma$, and the
  equivalence with the frequentist confidence interval: Fall 2025, Lecture Five, part 3 ("3 Back to
  Regression"), matching Fall 2026 §1.3. The claim that $\hat\sigma$ is also a Bayesian estimator is
  attributed to a homework exercise — Fall 2025 cites "Question 5(e) of Homework One", Fall 2026
  cites "Question 4(e) of Homework One"; the homework itself is not part of the supplied material.
- The general nonlinear-regression framing and the change-of-slope/broken-stick model: Fall 2025,
  Lecture Five, part 5 ("5 Nonlinear Regression"). This file is truncated mid-derivation in the
  source conversion, immediately after the formula for $\hat\beta_c$; nothing past that point was
  taught in the supplied material, and the closing paragraph of that section says so explicitly.
- The sinusoidal model, the restriction of frequency to $[0,1/2]$ and its proof, the MLE grid-search
  algorithm, and the Bayesian marginal posterior for $f$: STAT 153/248, Spring 2025, Lecture Five,
  parts 2–3 ("2 The Sinusoid", "3 The sinusoidal model"), Aditya Guntuboyina, 4 February 2025.
- All of the above are model-reconstructed conversions (route: llm, fidelity: reconstructed) of PDF
  slide/notes decks with no text layer; per their own headers, every displayed equation is
  unverified against the original PDF. Treat the numbered equations here as a best-effort transcription of that reconstruction, not as independently checked mathematics.

---

[← 103. Smoothing the Periodogram (part 3)](103-smoothing-the-periodogram-part-3.md) · [Contents](index.md) · [105. Frequentist and Bayesian Linear Regression →](105-frequentist-and-bayesian-linear-regression.md)
