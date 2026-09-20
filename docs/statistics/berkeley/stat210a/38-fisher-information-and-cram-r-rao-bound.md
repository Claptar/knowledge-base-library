---
title: "38. Fisher Information and Cram\u00e9r\u2013Rao Bound"
course: "Berkeley Stat 210A Fall 2024"
chapter: 38
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 38. Fisher Information and Cramér–Rao Bound

## What this covers

How much information does one observation carry about a parameter, and how much better can any
unbiased estimator possibly be? This chapter builds the score function, defines Fisher information
in two equivalent ways, and uses it to prove the Cramér–Rao lower bound on the variance of any
unbiased estimator. It closes with two payoffs: Fisher information in exponential families reduces
to a Hessian of the log-partition function, and Fisher information has a second life as the local
curvature of Kullback–Leibler divergence. It assumes exponential families (natural parameter
$\eta$, sufficient statistic $T(x)$, log-partition function $A(\eta)$, and the identities
$\mathbb{E}_\eta[T(X)] = \nabla A(\eta)$, $\mathrm{Var}_\eta(T(X)) = \nabla^2 A(\eta)$) and the idea
of a complete sufficient statistic.

## Motivating the score: the tangent to a curved family

Start from a full exponential family with a two-dimensional natural parameter,
$$p_\theta(x) = e^{\eta(\theta)'T(x) - A(\eta(\theta))} h(x), \qquad \eta: \mathbb{R} \to \mathbb{R}^2,$$
where $\theta$ ranges over a curve $\Xi = \{\eta(\theta) : \theta \in \mathbb{R}\}$ inside the natural
parameter space. If $\eta(\theta)$ is a nonlinear function of $\theta$ this is a **curved family**:
$T(x)$ is minimal sufficient for the full exponential family, but restricting to the curve generally
destroys sufficiency, because $\theta$ moves along only a one-dimensional slice of a
higher-dimensional parameter. Sufficiency is recovered only in the special case
$\eta(\theta) = \eta_0 + \theta\delta$, linear in $\theta$: then $p_\theta$ is itself a one-parameter
exponential family with natural statistic $\delta'T(x)$, which is complete sufficient.

The fix for the general, nonlinear case is to linearize locally. Fix a base point $\theta_0$ and
replace the curve by its **tangent line** there,
$$\Xi_{\text{tan}} = \{\eta(\theta_0) + \varepsilon\,\dot\eta(\theta_0) : \varepsilon \in \mathbb{R}\},
\qquad \dot\eta(\theta_0) = \frac{d\eta}{d\theta}(\theta_0).$$
This **tangent family** is exactly linear in $\varepsilon$, so it is an honest one-parameter
exponential family and does have a complete sufficient statistic. Writing out its density,
$$q_\varepsilon(x) = \exp\big((\eta(\theta_0) + \varepsilon\dot\eta(\theta_0))'T(x) - A(\eta(\theta_0)+\varepsilon\dot\eta(\theta_0))\big)h(x),$$
and collecting everything that does not multiply $\varepsilon T(x)$ into the base density $p_{\theta_0}$
and a normalizing function of $\varepsilon$ alone (re-centering $T(x)$ at its mean under $\theta_0$
so that $q_0 = p_{\theta_0}$) gives
$$q_\varepsilon(x) = e^{\varepsilon\,\dot\eta(\theta_0)'(T(x) - \mathbb{E}_{\theta_0}T(X)) - B(\varepsilon)}\, k(x).$$

The natural statistic of this tangent family,
$$S_{\theta_0}(x) := \dot\eta(\theta_0)'\big(T(x) - \mathbb{E}_{\theta_0}T(X)\big),$$
is complete sufficient *for the tangent family at $\theta_0$*. This is the **score function**. It
is not a sufficient statistic for the original curved family — sufficiency here is only a local,
first-order notion, valid for $\theta$ near $\theta_0$ — but it captures exactly the direction along
which the density changes as $\theta$ moves through $\theta_0$.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A curved exponential family traced by eta of theta, with its tangent line at one point">
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M 0 0 L 10 5 L 0 10 z" fill="currentColor"/>
</marker>
</defs>
<path d="M 40 190 C 100 60, 220 40, 300 90" fill="none" stroke="currentColor" stroke-width="1.5"/>
<text x="255" y="65" font-size="12" fill="currentColor">Ξ = {η(θ)}</text>
<circle cx="170" cy="80" r="3" fill="currentColor"/>
<text x="178" y="70" font-size="12" fill="currentColor">η(θ₀)</text>
<line x1="100" y1="145" x2="255" y2="35" stroke="currentColor" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="205" y="140" font-size="12" fill="currentColor">tangent family Ξ_tan</text>
<line x1="170" y1="80" x2="230" y2="38" stroke="currentColor" stroke-width="2" marker-end="url(#arrow)"/>
<text x="234" y="45" font-size="12" fill="currentColor">η̇(θ₀)</text>
</svg>
<figcaption>The curved family traces a curve through the natural parameter space; replacing it by its
tangent line at θ₀ gives a genuine one-parameter exponential family whose natural statistic,
η̇(θ₀)′(T(x) − E T), is the score at θ₀.</figcaption>
</figure>

## The score function, in general

Now drop the exponential-family scaffolding and work with a general model $\{p_\theta : \theta \in
\Theta \subseteq \mathbb{R}^d\}$, densities with respect to a common measure $\mu$, and — this is the
standing "regularity" assumption for everything below — common support $\{x : p_\theta(x) > 0\}$ not
depending on $\theta$. Write $\ell(\theta; x) = \log p_\theta(x)$, thought of as a random function of
$\theta$.

**Definition.** The **score** is $\nabla\ell(\theta; x)$.

The tangent-family computation above is the special case of a general fact: for $\eta$ small,
$$p_{\theta_0+\eta}(x) = e^{\ell(\theta_0+\eta;\,x)} \approx e^{\eta'\nabla\ell(\theta_0; x)}\,p_{\theta_0}(x),$$
so the score is the direction, in log-density, along which $p_\theta$ moves to first order as $\theta$
leaves $\theta_0$ — a "local complete sufficient statistic" even for models that are not exponential
families at all.

Two differential identities follow from differentiating the normalization
$1 = \int_{\mathcal{X}} e^{\ell(\theta;x)}\,d\mu(x)$ under the integral sign (this is exactly where
the regularity is being used):

$$\frac{\partial}{\partial\theta_j}: \qquad 0 = \int \frac{\partial \ell}{\partial \theta_j}(\theta;x)\, e^{\ell(\theta;x)}\,d\mu(x) \implies \mathbb{E}_\theta[\nabla\ell(\theta; X)] = 0.$$

The score has mean zero — but only when the $\theta$ inside the expectation matches the $\theta$ at
which the score is evaluated. Differentiating once more,

$$\frac{\partial}{\partial \theta_k}: \qquad 0 = \int\left(\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k} + \frac{\partial\ell}{\partial\theta_j}\frac{\partial\ell}{\partial\theta_k}\right)e^{\ell}\,d\mu = \mathbb{E}_\theta\left[\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}\right] + \mathbb{E}_\theta\left[\frac{\partial\ell}{\partial\theta_j}\frac{\partial\ell}{\partial\theta_k}\right],$$

so, again only at matching $\theta$,
$$\mathrm{Var}_\theta(\nabla\ell(\theta;X)) = \mathbb{E}_\theta[-\nabla^2\ell(\theta;X)] =: \mathcal{J}(\theta).$$

This matrix is the **Fisher information**: it has both a covariance-of-the-score reading and a
curvature-of-the-log-likelihood reading, and the identity says the two always agree. (The definition
extends to some non-differentiable cases — the Laplace location family is the standard example — but
we work throughout under enough regularity for the calculus above to be valid.)

One more identity, for an arbitrary statistic $\delta(X)$ with $g(\theta) := \mathbb{E}_\theta[\delta(X)]$
(so $\delta$ is an "unbiased estimator" of $g$):
$$g(\theta) = \int \delta\, e^{\ell(\theta;x)}\,d\mu(x) \implies \nabla g(\theta) = \int \delta\,\nabla\ell\, e^{\ell(\theta;x)}\,d\mu(x) = \mathbb{E}_\theta[\delta(X)\nabla\ell(\theta;X)] = \mathrm{Cov}_\theta(\delta(X), \nabla\ell(\theta;X)),$$
the last step using $\mathbb{E}_\theta[\nabla\ell] = 0$. Differentiating the bias-free-ness of an
estimator turns its derivative into a covariance with the score — this is the identity Cauchy–Schwarz
is about to be applied to.

## The Cramér–Rao lower bound

**One parameter.** Cauchy–Schwarz applied to $\delta(X)$ and $\dot\ell(\theta;X)$ gives
$$\mathrm{Var}_\theta(\delta)\cdot\mathrm{Var}_\theta(\dot\ell(\theta;X)) \ge \mathrm{Cov}_\theta(\delta,\dot\ell(\theta;X))^2 = \dot g(\theta)^2,$$
so
$$\mathrm{Var}_\theta(\delta) \ge \frac{\dot g(\theta)^2}{\mathcal{J}(\theta)}.$$

**Several parameters.** For $\theta \in \mathbb{R}^d$ and a scalar $g(\theta) = \mathbb{E}_\theta[\delta(X)]$,
$$\mathrm{Var}_\theta(\delta) \ge \nabla g(\theta)'\,\mathcal{J}(\theta)^{-1}\,\nabla g(\theta).$$

*Proof.* Apply the one-parameter bound to $\delta(X)$ against the scalar $a'\nabla\ell(\theta;X)$ for
an arbitrary direction $a \in \mathbb{R}^d$:
$$\mathrm{Var}_\theta(\delta)\cdot a'\mathcal{J}(\theta)a = \mathrm{Var}_\theta(\delta)\,\mathrm{Var}_\theta(a'\nabla\ell(\theta;X)) \ge \mathrm{Cov}_\theta(\delta, a'\nabla\ell(\theta;X))^2 = a'\nabla g\,\nabla g'\,a, \quad \text{for every } a.$$
So
$$\mathrm{Var}_\theta(\delta) \ge \max_{a \ne 0} \frac{a'\nabla g\,\nabla g'\,a}{a'\mathcal{J}(\theta)a}.$$
This is a generalized Rayleigh quotient: substitute $u = \mathcal{J}(\theta)^{1/2}a$ to turn it into
$\max_u \dfrac{u'(\mathcal{J}^{-1/2}\nabla g)(\mathcal{J}^{-1/2}\nabla g)'u}{u'u}$, which is maximized at
$u \propto \mathcal{J}^{-1/2}\nabla g$ (equivalently $a \propto \mathcal{J}(\theta)^{-1}\nabla g$), with
maximal value $\nabla g'\,\mathcal{J}(\theta)^{-1}\,\nabla g$. $\blacksquare$

**Interpretation.** If $g(\theta)$ is the quantity being estimated, no unbiased estimator can have
variance smaller than $\nabla g(\theta)'\mathcal{J}(\theta)^{-1}\nabla g(\theta)$, at any $\theta$.

## Example: an i.i.d. sample

Let $X_1,\dots,X_n \overset{\text{iid}}{\sim} p_\theta^{(1)}$ with $\theta \in \Theta \subseteq \mathbb{R}^d$,
the family regular (common support, finite derivatives in $\theta$). Writing
$\ell_1(\theta;x_i) = \log p_\theta^{(1)}(x_i)$, the joint log-likelihood is additive,
$\ell(\theta;x) = \sum_i \ell_1(\theta;x_i)$, hence so is the score, and independence turns the
variance of the sum into a sum of variances:
$$\mathcal{J}(\theta) = \mathrm{Var}_\theta\!\left(\sum_i \nabla\ell_1(\theta;X_i)\right) = n\,\mathcal{J}_1(\theta),$$
where $\mathcal{J}_1(\theta)$ is the Fisher information in a single observation. The Cramér–Rao bound
therefore scales like $n^{-1}$ — the best achievable standard deviation of an unbiased estimator
scales like $n^{-1/2}$, the familiar parametric rate, for any regular family.

## Efficiency

The Cramér–Rao bound need not be attainable. The **efficiency** of an unbiased estimator $\delta$ is
$$\mathrm{eff}_\theta(\delta) = \frac{\text{CRLB}}{\mathrm{Var}_\theta(\delta)} \qquad \left(= \frac{1/\mathcal{J}(\theta)}{\mathrm{Var}_\theta(\delta)} \text{ if } g(\theta) = \theta \in \mathbb{R}\right), \qquad \mathrm{eff}_\theta(\delta) \le 1,$$
and $\delta$ is called **efficient** if $\mathrm{eff}_\theta(\delta) = 1$ for every $\theta$.
Efficiency is a squared correlation with the score:
$$\mathrm{eff}_\theta(\delta) = \frac{\mathrm{Cov}_\theta(\delta,\dot\ell(\theta))^2}{\mathrm{Var}_\theta(\delta)\,\mathrm{Var}_\theta(\dot\ell(\theta))} = \mathrm{Corr}_\theta^2(\delta,\dot\ell(\theta)) \le 1,$$
so $\delta$ is efficient exactly when it is perfectly correlated with the score at every $\theta$ —
equivalently, an affine function of the score. This is rarely achieved by any fixed estimator at
finite $n$, but it can be approached asymptotically as $n \to \infty$.

## Example: exponential families

For a full exponential family $p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x)$,
$$\ell(\eta;x) = \eta'T(x) - A(\eta) + \log h(x), \qquad \nabla\ell(\eta;x) = T(x) - \nabla A(\eta) = T(x) - \mathbb{E}_\eta[T(X)],$$
confirming the score has mean zero. Its variance is
$$\mathrm{Var}_\eta(\nabla\ell(\eta;X)) = \mathrm{Var}_\eta(T(X)) = \nabla^2 A(\eta),$$
and directly from $\nabla^2\ell(\eta;x) = -\nabla^2 A(\eta)$, $\mathbb{E}_\eta[-\nabla^2\ell(\eta;X)] = \nabla^2 A(\eta)$
as well — the two readings of Fisher information agree, as they must. So for exponential families,
$$\mathcal{J}(\eta) = \nabla^2 A(\eta),$$
the Fisher information is exactly the Hessian of the log-partition function, and any unbiased
estimator of $\eta$ satisfies $\mathrm{Var}_\eta(\delta) \ge \nabla^2 A(\eta)^{-1}$.

**Curved exponential families, revisited.** For $p_\theta(x) = e^{\eta(\theta)'T(x) - B(\theta)}h(x)$
with $\theta \in \mathbb{R}$ and $B(\theta) = A(\eta(\theta))$, the chain rule gives
$$\dot\ell(\theta;x) = \dot\eta(\theta)'T(x) - \dot B(\theta) = \dot\eta(\theta)'\big(T(x) - \nabla_\eta A(\eta(\theta))\big) = \dot\eta(\theta)'\big(T(x) - \mathbb{E}_\theta T(X)\big),$$
recovering exactly the tangent-family score from the opening section. It is the projection of
$T(x) - \mathbb{E}_\theta T(X)$ onto the tangent direction $\dot\eta(\theta)$, so $\dot\eta(\theta)'T(X)$
is the "locally complete sufficient statistic" — and combining this with $\mathrm{Var}_\eta(T(X)) =
\nabla^2 A(\eta)$ from above gives the Fisher information of the curved family directly:
$$\mathcal{J}(\theta) = \dot\eta(\theta)'\,\nabla^2 A(\eta(\theta))\,\dot\eta(\theta).$$
Which coordinate of $T$ matters locally is entirely a question of which direction the curve is
heading: if $\dot\eta(\theta) = (0,1)'$, only $T_2(X)$ is locally relevant; if $\dot\eta(\theta) = (1,0)'$,
only $T_1(X)$ is.

## Fisher information as a local metric

Fisher information also measures how distinguishable two nearby members of a family are, via the
**Kullback–Leibler divergence**,
$$D_{KL}(p \| q) = \mathbb{E}_p[\log p(X) - \log q(X)] = \int \log\!\left(\frac{p}{q}\right) p\, d\mu,$$
a standard (asymmetric) notion of distance between distributions. For a parametric family, writing
$\theta^*$ for a fixed "true" value and letting $\theta$ vary,
$$D_{KL}(\theta^* \| \theta) := D_{KL}(p_{\theta^*} \| p_\theta) = \int\big(\ell(\theta^*;x) - \ell(\theta;x)\big)\,e^{\ell(\theta^*;x)}\,d\mu(x) = \mathbb{E}_{\theta^*}[\ell(\theta^*;X) - \ell(\theta;X)].$$

As a function of $\theta$, this is nonnegative and equal to $0$ at $\theta = \theta^*$, so it is
**minimized** there. Differentiating confirms $\theta^*$ is a stationary point:
$$\frac{\partial}{\partial\theta_j}D_{KL}(\theta^*\|\theta) = -\int\frac{\partial\ell}{\partial\theta_j}(\theta;x)\,e^{\ell(\theta^*;x)}\,d\mu(x) = -\mathbb{E}_{\theta^*}\!\left[\frac{\partial\ell}{\partial\theta_j}(\theta;X)\right],$$
which at $\theta = \theta^*$ is $-\mathbb{E}_{\theta^*}[\partial_j\ell(\theta^*;X)] = 0$ by the mean-zero
score identity. The second derivative,
$$\frac{\partial^2}{\partial\theta_j\partial\theta_k}D_{KL}(\theta^*\|\theta) = -\mathbb{E}_{\theta^*}\!\left[\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}(\theta;X)\right],$$
evaluated at $\theta = \theta^*$ is $\mathbb{E}_{\theta^*}[-\nabla^2\ell(\theta^*;X)] = \mathcal{J}(\theta^*)$ —
exactly the Fisher information matrix, and its positive semi-definiteness here is just the second-order
condition for $\theta^*$ to be a minimum. Putting the two derivatives together, the second-order Taylor
expansion of $D_{KL}$ around its minimum is
$$D_{KL}(\theta^* \| \theta) \approx \tfrac{1}{2}(\theta - \theta^*)'\,\mathcal{J}(\theta^*)\,(\theta - \theta^*) \qquad (\theta \to \theta^*).$$
So Fisher information is the quadratic form that locally governs Kullback–Leibler distance: two
parameter values close together in the metric $\mathcal{J}(\theta^*)$ are hard to statistically
distinguish, and the same matrix that bounds estimator variance in the Cramér–Rao inequality also
measures how sharply the likelihood separates nearby parameter values.

## Sources

- Both files are model reconstructions of a handwritten PDF with no text layer
  (`handwritten/lecture08-fisherinfo.pdf`, berkeley-stat210a fall-2024, CC BY 4.0); the source banner
  in each file flags that every equation is unverified, so the derivations above have been checked and
  filled in for internal consistency rather than taken on faith.
- Tangent family motivation, score function, differential identities, Fisher information, the
  Cramér–Rao lower bound (one-parameter and multivariate, with proof), the i.i.d. example, and
  efficiency:
  `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture08-fisherinfo/01-lecture-08-fisherinfo-part-01.md`.
- Exponential-family example (score and Fisher information as $\nabla^2 A$), the curved-family score
  revisited, and Fisher information as the local curvature of KL divergence:
  `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture08-fisherinfo/02-ex-exponential-families.md`.
- One correction: the source states $D_{KL}(\theta^*\|\theta)$ is "maximized" at $\theta = \theta^*$;
  this chapter uses "minimized," which is what the surrounding computation actually shows (KL
  divergence is nonnegative and zero at $\theta^*$, and the second derivative there is $+\mathcal{J}(\theta^*) \succeq 0$,
  the signature of a minimum, not a maximum).
- The source notes cut off mid-sentence after "$d=1$:", apparently about to specialize the quadratic
  approximation to the scalar case; the closing display above completes that step directly from the
  two derivatives already computed in the source, without introducing anything beyond them.
- No slide deck, transcript, or problem set was supplied for this lecture, and no exercises are
  listed in the task input, so no Exercises section is included. A "Part 02" is implied by the "Part
  01" title but was not supplied.

---

[← 37. Unbiased Estimation and the UMVUE](37-unbiased-estimation-and-the-umvue.md) · [Contents](index.md) · [39. Bayes Estimation for Frequentists →](39-bayes-estimation-for-frequentists.md)
