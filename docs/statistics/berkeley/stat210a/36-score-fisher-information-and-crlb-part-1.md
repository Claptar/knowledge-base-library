---
title: "36. Score, Fisher Information, and CRLB (part 1)"
course: "Berkeley Stat 210A Fall 2024"
chapter: 36
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 36. Score, Fisher Information, and CRLB (part 1)

## What this covers

This chapter answers: given a statistical model $\{p_\theta\}$, how much does one observation tell
you about the parameter $\theta$, and what does that translate into as a hard lower bound on the
variance of *any* unbiased estimator? The tool built to answer it is the **score function** and its
variance, the **Fisher information**; the payoff is the **Cramér–Rao lower bound** and the notion
of **efficiency** it defines. It assumes the reader already has the canonical form of an exponential
family — the cumulant function $A(\eta)$ and the identities $\nabla A(\eta) = \mathbb{E}_\eta T(X)$,
$\nabla^2 A(\eta) = \operatorname{Var}_\eta(T(X))$ — and the fact that a full-rank exponential
family has a complete sufficient statistic, both of which motivate the definition below. Basic
multivariate calculus (differentiating under an integral sign) and the Cauchy–Schwarz inequality
for covariances are used without further comment, as the lecture does.

## Warm-up: a curved family and its tangent line

Start from a one-parameter family embedded in a two-dimensional exponential family,

$$p_\theta(x) = e^{\eta(\theta)'T(x) - A(\eta(\theta))} h(x), \qquad \eta : \mathbb{R} \to \mathbb{R}^2,$$

so that as $\theta$ ranges over $\mathbb{R}$, the canonical parameter traces a curve
$\Xi = \{\eta(\theta) : \theta \in \mathbb{R}\}$ in $\mathbb{R}^2$. If that curve happens to be a
straight line, $\eta(\theta) = \eta_0 + \theta\delta$, the family is an honest one-parameter
exponential family in $\theta$ with $T(x)$ replaced by the sufficient statistic $\delta'T(x)$, which
is complete by the usual full-rank theory. If the curve is genuinely nonlinear — a **curved**
family — no single fixed statistic plays that role globally, because the "direction" that matters
changes as $\theta$ moves.

Locally, though, every smooth curve looks like its tangent line. Fix $\theta_0$ and replace the
curve by the tangent family

$$\Xi_{\theta_0} = \{\eta(\theta_0) + \varepsilon\,\dot\eta(\theta_0) : \varepsilon \in \mathbb{R}\},
\qquad \dot\eta(\theta_0) = \frac{d\eta}{d\theta}(\theta_0),$$

a genuine straight line through $\eta(\theta_0)$ in the direction of the curve's velocity there.
Substituting into the exponential family form and expanding,

$$q_\varepsilon(x) = e^{(\eta(\theta_0) + \varepsilon\dot\eta(\theta_0))'T(x) - A(\cdot)}h(x)
= e^{\varepsilon\,\dot\eta(\theta_0)'(T(x) - \mathbb{E}_{\theta_0}T) - B(\varepsilon)} k(x),$$

where everything not depending on $\varepsilon$ has been absorbed into $k(x)$. Centering $T(x)$ at
its mean under $\theta_0$ is what turns this into a clean one-parameter canonical form in
$\varepsilon$: the quantity

$$S_{\theta_0}(x) = \dot\eta(\theta_0)'\big(T(x) - \mathbb{E}_{\theta_0}T\big)$$

is the natural sufficient statistic of the tangent family, hence complete sufficient for it. This is
the object the lecture names the **score function**. The name will turn out to be exactly right: the
general definition below reduces to this same expression once the curved family is written out in
full, in the section on curved families near the end of the chapter.

## The score function

Assume $\mathcal{P} = \{p_\theta : \theta \in \Theta\}$, $\Theta \subseteq \mathbb{R}^d$, has
densities $p_\theta$ with respect to a common dominating measure $\mu$, with **common support**:
the set $\{x : p_\theta(x) > 0\}$ does not depend on $\theta$. Write the log-likelihood

$$\ell(\theta; x) = \log p_\theta(x),$$

thought of as a random function of $\theta$ (through $x$) for the purposes of taking expectations,
and as an ordinary function of $\theta$ when differentiating.

**Definition.** The **score** is $\nabla\ell(\theta; x)$, the gradient with respect to $\theta$. It
plays a central role across statistics, especially in asymptotic theory.

The score can be read as a "local complete sufficient statistic": for $\tau$ near $0$,

$$p_{\theta_0 + \tau}(x) = e^{\ell(\theta_0 + \tau; x)} \approx e^{\tau'\nabla\ell(\theta_0; x)}\,
p_{\theta_0}(x),$$

by a first-order Taylor expansion of $\ell$ around $\theta_0$. Reweighting the density at $\theta_0$
by $e^{\tau'\nabla\ell(\theta_0;x)}$ to move to a nearby $\theta_0+\tau$ is exactly the tangent-family
construction above, now stated for an arbitrary regular model rather than only a curved exponential
family.

Throughout, "sufficient regularity" is assumed to justify differentiating under the integral sign.
(It is possible to extend the definition to certain non-differentiable cases — the Laplace location
family is the standard example — but that extension is not developed here.)

## Two identities from differentiating under the integral

Since every density integrates to $1$,

$$1 = \int_{\mathcal{X}} e^{\ell(\theta;x)}\,d\mu(x).$$

Differentiating with respect to $\theta_j$ and using $\partial_j e^{\ell} = (\partial_j \ell)e^\ell$,

$$0 = \int_{\mathcal{X}} \frac{\partial \ell}{\partial \theta_j}(\theta;x)\,e^{\ell(\theta;x)}\,d\mu(x)
\quad\Longrightarrow\quad \mathbb{E}_\theta\big[\nabla\ell(\theta;X)\big] = 0.$$

**The score has mean zero — but only when the $\theta$ inside $\mathbb{E}_\theta$ is the same $\theta$
at which $\ell$ was differentiated.** Evaluating the score at one parameter value and taking its
expectation under another gives no such identity.

Differentiating the same equation once more, with respect to $\theta_k$, and using the product rule
on $\partial_j\ell \cdot e^\ell$:

$$0 = \int\left(\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}
+ \frac{\partial \ell}{\partial\theta_j}\frac{\partial\ell}{\partial\theta_k}\right)e^{\ell}\,d\mu
= \mathbb{E}_\theta\!\left[\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}\right]
+ \mathbb{E}_\theta\!\left[\frac{\partial\ell}{\partial\theta_j}\frac{\partial\ell}{\partial\theta_k}\right].$$

Because the score has mean zero, the second expectation on the right is exactly the
$(j,k)$ entry of $\operatorname{Var}_\theta(\nabla\ell(\theta;X))$, so rearranging gives

$$\underbrace{\operatorname{Var}_\theta\big[\nabla\ell(\theta;X)\big]}_{J(\theta)}
= \mathbb{E}_\theta\big[-\nabla^2\ell(\theta;X)\big] \qquad \text{(same $\theta$ on both sides).}$$

This matrix $J(\theta)$ is the **Fisher information**: the covariance matrix of the score, which is
also (by this identity) the expected negative curvature of the log-likelihood.

## The covariance of an estimator with the score

Take any statistic $\delta(X)$ and let $g(\theta) = \mathbb{E}_\theta[\delta(X)]$ — if $\delta$ is an
unbiased estimator of some quantity, $g$ *is* that quantity, written as a function of $\theta$.
Writing the expectation as an integral and differentiating under the integral sign,

$$g(\theta) = \int \delta(x)\, e^{\ell(\theta;x)}\, d\mu(x)
\quad\Longrightarrow\quad
\nabla g(\theta) = \int \delta(x)\,\nabla\ell(\theta;x)\,e^{\ell(\theta;x)}\,d\mu(x)
= \mathbb{E}_\theta\big[\delta(X)\nabla\ell(\theta;X)\big].$$

Since $\mathbb{E}_\theta[\nabla\ell(\theta;X)] = 0$, this expectation is a covariance:

$$\nabla g(\theta) = \operatorname{Cov}_\theta\big(\delta(X), \nabla\ell(\theta;X)\big).$$

In words: the sensitivity of an estimator's expectation to $\theta$ is entirely governed by how
correlated the estimator is with the score. This is the identity the Cramér–Rao bound is built from.

## The Cramér–Rao lower bound

**One parameter.** Cauchy–Schwarz applied to the covariance above,
$\operatorname{Cov}_\theta(\delta,\dot\ell)^2 \le \operatorname{Var}_\theta(\delta)\operatorname{Var}_\theta(\dot\ell)$,
gives immediately

$$\operatorname{Var}_\theta(\delta)\cdot J(\theta) \ge \dot g(\theta)^2
\quad\Longrightarrow\quad
\operatorname{Var}_\theta(\delta) \ge \frac{\dot g(\theta)^2}{J(\theta)}.$$

**Multivariate.** Now let $\theta \in \mathbb{R}^d$, with $g(\theta) \in \mathbb{R}$ and
$\delta(X) \in \mathbb{R}$ still scalar. For any direction $a \in \mathbb{R}^d$, apply the
one-dimensional argument to the projected score $a'\nabla\ell(\theta)$, whose variance is
$a'J(\theta)a$:

$$\operatorname{Var}_\theta(\delta)\cdot a'J(\theta)a = \operatorname{Var}_\theta(\delta)
\operatorname{Var}_\theta\big(a'\nabla\ell(\theta)\big)
\ge \operatorname{Cov}_\theta\big(\delta, a'\nabla\ell(\theta)\big)^2
= a'\nabla g\,\nabla g'a, \qquad \text{for every } a.$$

Dividing through and taking the best (largest) bound over directions,

$$\operatorname{Var}_\theta(\delta) \ge \max_{a \ne 0} \frac{a'\nabla g\,\nabla g' a}{a'J(\theta)a}
= \nabla g(\theta)'J(\theta)^{-1}\nabla g(\theta)$$

— the last equality is a general fact about this kind of ratio, left as an exercise below.

**Interpretation.** If $g(\theta)$ is the quantity being estimated, no unbiased estimator can have
variance smaller than $\nabla g(\theta)'J(\theta)^{-1}\nabla g(\theta)$, at any $\theta$.

## Example: an i.i.d. sample

Let $X_1, \dots, X_n \overset{\text{iid}}{\sim} p_\theta^{(1)}$, $\theta \in \Theta \subseteq
\mathbb{R}^d$, with the family "regular" in the sense above: common support and finite derivatives
with respect to $\theta$. Writing $\ell_1(\theta; x_i) = \log p_\theta^{(1)}(x_i)$ for the
single-observation log-likelihood, independence gives $\ell(\theta;x) = \sum_i \ell_1(\theta;x_i)$,
so the score is a sum of i.i.d., mean-zero terms and

$$J(\theta) = \operatorname{Var}_\theta\!\left(\sum_i \nabla\ell_1(\theta;X_i)\right) = n\,J_1(\theta),$$

where $J_1(\theta)$ is the Fisher information in a single observation. The Cramér–Rao bound
therefore scales like $n^{-1}$, so the best achievable standard deviation of an unbiased estimator
scales like $n^{-1/2}$ for a regular family — the familiar $\sqrt{n}$-rate.

## Efficiency

The Cramér–Rao bound need not be attainable by any actual unbiased estimator. Define the
**efficiency** of an unbiased $\delta$ as

$$\operatorname{eff}_\theta(\delta) = \frac{\text{CRLB}}{\operatorname{Var}_\theta(\delta)}
\qquad \left(= \frac{1/J(\theta)}{\operatorname{Var}_\theta(\delta)} \text{ if } g(\theta) = \theta
\in \mathbb{R}\right),$$

so that $\operatorname{eff}_\theta(\delta) \le 1$ by the bound itself, with equality — $\delta$
**efficient** — meaning $\operatorname{eff}_\theta(\delta) = 1$ for every $\theta$.

Efficiency has a clean interpretation: since the Cramér–Rao bound *is* the Cauchy–Schwarz bound,

$$\operatorname{eff}_\theta(\delta) = \frac{\operatorname{Cov}_\theta^2(\delta(X), \dot\ell(\theta;X))}
{\operatorname{Var}_\theta(\delta)\operatorname{Var}_\theta(\dot\ell(\theta))}
= \operatorname{Corr}_\theta^2\big(\delta, \dot\ell(\theta)\big) \le 1,$$

so $\delta$ is efficient if and only if its correlation with the score is exactly $\pm 1$ at every
$\theta$ — that is, $\delta$ is (up to an affine transformation depending on $\theta$) the score
itself. This is rarely achieved exactly in finite samples, but it can be approached asymptotically
as $n \to \infty$.

## Example: exponential families

For the canonical form $p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x)$,

$$\ell(\eta;x) = \eta'T(x) - A(\eta) + \log h(x), \qquad
\nabla\ell(\eta;x) = T(x) - \nabla A(\eta) = T(x) - \mathbb{E}_\eta T(X),$$

using the standard identity $\nabla A(\eta) = \mathbb{E}_\eta T(X)$. The score is *already* centered,
with no extra work — the mean being subtracted is exactly $\nabla A(\eta)$. Its variance is

$$\operatorname{Var}_\eta\big(\nabla\ell(\eta)\big) = \operatorname{Var}_\eta(T(X)) = \nabla^2A(\eta).$$

As a check against the other formula for $J$: since $\eta'T(x)$ is linear in $\eta$,
$\nabla^2\ell(\eta;x) = -\nabla^2A(\eta)$ outright (no expectation needed), so
$\mathbb{E}_\eta[-\nabla^2\ell(\eta;x)] = \nabla^2A(\eta)$ too — the two routes to $J(\theta)$ agree,
as the general identity guarantees. Consequently any unbiased estimator of $\eta$ satisfies

$$\operatorname{Var}_\eta(\delta) \ge \nabla^2A(\eta)^{-1}.$$

## Back to curved families

Now return to the curved family from the warm-up, written with the actual (scalar) parameter
$\theta$ made explicit:

$$p_\theta(x) = e^{\eta(\theta)'T(x) - B(\theta)}h(x), \qquad B(\theta) = A(\eta(\theta)), \qquad
\theta \in \mathbb{R}.$$

Then $\ell(\theta;x) = \eta(\theta)'T(x) - B(\theta) + \log h(x)$, and differentiating with the chain
rule (using $\dot B(\theta) = \dot\eta(\theta)'\nabla_\eta A(\eta(\theta))$):

$$\dot\ell(\theta;x) = \dot\eta(\theta)'T(x) - \dot\eta(\theta)'\nabla_\eta A(\eta(\theta))
= \dot\eta(\theta)'\big(T(x) - \mathbb{E}_\theta T(X)\big).$$

This is exactly $S_\theta(x)$ from the warm-up — the general score formula, applied to a curved
exponential family, reproduces the tangent-family sufficient statistic without any separate
argument. It confirms that $\dot\eta(\theta)'T(X)$ is a "locally complete sufficient statistic" at
every $\theta$, and it says something concrete about *which* coordinates of $T$ matter, locally: if
the curve $\eta(\theta)$ has tangent vector $(1,0)'$ at some $\theta$, only $T_1(X)$ is locally
informative there; where the tangent is $(0,1)'$, only $T_2(X)$ is.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="A curve of canonical parameters with tangent vectors at two points, one horizontal and one vertical, showing which coordinate of the sufficient statistic is locally informative">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="292" y="205" text-anchor="end" font-size="12" fill="currentColor">$\eta_1$</text>
  <text x="30" y="28" text-anchor="end" font-size="12" fill="currentColor">$\eta_2$</text>
  <path d="M 80 170 A 130 130 0 0 1 210 40" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="150" y="150" font-size="12" fill="currentColor">$\Xi=\{\eta(\theta)\}$</text>
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="80" y1="170" x2="135" y2="170" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <circle cx="80" cy="170" r="2.5" fill="currentColor"/>
  <text x="80" y="205" text-anchor="middle" font-size="11" fill="currentColor">tangent $(1,0)$: only $T_1$ matters</text>
  <line x1="210" y1="80" x2="210" y2="25" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <circle cx="210" cy="40" r="2.5" fill="currentColor"/>
  <text x="230" y="65" font-size="11" fill="currentColor">tangent $(0,1)$:</text>
  <text x="230" y="80" font-size="11" fill="currentColor">only $T_2$ matters</text>
</svg>
<figcaption>The canonical parameter traces a curve $\Xi$ in the $(\eta_1,\eta_2)$ plane as $\theta$
varies; the direction of the tangent line at $\theta$ picks out which coordinate of $T(X)$ is
locally complete sufficient there.</figcaption>
</figure>

## Exercises

1. For $v \in \mathbb{R}^d$ and $M$ a positive-definite $d\times d$ matrix, show that
   $$\max_{a \ne 0} \frac{a'vv'a}{a'Ma} = v'M^{-1}v.$$
   (This is the step the multivariate Cramér–Rao derivation above leans on; the lecture marks it
   as an exercise rather than proving it.)

## Sources

- Handwritten lecture notes: `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture07-F24.md`
  (Berkeley STAT 210A, an outline of score function / Fisher information / Cramér–Rao lower bound /
  examples, dated 9/19/2023 in the source; reconstructed by a model from a PDF with no text layer,
  so every equation there is flagged unverified and is transcribed here as given). Covers, in order:
  the tangent-family motivation for the score, built from a curved two-parameter exponential family
  and its linear approximation; the general definition of the score and its "local complete
  sufficient statistic" reading, including the aside that the definition can be extended to certain
  non-differentiable cases such as the Laplace location family (not developed further); the two
  differential identities giving $\mathbb{E}_\theta[\nabla\ell] = 0$ and the Fisher information
  $J(\theta)$; the covariance identity $\nabla g(\theta) = \operatorname{Cov}_\theta(\delta,
  \nabla\ell(\theta))$ for an unbiased-type statistic; the one-parameter and multivariate
  Cramér–Rao lower bounds, with the multivariate proof via projecting the score onto an arbitrary
  direction $a$; the i.i.d.-sample example showing $J(\theta) = nJ_1(\theta)$; the definition of
  efficiency and its identity with squared correlation to the score; the exponential-family example
  computing the score and Fisher information both ways; and the curved-family calculation that
  recovers the tangent-family score from the general formula, together with the hand-drawn picture
  of the curve $\eta(\theta)$ and its tangent directions reproduced above as a diagram.
- The final step of the multivariate Cramér–Rao derivation — that
  $\max_{a\neq0} a'vv'a/(a'Ma) = v'M^{-1}v$ — is marked "Exercise" in the source itself and is
  carried into the Exercises section above rather than solved.
- The lecture cites the "regular" family assumption (common support, finite derivatives) and
  "sufficient regularity" for differentiating under the integral sign throughout, without stating
  precise conditions; none are supplied beyond what is quoted above.

---

[← 35. Rao–Blackwell and UMVU Estimators](35-rao-blackwell-and-umvu-estimators.md) · [Contents](index.md) · [37. Unbiased Estimation and the UMVUE →](37-unbiased-estimation-and-the-umvue.md)
