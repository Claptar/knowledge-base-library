---
title: "32. Exponential Families"
course: "Berkeley Stat 210A"
chapter: 32
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 32. Exponential Families

## What this covers

Poisson, Normal, Binomial and Beta densities all turn out to be instances of one algebraic shape.
This chapter answers what that shape is, why so many families fall into it, and what falls out for
free once a family is written that way: the sufficient statistic, the mean and variance of that
statistic, its moment-generating function, and a precise notion of when the parameterization is
"as small as possible." It assumes the factorization theorem for sufficiency, the definition of a
moment-generating function, and comfort with differentiating under an integral sign.

## The exponential family form

An **$s$-parameter exponential family** is a family of distributions $\mathcal{P} = \{P_\eta : \eta \in \Xi\}$
with densities, with respect to a base measure $\mu$ on a sample space $\mathcal{X}$, of the form

$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x).$$

The pieces are:

- $\eta \in \Xi \subseteq \mathbb{R}^s$, the **natural parameter**.
- $T(x)$, an $s$-dimensional **sufficient statistic**. This is immediate from the factorization
  theorem: the density factors as $g_\eta(T(x)) \cdot h(x)$ with $g_\eta(t) = e^{\eta' t - A(\eta)}$,
  so all of the $\eta$-dependence runs through $T(x)$.
- $h(x) \ge 0$, the **base** (or **carrier**) **density**. It can always be absorbed into the base
  measure $\mu$ if one prefers.
- $A(\eta)$, the **log-partition function** (also: normalizing constant, cumulant generating
  function — see below). It is not a free choice: once $T$, $h$, and $\mu$ are fixed, $A$ is
  determined by requiring the density to integrate to $1$,
  $$A(\eta) = \log \left[ \int_{\mathcal{X}} e^{\eta' T(x)} h(x) \, d\mu(x) \right] \le \infty.$$

The **natural parameter space** is the set of $\eta$ for which this integral is actually finite,

$$\Xi_1 = \{\eta : A(\eta) < \infty\}.$$

A particular family $\mathcal{P}$ is free to use a strict subset $\Xi \subsetneq \Xi_1$, if scientific
considerations restrict which $\eta$ are plausible; $\Xi_1$ is just the largest set on which the
recipe produces a normalizable density. $A(\eta)$ is always convex, and consequently $\Xi_1$ is
always a convex set.

If $h$ is absorbed into $\mu$, the log-density becomes exactly linear in $T(x)$:
$$\log p_\eta(x) = \eta' T(x) - A(\eta) \qquad (\text{with respect to } h\,d\mu).$$
It is worth thinking of $T(x)$ as a basis: $\eta$ picks out a linear combination of the coordinates
of $T$, and that combination is the entire content of how $\eta$ enters the density.

This form is convenient exactly because multiplying or dividing densities in the family stays
simple:

- **Multiplying** densities — combining evidence from independent observations, or forming
  prior $\times$ likelihood in a Bayesian calculation — just adds exponents.
- **Dividing** densities — computing conditional probabilities, likelihood ratios, or relative
  densities — just subtracts them.

## A first example: Poisson, and why $n$ observations cost nothing

**Single observation.** For $X \sim \mathrm{Poisson}(\lambda)$,
$$p_\lambda(x) = \frac{\lambda^x e^{-\lambda}}{x!}, \qquad x = 0, 1, 2, \dots,$$
which rewrites as
$$p_\lambda(x) = \exp\{(\log\lambda)\, x - \lambda\} \cdot \frac{1}{x!}.$$
Reading off the pieces: $\eta(\lambda) = \log \lambda$, $T(x) = x$, $A(\eta) = \lambda = e^\eta$,
$h(x) = 1/x!$.

**$n$ i.i.d. observations.** For $X_1, \dots, X_n \overset{\text{iid}}{\sim} \mathrm{Poisson}(\lambda)$,
$$p_\lambda(x) = \prod_{i=1}^n \exp\{(\log\lambda)\, x_i - \lambda\} \frac{1}{x_i!} = \exp\Big\{(\log\lambda)\Big(\sum_i x_i\Big) - n\lambda\Big\} \prod_i \frac{1}{x_i!}.$$
So $\eta(\lambda) = \log\lambda$ is unchanged, $T(x) = \sum_i x_i$, $A(\eta) = n e^\eta$, and
$h(x) = \prod_i (1/x_i!)$.

**In general**, if $X_1, \dots, X_n$ are i.i.d. from a one-observation exponential family
$p_\eta^{(1)}(x) = e^{\eta' T^{(1)}(x) - A^{(1)}(\eta)} h^{(1)}(x)$, then
$$p_\eta(x) = \prod_{i=1}^n \exp\{\eta' T^{(1)}(x_i) - A^{(1)}(\eta)\} h^{(1)}(x_i) = \exp\Big\{\eta'\underbrace{\Big(\sum_i T^{(1)}(x_i)\Big)}_{T(x)} - \underbrace{n A^{(1)}(\eta)}_{A(\eta)}\Big\}\underbrace{\prod_i h^{(1)}(x_i)}_{h(x)}.$$
The natural parameter $\eta$ does not change with $n$, and — the point worth remembering — the
**dimension of $T(x)$ does not grow with $n$**: no matter how many observations arrive, an
$s$-dimensional sufficient statistic stays $s$-dimensional.

## Differential identities

Write the normalizing identity as
$$e^{A(\eta)} = \int e^{\eta' T(x)} h(x) \, d\mu(x). \qquad (*)$$

A great deal of useful structure comes from differentiating $(*)$ with respect to $\eta$ and
pulling the derivative inside the integral — which is not always legitimate, but is licensed here
by a standard result (Keener, Thm 2.4): for $f : \mathcal{X} \to \mathbb{R}$, let
$$\Xi_f = \Big\{\eta \in \mathbb{R}^s : \int |f|\, e^{\eta' T} h \, d\mu < \infty\Big\}.$$
Then $g(\eta) = \int f\, e^{\eta' T} h\, d\mu$ has continuous partial derivatives of all orders on
the interior $\Xi_f^\circ$, and they can be obtained by differentiating under the integral sign.
Taking $f \equiv 1$ shows $A(\eta)$ has all partial derivatives on $\Xi_1^\circ$.

**Differentiating once.** Differentiate $(*)$ with respect to $\eta_j$:
$$\frac{\partial}{\partial \eta_j} e^{A(\eta)} = \frac{\partial}{\partial \eta_j}\int e^{\eta' T(x)} h(x)\, d\mu(x)
\;\Longrightarrow\; e^{A(\eta)} \frac{\partial A}{\partial \eta_j}(\eta) = \int T_j(x)\, e^{\eta' T(x) - A(\eta)} h(x)\, d\mu(x).$$
The right side is exactly $\mathbb{E}_\eta[T_j(X)]$, so
$$\frac{\partial A}{\partial \eta_j}(\eta) = \mathbb{E}_\eta[T_j(X)] \qquad\Longrightarrow\qquad \nabla A(\eta) = \mathbb{E}_\eta[T(X)].$$

**Differentiating twice.** Differentiating $(*)$ again with respect to $\eta_k$ and using the
product rule on the left side,
$$e^{A(\eta)}\left(\frac{\partial^2 A}{\partial \eta_j \partial \eta_k} + \underbrace{\frac{\partial A}{\partial \eta_j}}_{\mathbb{E}[T_j]}\underbrace{\frac{\partial A}{\partial \eta_k}}_{\mathbb{E}[T_k]}\right) = \underbrace{\int T_j T_k\, e^{\eta' T - A(\eta)} h\, d\mu}_{\mathbb{E}[T_j T_k]},$$
so the cross term $\mathbb{E}[T_j]\mathbb{E}[T_k]$ subtracts off to leave
$$\frac{\partial^2 A}{\partial \eta_j \partial \eta_k}(\eta) = \mathrm{Cov}_\eta(T_j, T_k) \qquad\Longrightarrow\qquad \nabla^2 A(\eta) = \mathrm{Var}_\eta(T(X)) \in \mathbb{R}^{s\times s}.$$

So the log-partition function is a generating function for the moments of $T(X)$: its gradient is
the mean, and its Hessian is the variance — automatically a positive semi-definite matrix, which is
another way to see that $A$ is convex.

**Worked example: Poisson.** With $T(X) = X$ and $A(\eta) = e^\eta$ ($= \lambda$),
$$\mathbb{E}_\eta[X] = \frac{d}{d\eta} e^\eta = e^\eta = \lambda, \qquad \mathrm{Var}_\eta(X) = \frac{d^2}{d\eta^2} e^\eta = e^\eta = \lambda,$$
recovering the familiar fact that a Poisson's mean and variance coincide. The identities only work
this cleanly with respect to the **natural** parameter $\eta$; differentiating with respect to
$\lambda$ directly, rather than $\eta = \log\lambda$, gives the wrong answer.

## Moment- and cumulant-generating functions

The same trick that produced the mean and variance produces every moment of $T(X)$ at once: the
function
$$M_\eta^{T(X)}(u) = \mathbb{E}_\eta[e^{u' T(X)}]$$
is the moment-generating function of $T(X)$ when $X \sim P_\eta$, and it has a closed form directly
in terms of $A$:
$$M_\eta^{T(X)}(u) = \int e^{u' T} e^{\eta' T - A(\eta)} h\, d\mu = e^{A(\eta+u) - A(\eta)} \underbrace{\int e^{(\eta+u)'T - A(\eta+u)} h\, d\mu}_{=\,1} = e^{A(\eta+u) - A(\eta)}.$$
The underbraced integral is $1$ because it is the total mass of the density at parameter $\eta+u$
(so this requires $\eta + u \in \Xi_1$). This is useful both for extracting individual moments (by
differentiating $M$ at $u=0$, which is just differentiating $(*)$ $k$ times and dividing by
$e^{A(\eta)}$) and for finding the distribution of sums of independent random variables, since
mgfs of independent sums multiply.

The **cumulant-generating function** is
$$K_\eta^T(u) = \log M_\eta^T(u) = A(\eta + u) - A(\eta),$$
which is why $A$ is sometimes simply called the cumulant generating function of the family.

## Other parameterizations

It is often more natural to describe a family by some parameter $\theta$ other than $\eta$ itself
— $\theta$ might be the mean and variance of a Normal, say, rather than the two coordinates of its
natural parameter. Write
$$p_\theta(x) = e^{\eta(\theta)' T(x) - B(\theta)} h(x), \qquad B(\theta) = A(\eta(\theta)),$$
so all the machinery above still applies after substituting $\eta(\theta)$ for $\eta$. Many, many
distributions take this form, sometimes after some algebraic massaging.

**Worked example: Normal.** For $X \sim N(\mu, \sigma^2)$ with $\theta = (\mu, \sigma^2)$,
$$p_\theta(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(\mu - x)^2/2\sigma^2} = \exp\left\{\frac{\mu}{\sigma^2} x - \frac{1}{2\sigma^2} x^2 - \frac{\mu^2}{2\sigma^2} - \frac{1}{2}\log(2\pi\sigma^2)\right\},$$
giving
$$\eta(\theta) = \begin{pmatrix}\mu/\sigma^2 \\ -1/2\sigma^2\end{pmatrix}, \qquad T(x) = \begin{pmatrix}x \\ x^2\end{pmatrix}, \qquad h(x) = 1, \qquad B(\theta) = \frac{\mu^2}{2\sigma^2} + \frac{1}{2}\log(2\pi\sigma^2).$$
Writing the same density directly in terms of the natural parameter,
$$p_\eta(x) = e^{\eta'\binom{x}{x^2} - A(\eta)}, \qquad A(\eta) = \frac{-\eta_1^2}{4\eta_2} + \frac{1}{2}\log\left(\frac{-\pi}{\eta_2}\right).$$

**Worked example: Binomial.** For $X \sim \mathrm{Binomial}(n, \theta)$,
$$p_\theta(x) = \theta^x(1-\theta)^{n-x}\binom{n}{x} = \left(\frac{\theta}{1-\theta}\right)^x (1-\theta)^n \binom{n}{x} = \exp\left\{\log\left(\frac{\theta}{1-\theta}\right) x + n\log(1-\theta)\right\}\binom{n}{x},$$
so $T(x) = x$, $h(x) = \binom{n}{x}$, and the natural parameter is the **log odds**,
$$\eta(\theta) = \log\left(\frac{\theta}{1-\theta}\right).$$

**Worked example: Beta.** For $X \sim \mathrm{Beta}(\alpha, \beta)$,
$$p_{\alpha,\beta}(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)} = \exp\{\alpha \log x + \beta \log(1-x) - \log B(\alpha,\beta)\} \cdot \frac{1}{x(1-x)},$$
so
$$\eta = \begin{pmatrix}\alpha\\\beta\end{pmatrix}, \qquad T(x) = \begin{pmatrix}\log x \\ \log(1-x)\end{pmatrix}, \qquad h(x) = \frac{1}{x(1-x)}.$$

Practically every other named family one meets — Gamma, Multinomial, Dirichlet, Pareto, Wishart,
and more — is an exponential family too, by the same kind of rewriting.

## Interpretation: exponential tilting

The form $p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x)$ can be read as an **exponential tilt** of the
carrier density $h(x)$: start with $h(x)$, multiply it pointwise by $e^{\eta' T(x)}$, and
renormalize by dividing by $e^{A(\eta)}$. The coordinates of $T(x) = (T_1(x), \dots, T_s(x))$ span a
linear space of directions in which $h$ can be tilted, and $\Xi_1$ is exactly the set of tilts after
which renormalization is still possible (the integral stays finite).

This also shows the decomposition into $(\eta, T, h, A)$ is highly non-unique:

1. Only $\mathrm{span}(T_1, \dots, T_s)$ matters — replacing $T$ by any other basis of the same
   span, with a compensating linear change of $\eta$, gives the same family.
2. $h$ can always be absorbed into $\mu$ (setting $d\nu(x) = h(x)\, d\mu(x)$), so without loss of
   generality one can take $h(x) \equiv 1$.
3. A constant can be added to $T(x)$ (absorbed by $A$) without changing the family.

## The distribution of $T(X)$

Suppose $X \sim p_\eta(x) = e^{\eta'T(x) - A(\eta)}$ with respect to $\mu$ (taking $h \equiv 1$
without loss of generality, by the remark above). Then $T(X)$ itself is exponential-family
distributed, in its own natural coordinate:
$$T(X) \sim q_\eta(t) = e^{\eta' t - A(\eta)} \quad \text{with respect to } \nu,$$
where $\nu$ is the measure $\mu$ pushed forward through $T : \mathcal{X} \to \mathbb{R}^s$,
$$\nu(B) \triangleq \mu(\{x : T(x) \in B\}).$$
Indeed,
$$\mathbb{P}_\eta(T(X) \in B) = \int \mathbf{1}_B(T(x))\, e^{\eta'T(x) - A(\eta)}\, d\mu(x) = \int \mathbf{1}_B(t)\, e^{\eta' t - A(\eta)}\, d\nu(t).$$
This is simplest to see in the discrete case (restoring $h$): grouping the atoms of $x$ by their
common value of $T(x)$,
$$\mathbb{P}_\eta(T(X) = t) = \sum_{x\,:\,T(x)=t} e^{\eta' T(x) - A(\eta)} h(x)\,\mu(\{x\}) = e^{\eta' t - A(\eta)} \underbrace{\sum_{x\,:\,T(x)=t} h(x)\,\mu(\{x\})}_{\nu(\{t\})}.$$
The same $A(\eta)$ that normalizes $p_\eta$ also normalizes the induced density of $T(X)$ — a
consequence of the fact that $A$ was defined purely in terms of $T$, $h$ and $\mu$ in the first
place.

## Canonical and minimal form

The exponential-family structure is most transparent in **canonical form**, reached by three
reductions each justified above: take $T(x) = x$ (a sufficiency reduction — always legitimate), take
$h(x) \equiv 1$ (absorb $h$ into $\mu$), and parameterize by $\eta$ itself rather than some $\theta$.
Then
$$p_\eta(x) = e^{\eta' x - A(\eta)}.$$

A representation $p_\eta(x) = e^{\eta'T(x) - A(\eta)} h(x)$ is called **minimal** if neither $\eta$
nor $T(x)$ satisfies a nontrivial linear constraint: there is no $a \ne 0$ and $b \in \mathbb{R}$
with $\eta' a = b$ for every $\eta \in \Xi$, and no such $a, b$ with $T(x)'a = b$ holding
$P$-almost surely. If such a constraint exists, the family can be re-expressed as an exponential
family of some smaller dimension $r < s$ (by absorbing the constraint, as illustrated below).

**Minimality implies minimal sufficiency of $T$.** Recall the Lehmann–Scheffé criterion: $T$ is a
minimal sufficient statistic if, for every $x, y$, the likelihood ratio $\ell(\cdot; x) /
\ell(\cdot; y)$ is constant in the parameter if and only if $T(x) = T(y)$. The "if" direction holds
automatically from sufficiency; the content is the "only if" direction — that a constant
likelihood ratio forces $T(x) = T(y)$. For an exponential family in minimal form, suppose
$$\ell(\eta; x) - \ell(\eta; y) = \eta'\underbrace{(T(x) - T(y))}_{a}$$
is constant in $\eta$ (equal to some $c_{xy}$ not depending on $\eta$). Because the family is
minimal, there is no nontrivial linear constraint on $\Xi$, so the map $\eta \mapsto \eta' a$ is
non-constant on $\Xi$ unless $a = 0$: one can always find $\eta, \zeta \in \Xi$ with $\eta' a \ne
\zeta' a$, unless $a = 0$. So constancy forces $a = 0$, i.e. $T(x) = T(y)$, exactly as required.

**The converse is not true.** Reducing the dimension of $T(X)$ — writing the family with a smaller
sufficient statistic — may or may not throw away information about $X$ that is not captured by the
parameter; whether it does is a separate question from minimality of the representation. (The
lecture flagged a homework problem on the multinomial that makes this distinction concrete, but
that problem was not part of the material collected here.)

**Turning a non-minimal representation into a minimal one.** If $s = 2$ but $\Xi$ is confined to a
line $\eta = \eta_0 + \theta\gamma$, $\theta \in \Theta \subseteq \mathbb{R}$ — so that every $\eta
\in \Xi$ satisfies the linear constraint $\gamma_\perp' \eta = \gamma_\perp' \eta_0$ for the
direction $\gamma_\perp$ orthogonal to $\gamma$ — the representation collapses to a genuine
one-parameter family:
$$e^{\eta' T(x) - A(\eta)} h(x) = e^{\theta \underbrace{(\gamma' T(x))}_{\text{new }T(x)} - A(\eta_0 + \theta\gamma)} h(x).$$
The new sufficient statistic $\gamma' T(x)$ is one-dimensional, matching the one genuine degree of
freedom $\theta$.

<figure>
<svg viewBox="0 0 340 260" role="img" aria-label="The natural parameter space as a convex region in the eta-plane, with a full two-dimensional sub-family shown as minimal and a one-dimensional line through it shown as not minimal">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
    </marker>
    <marker id="arrowAccent" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="orangered"/>
    </marker>
  </defs>

  <line x1="40" y1="225" x2="315" y2="225" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="315" y="245" text-anchor="end" font-size="12" fill="currentColor">η₁</text>
  <line x1="40" y1="225" x2="40" y2="20" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="20" y="30" text-anchor="start" font-size="12" fill="currentColor">η₂</text>

  <ellipse cx="185" cy="130" rx="120" ry="90" fill="currentColor" fill-opacity="0.12" stroke="currentColor" stroke-width="1.5"/>
  <text x="290" y="55" text-anchor="end" font-size="12" fill="currentColor">Ξ₁</text>

  <line x1="95" y1="195" x2="278" y2="60" stroke="orangered" stroke-width="2.5" marker-end="url(#arrowAccent)"/>
  <circle cx="187" cy="127" r="4" fill="orangered"/>
  <text x="196" y="120" font-size="12" fill="currentColor">η₀</text>
  <text x="255" y="72" font-size="12" fill="currentColor">γ</text>

  <line x1="187" y1="127" x2="140" y2="160" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="108" y="172" font-size="11" fill="currentColor">γ⊥</text>

  <text x="115" y="90" font-size="12" fill="currentColor">(A) minimal</text>
  <text x="215" y="185" font-size="12" fill="currentColor">(B) minimal</text>
  <text x="250" y="95" font-size="12" fill="currentColor">(C) not minimal</text>
</svg>
<figcaption>The natural parameter space $\Xi_1 \subseteq \mathbb{R}^2$ is convex. Choosing $\Xi$ to
be either of the shaded two-dimensional regions (A) or (B) gives a minimal representation, since no
linear constraint holds on all of $\Xi$. Choosing $\Xi$ to be the line through $\eta_0$ in direction
$\gamma$ (C) is not minimal: every point on it satisfies $\gamma_\perp'\eta = \gamma_\perp'\eta_0$,
so it collapses to a one-dimensional family with sufficient statistic $\gamma' T(x)$.</figcaption>
</figure>

## Sources

- Handwritten lecture notes, Berkeley STAT 210A, fall 2024, lecture 5 ("Exponential Families"),
  reconstructed from PDF: `01-exponential-families.md` (the definition, natural parameter space,
  Poisson and generic-$n$-observation examples) and `02-differential-identities.md` (differential
  identities, MGF/CGF, other parameterizations with the Normal/Binomial/Beta examples, exponential
  tilting, the distribution of $T(X)$, canonical form, and minimality, including the minimal-vs-not
  diagram). Both files carry the conversion note that the source PDF had no text layer, so the
  prose is a model's paraphrase and every equation is otherwise unverified against the original
  scan.
- The equivalent fall-2025 and fall-2026 lecture-5 files (`fall-2025/handwritten/lecture05-exponentialfamilies.md`,
  `fall-2026/handwritten/lecture05-exponentialfamilies.md`) cover the same lecture but their
  conversions stop after the opening definition, matching the fall-2024 material as far as they go;
  they contributed nothing beyond it.
- The lecture referred to, but this material does not contain: Keener's *Theoretical Statistics*
  (cited by name as "Keener Thm 2.4" for the theorem licensing differentiation under the integral
  sign), a homework problem on the multinomial illustrating that a non-minimal-to-minimal reduction
  need not be a genuine data reduction, and the further worked-out forms of the Gamma, Multinomial,
  Dirichlet, Pareto and Wishart families ("practically everything else on Wikipedia too").

---

[← 31. Sufficiency and Minimal Sufficiency (part 1)](31-sufficiency-and-minimal-sufficiency-part-1.md) · [Contents](index.md) · [33. Completeness of Sufficient Statistics →](33-completeness-of-sufficient-statistics.md)
