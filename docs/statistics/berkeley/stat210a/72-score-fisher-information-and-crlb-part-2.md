---
title: "72. Score, Fisher Information, and CRLB (part 2)"
course: "Berkeley Stat 210A"
chapter: 72
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 72. Score, Fisher Information, and CRLB (part 2)

## What this covers

How much a sample tells you about an unknown parameter, and what that limits about estimation.
Starting from the log-likelihood, this chapter builds the score function, shows why its variance
— the Fisher information — governs how sharply the likelihood curves near the truth, and uses it
to derive the Cramér–Rao lower bound: a hard floor on the variance of any unbiased estimator. It
closes with how score and information behave in i.i.d. samples and in (curved) exponential
families. It assumes log-likelihoods, sufficiency and completeness in exponential families, and
basic vector calculus (gradients, Hessians) together with covariance, correlation and the
Cauchy–Schwarz inequality.

## The score function

Let $\mathcal P = \{P_\theta : \theta \in \Theta \subseteq \mathbb R^d\}$ be a family of
distributions with densities $p_\theta$ with respect to a common measure $\mu$. Assume the
densities have **common support**: $\{x : p_\theta(x) > 0\}$ does not depend on $\theta$ (if it
did, we could just truncate the sample space to the common part).

Write the log-likelihood as a random function of $\theta$,
$$\ell(\theta; X) = \log p_\theta(X),$$
and define the **score function**
$$S_\theta(X) = \nabla_\theta \ell(\theta; X) \in \mathbb R^d.$$

**Why the score matters.** The whole log-likelihood curve $\ell(\cdot\,;X)$, as a function of
$\theta$, is a minimal sufficient statistic for $X$, up to an additive (vertical) shift. Fix a
reference point $\theta_0 \in \Theta$ and subtract off $\ell(\theta_0;X)$; then $\ell(\theta;X) -
\ell(\theta_0;X)$ is still minimal sufficient. For $\theta = \theta_0 + \eta$ with $\eta$ small,
$$\ell(\theta_0 + \eta; X) - \ell(\theta_0; X) \approx \eta' S_{\theta_0}(X),$$
so the single vector $S_{\theta_0}(X)$ already captures, to first order, everything the whole
log-likelihood curve says about which nearby $\theta$ generated the data. That is the sense in
which the score is a "local" sufficient statistic for the family restricted to a small
neighborhood of $\theta_0$.

This can be made literal. Build the exponential family obtained by tilting $p_{\theta_0}$ by
$S_{\theta_0}(X)$,
$$q(x;t) = e^{t'S_{\theta_0}(x) - k(t)}\,p_{\theta_0}(x), \qquad k(t) = \log\int e^{t'S_{\theta_0}(x)}p_{\theta_0}(x)\,d\mu(x);$$
then $S_{\theta_0}(X)$ is complete sufficient for this **tangent family** at $t=0$. That is the
exponential-family picture behind the approximation
$$p_{\theta_0+\eta}(x) = e^{\ell(\theta_0+\eta;x)} \approx e^{\eta' S_{\theta_0}(x)}\,p_{\theta_0}(x),$$
which says the local family $\{P_{\theta_0+\eta} : \eta \text{ small}\}$ looks, to first order,
like an exponential family tilted by the score.

**Is the score a statistic?** This deserves care, because a statistic must be computable from the
data without knowing the true $\theta$. The notation $\ell(\theta;X)$ is ambiguous between two
readings:

- $\ell(\cdot\,;X)$, the *whole function* of $\theta$ — the analyst can plot this graph without
  knowing the truth, so the graph itself (and hence $S_{\theta_0}(X)$ for any *fixed, known*
  $\theta_0$) is a statistic;
- $\ell(\theta;X)$ evaluated *at the true $\theta$* — not something the analyst can compute
  without already knowing $\theta$, so this is not a statistic.

So whether $S_\theta(X)$ "is a statistic" depends on what $\theta$ means in it. If $\theta_0$ is a
value the analyst has chosen — say, testing $H_0 : \theta = \theta_0$ without knowing whether
$H_0$ is true — then $S_{\theta_0}(X)$ is a genuine statistic, sometimes called a *score
statistic*. But in most of the theory below, $S_\theta(X)$ is evaluated at the true parameter
governing the data, purely as a theoretical device for studying the local behavior of the model —
and in that role it is not a statistic at all. This matters because these local models, indexed by
a small neighborhood of the true parameter, are exactly what asymptotic theory studies: with a
large sample, most values of $\theta$ get ruled out and only a small neighborhood of the truth
remains plausible.

## Differential identities and the Fisher information

Assuming enough regularity to differentiate under the integral sign, two identities follow from
differentiating
$$1 = \int_{\mathcal X} e^{\ell(\theta;x)}\,d\mu(x)$$
with respect to $\theta$. (The exact regularity conditions are delicate and are not spelled out
here; the score remains useful even in some models where $\ell$ fails to be differentiable, such
as the Laplace location family, though that case is not developed in this chapter.)

Differentiating once with respect to $\theta_j$ gives
$$0 = \int_{\mathcal X} \frac{\partial \ell}{\partial \theta_j}(\theta;x)\, e^{\ell(\theta;x)}\,d\mu(x) = \mathbb E_\theta\!\left[\frac{\partial \ell}{\partial\theta_j}(\theta;X)\right],$$
and collecting these into a vector,
$$\mathbb E_\theta[S_\theta(X)] = 0.$$
This identity is easy to misuse: it only holds when the $\theta$ indexing the expectation matches
the $\theta$ at which the score is evaluated. If the true parameter is $\theta$ but the score is
evaluated at some other reference point $\theta_0$, then in general $\mathbb
E_\theta[S_{\theta_0}(X)] \neq 0$.

Differentiating a second time, with respect to $\theta_k$, gives
$$0 = \int_{\mathcal X}\left(\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k} + \frac{\partial \ell}{\partial\theta_j}\frac{\partial\ell}{\partial\theta_k}\right)e^{\ell}\,d\mu = \mathbb E_\theta\!\left[\frac{\partial^2\ell}{\partial\theta_j\partial\theta_k}\right] + \mathbb E_\theta\!\left[\frac{\partial \ell}{\partial\theta_j}\frac{\partial \ell}{\partial\theta_k}\right].$$
Since $\mathbb E_\theta[S_\theta(X)] = 0$, the second term on the right is exactly
$\mathrm{Cov}_\theta(S_{\theta,j}(X), S_{\theta,k}(X))$, so collecting into matrices,
$$\mathrm{Var}_\theta(S_\theta(X)) = \mathbb E_\theta[-\nabla^2\ell(\theta;X)].$$
Again this holds only when both $\theta$'s — the one indexing the expectation, and the one where
the derivatives are evaluated — agree.

The left-hand side, the variance of the score, is the **Fisher information matrix**
$$J(\theta) := \mathrm{Var}_\theta(S_\theta(X)),$$
always positive semidefinite. It measures how sharply the log-likelihood curves near $\theta$: a
large Fisher information means the log-likelihood typically has high curvature there, i.e. nearby
parameter values are easy to tell apart from a typical sample.

## The Cramér–Rao lower bound

The score and Fisher information have a finite-sample payoff: they bound the variance of any
unbiased estimator.

Let $\delta(X)$ be an unbiased estimator of $g(\theta) = \mathbb E_\theta[\delta(X)] = \int
\delta(x) e^{\ell(\theta;x)}\,d\mu(x)$. Differentiating this identity with respect to $\theta_j$
and collecting into a vector gives
$$\nabla g(\theta) = \mathbb E_\theta[\delta(X) S_\theta(X)] = \mathrm{Cov}_\theta(\delta(X), S_\theta(X)),$$
using $\mathbb E_\theta[S_\theta(X)]=0$ from above. (This covariance is a $d$-vector, since
$\delta(X)$ is scalar and $S_\theta(X)$ is a $d$-vector.)

**Single parameter ($d=1$).** Write $\dot g(\theta)$ for the derivative. The squared correlation
between $\delta(X)$ and the score is
$$\mathrm{Corr}_\theta^2(\delta(X), S_\theta(X)) = \frac{\mathrm{Cov}_\theta(\delta(X),S_\theta(X))^2}{\mathrm{Var}_\theta(\delta(X)) J(\theta)} = \frac{\dot g(\theta)^2}{\mathrm{Var}_\theta(\delta(X)) J(\theta)}.$$
A squared correlation is at most $1$, so rearranging gives the **Cramér–Rao lower bound (CRLB)**,
also called the information bound:
$$\mathrm{Var}_\theta(\delta(X)) \geq \frac{\dot g(\theta)^2}{J(\theta)}.$$
Taking $g(\theta) = \theta$, no unbiased estimator of $\theta$ can have variance below
$1/J(\theta)$.

**A unit-conversion sanity check.** Is it really "harder" to estimate $g(\theta) = 12\theta$ than
to estimate $\theta$ itself? In one sense yes — the CRLB says the variance of an estimator of
$12\theta$ should be $144$ times larger. But if $\theta$ is measured in inches and $g(\theta)$ in
feet, this is no more than the unit conversion showing up in $\dot g(\theta) = 12$: if $\theta$ has
units of feet, then $S_\theta(X)$ has units of inverse feet and $J(\theta)$ has units of inverse
square feet, and the bound is dimensionally consistent throughout.

**Efficiency.** The CRLB need not be attainable. Define the efficiency of an unbiased estimator
$\delta$ as
$$\mathrm{eff}_\delta(\theta) = \frac{\mathrm{CRLB}(\theta)}{\mathrm{Var}_\theta(\delta)} \leq 1,$$
and call $\delta$ **efficient** if $\mathrm{eff}_\delta(\theta) = 1$ for every $\theta$. Unwinding
the definitions,
$$\mathrm{eff}_\delta(\theta) = \frac{\mathrm{Cov}_\theta(\delta(X),S_\theta(X))^2}{\mathrm{Var}_\theta(\delta(X))\,\mathrm{Var}_\theta(S_\theta(X))} = \mathrm{Corr}_\theta^2(\delta, S_\theta),$$
so an estimator is efficient exactly when it is perfectly correlated with the score. Roughly, if
$\delta(X)$ has only, say, a $50\%$ "R-squared" with the score, it is using only half the
information locally available, which accounts for its inefficiency. Finite-sample efficiency is
rare — even the UMVU estimator typically falls short — but as $n \to \infty$ in i.i.d. sampling,
estimators (notably the maximum likelihood estimator) typically become both asymptotically
unbiased and efficient.

**Multivariate case.** For $\theta \in \mathbb R^d$ and scalar $g(\theta)$,
$$\mathrm{Var}_\theta(\delta(X)) \geq \nabla g(\theta)' J(\theta)^{-1} \nabla g(\theta).$$
To see this, project the score onto an arbitrary direction $a \in \mathbb R^d$: since
$\mathrm{Cov}_\theta(\delta(X), a'S_\theta(X)) = a'\nabla g(\theta)$ and
$\mathrm{Var}_\theta(a'S_\theta(X)) = a'J(\theta)a$, the single-parameter argument applied to
$a'S_\theta(X)$ gives, for every nonzero $a$,
$$\mathrm{Var}_\theta(\delta(X)) \geq \frac{(a'\nabla g(\theta))^2}{a'J(\theta)a}.$$
The right side is a Rayleigh quotient, maximized at $a^* = J(\theta)^{-1}\nabla g(\theta)$; since
the bound above holds for every $a$, it holds in particular at this optimizer, and substituting it
in gives exactly $\nabla g(\theta)'J(\theta)^{-1}\nabla g(\theta)$. Taking $g(\theta) = \theta_j$,
no unbiased estimator can have variance below $(J(\theta)^{-1})_{jj}$.

## Score and information add up over independent samples

Suppose $X_1,\dots,X_n$ are i.i.d. from a "regular" density $p_\theta^{(1)}$ (common support, tame
derivatives in $\theta$), so the full-sample density factors as $p_\theta(x) = \prod_i
p_\theta^{(1)}(x_i)$ and the log-likelihood adds: $\ell(\theta;X) = \sum_i \ell_1(\theta;X_i)$,
where $\ell_1(\theta;X_i) = \log p_\theta^{(1)}(X_i)$.

The score is then a sum of i.i.d. single-observation scores, $S_\theta(X) = \sum_i
S_\theta^{(1)}(X_i)$, and since these are independent, the Fisher information for the full sample
is
$$J(\theta) = \mathrm{Var}_\theta(S_\theta(X)) = \sum_{i=1}^n \mathrm{Var}_\theta(S_\theta^{(1)}(X_i)) = nJ_1(\theta),$$
where $J_1(\theta)$ is the single-observation Fisher information. So the CRLB scales like
$n^{-1}$: the standard deviation of a good estimator should scale like $1/\sqrt n$.

## Score and Fisher information in exponential families

**Natural exponential family.** For $p_\eta(x) = e^{\eta'T(x) - A(\eta)}h(x)$, the log-likelihood
is $\ell(\eta;X) = \eta'T(X) - A(\eta) + \log h(X)$, so the score is
$$S_\eta(X) = \nabla\ell(\eta;X) = T(X) - \nabla A(\eta) = T(X) - \mathbb E_\eta[T(X)].$$
So — up to the centering needed to make its mean zero — **the score in a natural exponential
family is just the sufficient statistic $T(X)$ itself.** This is exactly what the tangent-family
picture above predicted. Since $\mathbb E_\eta[T(X)]$ is non-random, the Fisher information is
$$J(\eta) = \mathrm{Var}_\eta(T(X)) = \nabla^2 A(\eta).$$
As a check, the second derivative of the log-likelihood is $\nabla^2\ell(\eta;X) = -\nabla^2
A(\eta)$, deterministic and equal to $-\mathrm{Var}_\eta(T(X))$, confirming $J(\eta) = \mathbb
E_\eta[-\nabla^2\ell]$.

**Curved exponential family.** Now let $\theta \in \mathbb R$ index a *curve* $\eta(\theta)$
through the ambient $s$-dimensional natural parameter space,
$$p_\theta(x) = e^{\eta(\theta)'T(x) - A(\eta(\theta))}h(x).$$
By the chain rule, the score is
$$S_\theta(X) = \dot\ell(\theta;X) = \dot\eta(\theta)'\big(T(X) - \mathbb E_\theta[T(X)]\big) = \dot\eta(\theta)'S_{\eta(\theta)}(X),$$
the projection of the ambient score onto the tangent direction $\dot\eta(\theta) \in \mathbb R^s$.
The Fisher information is likewise
$$J(\theta) = \dot\eta(\theta)'J(\eta(\theta))\dot\eta(\theta).$$

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A curve traced by eta of theta through the ambient exponential-family parameter space, with its tangent vector at one point">
  <line x1="30" y1="195" x2="320" y2="195" stroke="currentColor" stroke-width="1"/>
  <line x1="30" y1="195" x2="30" y2="15" stroke="currentColor" stroke-width="1"/>
  <text x="300" y="212" font-size="12" fill="currentColor">η₁</text>
  <text x="10" y="18" font-size="12" fill="currentColor">η₂</text>
  <path d="M 60 190 Q 170 20 300 100" fill="none" stroke="currentColor" stroke-width="2"/>
  <circle cx="175" cy="82" r="3.5" fill="currentColor"/>
  <text x="120" y="108" font-size="12" fill="currentColor">η(θ₀)</text>
  <defs>
    <marker id="arrow089e" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#d97706"/>
    </marker>
  </defs>
  <line x1="175" y1="82" x2="240" y2="57" stroke="#d97706" stroke-width="2" marker-end="url(#arrow089e)"/>
  <text x="243" y="52" font-size="12" fill="#d97706">η̇(θ₀)</text>
  <text x="255" y="128" font-size="11" fill="currentColor">θ increasing →</text>
</svg>
<figcaption>The curved family traces a curve η(θ) through the ambient natural-parameter space. The
tangent vector η̇(θ₀) points in the direction of T(X) that is locally informative near θ₀; its
length sets the size of the Fisher information J(θ₀).</figcaption>
</figure>

Geometrically: the *direction* of $\dot\eta(\theta)$ picks out which linear combination of $T(X)$
is locally informative about $\theta$; its *magnitude* is the speed at which the curve is
traversed as $\theta$ moves. A "faster" parameterization of the same curve — the same subfamily of
distributions — produces a larger Fisher information, purely because $J(\theta)$ scales like
squared speed. This is not the data becoming more informative; it is the same unit-conversion
effect as with $g(\theta) = 12\theta$ above: the faster $P_{\eta(\theta)}$ moves away from
$P_{\eta(\theta \pm 0.1)}$, the better your chances of pinning $\theta$ down to within $0.1$.

**Curved Gaussian location family.** Concretely, let $X_1,\dots,X_n \overset{\text{iid}}\sim
N_d(\mu(\theta), I_d)$ for $\theta \in \mathbb R$, where $\mu(\theta) \in \mathbb R^d$ traces a
curve through the ambient $d$-dimensional Gaussian location family. In the ambient family the
score is
$$S_\mu^{(\mu)}(X) = \sum_i X_i - n\mu = n(\bar X - \mu), \qquad J^{(\mu)}(\mu) = nI_d,$$
so in the curved subfamily,
$$S_\theta(X) = n\dot\mu(\theta)'(\bar X - \mu(\theta)), \qquad J(\theta) = n\|\dot\mu(\theta)\|^2:$$
the sample size, times the squared speed of the parameterization.

## Sources

All material is from the "Score Function and Fisher Information" reader chapter of Berkeley
STAT210A, converted from three successive offerings; the offerings restate the same argument with
different degrees of polish, and this chapter takes the clearest version of each part rather than
repeating all three.

- **The score function, its motivation, and "is the score a statistic?"** — the tangent-family
  construction is from fall-2024 `reader/score-fisher.qmd` §1 ("Under construction") and its
  near-duplicate in fall-2025 `units/reader/score-fisher.html` §§1–3; the fuller discussion of why
  the score is a "local" sufficient statistic and the classroom exchange about whether it is a
  statistic is from fall-2025 `reader/score-fisher.html` §1 and fall-2026 `reader/score-fisher.qmd`
  (the two opening sections). fall-2026's text breaks off mid-sentence ("A third possibility is
  that we could be evaluating $\ell(\dots$") in the same place fall-2025's does; that unfinished
  fragment is omitted here rather than completed, since the source itself never finishes the
  thought.
- **Differential identities and the Fisher information matrix** — fall-2024 §2, fall-2025
  `reader` §2, fall-2025 `units/reader` §4, and fall-2026 §3, which are essentially identical
  across offerings.
- **The Cramér–Rao lower bound**, including the multivariate Rayleigh-quotient proof — the
  statement and the "expand to see proof" derivation are from fall-2024 §3 and fall-2025
  `units/reader` §5; the unit-conversion remark and the informal efficiency discussion are from
  fall-2025 `reader` §3 and fall-2026 §4. The formal definition
  $\mathrm{eff}_\delta(\theta)=\mathrm{CRLB}(\theta)/\mathrm{Var}_\theta(\delta)$ is from the
  separate "Efficiency" section of fall-2024 §4 and fall-2025 `units/reader` §6; both framings are
  merged here since they state the same identity.
- **Score and information additivity in i.i.d. samples** — fall-2024 §4 (first example),
  fall-2025 `reader` §4, fall-2025 `units/reader` §6 (first example), and fall-2026's fifth part.
- **Exponential family and curved exponential family examples** — fall-2024 §4 and fall-2025
  `units/reader` §6 (natural and curved exponential family only); fall-2025 `reader` §5 and
  fall-2026's sixth part add the curved Gaussian location family example. The Gaussian example
  breaks off mid-sentence in both of the latter two ("...times the parameterization speed. The")
  and is presented here only up to the last complete sentence.
- **Named but not in any supplied file**: the handwritten-notes figures for the tangent-family and
  curved-family discussion, which a callout in fall-2024 §1 and fall-2025 `units/reader` §1 asks
  to "add back in" but which were not part of the converted reader text. The diagram above is this
  chapter's own schematic of the curve/tangent-vector geometry described in the curved exponential
  family section, not a reproduction of that missing figure. The same callout also questions
  whether the tangent-family motivation duplicates the later curved exponential family example;
  the lecturer never resolved this in any of the three offerings, so this chapter keeps the
  tangent family briefly as motivation and treats the curved exponential family section as the
  worked-out computation.

Source files (berkeley-stat210a, CC BY 4.0):
[fall-2024 reader/score-fisher.qmd](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd),
[fall-2025 reader/score-fisher.html](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html),
[fall-2025 units/reader/score-fisher.html](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html),
[fall-2026 reader/score-fisher.qmd](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/score-fisher.qmd).

---

[← 71. Recitation Materials Index](71-recitation-materials-index.md) · [Contents](index.md) · [73. A Curved Gaussian Family →](73-a-curved-gaussian-family.md)
