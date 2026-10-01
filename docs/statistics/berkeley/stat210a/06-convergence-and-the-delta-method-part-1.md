---
title: "6. Convergence and the Delta Method (part 1)"
course: "Berkeley Stat 210A"
chapter: 6
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. Convergence and the Delta Method (part 1)

## What this covers

Everything in the course so far has been exact, finite-sample calculation, usually relying on some
special structure of the model (an exponential family, say) to make the computation possible. This
chapter opens the asymptotic toolkit used when that structure is absent: what it means for a
sequence of random variables to converge, in probability or in distribution; how convergence
survives continuous transformations and combinations of sequences; and the delta method, which
turns the limiting distribution of an estimator into the limiting distribution of a smooth function
of it. It assumes the definitions of a random variable, a distribution function and expectation,
and it uses without re-deriving the weak law of large numbers and the central limit theorem for
i.i.d. sums — those two facts are the engine every later result runs on.

## Why approximate at all

For a generic model, exact finite-sample calculations can be intractable or simply impossible. The
way out is to replace the exact problem with a simpler one that is easy to compute with, by taking
a limit as the number of observations $n \to \infty$. The limit that appears almost everywhere is
Gaussian. This move is only useful, though, if the Gaussian approximation is actually good at the
sample sizes met in practice — the asymptotic statement is the tool, not the goal.

## Two kinds of convergence

Let $X_1, X_2, \ldots \in \mathbb{R}^d$ be a sequence of random vectors. Two different senses in
which such a sequence can "converge" recur throughout the subject.

**Convergence in probability.** $X_n$ converges in probability to a constant $c \in \mathbb{R}^d$,
written $X_n \xrightarrow{p} c$, if

$$
\mathbb{P}(\|X_n - c\| > \epsilon) \to 0 \quad \text{for every } \epsilon > 0.
$$

(The norm here could be any distance on any space $\mathcal{X}$ — nothing below is special to
$\mathbb{R}^d$.) This is a statement that the *mass* of $X_n$ concentrates at $c$; it says nothing
about any particular realization of $X_n$. One can also define convergence in probability to a
random variable rather than a constant, but that generality is not needed here.

**Convergence in distribution.** $X_n$ converges in distribution to a random variable $X$, written
$X_n \xrightarrow{d} X$, if

$$
\mathbb{E}[f(X_n)] \to \mathbb{E}[f(X)] \quad \text{for every bounded continuous } f : \mathcal{X} \to \mathbb{R}.
$$

This is also called *weak convergence*. Notice that the definition is entirely about the
*distributions* (laws) of $X_n$ and $X$ — it makes sense even if $X_n$ and $X$ are not defined on
the same probability space, unlike convergence in probability.

For real-valued sequences this abstract definition has a concrete, checkable form. If
$F_n(x) = \mathbb{P}(X_n \le x)$ and $F(x) = \mathbb{P}(X \le x)$, then

$$
X_n \xrightarrow{d} X \iff F_n(x) \to F(x) \text{ for every } x \text{ at which } F \text{ is continuous.}
$$

The restriction to continuity points of $F$ is not a technicality to skip past — it is exactly what
the following example is built to test.

Consider a sequence with

$$
F_n(x) = \begin{cases} 1 & x > 0 \\ 1 - \frac{1}{n} & x = 0 \\ 0 & x < 0 \end{cases}
\qquad\text{compared against}\qquad
F(x) = \begin{cases} 1 & x > 0 \\ 0 & x \le 0. \end{cases}
$$

Away from $x = 0$ the two functions already agree for every $n$, and at $x=0$ itself
$F_n(0) = 1 - \tfrac1n \to 1 \ne F(0)$. So pointwise convergence of $F_n$ to $F$ fails exactly at
$x = 0$ — but $x=0$ is precisely the point where the limit places its atom, i.e. the one point at
which $F$ is *not* continuous. The theorem above never asked for convergence there, so this failure
does not stand in the way of $X_n \xrightarrow{d} X$. The moral: weak convergence is a statement
about where the mass ends up, and it is deliberately indifferent to what happens exactly at an atom
of the limit.

## Convergence in probability and in distribution to a constant coincide

Convergence in probability is the stronger notion in general, but when the target is a *constant*
the two notions agree: $X_n \xrightarrow{p} c \iff X_n \xrightarrow{d} c$. This is worth proving
because the argument is the standard bridge between the two definitions, and it is reused
constantly.

One direction is immediate given the right test function. Let

$$
f_\epsilon(x) = \max\left\{1 - \frac{\|x - c\|}{\epsilon}, 0\right\},
$$

a "tent" that equals $1$ at $c$, decreases linearly to $0$ as $\|x-c\|$ reaches $\epsilon$, and is
identically $0$ beyond that — bounded and continuous by construction. Because
$\mathbf{1}\{\|x-c\|>\epsilon\} \le 1 - f_\epsilon(x)$ pointwise (both sides equal $1$ once
$\|x-c\|>\epsilon$, and the right side is nonnegative otherwise), if $X_n \xrightarrow{d} c$ then
in particular $\mathbb{E}[f_\epsilon(X_n)] \to f_\epsilon(c) = 1$, so

$$
\mathbb{P}(\|X_n - c\| > \epsilon) \le \mathbb{E}[1 - f_\epsilon(X_n)] \to 0,
$$

which is exactly $X_n \xrightarrow{p} c$.

The other direction needs a genuine argument, because it has to work for *every* bounded continuous
$f$, not just the tent function. Suppose $X_n \xrightarrow{p} c$ and fix a bounded continuous $f$.
By continuity, for every $\epsilon>0$ there is $\delta>0$ with $\|x-c\|<\delta \implies
|f(x)-f(c)|<\epsilon$. Split the expectation on whether $X_n$ is within $\delta$ of $c$:

$$
|\mathbb{E}[f(X_n)] - f(c)| \le \big|\mathbb{E}[(f(X_n)-f(c))\mathbf{1}\{\|X_n-c\|<\delta\}]\big|
+ \big|\mathbb{E}[(f(X_n)-f(c))\mathbf{1}\{\|X_n-c\|\ge\delta\}]\big|
\le \epsilon + 2\sup|f|\cdot \mathbb{P}(\|X_n-c\|\ge\delta).
$$

The first term is at most $\epsilon$ by the choice of $\delta$; the second $\to 0$ as $n\to\infty$
because $X_n \xrightarrow{p} c$, using boundedness of $f$ to control the piece where $X_n$ is far
from $c$. Since $\epsilon$ was arbitrary, $\mathbb{E}[f(X_n)] \to f(c)$ for every bounded continuous
$f$, i.e. $X_n \xrightarrow{d} c$. $\blacksquare$

**Consistency.** This equivalence is what sits behind the definition of a consistent estimator. In
a sequence of statistical models $\mathcal{P}_n = \{P_{n,\theta} : \theta \in \Theta\}$ with
$X_n \sim P_{n,\theta}$, an estimator sequence $\hat\theta_n$ is *consistent* for $g(\theta)$ if
$\hat\theta_n \xrightarrow{p} g(\theta)$, i.e.

$$
\mathbb{P}_\theta(|\hat\theta_n - g(\theta)| > \epsilon) \to 0 \quad \text{for every } \epsilon>0.
$$

(The index $n$ on $\theta$ and on the model is usually dropped once the sequence is understood.)

## The two facts everything else is built from

Let $\bar X_n = \frac1n\sum_{i=1}^n X_i$ for i.i.d. $X_i$.

**Law of large numbers.** If $\mathbb{E}|X_i|<\infty$ and $\mathbb{E}X_i = \mu$, then
$\bar X_n \xrightarrow{p} \mu$.

**Central limit theorem.** If $\mathrm{Var}(X_i) = \sigma^2 < \infty$, then
$\sqrt n(\bar X_n - \mu) \xrightarrow{d} N(0,\sigma^2)$.

Stronger versions of both exist, but these will be enough for everything that follows: the LLN
supplies the constants that things converge *to*, and the CLT supplies the Gaussian fluctuation
*around* them.

## The continuous mapping theorem

Convergence — of either kind — passes through continuous functions.

> **Theorem.** Let $g$ be continuous and $X_n, X$ random variables.
> 1. If $X_n \xrightarrow{d} X$, then $g(X_n) \xrightarrow{d} g(X)$.
> 2. If $X_n \xrightarrow{p} c$, then $g(X_n) \xrightarrow{p} g(c)$.

The proof is one line once the definitions are in hand: if $f$ is bounded and continuous, so is
$f \circ g$ (composition of continuous functions is continuous, and $f\circ g$ inherits $f$'s
bound). So $X_n \xrightarrow{d} X$ gives $\mathbb{E}[f(g(X_n))] \to \mathbb{E}[f(g(X))]$ for every
such $f$, which is exactly $g(X_n) \xrightarrow{d} g(X)$. Part 2 is the special case $X \equiv c$,
using the equivalence proved above.

## Slutsky's theorem

Continuous mapping handles a single sequence; Slutsky's theorem handles *combining* two.

> **Theorem (Slutsky).** Suppose $X_n \xrightarrow{d} X$ and $Y_n \xrightarrow{p} c$. Then
> 1. $X_n + Y_n \xrightarrow{d} X + c$,
> 2. $X_n Y_n \xrightarrow{d} cX$,
> 3. $X_n / Y_n \xrightarrow{d} X/c$ if $c \ne 0$.

The proof reduces to the continuous mapping theorem: one shows the pair converges jointly,
$(X_n, Y_n) \xrightarrow{d} (X, c)$, and then applies continuous mapping to the appropriate
continuous map (addition, multiplication, or division).

The one nonnegotiable hypothesis is that the *second* sequence converges to a **constant** in
probability. It would not, in general, be true that $X_n \xrightarrow{d} X$ and
$Y_n \xrightarrow{d} Y$ together imply $X_n + Y_n \xrightarrow{d} X + Y$: without knowing the joint
distribution of $(X_n, Y_n)$, the limiting sum could be almost anything, because the two marginal
limits say nothing about how $X_n$ and $Y_n$ move together. Slutsky's theorem escapes that trap only
because the nuisance sequence collapses to a single point, which removes any question of joint
dependence.

## The delta method

The delta method answers: if $X_n$ is asymptotically normal, what is the asymptotic distribution of
a smooth function of $X_n$?

> **Theorem (Delta method).** If $\sqrt n (X_n - \mu) \xrightarrow{d} N(0,\sigma^2)$ and $f$ is
> differentiable at $x=\mu$, then
> $$
> \sqrt n \big(f(X_n) - f(\mu)\big) \xrightarrow{d} N\big(0, [f'(\mu)]^2 \sigma^2\big).
> $$

Informally — treating "$X \sim N(\mu,\sigma^2/n)$" as shorthand for the CLT statement above — this
says $f(X) \sim N\big(f(\mu), [f'(\mu)]^2\sigma^2/n + o(1/n)\big)$: transforming an approximately
Gaussian quantity by a smooth $f$ gives back an approximately Gaussian quantity, with the variance
scaled by the square of the local slope of $f$.

**Why it is true.** Write the first-order Taylor expansion of $f$ around $\mu$:

$$
f(X_n) = f(\mu) + f'(\mu)(X_n - \mu) + o(X_n - \mu).
$$

Multiplying through by $\sqrt n$,

$$
\sqrt n\big(f(X_n)-f(\mu)\big) = f'(\mu)\sqrt n (X_n-\mu) + \sqrt n \, o(X_n - \mu).
$$

The first term converges in distribution to $N(0, [f'(\mu)]^2\sigma^2)$, by the continuous mapping
theorem applied to $\sqrt n(X_n-\mu) \xrightarrow{d} N(0,\sigma^2)$ and the linear map
$x \mapsto f'(\mu) x$. The second term vanishes in probability, because $X_n - \mu = O_p(n^{-1/2})$
(it is $\sqrt n$-scaled and convergent) while the remainder is $o(X_n-\mu)$, so the whole term is
$o_p(1)$. Adding a term converging to $0$ in probability to a term converging in distribution, by
Slutsky, gives the stated limit.

<figure>
<svg viewBox="0 0 320 230" role="img" aria-label="A smooth increasing curve near a point mu, together with its tangent line, showing how a small interval on the x-axis maps to an interval on the y-axis">
  <line x1="40" y1="210" x2="300" y2="210" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="210" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="300" y="225" text-anchor="end" font-size="12" fill="currentColor">x</text>
  <text x="25" y="25" text-anchor="end" font-size="12" fill="currentColor">f(x)</text>

  <rect x="131" y="204" width="78" height="6" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <rect x="34" y="92" width="6" height="60" fill="currentColor" fill-opacity="0.15" stroke="none"/>

  <line x1="131" y1="210" x2="131" y2="152" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="131" y1="152" x2="40" y2="152" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="209" y1="210" x2="209" y2="92" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="209" y1="92" x2="40" y2="92" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>

  <path d="M 66,183 Q 170,147 274,23" fill="none" stroke="currentColor" stroke-width="2"/>

  <line x1="113" y1="169" x2="227" y2="81" stroke="currentColor" stroke-width="1.5" stroke-dasharray="6,3"/>

  <circle cx="170" cy="125" r="3" fill="currentColor"/>
  <line x1="170" y1="125" x2="170" y2="210" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>
  <line x1="170" y1="125" x2="40" y2="125" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2"/>

  <text x="170" y="224" text-anchor="middle" font-size="12" fill="currentColor">μ</text>
  <text x="30" y="129" text-anchor="end" font-size="12" fill="currentColor">f(μ)</text>
  <text x="230" y="75" text-anchor="start" font-size="11" fill="currentColor">tangent, slope f'(μ)</text>
  <text x="195" y="45" text-anchor="start" font-size="12" fill="currentColor">y = f(x)</text>
</svg>
<figcaption>Near μ, f is well approximated by its tangent line: a small spread of X_n around μ
(shaded on the x-axis) is carried by f into a spread of f(X_n) around f(μ) (shaded on the y-axis)
whose width scales, to first order, by f′(μ) — the local linearization the delta method makes
precise.</figcaption>
</figure>

**The multivariate version.** If $\sqrt n(X_n - \mu) \xrightarrow{d} N(0,\Sigma)$ for
$X_n \in \mathbb{R}^d$, and $f : \mathbb{R}^d \to \mathbb{R}^k$ has derivative (Jacobian)
$Df(\mu)$ existing at $\mu$, then

$$
\sqrt n\big(f(X_n) - f(\mu)\big) \xrightarrow{d} N\big(0, \; Df(\mu)\, \Sigma \, Df(\mu)^T\big),
$$

with the same "instant" reading when $k=1$: $f(X) \sim N\big(f(\mu), Df(\mu)\Sigma Df(\mu)^T/n +
o(1/n)\big)$.

### Worked example: the ratio of two sample means

Let $X_1,\ldots,X_n \sim \mathrm{Unif}[0,\theta]$ i.i.d. and, independently,
$Y_1,\ldots,Y_m \sim \mathrm{Unif}[0,\theta]$ i.i.d. For large $n,m$, what is the distribution of
$T_n = \bar X / \bar Y$?

By the CLT, $\sqrt n(\bar X - \theta/2) \xrightarrow{d} N(0, \theta^2/12)$ and
$\sqrt m(\bar Y - \theta/2) \xrightarrow{d} N(0,\theta^2/12)$ (the variance of $\mathrm{Unif}[0,\theta]$
is $\theta^2/12$). Since both means converge to $\theta/2$,

$$
T_n = \frac{\bar X}{\bar Y} = \frac{\theta/2}{\theta/2} = 1 + O_p\big(n^{-1/2} + m^{-1/2}\big).
$$

Apply the multivariate delta method to the pair $(\bar X, \bar Y)$ with $f(x,y) = x/y$. The partial
derivatives at $(\theta/2,\theta/2)$ are

$$
f'_x\left(\tfrac\theta2,\tfrac\theta2\right) = \frac{1}{\theta/2} = \frac2\theta, \qquad
f'_y\left(\tfrac\theta2,\tfrac\theta2\right) = -\frac{\theta/2}{(\theta/2)^2} = -\frac2\theta,
$$

so the gradient is $f'\left(\tfrac\theta2,\tfrac\theta2\right) = \left(\tfrac2\theta,
-\tfrac2\theta\right)$. Applying the "instant" delta-method heuristic directly to $\bar X$ and
$\bar Y$ (independent, so no covariance term) gives

$$
T_n \approx N\left(1, \ \frac{4}{\theta^2}\cdot\frac{\theta^2}{12n} + \frac{4}{\theta^2}\cdot\frac{\theta^2}{12m}\right)
= N\left(1, \ \frac{1}{3n} + \frac{1}{3m}\right).
$$

A more careful accounting of the two different sample sizes in the $\sqrt n$-scaled limit gives

$$
\sqrt n (T_n - 1) \xrightarrow{d} N\left(0, \ \frac43\left(1 + \frac{n}{m}\right)\right).
$$

### When the derivative vanishes: a second-order delta method

The delta method as stated is useless when $f'(\mu) = 0$: the leading term of the Taylor expansion
disappears and the theorem would (wrongly) suggest a degenerate, zero-variance limit. Suppose $T_n$
has the shape seen above but now centered so that both pieces have mean $0$:

$$
T_n = \frac{1 + O_p(n^{-1/2})}{1 + O_p(m^{-1/2})} = 1 + O_p\big(n^{-1/2}+m^{-1/2}\big).
$$

Since $1/(1+n^{-1/2}) \to 1$, the fact that $T_n \xrightarrow{p} 1$ is just the continuous mapping
theorem applied to a ratio of two sequences each converging in probability — not Slutsky, which
needs a limit that is already known to be nondegenerate in distribution on one side. If the
$\sqrt n$-scaled fluctuation of $T_n$ around $1$ is itself asymptotically standard normal,
$\sqrt n (T_n - 1) \xrightarrow{d} Z \sim N(0,1)$, then squaring — again continuous mapping —
gives

$$
n(T_n - 1)^2 \xrightarrow{d} Z^2 \sim \chi^2_1.
$$

Why does the ordinary delta method not produce this directly? Apply it (naively) to
$g(t) = (t-1)^2$ at $t=1$: $g'(1) = 2(1-1) = 0$, so the first-order term is exactly the degenerate
case the delta method cannot handle. The fix is to carry the Taylor expansion one order further:

$$
f(X_n) = f(\mu) + f'(\mu)(X_n-\mu) + \tfrac12 f''(\mu)(X_n-\mu)^2 + O_p(n^{-3/2}).
$$

When $f'(\mu) = 0$, the first-order term drops out and the *second*-order term dominates, at rate
$n$ rather than $\sqrt n$:

$$
n\big(f(X_n) - f(\mu)\big) \xrightarrow{d} \tfrac12 f''(\mu) \, \chi^2_1.
$$

Checking this against the example: $g(t)=(t-1)^2$ has $g''(1) = 2$, so the formula gives
$n(T_n-1)^2 \xrightarrow{d} \tfrac12\cdot 2 \cdot \chi^2_1 = \chi^2_1$, matching the direct
calculation above. In general, whenever the first derivative of the transformation vanishes at the
point of interest, the limit is a (scaled) chi-squared rather than a normal, and it appears at the
faster rate $n$ instead of $\sqrt n$.

## Sources

- Berkeley STAT 210A course reader, "Asymptotic Theory: Convergence, Continuous Mapping, and Delta
  Method." Two parallel conversions of the same reader chapter were supplied and used together:
  the fall-2025 reader (`reader/convergence.html`, split into
  `fall-2025/reader/convergence/01-introduction.md`, `02-2-convergence.md`, `03-5-delta-method.md`,
  duplicated verbatim at `fall-2025/units/reader/convergence/`) and the fall-2026 reader
  (`reader/convergence.qmd`, split into `fall-2026/reader/convergence/01-convergence.md` and
  `02-delta-method.md`), both licensed CC BY 4.0. The two versions cover identical material with
  the section breaks drawn slightly differently; nothing in one that is absent from the other.
  - Motivation for asymptotics ("why approximate at all"): `01-introduction.md` / the opening of
    `01-convergence.md`.
  - Convergence in probability, convergence in distribution, the CDF criterion, the atom example,
    the proof that convergence in probability and in distribution to a constant coincide,
    consistency, the LLN and CLT, the continuous mapping theorem, and Slutsky's theorem:
    `02-2-convergence.md` / the remainder of `01-convergence.md`.
  - The delta method (univariate and multivariate statements, the uniform-ratio worked example,
    and the second-order delta method when the derivative vanishes): `03-5-delta-method.md` /
    `02-delta-method.md`.
- No slides, transcript, or exercise set were supplied for this chapter; the source is a written
  course reader rather than a recorded lecture, and no problems were provided to convert into an
  Exercises section.

---

[← 5. Completeness](05-completeness.md) · [Contents](index.md) · [7. Gaussian sequence model →](07-gaussian-sequence-model.md)
