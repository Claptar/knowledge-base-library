---
title: "61. Wald, Score, and Likelihood-Ratio Tests (part 2)"
course: "Berkeley Stat 210A"
chapter: 61
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 61. Wald, Score, and Likelihood-Ratio Tests (part 2)

## What this covers

This chapter turns the asymptotic normality of the MLE into actual tests and confidence regions for
$\theta$, and develops three classical constructions — the Wald test, the score (Rao) test, and the
generalized likelihood ratio test (GLRT) — that each answer "is $\theta=\theta_0$ plausible?" using a
different piece of the log-likelihood. It closes by comparing estimators directly, via asymptotic
relative efficiency. It assumes the asymptotic-normality result for the MLE (consistency, the score
CLT, Fisher information $J_1(\theta)$) and multivariate Slutsky; the first section recaps that
background just far enough to fix notation.

## The MLE is asymptotically normal (recap)

Setting: $X_1,\dots,X_n \overset{\mathrm{iid}}{\sim} p_\theta(x)$, $\theta\in\Theta\subset\mathbb R^d$,
with $p_\theta(x)$ smooth in $\theta$. Write $\ell(\theta;x)=\log p_\theta(x)$ and
$\ell_n(\theta;X)=\sum_{i=1}^n \ell(\theta;X_i)$ for the log-likelihood. Assume the usual regularity,

$$\mathbb E_\theta \nabla\ell(\theta;X_i) = 0, \qquad \mathrm{Var}_\theta[\nabla\ell(\theta;X_i)] =
-\mathbb E_\theta \nabla^2\ell(\theta;X_i) = J_1(\theta) \succ 0,$$

and that $\hat\theta_n=\hat\theta_{\mathrm{MLE}}$ is consistent, $\hat\theta_n\xrightarrow{P_\theta}\theta$.
Here $J_1(\theta)$ is the Fisher information carried by *one* observation; write $J_n(\theta) :=
nJ_1(\theta)$ for the information in the full sample — a deterministic function of $\theta$, not a
random variable, once $\theta$ is fixed.

Under $\theta=\theta_0$, the score is a sum of iid mean-zero terms and the Hessian is an average, so

$$\frac{1}{\sqrt n}\nabla\ell_n(\theta_0;X) \Rightarrow \mathcal N_d(0, J_1(\theta_0)) \qquad\text{(CLT)},
\qquad \frac1n \nabla^2\ell_n(\theta_0;X) \xrightarrow{P} -J_1(\theta_0) \qquad\text{(LLN)}.$$

Taylor-expanding the score equation $0=\nabla\ell_n(\hat\theta_n)$ around $\theta_0$,

$$0 = \nabla\ell_n(\hat\theta_n) \approx \nabla\ell_n(\theta_0) + \nabla^2\ell_n(\theta_0)(\hat\theta_n-\theta_0),$$

and solving for $\hat\theta_n-\theta_0$ turns the CLT and the LLN into

$$\sqrt n(\hat\theta_n-\theta_0) \Rightarrow \mathcal N_d\bigl(0, J_1(\theta_0)^{-1}\bigr).$$

This one display is what everything below is built from: it says the MLE is approximately
$\mathcal N_d(\theta_0, J_n(\theta_0)^{-1})$, and inference on $\theta_0$ becomes a matter of inverting
that approximate distribution.

## Confidence regions from the Wald pivot

Suppose $\hat J_n \succ 0$ is *some* estimator with $\frac1n\hat J_n \xrightarrow{P} J_1(\theta_0)\succ 0$
— not necessarily the MLE-based one, just consistent. Standardizing,

$$J_1(\theta_0)^{1/2}\sqrt n(\hat\theta_n-\theta_0) \Rightarrow \mathcal N_d(0,I_d) \quad\Longrightarrow\quad
\hat J_n^{1/2}(\hat\theta_n-\theta_0) \Rightarrow \mathcal N_d(0,I_d) \qquad\text{(Slutsky)},$$

the last step replacing the unknown $J_1(\theta_0)$ by its consistent estimate. Squaring the norm gives
a pivot whose limiting distribution does not depend on $\theta_0$:

$$\bigl\|\hat J_n^{1/2}(\hat\theta_n-\theta_0)\bigr\|^2 \;\Rightarrow\; \chi^2_d,$$

so the test "reject $H_0:\theta=\theta_0$ when this statistic is large" has asymptotic level $\alpha$
against the $1-\alpha$ quantile $\chi^2_d(\alpha)$:
$\mathbb P_{\theta_0}\bigl(\|\hat J_n^{1/2}(\hat\theta_n-\theta_0)\|^2 \ge \chi^2_d(\alpha)\bigr) \to \alpha$.

Inverting the test — collecting every $\theta_0$ that is *not* rejected — gives the **Wald confidence
ellipsoid**:

$$\text{reject } \theta_0 \iff \theta_0 \notin \hat\theta_n + \hat J_n^{-1/2} B_{\chi^2_d(\alpha)}(0).$$

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="A confidence ellipsoid centered at the MLE, containing one hypothesized value and excluding another">
  <ellipse cx="160" cy="120" rx="100" ry="55" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="160" cy="120" r="3" fill="currentColor"/>
  <text x="160" y="106" text-anchor="middle" font-size="12" fill="currentColor">MLE</text>
  <circle cx="125" cy="100" r="3" fill="currentColor"/>
  <text x="125" y="88" text-anchor="middle" font-size="12" fill="currentColor">theta_0</text>
  <text x="125" y="212" text-anchor="middle" font-size="11" fill="currentColor">not rejected</text>
  <circle cx="278" cy="72" r="3" fill="currentColor"/>
  <text x="278" y="60" text-anchor="middle" font-size="12" fill="currentColor">theta_0'</text>
  <text x="278" y="212" text-anchor="middle" font-size="11" fill="currentColor">rejected</text>
</svg>
<figcaption>The Wald confidence ellipsoid is centered at the MLE $\hat\theta_n$ and shaped by
$\hat J_n$; a hypothesized value is rejected exactly when it lands outside it. More data means a
smaller ellipse, shrinking like $1/\sqrt n$ since $\hat J_n$ itself grows like $n$.</figcaption>
</figure>

## Choosing $\hat J_n$: plug-in vs. observed information

The Wald construction only asked for *some* consistent $\hat J_n$; two natural choices differ in what
they condition on.

1. **Plug-in (expected) information.** Substitute the MLE into $J_n(\theta)$ itself:
   $$\hat J_n = J_n(\hat\theta_n) = \mathrm{Var}_\theta\bigl(\nabla\ell_n(\theta;X)\bigr)\Big|_{\theta=\hat\theta_n}
   = -\mathbb E_\theta \nabla^2\ell_n(\theta)\Big|_{\theta=\hat\theta_n}.$$
   A trap worth naming: this is **not** the same object as
   $\mathrm{Var}_{\hat\theta_n}\bigl(\nabla\ell_n(\hat\theta_n(X);X)\bigr)$, which is identically $0$ —
   the score evaluated *at the MLE computed from the same data* is always zero by definition of the
   MLE. The plug-in information asks "how variable would the score at $\hat\theta_n$ be across
   hypothetical new data sets", not "how variable is the observed score", and the two questions have
   different answers.

2. **Observed Fisher information.** Don't take an expectation at all — evaluate the curvature of the
   actual log-likelihood at $\hat\theta_n$:
   $$\hat J_n = -\nabla^2\ell_n(\hat\theta_n;X).$$

Both satisfy $\frac1n\hat J_n \xrightarrow{P} J_1(\theta_0)$ in the "nice" iid setting, and both continue
to make sense outside it, wherever there is a log-likelihood to differentiate. Heuristically, the
plug-in version measures the information about $\theta$ in a "typical" data set, while the observed
version measures the information in *this* data set.

## Wald intervals for one coordinate or a subvector

Since $\hat\theta_n \approx \mathcal N_d(\theta_0, J_n(\theta_0)^{-1})$, each coordinate is
approximately univariate normal, $\hat\theta_{n,j} \approx \mathcal N_1\bigl(\theta_{0,j},
(J_n(\theta_0)^{-1})_{jj}\bigr)$, which gives the familiar interval

$$C_j = \hat\theta_{n,j} \pm \widehat{\mathrm{s.e.}}(\hat\theta_{n,j})\cdot z_{\alpha/2}, \qquad
\widehat{\mathrm{s.e.}}(\hat\theta_{n,j}) = \sqrt{(\hat J_n^{-1})_{jj}}.$$

This is exactly what R's `glm` reports, using the observed information $\hat J_n = -\nabla^2\ell(\hat\theta_n)$.

The same idea covers a subvector $\theta_{0,S}=(\theta_{0,j})_{j\in S}$ with $|S|=k$:

$$\hat\theta_{n,S} \approx \mathcal N_k\bigl(\theta_{0,S}, (J_n(\theta_0)^{-1})_{SS}\bigr) \quad\leadsto\quad
C_S = \hat\theta_{n,S} + \bigl((\hat J_n^{-1})_{SS}\bigr)^{1/2}B_{\chi^2_k(\alpha)}(0).$$

Nothing here actually required $\hat\theta_n$ to be the MLE: if $\sqrt n(\hat\theta_n-\theta_0)
\Rightarrow \mathcal N(0,\Sigma(\theta_0))$ for some other consistent, asymptotically normal estimator,
with a consistent $\hat\Sigma_n$ for $n\Sigma(\theta_0)$, every construction above goes through
unchanged with $\hat J_n^{-1}$ replaced by $\hat\Sigma_n$.

## Worked example: canonical generalized linear models

Fix $x_1,\dots,x_n\in\mathbb R^d$ (non-random), and let $Y_i$ be independent draws from a
one-parameter exponential family in canonical form,

$$Y_i \sim p_{\eta_i}(y) = e^{\eta_i y - A(\eta_i)} h(y), \qquad \eta_i = \beta'x_i,$$

so $\beta$ is the parameter of interest and $\eta_i(\beta)$ is the *natural* (canonical) parameter for
observation $i$. Write $\mu_i(\beta) = \mathbb E_\beta Y_i$ for the mean. Logistic regression
($Y_i\sim\mathrm{Bern}(e^{x_i'\beta}/(1+e^{x_i'\beta}))$) and the Poisson log-linear model
($Y_i\sim\mathrm{Pois}(e^{x_i'\beta})$) are the two standard examples.

The log-likelihood, score, and negative Hessian are

$$\ell_n(\beta;Y) = \sum_i \bigl[\eta_i y_i - A(\eta_i) + \log h(y_i)\bigr], \qquad \nabla\ell_n(\beta;Y) =
\sum_i (y_i-\mu_i(\beta))\,x_i,$$

$$-\nabla^2\ell_n(\beta;Y) = \sum_i \ddot A(x_i'\beta)\,x_ix_i' = \sum_i \mathrm{Var}_\beta(Y_i)\,x_ix_i' =
\mathrm{Var}_\beta\bigl(\nabla\ell_n(\beta;Y)\bigr),$$

using $\ddot A(\eta) = \mathrm{Var}(Y)$ for an exponential family. The last display is worth pausing on:
the negative Hessian here is **not random** — it depends on $\beta$ and the fixed design
$x_1,\dots,x_n$ only, never on the data $Y$. So for a canonical GLM the observed and expected Fisher
information are literally the same quantity; the distinction from the previous section collapses.

Because the negative Hessian doesn't depend on $Y$, there is an exact finite-sample statement before
any asymptotics: $\bigl(-\nabla^2\ell_n(\beta)\bigr)^{-1/2}\nabla\ell_n(\beta)$ has mean $0$ and
covariance $I_d$ for *every* $n$, and, under regularity conditions on the design matrix $X$ whose rows
are the $x_i'$, converges in distribution to $\mathcal N_d(0,I_d)$. Taylor-expanding $\ell_n$ as before
recovers the general result, $\hat J_n^{1/2}(\hat\beta_n-\beta) \Rightarrow \mathcal N_d(0,I_d)$.

This example is also a convenient place to weigh the Wald test against the alternatives developed
below.

**Advantages:** it is easy to invert into simple confidence regions, and it is asymptotically correct.

**Disadvantages:** it requires computing the MLE $\hat\beta_n$; it depends on the parameterization used
(reparameterize $\beta$ and the same confidence set becomes a different shape); it relies on two
approximations at once — that $\nabla\ell_n$ is close to Gaussian *and* that $\ell_n$ is close to
quadratic; it needs $\hat\beta_n$ to be consistent to begin with; and the resulting interval or
ellipsoid can land outside $\Theta$ altogether.

## The score test: testing without fitting $\hat\theta_n$

Several of the Wald test's weaknesses trace back to needing $\hat\theta_n$ and a quadratic
approximation to $\ell_n$ around it. The **score test** avoids both, by using the score itself,
evaluated at the *hypothesized* value $\theta_0$, as the test statistic. From the recap, under
$H_0:\theta=\theta_0$,

$$\frac{1}{\sqrt n}\nabla\ell_n(\theta_0;X) \Rightarrow \mathcal N_d(0,J_1(\theta_0)), \qquad\text{equivalently}\qquad
J_n(\theta_0)^{-1/2}\nabla\ell_n(\theta_0;X) \Rightarrow \mathcal N_d(0,I_d).$$

So reject $H_0$ when

$$\bigl\|J_n(\theta_0)^{-1/2}\nabla\ell_n(\theta_0;X)\bigr\|_2^2 \ge \chi^2_d(\alpha).$$

For $d=1$ this is $\dot\ell_n(\theta_0)/\sqrt{J_n(\theta_0)} \Rightarrow \mathcal N(0,1)$, which — unlike
the squared Wald and GLRT statistics — retains a sign, so one-sided tests come for free.

Two things distinguish this from the Wald test, and both come from evaluating everything *at
$\theta_0$* rather than at an estimate:

- **No quadratic approximation to $\ell_n$, and no MLE.** The test statistic is the score itself, not
  a Taylor expansion of the likelihood around a fitted value.
- **No need to estimate Fisher information.** $J_n(\theta_0)$ is a known function of the hypothesized
  $\theta_0$ — there is nothing to plug an estimate into, because $\theta_0$ is not itself estimated.

The test generalizes to hypotheses with nuisance parameters (only part of $\theta$ is fixed under
$H_0$); the standard approach is to estimate the nuisance coordinates by maximizing the likelihood
over the constrained set $\Theta_0$.

## Why the score test doesn't care how you parameterize

Reparameterization-invariance is exactly what the Wald test lacks. Suppose $d=1$ and $\theta=g(\zeta)$
for a smooth increasing $g$ ($\dot g(\zeta)>0$ for all $\zeta$), so $q_\zeta(x) := p_{g(\zeta)}(x)$ is
the model written in the $\zeta$-parameterization. By the chain rule,

$$\dot\ell^{(\zeta)}(\zeta;x) = \frac{d}{d\zeta}\log p_{g(\zeta)}(x) = \dot\ell^{(\theta)}(g(\zeta);x)\cdot\dot g(\zeta),$$

and since Fisher information is (minus) an expected second derivative, it picks up the square of the
same factor: $J^{(\zeta)}(\zeta) = J^{(\theta)}(g(\zeta))\cdot \dot g(\zeta)^2$. The factor of
$\dot g(\zeta)$ then cancels between numerator and denominator of the standardized score:

$$\frac{\dot\ell^{(\zeta)}(\zeta_0;x)}{\sqrt{J^{(\zeta)}(\zeta_0)}} = \frac{\dot\ell^{(\theta)}(\theta_0;x)}{\sqrt{J^{(\theta)}(\theta_0)}}
\qquad\text{whenever } \theta_0=g(\zeta_0).$$

So the score test statistic — hence the test itself — is exactly the same regardless of which smooth
coordinate is used to describe $\theta$.

## Worked example: exponential families and Pearson's chi-squared test

**A full exponential family.** Let $X_1,\dots,X_n \overset{\mathrm{iid}}{\sim} e^{\eta'T(x)-A(\eta)}h(x)$
be an $s$-parameter exponential family in its natural parameter $\eta$. The score is

$$\nabla\ell(\eta;X) = \sum_i T(X_i) - n\mu(\eta),$$

so the score test of $H_0:\eta=\eta_0$ compares the sum of the sufficient statistic to its expectation
under $\eta_0$:

$$\bigl\|J_n(\eta_0)^{-1/2}\bigl(\textstyle\sum_i T(X_i)-n\mu(\eta_0)\bigr)\bigr\|^2 \Rightarrow \chi^2_d,
\qquad\text{or, for } s=1, \qquad \frac{\sum_i T(X_i) - n\mu(\eta_0)}{\sqrt{n\,\mathrm{Var}_{\eta_0}(T(X_i))}}
\Rightarrow \mathcal N(0,1).$$

**Pearson's $\chi^2$ goodness-of-fit test.** Take $N=(N_1,\dots,N_d)\sim\mathrm{Multinomial}(n,\pi)$
with $\sum_j\pi_j=1$. This is a full-rank $(d-1)$-parameter exponential family: writing
$\eta_2,\dots,\eta_d$ for the log-odds against category $1$,

$$\pi_1 = \frac{1}{1+\sum_{k>1}e^{\eta_k}}, \qquad \pi_j = \frac{e^{\eta_j}}{1+\sum_{k>1}e^{\eta_k}}\ (j>1),$$

the score in $\eta$ is $\nabla\ell(\eta;N) = (N_2,\dots,N_d) - n(\pi_2,\dots,\pi_d)$, with covariance

$$\mathrm{Var}_\eta(\nabla\ell(\eta)) = n\bigl(\mathrm{diag}(\pi_{2:d}) - \pi_{2:d}\pi_{2:d}'\bigr).$$

Inverting this (Sherman–Morrison) gives $J_n(\eta)^{-1} = \frac1n\bigl[(\mathrm{diag}(\pi_{2:d}))^{-1} -
\pi_1^{-1}\mathbf 1\mathbf 1'\bigr]$, and substituting into the score-test statistic for
$H_0:\pi=\pi_0$, after algebra, collapses to the classical statistic:

$$\nabla\ell_n(\eta_0)'J_n(\eta_0)^{-1}\nabla\ell_n(\eta_0) = \sum_{j=1}^d \frac{(N_j-n\pi_{0,j})^2}{n\pi_{0,j}}
\;\Rightarrow\; \chi^2_{d-1}.$$

So Pearson's familiar "observed minus expected, squared, over expected" statistic *is* the score test
for the multinomial model — though, being a classical result in its own right, it doesn't actually
need the general asymptotic machinery to justify it.

## The generalized likelihood ratio test

For the simple hypothesis $H_0:\theta=\theta_0$ vs. $H_1:\theta\neq\theta_0$, Taylor-expand the
log-likelihood — this time around $\hat\theta_n$ rather than $\theta_0$:

$$\ell_n(\theta_0)-\ell_n(\hat\theta_n) = \underbrace{\nabla\ell_n(\hat\theta_n)}_{=0}{}'(\theta_0-\hat\theta_n)
+ \tfrac12(\theta_0-\hat\theta_n)'\nabla^2\ell_n(\tilde\theta_n)(\theta_0-\hat\theta_n)$$

(the linear term vanishes because $\hat\theta_n$ is a stationary point of $\ell_n$). Writing
$-\frac1n\nabla^2\ell_n(\tilde\theta_n) \xrightarrow{P} J_1(\theta_0)$ and
$\sqrt n(\theta_0-\hat\theta_n)\Rightarrow \mathcal N(0,J_1(\theta_0)^{-1})$,

$$\ell_n(\theta_0) - \ell_n(\hat\theta_n) \approx -\tfrac12\Bigl\|\bigl(-\tfrac1n\nabla^2\ell_n(\tilde\theta_n)\bigr)^{1/2}
\sqrt n(\theta_0-\hat\theta_n)\Bigr\|_2^2 \;\Rightarrow\; -\tfrac12\chi^2_d,$$

so the **generalized likelihood ratio statistic**

$$2\bigl(\ell_n(\hat\theta_n;X) - \ell_n(\theta_0;X)\bigr) \;\overset{P_{\theta_0}}{\Longrightarrow}\; \chi^2_d.$$

## Composite null hypotheses: a projection argument

The same idea extends to a composite null $H_0:\theta\in\Theta_0$ against $H_1:\theta\in\Theta\setminus
\Theta_0$, where $\Theta=\mathbb R^d$ and $\Theta_0$ is a $d_0$-dimensional manifold, provided
$\theta_0\in\mathrm{relint}(\Theta_0)$, the unconstrained MLE $\hat\theta_n\xrightarrow{P_{\theta_0}}\theta_0$,
and the likelihood is smooth. Let $\hat\theta_0 = \operatorname{argmax}_{\theta\in\Theta_0}\ell_n(\theta;X)$
be the *constrained* MLE. Then

$$2\bigl(\ell_n(\hat\theta_n)-\ell_n(\hat\theta_0)\bigr) \;\Rightarrow\; \chi^2_{d-d_0},$$

with $d-d_0$ — the codimension of $\Theta_0$, i.e. the number of independent restrictions $H_0$
imposes — replacing the $d$ of the simple-hypothesis case.

Why this particular degrees of freedom? Reparameterize (this can always be done locally) so that
$\theta_0=0$ and $J_1(0)=I_d$. Then $\hat\theta_n \approx \mathcal N_d(0,\tfrac1n I_d)$, and near
$\theta_0$ the log-likelihood is locally a quadratic bowl, $\nabla^2\ell_n(\theta)\approx -nI_d$, so

$$\ell_n(\theta) - \ell_n(\hat\theta_n) \approx \tfrac n2\|\theta-\hat\theta_n\|^2.$$

Maximizing the right side over $\theta\in\Theta_0$ is just Euclidean projection, so
$\hat\theta_0\approx \mathrm{Proj}_{\Theta_0}(\hat\theta_n)$, and

$$2\bigl(\ell_n(\hat\theta_n)-\ell_n(\hat\theta_0)\bigr) \approx n\|\hat\theta_n - \mathrm{Proj}_{\Theta_0}(\hat\theta_n)\|^2
= n\bigl\|\mathrm{Proj}_{\Theta_0}^{\perp}(\hat\theta_n)\bigr\|^2.$$

Since $\hat\theta_n\approx\mathcal N_d(0,\tfrac1nI_d)$ in these (now orthonormal) local coordinates, the
component of $\sqrt n\,\hat\theta_n$ orthogonal to the $d_0$-dimensional $\Theta_0$ lives in a
$(d-d_0)$-dimensional space and is standard Gaussian there — so its squared norm is $\chi^2_{d-d_0}$.

## The three tests are asymptotically the same test

Near $\hat\theta_n$, all three constructions are reading off the same quadratic approximation to the
log-likelihood. For $d=1$,

$$\ell_n(\theta) - \ell_n(\theta_0) \approx \dot\ell_n(\theta_0)(\theta-\theta_0) + \tfrac12
J_n(\theta_0)(\theta-\theta_0)^2,$$

and each test statistic reads a different feature of this parabola:

- **GLRT** reads the height at the top: $\ell_n(\hat\theta_n)-\ell_n(\theta_0) \approx \tfrac12
  J_n(\theta_0)^{-1}\dot\ell_n(\theta_0)^2$.
- **Score** reads the slope at $\theta_0$: the test statistic *is* $\dot\ell_n(\theta_0)$.
- **Wald** reads the horizontal distance to the top: $\hat\theta_n-\theta_0 \approx
  J_n(\theta_0)^{-1}\dot\ell_n(\theta_0)$.

For large $n$ these are the same number, up to the substitutions each test uses in practice ($\hat
J_n$ in place of $J_n(\theta_0)$, and so on):

$$\underbrace{\ell_n(\hat\theta_n)-\ell_n(\theta_0)}_{\text{GLRT}} \approx
\bigl\|J_n(\theta_0)^{1/2}(\hat\theta_n-\theta_0)\bigr\|^2 \approx
\underbrace{\bigl\|\hat J_n^{1/2}(\hat\theta_n-\theta_0)\bigr\|^2}_{\text{Wald}} \approx
\underbrace{\bigl\|J_n(\theta_0)^{-1/2}\nabla\ell_n(\theta_0)\bigr\|^2}_{\text{Score}}.$$

So the three tests share the same limiting null distribution and, to first order, the same numeric
value. The choice between them in practice is about the finite-sample trade-offs from the sections
above — needing $\hat\theta_n$, sensitivity to parameterization, needing a nuisance-parameter estimate
— not about which one is "more correct" asymptotically.

## Comparing estimators: asymptotic relative efficiency

Suppose $\hat\theta_n^{(1)}, \hat\theta_n^{(2)}$ are two asymptotically normal estimators of a scalar
$\theta$, $\sqrt n(\hat\theta_n^{(i)}-\theta_0)\Rightarrow\mathcal N(0,\sigma_i^2)$. The **asymptotic
relative efficiency (ARE)** of $\hat\theta^{(2)}$ with respect to $\hat\theta^{(1)}$ is
$\sigma_1^2/\sigma_2^2$; e.g. if $\sigma_2^2=2\sigma_1^2$, then $\hat\theta^{(2)}$ is $50\%$ as
efficient as $\hat\theta^{(1)}$.

The number has a concrete reading. If $\sigma_1^2/\sigma_2^2 = \gamma\in(0,1)$, then for large $n$

$$\hat\theta^{(1)}_{\lfloor \gamma n\rfloor}(X_1,\dots,X_{\lfloor\gamma n\rfloor}) \overset{D}{\approx}
\hat\theta^{(2)}_n(X_1,\dots,X_n) \approx \mathcal N\Bigl(\theta,\frac{\sigma_2^2}{n}\Bigr):$$

using $\hat\theta^{(2)}$ on all $n$ observations is, in distribution, the same as throwing away
$100(1-\gamma)\%$ of the data and applying $\hat\theta^{(1)}$ to what's left.

## Sources

- Handwritten lecture notes, *Likelihood-Based Inference* — Berkeley STAT 210A, fall 2024,
  `handwritten/lecture23-likelihoodbasedinference.pdf`, reconstructed as four pages: Outline; Ex.
  generalized linear model with fixed $x$; Part 03 (score test, its invariance, and its examples);
  Generalized LRT. This offering has the complete lecture and is the primary source for the whole
  chapter.
- The same lecture recurs in fall 2025 and fall 2026
  (`handwritten/lecture23-likelihoodbasedinference.md` in each), with essentially identical material
  through the Wald test, the choice of $\hat J_n$, and the Wald interval/ellipsoid — including the
  same hand-drawn confidence-ellipsoid figure the SVG above reconstructs. Both of those conversions
  stop at a placeholder "## Ex" heading, so the GLM example, the score test, the reparameterization
  argument, the exponential-family and Pearson examples, the GLRT, the composite-hypothesis
  projection argument, and asymptotic relative efficiency are drawn from the fall-2024 version only.
- All six source files are model reconstructions of a handwritten PDF with no text layer
  ("fidelity: reconstructed"); every displayed equation is flagged unverified in the source. One
  inconsistency was resolved for internal consistency rather than left as transcribed: the
  fall-2024 note's GLM log-likelihood was OCR'd with a $-\log h(y_i)$ term, which contradicts the
  density $p_{\eta_i}(y) = e^{\eta_i y_i - A(\eta_i)}h(y_i)$ given two lines above it in the same
  note; this chapter uses $+\log h(y_i)$, matching that density.
- No slide deck, transcript, or problem set was supplied for this lecture.

---

[← 60. Wald, Score, and Likelihood-Ratio Tests (part 1)](60-wald-score-and-likelihood-ratio-tests-part-1.md) · [Contents](index.md) · [62. The Nonparametric Bootstrap →](62-the-nonparametric-bootstrap.md)
