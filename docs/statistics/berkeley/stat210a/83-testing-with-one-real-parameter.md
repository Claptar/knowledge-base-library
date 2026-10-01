---
title: "83. Testing With One Real Parameter"
course: "Berkeley Stat 210A"
chapter: 83
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 83. Testing With One Real Parameter

## What this covers

This chapter asks how to test hypotheses about a single real parameter $\theta$ when the earlier
machinery — a monotone likelihood ratio (MLR) family with a genuinely uniformly most powerful (UMP)
test — no longer applies, either because no statistic has MLR in the model, or because the
alternative is two-sided. It assumes the reader already has the Neyman–Pearson lemma, the notion of
a UMP test, MLR families, one-parameter exponential families, and the idea of a test's power
function.

## The testing problems

We observe $X\sim P_\theta$ for $\theta\in\Theta\subseteq\mathbb{R}$. Three shapes of hypothesis
recur:

- a **one-sided alternative**: $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$;
- a **point null** against a **two-sided alternative**: $H_0:\theta=\theta_0$ vs
  $H_1:\theta\ne\theta_0$;
- an **interval null**: $H_0:|\theta-\theta_0|\le\delta$ vs $H_1:|\theta-\theta_0|>\delta$, for some
  tolerance $\delta\ge 0$ (which reduces to the point null when $\delta=0$).

Recall the earlier result: if the family $\mathcal{P}$ has MLR in a statistic $T(X)$, the test that
rejects for large $T(X)$ is UMP for $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$, because it is
simultaneously the likelihood ratio test (LRT) of $\theta_0$ against every $\theta_1>\theta_0$, and
it controls the Type I error for every $\theta<\theta_0$. Concretely, "rejects for large $T(X)$"
means

$$
\phi(X)=\begin{cases}1 & T(X)>c\\ 0 & T(X)<c\\ \gamma & T(X)=c\end{cases},
$$

with $c=c_\alpha=\min\{c:\mathbb{P}_{\theta_0}(T(X)>c)\le\alpha\}$ the upper-$\alpha$ quantile of
$T(X)$ under $\theta_0$, and $\gamma$ a randomization used to "top off" the level when $T(X)$ is
discrete. We will mostly ignore randomization from here on and accept a conservative test instead.

## When there is no MLR statistic

A generic one-parameter model has MLR in no statistic at all: the LRT of $\theta_0$ against
$\theta_0+1$ need not agree with the LRT of $\theta_0$ against $\theta_0+2$, so no single test can
maximize power at both alternatives simultaneously.

What survives is a weaker requirement. Call $T(X)$ **stochastically increasing in $\theta$** if
$\mathbb{P}_\theta(T(X)>c)$ is non-decreasing in $\theta$ for every $c$. Then the power function of
$\phi(X)=1\{T(X)>c_\alpha\}$ is itself non-decreasing in $\theta$, which is exactly what is needed
for $\phi$ to be a valid level-$\alpha$ test of $H_0:\theta\le\theta_0$: the Type I error is
controlled not just at $\theta_0$ but at every null value. This is a much lower bar than MLR, and it
is often all that is available.

## The score test

Suppose $X_1,\dots,X_n$ are i.i.d. $P_\theta$ for large $n$, and $\mathcal{P}$ has no MLR statistic.
A useful heuristic: for large $n$ we have a lot of information about $\theta$, so most reasonable
tests will already have power close to $1$ far from $\theta_0$. The place where tests actually
differ is *near* $\theta_0$, so we prioritize maximizing power at $\theta_0+\varepsilon$ for small
$\varepsilon>0$.

The LRT of $\theta_0$ against $\theta_0+\varepsilon$ rejects for large values of

$$
\log\frac{p_{\theta_0+\varepsilon}(X)}{p_{\theta_0}(X)}=\ell(\theta_0+\varepsilon;X)-\ell(\theta_0;X)
\approx \varepsilon\,\dot\ell(\theta_0;X),
$$

so, for small $\varepsilon>0$, this is the same as rejecting for large values of the **score
statistic** $S_{\theta_0}(X)=\dot\ell(\theta_0;X)$ — provided we can separately show that the power
of that test is monotone, e.g. because $S_{\theta_0}(X)$ is stochastically increasing in $\theta$.
The score test is only justified as *locally* optimal; it need not be UMP, but it is often simple
and can perform well even away from $\theta_0$.

### Worked example: the Laplace location test

Let $X_1,\dots,X_n$ be i.i.d. $\mathrm{Laplace}(\theta)=\tfrac12 e^{-|x-\theta|}$, and test
$H_0:\theta\le 0$ vs $H_1:\theta>0$. For a fixed alternative $\theta_1>0$, the log-likelihood ratio
is

$$
\log\frac{p_{\theta_1}(X)}{p_0(X)}=\sum_i\bigl(|X_i|-|X_i-\theta_1|\bigr)=\theta_1\sum_i
T_{\theta_1}(X_i),
$$

where

$$
T_\theta(x)=\begin{cases}-1 & x\le 0\\ \dfrac{2x}{\theta}-1 & 0\le x\le\theta\\ +1 & x\ge\theta.
\end{cases}
$$

So the LRT for a fixed $\theta_1$ rejects for large $\sum_i T_{\theta_1}(X_i)$.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="The Laplace test statistic caps the contribution of each observation, unlike an unbounded linear statistic">
  <line x1="40" y1="100" x2="300" y2="100" stroke="currentColor" stroke-width="1"/>
  <line x1="144" y1="20" x2="144" y2="180" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3"/>
  <line x1="196" y1="20" x2="196" y2="180" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3"/>
  <text x="144" y="192" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="196" y="192" text-anchor="middle" font-size="12" fill="currentColor">&#952;</text>
  <text x="300" y="112" text-anchor="end" font-size="12" fill="currentColor">x</text>
  <line x1="40" y1="180" x2="300" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="5,4" opacity="0.6"/>
  <text x="255" y="35" font-size="11" fill="currentColor" opacity="0.7">unbounded (e.g. sample mean)</text>
  <polyline points="40,153.3 144,153.3 196,46.7 300,46.7" fill="none" stroke="currentColor" stroke-width="2.5"/>
  <text x="60" y="145" font-size="11" fill="currentColor">T&#952;(x)</text>
  <text x="10" y="50" font-size="12" fill="currentColor">+1</text>
  <text x="10" y="158" font-size="12" fill="currentColor">&#8722;1</text>
</svg>
<figcaption>The clipped statistic $T_\theta(x)$ (solid) treats every observation past $\theta$ as
equally strong evidence, capping the influence any single $X_i$ can have; a statistic linear in $x$,
like the sample mean (dashed), has no such cap.</figcaption>
</figure>

Once $X_i>\theta_1$, it contributes the same evidence for $\theta_1$ over $0$ no matter how far past
$\theta_1$ it lies — unlike the sample mean, where a single outlying $X_i$ has unbounded influence.
Because $f(X_i)$ is stochastically increasing in $\theta$ for *any* non-decreasing $f$, every one of
these LRTs is a valid level-$\alpha$ test on the whole null, even though only one of them is optimal
at its own $\theta_1$.

Taking $\theta_1\downarrow 0$, the statistic converges to

$$
T_{0^+}(x)=\begin{cases}-1 & x\le 0\\ +1 & x>0,\end{cases}
$$

which is exactly the score statistic at $\theta=0$:
$S_0(X)=\dot\ell(0;X)=\sum_i T_{0^+}(X_i)$. This is the **sign test**: writing
$B(X)=\tfrac{S_0(X)+n}{2}=\#\{X_i>0\}$, we have $B(X)\sim\mathrm{Binom}(n,\tfrac12)$ under $H_0$.

For $n=100$ and $\alpha=0.1$, simulation shows the score (sign) test performing noticeably better
than the test based on $\sum_i X_i$, especially at "moderately hard" alternatives such as
$\theta_1=0.2$ — though the LRT built for that specific $\theta_1=0.2$ does even better there, as it
must, since it is exactly optimal for that one alternative.

## The sign test as a nonparametric test

The appeal of the sign test is that it does not need the Laplace model at all. Suppose
$X_1,\dots,X_n$ are i.i.d. $F$ for an unknown continuous, strictly increasing cdf $F$, so the median
$\theta(F)=F^{-1}(1/2)$ is well defined, and consider $H_0:\theta(F)\le 0$ vs $H_1:\theta(F)>0$.
Exactly, with no large-$n$ approximation, $B(X)\sim\mathrm{Binom}(n,1-F(0))$, and $1-F(0)\le\tfrac12$
iff $H_0$ holds. So the test that rejects when $B(X)$ exceeds the upper-$(1-\alpha)$ quantile of
$\mathrm{Binom}(n,\tfrac12)$ is level-$\alpha$ **for every such $F$** — a genuinely distribution-free
test, recovered here as the limit of a locally-optimal parametric heuristic.

## Two-sided alternatives: why no UMP test exists

Now consider $H_0:|\theta-\theta_0|\le\delta$ vs $H_1:|\theta-\theta_0|>\delta$. A **two-tailed
test** based on $T(X)$ rejects for extreme values:

$$
\phi(X)=\begin{cases}1 & T(X)<c_1\text{ or }T(X)>c_2\\ 0 & c_1<T(X)<c_2\\ \gamma_i &
T(X)=c_i,\ i=1,2.\end{cases}
$$

Here there is generally no way to optimize power everywhere. Take the $z$-test, $X\sim N(\theta,1)$,
$H_0:\theta=0$ vs $H_1:\theta\ne 0$. Every test of the form

$$
\phi_{\alpha_1}(x)=1\{x<-z_{\alpha_1}\}+1\{x>z_{\alpha-\alpha_1}\},\qquad \alpha_1\in[0,\alpha],
$$

is level $\alpha$; $\alpha_1=0$ and $\alpha_1=\alpha$ recover the one-tailed tests, and
$\alpha_1=\alpha/2$ gives the familiar symmetric two-tailed test. No choice is as powerful for
$\theta>0$ as the right-tailed test, and none is as powerful for $\theta<0$ as the left-tailed test
— so no test maximizes power on both sides of the alternative at once, and any $\alpha_1\ne 0,\alpha$
is a genuine compromise. Worse, for $\alpha_1$ away from $\alpha/2$ the power actually dips *below*
$\alpha$ somewhere on the alternative: there are values of $\theta\ne 0$ where you are less likely to
reject than if $H_0$ were true.

The symmetric test, $\alpha_1=\alpha/2$, is distinguished in two ways:

1. it is **equal-tailed** — the Type I error budget is split evenly between the two lobes;
2. it is **unbiased** — its power is at least $\alpha$ everywhere on $H_1$.

Equal-tailedness only makes sense when $H_0$ is simple (a single value under which to split the
budget); it is not obvious how to define it for a composite interval null. Unbiasedness generalizes
cleanly to any testing problem, so it is the criterion to build on.

## Equal-tailed and unbiased tests: the exponential example

Equal-tailed and unbiased tests need not coincide once the null distribution is asymmetric. Let
$X\sim\mathrm{Exp}(\theta)$ (mean $\theta$), with $F_\theta(t)=1-e^{-t/\theta}$, and test
$H_0:\theta=1$ vs $H_1:\theta\ne1$.

The equal-tailed cutoffs are $c_1^{\mathrm{ET}}=-\log(1-\alpha/2)$ and $c_2^{\mathrm{ET}}=
-\log(\alpha/2)$, giving power function

$$
\beta_{\phi^{\mathrm{ET}}}(\theta)=1-(1-\alpha/2)^{1/\theta}+(\alpha/2)^{1/\theta}.
$$

This hits $\beta(1)=\alpha$ exactly, as it must — but it *also* equals $\alpha$ at $\theta=1/2$, and
dips below $\alpha$ on the interval $(1/2,1)$. The equal-tailed test is **not** unbiased here.

To get an unbiased test we instead need the *derivative* of the power to vanish at $\theta=1$, which
means solving for the left-tail budget $\alpha_1$ numerically:
$c_1(\alpha_1)=-\log(1-\alpha_1)$, $c_2(\alpha_1)=-\log(\alpha-\alpha_1)$. For $\alpha=0.1$ this gives
$\alpha_1=0.080$, $c_1=0.083$, $c_2=3.9$, against $c_1=0.051,c_2=3.0$ for the equal-tailed test. The
unbiased test trades some power for $\theta>1$ for more power at $\theta<1$, and its power is
minimized (at exactly $\alpha$) at $\theta=1$ rather than dipping below it nearby.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Rejection lobes of the unbiased two-sided test for the exponential mean, shaded under the null density, balanced around the mean">
  <polygon points="40,180 40,30 42.9,42 42.9,180" fill="currentColor" fill-opacity="0.25" stroke="none"/>
  <polygon points="176.5,180 176.5,178 285,180" fill="currentColor" fill-opacity="0.25" stroke="none"/>
  <polyline points="40,30 57.5,89 75,125 92.5,146.5 110,160 145,172.5 180,178 215,179 250,179.6 285,179.9"
            fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1"/>
  <line x1="75" y1="180" x2="75" y2="20" stroke="currentColor" stroke-width="0.75" stroke-dasharray="3,3"/>
  <text x="75" y="15" text-anchor="middle" font-size="12" fill="currentColor">E&#8321;X = 1</text>
  <text x="42.9" y="195" text-anchor="middle" font-size="11" fill="currentColor">c&#8321;</text>
  <text x="176.5" y="195" text-anchor="middle" font-size="11" fill="currentColor">c&#8322;</text>
  <text x="290" y="172" text-anchor="end" font-size="12" fill="currentColor">x</text>
</svg>
<figcaption>The rejection region of the unbiased test (shaded) balances so that the mean of $X$
conditional on rejection equals the unconditional mean under $H_0$: the near lobe below $c_1$ is
thin but tall, the far lobe past $c_2$ is thin but long, and the two carry matching moment against
$\mathbb{E}_1 X=1$.</figcaption>
</figure>

## Optimal unbiased tests (UMPU)

Unbiasedness is attractive beyond this one example precisely because it is well defined even when
$H_0$ is composite — an interval null has no single distribution to be "equal-tailed" against, but
it always has a power function that can be required to stay above $\alpha$.

If the power function $\beta_\phi$ is differentiable and $\theta_0$ is interior to $\Theta$, any
unbiased test must satisfy $\beta_\phi(\theta_0)=\alpha$ *and* $\dot\beta_\phi(\theta_0)=0$ —
otherwise the power would fall strictly below $\alpha$ on one side of $\theta_0$ for $\theta$ close
enough to $\theta_0$.

In a one-parameter exponential family $p_\theta(x)=e^{\theta T(x)-A(\theta)}h(x)$, this derivative
condition has a clean form. Differentiating the power function under the integral sign,

$$
\dot\beta_\phi(\theta_0)=\mathbb{E}_{\theta_0}\bigl[\phi(X)\bigl(T(X)-\mathbb{E}_{\theta_0}T(X)\bigr)
\bigr]=\mathrm{Cov}_{\theta_0}(T(X),\phi(X))=\mathbb{E}_{\theta_0}\bigl[(\phi(X)-\alpha)T(X)\bigr].
$$

Setting this to zero and rearranging,

$$
\mathbb{E}_{\theta_0}T(X)=\mathbb{E}_{\theta_0}\bigl[T(X)\mid \phi(X)\text{ rejects }H_0\bigr]:
$$

the conditional mean of $T(X)$ given rejection equals its unconditional mean under the null. That is
the "balance point" behind the figure above: the two rejection lobes need not carry equal
probability, only equal leverage on $T(X)$ around $\mathbb{E}_{\theta_0}T(X)$.

**Theorem (UMP unbiased tests).** In the exponential family $p_\theta(x)=e^{\theta T(x)-A(\theta)}
h(x)$, consider $H_0:|\theta-\theta_0|\le\delta$ vs $H_1:|\theta-\theta_0|>\delta$
($\delta\ge0$, $\theta_0\pm\delta\in\Theta^\circ$). Suppose $\phi^*$ rejects for extreme values of
$T(X)$, with cutoffs chosen so that

1. $\phi^*$ has power exactly $\alpha$ at the boundary of the null, $\beta_{\phi^*}(\theta_0-\delta)
   =\beta_{\phi^*}(\theta_0+\delta)=\alpha$; and
2. if $\delta>0$, the power function is flat at the center, $\dot\beta_{\phi^*}(\theta_0)=0$.

Then $\phi^*$ is UMP among unbiased level-$\alpha$ tests (UMPU).

**Sketch of the argument** (the point-null case $\delta=0$, $\theta_0=0$ without loss of
generality). For a fixed alternative $\theta\ne 0$, maximize $\int\phi\,p_\theta\,d\mu$ subject to
the two unbiasedness constraints $\int\phi\,p_0\,d\mu=\alpha$ and
$\int\phi(T-\nu_0)p_0\,d\mu=0$, where $\nu_0=\mathbb{E}_0 T(X)$ — both constraints hold with
*equality* because an unbiased test must touch $\alpha$ exactly at $\theta_0$. As in the
Neyman–Pearson argument, form the Lagrangian and note that $p_\theta/p_0(x)=e^{\theta T(x)-A(\theta)
+A(0)}$, so the maximizing test compares the convex function $e^{\theta t}$ to a *line*
$a_0+a_1t$ in $t=T(x)$:

$$
\phi^*(x)=\begin{cases}1 & e^{\theta T(x)}>a_0+a_1T(x)\\ 0 & e^{\theta T(x)}<a_0+a_1T(x)\\
\text{either} & \text{equality.}\end{cases}
$$

Because $e^{\theta t}$ is strictly convex, it crosses any line at exactly two points $c_1,c_2$, and
lies above the line outside $[c_1,c_2]$ — so $\phi^*$ is automatically a two-tailed test rejecting
for $T(x)<c_1$ or $T(x)>c_2$, for suitable $a_0,a_1$ matching any desired $c_1,c_2$. For any other
unbiased $\phi$,

$$
\beta_\phi(\theta)=\beta_\phi(\theta)-\lambda_1(\beta_\phi(0)-\alpha)-\lambda_2\dot\beta_\phi(0)
\le\beta_{\phi^*}(\theta)-\lambda_1(\beta_{\phi^*}(0)-\alpha)-\lambda_2\dot\beta_{\phi^*}(0)
=\beta_{\phi^*}(\theta),
$$

using that $\phi^*$ maximizes the Lagrangian pointwise and that both constraint terms vanish for any
unbiased $\phi$. Since $\theta$ was arbitrary, $\phi^*$ dominates every unbiased test everywhere on
$H_1$. The case $\delta>0$ is identical, with the two constraints imposed at $\theta_0-\delta$ and
$\theta_0+\delta$ instead of at $\theta_0$ itself.

## Sources

- One-sided testing, the score test, the Laplace example, and the sign test: `reader/testing-one-parameter`, section "One-sided testing" / "2 One-sided testing", from the berkeley-stat210a course reader (fall-2024, fall-2025, and fall-2026 editions — essentially identical; the fall-2025 wording is used here as the clearest of the three, and it is the edition that spells out $B(X)=\#\{X_i>0\}\sim\mathrm{Binom}(n,1/2)$ explicitly).
- Two-sided alternatives, equal-tailed vs. unbiased tests, the exponential worked example, and the UMPU theorem with proof: `reader/testing-one-parameter`, section "Two-sided alternatives" / "3 Two-sided alternatives", same editions.
- The fall-2025 `units/reader/testing-one-parameter` copies are identical in substance to the fall-2025 `reader/testing-one-parameter` copies (checked directly); only image asset paths differ.
- The R code that produced the power-comparison and rejection-region plots described in prose above is in the fall-2024 and fall-2026 `.qmd` sources but is not reproduced here; the diagrams in this chapter redraw the two arguments that code was illustrating (the capped influence of $T_\theta$, and the balance point of the unbiased rejection region) rather than the numerical simulation itself.
- An interactive Gamma-distribution widget in the fall-2025/fall-2026 two-sided-alternatives page, illustrating the same equal-tailed/unbiased tradeoff as the shape parameter varies, exists only as embedded Observable JS in the source and is not reproduced here; the same tradeoff is worked out exactly, with numbers, in the Exponential example above.
- No slides, transcript, or exercises were supplied for this chapter.

---

[← 82. Nuisance Parameters](82-nuisance-parameters.md) · [Contents](index.md) · [84. Unbiased Estimation →](84-unbiased-estimation.md)
