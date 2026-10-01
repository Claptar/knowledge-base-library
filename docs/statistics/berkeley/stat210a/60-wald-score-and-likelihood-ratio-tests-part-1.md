---
title: "60. Wald, Score, and Likelihood-Ratio Tests (part 1)"
course: "Berkeley Stat 210A"
chapter: 60
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 60. Wald, Score, and Likelihood-Ratio Tests (part 1)

## What this covers

This chapter builds the three tests that fall out of maximizing a log-likelihood in large
samples — the **Wald test**, the **score test**, and the **generalized likelihood ratio test**
(GLRT) — and shows that all three are, to leading order, the same test computed three different
ways, so the choice between them is a matter of what is easy to compute rather than of power. It
closes with **asymptotic relative efficiency (ARE)**, a way to compare two consistent,
asymptotically normal estimators of the same parameter by how much data one would have to throw
away to make the worse one behave like the better one. It assumes the asymptotic normality of the
MLE (from the score CLT plus a Taylor expansion of the likelihood equation, recapped below) and
basic exponential-family notation: natural parameter, log-partition function $A$, and the facts
$\dot A(\eta) = \mathbb{E}_\eta Y$, $\ddot A(\eta) = \operatorname{Var}_\eta(Y)$.

## Asymptotic normality of the MLE, recapped

Setting: $X_1, \ldots, X_n \overset{\text{iid}}{\sim} p_\theta(x)$ with $p_\theta$ smooth in
$\theta \in \Theta$. Assume the score has mean zero, $\mathbb{E}_\theta \nabla\ell(\theta;X_i) = 0$,
and define the (per-observation) **Fisher information**

$$\operatorname{Var}_\theta[\nabla \ell(\theta; X_i)] = -\mathbb{E}_\theta \nabla^2 \ell(\theta; X_i) = J_1(\theta) \succ 0,$$

the two expressions agreeing by the usual information identity. Assume also that the MLE is
consistent, $\hat\theta_{\text{MLE}} \xrightarrow{P_\theta} \theta$. Then at the true value
$\theta_0$, the CLT and LLN applied to the score and Hessian give

$$\frac{1}{\sqrt{n}} \nabla \ell_n(\theta_0; X) \Rightarrow N_d(0, J_1(\theta_0)), \qquad \frac{1}{n} \nabla^2 \ell_n(\theta_0; X) \xrightarrow{P} -J_1(\theta_0).$$

The MLE solves the score equation $0 = \nabla\ell_n(\hat\theta_n)$; Taylor-expanding this around
$\theta_0$,

$$0 = \nabla \ell(\hat{\theta}_n) \approx \nabla \ell_n(\theta_0) + \nabla^2 \ell_n(\theta_0)(\hat{\theta}_n - \theta_0),$$

and solving for $\hat\theta_n - \theta_0$ turns the two limits above into

$$\sqrt{n}(\hat{\theta}_n - \theta_0) \Rightarrow N_d\big(0, J_1(\theta_0)^{-1}\big).$$

This is the single fact the rest of the chapter is built on: it says how the MLE fluctuates around
the truth, and everything below is a way of turning that fluctuation into a test or a confidence
region.

## The Wald test and confidence ellipsoids

Write $J_n(\theta) = n J_1(\theta)$ for the information in the full sample. Suppose $\hat J_n \succ
0$ is an estimator with $\frac{1}{n}\hat J_n \xrightarrow{P} J_1(\theta_0)$. Starting from
$\sqrt n(\hat\theta_n-\theta_0)\Rightarrow N_d(0,J_1(\theta_0)^{-1})$, multiplying by
$J_1(\theta_0)^{1/2}$ standardizes it to $N_d(0,I_d)$, and Slutsky's theorem lets the estimated
$\hat J_n$ stand in for the unknown $J_1(\theta_0)$:

$$\hat{J}_n^{1/2} (\hat{\theta}_n - \theta_0) \Rightarrow N_d(0, I_d).$$

Squaring the norm gives a test of $H_0:\theta=\theta_0$ that rejects for large values of

$$\|\hat{J}_n^{1/2} (\hat{\theta}_n - \theta_0)\|^2 \Rightarrow \chi_d^2,$$

so that $\mathbb{P}_{\theta_0}\big(\|\hat J_n^{1/2}(\hat\theta_n-\theta_0)\|^2 \ge \chi_d^2(\alpha)\big)
\to \alpha$, where $\chi_d^2(\alpha)$ is the $1-\alpha$ quantile of $\chi_d^2$. This is the **Wald
test**.

Inverting the test gives a confidence region for free: rejecting $\theta_0$ is exactly the same
event as $\theta_0$ falling outside a specific set around $\hat\theta_n$,

$$\|\hat{J}_n^{1/2}(\hat{\theta}_n - \theta_0)\|^2 > \chi_d^2(\alpha) \iff \theta_0 \notin \underbrace{\hat{\theta}_n + \hat{J}_n^{-1/2} B_{\chi_d^2(\alpha)}(0)}_{\text{confidence ellipsoid}},$$

where $B_r(0)$ is the ball of radius $\sqrt r$. So the set of $\theta_0$ *not* rejected by the Wald
test at level $\alpha$ is, asymptotically, a valid $(1-\alpha)$-confidence ellipsoid centered at
$\hat\theta_n$. Since $\hat J_n$ grows like $n$, its shape is fixed but its size shrinks like
$1/\sqrt n$: more information means a smaller ellipse.

## Choosing $\hat J_n$: plug-in versus observed information

Two natural estimators of $J_n(\theta_0)$:

1. **Plug in the MLE** into the (expected) information function:
   $$\hat{J}_n = J_n(\hat{\theta}_n) = \operatorname{Var}_\theta(\nabla \ell_n(\theta; X))\Big|_{\theta = \hat{\theta}_n} = -\mathbb{E}_\theta \nabla^2 \ell_n(\theta)\Big|_{\theta = \hat{\theta}_n}.$$
   Note this is *not* the same object as $\operatorname{Var}_{\hat\theta_n}\!\big(\nabla\ell_n(\hat\theta_n(X);X)\big)$, which is identically $0$ because $\hat\theta_n$ is chosen to zero out the score.
2. **Observed Fisher information**: skip the expectation and use the Hessian at the data actually
   observed,
   $$\hat{J}_n = -\nabla^2 \ell_n(\hat{\theta}_n; X).$$

Both satisfy $\frac1n \hat J_n \xrightarrow{P} J_1(\theta_0)$ in a "nice" iid setting, and both make
sense even outside the iid setting (where $J_n(\theta)$ has no simpler closed form). Heuristically,
the plug-in version measures the information about $\theta$ in a *typical* data set generated at
$\hat\theta_n$, while the observed information measures the information about $\theta$ actually
present in *this* data set.

## Wald intervals for one coordinate or a subset

If $\hat\theta_n \approx N_d(\theta_0, J_n(\theta_0)^{-1})$ then each coordinate is marginally
normal, $\hat\theta_{n,j} \approx N_1\big(\theta_{0,j}, (J_n(\theta_0)^{-1})_{jj}\big)$, which gives
the familiar univariate interval

$$C_j = \hat{\theta}_{n,j} \pm \widehat{\text{s.e.}}(\hat{\theta}_{n,j}) \cdot z_{\alpha/2} = \hat{\theta}_{n,j} \pm \sqrt{(\hat{J}_n^{-1})_{jj}} \cdot z_{\alpha/2},$$

with $\widehat{\text{s.e.}}(\hat\theta_{n,j})^2 = (\hat J_n^{-1})_{jj}$. This is exactly what the
`glm` function in R reports, using $\hat J_n = -\nabla^2\ell(\hat\theta_n)$ (observed information).

The same idea extends to a subset $S$ of coordinates, $|S|=k$: $\hat\theta_{n,S} \approx
N_k\big(\theta_{0,S}, (J_n(\theta_0)^{-1})_{SS}\big)$ gives the confidence ellipsoid

$$C_S = \hat{\theta}_{n,S} + \big((\hat{J}_n^{-1})_{SS}\big)^{1/2} B_{\chi_k^2(\alpha)}(0).$$

None of this needs $\hat\theta_n$ to be the MLE specifically: whenever $\sqrt n(\hat\theta_n -
\theta_0) \Rightarrow N(0,\Sigma(\theta_0))$ for some other asymptotically normal estimator, and
$\frac1n \hat\Sigma_n \xrightarrow{P_{\theta_0}} \Sigma(\theta_0)$, the same Wald construction goes
through with $\Sigma$ in place of $J_1^{-1}$.

## Worked example: a generalized linear model with fixed design

Take covariates $x_1,\ldots,x_n \in \mathbb{R}^d$ fixed and responses drawn independently from a
canonical one-parameter exponential family,

$$Y_i \overset{\text{ind.}}{\sim} p_{\eta_i}(y) = e^{\eta_i y - A(\eta_i)} h(y), \qquad \eta_i = \beta' x_i,$$

so $\eta_i$ (the natural parameter) is a linear function of $x_i$ — the canonical link. (More
generally a link function $f$ enters through $f(\mu_i) = \beta'x_i$, but the canonical case
$\eta_i=\beta'x_i$ is what makes the computation below clean.) Writing $\mu_i(\beta) =
\mathbb{E}_\beta Y_i = \dot A(\eta_i(\beta))$, the two standard instances are logistic regression,
$Y_i \sim \operatorname{Bern}\!\big(e^{x_i'\beta}/(1+e^{x_i'\beta})\big)$, and Poisson log-linear
regression, $Y_i \sim \operatorname{Pois}(e^{x_i'\beta})$.

The log-likelihood, score, and (negative) Hessian are

$$\ell_n(\beta;Y) = \sum_i (x_i'\beta) y_i - A(x_i'\beta) - \log h(y_i),$$
$$\nabla \ell_n(\beta;Y) = \sum_i \big(y_i - \dot A(x_i'\beta)\big)x_i = \sum_i (y_i - \mu_i(\beta)) x_i,$$
$$-\nabla^2 \ell_n(\beta;Y) = \sum_i \ddot A(x_i'\beta)\, x_ix_i' = \sum_i \operatorname{Var}_\beta(y_i)\, x_ix_i'.$$

The last expression depends on $\beta$ but not on the data $y$ — it is not random — and it equals
$\operatorname{Var}_\beta(\nabla\ell_n(\beta;Y))$ exactly. So for a canonical GLM the observed and
expected information coincide: there is only one object to estimate, and standardizing the score
by it,

$$(-\nabla^2 \ell_n(\beta))^{-1/2} \nabla \ell_n(\beta) \sim (0, I_d) \ \text{ in finite samples,}$$

gives something with mean zero and identity covariance for *every* $n$, converging to $N_d(0,I_d)$
under a regularity condition on the design matrix $X$ (with rows $x_i'$) that keeps the CLT
applicable to $\sum_i(y_i-\mu_i)x_i$. A Taylor expansion of $\ell_n$ then gives the same
$\hat J_n^{1/2}(\hat\beta_n-\beta) \Rightarrow N_d(0,I_d)$ as in the general recap.

**Advantages of the Wald test:** easy to invert into simple confidence regions; asymptotically
correct.

**Disadvantages:** it requires computing the MLE; it depends on the parameterization (a
nonlinear reparametrization changes the shape and the coverage properties of the ellipsoid at
finite $n$); it relies on two approximations stacked together — that $\nabla\ell_n$ is
approximately normal and that $\ell_n$ is approximately quadratic; it needs the MLE to be
consistent; and the resulting confidence interval or ellipsoid can extend outside the parameter
space $\Theta$.

## The score test

Test $H_0:\theta=\theta_0$ against $H_1:\theta\neq\theta_0$. The score test bypasses the quadratic
approximation to $\ell_n$ entirely, using only the score CLT at the hypothesized value:

$$J_n(\theta_0)^{-1/2}\nabla \ell_n(\theta_0; X) \xrightarrow{P_{\theta_0}} N_d(0, I_d),$$

so $H_0$ is rejected when

$$\|J_n(\theta_0)^{-1/2} \nabla \ell_n(\theta_0; X)\|_2^2 \ge \chi_d^2(\alpha).$$

In one dimension this is $\dot\ell_n(\theta_0)/\sqrt{J_n(\theta_0)} \Rightarrow N(0,1)$, which also
supports a one-sided test — something the (squared) Wald and GLRT statistics do not naturally give.

Two things the score test buys: no quadratic approximation, and no need to compute the MLE at all.
It also needs no estimate of Fisher information away from $\theta_0$, since $J_n(\theta_0)$ is a
known function of the hypothesized value. It generalizes to problems with nuisance parameters,
typically by evaluating the score at the restricted MLE fit under $\Theta_0$.

## The score test is invariant to reparametrization

Take $d=1$ and reparametrize by $\theta=g(\zeta)$ with $\dot g(\zeta)>0$ everywhere, so $g$ is a
smooth increasing change of variables. Writing $q_\zeta(x)=p_{g(\zeta)}(x)$, the chain rule gives

$$\dot\ell^{(\zeta)}(\zeta;x) = \frac{d}{d\zeta}\log p_{g(\zeta)}(x) = \dot\ell^{(\theta)}(g(\zeta);x)\cdot \dot g(\zeta), \qquad J^{(\zeta)}(\zeta) = J^{(\theta)}(g(\zeta))\cdot \dot g(\zeta)^2.$$

The factor of $\dot g(\zeta)$ appears once in the numerator score and is squared in the
denominator's information, so it cancels exactly in the standardized score:

$$\frac{\dot\ell^{(\zeta)}(\zeta_0;X)}{\sqrt{J^{(\zeta)}(\zeta_0)}} \overset{\text{a.s.}}{=} \frac{\dot\ell^{(\theta)}(\theta_0;X)}{\sqrt{J^{(\theta)}(\theta_0)}}, \qquad \theta_0=g(\zeta_0).$$

So the score test statistic — and hence the test itself — does not depend on which parametrization
$\theta$ or $\zeta$ the likelihood happens to be written in. The Wald test, by contrast, does
depend on the parametrization (item 2 in its disadvantages above): reparametrizing changes
$\hat\theta_n - \theta_0$ nonlinearly and the quadratic approximation is not invariant to that.

## Worked example: an $s$-parameter exponential family

For $X_1,\ldots,X_n \overset{\text{iid}}{\sim} e^{\eta' T(x) - A(\eta)}h(x)$, the score is

$$\nabla \ell(\eta;X) = \sum_i T(X_i) - n\mu(\eta), \qquad \mu(\eta)=\dot A(\eta)=\mathbb{E}_\eta T(X),$$

so the score test of $H_0:\eta=\eta_0$ rejects for large

$$\Big\|J_n(\eta_0)^{-1/2}\Big(\sum_i T(X_i) - n\mu(\eta_0)\Big)\Big\|^2 \Rightarrow \chi_d^2,$$

which in one dimension is just the standardized sufficient statistic,

$$\frac{\sum_i T(X_i) - n\mu(\eta_0)}{\sqrt{n\operatorname{Var}_{\eta_0}(T(X_i))}} \xrightarrow{P_{\eta_0}} N(0,1).$$

The score test in an exponential family is exactly a normalized test on the sufficient statistic —
no maximization is needed to write it down.

## Worked example: the Laplace location family and the sign test

Let $X_1,\ldots,X_n \overset{\text{iid}}{\sim} \operatorname{Laplace}(\theta) = \tfrac12
e^{-|x-\theta|}$, and test $H_0:\theta\le 0$ against $H_1:\theta>0$ (right-tailed). The
log-likelihood and score are

$$\ell_n(\theta;X) = -\sum_{i=1}^n |X_i-\theta| - n\log 2, \qquad \dot\ell_n(\theta;X) = \sum_{i=1}^n \operatorname{sgn}(X_i-\theta),$$

with $\operatorname{sgn}(z)=+1,0,-1$ for $z>0,=0,<0$. At $\theta_0=0$,

$$\dot\ell_n(0;X) = \sum_i \operatorname{sgn}(X_i) = \#\{i:X_i>0\} - \#\{i:X_i<0\} = 2\#\{i:X_i>0\} - n.$$

Under $H_0:\theta=0$, $\#\{i:X_i>0\}\sim\operatorname{Binom}(n,1/2)$, so the score test here *is*
the classical **sign test**.

Two remarks the lecture makes about this example. First, the sign test is approximately the exact
Neyman–Pearson likelihood ratio test of $\theta=0$ against $\theta=\varepsilon$, as
$\varepsilon\downarrow 0$: for small $\varepsilon>0$,

$$\log \frac{p_{\theta_0+\varepsilon}(x)}{p_{\theta_0}(x)} \approx \varepsilon\, \dot\ell_n(\theta_0;X),$$

so the NP-optimal test against a *nearby* alternative rejects for large values of exactly the
score $\dot\ell_n(\theta_0)$. Second, the intuition for why this matters: a one-sided score test
is maximizing power against nearby alternatives, precisely because for alternatives far from
$\theta_0$ (i.e. $\theta \gg 1/\sqrt n$) almost any reasonable test already has power close to $1$,
so there is nothing left to optimize there — the interesting competition between tests is local.
More generally, the one-sided score test is "almost" uniformly most powerful for alternatives near
$\theta_0$.

## Worked example: Pearson's $\chi^2$ goodness-of-fit test

Let $N=(N_1,\ldots,N_d) \sim \operatorname{Multinom}(n,(\pi_1,\ldots,\pi_d))$. Since
$\sum_j\pi_j=1$, the cell counts $(N_2,\ldots,N_d)$ form a full-rank $(d-1)$-parameter exponential
family; one canonical (multiple-logistic) parametrization is

$$\pi_j = \begin{cases} \dfrac{1}{1+\sum_{k>1}e^{\eta_k}} & j=1 \\[4pt] \dfrac{e^{\eta_j}}{1+\sum_{k>1}e^{\eta_k}} & j>1. \end{cases}$$

The score in $\eta=(\eta_2,\ldots,\eta_d)$ is $\nabla\ell(\eta;N) = (N_2,\ldots,N_d) -
n(\pi_2,\ldots,\pi_d)$, with covariance the standard multinomial covariance matrix restricted to
categories $2,\ldots,d$,

$$\operatorname{Var}_\eta(\nabla\ell(\eta)) = n\big(\operatorname{diag}(\pi_{2:d}) - \pi_{2:d}\pi_{2:d}'\big).$$

Inverting this rank-one perturbation of a diagonal matrix (via $(A+uv')^{-1} = A^{-1} -
A^{-1}uv'A^{-1}/(1+v'A^{-1}u)$) gives

$$J_n(\eta)^{-1} = \frac1n\Big(\operatorname{diag}(\pi_{2:d})^{-1} - \pi_1^{-1}\mathbf{1}\mathbf{1}'\Big).$$

Plugging this into the score statistic for $H_0:\pi=\pi_0$ and simplifying — the algebra collapses
the quadratic form onto the diagonal — recovers exactly the classical statistic:

$$\nabla\ell_n(\eta_0)'J_n^{-1}(\eta_0)\nabla\ell_n(\eta_0) = \sum_{j=1}^d \frac{(N_j-n\pi_{0,j})^2}{n\pi_{0,j}} \xrightarrow{P_{\pi_0}} \chi_{d-1}^2.$$

So Pearson's $\chi^2$ goodness-of-fit statistic is nothing but the multinomial score statistic
written out — the algebra that turns the quadratic form into $\sum_j(N_j-n\pi_{0,j})^2/(n\pi_{0,j})$
is exact for every $n$; only the $\chi^2_{d-1}$ limit is asymptotic, and the $d-1$ degrees of
freedom match the dimension of the exponential family exactly.

## The generalized likelihood ratio test

**Simple null.** For $H_0:\theta=\theta_0$ vs $H_1:\theta\neq\theta_0$, Taylor-expand the
log-likelihood around the unrestricted MLE $\hat\theta_n$ rather than around $\theta_0$. The
first-order term vanishes because $\hat\theta_n$ zeroes the score:

$$\ell_n(\theta_0) - \ell_n(\hat{\theta}_n) = \underbrace{\nabla \ell(\hat{\theta}_n)}_{=\,0} \cdot(\theta_0-\hat\theta_n)+ \frac{1}{2}(\theta_0 - \hat{\theta}_n)' \nabla^2 \ell_n(\tilde{\theta}_n)(\theta_0 - \hat{\theta}_n)$$

for some $\tilde\theta_n$ between $\theta_0$ and $\hat\theta_n$. Regrouping the quadratic form as a
squared norm,

$$\ell_n(\theta_0)-\ell_n(\hat\theta_n) = -\frac12 \Big\| \underbrace{\Big(-\tfrac1n\nabla^2\ell_n(\tilde\theta_n)\Big)^{1/2}}_{\xrightarrow{P} J_1(\theta_0)^{1/2}} \underbrace{\sqrt n(\theta_0-\hat\theta_n)}_{\Rightarrow\, N(0,J_1(\theta_0)^{-1})} \Big\|_2^2 \Rightarrow -\frac12 \chi_d^2,$$

so the **generalized likelihood ratio statistic**

$$2\big(\ell_n(\hat{\theta}_n; X) - \ell_n(\theta_0; X)\big) \xrightarrow{P_{\theta_0}} \chi_d^2.$$

## Composite versus composite: the projection picture

More generally test $H_0:\theta\in\Theta_0$ against $H_1:\theta\in\Theta\setminus\Theta_0$, where
$\Theta=\mathbb{R}^d$ and $\Theta_0$ is a $d_0$-dimensional manifold, $\theta_0 \in
\operatorname{relint}(\Theta_0)$, $\hat\theta_n \xrightarrow{P_{\theta_0}} \theta_0$, and the
likelihood is smooth. Let $\hat\theta_0 = \arg\max_{\theta\in\Theta_0} \ell_n(\theta;X)$ be the MLE
restricted to $\Theta_0$. Then

$$2\big(\ell_n(\hat{\theta}_n) - \ell_n(\hat{\theta}_0)\big) \Rightarrow \chi_{d-d_0}^2.$$

**Why the degrees of freedom drop to $d-d_0$.** Reparametrize so that (locally, near $\theta_0$)
$\theta_0=0$ and $J_1(0)=I_d$. Then $\hat\theta_n \approx N_d(\theta_0, \tfrac1n I_d)$, and locally
$\nabla^2\ell_n(\theta) \approx -nI_d$, so the log-likelihood is locally a paraboloid,

$$\ell_n(\theta) - \ell_n(\hat\theta_n) \approx -\frac{n}{2}\|\theta-\hat\theta_n\|^2.$$

Maximizing over $\theta \in \Theta_0$ is then the same, to this approximation, as *minimizing
Euclidean distance* to $\hat\theta_n$ over $\Theta_0$ — i.e. $\hat\theta_0$ is (approximately) the
projection of $\hat\theta_n$ onto $\Theta_0$:

$$\hat\theta_0 \approx \operatorname*{arg\,min}_{\theta\in\Theta_0}\|\theta-\hat\theta_n\| = \operatorname{Proj}_{\Theta_0}(\hat\theta_n).$$

Substituting back,

$$2\big(\ell_n(\hat\theta_n)-\ell_n(\hat\theta_0)\big) \approx n\|\hat\theta_n - \operatorname{Proj}_{\Theta_0}(\hat\theta_n)\|^2 = n\big\|\operatorname{Proj}^{\perp}_{\Theta_0}(\hat\theta_n)\big\|^2 \Rightarrow \chi^2_{d-d_0}.$$

The quantity being squared is the component of $\hat\theta_n$ that lives in the $(d-d_0)$-dimensional
subspace orthogonal to $\Theta_0$ — that subspace has exactly $d-d_0$ dimensions, which is where the
degrees of freedom of the limiting $\chi^2$ come from.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="The restricted MLE as the projection of the unrestricted MLE onto the null-hypothesis manifold, with the orthogonal residual driving the GLRT statistic">
  <line x1="30" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="180" text-anchor="end" font-size="12" fill="currentColor">Θ₀ (dim d₀)</text>

  <circle cx="150" cy="160" r="3" fill="currentColor"/>
  <text x="150" y="178" text-anchor="middle" font-size="12" fill="currentColor">θ₀</text>

  <circle cx="230" cy="55" r="3" fill="currentColor"/>
  <text x="240" y="50" font-size="12" fill="currentColor">θ̂ₙ</text>

  <line x1="230" y1="55" x2="230" y2="160" stroke="currentColor" stroke-width="1.2" stroke-dasharray="4 3"/>
  <polyline points="220,160 220,150 230,150" fill="none" stroke="currentColor" stroke-width="1"/>

  <circle cx="230" cy="160" r="3" fill="currentColor"/>
  <text x="230" y="178" text-anchor="middle" font-size="12" fill="currentColor">θ̂₀ = Proj_Θ₀(θ̂ₙ)</text>

  <text x="245" y="105" font-size="12" fill="currentColor">Proj⊥_Θ₀(θ̂ₙ)</text>
</svg>
<figcaption>The restricted MLE θ̂₀ is the point of Θ₀ closest to the unrestricted MLE θ̂ₙ. The GLRT
statistic is, asymptotically, n times the squared length of the segment removed by that
projection, and its d − d₀ degrees of freedom count the dimensions of the space orthogonal to
Θ₀ that the projection removes.</figcaption>
</figure>

## Wald, score, and GLRT are asymptotically the same test

All three statistics come from the same local quadratic picture of $\ell_n$ around $\theta_0$ (take
$d=1$ for the picture):

$$\ell_n(\theta) - \ell_n(\theta_0) \approx \dot\ell_n(\theta_0)(\theta-\theta_0) + \frac12 J_n(\theta_0)(\theta-\theta_0)^2.$$

Reading off each statistic from this one expansion:

- **GLRT**: $\ell_n(\hat\theta_n)-\ell_n(\theta_0) \approx \tfrac12 J_n^{-1}\dot\ell_n(\theta_0)^2$ (maximize the quadratic in $\theta$)
- **Wald**: $\hat\theta_n-\theta_0 \approx J_n^{-1}\dot\ell_n(\theta_0)$ (the maximizer itself)
- **Score**: $\dot\ell_n(\theta_0)$ (the slope of $\ell_n$ at $\theta_0$)

so that for large $n$,

$$\underbrace{\ell_n(\hat\theta_n)-\ell_n(\theta_0)}_{\text{GLRT}} \approx \big\|J_n(\theta_0)^{1/2}(\hat\theta_n-\theta_0)\big\|^2 \approx \underbrace{\big\|J_n(\theta_0)^{-1/2}\nabla\ell_n(\theta_0)\big\|^2}_{\text{score}} \approx \underbrace{\big\|\hat J_n^{1/2}(\hat\theta_n-\theta_0)\big\|^2}_{\text{Wald}}.$$

All three converge to the same $\chi^2_d$ limit under $H_0$, because they are the same quadratic
form written in terms of the slope, the maximizer, or the height of one parabola. What
distinguishes them in practice is not power but what each needs to compute: the score test needs
no MLE and no information estimate away from $\theta_0$; the Wald test needs the MLE and an
estimate of $J_n$ but inverts easily into a confidence region; the GLRT needs both the unrestricted
and restricted MLEs but is invariant to reparametrization, unlike Wald.

## Asymptotic relative efficiency

Suppose $\hat\theta_n^{(1)}, \hat\theta_n^{(2)}$ are two asymptotically normal estimators of the
same $\theta_0\in\mathbb{R}$,

$$\sqrt n\big(\hat\theta_n^{(i)}-\theta_0\big) \Rightarrow N(0,\sigma_i^2), \qquad i=1,2.$$

The **asymptotic relative efficiency (ARE)** of $\hat\theta^{(2)}$ with respect to $\hat\theta^{(1)}$
is $\sigma_1^2/\sigma_2^2$. For example, if $\sigma_2^2=2\sigma_1^2$, then $\hat\theta^{(2)}$ is
$50\%$ as efficient as $\hat\theta^{(1)}$.

**Interpretation.** Suppose $\sigma_1^2/\sigma_2^2 = \gamma \in (0,1)$. Then for large $n$,

$$\hat\theta^{(1)}_{\lfloor \gamma n\rfloor}(X_1,\ldots,X_{\lfloor \gamma n\rfloor}) \overset{D}{\approx} \hat\theta^{(2)}_n(X_1,\ldots,X_n) \approx N\Big(\theta,\frac{\sigma_2^2}{n}\Big).$$

So using the less efficient estimator $\hat\theta^{(2)}$ on the full sample of size $n$ is, in
distribution, like throwing away $100(1-\gamma)\%$ of the data and then using the more efficient
$\hat\theta^{(1)}$ on what is left. ARE turns a ratio of asymptotic variances into a concrete
statement about wasted data.

## Sources

All content is from a single handwritten lecture, Stat 210A (Berkeley, Fall 2024 offering),
lecture 23, dated on the page 11/16/2023: the outline
(`fall-2024/handwritten/lecture23-F24/01-outline.md`, covering Wald-type inference: the recap of
MLE asymptotic normality, the Wald test, confidence ellipsoids, choice of $\hat J_n$, and Wald
intervals for coordinates/subsets); the GLM and score-test file
(`.../02-ex-generalized-linear-model-with-fixed.md`, covering the fixed-design GLM example, the
Wald test's advantages/disadvantages, the score test, its reparametrization invariance, the
$s$-parameter exponential family example, and the Laplace/sign-test example); and the Pearson/GLRT
file (`.../03-ex-pearson-s-test-goodness-of-fit.md`, covering the Pearson $\chi^2$ example, the
simple and composite GLRT, the asymptotic equivalence of the three tests, and ARE).

These notes are a **model reconstruction of a handwritten PDF with no text layer** (conversion
metadata: `route: llm`, `fidelity: reconstructed`); the source markdown itself warns that "every
equation is unverified." No slides or transcript were supplied for this lecture, and no other
material (textbook, problem set) was referenced by name in the notes beyond a passing mention of
R's `glm` function. The definitions $\dot A(\eta)=\mathbb{E}_\eta Y$ and
$\ddot A(\eta)=\operatorname{Var}_\eta(Y)$ used to explain the GLM score and Hessian are standard
exponential-family identities used implicitly in the source, not separately stated there. The
restricted MLE in the composite-vs-composite result is written here as $\arg\max_{\theta\in\Theta_0}
\ell_n(\theta;X)$ rather than the source's literal "argmin," to match the surrounding argument
(maximizing the likelihood is what "MLE on $\Theta_0$" means, and it is what is actually used a few
lines later) — flagged here since the reconstruction is unverified.

---

[← 59. Asymptotic Distribution of the MLE](59-asymptotic-distribution-of-the-mle.md) · [Contents](index.md) · [61. Wald, Score, and Likelihood-Ratio Tests (part 2) →](61-wald-score-and-likelihood-ratio-tests-part-2.md)
