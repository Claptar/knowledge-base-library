---
title: "52. Multiparameter Exp. Families"
course: "Berkeley Stat 210A Fall 2024"
chapter: 52
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 52. Multiparameter Exp. Families

## What this covers

Every test built so far assumed the model had a single unknown parameter. This chapter asks what
happens when it does not: the parameter of interest $\theta$ shares the model with a nuisance
parameter $\lambda$ that we do not care about but that can still corrupt the level or the power of
a test. The answer developed here is *conditioning*: find a statistic $U(X)$ whose conditional
distribution, given $U(X)=u$, no longer depends on $\lambda$, and build the test inside that
conditional model instead. For multiparameter exponential families this can be done exactly, and
when the parameter of interest is one-dimensional it produces an honest UMPU (uniformly most
powerful unbiased) test. This assumes the earlier machinery of the course: exponential families,
complete sufficiency, monotone likelihood ratio (MLR), and Neyman–Pearson / UMP(U) theory for a
single real parameter.

## Nuisance parameters

The general setup: a family $\mathcal P = \{P_{\theta,\lambda} : (\theta,\lambda)\in\Omega\}$, and a
test of $H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$. Here $\theta$ is the **parameter of
interest** and $\lambda$ the **nuisance parameter**. The issue is that $\lambda$ is unknown, and a
test built ignoring it may have type I error or power that depends on the true (unknown) value of
$\lambda$.

**Example.** $X_1,\dots,X_n\overset{\text{iid}}{\sim}N(\mu,\sigma^2)$ and
$Y_1,\dots,Y_m\overset{\text{iid}}{\sim}N(\nu,\sigma^2)$, with $\mu,\nu,\sigma^2$ all unknown, and
$H_0:\mu=\nu$ vs $H_1:\mu\ne\nu$. Here $\theta=\mu-\nu$ is what we want to test, and
$\lambda=(\mu+\nu,\sigma^2)$ (or equivalently $(\mu,\sigma^2)$) is nuisance.

**Example.** $X\sim\mathrm{Pois}(\mu)$, $Y\sim\mathrm{Pois}(\nu)$, independent, and
$H_0:\mu\le\nu$ vs $H_1:\mu>\nu$. Writing $\theta=\mu/(\mu+\nu)$ and $\lambda=\mu+\nu$ turns this
into $H_0:\theta\le\tfrac12$ vs $H_1:\theta>\tfrac12$, with the total intensity $\lambda$ as
nuisance. (Contrast this with two independent binomials with *known* sample sizes $n_1,n_2$: there
the sample sizes are not nuisance parameters at all, they are just known constants.)

## A motivating puzzle: conditioning on an ancillary count

Before tackling exponential families in general, it is worth seeing why conditioning is the right
move at all, in a toy problem where the nuisance parameter is not even part of $\theta,\lambda$ in
the usual sense.

Suppose we sample $N\sim\mathrm{Pois}(10)$ (say, the number of survey respondents who show up), and
then $X\mid N=n\sim\mathrm{Binomial}(n,\theta)$. We observe the pair $(N,X)$ and want to test
$H_0:\theta\le\tfrac12$ vs $H_1:\theta>\tfrac12$. Two natural strategies:

1. **Use the marginal distribution of $X$ alone**: $X\sim\mathrm{Pois}(10\theta)$. This family has
   MLR in $X$, so reject when $X>c^{(1)}_\alpha$, the upper-$\alpha$ quantile of $\mathrm{Pois}(5)$
   (the boundary case $\theta=\tfrac12$). This controls $\mathbb E_\theta[\phi_1(X)]\le\alpha$ for
   $\theta\le\tfrac12$.
2. **Use the conditional distribution given $N$**: $X\mid N=n\sim\mathrm{Binomial}(n,\tfrac12)$ at
   the boundary. This also has MLR in $X$, so reject when $X>c^{(2)}_\alpha(n)$, the upper-$\alpha$
   quantile of $\mathrm{Binomial}(n,\tfrac12)$. Since
   $\mathbb E_\theta[\phi_2(X)\mid N]\overset{\text{a.s.}}{\le}\alpha$ for $\theta\le\tfrac12$, taking
   expectations over $N$ gives $\mathbb E_\theta[\phi_2(X)]\le\alpha$ too.

Neither test is UMP for the *joint* problem: the likelihood ratio
$p_{\theta_1}(x,n)/p_{\theta_0}(x,n)$ depends on both $n$ and $x$ together, so no single rejection
rule dominates uniformly over $\theta_1$. But $\phi_2$ **is** UMP once you fix attention on the
conditional problem given $N=n$ — there it is an ordinary one-parameter binomial family with MLR,
and Neyman–Pearson applies directly.

This is an instance of the **conditionality principle**: $N$ is *ancillary* (its own distribution,
$\mathrm{Pois}(10)$, does not depend on $\theta$), so we should condition on it — treat the sample
size we actually got as if it had been fixed in advance. There is no reason to average performance
over surveys that did not happen.

The general fact that licenses this move:

> **Proposition.** If $\phi(X)$ has conditional level $\alpha$ (and is unbiased) given $U(X)$, then
> $\phi(X)$ has level $\alpha$ (and is unbiased) marginally.

*Proof.* $\mathbb E_\theta[\phi(X)] = \mathbb E_\theta\big[\mathbb E_\theta[\phi(X)\mid U(X)]\big]$.
$\blacksquare$

The same idea survives even when the nuisance is not a single number but an entire unknown
distribution. Suppose $N\sim P^N$ for some *unknown* distribution $P^N$ (an infinite-dimensional
nuisance parameter), still with $X\mid N=n\sim\mathrm{Binomial}(n,\tfrac12)$ under $H_0$. Then
$$
\mathbb E_{\theta,P^N}[\phi_2(X)] = \mathbb E_{\theta,P^N}\big[\mathbb E_\theta[\phi_2(X)\mid N]\big] \le \alpha
$$
still holds, because $N$ is **sufficient for the nuisance parameter** $P^N$ — meaning sufficient for
the model in which $\theta$ is treated as known. Conditioning on a statistic that is sufficient for
$\lambda$ removes $\lambda$ from the problem *regardless of how large or complicated $\lambda$ is*.
Stated in general:

> If $U(X)$ is sufficient for $\lambda$ (i.e. sufficient in the sub-model where $\theta$ is held
> fixed and known), then $\theta$ is the only parameter of the conditional family
> $\mathcal Q_u = \{Q_\theta(X\mid U(X)=u):\theta\in\Theta\}$.

The comparing-Poissons example above is a special case of exactly this: let $N=X+Y$. Then
$X\mid N=n\sim\mathrm{Binomial}(n,\theta)$ with $\theta=\mu/(\mu+\nu)$, and testing
$H_0:\mu\le\nu$ vs $H_1:\mu>\nu$ becomes testing $H_0:\theta\le\tfrac12$ vs $H_1:\theta>\tfrac12$ —
precisely the survey toy problem, but now with *both* Poisson means unknown rather than one sample
size known. The next section makes this systematic.

## Multiparameter exponential families: conditioning kills $\lambda$

Let $X$ have density (with respect to some dominating measure) in a full multiparameter exponential
family,
$$
p_{\theta,\lambda}(x) = e^{\theta' T(x) + \lambda' U(x) - A(\theta,\lambda)}\,h(x),
\qquad \theta\in\mathbb R^s,\ \lambda\in\mathbb R^r,
$$
both unknown, and suppose we want to test $H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$ without
$\lambda$ interfering. The idea is to **condition on $U(X)$**.

**Step 1 (sufficiency reduction).** $(T(X),U(X))$ is sufficient, with joint density
$$
(T,U)\sim q_{\theta,\lambda}(t,u) = e^{\theta' t + \lambda' u - A(\theta,\lambda)}\,g(t,u)
$$
with respect to, say, Lebesgue measure on $\mathbb R^{s+r}$, where $g\,dt\,du$ is the push-forward of
$h\,d\mu$ under $(T,U)$.

**Step 2 (condition on $U$).**
$$
q_\theta(t\mid u) = \frac{q_{\theta,\lambda}(t,u)}{\int q_{\theta,\lambda}(z,u)\,dz}
= \frac{e^{\theta't+\lambda'u-A(\theta,\lambda)}g(t,u)}{e^{B_u(\theta)}\displaystyle\int e^{\theta'z+\lambda'u-A(\theta,\lambda)}g(z,u)\,dz}
= e^{\theta't - B_u(\theta)}\,g(t,u),
$$
where $B_u(\theta) = \log\int e^{\theta'z}g(z,u)\,dz$ absorbs the normalizing constant. Every factor
involving $\lambda$ cancels between numerator and denominator — the conditional law of $T$ given
$U=u$ depends on $\theta$ alone.

**Step 3 (conditional test).** Test $H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$ inside the
$s$-parameter family $\mathcal Q_u = \{q_\theta(t\mid u):\theta\in\Theta\}$. If $s=1$ this is a
one-parameter exponential family, hence has MLR in $T$, and everything already known about
UMP/UMPU tests for one-parameter exponential families applies verbatim. Even when $s>1$ and no
single optimal test is guaranteed, conditioning has still done its job: $\lambda$ is gone.

**Worked example (comparing two Poisson means, in full).** Let $X_i\overset{\text{ind.}}{\sim}
\mathrm{Pois}(\mu_i)$, $i=1,2$, and test $H_0:\mu_1\le\mu_2$ vs $H_1:\mu_1>\mu_2$. Writing
$\eta_i=\log\mu_i$,
$$
p_\mu(x) = \prod_{i=1}^2\frac{\mu_i^{x_i}e^{-\mu_i}}{x_i!}
= e^{x_1\eta_1 + x_2\eta_2 - (e^{\eta_1}+e^{\eta_2})}\,\frac{1}{x_1!x_2!}
= e^{\overbrace{x_1}^{T}\overbrace{(\eta_1-\eta_2)}^{\theta} + \overbrace{(x_1+x_2)}^{U}\overbrace{\eta_2}^{\lambda} - A(\eta)}\frac{1}{x_1!x_2!}.
$$
So $\theta=\eta_1-\eta_2=\log(\mu_1/\mu_2)$, and $H_0:\theta\le0$ vs $H_1:\theta>0$ is exactly the
original hypothesis. Conditioning on $U=X_1+X_2=u$,
$$
P_\theta(X_1=x_1\mid U=u) = \frac{e^{x_1\theta+u\lambda-A(\cdot)}\,\frac{1}{x_1!(u-x_1)!}}{\sum_{z=0}^u e^{z\theta+u\lambda-A(\cdot)}\frac{1}{z!(u-z)!}}
\propto_{x_1} e^{x_1\theta}\binom{u}{x_1}
= \mathrm{Binomial}\!\left(u,\frac{e^\theta}{1+e^\theta}\right) = \mathrm{Binomial}\!\left(u,\frac{\mu_1}{\mu_1+\mu_2}\right).
$$
So the optimal test, once $\lambda$ is removed, is exactly a Binomial test: reject for large $X_1$
given $X_1+X_2=u$. This is the same conclusion reached in the previous section by treating $N=X+Y$
as sufficient for the nuisance total intensity — the exponential-family machinery makes that
argument automatic and exact.

## An explicit optimal test when $\theta$ is one-dimensional

Now specialize to $s=1$, where the conditioning argument above produces not just *a* test free of
$\lambda$, but a genuinely optimal one.

**Theorem.** Let $\mathcal P$ be a full-rank exponential family with densities
$$
p_{\theta,\lambda}(x) = e^{\theta T(x) + \lambda' U(x) - A(\theta,\lambda)}\,h(x),
\qquad \theta\in\mathbb R,\ \lambda\in\mathbb R^r,\ (\theta,\lambda)\in\Omega\text{ open}.
$$

**(a)** To test $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$, there is a UMPU test
$\phi^*(x)=\psi(T(x);U(x))$ with
$$
\psi(t;u) = \begin{cases} 1 & t>c(u)\\ \gamma(u) & t=c(u)\\ 0 & t<c(u)\end{cases}
$$
where $c(u),\gamma(u)$ are chosen so that $\mathbb E_{\theta_0}[\phi^*(X)\mid U(X)=u]=\alpha$.

**(b)** To test $H_0:\theta=\theta_0$ vs $H_1:\theta\ne\theta_0$, there is a UMPU test
$\phi^*(x)=\psi(T(x);U(x))$ with
$$
\psi(t;u) = \begin{cases} 1 & t<c_1(u)\text{ or }t>c_2(u)\\ \gamma_i(u) & t=c_i(u)\\ 0 & t\in(c_1(u),c_2(u))\end{cases}
$$
where $c_i(u),\gamma_i(u)$ are chosen so that
$$
\mathbb E_{\theta_0}[\phi^*(X)\mid U(X)=u]=\alpha, \qquad
\mathbb E_{\theta_0}\big[T(X)(\phi^*(X)-\alpha)\mid U(X)=u\big]=0.
$$

In both cases $\lambda$ has entirely disappeared from the problem: the cutoffs and randomization
depend on $u$, never on an unknown nuisance value.

## Why the theorem holds

Let $\phi$ be **any** unbiased test at level $\alpha$; the goal is to show $\phi^*$ dominates it.

**Step 1.** Since $\mathbb E_{\theta,\lambda}|\phi(X)|\le 1<\infty$ for all $(\theta,\lambda)\in\Omega$,
a standard differentiation-under-the-integral result for exponential families (Keener, Thm 2.4)
gives that $\mathbb E_{\theta,\lambda}\phi(X)$ is infinitely differentiable on $\Omega$ and can be
differentiated under the integral sign. Unbiasedness forces
$\mathbb E_{\theta_0,\lambda}[\phi(X)]=\alpha$ for every $(\theta_0,\lambda)\in\Omega$ — the power
function is exactly $\alpha$ along the whole null boundary $\{\theta_0\}\times\{\lambda:(\theta_0,\lambda)\in\Omega\}$.

**Step 2.** Restrict to the boundary sub-model $\mathcal P_{\theta_0}=\{P_{\theta_0,\lambda}:(\theta_0,\lambda)\in\Omega\}$, which has density
$$
p_{\theta_0,\lambda}(x) = e^{\lambda'U(x)-A(\theta_0,\lambda)}\cdot\frac{e^{\theta_0T(x)}}{h(x)}
$$
— a full-rank, $r$-parameter exponential family in $\lambda$ alone, in which $U(X)$ is **complete
sufficient**. Let $f(u)=\mathbb E_{\theta_0}[\phi(X)\mid U(X)=u]-\alpha$. Then, for every $\lambda$,
$$
\mathbb E_{\theta_0,\lambda}[f(U(X))] = \mathbb E_{\theta_0,\lambda}[\phi(X)] - \alpha = 0,
$$
and completeness forces $f(u)\overset{\text{a.s.}}{=}0$, i.e.
$\mathbb E_{\theta_0}[\phi(X)\mid U(X)=u]=\alpha$ for (almost) every $u$: the *conditional* level is
exactly $\alpha$, not just the marginal one. In the two-sided case, unbiasedness also forces the
derivative of the power function to vanish at $\theta_0$ for every $\lambda$; writing
$g(u)=\frac{d}{d\theta}\mathbb E_{\theta_0}[\phi\mid U=u] = \mathbb E_{\theta_0}[T(\phi-\alpha)\mid U]$,
the same completeness argument applied to
$\mathbb E_{\theta_0,\lambda}[g(U)]=\frac{\partial}{\partial\theta}\beta_\phi(\theta_0)=0$ for all
$\lambda$ gives $\frac{d}{d\theta}\mathbb E_{\theta_0}[\phi\mid U]\overset{\text{a.s.}}{=}0$: the
conditional power curve is flat at $\theta_0$, not just its average over $\lambda$.

**Step 3.** Fix $u$. The conditional model $q_\theta(t\mid u)=e^{\theta t - B_u(\theta)}g(t,u)$ is a
one-parameter exponential family, so the one-parameter UMP theory (one-sided) or UMPU theory
(two-sided) already available from earlier in the course says $\psi(t;u)$ is optimal among
*conditional* tests of $\theta=\theta_0$ with the constraints established in Step 2. Now let
$\bar\phi(t;u)=\mathbb E[\phi(X)\mid T(X)=t,U(X)=u]$: by Step 2,
$\mathbb E_\theta[\bar\phi(T;u)\mid U=u]=\mathbb E_\theta[\phi(X)\mid U(X)=u]=\alpha$ at $\theta_0$,
so $\bar\phi(\cdot;u)$ is itself a valid conditional test satisfying the same constraints. Since
$\psi(\cdot;u)$ is optimal among such tests, it has conditional power at least as large,
almost surely. Finally, for $(\theta,\lambda)\in\Omega_1$,
$$
\mathbb E_{\theta,\lambda}[\phi(X)] = \mathbb E_{\theta,\lambda}\big[\mathbb E_\theta[\bar\phi(T;U)\mid U]\big]
\le \mathbb E_{\theta,\lambda}\big[\mathbb E_\theta[\psi(T;U)\mid U]\big] = \mathbb E_{\theta,\lambda}[\phi^*(X)].
$$
So $\phi^*$ has power at least that of any unbiased level-$\alpha$ test, everywhere in the
alternative — it is UMPU.

## Conditioning without an optimal test: permutation tests

Even outside exponential families, and even when no UMPU test exists, conditioning on a statistic
that is complete sufficient *under the null* still buys something: an exact, distribution-free test.

**Two-sample problem.** $X_1,\dots,X_n\overset{\text{iid}}{\sim}P$, $Y_1,\dots,Y_m\overset{\text{iid}}{\sim}Q$,
$H_0:P=Q$ vs $H_1:P\ne Q$, with $P,Q$ ranging over an unrestricted (nonparametric) family. Under
$H_0$, the pooled sample $Z=(X_1,\dots,X_n,Y_1,\dots,Y_m)$ is $n+m$ iid draws from the common $P$,
and its order statistics $U(Z)=(Z_{(1)},\dots,Z_{(n+m)})$ are complete sufficient for $P$. Given
$U(Z)$, all $(n+m)!$ ways of assigning the sorted values back to labels ("which came from $X$,
which from $Y$") are equally likely:
$$
(X,Y)\mid U \overset{H_0}{\sim} \mathrm{Uniform}(\{\pi U : \pi\in S_{n+m}\}).
$$
So for *any* test statistic $T$, under $H_0$,
$$
\mathbb P_{P,Q}(T(Z)\ge t\mid U) = \frac{1}{(n+m)!}\sum_{\pi\in S_{n+m}}\mathbf 1\{T(\pi Z)\ge t\},
$$
exactly — no matter what $P$ is. In practice $(n+m)!$ is too large to enumerate, so a **Monte Carlo
test** samples $\pi_1,\dots,\pi_B\overset{\text{iid}}{\sim}S_{n+m}$ (e.g. $B=1000$) and computes
$$
p = \frac{1}{1+B}\Big(1+\sum_{b=1}^B\mathbf 1\{T(Z)\le T(\pi_bZ)\}\Big).
$$
Since $Z,\pi_1Z,\dots,\pi_BZ$ are exchangeable under $H_0$, $p$ is exactly uniform on the grid
$\{1/(B+1),2/(B+1),\dots,1\}$ when $T$ has no ties, and stochastically larger (still conservative)
if there are ties. This holds for an arbitrary nonparametric $P$ — conditioning has removed an
infinite-dimensional nuisance parameter, at the cost of only having a valid, not necessarily
optimal, test.

## Worked example: the one-sample $t$-test as a conditional test

The same mechanism, run on a continuous rather than discrete family, recovers a very familiar
statistic and shows *why* it takes the form it does.

Let $X_1,\dots,X_n\overset{\text{iid}}{\sim}N(\mu,\sigma^2)$, both unknown, and test $H_0:\mu=0$ vs
$H_1:\mu\ne0$ (the general $H_0:\mu=\mu_0$ case is the same argument after re-centering). In
exponential family form,
$$
p_{\mu,\sigma^2}(x) = e^{\overbrace{\mu/\sigma^2}^{\theta}\overbrace{\textstyle\sum X_i}^{n\bar X} - \overbrace{1/(2\sigma^2)}^{\lambda}\overbrace{\textstyle\sum X_i^2}^{u=\|X\|^2} - n\mu^2/(2\sigma^2)}\left(\frac{1}{2\pi\sigma^2}\right)^{n/2},
$$
so $T\propto\bar X$ is the statistic of interest and $U=\|X\|^2$ is what we must condition on to
eliminate $\sigma^2$. The optimal test rejects for extreme $\bar X$ given $\|X\|^2$.

At $\mu=0$, the density is a function of $\|x\|^2$ alone — it is **rotationally symmetric**. So
$X/\|X\|$ is uniform on the sphere $S^{n-1}$ and independent of $\|X\|$; equivalently, conditional
on $\|X\|^2=u$, $X$ is uniform on the sphere of radius $\sqrt u$. This means the awkward
conditional-on-$U$ test can be replaced by an equivalent one based on the *marginal* distribution of
$\bar X/\|X\|$ — the projection of $X$ onto the direction $1_n=(1,\dots,1)$, normalized.

For $n=2$ this is a picture in the plane: $X$ lies on a circle of radius $\|X\|$, and the direction
of interest is the diagonal $1_2$.

<figure>
<svg viewBox="0 0 320 320" role="img" aria-label="Circle of constant norm with the diagonal direction 1_2 and the two rejection arcs for the one-sample t-test">
  <line x1="20" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1" opacity="0.4"/>
  <line x1="160" y1="20" x2="160" y2="300" stroke="currentColor" stroke-width="1" opacity="0.4"/>
  <text x="288" y="152" font-size="12" fill="currentColor">X&#8321;</text>
  <text x="168" y="30" font-size="12" fill="currentColor">X&#8322;</text>

  <circle cx="160" cy="160" r="95" fill="none" stroke="currentColor" stroke-width="1.5"/>

  <line x1="78.7" y1="241.3" x2="241.3" y2="78.7" stroke="currentColor" stroke-width="1.5"/>
  <text x="243" y="72" font-size="12" fill="currentColor">1&#8322; = (1,1)</text>

  <path d="M160,160 L246.1,119.9 A95,95 0 0,1 200.1,73.9 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M160,160 L73.9,200.1 A95,95 0 0,1 119.9,246.1 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <text x="204" y="103" font-size="11" fill="currentColor">large T</text>
  <text x="56" y="232" font-size="11" fill="currentColor">small T</text>

  <line x1="160" y1="160" x2="127.5" y2="70.7" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="127.5" cy="70.7" r="2.5" fill="currentColor"/>
  <text x="108" y="62" font-size="12" fill="currentColor">X</text>

  <path d="M181.2,138.8 A30,30 0 0,1 149.7,131.8" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="172" y="118" font-size="11" fill="currentColor">&#966;</text>

  <text x="118" y="308" font-size="12" fill="currentColor">||X||&#178; = u fixed</text>
</svg>
<figcaption>Under $H_0:\mu=0$, conditioning on $\|X\|^2=u$ places $X$ uniformly on a circle of
radius $\sqrt u$; the test rejects when $X$ lands in one of the two arcs near the $1_2$ direction,
i.e. when the angle $\varphi$ between $X$ and $1_2$ is close to $0$ or $\pi$.</figcaption>
</figure>

Write $R=\dfrac{1_2'X}{\sqrt2\|X\|}=\cos\varphi$, which is independent of $\|X\|^2$ under $H_0$.
Rejecting for $R$ near $\pm1$ is equivalent to rejecting for extreme
$T=R/\sqrt{1-R^2}=\cot\varphi$, which under $H_0$ has a $t_1$ distribution.

The same logic in general $n$: let $R=\dfrac{1_n'X}{\sqrt n\|X\|}=\dfrac{\sqrt n\bar X}{\|X\|}$, and
form
$$
T = \sqrt{n-1}\cdot\frac{R}{\sqrt{1-R^2}} = \sqrt{n-1}\cdot\frac{\sqrt n\bar X}{\sqrt{\|X\|^2-n\bar X^2}} = \frac{\sqrt n\bar X}{\sqrt{S^2}},
$$
where
$$
S^2 = \frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2 = \frac{1}{n-1}\|X-\bar X1_n\|^2 = \frac{1}{n-1}\big(\|X\|^2-n\bar X^2\big)
$$
is the sample variance — the squared length of the part of $X$ orthogonal to $1_n$. So $T$ is
exactly the ordinary one-sample $t$-statistic, and conditioning is *why* it is the right pivot:
extreme $\bar X$ given $\|X\|^2$, translated through rotational symmetry, becomes extreme $\bar X$
relative to $S^2$. (Why $\sqrt n\bar X$ and $S^2$ come out independent, with $S^2\sim\sigma^2\chi^2_{n-1}/(n-1)$,
is the content flagged as the course's next theme — "ratios of projections" — and is not derived
in this lecture.)

## Sources

- Handwritten lecture notes, Berkeley STAT 210A, Lecture 17 ("Nuisance parameters" /
  "Multiparameter exponential families"), converted from PDF by a model (no text layer in the
  original scans). Three offerings of the same lecture were used together, taking the fullest
  treatment of each part rather than repeating any of them:
  - Fall 2024: `handwritten/lecture17-nuisanceparams.pdf` — nuisance-parameter setup, the
    multiparameter exponential family derivation, the theorem, and the fully worked
    Poisson-vs-Poisson conditional Binomial computation; the one-sample $t$-test example (this copy
    is cut off mid-derivation of $S^2$).
  - Fall 2025 and Fall 2026: `handwritten/lecture17-nuisanceparams.pdf` (near-identical content in
    both years) — the motivating survey/conditionality-principle example, the conditionality
    principle and the general sufficient-for-$\lambda$ statement, the permutation-test section, and
    the complete one-sample $t$-test derivation (including the general-$n$ geometric picture).
  All three files carry the note that they are model reconstructions of handwritten PDF pages with
  no text layer, and that every equation is unverified against the original; treat this chapter as
  a guide to the lecture, not a citable transcription of it.
- **Referred to but not contained in the lecture:** "Keener, Thm 2.4," used to justify
  differentiating the power function of an exponential family under the integral sign — the course
  textbook is Robert Keener's *Theoretical Statistics: Topics for a Core Course*, not supplied here.
- The geometric figure in the last section redraws the lecture's own hand-sketched picture
  (circle of constant $\|X\|$, the $1_2$ direction, and the two rejection arcs) as an SVG.

---

[← 51. Nuisance Parameters and Conditioning](51-nuisance-parameters-and-conditioning.md) · [Contents](index.md) · [53. The Canonical Linear Model →](53-the-canonical-linear-model.md)
