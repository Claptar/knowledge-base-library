---
title: "82. Nuisance Parameters"
course: "Berkeley Stat 210A"
chapter: 82
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 82. Nuisance Parameters

## What this covers

Most testing problems have more unknown parameters than the hypothesis is actually about. This
chapter asks how to test a hypothesis on a parameter of interest $\theta$ when the model also
carries an unknown **nuisance parameter** $\lambda$ that can shift the size or power of any test.
It develops the main tool — conditioning on a statistic that is sufficient for $\lambda$ — states
the resulting optimal (UMPU) test for exponential families, sketches why it is optimal, and shows
the same conditioning idea surviving even when there is no exponential family at all, in
permutation tests. It assumes UMP and UMP-unbiased testing for one-parameter exponential families,
sufficiency and completeness, and the natural-parameter form of an exponential family density.

## Nuisance parameters: the setup

One-parameter families are the exception in statistics, not the rule. Formally, we observe $X$
from a model

$$
\mathcal P = \{P_{\theta,\lambda} : (\theta,\lambda) \in \Omega\},
$$

where $\theta$ and $\lambda$ may be real vectors, or may represent infinite-dimensional objects
such as unknown distributions. The hypotheses concern $\theta$ alone — $H_0:\theta\in\Theta_0$ vs
$H_1:\theta\in\Theta_1$ — and $\lambda$ is the **nuisance parameter**: unknown, not of interest,
but capable of changing the type-I error or the power of a test we might otherwise like to use.

Three examples fix the pattern.

- **Two-sample Gaussian.** $X_1,\dots,X_n\stackrel{\text{iid}}\sim N(\mu,\sigma^2)$,
  $Y_1,\dots,Y_m\stackrel{\text{iid}}\sim N(\nu,\sigma^2)$, all three of $\mu,\nu,\sigma^2$
  unknown, testing $H_0:\mu=\nu$ vs $H_1:\mu\neq\nu$. Here $\theta=\mu-\nu$ is the parameter of
  interest, and $\lambda=(\mu+\nu,\sigma^2)$ (or $(\mu,\sigma^2)$, or any other coordinatization of
  what remains) is the nuisance parameter.
- **Comparing two Poissons.** $X\sim\mathrm{Pois}(\mu)$, $Y\sim\mathrm{Pois}(\nu)$, testing
  $H_0:\mu\le\nu$ vs $H_1:\mu>\nu$. One could use $\mu-\nu$ as the parameter of interest, but it
  turns out to be more natural to use the ratio $\mu/\nu$, or $\theta=\mu/(\mu+\nu)$.
- **Two-sample binomial.** $X_1\sim\mathrm{Binom}(n_1,\pi_1)$, $X_2\sim\mathrm{Binom}(n_2,\pi_2)$,
  with $n_1,n_2$ *known* (so not nuisance parameters), testing $H_0:\pi_1\le\pi_2$ vs
  $H_1:\pi_1>\pi_2$. Again $\pi_1-\pi_2$ is an option, but the natural quantity turns out to be the
  **odds ratio** $\rho = \frac{\pi_1/(1-\pi_1)}{\pi_2/(1-\pi_2)}$, whose log is the difference
  between the two natural (logit) parameters.

In each case the question is the same: how do we test $\theta$ without the unknown $\lambda$
contaminating the answer?

## Conditioning as a strategy

The central idea is to **condition on a statistic $U$ that carries all the information about
$\lambda$**, so that the conditional distribution of the rest of the data no longer depends on
$\lambda$ at all.

**A warm-up: binomial counts with a random sample size.** Suppose $N$ is a sample size and, given
$N=n$, we observe $X\sim\mathrm{Binom}(n,\theta)$ — the situation, for instance, of a survey with a
random number of respondents. First suppose the distribution of $N$ is *known*, say
$N\sim\mathrm{Pois}(10)$, and we want to test $H_0:\theta\le\tfrac12$ vs $H_1:\theta>\tfrac12$. The
full likelihood is

$$
p_\theta(n,x) = \frac{10^n e^{-10}}{n!}\binom nx \theta^x(1-\theta)^{n-x}, \qquad 0\le x\le n.
$$

There is no UMP test here: the likelihood ratio between $\theta=\tfrac12$ and any alternative
$\theta_1>\tfrac12$,

$$
\log\frac{p_{\theta_1}}{p_{1/2}}(n,x) = x\log\frac{\theta_1}{1-\theta_1} - n\log\big(2(1-\theta_1)\big),
$$

is a different linear combination of $x$ and $n$ for each $\theta_1$, so no single rejection
region can be best against every alternative at once. Two natural tests are available instead.

- *Marginal test.* Marginally $X\sim\mathrm{Pois}(10\theta)$, which has monotone likelihood ratio
  in $X$; reject when $X$ exceeds the upper-$\alpha$ quantile of $\mathrm{Pois}(5)$. Call this
  $\phi_1$; it certainly satisfies $\mathbb E_\theta[\phi_1]\le\alpha$ for $\theta\le\tfrac12$.
- *Conditional test.* Conditionally, $X\mid N=n \sim \mathrm{Binom}(n,\theta)$, which also has MLR
  in $x$ for fixed $n$; reject when $X$ exceeds the upper-$\alpha$ quantile of
  $\mathrm{Binom}(n,\tfrac12)$. Call this $\phi_2$; it satisfies
  $\mathbb E_\theta[\phi_2\mid N=n]\le\alpha$ for *every* $n$ and every $\theta\le\tfrac12$, and
  hence $\mathbb E_\theta[\phi_2]\le\alpha$ as well.

The test $\phi_2$ is UMP in the **conditional model** $\mathcal Q_n=\{q_\theta(x\mid n):\theta\}$,
the family of conditional distributions of $X$ given $N=n$. This example illustrates a fact that
holds in general: **any level-$\alpha$ (or unbiased) test in a conditional model is automatically
level-$\alpha$ (or unbiased) in the marginal model**, because marginal power is an average of
conditional powers, and an average of numbers each $\le\alpha$ is itself $\le\alpha$. The same
holds for confidence sets.

The **conditionality principle** says that, since $N$ here is ancillary (its distribution does not
involve $\theta$), we ought to condition on it: the observed value of $N$ tells us nothing about
$\theta$ on its own, so it should be treated as fixed rather than as informative data. Whether or
not one accepts this principle as a general rule, conditioning is forced on us in a more serious
case:

**When the nuisance parameter is the distribution of $N$ itself.** Suppose instead $N$ is drawn
from an *unknown* distribution $P^N$ on $\{0,1,2,\dots\}$, with $X\mid N=n$ still
$\mathrm{Binom}(n,\theta)$. Now $P^N$ is an infinite-dimensional nuisance parameter, and the
marginal test $\phi_1$ is no longer even available — there is no fixed marginal distribution of
$X$ to appeal to. But the conditional test $\phi_2$ is untouched: the conditional model
$\mathcal Q_n$ never depended on $P^N$ in the first place. **Conditioning on $N$ removes the
nuisance parameter entirely.**

**Comparing two Poissons, revisited.** Let $N=X+Y\sim\mathrm{Pois}(\mu+\nu)$. A short calculation
(expand each Poisson pmf, divide, and use $\mathrm{Pois}(\mu)*\mathrm{Pois}(\nu)=\mathrm{Pois}(\mu+\nu)$
for the sum) gives

$$
X \mid X+Y=n \;\sim\; \mathrm{Binom}(n,\theta), \qquad \theta = \frac{\mu}{\mu+\nu}.
$$

Since $Y=N-X$, the pair $(N,X)$ carries the same information as $(X,Y)$, and conditioning on $N$
removes the nuisance parameter $\lambda=\mu+\nu$ altogether, leaving exactly the hypothesis
$H_0:\theta\le\tfrac12 \iff \mu\le\nu$ against $H_1:\theta>\tfrac12$. This reduction is not a
coincidence — it is forced by the exponential family structure of the model, which is the general
mechanism behind conditioning.

## Multiparameter exponential families: the general recipe

Take a generic exponential family in which the natural parameter splits into a parameter of
interest $\theta\in\mathbb R^s$ and a nuisance parameter $\lambda\in\mathbb R^r$:

$$
p_{\theta,\lambda}(x) = e^{\theta\cdot T(x) + \lambda\cdot U(x) - A(\theta,\lambda)}\, h(x).
$$

We want to test $H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$, treating $\lambda$ as a
nuisance parameter. The recipe is: **condition on $U(X)$, and base the test on the conditional
model for $T(X)$**, which will depend on $\theta$ alone.

No generality is lost in reducing to the sufficient statistic $(T,U)$, since any test $\phi(X)$
has exactly the same power function as $\psi(T(X),U(X)) := \mathbb E[\phi(X)\mid T,U]$. The joint
density of $(T,U)$ has the same exponential-family form,

$$
(T,U) \sim p_{\theta,\lambda}(t,u) = e^{\theta\cdot t + \lambda\cdot u - A(\theta,\lambda)}\,g(t,u),
$$

and when we form the conditional density of $T$ given $U=u$, the factor $e^{\lambda\cdot u -
A(\theta,\lambda)}$ appears in both numerator and denominator and **cancels**:

$$
q_\theta(t\mid u) = \frac{p_{\theta,\lambda}(t,u)}{\int p_{\theta,\lambda}(z,u)\,dz}
= \frac{e^{\theta\cdot t}\,g(t,u)}{\int e^{\theta\cdot z}\,g(z,u)\,dz}
= e^{\theta\cdot t - B_u(\theta)}\, g(t,u), \qquad B_u(\theta)=\log\!\int e^{\theta\cdot z}g(z,u)\,dz.
$$

The nuisance parameter $\lambda$ has vanished completely: $q_\theta(t\mid u)$ is an $s$-parameter
exponential family in $\theta$ with sufficient statistic $T$, for **every** fixed $u$. If $s=1$,
this conditional family automatically has monotone likelihood ratio in $T$, so ordinary
one-parameter theory (UMP one-sided tests, UMPU two-sided tests) applies directly, conditionally
on $u$. Even when $s>1$, the nuisance parameter is still gone, which is already useful. Note also
that the base measure $h$ never has to be dealt with separately: it is absorbed into $g(t,u)$ by
the sufficiency reduction to $(T,U)$, and plays no further role.

**Poisson comparison, done via the recipe.** Write the joint pmf of $(X,Y)$ and split the exponent
by adding and subtracting $x\log\nu$:

$$
p_{\mu,\nu}(x,y) = \exp\{x\log\mu + y\log\nu - (\mu+\nu)\}\frac{1}{x!\,y!}
= \exp\Big\{ x\log\frac\mu\nu + (x+y)\log\nu - (\mu+\nu)\Big\}\frac1{x!\,y!}.
$$

This is exactly the multiparameter exponential-family form with $\theta=\log(\mu/\nu)$, $T(x,y)=x$,
$\lambda=\log\nu$, and $U(x,y)=x+y$. So the general strategy again tells us to condition on
$X+Y=u$, and the conditional family in $T=X$ is one-parameter with MLR — reconciling this with the
earlier computation: writing out $P_\theta(X=x_1\mid X_1+X_2=u)$ explicitly gives

$$
P_\theta(X_1=x_1\mid X_1+X_2=u) = \frac{e^{\theta x_1}}{\sum_{i=0}^u e^{\theta i}}
= \binom{u}{x_1}\Big(\frac{e^\theta}{1+e^\theta}\Big)^{x_1}\Big(\frac1{1+e^\theta}\Big)^{u-x_1},
$$

i.e. $X_1\mid X_1+X_2=u \sim \mathrm{Binom}\big(u,\,e^\theta/(1+e^\theta)\big)$. The success
probability $e^\theta/(1+e^\theta)$ is exactly $\mu/(\mu+\nu)$ written on the log-odds scale — the
same conclusion as before, just derived structurally rather than by direct calculation. In the
end, testing $H_0:\theta=0$ vs $H_1:\theta\ne 0$ reduces to an ordinary two-sided binomial test.
The two-sample binomial problem from the first section is another instance of exactly this
pattern: conditioning $X_1$ on $X_1+X_2$ leaves a conditional distribution that depends only on the
log odds ratio $\rho$, and not on the nuisance parameter $\pi_2$.

## The UMPU test in exponential families

Putting the recipe together with one-parameter exponential family theory gives an exact optimal
test whenever $\theta$ is scalar ($s=1$). Let $\mathcal P$ be a full-rank exponential family
$p_{\theta,\lambda}(x) = e^{\theta T(x) + \lambda\cdot U(x) - A(\theta,\lambda)}h(x)$ with
$\theta\in\mathbb R$, $\lambda\in\mathbb R^r$.

**Two-sided case.** To test $H_0:\theta=\theta_0$ vs $H_1:\theta\ne\theta_0$, there is a UMPU test
of the form $\phi(x)=\psi(T(x),U(x))$, where

$$
\psi(t,u) = \begin{cases}
1 & t>c_2(u)\\
\gamma_2(u) & t=c_2(u)\\
0 & c_1(u)<t<c_2(u)\\
\gamma_1(u) & t=c_1(u)\\
1 & t<c_1(u)
\end{cases}
$$

with $c_1,c_2,\gamma_1,\gamma_2$ chosen so that $\mathbb E_{\theta_0}[\phi]=\alpha$ and
$\mathbb E_{\theta_0}[T\phi] = \alpha\,\mathbb E_{\theta_0}[T]$ (the second condition is what makes
$\theta_0$ a stationary point of the power function, the unbiasedness requirement).

**One-sided case.** To test $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$, there is a UMP test
$\phi(x)=\psi(T(x),U(x))$ with

$$
\psi(t,u) = \begin{cases}
1 & t>c(u)\\
\gamma(u) & t=c(u)\\
0 & t<c(u)
\end{cases}
$$

and $c(u),\gamma(u)$ chosen so that $\mathbb E_{\theta_0}[\phi]=\alpha$.

In both cases, the thresholds and randomization probabilities depend on $u$: the test conditions
on $U(X)=u$, applies the ordinary optimal one-parameter test inside the conditional family
$q_\theta(\cdot\mid u)$, and lets $u$ vary freely across its whole range. Applied to the Poisson
comparison example, this is the two-sided binomial test derived above: reject when $X_1$,
conditional on $X_1+X_2=u$, is either far below or far above what $H_0$ predicts.

## Why conditioning is optimal: a proof sketch

The claim is that among *all* unbiased tests of $H_0:\theta=\theta_0$ — not just tests built by
conditioning — $\psi$ has the highest possible power at every alternative. The argument has three
steps.

**1. Unbiasedness pins down a derivative condition at $\theta_0$.** Let $\phi$ be any unbiased
test, with power function $\beta(\theta)=\mathbb E_\theta[\phi]$. Unbiasedness forces
$\beta(\theta_0)=\alpha$, and since $\beta(\theta)\ge\alpha$ for $\theta\ne\theta_0$ while
$\beta(\theta_0)=\alpha$, the point $\theta_0$ is a minimum of $\beta$, so $\beta'(\theta_0)=0$
(the power function of an exponential-family test is infinitely differentiable, and one may
differentiate under the integral sign). Since
$\partial_\theta\mathbb E_\theta[\phi]=\mathbb E_\theta[T\phi]-\mathbb E_\theta[T]\,\mathbb E_\theta[\phi]$
for an exponential family, this translates into exactly the two moment conditions used to define
$\psi$ above: $\mathbb E_{\theta_0}[\phi]=\alpha$ and $\mathbb E_{\theta_0}[T\phi]=\alpha\,\mathbb
E_{\theta_0}[T]$.

**2. These conditions hold for every value of the nuisance parameter, hence almost surely given
$U$.** At $\theta=\theta_0$, the family reduces to the boundary submodel
$\mathcal P_0=\{p_{\theta_0,\lambda}:\lambda\in\mathbb R^r\}$, itself a full-rank $r$-parameter
exponential family in $\lambda$ with complete sufficient statistic $U(X)$. Both moment conditions
above hold for *every* $\lambda$, since $\phi$ is unbiased against the whole boundary. But two
functions of $U$ with the same expectation for every $\lambda$ in a complete family must agree
almost surely — this is exactly what completeness buys us — so the conditions strengthen from "on
average" to "conditionally, given $U$, almost surely":
$\mathbb E_{\theta_0}[\phi\mid U]=\alpha$ a.s., and (two-sided case)
$\mathbb E_{\theta_0}[T\phi\mid U]=\alpha\,\mathbb E_{\theta_0}[T\mid U]$ a.s.

**3. Conditionally on each value of $U=u$, $\phi$ is competing inside a one-parameter exponential
family, where the optimal test is already known.** For any fixed $u$, the conditional model
$\{p_\theta(\cdot\mid u)\}$ is a one-parameter exponential family in $T$ with density
$e^{\theta t}g(t,u)$. Step 2 says that $\phi$'s conditional expectation given $(T,U)=(t,u)$,
$g(t,u) := \mathbb E_{\theta_0}[\phi\mid T=t,U=u]$, defines a test of level (or unbiasedness) exactly
$\alpha$ *inside this one-parameter conditional family*. But $\psi(t,u)$ is, by construction, the
UMP test (one-sided case) or UMPU test (two-sided case, via the analogous one-parameter theorem)
in precisely this conditional family. So $\psi$ has conditional power at least as large as $\phi$'s
conditional power, for every $\theta$ and (almost) every $u$. Averaging over $u$,

$$
\mathbb E_\theta[\phi] = \mathbb E_\theta\big[\mathbb E[\phi\mid T,U]\big] \le \mathbb E_\theta\big[\mathbb E[\psi\mid T,U]\big] = \mathbb E_\theta[\psi]
$$

for every $\theta\ne\theta_0$ and every unbiased $\phi$ — which is exactly UMPU optimality of
$\psi$. (The underlying one-parameter facts used here — the derivative characterization of
unbiasedness, and the two-sided UMPU theorem for one-parameter exponential families — are standard
results referred to in the lecture as Keener's *Statistical Theory*, Theorems 12.4 and 12.22.)

## Example: normal mean, unknown variance

Let $X=(X_1,\dots,X_n)\sim N(\mu\mathbf 1,\sigma^2 I_n)$ with $\mu\in\mathbb R$ the parameter of
interest and $\sigma^2>0$ unknown, and test $H_0:\mu=0$ vs $H_1:\mu\ne0$. Writing the density in
natural-parameter form gives $T=\bar X/\|X\|$ and $U=\|X\|^2$, and the recipe says the optimal test
rejects when $\bar X$ is conditionally extreme given $\|X\|^2$.

Here is where the geometry does the work. Decompose $\mathbb R^n$ into the line spanned by
$\mathbf 1=(1,\dots,1)$ — the direction along which the mean $\mu$ moves the data — and its
orthogonal complement $\mathbf 1^\perp$. Any Gaussian vector splits into independent projections
onto these two orthogonal subspaces, so $\mathrm{Proj}_{\mathbf 1}(X)$ and
$\mathrm{Proj}_{\mathbf 1^\perp}(X)$ are independent; the first carries all the information about
$\mu$ (its length is $\sqrt n\,\bar X$), while the second carries none — it is exactly
$N(0,\sigma^2 P)$ regardless of $\mu$, so it is what informs us about $\sigma^2$ alone.

Under $H_0:\mu=0$, the whole vector $X$ is spherically symmetric, so $X/\|X\|$ is uniformly
distributed on the sphere $S^{n-1}$ and is independent of $\|X\|$. This means the optimal test
rejects for conditionally extreme $\bar X$ given $\|X\|^2$, *and* — because the null distribution
of the angle doesn't depend on $u$ at all — for marginally extreme $\bar X/\|X\|$: the two
descriptions coincide. Squaring and rearranging gives a familiar statistic:

$$
T^2 = \frac{(\sum X_i)^2}{\sum X_i^2 - \tfrac1n(\sum X_i)^2} = \frac{n\bar X^2}{\|X\|^2-n\bar X^2}
= \frac{n\bar X^2}{S^2}, \qquad S^2=\frac1{n-1}\sum(X_i-\bar X)^2,
$$

which, written in terms of the two projections, is

$$
T^2 = \frac{\|\mathrm{Proj}_{\mathbf 1}X\|^2}{\|\mathrm{Proj}_{\mathbf 1^\perp}X\|^2}\cdot\frac{n-1}n.
$$

This is (the square of) the ordinary one-sample $t$-statistic, arrived at here as a ratio of the
squared length along the "signal" direction to the squared length along the "noise" directions —
exactly the picture that makes ratios of projections the right way to think about tests with an
unknown variance nuisance parameter, a theme that recurs beyond this one example.

<figure>
<svg viewBox="0 0 300 300" role="img" aria-label="Decomposition of a Gaussian vector into its projection along the mean direction 1 and its projection onto the orthogonal complement, with the two-sided rejection region as an extreme-angle wedge">
  <circle cx="150" cy="150" r="110" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <polygon points="150,150 196.49,50.31 178.47,43.75 159.59,40.42 150,40 140.41,40.42 121.53,43.75 103.51,50.31" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <polygon points="150,150 103.51,249.69 121.53,256.25 140.41,259.58 150,260 159.59,259.58 178.47,256.25 196.49,249.69" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="150" y1="20" x2="150" y2="280" stroke="currentColor" stroke-width="1"/>
  <line x1="20" y1="150" x2="280" y2="150" stroke="currentColor" stroke-width="1"/>
  <text x="150" y="14" text-anchor="middle" font-size="12" fill="currentColor">along 1 (signal, μ)</text>
  <text x="286" y="154" text-anchor="start" font-size="12" fill="currentColor">1⊥ (noise, σ²)</text>
  <circle cx="234.26" cy="79.27" r="3" fill="currentColor"/>
  <line x1="234.26" y1="79.27" x2="234.26" y2="150" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3,3"/>
  <line x1="234.26" y1="79.27" x2="150" y2="79.27" stroke="currentColor" stroke-width="0.8" stroke-dasharray="3,3"/>
  <text x="240" y="75" font-size="12" fill="currentColor">X</text>
</svg>
<figcaption>Fixing $\|X\|^2=u$ places $X$ on a sphere. $X$ splits into an independent projection
along $\mathbf 1$ (carrying $\mu$) and onto $\mathbf 1^\perp$ (carrying only $\sigma^2$); the
two-sided test rejects when $X$'s angle from $\mathbf 1^\perp$ is extreme in either direction
(shaded wedges), which is both the conditional-given-$u$ test and, since the null angle
distribution does not depend on $u$, the marginal test.</figcaption>
</figure>

## Beyond exponential families: permutation tests

Conditioning on a statistic that is sufficient *under the null* remains useful even when there is
no exponential family — and no UMPU test — in sight.

**Two-sample permutation test.** Observe independent samples $X_1,\dots,X_n\stackrel{\text{iid}}\sim
P$ and $Y_1,\dots,Y_m\stackrel{\text{iid}}\sim Q$, and test $H_0:P=Q$ vs $H_1:P\ne Q$. This model
is not an exponential family, but under $H_0$ all $n+m$ observations are iid from the common
distribution $P$. Pool them into $Z=(Z_1,\dots,Z_{n+m})=(X_1,\dots,X_n,Y_1,\dots,Y_m)$. Under
$H_0$, the vector of pooled order statistics $U(Z)=(Z_{(1)},\dots,Z_{(n+m)})$ is complete
sufficient for $Z$, and the conditional distribution of $Z$ given $U(Z)=u$ is uniform over all
$(n+m)!$ permutations of $u$:

$$
Z \mid U(Z)=u \ \stackrel{H_0}{\sim}\ \mathrm{Unif}\{\pi u : \pi \in \mathcal S_{n+m}\}.
$$

Conditioning on $U$ makes $H_0$ a *simple* null in the conditional model — there is exactly one
conditional distribution to compare against — even though the alternative remains highly
composite (a stochastically larger $Q$, a more variable $Q$, and so on are all different ways
$H_1$ could hold, with no single best direction to test against). Because there is no generically
optimal statistic, we are free to plug in *any* test statistic $T(X,Y)$ and still get an exact
conditional test by conditioning on $U(X,Y)$. Rejecting when $T$ exceeds its conditional
$\alpha$-quantile is equivalent to rejecting for a small $p$-value

$$
p(x,y\mid u) = \mathbb P_{H_0}\big(T(X,Y)\ge T(x,y) \mid U(X,Y)=u\big)
= \frac1{(n+m)!}\sum_{\pi\in\mathcal S_{n+m}} \mathbb 1\{T(\pi u)\ge T(x,y)\}.
$$

Enumerating all $(n+m)!$ permutations is rarely feasible, so in practice one samples
$\pi_1,\dots,\pi_B\stackrel{\text{iid}}\sim\mathrm{Unif}(\mathcal S_{n+m})$ and forms the **Monte
Carlo $p$-value**

$$
p = \frac1{B+1}\Big(1+\sum_{b=1}^B \mathbb 1\{T(\pi_b u)\ge T(x,y)\}\Big).
$$

This is exact, not approximate: if $\pi_0$ is the permutation with $\pi_0 u = (x,y)$, then under
$H_0$ the permutations $\pi_0,\pi_1,\dots,\pi_B$ are themselves iid draws from $\mathcal S_{n+m}$,
so the observed data has exactly the same chance as any of the $B$ resampled versions of producing
the largest value of $T$ — giving a valid $p$-value with no asymptotics needed. (In practice one
usually permutes $(x,y)$ directly rather than permuting $u$ and reapplying $\pi$; the two are
equivalent, since $\tilde\pi_b=\pi_b\circ\pi_0^{-1}$ are again iid uniform on $\mathcal S_{n+m}$.)
This idea — sampling from the exact null distribution rather than computing its quantiles
analytically — is the Monte Carlo test, of which the permutation test is one instance; the same
principle extends to settings where Markov chain Monte Carlo is needed to sample from the null
when direct sampling isn't available.

It matters *which* statistic we condition on. $U(Z)$, the pooled order statistics, is sufficient
for $Z$ *under $H_0$ only* — it is not sufficient once $P$ and $Q$ are allowed to differ, which is
exactly why conditioning on it still leaves room to detect a difference. Compare this with
conditioning on the order statistics of each sample separately,
$V(X,Y)=(X_{(1)},\dots,X_{(n)},Y_{(1)},\dots,Y_{(m)})$: given $V$, the distribution of $(X,Y)$
would be completely known whether or not $H_0$ holds, collapsing the entire model — null and
alternative alike — to a single point and destroying all information in the data. Conditioning on
the right statistic removes the nuisance parameter (here, the unknown common distribution under
$H_0$) without also erasing the distinction between the hypotheses; conditioning on too much erases
everything.

## Sources

Berkeley STAT 210A course reader, "Testing with Nuisance Parameters," as it appears across three
offerings of the course (CC BY 4.0 throughout, converted 2026-09-18):

- Fall 2024: `reader/testing-nuisance.qmd`, split into
  [`01-nuisance-parameters.md`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-nuisance.qmd),
  `02-theorem-informal.md`, `03-proof-sketch.md`. This is the source for the formal statement of
  the UMPU/UMP theorem, the proof-sketch steps (including the reference to Keener's *Statistical
  Theory*, Theorems 12.4 and 12.22, which the lecture cites but which is not itself part of the
  supplied material), and the normal-mean-with-unknown-variance example.
- Fall 2025: `reader/testing-nuisance.html` and the duplicate `units/reader/testing-nuisance.html`
  (same content, split into `01-1-nuisance-parameters.md`, `02-2-theorem-informal.md`,
  `03-3-proof-sketch.md`). This is the source for the fuller prose motivation: the definition of
  nuisance parameters, the three opening examples, the random-sample-size conditioning examples,
  and the conditionality principle.
- Fall 2026: `reader/testing-nuisance.qmd`, split into `01-introduction.md`,
  `02-conditional-testing.md`, `03-multiparameter-exponential-families.md`,
  `04-permutation-tests.md`. Same content as the fall-2025 prose version, reorganized into shorter
  pages; used here for the multiparameter exponential family derivation and the permutation-test
  section.

Two things the lecture pointed to but the supplied material does not contain: the fall-2024 and
fall-2025 "Geometric Picture" subsections mark the spot of a figure with the placeholder "[Insert
geometric picture here]" and no image is present in the converted source — the diagram above
reconstructs the projection argument described in the surrounding text, not the original figure.
Separately, the fall-2025/fall-2026 pages embed an interactive Observable JS widget that lets a
reader vary $n$, $\pi_2$, and the odds ratio $\rho$ to see how the conditional distribution of
$X_1$ given $X_1+X_2$ depends only on $\rho$; the widget's code is in the source but is not
reproducible here and is described in prose instead, in the two-sample binomial remark. Finally,
the two-sample binomial comparison is noted in the fall-2025/2026 text as "shown in the problem
set" — that problem set was not included among the supplied material, so no exercise is given for
it here.

---

[← 81. t, F, and Linear Models](81-t-f-and-linear-models.md) · [Contents](index.md) · [83. Testing With One Real Parameter →](83-testing-with-one-real-parameter.md)
