---
title: "9. Exponential Family Structure"
course: "Berkeley Stat 210A"
chapter: 9
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Exponential Family Structure

## What this covers

This chapter introduces exponential families: a class of statistical models whose densities all
share one exponential form, and works out what that shared form buys you. It assumes familiarity
with densities taken with respect to a dominating measure, differentiating under an integral sign,
and the moment- and cumulant-generating functions of a random vector.

## The definition

A model $\mathcal P = \{P_\eta : \eta \in \Xi\}$ is an $s$-parameter exponential family if every
member has a density, with respect to some common dominating measure $\mu$ (i.e. $P_\eta \ll \mu$
for every $\eta$), of the form

$$p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x).$$

Four objects appear, each with a name:

- $T:\mathcal X\to\mathbb R^s$ — the **sufficient statistic**
- $h:\mathcal X \to [0,\infty)$ — the **carrier density** (or base density)
- $\eta \in \Xi \subseteq \mathbb R^s$ — the **natural parameter**
- $A:\Xi\to\mathbb R$ — the **log-partition function**

$A$ is not a free choice: it is whatever normalizes the density to integrate to 1,

$$A(\eta) = \log\left(\int_{\mathcal X} e^{\eta'T(x)}h(x)\,d\mu(x)\right) \le \infty.$$

If this integral diverges, $\eta$ cannot be a legal value of the natural parameter — there is no
way to normalize $p_\eta$. The **natural parameter space** $\Xi_1 = \{\eta : A(\eta)<\infty\}$
collects exactly the $\eta$ for which the family is well defined. It turns out to be a convex set,
because $A$ is a convex function (shown as an exercise in the course, not reproduced here).

**$h$ is not really extra structure.** Since $\mu$ can be any dominating measure, $h$ can always be
folded into it: replace $\mu$ by the measure $\nu$ with $d\nu = h\,d\mu$, and $P_\eta$ has density
$e^{\eta'T(x)}$ with respect to $\nu$ instead of $e^{\eta'T(x)}h(x)$ with respect to $\mu$. A
maximally parsimonious definition would drop $h$ entirely. It is kept in because it is convenient:
it lets $\mu$ be an ordinary counting or Lebesgue measure, so that $p_\eta$ reads as an everyday pmf
or pdf rather than forcing every statement through measure theory.

## Worked example: the Poisson family

The Poisson pmf $p_\lambda(x) = \lambda^x e^{-\lambda}/x!$ on $x=0,1,2,\dots$ does not look like an
exponential family until the exponent is rewritten:

$$p_\lambda(x) = \exp\{(\log\lambda)x - \lambda\}\frac{1}{x!}.$$

Setting $\eta = \log\lambda$ gives $p_\eta(x) = \exp\{\eta x - e^\eta\}\frac1{x!}$ — now visibly of
the canonical form, with $T(x)=x$, $h(x) = 1/x!$, and $A(\eta) = e^\eta$.

**The decomposition is not unique.** Take $T(x) = x/2$ instead: then $\eta = 2\log\lambda$ and
$A(\eta) = e^{\eta/2}$ — the same family, with a different sufficient statistic and natural
parameter. Or take $T(x) = x+1$, giving $A(\eta) = e^\eta + \eta$. In general, for any exponential
family, an invertible affine change of the sufficient statistic $S(x) = UT(x)+v$ (with
$U\in\mathbb R^{s\times s}$ invertible) reparameterizes to $\zeta = (U^{-1})'\eta$ and
$B(\zeta) = A(U'\zeta) + \zeta'v$, giving the identical density $e^{\zeta'S(x)-B(\zeta)}h(x)$. So
"the" sufficient statistic of an exponential family is only defined up to invertible affine
transformations: pinning down $T$ pins down $\eta$ and $A$ along with it, but there is no canonical
choice of $T$ itself.

## Differential identities: mean and variance from $A$

Exponentiate the normalizing identity to get $e^{A(\eta)} = \int_{\mathcal X}
e^{\eta'T(x)}h(x)\,d\mu(x)$, and differentiate both sides with respect to $\eta$. Differentiating
under the integral sign is not always legitimate, but it is valid on the interior of $\Xi_1$
(a fact attributed to Theorem 2.4 of Keener, cited in the source but not reproduced here).

Differentiating once, coordinate by coordinate,

$$
e^{A(\eta)}\frac{\partial A}{\partial \eta_j} = \int_{\mathcal X} T_j(x)\,e^{\eta'T(x)}h(x)\,d\mu(x)
\quad\Longrightarrow\quad
\frac{\partial A}{\partial \eta_j} = \mathbb E_\eta[T_j(X)],
$$

so, stacking the partials into a vector,

$$\nabla A(\eta) = \mathbb E_\eta[T(X)].$$

The gradient of the log-partition function hands you the mean of the sufficient statistic, with no
integral left to do.

Differentiate a second time and the cross terms produce a covariance:

$$
\frac{\partial^2 A}{\partial\eta_j\partial\eta_k}
= \mathbb E_\eta[T_j(X)T_k(X)] - \mathbb E_\eta[T_j(X)]\,\mathbb E_\eta[T_k(X)]
= \mathrm{Cov}_\eta(T_j(X),T_k(X)),
$$

i.e. $\nabla^2 A(\eta) = \mathrm{Var}_\eta(T(X))$: the Hessian of the log-partition function is the
variance-covariance matrix of $T(X)$.

**Why it has to be $\eta$ you differentiate with respect to, and not just any parameter.** For the
Poisson family, $T(X)=X$, $\eta=\log\lambda$, and $A(\eta)=e^\eta=\lambda$. Writing "$A(\eta) =
\lambda$" and differentiating with respect to $\lambda$ directly would give $\mathbb E[X] =
\partial\lambda/\partial\lambda = 1$ and $\mathrm{Var}(X) = 0$ — both nonsense. The identity
$\nabla A(\eta) = \mathbb E_\eta[T(X)]$ is a statement about $A$ as a function of the *natural*
parameter specifically; differentiating with respect to the wrong parameterization silently breaks
it.

## Moment- and cumulant-generating functions

For a $d$-dimensional random vector $X\sim P$, the moment generating function is $M^X(u) =
\mathbb E[e^{u'X}]$. Where it is well defined near $u=0$, its derivatives at $0$ recover the
moments of $X$, by the same differentiate-under-the-integral argument used above:

$$
\left.\frac{\partial^{m_1+\cdots+m_d}}{\partial u_1^{m_1}\cdots \partial u_d^{m_d}}M^X(u)
\right|_{u=0} = \mathbb E[X_1^{m_1}\cdots X_d^{m_d}].
$$

Two properties make the MGF useful beyond bookkeeping moments: it turns convolution into
multiplication ($M^{X+Y}(u) = M^X(u)M^Y(u)$ for independent $X,Y$), and it determines the
distribution — two random variables with the same MGF have the same law.

In an exponential family the MGF of the sufficient statistic is available in closed form:

$$
M_\eta^{T(X)}(u) = \mathbb E_\eta[e^{u'T(X)}]
= e^{-A(\eta)}\int_{\mathcal X} e^{(u+\eta)'T(x)}h(x)\,d\mu(x)
= e^{A(\eta+u)-A(\eta)}.
$$

**Worked example.** For $X\sim\mathrm{Pois}(\lambda)$ with $\eta=\log\lambda$, this gives
$M^X_\eta(u) = \exp\{e^{\eta+u}-e^\eta\} = \exp\{\lambda(e^u-1)\}$. Now suppose
$X_1,\dots,X_n$ are independent with $X_i\sim\mathrm{Pois}(\lambda_i)$, and the distribution of
$X_+=\sum_i X_i$ is wanted. Multiplying MGFs,

$$M^{X_+}(u) = \prod_i M^{X_i}_{\eta_i}(u) = \exp\left\{\sum_i \lambda_i(e^u-1)\right\},$$

which is exactly the MGF of $\mathrm{Pois}(\lambda_+)$ for $\lambda_+=\sum_i\lambda_i$ — so
$X_+\sim\mathrm{Pois}(\lambda_+)$, read off without ever summing a convolution.

The cumulant-generating function is $K^{T(X)}_\eta(u) = \log M^{T(X)}_\eta(u) = A(\eta+u)-A(\eta)$,
and its derivatives at $u=0$ give the cumulants of $T(X)$ (the first two of which are the mean and
variance already found above). Note that
$\left.\partial K^{T}_\eta(u)/\partial \eta_j\right|_{u=0} = \partial A(\eta)/\partial\eta_j$ —
which is why $A$ is sometimes loosely called "the CGF," even though it is strictly not the CGF of
$T(X)$ itself; that role belongs to $K^{T(X)}_\eta$.

## Other parameterizations

The natural parameter $\eta$ is rarely how a family is originally stated. If $\theta$ is some
other, more familiar parameter, write

$$p_\theta(x) = e^{\eta(\theta)'T(x) - B(\theta)}h(x), \qquad B(\theta) = A(\eta(\theta)).$$

The Poisson mean $\lambda$ is exactly this: $\eta(\lambda)=\log\lambda$, $B(\lambda)=\lambda$.

**Normal.** For $X\sim N(\mu,\sigma^2)$ with the usual parameter $\theta=(\mu,\sigma^2)$,

$$
p_\theta(x) = \exp\left\{\frac{\mu}{\sigma^2}x - \frac{1}{2\sigma^2}x^2 - \frac{\mu^2}{2\sigma^2}
- \frac12\log(2\pi\sigma^2)\right\},
$$

an exponential family with $T(x)=(x,x^2)$, $h(x)=1$, $\eta(\theta) = (\mu/\sigma^2,
-1/2\sigma^2)$, and $B(\theta) = \mu^2/2\sigma^2 + \frac12\log(2\pi\sigma^2)$. Writing $\mu,
\sigma^2$ in terms of $\eta_1,\eta_2$ gives the log-partition function in natural-parameter form:

$$A(\eta) = -\frac{\eta_1^2}{4\eta_2} + \frac12\log(-\pi/\eta_2).$$

So the Gaussian is *the* exponential family with $T(x)=(x,x^2)$ and $h(x)=1$ with respect to
Lebesgue measure on $\mathbb R$ — that pair of choices determines the family uniquely.

**Binomial.** $X\sim\mathrm{Binom}(n,\theta)$ has pmf $\theta^x(1-\theta)^{n-x}\binom nx$, which
rearranges to

$$p_\theta(x) = \exp\left\{x\log\left(\frac{\theta}{1-\theta}\right) - n\log(1-\theta)\right\}
\binom nx,$$

giving $T(x)=x$ and natural parameter $\eta = \log(\theta/(1-\theta))$ — the log-odds, or logit,
the quantity that logistic regression and its relatives model linearly.

**Beta.** $X\sim\mathrm{Beta}(\alpha,\beta)$ has pdf $x^{\alpha-1}(1-x)^{\beta-1}/B(\alpha,\beta)$,
i.e.

$$
p_{\alpha,\beta}(x) = \exp\{\alpha\log x + \beta\log(1-x) - \log B(\alpha,\beta)\}\cdot
\frac{1}{x(1-x)},
$$

an exponential family with $T(x) = (\log x, \log(1-x))$, $\eta=(\alpha,\beta)$, and carrier density
$h(x)=1/(x(1-x))$.

The same trick applies to most of the other standard named families — Gamma, multinomial,
Dirichlet, Pareto, and Wishart among them.

## Exponential tilting

$p_\eta(x) = e^{\eta'T(x)-A(\eta)}h(x)$ can be read as an operation on the carrier density $h$:
multiply by $e^{\eta'T(x)}$, which inflates the density wherever $\eta'T(x)$ is large relative to
elsewhere, then renormalize by $e^{-A(\eta)}$ to make it a probability distribution again. This is
the *exponential tilt* of $h$ by $\eta$: moving $\eta$ reweights the distribution toward the region
where the sufficient statistic is large in the direction $\eta$ points.

## Repeated sampling

If $X_1,\dots,X_n$ are i.i.d. draws from a one-observation exponential family
$p^{(1)}_\eta(x) = e^{\eta'T(x)-A(\eta)}h(x)$, the joint density of the whole sample is again an
exponential family:

$$
p_\eta(x) = \prod_{i=1}^n e^{\eta'T(x_i)-A(\eta)}h(x_i)
= \exp\left\{\eta'\sum_{i=1}^n T(x_i) - nA(\eta)\right\}\prod_{i=1}^n h(x_i),
$$

with the same natural parameter $\eta$, sufficient statistic $\sum_i T(X_i)$, carrier density
$\prod_i h(x_i)$, and log-partition function $nA(\eta)$.

The point to hold onto: the sufficient statistic $\sum_i T(X_i)$ stays $s$-dimensional no matter
how large $n$ gets. An arbitrarily large i.i.d. sample from an exponential family compresses,
without loss, into a fixed-dimension summary — a fact whose consequences for what sufficiency buys
you are picked up in the next lecture.

## Sources

- Berkeley STAT 210A course reader, "Exponential Families" (Will Fithian), section "Exponential
  family structure" — the definition, the Poisson example, and the affine-reparameterization
  argument. Supplied as four conversions of the same text (fall-2024, two fall-2025 conversions,
  fall-2026); the prose is identical across all four, differing only in conversion route and
  source URL, and is treated here as a single source.
- Same reader, "Differential identities" — the mean/variance identities $\nabla A$, $\nabla^2 A$;
  the Poisson-parameterization counterexample; the MGF/CGF of $T(X)$ and the Poisson-sum example.
- Same reader, "Other parameterizations" — the $\theta \to \eta(\theta)$ setup and the Normal,
  Binomial, and Beta examples.
- Same reader, "Repeated sampling from exponential families" — the i.i.d.-sample exponential
  family and its fixed-dimension sufficient statistic.
- Referred to by the reader but not supplied: Homework 1 of the course (proof that $A$ is convex),
  Theorem 2.4 of Keener's *Statistical Theory* (justifying differentiation under the integral
  sign), and a "Visualization of exponential tilting" page that the reader links to but which was
  not among the files provided — the reader's own exponential-tilting worked example is left
  unfinished in the source ("this is easiest to understand ... (need to finish)") and is
  reproduced above only as far as it goes.

---

[← 8. Statistical Models and Estimation](08-statistical-models-and-estimation.md) · [Contents](index.md) · [10. The Factorization Theorem →](10-the-factorization-theorem.md)
