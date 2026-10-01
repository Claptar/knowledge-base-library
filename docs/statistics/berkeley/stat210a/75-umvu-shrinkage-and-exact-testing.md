---
title: "75. UMVU, Shrinkage, and Exact Testing"
course: "Berkeley Stat 210A"
chapter: 75
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 75. UMVU, Shrinkage, and Exact Testing

## What this covers

This chapter works through a complete final examination from Berkeley's STAT210A (Fall 2020,
Prof. Will Fithian), together with its model solutions, as a review of four pieces of the course's
toolkit in action: exponential-family sufficiency and UMVU estimation together with the asymptotics
and efficiency of competing estimators, decision-theoretic and Bayesian estimation of a mean
constrained to lie in a bounded interval, exact and distribution-free inference in a two-parameter
Gamma model, and maximum likelihood together with a finite-sample pivot in a nonlinear regression
model. It assumes the standard machinery built up earlier in the course: exponential families,
sufficiency and completeness, the Lehmann–Scheffé route to UMVU estimators, Fisher information and
the asymptotic normality of the MLE, the delta method, Bayes estimation and Gibbs sampling, and
classical hypothesis testing (Neyman–Pearson, UMP/UMPU, and the generalized likelihood ratio test).
Each problem is presented as a worked example — problem statement, then the full argument — rather
than as an exercise to solve separately, since the solutions *are* the material being reviewed.

## Problem 1: a two-Poisson exponential family

**Setup.** Observe independent $X \sim \mathrm{Pois}(\theta)$ and $Y \sim \mathrm{Pois}(\theta^2)$
for a single unknown $\theta > 0$ — so the mean of $Y$ is pinned to the *square* of the mean of $X$,
a genuinely one-parameter model even though it looks two-dimensional.

**(a) Exponential family and complete sufficient statistic.** Multiplying the two Poisson
densities,
$$p_\theta(x,y) = \frac{\theta^x e^{-\theta}}{x!}\cdot\frac{\theta^{2y}e^{-\theta^2}}{y!}
= \exp\{(x+2y)\log\theta - \theta - \theta^2\}\,\frac{1}{x!\,y!},$$
which exhibits the model as a one-parameter exponential family with natural parameter
$\eta = \log\theta$, complete sufficient statistic $T = X+2Y$, and carrier density $1/(x!y!)$.
Completeness holds because $\log\theta$ ranges over an open subset of $\mathbb{R}$ (all of it), and
full-rank one-parameter exponential families with an open natural parameter space always have a
complete sufficient statistic for their canonical statistic.

**(b) The UMVU estimator, by Rao–Blackwellization.** Since $\mathbb{E}_\theta X = \theta$, $X$
itself is unbiased for $\theta$; Rao–Blackwellizing it against the complete sufficient statistic
$T=X+2Y$ produces the UMVU estimator
$$\delta(t) = \mathbb{E}[X\mid X+2Y=t] = \left(\sum_{x\in\mathcal P(t)} \frac{x}{x!\left(\frac{t-x}2\right)!}\right)\Bigg/\left(\sum_{x\in\mathcal P(t)}\frac1{x!\left(\frac{t-x}2\right)!}\right),$$
where $\mathcal P(t) = \{x \in \{0,\dots,t\} : t-x \text{ even}\}$ is the set of values $X$ can take
given $X+2Y=t$ (so $Y=(t-x)/2$ is a nonnegative integer), and every factor involving $\theta$
cancels between numerator and denominator because both sides condition on the same value of the
sufficient statistic. If $X=Y=2$, so $T=6$, then
$$\delta(6) = \frac{\frac{0}{0!\,3!}+\frac{2}{2!\,2!}+\frac{4}{4!\,1!}+\frac{6}{6!\,0!}}{\frac1{0!\,3!}+\frac1{2!\,2!}+\frac1{4!\,1!}+\frac1{6!\,0!}} = \frac{486}{331}\approx 1.47.$$

**(c) The MLE from an i.i.d. sample.** With $n$ i.i.d. pairs $(X_i,Y_i)$, the sample is again a
one-parameter exponential family, now with sufficient statistic $T=\sum_i(X_i+2Y_i)$. The MLE sets
the sufficient statistic equal to its expectation, $n(\theta+2\theta^2)$, and solves for $\theta$:
$$2n\hat\theta_n^2 + n\hat\theta_n = T \iff \hat\theta_n = \frac{-1+\sqrt{1+8T/n}}4$$
(the positive root, since $\hat\theta_n>0$). If $\sum_i X_i=\sum_i Y_i=2n$, i.e. $T=6n$, this gives
$\hat\theta_n = 3/2 = 1.50$.

**(d) Asymptotic normality of the MLE.** The per-observation log-likelihood and its derivatives are
$$\ell_1(\theta) = (X+2Y)\log\theta - \theta-\theta^2 - \log(X!Y!), \qquad
\dot\ell_1(\theta) = \frac{X+2Y}\theta - (1+2\theta), \qquad
\ddot\ell_1(\theta) = -\frac{X+2Y}{\theta^2}-2,$$
and the Fisher information, computed either as $\mathrm{Var}_\theta(\dot\ell_1)$ or as
$-\mathbb{E}\ddot\ell_1$ (the two must agree, and checking that they do is a useful consistency
check), is
$$J_1(\theta) = \frac{1+4\theta}{\theta}.$$
The usual MLE asymptotics then give
$$\sqrt n(\hat\theta_n-\theta) \Rightarrow N\!\left(0,\ \frac\theta{1+4\theta}\right).$$

**(e) A naive competitor, and why it loses badly.** Consider
$\tilde\theta_n = (\overline X_n+\overline Y_n^{1/2})/2$. This is a delta-method problem for
$g(x,y)=(x+\sqrt y)/2$, applied to $(\overline X_n,\overline Y_n)$, which by the CLT satisfies
$$\sqrt n\left(\binom{\overline X_n}{\overline Y_n}-\binom\theta{\theta^2}\right)\Rightarrow N_2\!\left(0,\begin{pmatrix}\theta&0\\0&\theta^2\end{pmatrix}\right).$$
Since $\nabla g(\theta,\theta^2) = (1/2,\ 1/(4\theta))$, the delta method gives
$$\sqrt n(\tilde\theta_n-\theta)\Rightarrow N\!\left(0,\ \frac{4\theta+1}{16}\right).$$
The asymptotic relative efficiency of $\tilde\theta_n$ against the MLE is
$$\mathrm{ARE}_\theta = \frac{\theta/(1+4\theta)}{(4\theta+1)/16} = \frac1{\theta+\tfrac12+\tfrac1\theta},$$
which peaks at a mere $40\%$ (at $\theta=1$) and tends to $0$ as $\theta\to0$ or $\theta\to\infty$.
The reason is instructive: as $\theta\to\infty$, $\theta^2\gg\theta$, so almost all the information
about $\theta$ is in $\overline Y_n$; as $\theta\to0$, the reverse holds and $\overline X_n$ carries
the information. The sufficient statistic $\overline X_n+2\overline Y_n$, which both the MLE and the
UMVU estimator are built from, automatically lets whichever of $\overline X_n,\overline Y_n$ is more
informative dominate the sum — an "everyday miracle" of using a sufficiency reduction, which would
be hard to engineer by hand. $\tilde\theta_n$, by contrast, gives the two sources of information an
equal vote regardless of $\theta$, and pays for it in efficiency.

**(f) Testing the model itself.** Now embed the model in the larger family
$X_i\sim\mathrm{Pois}(\theta)$, $Y_i\sim\mathrm{Pois}(\lambda)$ with $\theta,\lambda$ unrelated, and
test $H_0:\lambda=\theta^2$ against $H_1:\lambda\ne\theta^2$. The easiest route is the generalized
likelihood ratio test: under $H_0$ the MLE is $\hat\theta_n$ from part (c); under $H_1$ the two
Poisson means are estimated separately by $\overline X_n$ and $\overline Y_n$. Twice the difference
in maximized log-likelihoods simplifies to
$$G(X) = 2n\left\{\overline X_n\left(\log\frac{\overline X_n}{\hat\theta_n}-1\right)+\overline Y_n\left(\log\frac{\overline Y_n}{\hat\theta_n^2}-1\right)-\hat\theta_n(1+\hat\theta_n)\right\}.$$
The null model has one free parameter and the alternative has two, so under $H_0$,
$G(X)\Rightarrow\chi^2_1$, and the test rejects when $G(X)$ exceeds the upper-$\alpha$ quantile of
$\chi^2_1$.

## Problem 2: a mean constrained to an interval

**Setup.** In the Gaussian sequence model $X_i \overset{\text{ind.}}{\sim} N(\mu_i,1)$,
$i=1,\dots,d$, suppose it is additionally known that $|\mu_i|\le\theta$ for a bound $\theta>0$
(known unless stated otherwise). This is a simple model of *shrinkage from a hard constraint*, in
contrast to shrinkage toward $0$ from a prior belief.

**(a) The constrained MLE.** Maximizing $-\tfrac12\sum_i(X_i-\mu_i)^2$ subject to $|\mu_i|\le\theta$
just means choosing $\hat\mu_i$ as close to $X_i$ as the constraint allows, i.e. clipping:
$$\hat\mu_i = \begin{cases}\theta & X_i>\theta\\ X_i & -\theta\le X_i\le\theta\\ -\theta & X_i<-\theta.\end{cases}$$

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="The clipped MLE of a mean constrained to an interval, plotted against the observed data.">
<defs>
<marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
</marker>
</defs>
<rect x="30" y="20" width="80" height="180" fill="currentColor" fill-opacity="0.15"/>
<rect x="210" y="20" width="80" height="180" fill="currentColor" fill-opacity="0.15"/>
<line x1="30" y1="110" x2="300" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
<line x1="160" y1="205" x2="160" y2="15" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
<line x1="110" y1="20" x2="110" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
<line x1="210" y1="20" x2="210" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
<line x1="30" y1="160" x2="290" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
<line x1="30" y1="60" x2="290" y2="60" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.6"/>
<polyline points="30,160 110,160 210,60 290,60" fill="none" stroke="currentColor" stroke-width="2.5"/>
<text x="292" y="124" font-size="12" fill="currentColor">X</text>
<text x="166" y="24" font-size="12" fill="currentColor">estimate</text>
<text x="206" y="130" font-size="11" fill="currentColor">θ</text>
<text x="96" y="130" font-size="11" fill="currentColor">−θ</text>
<text x="166" y="64" font-size="11" fill="currentColor">θ</text>
<text x="162" y="172" font-size="11" fill="currentColor">−θ</text>
</svg>
<figcaption>The clipped MLE tracks $X_i$ exactly inside $[-\theta,\theta]$ (the diagonal, unshaded
segment) and is flat outside it (the two shaded regions). Its derivative is $1$ in the middle and
$0$ in the shaded regions — exactly the quantity that appears in the SURE calculation in part (b).</figcaption>
</figure>

**(b) An unbiased estimate of its risk (SURE).** Write $\hat\mu(X)=X-h(X)$, where
$$h_i(x) = x_i-\hat\mu_i(x) = \begin{cases}x_i-\theta & x_i>\theta\\0&-\theta\le x_i\le\theta\\ x_i+\theta & x_i<-\theta\end{cases}$$
is the amount clipped off. Its derivative is $0$ inside $[-\theta,\theta]$ and $1$ outside, matching
the two regions of the figure above. Stein's unbiased risk estimate is then
$$R(X) = d + \sum_{i=1}^d(|X_i|-\theta)_+^2 - 2\sum_{i=1}^d \mathbf 1\{|X_i|>\theta\}.$$

**(c) A Bayesian version.** Now add the assumption $\mu_i\overset{\text{i.i.d.}}\sim\mathrm{Unif}[-\theta,\theta]$
(still with $\theta$ known). Because the $(\mu_i,X_i)$ pairs are then i.i.d., the posterior for
$\mu_i$ only depends on $X_i$, and the uniform prior density $1/(2\theta)$ cancels between the
numerator and denominator of Bayes' rule, leaving
$$p(\mu_i\mid X) = \frac{\phi(X_i-\mu_i)}{\int_{-\theta}^\theta \phi(X_i-u)\,du}\cdot\mathbf 1\{|\mu_i|\le\theta\}$$
— a $N(X_i,1)$ density truncated to $[-\theta,\theta]$. The Bayes estimator under squared error is
the posterior mean,
$$\mathbb{E}[\mu_i\mid X] = \frac{\int_{-\theta}^\theta u\,\phi(X_i-u)\,du}{\int_{-\theta}^\theta \phi(X_i-u)\,du}.$$
This is a *soft* version of the clipped MLE: instead of hard-truncating at $\theta$, it averages
$X_i$ against the truncated normal density, so it shrinks toward the interior smoothly rather than
snapping to the boundary.

**(d) A hierarchical model and its Gibbs sampler.** Now let $\theta$ itself be random, with an
exponential hyperprior:
$$\theta\sim\mathrm{Exp}(\lambda), \qquad \mu_i\mid\theta \overset{\text{i.i.d.}}\sim \mathrm{Unif}[-\theta,\theta], \qquad X_i\mid\theta,\mu\overset{\text{ind.}}\sim N(\mu_i,1).$$
Part (c) already gives the conditional law of $\mu$ given $(\theta,X)$: independent truncated
normals, $\mu_i\mid X,\theta \overset{\text{ind.}}\sim N(X_i,1)\mathbf 1\{|\mu_i|\le\theta\}$ (they
are conditionally, though not marginally, independent, because the pairs $(\mu_i,X_i)$ are i.i.d.
*given* $\theta$). The conditional law of $\theta$ given $(\mu,X)$ is proportional to
$$p(\theta\mid\mu,X) \propto \frac1\lambda e^{-\theta/\lambda}\prod_{i=1}^d \frac1{2\theta}\mathbf 1\{|\mu_i|\le\theta\} \propto \theta^{-d}e^{-\theta/\lambda}\,\mathbf 1\{\theta\ge \max_i|\mu_i|\},$$
i.e. a truncated version of a "Gamma$(1-d,\lambda)$" density with a negative shape parameter
(not normalizable without the truncation at $\max_i|\mu_i|$, but perfectly well defined once
truncated there), sampled by plugging a uniform draw into its inverse CDF. The Gibbs sampler
alternates:

1. Draw $\mu_i^{(t+1)}\overset{\text{ind.}}\sim N(X_i,1)\mathbf 1\{|\mu_i|\le\theta^{(t)}\}$ for
   $i=1,\dots,d$.
2. Draw $\theta^{(t+1)}$ from $p(\theta\mid\mu^{(t+1)},X)\propto \theta^{-d}e^{-\theta/\lambda}\mathbf 1\{\theta\ge\max_i|\mu_i^{(t+1)}|\}$.

(With the improper flat hyperprior $p(\theta)\equiv1$ instead of $\mathrm{Exp}(\lambda)$, step 2
would have been an exact Pareto draw.)

## Problem 3: exact and distribution-free inference for a Gamma model

**Setup.** Observe independent $X_{ij}\sim\mathrm{Gamma}(k_i,\sigma_j)$ for $i=1,\dots,n\ge2$ groups
and $j=1,2$ replicate "columns," each $X_{ij}$ scaled by its own column parameter $\sigma_j$ but
with a shape $k_i$ shared across the two columns within a row. Write $S_j=\sum_i X_{ij}$ and
$M_i=X_{i1}X_{i2}$. Each part restricts a different subset of $(k_1,\dots,k_n,\sigma_1,\sigma_2)$ to
be known.

**(a) A full-rank exponential family.** Multiplying the $2n$ Gamma densities and collecting terms,
$$p_{k,\sigma}(x) = \exp\left\{\sum_i k_i\log M_i + \sum_j \frac{S_j}{\sigma_j} - \sum_{i,j}k_i\log\sigma_j - \log\Gamma(k_i)\right\}\frac1{\prod_{i,j}x_{ij}},$$
a full-rank exponential family with natural parameter $\left(k_1,\dots,k_n,\tfrac1{\sigma_1},\tfrac1{\sigma_2}\right)\in\mathbb R_+^{n+2}$
(an open set) and sufficient statistic $(\log M_1,\dots,\log M_n, S_1,S_2)$, or equivalently — since
it's a bijection of the same information — $T(X)=(S_1,S_2,M_1,\dots,M_n)$. Full rank plus an open
natural parameter space makes $T$ complete sufficient.

**(b) An exact confidence interval for $\sigma_2/\sigma_1$, shapes known.** With $k_1,\dots,k_n$
known, $(S_1,S_2)$ is itself complete sufficient, and
$$S_j\overset{\text{ind.}}\sim\mathrm{Gamma}(k_+,\sigma_j) = \frac{\sigma_j}2\chi^2_{2k_+}, \qquad k_+=\textstyle\sum_ik_i.$$
Writing $\rho=\sigma_2/\sigma_1$ and $R=S_2/S_1$, $R = \rho\cdot\frac{S_2/\sigma_2}{S_1/\sigma_1}\sim\rho\,F_{2k_+,2k_+}$,
a pivot. If $c_1,c_2$ are the lower and upper $\alpha/2$ quantiles of $F_{2k_+,2k_+}$, inverting
$c_1\le R/\rho\le c_2$ gives the exact $1-\alpha$ confidence interval $[R/c_2,\ R/c_1]$.

**(c) A UMP test for a common shape, scales known.** If instead $\sigma_1,\sigma_2$ are known and
$k_1=\dots=k_n=k$ for an unknown common $k$, the likelihood collapses to a one-parameter exponential
family in $k$ with sufficient statistic $\sum_i\log M_i$ (equivalently $P=\prod_i M_i=\prod_{i,j}X_{ij}$),
so by the same one-sided-testing argument used earlier in the course for monotone-likelihood-ratio
families, the UMP test of $H_0:k=k_0$ against $H_1:k>k_0$ rejects for large $P$ — or, to remove the
dependence on $\sigma_1,\sigma_2$, for large values of $P_1 = P/(\sigma_1^n\sigma_2^n)$, which under
$H_0$ is exactly a product of $2n$ independent $\mathrm{Gamma}(k_0,1)$ variables. Since this
distribution has no closed form, the rejection cutoff is obtained by Monte Carlo: simulate many
draws of $P_1$ under $k=k_0$ and take the empirical upper-$\alpha$ quantile, which is exact up to
(controllable) simulation error.

**(d) A UMPU test for comparing two shapes, $n=2$.** With $n=2$ and all four parameters unknown, the
exponent of the joint density can be rewritten to isolate the comparison of interest,
$$\frac{k_1-k_2}2(\log M_1-\log M_2) + \frac{k_1+k_2}2(\log M_1+\log M_2) + \frac{S_1}{\sigma_1}+\frac{S_2}{\sigma_2} - \sum_{i,j}k_i\log\sigma_j-\log\Gamma(k_i),$$
so $(\log M_1-\log M_2)$ is paired with the parameter of interest $k_1-k_2$, while
$(k_1+k_2,\sigma_1,\sigma_2)$ are nuisance parameters with their own sufficient statistics
$(\log M_1+\log M_2, S_1, S_2)$, or equivalently $(M_1M_2,S_1,S_2)$. The standard construction for
testing one exponential-family parameter in the presence of nuisance parameters gives a UMPU test
of $H_0:k_1=k_2$ against $H_1:k_1>k_2$ that rejects for large values of $M_1/M_2$, conditional on
$(M_1M_2,S_1,S_2)$.

**(e) Dropping the Gamma assumption entirely.** Now let $n$ be arbitrary, no parameter be known, and
replace the Gamma family by a generic, unknown continuous scale family per row,
$X_{ij}\overset{\text{i.i.d.}}\sim G_i(x/\sigma_j)$ with $G_i(0)=0$. We still want an exact 95%
confidence interval for $\rho=\sigma_2/\sigma_1$ that is guaranteed valid no matter what
$G_1,\dots,G_n$ are. Rewriting $X_{i1},\,X_{i2}/\rho \overset{\text{i.i.d.}}\sim G_i(x/\sigma_1)$
whenever $\rho=\sigma_2/\sigma_1$ is the true ratio shows the two members of pair $i$ are
exchangeable at the true $\rho$, which licenses a permutation argument: consider
$$B(X;\rho_0) = \sum_{i=1}^n\mathbf 1\{X_{i2}/\rho_0 > X_{i1}\} = \sum_{i=1}^n\mathbf 1\{R_i>\rho_0\}, \qquad R_i := X_{i2}/X_{i1},$$
which under $H_0:\rho=\rho_0$ is exactly $\mathrm{Binom}(n,1/2)$, because exchangeability of
$(X_{i1},X_{i2}/\rho_0)$ makes each indicator a fair coin flip, independently across $i$ — and this
holds *for every* choice of $G_1,\dots,G_n$, which is the whole point. Writing
$R_{(1)}>\dots>R_{(n)}$ for the order statistics of $R_1,\dots,R_n$ and $b_1$ for the lower
$\alpha/2$ quantile of $\mathrm{Binom}(n,1/2)$ (so $n-b_1$ is the upper quantile), the two-sided
permutation test fails to reject $\rho_0$ exactly when
$$b_1 \le \sum_i\mathbf1\{R_i>\rho_0\}\le n-b_1 \iff R_{(n+1-b_1)}\le\rho_0<R_{(b_1)},$$
so $\big[R_{(n+1-b_1)},\,R_{(b_1)}\big]$ is an exact, distribution-free confidence interval for
$\rho$ — no Monte Carlo needed, because the null distribution of $B$ is exactly binomial and does
not depend on the nuisance statistic at all.

## Problem 4: nonlinear regression — a pivot, consistency, and a failure of identifiability

**Setup.** Observe i.i.d. pairs $(X_i,Y_i)$, $X_i\in\mathbb R^k$ drawn from a *known* density $q(x)$,
independent of the errors, with
$$Y_i = f_\tau(X_i)+\varepsilon_i, \qquad \varepsilon_i\overset{\text{i.i.d.}}\sim N(0,\sigma^2).$$
The parameters $\tau\in[-1,1]$ and $\sigma^2>0$ are unknown; $f_\tau$ is known up to $\tau$, is
infinitely differentiable in $\tau$ with $g_\tau=\partial f/\partial\tau>0$ everywhere and
$h_\tau=\partial^2f/\partial\tau^2$, and $|g_\tau(x)|,|h_\tau(x)|\le1$ for all $\tau,x$.

**(a) A finite-sample $t$-test, $X$ fixed.** For $X_1,\dots,X_n$ *fixed*, test $H_0:\tau=0$ against
$H_1:\tau\ne0$ with
$$T = \frac{\sum_i g_0(X_i)(Y_i-f_0(X_i))}{\hat\sigma\big(\sum_i g_0(X_i)^2\big)^{1/2}}, \qquad
\hat\sigma^2 = \frac1d\left[\sum_i(Y_i-f_0(X_i))^2 - \frac{\big[\sum_ig_0(X_i)(Y_i-f_0(X_i))\big]^2}{\sum_ig_0(X_i)^2}\right].$$
Let $z=(g_0(X_1),\dots,g_0(X_n))$ and $q_1=z/\|z\|$. Under $H_0$, $Y_i-f_0(X_i)=\varepsilon_i$, so
the numerator of $T$ is $q_1'\varepsilon\cdot\|z\|$ and $\hat\sigma^2$ is
$\tfrac1d\varepsilon'(I_n-q_1q_1')\varepsilon = \tfrac1d\|Q_r'\varepsilon\|^2$, where $Q_r$'s columns
span the $(n-1)$-dimensional orthogonal complement of $q_1$. Because $Q_r'q_1=0$, the Gaussian
vectors $q_1'\varepsilon\sim N(0,\sigma^2)$ and $\|Q_r'\varepsilon\|^2\sim\sigma^2\chi^2_{n-1}$ are
independent, and this pins down $d=n-1$ and
$$T = \frac{N(0,\sigma^2)}{\sqrt{\sigma^2\chi^2_{n-1}/(n-1)}} \sim t_{n-1}$$
under $H_0$ — the same projection argument that makes ordinary least-squares $t$-statistics exact.

**(b) The same test works with $X$ random.** If $X_1,\dots,X_n$ are instead i.i.d. from an unknown
distribution, conditioning on $X_1,\dots,X_n$ reduces exactly to part (a), so $T\mid X$ is
$t_{n-1}$-distributed regardless of the realized $X$'s. A conditional distribution that does not
depend on the conditioning variable is also the unconditional distribution, and moreover implies
independence of $T$ and $X$: $T\sim t_{n-1}$ unconditionally, and the test's null distribution is
unaffected by whether $X$ is fixed or random.

**(c) Consistency of the MLE, $\sigma^2$ known.** Because $[-1,1]$ is compact, the general theorem
for consistency of the MLE on a compact parameter space only requires identifiability and the
integrability condition $\mathbb{E}_{\tau_0}\big[\sup_{\tau\in[-1,1]}|\ell_1(\tau)-\ell_1(\tau_0)|\big]<\infty$.
Since $|g_\tau(x)|\le1$, the log-likelihood derivative satisfies
$|\dot\ell_1(\tau)|=|g_\tau(X)(Y-f_\tau(X))|/\sigma^2 \le (|\varepsilon|+2)/\sigma^2$ for every $\tau$
(using $|f_\tau(x)-f_{\tau_0}(x)|\le|\tau-\tau_0|\sup_\tau|g_\tau(x)|\le2$ on $[-1,1]$), which bounds
the required expectation by $\mathbb E_{\tau_0}[2|\varepsilon|+4]/\sigma^2<\infty$. For
identifiability: if $\tau_2>\tau_1$, the mean value theorem gives
$f_{\tau_2}(x)-f_{\tau_1}(x)=(\tau_2-\tau_1)g_{\tilde\tau(x)}(x)$ for some $\tilde\tau(x)\in[\tau_1,\tau_2]$,
so
$$\mathbb E_{\tau_2}Y-\mathbb E_{\tau_1}Y = (\tau_2-\tau_1)\,\mathbb E\big[g_{\tilde\tau(X)}(X)\big] > 0$$
since $g_{\tilde\tau(x)}(x)>0$ almost surely — different values of $\tau$ give strictly different
mean functions, so $\tau$ is identifiable and $\hat\tau_n\overset{p}\to\tau$.

**(d) Asymptotic normality.** Continuing with $\sigma^2$ known and $\tau$ in the interior $(-1,1)$,
the second derivative is
$\ddot\ell_1(\tau) = \sigma^{-2}\{h_\tau(X)(Y-f_\tau(X)) - g_\tau(X)^2\}$, whose expectation is
$$J_1(\tau) = -\mathbb E\ddot\ell_1(\tau) = \frac1{\sigma^2}\mathbb E_\tau\big[g_\tau(X)^2\big]$$
(the $h_\tau(X)(Y-f_\tau(X))$ term has conditional mean zero given $X$). Given consistency, the
usual MLE asymptotics give
$$\sqrt n(\hat\tau_n-\tau)\Rightarrow N\!\left(0,\ \frac{\sigma^2}{\mathbb E_\tau[g_\tau(X)^2]}\right).$$

**(e) Adding an intercept breaks identifiability.** If instead $Y_i\mid X_i \sim N(\alpha+f_\tau(X_i),\sigma^2)$
with $\alpha$ also unknown, $\tau$ can no longer be estimated consistently in general — no proof is
possible because it's false. Take $f_\tau(x)\equiv\tau$ (a constant function of $x$), which
satisfies every stated condition ($g_\tau\equiv1$, $h_\tau\equiv0$, both bounded, $g_\tau>0$). Then
the model only ever sees $\alpha+\tau$: the log-likelihood is a function of $\alpha+\tau$ alone
(it equals $\overline Y_n$ at its maximum), so *any* pair $(\alpha,\tau)$ with $\alpha+\tau=\overline Y_n$
maximizes the likelihood equally well. There is no way for a sequence of MLEs to pick out the true
$\tau$ specifically — the parameter is unidentifiable, and no estimator, maximum likelihood or
otherwise, can be consistent for it.

## Sources

All four problems and their solutions come from the same reconstructed document: Berkeley
STAT210A (Prof. Will Fithian), Fall 2020 final examination and model solutions, converted to
markdown at
`docs/statistics/berkeley/stat210a/fall-2024/old-exams/solution2020/` in the knowledge-base-library
(identical copies of the same two files are filed under the `fall-2025`, `fall-2025/units` and
`fall-2026` course-instance directories in the same repository; only one copy of each was used
here). The correspondence:

- Front matter and exam instructions (timing, collaboration rules, point values, the note that
  "results from lecture or homework" may be cited without re-derivation) —
  `01-final-examination-question-booklet.md`.
- All four problem statements and all four model solutions — `02-good-luck.md`: Problem 1
  ("One Poisson, two Poissons") and its solution, Problem 2 ("A problem of limited means") and its
  solution, Problem 3 ("Gamma palooza") and its solution, Problem 4 ("Apocalypse $\tau$") and its
  solution.

No slides or lecture transcript were supplied for this chapter — the exam booklet and its solutions
were the only input, and the exam explicitly is not itself a lecture but a semester-end review
instrument. The source file carries a conversion notice worth repeating here: the original PDF had
no extractable text layer, so this markdown is a model's reconstruction of scanned pages, and every
displayed equation in it is flagged there as unverified against the original scan.

---

[← 74. Sufficiency, Minimax, and Asymptotic Theory](74-sufficiency-minimax-and-asymptotic-theory.md) · [Contents](index.md) · [76. Regression with Correlated Errors →](76-regression-with-correlated-errors.md)
