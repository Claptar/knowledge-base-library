---
title: "47. One-Sided Tests in General"
course: "Berkeley Stat 210A Fall 2024"
chapter: 47
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 47. One-Sided Tests in General

## What this covers

This chapter takes up hypothesis testing once the uniformly most powerful (UMP) construction for
monotone-likelihood-ratio (MLR) exponential families stops applying — either because the alternative
is one-sided but the family is not MLR, or because the alternative is two-sided altogether. It
assumes the Neyman–Pearson lemma and the MLR construction of UMP one-sided tests from earlier
lectures. Two questions drive it: when no UMP test exists, what can still be said about a one-sided
test built from a well-behaved statistic; and for a two-sided (or point) null, how should a rejection
region be split between its two tails. The answer to the second question is the notion of an
**unbiased** test, and the chapter ends with the theorem that recovers a UMP result once the class of
competitors is restricted to unbiased tests.

## When no UMP test exists

Setup: $\mathcal P = \{P_\theta : \theta \in \Theta \subseteq \mathbb R\}$, $\theta_0\in\Theta$. The
hypothesis
$$H_0:\theta\le\theta_0 \quad\text{vs}\quad H_1:\theta>\theta_0$$
is called a **one-sided hypothesis**. In an MLR family, the Neyman–Pearson test of a single pair
$(\theta_0,\theta_1)$ turns out not to depend on $\theta_1$, and that test is then UMP for the whole
one-sided problem. Outside MLR families this collapse need not happen, and often no UMP test exists
at all.

**Example (Laplace location family).** Let $X_1,\dots,X_n\overset{\text{iid}}\sim \tfrac12
e^{-|x-\theta|}$. The likelihood-ratio test of the simple hypotheses $\theta=\theta_0$ against
$\theta=\theta_1$, with $\theta_1>\theta_0$, rejects for large values of
$$\log\frac{p_1(x)}{p_0(x)} = \sum_{i=1}^n \big(|x_i-\theta_0|-|x_i-\theta_1|\big) = \sum_{i=1}^n T(x_i),$$
where working out the three ranges $x\le\theta_0$, $\theta_0\le x\le\theta_1$, $x\ge\theta_1$ gives
$$T(x) = \begin{cases}\theta_0-\theta_1 & x\le\theta_0\\ 2x-\theta_0-\theta_1 & \theta_0\le x\le\theta_1\\ \theta_1-\theta_0 & x\ge\theta_1.\end{cases}$$

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="The Laplace log-likelihood-ratio statistic T(x): flat, then a linear ramp between theta0 and theta1, then flat again">
  <defs>
    <marker id="arrow47" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="150" x2="315" y2="150" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow47)"/>
  <line x1="40" y1="200" x2="40" y2="25" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow47)"/>
  <text x="308" y="140" font-size="12" fill="currentColor">x</text>
  <text x="18" y="28" font-size="12" fill="currentColor">T(x)</text>
  <polyline points="45,185 150,185 190,115 300,115" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="150" y1="150" x2="150" y2="185" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="190" y1="150" x2="190" y2="115" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="138" y="200" font-size="12" fill="currentColor">&#952;&#8320;</text>
  <text x="193" y="200" font-size="12" fill="currentColor">&#952;&#8321;</text>
  <text x="55" y="180" font-size="11" fill="currentColor">&#952;&#8320;&#8722;&#952;&#8321;</text>
  <text x="230" y="110" font-size="11" fill="currentColor">&#952;&#8321;&#8722;&#952;&#8320;</text>
</svg>
<figcaption>The likelihood-ratio statistic T(x) for the Laplace example: constant below θ₀, a linear
ramp across [θ₀, θ₁], constant above θ₁. As θ₁ ↓ θ₀ the ramp steepens into a jump at θ₀, turning the
test into the sign test.</figcaption>
</figure>

$T$ is flat to the left of $\theta_0$, rises linearly across $[\theta_0,\theta_1]$, and is flat again
to the right of $\theta_1$. The *shape* of this optimal statistic — where the flat parts end and how
wide the ramp is — depends on the specific pair $(\theta_0,\theta_1)$, not just on the fact that
$\theta_1>\theta_0$. So the most powerful test against $\theta_1=1$ is not the most powerful test
against $\theta_1=2$: no single statistic is simultaneously optimal against every alternative in
$H_1:\theta>\theta_0$, and hence there is no UMP test for $H_0:\theta\le0$ vs $H_1:\theta>0$.

## Locally most powerful tests: the sign test as a limit

Although no test is optimal against every alternative at once, something can still be said about the
test that is optimal against alternatives infinitesimally close to the null. Take $\theta_0=0$ and let
$\theta_1=\varepsilon\downarrow0$. Splitting the sum according to where each $x_i$ falls relative to
$0$ and $\varepsilon$,
$$\sum_i T(x_i) = -\varepsilon\,\#\{x_i\le0\} + \varepsilon\,\#\{x_i\ge\varepsilon\} + \sum_{x_i\in[0,\varepsilon]}(2x_i-\varepsilon).$$
Dividing by $\varepsilon$ and letting $\varepsilon\to0$ (the middle sum, over the shrinking window
$[0,\varepsilon]$, contributes nothing in the limit),
$$\frac1\varepsilon\sum_i T(x_i) \longrightarrow \#\{x_i>0\}-\#\{x_i\le0\} = 2\#\{x_i>0\}-n,$$
so that
$$n+\frac1{2\varepsilon}\sum_i T(x_i) \longrightarrow \#\{x_i>0\}.$$
Under the null, each $X_i$ is symmetric about $0$, so $\#\{x_i>0\}\sim\text{Binomial}(n,\tfrac12)$: the
limit of the likelihood-ratio statistic, as the alternative approaches the null, is exactly the
classical **sign test**. This is the general phenomenon behind a "locally most powerful" test: even
where no UMP test exists, the LRT against a nearby alternative can stabilize to a fixed statistic as
the alternative is pushed to the boundary of the null.

## Stochastically increasing statistics

A weaker, more robust demand than optimality is that a test's power should at least move the right
way as $\theta$ increases — otherwise a "one-sided test" built from it need not even be valid.

**Definition.** A real-valued statistic $T(X)$ is **stochastically increasing** in $\theta$ if
$$P_\theta(T(X)\le t) \text{ is non-increasing in } \theta,\ \forall t.$$

If $T$ is stochastically increasing in $\theta$ and $\phi$ is the right-tailed test based on it,
$$\phi(x) = \mathbf 1\{T(x)>c\} + \gamma\,\mathbf 1\{T(x)=c\},$$
then its power function
$$\mathbb E_\theta\phi(X) = (1-\gamma)P_\theta(T>c)+\gamma P_\theta(T\ge c)$$
is non-decreasing in $\theta$. Calibrating $c,\gamma$ so that this power equals $\alpha$ at $\theta_0$
therefore gives a valid level-$\alpha$ test of $H_0:\theta\le\theta_0$ against $H_1:\theta>\theta_0$ —
not necessarily UMP, but guaranteed not to work against you as $\theta$ moves into the alternative.

Two standard sources of stochastically increasing statistics:

- **Location family**, $X_i\overset{\text{iid}}\sim p(x-\theta)$: the sample mean, the sample median,
  and the sign statistic are all stochastically increasing in $\theta$.
- **Scale family**, $X_i\overset{\text{iid}}\sim \theta^{-1}p(x/\theta)$: $\sum X_i^2$ and the median of
  $|X_1|,\dots,|X_n|$ are stochastically increasing in $\theta$.

## Two-sided alternatives

Now let $\theta_0$ be an *interior* point of $\Theta$, and test
$$H_0:\theta=\theta_0 \quad\text{vs}\quad H_1:\theta\ne\theta_0$$
(the setup generalizes naturally to an interval null $H_0:\theta\in[\theta_1,\theta_2]$). A
**two-tailed test** based on a statistic $T(X)$ rejects when $T$ is extreme in either direction:
$$\phi(x) = \begin{cases}1 & T(x)>c_2 \text{ or } T(x)<c_1\\ 0 & T(x)\in(c_1,c_2)\\ \gamma_i & T(x)=c_i.\end{cases}$$
There are now two ways to reject, and a size-$\alpha$ constraint only pins down the *sum* of the two
tail probabilities — it leaves a free parameter to balance them. For a symmetric family such as
$N(\theta,1)$ the natural choice is to equalize the two "lobes" of the rejection region, giving the
familiar $\phi(x)=\mathbf 1\{|X-\theta_0|>z_{\alpha/2}\}$. For an asymmetric distribution, or for an
interval null, balancing the tails is not automatic.

## Equal-tailed tests, and why they can be biased

Write $\alpha_1 = P_{\theta_0}(T<c_1)+\gamma_1P_{\theta_0}(T=c_1)$ and
$\alpha_2 = P_{\theta_0}(T>c_2)+\gamma_2P_{\theta_0}(T=c_2)$; any choice with $\alpha_1+\alpha_2=\alpha$
gives a level-$\alpha$ test, with $\alpha_1$ a free parameter. The most obvious choice is the
**equal-tailed test**, $\alpha_1=\alpha_2=\alpha/2$.

**Example.** Let $X\sim\text{Exp}(\theta)$ (mean $\theta$) and test $H_0:\theta=1$. Solving
$$\tfrac\alpha2 = P_1(X\le c_1)=1-e^{-c_1}, \qquad 1-\tfrac\alpha2 = 1-e^{-c_2}$$
gives $c_1=-\log(1-\alpha/2)$, $c_2=-\log(\alpha/2)$, and
$\phi(x)=\mathbf1\{x<c_1\}+\mathbf1\{x>c_2\}$. Writing $X=\theta Z$ with $Z\sim\text{Exp}(1)$, the power
function is
$$\beta_\phi(\theta) = 1-\Big(1-\tfrac\alpha2\Big)^{1/\theta} + \Big(\tfrac\alpha2\Big)^{1/\theta}.$$
This equals $\alpha$ not only at $\theta=1$ but also — by direct expansion of the square when
$\theta=\tfrac12$ — at $\theta=\tfrac12$, and for every $\theta$ strictly between $\tfrac12$ and $1$,
$\beta_\phi(\theta)<\alpha$: the test rejects *less* often at these alternatives than at the null it is
supposed to be testing against. Equal-tailed splitting, chosen purely by symmetry of the significance
level, is not guaranteed to give a sensible power function once the underlying distribution is not
itself symmetric.

## Unbiased tests

**Definition.** $\phi$ is **unbiased** if $\inf_{\theta\in\Theta_1}\mathbb E_\theta\phi(X)\ge\alpha$:
its power at every alternative is at least the significance level, so — together with being level
$\alpha$ under $H_0$ — the power function never dips below $\alpha$ anywhere.

The equal-tailed exponential test above is *not* unbiased, since its power dips below $\alpha$ on
$(\tfrac12,1)$. The fix is to choose the cutoffs directly from the requirement that $\theta_0$ be a
stationary point of the power function sitting exactly at height $\alpha$:
$$\beta_\phi(\theta_0)=\alpha, \qquad \frac{d\beta_\phi}{d\theta}(\theta_0)=0.$$
This is two equations for the two unknowns $(c_1,c_2)$ when $T$ is continuous, so that no
randomization is needed at the boundary.

**Example (one-parameter exponential family).** Let $X\sim e^{\eta T(x)-A(\eta)}h(x)$, which has
monotone likelihood ratio in $T(X)$, and test $H_0:\eta=\eta_0$ vs $H_1:\eta\ne\eta_0$ with $T$
continuous. The size condition is
$$\alpha=\beta_\phi(\eta_0) = P_{\eta_0}(T<c_1)+P_{\eta_0}(T>c_2).$$
For the derivative condition, differentiate $\beta_\phi(\eta)=\int\phi(x)e^{\eta T(x)-A(\eta)}h(x)\,d\mu$
under the integral sign:
$$\frac{d\beta_\phi}{d\eta}(\eta) = \mathbb E_\eta\big[\phi(T)(T-A'(\eta))\big] = \mathbb E_\eta[\phi(T)T]-A'(\eta)\,\mathbb E_\eta[\phi(T)],$$
and since $A'(\eta)=\mathbb E_\eta[T]$, this is $\text{Cov}_\eta(\phi(T),T)$. At $\eta=\eta_0$, using
$\mathbb E_{\eta_0}[\phi(T)]=\alpha$ from the size condition, the derivative condition becomes
$$0 = \text{Cov}_{\eta_0}(\phi(T),T) = \mathbb E_{\eta_0}\big[(\phi(T)-\alpha)\,T(X)\big].$$

## The UMPU theorem

Restricting attention to *unbiased* tests restores a UMP result, for one-parameter exponential
families.

**Theorem.** Let $X_1,\dots,X_n\overset{\text{iid}}\sim e^{\theta T(x)-A(\theta)}h(x)$, and test
$$H_0:\theta\in[\theta_1,\theta_2] \quad\text{vs}\quad H_1:\theta<\theta_1 \text{ or } \theta>\theta_2$$
(a point null is the case $\theta_1=\theta_2$). Then:

a) The unbiased level-$\alpha$ test that rejects for extreme values of $\sum_i T(X_i)$ is uniformly
   most powerful among *all* unbiased level-$\alpha$ tests — it is UMPU.

b) If $\theta_1<\theta_2$, its cutoffs $(c_1,\gamma_1,c_2,\gamma_2)$ are found by solving
   $$\mathbb E_{\theta_1}\phi = \mathbb E_{\theta_2}\phi = \alpha:$$
   the power function must equal $\alpha$ at *both* endpoints of the null interval.

c) If $\theta_1=\theta_2=\theta_0$, the cutoffs solve
   $$\mathbb E_{\theta_0}\phi(X)=\alpha, \qquad \frac{d\beta_\phi}{d\theta}(\theta_0)=\mathbb E_{\theta_0}\Big[\big(\textstyle\sum_i T(X_i)\big)(\phi(X)-\alpha)\Big]=0,$$
   exactly the two conditions worked out above.

The notes cite the proof to Keener's text rather than giving it in full; the fragment sketched in
lecture runs as follows. For a one-parameter exponential family,
$$\frac{d^2}{d\eta^2}\int e^{\eta T(x)-A(\eta)}\phi(x)\,d\mu(x) = \int\big[(T-A'(\eta))^2-A''(\eta)\big]\,p_\eta\,\phi\,d\mu,$$
which controls the curvature of the power function at a stationary point — needed to confirm that the
point solving (c) is a genuine local *minimum* of the power, not a maximum, so the power curve turns
upward on both sides of $\theta_0$. The construction of the optimal test itself is a constrained
(Lagrangian) version of Neyman–Pearson: maximizing power against a fixed alternative $p_2=p_{\theta_2}$
subject to size $\alpha$ under $p_0=p_{\theta_0}$ and the unbiasedness constraint leads to maximizing,
over $\phi$,
$$\int\phi\,p_2\,d\mu - \lambda_0\int\phi\,p_0\,d\mu - \lambda_1\int(T-\mathbb E_0T)\,\phi\,p_0\,d\mu = \int\phi\Big(\frac{p_2}{p_0}-\lambda_0-\lambda_1(T-\mathbb E_0T)\Big)p_0\,d\mu,$$
which is maximized pointwise by rejecting exactly where the bracket is positive. Because $p_2/p_0$ is
a strictly increasing function of $T$ in an exponential family, the set where an increasing function
of $T$ exceeds a linear function of $T$ is the complement of an interval — recovering the two-tailed,
extreme-values-of-$T$ shape asserted in part (a). The notes break off at this point without finishing
the computation; the complete proof is in Keener, which was not supplied here.

## Sources

- Berkeley Stat 210A, Fall 2024, handwritten Lecture 15 notes: `01-one-sided-tests-in-general.md`
  (outline, the Laplace no-UMP example and its sign-test limit, stochastically increasing statistics,
  the two-sided setup, the equal-tailed exponential example, and the unbiased-test definition and
  exponential-family example) and `02-theorem.md` (the UMPU theorem statement and its proof sketch).
- The lecture's own outline also lists a "score test" and a "many-tailed test" as agenda items;
  neither is developed in the body of the notes, so neither is covered here.
- The notes cite Keener's textbook for the full proof of the UMPU theorem; that text was not supplied
  and is not reproduced here.
- Both source files carry a "fidelity: reconstructed" note in their front matter: they were produced
  by a model reading handwritten scans with no text layer, and every equation is flagged unverified
  against the original.

---

[← 46. Hypothesis Testing and Power Functions](46-hypothesis-testing-and-power-functions.md) · [Contents](index.md) · [48. Testing with one real parameter →](48-testing-with-one-real-parameter.md)
