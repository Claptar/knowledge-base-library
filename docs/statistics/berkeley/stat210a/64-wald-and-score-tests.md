---
title: "64. Wald and Score Tests"
course: "Berkeley Stat 210A"
chapter: 64
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 64. Wald and Score Tests

## What this covers

This chapter answers: once the maximum likelihood estimator (MLE) is known to be asymptotically normal, how do
you turn that into a confidence region or a hypothesis test for $\theta$ — and is there a way to test
$H_0:\theta=\theta_0$ without ever computing the MLE at all? It builds directly on the asymptotic theory of the
MLE: consistency, the score function, and the Fisher information $J(\theta)$. It assumes comfort with the central
limit theorem, Slutsky's theorem, the $\chi^2$ distribution as a sum of squared normals, and the basic language of
hypothesis testing (Neyman–Pearson, one- and two-sided tests).

## The setting

Let $X_1,\ldots,X_n \stackrel{\text{iid}}{\sim} p_\theta$, with $p_\theta \in \mathcal P$ smooth in
$\theta \in \mathbb R^d$. Write $\ell_\theta(x) = \log p_\theta(x)$ for the log-likelihood of a single observation
and $\ell_n(\theta;X) = \sum_{i=1}^n \ell_\theta(X_i)$ for the log-likelihood of the whole sample, with score
$\nabla \ell_n(\theta;X) = \sum_i \nabla\ell_\theta(X_i)$.

Three standing assumptions carry the whole chapter:

- $\mathbb E_\theta[\nabla\ell_\theta(X)] = 0$ — the score has mean zero at the truth,
- $\operatorname{Var}_\theta[\nabla\ell_\theta(X)] = \mathbb E_\theta[-\nabla^2\ell_\theta(X)] = J(\theta) > 0$ — the
  two standard expressions for the (per-observation) Fisher information agree and are positive definite,
- the MLE $\hat\theta$ is consistent.

Two consequences follow from the CLT and the law of large numbers, at the true parameter $\theta_0$:

$$\nabla\ell_n(\theta_0;X) \sim N(0, nJ(\theta_0)), \qquad -\nabla^2\ell_n(\theta_0;X) \xrightarrow{p} nJ(\theta_0).$$

These two facts — the score is asymptotically normal, and the curvature of the log-likelihood stabilizes — are
what everything below is built from.

## Asymptotic normality of the MLE

The MLE solves $\nabla\ell_n(\hat\theta;X)=0$. Expand the score around $\theta_0$ and set the expansion at
$\hat\theta$ to zero:

$$0 = \nabla\ell_n(\hat\theta;X) \approx \nabla\ell_n(\theta_0;X) + \nabla^2\ell_n(\theta_0;X)(\hat\theta-\theta_0).$$

Rearranging, and using $-\nabla^2\ell_n(\theta_0;X)/n \xrightarrow{p} J(\theta_0)$,

$$\hat\theta = \theta_0 + J^{-1}(\theta_0)\,\frac{\nabla\ell_n(\theta_0;X)}{n} + o_p(n^{-1/2}).$$

The remainder term is the content of a regularity argument (uniform convergence of the Hessian, consistency of
$\hat\theta$) that this chapter takes as given. Combining this "one-step" expansion with the normality of the
score,

$$\sqrt n(\hat\theta - \theta_0) \xrightarrow{d} N\big(0,\, J^{-1}(\theta_0)\big).$$

This single fact licenses everything that follows: the MLE, rescaled by $\sqrt n$, looks like a mean-zero normal
with covariance the inverse Fisher information — the same object that lower-bounds the variance of any unbiased
estimator (the Cramér–Rao bound), so the MLE is, asymptotically, as concentrated as an estimator can be.

## The Wald statistic and the confidence ellipsoid

Nothing below actually needs $\hat\theta$ to be the MLE — only that it is asymptotically normal. So state the
construction for any estimator $\hat\theta_n$ with $\sqrt n(\hat\theta_n-\theta_0) \xrightarrow{d} N(0, J^{-1}(\theta_0))$,
and specialize to the MLE afterward.

Standardizing, $\sqrt{n}\,J^{1/2}(\theta_0)(\hat\theta_n-\theta_0) \sim N_d(0,I_d)$, so the squared norm is a sum
of $d$ squared standard normals:

$$n(\hat\theta_n-\theta_0)^T J(\theta_0)(\hat\theta_n-\theta_0) \xrightarrow{d} \chi^2_d.$$

(The convergence itself is Slutsky's theorem, applied to the map taking a vector to its quadratic form.) This
gives an immediate test of $H_0:\theta=\theta_0$ against $H_1:\theta\neq\theta_0$: reject when the statistic
exceeds $\chi^2_{d,1-\alpha}$, the upper-$\alpha$ quantile. By construction,

$$\mathbb P_{\theta_0}\Big(n(\hat\theta_n-\theta_0)^T J(\theta_0)(\hat\theta_n-\theta_0) \le \chi^2_{d,1-\alpha}\Big) \to 1-\alpha.$$

The step worth pausing on is what happens when the roles of $\theta_0$ and $\theta$ swap. The event above says:
the data fail to reject $\theta_0$ iff $\theta_0$ lies in the set $\{\theta : n(\hat\theta_n-\theta)^T J(\theta)(\hat\theta_n-\theta)
\le \chi^2_{d,1-\alpha}\}$. Read as a statement about $\theta_0$, this set — built from the data alone, containing
no unknowns — is a confidence region: it covers the true parameter with probability tending to $1-\alpha$,
whatever $\theta_0$ actually is. Testing every possible $\theta_0$ and collecting the ones not rejected *is* the
confidence region; there is no separate argument needed for the region beyond the test.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A confidence ellipsoid around the estimator, containing one candidate value of theta and excluding another">
  <line x1="20" y1="200" x2="300" y2="200" stroke="currentColor" stroke-width="1"/>
  <text x="300" y="215" text-anchor="end" font-size="11" fill="currentColor">θ₁</text>
  <line x1="20" y1="200" x2="20" y2="10" stroke="currentColor" stroke-width="1"/>
  <text x="10" y="18" text-anchor="start" font-size="11" fill="currentColor">θ₂</text>
  <ellipse cx="170" cy="110" rx="90" ry="55" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="170" cy="110" r="3" fill="currentColor"/>
  <text x="170" y="98" text-anchor="middle" font-size="12" fill="currentColor">θ̂ₙ</text>
  <circle cx="140" cy="130" r="3" fill="currentColor"/>
  <text x="105" y="152" text-anchor="middle" font-size="12" fill="currentColor">θ₀ (not rejected)</text>
  <circle cx="268" cy="48" r="3" fill="currentColor"/>
  <text x="268" y="34" text-anchor="middle" font-size="12" fill="currentColor">θ₀′ (rejected)</text>
</svg>
<figcaption>The Wald confidence ellipsoid, centered at the estimator. A candidate value is not rejected exactly
when it falls inside the ellipsoid — the test and the confidence region are the same picture, read two ways.</figcaption>
</figure>

More data shrinks the ellipsoid: its volume scales like $n^{-d/2}$, i.e. each axis shrinks like $1/\sqrt n$,
matching the $\sqrt n$ rate in the CLT for $\hat\theta_n$.

## Estimating $J(\theta)$

The construction above still has an unknown in it — $J(\theta_0)$ — sitting inside a set that is supposed to be
computable from data alone. Two data-driven estimators are standard:

1. **Observed information.** Plug the MLE into (minus) the empirical Hessian:
   $$J_n(\hat\theta_n) = -\frac1n \nabla^2\ell_n(\hat\theta_n;X).$$
2. **Estimated expected information.** Use $\operatorname{Var}_\theta[\nabla\ell_n(\theta;X)] = n\operatorname{Var}_\theta[\nabla\ell_\theta(X)]
   = nJ(\theta)$, and estimate the per-observation variance by its sample analogue:
   $$\hat J_n(\theta) = \frac1n\sum_{i=1}^n \nabla\ell_\theta(X_i)\nabla\ell_\theta(X_i)^T.$$

A third option, when $J(\theta)$ has a closed form (as in an exponential family), is to plug $\hat\theta_n$
directly into the model's own Fisher-information formula, $\hat J_n = \mathbb E_{\hat\theta_n}[-\nabla^2\ell_{\hat\theta_n}(X)]$.

Both (1) and (2) converge in probability to $J(\theta_0)$ in the iid setting, and both continue to make sense
outside it (e.g. independent-but-not-identical data, as in the GLM example below). Heuristically, the plug-in
expected information (2) measures how much information a *typical* data set of this size carries about $\theta$,
while the observed information (1) measures how much information *this* data set happens to carry — the
curvature of the likelihood actually realized.

## The Wald interval for a single coordinate

Since $\sqrt n(\hat\theta_n - \theta_0) \sim N_d(0, J^{-1}(\theta_0))$, marginally
$\hat\theta_{n,j} \stackrel{\cdot}{\sim} N(\theta_{0,j}, [J^{-1}(\theta_0)]_{jj}/n)$. Writing the standard error as
$\text{s.e.}(\hat\theta_{n,j}) = \sqrt{[J_n^{-1}(\hat\theta_n)]_{jj}/n}$, the usual interval follows:

$$C_j = \big[\hat\theta_{n,j} \pm z_{1-\alpha/2}\cdot \text{s.e.}(\hat\theta_{n,j})\big].$$

This is exactly what `glm` in R reports, using the observed-information estimate $\hat J_n = J_n(\hat\theta_n)$.
The matching multivariate confidence ellipsoid for $\theta_0$ is
$\{\theta : n(\hat\theta_n-\theta)^T \hat J_n(\hat\theta_n)(\hat\theta_n-\theta) \le \chi^2_{d,1-\alpha}\}$.

None of this used maximum likelihood specifically. Whenever $\sqrt n(\hat\theta_n-\theta_0) \xrightarrow{d}
N(0,\Sigma(\theta_0))$ for *some* covariance $\Sigma$, and $\hat\Sigma_n(\theta) \xrightarrow{p} \Sigma(\theta_0)$
for some estimator of it, the same intervals and ellipsoids go through with $\Sigma$ in place of $J^{-1}$.

## Worked example: generalized linear model with fixed design

Take $X_1,\ldots,X_n\in\mathbb R^d$ fixed (not random), and $Y_i\mid X_i \sim p_{\eta_i}$ independently, with the
canonical link $\eta_i = \beta^T X_i$ and $\mu_i(\beta) = \mathbb E_\beta[Y_i] = \psi'(\eta_i)$ for the
exponential-family cumulant function $\psi$. (More generally, $\eta_i = f(\beta^TX_i)$ for monotone $f$.)
Logistic regression ($Y_i\sim\text{Bernoulli}(e^{\eta_i}/(1+e^{\eta_i}))$) and Poisson log-linear regression
($Y_i\sim\text{Poisson}(e^{\eta_i})$) are the two standard cases.

The log-likelihood, score, and Hessian are

$$\ell_n(\beta;Y) = \sum_i\big[Y_i\eta_i - \psi(\eta_i) + \log h(Y_i)\big], \qquad
\nabla\ell_n(\beta;Y) = \sum_i (Y_i-\mu_i(\beta))X_i,$$
$$\nabla^2\ell_n(\beta;Y) = -\sum_i \psi''(\eta_i)X_iX_i^T,$$

using $\operatorname{Var}_\beta(Y_i) = \psi''(\eta_i)$ (non-random, since $X_i$ is fixed). Under regularity
conditions on the design $\{X_i\}$, Taylor-expanding $\ell_n$ exactly as above gives
$\sqrt n(\hat\beta_n-\beta) \xrightarrow{d} N(0, J^{-1})$, and the finite-sample approximation
$\hat\beta \stackrel{\cdot}{\sim} N(\beta, J_n^{-1}(\beta))$ is what `glm` reports coefficient standard errors from.

## Weighing the Wald construction

**In its favor:** the region is easy to invert into simple, closed-form intervals, and it is asymptotically
correct under the stated regularity conditions.

**Against it:**

1. It needs the MLE — an optimization problem that may not have a closed form.
2. It depends on the parameterization: the same hypothesis, tested on a reparameterized $\theta$, generally gives
   a different Wald statistic, because the quadratic approximation to $\ell_n$ is not preserved under a nonlinear
   change of coordinates.
3. It relies on two separate approximations at once — that the score is normal, and that the log-likelihood is
   well approximated by a quadratic near $\theta_0$ — and both can fail well before the sample size that
   guarantees normality of $\hat\theta_n$ alone.
4. It needs the MLE to actually be consistent, which requires regularity conditions on $\mathcal P$.
5. The resulting interval or ellipsoid is centered at $\hat\theta_n$ and can extend outside the parameter space
   $\Theta$ even when $\hat\theta_n$ itself is a sensible estimate.

## An alternative that never computes $\hat\theta$: the score test

Item 1 above is avoidable. The two approximations underlying the Wald test are: (i) the score at $\theta_0$ is
normal, and (ii) the log-likelihood is quadratic enough that Taylor-expanding the score locates $\hat\theta$
accurately. Approximation (i) alone is already enough to build a test — the quadratic approximation, and the MLE
itself, can be dropped entirely.

Directly from $\nabla\ell_n(\theta_0;X) \sim N(0, nJ(\theta_0))$, i.e.
$J_n^{-1/2}(\theta_0)\nabla\ell_n(\theta_0;X) \stackrel{\cdot}{\sim} N_d(0,I_d)$, reject $H_0:\theta=\theta_0$ when

$$\nabla\ell_n(\theta_0;X)^T \hat J_n^{-1}(\theta_0)\, \nabla\ell_n(\theta_0;X) > \chi^2_{d,1-\alpha},$$

the left side converging to $\chi^2_d$ under $H_0$. One-sided versions are available too, since the
un-squared standardized score is itself asymptotically standard normal.

A few remarks:

- No quadratic approximation to $\ell_n$ is used, and no MLE needs to be computed to evaluate the statistic —
  only the score and an estimate of $J$ at the single hypothesized value $\theta_0$.
- The construction extends to models with nuisance parameters (testing one coordinate while others are free),
  typically by evaluating the score at the MLE restricted to the null set $\Theta_0$.

## The score test does not depend on parameterization

This directly answers disadvantage 2 of the Wald test. Suppose $\eta = g(\theta)$ is a smooth reparameterization,
$\Psi = g(\Theta)$, and $q_\eta(x) = p_{g^{-1}(\eta)}(x)$, so $\ell_\eta(x) = \ell_{g^{-1}(\eta)}(x)$. By the chain
rule,

$$\nabla_\eta \ell_\eta(x) = \nabla_\theta\ell_\theta(x)\cdot \nabla g^{-1}(\eta), \qquad
J_\eta(\eta) = \nabla g^{-1}(\eta)^T J_\theta(g^{-1}(\eta))\,\nabla g^{-1}(\eta),$$

(using $\theta = g^{-1}(\eta)$). The Jacobian factors introduced in the score exactly cancel those introduced in
$J$, so the quadratic form is unchanged:

$$\nabla_\eta\ell_\eta(x)^T J_\eta^{-1}(\eta)\,\nabla_\eta\ell_\eta(x) = \nabla_\theta\ell_\theta(x)^T J_\theta^{-1}(\theta)\,\nabla_\theta\ell_\theta(x)$$

whenever $\eta_0 = g(\theta_0)$. Testing $H_0:\theta=\theta_0$ in the $\theta$-coordinates gives literally the
same statistic as testing $H_0:\eta=\eta_0$ in the $\eta$-coordinates — a guarantee the Wald statistic does not
carry, precisely because it is built from $\hat\theta_n - \theta_0$ directly rather than from the score.

## Score test examples

**One-parameter exponential family.** For $X_1,\ldots,X_n\stackrel{\text{iid}}{\sim} e^{\eta T(x)-A(\eta)}h(x)$,
$\nabla\ell_n(\eta;X) = \sum T(X_i) - n\mu(\eta)$ and $\ell_n''(\eta;X) = -n\operatorname{Var}_\eta[T(X)]$, with
$\hat\eta_n = A'^{-1}(\bar T)$. The score test statistic at $\eta_0$ reduces to the familiar standardized sum

$$\frac{\sum_i T(X_i) - n\mu(\eta_0)}{\sqrt{n\operatorname{Var}_{\eta_0}[T(X)]}} \stackrel{\cdot}{\sim} N(0,1).$$

**Laplace location: the sign test.** For $X_1,\ldots,X_n\stackrel{\text{iid}}{\sim}\text{Laplace}(\theta,2\sqrt2)$,
testing $H_0:\theta=0$ against $H_1:\theta\neq0$, $\ell_n(\theta;X) = \sum|X_i-\theta| - n\log(4\sqrt2)$, so

$$\nabla\ell_n(0;X) = \sum_i \big[\mathbb I(X_i<0)-\mathbb I(X_i>0)\big] = \sum_i \text{sgn}(-X_i), \qquad J_n(0) = n/2,$$

giving the score statistic $\sqrt{2/n}\sum_i\text{sgn}(-X_i) \stackrel{\cdot}{\sim} N(0,1)$ — the classical sign
test. It is not a coincidence that this matches a familiar test: this one-sided score test is exactly the
Neyman–Pearson optimal test of $H_0:\theta=0$ against the *specific nearby* alternative $|\theta|=\epsilon$ as
$\epsilon\to0$. The reason is a local expansion of the model near the null,
$p_\theta(x) \approx p_0(x)\big[1+\epsilon\,\ell_0'(x)\big]$ for small $\epsilon$: the likelihood ratio for a
nearby alternative is, to first order, an affine function of the score, so the Neyman–Pearson test — reject for
large likelihood ratio — becomes reject for large score. That is the general reason a one-sided score test is
(almost) uniformly most powerful against alternatives close to $\theta_0$, even though it may not be optimal, or
even sensible, far from $\theta_0$.

**Pearson's $\chi^2$ goodness-of-fit test.** For $N=(N_1,\ldots,N_d)\sim\text{Multinomial}(n,\pi)$ with
$\pi_i\ge0$, $\sum\pi_i=1$, the log-likelihood $\ell_n(\pi;N) = \sum_i N_i\log\pi_i$ is a full-rank $(d-1)$-parameter
exponential family (e.g. $T_j = \mathbb I(\text{category}=j)$, $j=1,\ldots,d-1$, with $\pi_d = 1-\sum_{j<d}\pi_j$),
with score $\nabla\ell_n(\pi;N) = (N_1/\pi_1,\ldots,N_d/\pi_d)^T - n\mathbf 1_d$ and MLE
$\hat\pi = (N_1/n,\ldots,N_d/n)$. The notes break off here, right before writing down $J_n(\pi)$ explicitly —
finishing that computation and forming the score statistic is exactly the classical route to Pearson's statistic,
which is presumably why the section carries that name, but the algebra itself is not present in the source.

## Sources

- Berkeley STAT 210A reader, "Likelihood-Based Inference" — the setting, asymptotic normality of the MLE,
  Wald-type confidence regions, the GLM example, and the advantages/disadvantages list — converted identically
  across three offerings:
  [fall-2024](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/likelihood-inference.qmd),
  [fall-2025](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/likelihood-inference.html),
  [fall-2026](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/likelihood-inference.qmd)
  (CC BY 4.0). The three copies are identical in content; this chapter follows the fall-2026 rendering.
- The score test, its invariance under reparameterization, and the three worked examples (one-parameter
  exponential family, the Laplace/sign test, Pearson's $\chi^2$) come from the "Score Test" section of the same
  reader, same three offerings.
- The reader's own Pearson's-$\chi^2$ derivation is incomplete in all three converted copies: it stops mid-expression
  while writing the Fisher information matrix $J_n(\pi)$, before the score statistic is formed. That gap is
  preserved here rather than filled in.
- Referred to but not contained in the supplied material: the generalized likelihood ratio test. The fall-2025
  reader's own page title, "Likelihood-Based Inference: Wald, Score, and Generalized Likelihood Ratio Tests",
  indicates this followed directly in the actual lecture but is outside the sections supplied for this chapter.

---

[← 63. Multiple Testing and FWER](63-multiple-testing-and-fwer.md) · [Contents](index.md) · [65. Maximum Likelihood Estimation →](65-maximum-likelihood-estimation.md)
