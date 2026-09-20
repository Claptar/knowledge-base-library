---
title: "51. Nuisance Parameters and Conditioning"
course: "Berkeley Stat 210A Fall 2024"
chapter: 51
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 51. Nuisance Parameters and Conditioning

## What this covers

A testing problem often comes with an unknown parameter that is not itself the object of
interest — a variance, a baseline rate, a common effect size — but that can still corrupt the
level or the power of a test aimed at the parameter that *is* of interest. This chapter answers:
how do you build a UMP-unbiased (UMPU) test for $\theta$ when an unknown nuisance parameter
$\lambda$ is also present? The device is to pass to a sufficient statistic and then condition on
the part of it that carries $\lambda$, which strips $\lambda$ out of the conditional problem
entirely and leaves a one-parameter testing problem to which the previous lecture's theory
applies directly. The chapter closes by showing the same conditioning idea still pays off even
where it does not deliver a clean optimality theorem: permutation tests.

It assumes exponential families, sufficiency and completeness, and the one-parameter UMP and
UMPU theorems for exponential families from the preceding lecture (the Karlin–Rubin one-sided
theorem and the two-sided UMPU theorem, there attributed to Keener Thm. 12.22).

## Nuisance parameters

**Setup.** $\mathcal{P} = \{P_{\theta,\lambda} : (\theta,\lambda) \in \Omega\}$, and the hypotheses
concern only $\theta$: $H_0 : \theta \in \Theta_0$ vs $H_1 : \theta \in \Theta_1$. Call $\theta$ the
**parameter of interest** and $\lambda$ the **nuisance parameter**. The issue is that $\lambda$ is
unknown, and a test built without accounting for it can have level or power that depends on the
true (unknown) value of $\lambda$.

**Example.** $X_1,\dots,X_n \overset{\text{iid}}{\sim} N(\mu,\sigma^2)$ and
$Y_1,\dots,Y_m \overset{\text{iid}}{\sim} N(\nu,\sigma^2)$, with $\mu,\nu,\sigma^2$ all unknown, and
$$H_0 : \mu = \nu \quad\text{vs}\quad H_1 : \mu \ne \nu.$$
Here $\theta = \mu - \nu$ is the parameter of interest, and $\lambda = (\mu+\nu,\sigma^2)$ (or
equally $(\mu,\sigma^2)$) is the nuisance parameter: some reparametrization of everything the
hypotheses don't mention.

**A contrasting example.** $X_1 \sim \mathrm{Binom}(n_1,\pi_1)$, $X_2 \sim \mathrm{Binom}(n_2,\pi_2)$
independent, with $n_1,n_2$ *known*, testing $H_0:\pi_1\le\pi_2$ vs $H_1:\pi_1>\pi_2$. Because
$n_1,n_2$ are known constants rather than unknown model parameters, they are **not** nuisance
parameters at all — the point of the contrast is that a nuisance parameter has to be an unknown
parameter of the model, not merely a quantity the hypotheses don't refer to.

## Removing $\lambda$ by conditioning: multiparameter exponential families

Take $X \sim p_{\theta,\lambda}(x) = e^{\theta' t(x) + \lambda' u(x) - A(\theta,\lambda)} h(x)$,
with $\theta \in \mathbb{R}^s$ and $\lambda \in \mathbb{R}^r$, both unknown, and ask how to test
$H_0 : \theta \in \Theta_0$ vs $H_1 : \theta \in \Theta_1$.

The idea: condition on $U(X)$ to eliminate the dependence on $\lambda$.

**1) Sufficiency reduction.** $(T(X),U(X))$ has density (with respect to, e.g., Lebesgue measure on
$\mathbb{R}^{s+r}$)
$$q_{\theta,\lambda}(t,u) = e^{\theta' t + \lambda' u - A(\theta,\lambda)} g(t,u).$$

**2) Condition on $U(X)$.**
$$q_\theta(t\mid u) = \frac{q_{\theta,\lambda}(t,u)}{\int q_{\theta,\lambda}(z,u)\,dz}
= \frac{e^{\theta' t + \lambda' u - A(\theta,\lambda)} g(t,u)}
       {e^{\lambda' u - A(\theta,\lambda)} \int e^{\theta' z} g(z,u)\,dz}
= e^{\theta' t - B_u(\theta)} g(t,u),$$
where $B_u(\theta) = \log \int e^{\theta' z} g(z,u)\,dz$. The $\lambda$ in the exponent of the
denominator cancels exactly against the $\lambda$ in the numerator — this is the whole mechanism.
What is left, $q_\theta(t\mid u)$, is a family indexed by $\theta$ alone.

**3) Conditional test.** Now test $H_0:\theta\in\Theta_0$ vs $H_1:\theta\in\Theta_1$ inside the
$s$-parameter family $\mathcal{Q}_u = \{q_\theta(t\mid u) : \theta\}$. If $s=1$, $q_\theta(t\mid u)$
is a one-parameter exponential family in canonical form, so it automatically has monotone
likelihood ratio in $T$ — exactly the structure the previous lecture's UMP and UMPU theorems need.
Even when $s>1$ and no such clean theory is available, the conditioning step has still done its
job: $\lambda$ is gone from the problem.

## Theorem: the conditional test is UMPU

Let $\mathcal{P}$ be a full-rank exponential family with densities
$$p_{\theta,\lambda}(x) = e^{\theta T(x) + \lambda' U(x) - A(\theta,\lambda)} h(x), \qquad
\theta \in \mathbb{R}, \ \lambda \in \mathbb{R}^r, \ (\theta,\lambda) \in \Omega \text{ open},$$
and fix a possible value $\theta_0$.

**a) One-sided.** To test $H_0:\theta\le\theta_0$ vs $H_1:\theta>\theta_0$, there is a UMPU test
$\phi^*(x) = \psi(T(x);U(x))$ with
$$\psi(t;u) = \begin{cases} 1 & t > c(u) \\ \gamma(u) & t = c(u) \\ 0 & t < c(u), \end{cases}$$
where $c(u)$ and $\gamma(u)$ are chosen so that $\mathbb{E}_{\theta_0}[\phi^*(X) \mid U(X)=u] = \alpha$.

**b) Two-sided.** To test $H_0:\theta=\theta_0$ vs $H_1:\theta\ne\theta_0$, there is a UMPU test
$\phi^*(x)=\psi(T(x);U(x))$ with
$$\psi(t;u) = \begin{cases} 1 & t<c_1(u) \text{ or } t>c_2(u) \\ \gamma_i(u) & t=c_i(u) \\
0 & t \in (c_1(u),c_2(u)), \end{cases}$$
where $c_i(u),\gamma_i(u)$ are chosen so that
$$\mathbb{E}_{\theta_0}[\phi^*(X)\mid U(X)=u] = \alpha, \qquad
\mathbb{E}_{\theta_0}[T(X)(\phi^*(X)-\alpha)\mid U(X)=u] = 0.$$

In both cases the test is built entirely from $c(u),\gamma(u)$ (or $c_i,\gamma_i$) chosen
*conditionally on each value of $u$* — and, notably, $\lambda$ has disappeared from the problem: it
never appears in the definition of $\phi^*$, only $\theta_0$ and the data.

## Worked example: comparing two Poisson rates

$X_1,X_2$ independent, $X_i \sim \mathrm{Poisson}(\mu_i)$, and
$$H_0 : \mu_1 \le \mu_2 \quad\text{vs}\quad H_1 : \mu_1 > \mu_2.$$
Write $\eta_i = \log\mu_i$, so
$$p_\mu(x) = \prod_{i=1}^2 \frac{\mu_i^{X_i}e^{-\mu_i}}{X_i!}
= e^{X_1\eta_1 + X_2\eta_2 - (e^{\eta_1}+e^{\eta_2})}\frac{1}{X_1!X_2!}.$$
Regroup the exponent using $\eta_1 = (\eta_1-\eta_2) + \eta_2$:
$$X_1\eta_1 + X_2\eta_2 = \underbrace{X_1}_{T(X)}\underbrace{(\eta_1-\eta_2)}_{\theta}
+ \underbrace{(X_1+X_2)}_{u(x)}\underbrace{\eta_2}_{\lambda},$$
so $H_0:\theta\le 0$ vs $H_1:\theta>0$ is exactly the one-sided problem above, with $\lambda=\eta_2$
the nuisance parameter and $U = X_1+X_2$ the statistic to condition on. The prescription: reject
for **conditionally** large values of $X_1$, given $X_1+X_2=u$. Computing the conditional law,
$$P_\theta(X_1=x_1\mid U=u) \propto_{x_1} e^{x_1\theta}\binom{u}{x_1}
= \mathrm{Binom}\!\left(u,\ \frac{e^\theta}{1+e^\theta}\right)
= \mathrm{Binom}\!\left(u,\ \frac{\mu_1}{\mu_1+\mu_2}\right),$$
using $e^\theta = \mu_1/\mu_2$. So the theorem reduces this two-parameter comparison to an ordinary
one-sample binomial test of $p=\tfrac12$ against $p>\tfrac12$, run on $X_1$ given $X_1+X_2=u$ — with
no trace of $\mu_2$ (equivalently $\lambda$) left in the test.

## Why the theorem is true

The whole argument hinges on one boundary slice of the parameter space. Fix $\theta_0$ and look at
the set of $(\theta,\lambda) \in \Omega$ with $\theta = \theta_0$ — the **boundary submodel**. Any
unbiased test must have power exactly $\alpha$ everywhere on that slice, for every value of
$\lambda$: this is forced by continuity of the power function together with the level and power
constraints of unbiasedness. Restricted to that slice, the density is itself a full-rank
exponential family in $\lambda$ alone, with $U(X)$ complete sufficient for it — and completeness
is exactly the tool that turns "power $\equiv \alpha$ on the boundary, for every $\lambda$" into
"conditional power given $U=u$ equals $\alpha$, for every $u$": a statement with no $\lambda$ in it
at all.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="The parameter space Omega sliced at theta = theta0, separating the null and alternative regions from the boundary submodel used to eliminate lambda">
  <path d="M 90 40 C 60 55, 55 90, 60 120 C 65 160, 100 190, 150 195 C 200 200, 250 185, 270 150 C 290 115, 285 70, 250 45 C 210 15, 130 20, 90 40 Z"
        fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="1.3"/>
  <line x1="170" y1="10" x2="170" y2="210" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 4"/>
  <line x1="30" y1="205" x2="320" y2="205" stroke="currentColor" stroke-width="1.2"/>
  <text x="325" y="209" font-size="12" fill="currentColor">&#952;</text>
  <text x="176" y="222" font-size="12" fill="currentColor">&#952;&#8320;</text>
  <text x="100" y="105" font-size="12" fill="currentColor">H&#8320;: &#952;&#8804;&#952;&#8320;</text>
  <text x="100" y="122" font-size="12" fill="currentColor">power &#8804; &#945;</text>
  <text x="210" y="105" font-size="12" fill="currentColor">H&#8321;: &#952;&#62;&#952;&#8320;</text>
  <text x="210" y="122" font-size="12" fill="currentColor">power &#8805; &#945;</text>
  <text x="176" y="30" font-size="11" fill="currentColor">boundary submodel &#119970;&#952;&#8320;</text>
  <text x="176" y="44" font-size="11" fill="currentColor">power &#8801; &#945; for every &#955;</text>
  <text x="176" y="58" font-size="11" fill="currentColor">(U complete suff. here)</text>
</svg>
<figcaption>The boundary slice θ = θ₀ inside Ω: continuity and unbiasedness force the power of any
unbiased test to equal α everywhere on this slice, for every value of λ, and completeness of U
there converts that into a pointwise statement about conditional power given U = u.</figcaption>
</figure>

## Proof

Let $\phi$ be any unbiased test.

**Step 1 (regularity).** Since $\mathbb{E}_{\theta,\lambda}|\phi(X)| \le 1 < \infty$ for all
$(\theta,\lambda) \in \Omega$, a smoothness result for exponential families (Keener, Thm. 2.4) gives
that $\mathbb{E}_{\theta,\lambda}\phi(X)$ is infinitely differentiable on $\Omega$ and can be
differentiated under the integral sign. Unbiasedness then forces
$$\mathbb{E}_{\theta_0,\lambda}[\phi(X)] = \alpha \quad \text{for every } (\theta_0,\lambda) \in \Omega.$$

**Step 2 (descend to the boundary submodel).** Let
$\mathcal{P}_{\theta_0} = \{P_{\theta_0,\lambda} : (\theta_0,\lambda) \in \Omega\}$. Since
$$P_{\theta_0,\lambda}(x) = e^{\lambda' U(x) - A(\theta_0,\lambda)} \cdot e^{\theta_0 T(x)} h(x),$$
$\mathcal{P}_{\theta_0}$ is itself a full-rank, $r$-parameter exponential family in $\lambda$, with
$U(X)$ complete sufficient for it. Set $f(u) = \mathbb{E}_{\theta_0}[\phi(X)\mid U(X)=u] - \alpha$.
Then, by the tower property and Step 1,
$$\mathbb{E}_{\theta_0,\lambda}[f(U(X))] = \mathbb{E}_{\theta_0,\lambda}[\phi(X)] - \alpha = 0
\quad \text{for every } \lambda,$$
and completeness of $U$ forces $f(u) = 0$ almost surely, i.e.
$$\mathbb{E}_{\theta_0}[\phi(X)\mid U(X)=u] = \alpha \quad \text{for (almost) every } u.$$

*Two-sided case.* Differentiating in $\theta$ at $\theta_0$ the same way,
$$g(u) := \frac{d}{d\theta}\mathbb{E}_{\theta_0}[\phi \mid U=u]
= \mathbb{E}_{\theta_0}\big[(T - \mathbb{E}_{\theta_0}[T\mid U])\phi \,\big|\, U\big]
= \mathbb{E}_{\theta_0}[T(\phi-\alpha)\mid U],$$
and $\mathbb{E}_{\theta_0,\lambda}[g(U)] = \mathbb{E}_{\theta_0,\lambda}[T(\phi-\alpha)]
= \partial\beta_\phi(\theta_0)/\partial\theta = 0$ for every $\lambda$, since unbiasedness for a
two-sided test forces the power function to have a stationary point at $\theta_0$. Completeness
again gives $g(u) = 0$ a.s.: the conditional power given $U=u$ has derivative $0$ at $\theta_0$,
pointwise in $u$.

**Step 3 (solve the one-parameter problem inside each fiber, and Rao–Blackwellize).** Fix $u$. The
conditional model $q_\theta(t\mid u) = e^{\theta t - B_u(\theta)}g(t,u)$ is a genuine one-parameter
exponential family, with no nuisance parameter left in it, and Step 2 says $\psi(\cdot\,;u)$ (from
the theorem) is exactly the UMP (one-sided) or UMPU (two-sided) test of level $\alpha$ inside that
family — this is where the previous lecture's one-parameter theorem is used. Now let
$\bar\phi(t;u) = \mathbb{E}[\phi(X)\mid T(X)=t, U(X)=u]$: this is the Rao–Blackwellization of $\phi$
within the $(T,U)=(t,u)$ fiber. By the tower property,
$\mathbb{E}_{\theta_0}[\bar\phi(T;u)\mid U=u] = \mathbb{E}_{\theta_0}[\phi(X)\mid U=u] = \alpha$, so
$\bar\phi(\cdot\,;u)$ is itself a valid test in $\mathcal{Q}_u$, at conditional level $\alpha$ (and,
in the two-sided case, satisfying the same derivative-zero condition). Since $\psi$ is optimal
among such tests inside $\mathcal{Q}_u$, it has conditional power at least as large as $\bar\phi$,
almost surely in $u$.

**Assembling the inequality.** For any $(\theta,\lambda) \in \Omega_1$ (the alternative),
$$\mathbb{E}_{\theta,\lambda}[\phi(X)] = \mathbb{E}_{\theta,\lambda}\big[\mathbb{E}_\theta[\bar\phi(T;U)\mid U]\big]
\le \mathbb{E}_{\theta,\lambda}\big[\mathbb{E}_\theta[\psi(T;U)\mid U]\big]
= \mathbb{E}_{\theta,\lambda}[\phi^*(X)].$$
So $\phi^*$ has power at least as large as any unbiased $\phi$, everywhere on $H_1$: it is UMPU.

## Worked example: conditioning your way to the one-sample $t$-test

$X_1,\dots,X_n \overset{\text{iid}}{\sim} N(\mu,\sigma^2)$, $\sigma^2>0$ unknown, and
$$H_0 : \mu = 0 \quad\text{vs}\quad H_1 : \mu \ne 0.$$
Writing the density in canonical exponential-family form,
$$p_{\mu,\sigma^2}(x) = e^{\overbrace{\mu/\sigma^2}^{\theta}\,\overbrace{\textstyle\sum X_i}^{T\ (\propto\bar X)}
\ -\ \overbrace{1/(2\sigma^2)}^{\lambda}\,\overbrace{\textstyle\sum X_i^2}^{u=\|X\|^2}
\ -\ n\mu^2/(2\sigma^2)}\left(\frac{1}{2\pi\sigma^2}\right)^{n/2},$$
so $\theta = \mu/\sigma^2$ is the parameter of interest, $\lambda = -1/(2\sigma^2)$ the nuisance
parameter, $T=\sum X_i$ (equivalently $\bar X$) and $U = \|X\|^2$. The theorem says the optimal
test rejects when $\bar X$ is conditionally extreme given $\|X\|$.

Under $H_0$ ($\mu=0$), the density is rotationally symmetric, so $X/\|X\|$ is uniform on the unit
sphere $S^{n-1}$ and, crucially, independent of $\|X\|$. That independence means "extreme $\bar X$
given $\|X\|=$ fixed" and "extreme $\bar X/\|X\|$, unconditionally" pick out the same event: the
optimal test can equivalently be described as rejecting when $\bar X/\|X\|$ is *marginally* (not
just conditionally) extreme — a test that could, at this point, simply be simulated directly.

**From there to a familiar statistic.** Let $S^2 = \tfrac{1}{n-1}\sum(X_i-\bar X)^2
= \tfrac{1}{n-1}(\|X\|^2 - n\bar X^2)$. Then
$$T = \frac{\sqrt n\,\bar X}{\sqrt{S^2}} = \sqrt{n-1}\cdot\frac{R}{\sqrt{1-R^2}},
\qquad R = \frac{\sqrt n\,\bar X}{\|X\|} = \cos\sphericalangle(\mathbf 1_n, X),$$
and $r \mapsto r/\sqrt{1-r^2}$ is strictly increasing, so extreme $T$ and extreme $R$ are the same
event. Since $R$ is a function of $X/\|X\|$ alone, it is independent of $\|X\|$ — exactly the
marginal statistic the argument above called for. This $T$ is the ordinary one-sample $t$-statistic:
the conditioning argument, applied to the Gaussian location-scale family, *derives* the Student
$t$-test rather than assuming it.

<figure>
<svg viewBox="0 0 300 260" role="img" aria-label="Geometric picture for n=2 of the t statistic as a ratio of two orthogonal projection lengths">
  <circle cx="150" cy="140" r="90" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="55" y1="235" x2="245" y2="45" stroke="currentColor" stroke-width="1.3"/>
  <text x="228" y="55" font-size="12" fill="currentColor">1&#8345; (X&#8321;=X&#8322; line)</text>
  <line x1="150" y1="140" x2="205" y2="85" stroke="currentColor" stroke-width="2"/>
  <circle cx="205" cy="85" r="2.5" fill="currentColor"/>
  <text x="212" y="80" font-size="12" fill="currentColor">X</text>
  <line x1="150" y1="140" x2="187" y2="103" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="112" font-size="11" fill="currentColor">Proj&#8321;&#8345;X, len=&#8730;n X&#772;</text>
  <line x1="187" y1="103" x2="205" y2="85" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="196" y="72" font-size="11" fill="currentColor">Proj&#8869;X, len=&#8730;(n-1) S</text>
  <path d="M 180 130 A 20 20 0 0 1 168 116" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="163" y="140" font-size="11" fill="currentColor">&#8736;(1&#8345;,X)</text>
  <text x="150" y="255" text-anchor="middle" font-size="11" fill="currentColor">R = cos&#8736;(1&#8345;,X), T = &#8730;(n-1)&#183;R/&#8730;(1-R&#178;)</text>
</svg>
<figcaption>For n = 2: X decomposes into its projection onto the direction 1ₙ (length √n·X̄) and the
orthogonal complement (length √(n-1)·S); the t-statistic is their ratio, equivalently a function of
the angle between 1ₙ and X alone.</figcaption>
</figure>

The notes flag this picture as opening onto the next major theme — tests built from ratios of
projections — which this chapter does not develop further.

## Even without a UMPU test: permutation tests

Conditioning on a null-sufficient statistic is useful even when it does not deliver a UMPU
optimality theorem. Take the fully nonparametric two-sample problem:
$X_1,\dots,X_n \overset{\text{iid}}{\sim} P$, $Y_1,\dots,Y_m \overset{\text{iid}}{\sim} Q$,
$$H_0 : P=Q \quad\text{vs}\quad H_1 : P \ne Q.$$
Under $H_0$, all $n+m$ observations are iid from the common $P$. Pool them into
$Z = (X_1,\dots,X_n,Y_1,\dots,Y_m)$; under $H_0$ the order statistic
$U(Z) = (Z_{(1)},\dots,Z_{(n+m)})$ is complete sufficient, and, given $U(Z)$, the vector $Z$ is
uniformly distributed over its $(n+m)!$ coordinate permutations:
$$(X,Y) \mid U \overset{H_0}{\sim} \mathrm{Unif}\big(\{\pi U : \pi \in S_{n+m}\}\big).$$
So, for **any** test statistic $T$, if $P=Q$,
$$\mathbb{P}_{P,Q}\big(T(Z)\ge t \mid U\big)
= \frac{1}{(n+m)!}\sum_{\pi\in S_{n+m}} \mathbf 1\{T(\pi Z)\ge t\}.$$
This gives an exact conditional (hence exact, unconditionally, by the tower property) null
distribution for $T$, valid for *any* common $P$ — no parametric family and no UMPU theorem needed;
just the exchangeability that conditioning on the null-sufficient statistic buys.

**Monte Carlo test.** Computing over all $(n+m)!$ permutations is usually infeasible, so in
practice sample $\pi_1,\dots,\pi_B \overset{\text{iid}}{\sim} \mathrm{Unif}(S_{n+m})$ (e.g. $B=1000$).
Under $H_0$, $Z,\pi_1 Z,\dots,\pi_B Z$ are exchangeable draws from $\mathrm{Unif}(S_{n+m}U)$, so the
Monte Carlo $p$-value
$$p = \frac{1}{1+B}\sum_{b=1}^B \mathbf 1\{T(Z) \le T(\pi_b Z)\}$$
satisfies, under $H_0$ and with no ties, $p \sim \mathrm{Unif}\big(\{\tfrac{1}{1+B},\dots,\tfrac{B}{1+B},1\}\big)$
— an exactly calibrated discrete $p$-value from a fixed, affordable computational budget — and
$p$ is stochastically larger than this uniform law (conservative) if there are ties.

## Sources

All material in this chapter is from Berkeley Stat 210A, Fall 2024, handwritten lecture notes for
lecture 17 (dated 10/24/23 in the notes themselves), converted to markdown by a model from a
handwritten PDF with no text layer (route: llm, fidelity: reconstructed, CC BY 4.0):

- `01-outline.md` — nuisance parameters, the two opening examples, and the multiparameter
  exponential family / conditioning derivation.
- `02-theorem.md` — the UMPU theorem (parts a and b) and the two-Poisson worked example.
- `03-proof.md` — the full proof (Steps 1–3 and the final inequality), and the one-sample normal
  / $t$-statistic worked example with its geometric pictures.
- `04-permutation-tests.md` — the permutation-test section.

Because the source PDF had no text layer, its own header flags every equation as unverified against
the original scan; the algebra above was checked for internal consistency but not against the
handwritten page images. The proof cites two results from Keener's *Theoretical Statistics*
(Thm. 2.4, on differentiating an exponential family's moment generating function under the
integral, and Thm. 12.22, the two-sided UMPU theorem) without reproducing them; both are used as
black boxes in `03-proof.md`. The theorem itself leans on the previous lecture's one-parameter
UMP/UMPU results (`lecture15-F24`), which are assumed rather than restated here. The closing remark
in `03-proof.md` that the geometric picture "opens onto ratios of projections" points forward to
material this chapter does not contain.

---

[← 50. P-Values and Confidence Sets](50-p-values-and-confidence-sets.md) · [Contents](index.md) · [52. Multiparameter Exp. Families →](52-multiparameter-exp-families.md)
