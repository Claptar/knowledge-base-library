---
title: "62. The Nonparametric Bootstrap"
course: "Berkeley Stat 210A Fall 2024"
chapter: 62
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 62. The Nonparametric Bootstrap

## What this covers

This chapter asks how to do inference when the sampling distribution $P$ itself is left completely
unspecified: no parametric family, just $X_1, \dots, X_n \overset{\text{iid}}{\sim} P$. It develops
the **plug-in estimator** for a functional $\theta(P)$, asks precisely when plugging in the empirical
distribution is a safe move, and then builds the **nonparametric bootstrap** — the general device for
getting a standard error, a bias correction, and a confidence interval for $\theta(P)$ when no formula
for its sampling distribution exists in closed form. It assumes the reader is comfortable with i.i.d.
sampling models, convergence in probability, and M-estimation (the KL-projection example below is the
same target as the MLE under model misspecification).

## The nonparametric model and its functionals

The setting is the nonparametric i.i.d. sampling model: $X_1, \dots, X_n \overset{\text{iid}}{\sim} P$,
where $P$ is an unknown distribution, unconstrained to lie in any parametric family. The object of
inference is a **functional** $\theta(P)$ — a number (or vector) computed from $P$ itself, rather than
from a finite-dimensional parameter indexing a family. Four examples fix the idea:

a) $\theta(P) = \operatorname{median}(P)$, for $X \in \mathbb{R}$.
b) $\theta(P) = \lambda_{\max}(\operatorname{Var}_P(X_i))$, the largest eigenvalue of the covariance
   matrix, for $X \in \mathbb{R}^d$.
c) $\theta(P) = \operatorname*{argmin}_{\theta \in \mathbb{R}^d} \mathbb{E}_P\left[(Y_i - \theta' X_i)^2\right]$,
   for $(X_i, Y_i) \overset{\text{iid}}{\sim} P$ — the best linear predictor of $Y$ from $X$ under $P$.
   This is well defined whether or not a linear model is actually true.
d) $\theta(P) = \operatorname*{argmin}_{\theta \in \Theta} D_{\mathrm{KL}}(P \parallel P_\theta)
   = \operatorname*{argmax}_{\theta} \mathbb{E}_P[\ell(\theta; X_i)]$ — the best-fitting member of a
   parametric family $\{P_\theta\}$, even when the family is misspecified and no $P_\theta$ equals $P$.
   This is exactly the target that the MLE is trying to estimate once you stop assuming the model is
   correct.

In each case $\theta$ is a map from distributions to numbers, and the question is how to estimate
$\theta(P)$ from a sample without knowing $P$.

### The plug-in estimator

Recall the **empirical distribution** of the sample,
$$\hat{P}_n = \frac{1}{n}\sum_{i=1}^n \delta_{X_i}, \qquad \hat{P}_n(A) = \frac{\#\{i : X_i \in A\}}{n}.$$
It is a genuine probability distribution — discrete, uniform on the $n$ observed points — and it is
completely known once the data is in hand.

The **plug-in estimator** of $\theta(P)$ is simply $\hat{\theta} = \theta(\hat{P}_n)$: replace the
unknown $P$ by the known $\hat{P}_n$ everywhere it appears in the definition of $\theta$. Applied to
the four examples above, this recovers exactly the natural estimators: (a) the sample median,
(b) the largest eigenvalue of the sample covariance, (c) the ordinary least squares estimator, and
(d) the maximum likelihood estimator for $\{P_\theta\}$. The plug-in principle is thus a single recipe
that reconstructs several familiar estimators as special cases, and it extends immediately to
functionals with no parametric analogue at all.

## Does the plug-in estimator work?

The plug-in estimator is only as good as the sense in which $\hat{P}_n$ approximates $P$, and that
depends entirely on which notion of convergence is meant.

- **Pointwise on events.** $\hat{P}_n(A) \overset{p}{\to} P(A)$ for every fixed measurable $A$ — this
  is just the law of large numbers applied to $\mathbf{1}\{X_i \in A\}$, and it holds without
  qualification.
- **Total variation** fails. $\sup_A |\hat{P}_n(A) - P(A)| \overset{p}{\not\to} 0$ whenever $P$ is
  continuous. Take $A_n = \{X_1, \dots, X_n\}$, the set of observed points: $\hat{P}_n(A_n) = 1$
  identically, while $P(A_n) = 0$ for every $n$ because $P$ is continuous and $A_n$ is finite. So the
  total-variation distance between $\hat{P}_n$ and $P$ never shrinks, no matter how large $n$ is.
- **Sup-norm on the CDF** succeeds, at least for $X \in \mathbb{R}$:
  $\sup_x |\hat{P}_n((-\infty, x]) - P((-\infty, x])| \overset{p}{\to} 0$. This is the
  **Glivenko–Cantelli theorem**: convergence of the empirical CDF to the true CDF, uniformly over $x$.

So $\hat{P}_n \to P$ is true in some topologies and false in others, and the right question is not
"does $\hat{P}_n$ converge to $P$" but "does it converge in a topology that $\theta$ respects." The
governing principle: if $\theta(P)$ is **continuous** with respect to some topology in which
$\hat{P}_n \overset{p}{\to} P$, then $\theta(\hat{P}_n) \overset{p}{\to} \theta(P)$ — the plug-in
estimator is consistent by a continuous-mapping argument. Total variation is too strong a topology to
be useful here (it essentially never holds for continuous $P$); the weak/Kolmogorov-type topology
underlying Glivenko–Cantelli is the one that plug-in estimators typically rely on.

### Two counterexamples

Continuity of $\theta$ is doing real work, and it can fail even for very simple-looking functionals.
Consider
$$\theta(P) = \mathbf{1}\{P \text{ is absolutely continuous}\} \qquad \text{and} \qquad
\theta(P) = \mathbf{1}\{P \text{ is integrable}\} = \mathbf{1}\{\mathbb{E}_P|X| < \infty\}.$$
The empirical distribution $\hat{P}_n$ is, for every sample and every $n$, a finite discrete
distribution supported on the $n$ observed points. It is therefore *always* integrable — trivially,
since it has finite support — and *never* absolutely continuous, since it is a sum of point masses.
Consequently $\theta(\hat{P}_n)$ is deterministically $1$ for the integrability functional and
deterministically $0$ for the absolute-continuity functional, for every $n$ and every sample,
regardless of what $P$ actually is. If $P$ is not integrable, or if $P$ is absolutely continuous, the
plug-in estimator is wrong with probability one and stays wrong as $n \to \infty$: no amount of data
fixes it, because these functionals are discontinuous at every $\hat{P}_n$ in the relevant topology.
The moral is that closeness of $\hat P_n$ to $P$ is necessary but not sufficient — the functional
itself has to be well behaved along the way $\hat P_n$ approaches $P$.

## Bootstrap standard errors

Suppose $\hat{\theta}_n(X)$ is some estimator of $\theta(P)$ — plug-in or otherwise. What is its
standard error? Apply the plug-in idea one level up: since we do not know the sampling distribution
of $\hat\theta_n$ under $P$, estimate it by the sampling distribution of the *same* estimator applied
to a fresh sample from $\hat{P}_n$ in place of $P$:
$$\widehat{\text{s.e.}}(\hat{\theta}_n) = \sqrt{\operatorname{Var}_{\hat{P}_n}(\hat{\theta}_n^*)},
\qquad
\operatorname{Var}_{\hat{P}_n}(\hat{\theta}_n^*)
= \operatorname{Var}_{X_1^*, \dots, X_n^* \overset{\text{iid}}{\sim} \hat{P}_n}
\big(\hat{\theta}_n(X_1^*, \dots, X_n^*)\big),$$
where the star notation marks a quantity computed from a *resampled* data set $X^*$, distinguished
from the original data $X$.

This variance is, in principle, computable exactly: sampling $X_1^*, \dots, X_n^*$ i.i.d. from
$\hat{P}_n$ means drawing $n$ points with replacement from the original sample, and there are only
$n^n$ possible such resampled vectors, so the "idealized" bootstrap estimator could be computed by
summing over all of them. In practice this is done by **Monte Carlo** instead:

For $b = 1, \dots, B$:
$$X_1^{*b}, \dots, X_n^{*b} \overset{\text{iid}}{\sim} \hat{P}_n \quad
(\text{i.e. sample } n \text{ points with replacement from the original data}),
\qquad \hat{\theta}^{*b} = \hat{\theta}(X_1^{*b}, \dots, X_n^{*b}).$$
$$\overline{\theta^*} = \frac{1}{B}\sum_{b=1}^B \hat{\theta}^{*b},
\qquad
\widehat{\text{s.e.}}(\hat{\theta}_n) = \sqrt{\frac{1}{B}\sum_{b=1}^B \big(\hat{\theta}^{*b} - \overline{\theta^*}\big)^2}.$$

The $B$ resamples are a numerical approximation to the exact ($n^n$-term) bootstrap quantity above;
$B$ is chosen large enough that Monte Carlo error is negligible next to the statistical error being
estimated.

## The real-world / bootstrap-world correspondence

It helps to keep two parallel pictures in mind, because every bootstrap quantity is literally the
same construction one level removed from the unobservable one.

<figure>
<svg viewBox="0 0 480 240" role="img" aria-label="Two parallel number lines showing the unknown real-world sampling distribution of an estimator around theta of P, and the known, simulable bootstrap-world sampling distribution around theta of P-hat-n.">
<defs>
<marker id="arrowhead" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
<polygon points="0 0, 8 4, 0 8" fill="currentColor"/>
</marker>
</defs>
<text x="20" y="30" font-size="12" fill="currentColor">Real world (unknown, observed once)</text>
<line x1="40" y1="70" x2="440" y2="70" stroke="currentColor" stroke-width="1.5"/>
<circle cx="150" cy="70" r="3" fill="none" stroke="currentColor"/>
<text x="150" y="95" text-anchor="middle" font-size="12" fill="currentColor">&#952;(P)</text>
<circle cx="230" cy="70" r="3" fill="currentColor"/>
<text x="230" y="45" text-anchor="middle" font-size="12" fill="currentColor">E_P[&#952;&#770;]</text>
<line x1="152" y1="58" x2="226" y2="58" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowhead)"/>
<text x="190" y="52" text-anchor="middle" font-size="11" fill="currentColor">Bias_P(&#952;&#770;)</text>
<line x1="190" y1="82" x2="270" y2="82" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowhead)"/>
<line x1="270" y1="82" x2="190" y2="82" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowhead)"/>
<text x="230" y="100" text-anchor="middle" font-size="11" fill="currentColor">s.e._P(&#952;&#770;)</text>
<text x="20" y="140" font-size="12" fill="currentColor">Bootstrap world (known, simulable at will)</text>
<line x1="40" y1="180" x2="440" y2="180" stroke="currentColor" stroke-width="1.5"/>
<circle cx="260" cy="180" r="3" fill="currentColor"/>
<text x="260" y="205" text-anchor="middle" font-size="12" fill="currentColor">&#952;(P&#770;_n)</text>
<circle cx="330" cy="180" r="3" fill="currentColor"/>
<text x="330" y="160" text-anchor="middle" font-size="12" fill="currentColor">E_(P&#770;_n)[&#952;&#770;*]</text>
<line x1="262" y1="168" x2="326" y2="168" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowhead)"/>
<text x="294" y="162" text-anchor="middle" font-size="11" fill="currentColor">Bias_(P&#770;_n)(&#952;&#770;*)</text>
<line x1="300" y1="192" x2="380" y2="192" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowhead)"/>
<line x1="380" y1="192" x2="300" y2="192" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrowhead)"/>
<text x="340" y="210" text-anchor="middle" font-size="11" fill="currentColor">s.e._(P&#770;_n)(&#952;&#770;*)</text>
</svg>
<figcaption>The real world has the true, unknown θ(P) and an estimator θ̂(X) with some bias and
spread around it under repeated sampling from P — but there is only one sample, so this sampling
distribution is never observed. The bootstrap world replaces P by the known P̂ₙ: θ(P̂ₙ) is
computable exactly, and the sampling distribution of θ̂* under repeated resampling from P̂ₙ can be
generated at will by Monte Carlo. Reading bias and spread off the bootstrap-world picture is the
whole idea.</figcaption>
</figure>

| | "Real world" | "Bootstrap world" |
| --- | --- | --- |
| Sampling distribution | $P$ (hidden) | $\hat{P}_n(X)$ (known) |
| Parameter | $\theta(P)$ | $\theta(\hat{P}_n(X))$ |
| Data set | $X_1, \dots, X_n \overset{\text{iid}}{\sim} P$, observed once | $X_1^*, \dots, X_n^* \overset{\text{iid}}{\sim} \hat{P}_n(X)$, generated at will |
| Estimator | $\hat{\theta}(X)$ | $\hat{\theta}^* = \hat{\theta}(X^*)$ |
| Sampling distribution of the estimator | centered near $\theta(P)$, unknown | centered near $\theta(\hat{P}_n(X))$, known/simulable |

Every bootstrap procedure in this chapter is the same move: take a quantity defined in terms of $P$
that cannot be computed, and substitute $\hat{P}_n$ for $P$ to get a quantity that can be computed —
possibly only by Monte Carlo, but computable in principle.

## Bootstrap bias correction

The bias of an estimator is
$$\operatorname{Bias}_P(\hat{\theta}_n) = \mathbb{E}_P\left[\hat{\theta}_n - \theta(P)\right].$$
Applying the same plug-in substitution as above,
$$\operatorname{Bias}_{\hat{P}_n}(\hat{\theta}_n^*) = \mathbb{E}_{\hat{P}_n}\left[\hat{\theta}_n^* - \theta(\hat{P}_n)\right]$$
is the bootstrap-world analogue, computed by the same kind of Monte Carlo loop as the standard error:

For $b = 1, \dots, B$: sample $X_1^{*b}, \dots, X_n^{*b} \overset{\text{iid}}{\sim} \hat{P}_n$ and set
$\hat{\theta}^{*b} = \hat{\theta}(X^{*b})$. Then
$$\overline{\theta^*} = \frac{1}{B}\sum_{b=1}^B \hat{\theta}^{*b}, \qquad
\widehat{\operatorname{Bias}}(\hat{\theta}_n) = \overline{\theta^*} - \theta(\hat{P}_n).$$

This estimated bias can be subtracted off to form the **bias-corrected estimator**
$$\hat{\theta}_n^{\text{BC}} = \hat{\theta}_n - \widehat{\operatorname{Bias}}(\hat{\theta}_n).$$

A subtlety worth holding onto: subtracting the *true* bias, $\hat\theta_n - \operatorname{Bias}_P(\hat\theta_n)$,
is always at least as good as $\hat\theta_n$ itself (it is, after all, unbiased). But subtracting the
*estimated* bias, $\hat\theta_n^{\text{BC}}$, is not guaranteed to be an improvement — the correction
itself is a random quantity computed from the same data, so it can add variance, and the net effect on
mean squared error is not automatically positive. Bias correction with an estimated bias is a
bias–variance trade, not a free lunch.

## Bootstrap confidence intervals

To build a confidence interval for $\theta(P)$, the key idea is a **root**: a quantity
$R_n(X, P)$, built from both the data and the (unknown) true distribution, whose distribution can be
used to pivot from a statement about $R_n$ to a statement about $\theta(P)$. The simplest root is
$$R_n(X, P) = \hat{\theta}_n(X) - \theta(P).$$
Suppose (hypothetically) that its sampling distribution
$$G_{n,P}(r) = \mathbb{P}_P\big(\hat\theta(X) - \theta(P) \le r\big)$$
were known. Let $r_1 = G_{n,P}^{-1}(\alpha/2)$ and $r_2 = G_{n,P}^{-1}(1 - \alpha/2)$ be its lower and
upper $\alpha/2$ quantiles. Then by definition
$$1 - \alpha = \mathbb{P}_P\big(r_1 \le \hat\theta_n - \theta \le r_2\big)
= \mathbb{P}_P\big(\theta \in [\hat\theta_n - r_2,\ \hat\theta_n - r_1]\big),$$
an exact $(1-\alpha)$ confidence interval for $\theta(P)$ — if only $G_{n,P}$ were known.

It generally is not, since it depends on the unknown $P$. Bootstrap it: replace $P$ by $\hat{P}_n$ to
get
$$G_{n,\hat{P}_n}(r) = \mathbb{P}_{\hat{P}_n}\big(\hat\theta(X^*) - \theta(\hat{P}_n) \le r\big),$$
which is a function of the observed data $X$ alone (not of the unknown $P$) and can therefore actually
be computed — by Monte Carlo:

For $b = 1, \dots, B$: sample $X_1^{*b}, \dots, X_n^{*b} \overset{\text{iid}}{\sim} \hat{P}_n$ and form
$R_n^{*b} = \hat\theta(X^{*b}) - \theta(\hat{P}_n)$. Return the empirical CDF of
$R_n^{*1}, \dots, R_n^{*B}$ as the estimate of $G_{n,\hat{P}_n}$, take its $\alpha/2$ and $1-\alpha/2$
quantiles $\hat{r}_1, \hat{r}_2$, and form
$$C_{n,\alpha} = [\hat\theta_n - \hat r_2,\ \hat\theta_n - \hat r_1].$$

The root need not be the plain difference $\hat\theta_n - \theta$. Other choices include the ratio
$R_n = \hat\theta_n(X)/\theta(P)$, or — usually the better choice — the **studentized root**
$$R_n(X, P) = \frac{\hat\theta_n(X) - \theta(P)}{\hat\sigma(X)},$$
where $\hat\sigma(X)$ is some estimate of $\text{s.e.}(\hat\theta_n)$ (for instance the bootstrap
standard error from above). The criterion for a good root is that its sampling distribution
$G_{n,P}$ should change *slowly* as $P$ varies, so that $G_{n,\hat{P}_n} \approx G_{n,P}$ even though
$\hat{P}_n \ne P$ — this is what makes the bootstrap approximation to the root's distribution
accurate. Studentizing typically achieves this better than the unstandardized difference, because it
removes the estimator's own scale from the picture. With the studentized root the interval becomes
$$C_{n,\alpha} = [\hat\theta_n - \hat r_2 \hat\sigma,\ \hat\theta_n - \hat r_1 \hat\sigma].$$

## The double bootstrap

Suppose theory guarantees that the bootstrap approximation to the root's distribution is asymptotically
exact, e.g.
$$\sup_{a < b} \big|G_{n,\hat{P}_n}([a,b]) - G_{n,P}([a,b])\big| \overset{p}{\to} 0.$$
This is an asymptotic statement, and it says nothing about how good the interval $C_{n,\alpha}$ is at
any particular, finite $n$. Define the actual coverage of the interval,
$$\gamma_{n,P}(\alpha) = \mathbb{P}_P\big(\theta(P) \in C_{n,\alpha}\big).$$
Asymptotic validity means $\gamma_{n,P}(\alpha) \to 1-\alpha$, but in finite samples it can miss badly
— a nominal "90% interval" might actually cover with probability $\gamma_{n,P}(0.1) = 0.87 < 0.9$.

The fix is to bootstrap the coverage function itself — the **double bootstrap**:

1. Estimate the unknown coverage function $\gamma_{n,P}(\cdot)$ by its plug-in analogue
   $\gamma_{n,\hat{P}_n}(\cdot)$.
2. Instead of using the nominal level $\alpha$, use whichever level $\hat\alpha$ the estimated coverage
   function says actually delivers $1 - \alpha$ coverage: solve $\hat\gamma(\hat\alpha) = 1 - \alpha$
   and report $C_{n,\hat\alpha}(X)$.

For example, if the estimated coverage function says the *nominal* 92% interval actually achieves 90%
coverage, then the calibrated level is $\hat\alpha = 0.08$ — report the interval that was nominally
built for 92% confidence, because that is the one that is really delivering 90%.

Estimating $\gamma_{n,\hat P_n}(\cdot)$ requires resampling from $\hat P_n$, computing the bootstrap
interval within that resample, and checking coverage — a bootstrap nested inside a bootstrap:

For $a = 1, \dots, A$ (outer resamples):
$$X_1^{*a}, \dots, X_n^{*a} \overset{\text{iid}}{\sim} \hat{P}_n, \qquad
\hat{P}_n^{*a} = \frac{1}{n}\sum_{i=1}^n \delta_{X_i^{*a}}.$$
For $b = 1, \dots, B$ (inner resamples, drawn from the outer resample):
$$X_1^{**a,b}, \dots, X_n^{**a,b} \overset{\text{iid}}{\sim} \hat{P}_n^{*a}, \qquad
R_n^{**a,b} = \big(\hat\theta_n(X^{**a,b}) - \theta(\hat{P}_n^{*a})\big) / \hat\sigma(X^{**a,b}).$$
Let $\hat{G}_n^{*a}$ be the empirical CDF of $R_n^{**a,1}, \dots, R_n^{**a,B}$. For each $\alpha$ on a
grid, form the inner bootstrap interval built from the outer resample,
$$C_{n,\alpha}^{*a} = \Big[\hat\theta_n^{*a} - \hat\sigma^{*a}\, r_2(\hat{G}_n^{*a}),\ \hat\theta_n^{*a} - \hat\sigma^{*a}\, r_1(\hat{G}_n^{*a})\Big].$$
Finally, for each $\alpha$ on the grid, estimate the coverage by the fraction of outer resamples whose
interval captured the (known) bootstrap-world truth $\theta(\hat{P}_n)$:
$$\hat\gamma(\alpha) = \frac{1}{A}\sum_{a=1}^A \mathbf{1}\{C_{n,\alpha}^{*a} \ni \theta(\hat{P}_n)\},$$
and solve $\hat\alpha = \hat\gamma^{-1}(1-\alpha)$ as the calibrated nominal level to actually report.

The double bootstrap is computationally expensive — $A \times B$ resamples rather than $B$ — but it
directly targets the object that matters at finite $n$: not whether the interval is asymptotically
correct, but whether it actually covers at the sample size in hand.

## Sources

Berkeley STAT 210A, lecture 25 ("Nonparametric estimation / bootstrap"), from the handwritten lecture
notes. The same lecture was taught, essentially verbatim, in three offerings of the course, and the
notes agree word for word and equation for equation across them; this chapter follows the fall-2026
version as primary text and uses the fall-2024 and fall-2025 versions only to cross-check the
transcription:

- Setting, examples (a)–(d), the plug-in estimator, and the discussion of when plug-in works
  (pointwise convergence, the total-variation counterexample, Glivenko–Cantelli, and the two
  discontinuous-functional counterexamples): `fall-2026/handwritten/lecture25-bootstrap/01-nonparametric-estimation.md`
  (also `fall-2024/.../01-nonparametric-estimation.md` and `fall-2025/.../01-nonparametric-estimation.md`).
- Bootstrap standard errors and the Monte Carlo algorithm:
  `fall-2026/handwritten/lecture25-bootstrap/02-bootstrap-standard-errors.md` (in fall-2024 this
  material sits inside `01-nonparametric-estimation.md`, and is split into its own file from
  fall-2025 on).
- Bootstrap bias correction and the "real world / bootstrap world" table and diagram:
  `fall-2026/handwritten/lecture25-bootstrap/03-bootstrap-bias-correction.md` (`fall-2024/.../02-bootstrap-bias-correction.md`).
- Roots, bootstrap confidence intervals, and the studentized root:
  `fall-2026/handwritten/lecture25-bootstrap/04-bootstrap-confidence-interval.md` (`fall-2024/.../03-bootstrap-confidence-interval.md`).
- The double bootstrap and its nested-resampling algorithm:
  `fall-2026/handwritten/lecture25-bootstrap/05-double-bootstrap.md` (`fall-2024/.../04-double-bootstrap.md`).

No slide deck, transcript, or problem set was supplied for this lecture, so there is no
`## Exercises` section. All source files carry the note that they were reconstructed by a model from
a handwritten PDF with no text layer, and that every equation is unverified against the original
scan; the diagram above renders the "real world / bootstrap world" picture that the fall-2025 and
fall-2026 notes describe as a table plus a hand-drawn sketch of two centered, spread-out
distributions, one hidden and one known.

---

[← 61. Wald, Score, and Likelihood-Ratio Tests (part 2)](61-wald-score-and-likelihood-ratio-tests-part-2.md) · [Contents](index.md) · [63. Multiple Testing and FWER →](63-multiple-testing-and-fwer.md)
