---
title: "59. Asymptotic Distribution of the MLE"
course: "Berkeley Stat 210A"
chapter: 59
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 59. Asymptotic Distribution of the MLE

## What this covers

The maximum likelihood estimator $\hat\theta_n$ maximizes the log-likelihood of the data over
$\theta$. This chapter answers two questions about it as the sample size $n\to\infty$: does
$\hat\theta_n$ converge to the true parameter $\theta_0$ at all, and if so, at what rate and with
what limiting shape? It assumes the reader already has the likelihood, score and Hessian, the weak
law of large numbers and central limit theorem, Slutsky's theorem, and Jensen's inequality.

## Setup and notation

Data $X_1,\dots,X_n$ are drawn i.i.d. from $P_{\theta_0}$, a member of a parametric family
$\{P_\theta : \theta\in\Theta\}$ with densities $p_\theta$ against a common dominating measure. The
family is **identifiable**: $\theta\neq\theta_0 \implies P_\theta \neq P_{\theta_0}$, so different
parameter values really do give different distributions.

Write $\ell(\theta;x) = \log p_\theta(x)$ for the log-likelihood of a single observation, and
$\ell_n(\theta;X) = \sum_{i=1}^n \ell(\theta;X_i)$ for the log-likelihood of the whole sample. The
MLE is
$$\hat\theta_n \in \operatorname*{argmax}_{\theta\in\Theta} \ell_n(\theta;X)$$
(or anything that comes close enough to maximizing $\ell_n$ — an exact maximizer is not needed
anywhere below). A subscript $1$ on a quantity below — $\nabla\ell_1(\theta_0;X_i)$,
$J_1(\theta_0)$ — marks that it is a *per-observation* quantity, as opposed to the sum over the
whole sample.

## A heuristic argument for asymptotic normality — and where it breaks

Suppose for a moment that everything is smooth and well-behaved, and see what a direct Taylor
expansion suggests. Two facts about the log-likelihood evaluated at the truth $\theta_0$ (assumed
interior to $\Theta$) come for free from the ordinary CLT and WLLN applied to the i.i.d. per-
observation scores and Hessians:

$$\nabla\ell_1(\theta_0;X_i) \overset{\text{iid}}{\sim} (0,\, J_1(\theta_0)), \qquad
\frac{1}{\sqrt n}\nabla\ell_n(\theta_0;X) = \sqrt n\cdot\frac1n\sum_i \nabla\ell_1(\theta_0;X_i)
\ \overset{P_{\theta_0}}{\Longrightarrow}\ \mathcal N\bigl(0, J_1(\theta_0)\bigr),$$

$$\frac1n \nabla^2\ell_n(\theta_0;X) \ \overset{P_{\theta_0}}{\longrightarrow}\
\mathbb E_{\theta_0}\nabla^2\ell_1(\theta_0;X_i) = -J_1(\theta_0).$$

So $J_1(\theta_0)$ plays two roles at once — it is the covariance of the per-observation score,
and (with a sign) the limit of the averaged Hessian — the usual Fisher information matrix.

Now expand the first-order condition $0 = \nabla\ell_n(\hat\theta_n;X)$ around $\theta_0$:

$$0 = \nabla\ell_n(\hat\theta_n;X) = \nabla\ell_n(\theta_0;X) + \nabla^2\ell_n(\tilde\theta_n;X)
(\hat\theta_n - \theta_0)$$

for some $\tilde\theta_n$ between $\theta_0$ and $\hat\theta_n$ (mean value theorem). Rearranging,

$$\sqrt n(\hat\theta_n - \theta_0) = -\left(\frac1n \nabla^2\ell_n(\tilde\theta_n;X)\right)^{-1}
\frac{1}{\sqrt n}\nabla\ell_n(\theta_0;X).$$

If the bracketed matrix could be replaced by its limit $J_1(\theta_0)$, Slutsky's theorem would
immediately give
$$\sqrt n(\hat\theta_n-\theta_0) \Longrightarrow \mathcal N_d\bigl(0, J_1(\theta_0)^{-1}\bigr).$$

The gap is exactly the point $\tilde\theta_n$ at which the Hessian is evaluated: the CLT-and-WLLN
facts above only pin down the Hessian average *at $\theta_0$*, but $\tilde\theta_n$ is a random,
data-dependent point that merely lies between $\theta_0$ and $\hat\theta_n$. For the averaged
Hessian at $\tilde\theta_n$ to converge to the same limit $J_1(\theta_0)$, $\tilde\theta_n$ itself
has to converge to $\theta_0$ — and that requires $\hat\theta_n \overset{P}\to \theta_0$ first.
**Consistency of the MLE has to be established before this Taylor expansion can be trusted at
all**, which is why it is proved separately, first.

## Consistency, first pass: the truth maximizes the population objective

Ask directly: when does $\hat\theta_n \overset{P}\to \theta_0$? Define the per-observation
log-likelihood *ratio against the truth*,
$$W_i(\theta) = \ell(\theta;X_i) - \ell(\theta_0;X_i), \qquad \bar W_n(\theta) = \frac1n\sum_i
W_i(\theta).$$
Subtracting $\ell_n(\theta_0;X)$ from $\ell_n(\theta;X)$ does not depend on $\theta$, so it does not
move the maximizer: $\hat\theta_n$ maximizes $\bar W_n(\theta)$ exactly as it maximizes
$\ell_n(\theta;X)$.

By the ordinary WLLN, for each fixed $\theta$,
$$\bar W_n(\theta) \overset{P}{\longrightarrow} \mathbb E_{\theta_0} W_1(\theta) =: \mu(\theta).$$
This $\mu(\theta)$ is (minus) a Kullback–Leibler divergence:
$$\mu(\theta) = \mathbb E_{\theta_0}\log\frac{p_\theta(X)}{p_{\theta_0}(X)} = -D_{\mathrm{KL}}
(\theta_0\,\|\,\theta).$$
Jensen's inequality (log is concave) bounds this above by zero:
$$-D_{\mathrm{KL}}(\theta_0\,\|\,\theta) \le \log \mathbb E_{\theta_0}\frac{p_\theta(X)}{p_{\theta_0}
(X)} = \log\int_{p_{\theta_0}(x)>0} \frac{p_\theta(x)}{p_{\theta_0}(x)}\, p_{\theta_0}(x)\,d\mu(x)
\le \log 1 = 0,$$
with equality throughout **only if $p_\theta/p_{\theta_0}$ is almost-everywhere constant**, i.e.
only if $P_\theta = P_{\theta_0}$. Under identifiability this happens only at $\theta = \theta_0$.
So $\mu(\theta) \le 0$ with equality *iff* $\theta = \theta_0$: the population objective is
uniquely maximized at the truth.

That looks like it should already finish the argument — the sample objective converges pointwise
to something uniquely maximized at $\theta_0$ — but it is **not enough on its own**. $\hat\theta_n$
is the maximizer of the *entire function* $\bar W_n(\cdot)$, not of its value at any one $\theta$.
Pointwise convergence at each fixed $\theta$ says nothing about the shape of $\bar W_n$ as a whole:
it is consistent with $\bar W_n$ spiking upward at some wandering, sample-dependent location, even
though it settles down at every individual point. What is needed is convergence of $\bar W_n$ to
$\mu$ *uniformly* in $\theta$.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="The population objective mu(theta), peaked uniquely at the truth theta0, staying below a strictly negative level outside any ball around theta0">
  <rect x="40" y="20" width="100" height="170" fill="currentColor" fill-opacity="0.15"/>
  <rect x="220" y="20" width="100" height="170" fill="currentColor" fill-opacity="0.15"/>
  <line x1="30" y1="190" x2="330" y2="190" stroke="currentColor" stroke-width="1.2"/>
  <text x="337" y="194" font-size="12" fill="currentColor">θ</text>
  <line x1="30" y1="60" x2="330" y2="60" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2 3"/>
  <text x="34" y="52" font-size="11" fill="currentColor">μ(θ) = 0</text>
  <line x1="30" y1="65.6" x2="330" y2="65.6" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2 3"/>
  <text x="248" y="80" font-size="11" fill="currentColor">μ*ε</text>
  <polyline points="40,128.6 60,110.4 80,95 100,82.4 120,72.6 140,65.6 160,61.4 180,60 200,61.4 220,65.6 240,72.6 260,82.4 280,95 300,110.4 320,128.6" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <line x1="180" y1="186" x2="180" y2="194" stroke="currentColor" stroke-width="1.2"/>
  <text x="180" y="208" text-anchor="middle" font-size="12" fill="currentColor">θ₀</text>
  <line x1="140" y1="186" x2="140" y2="194" stroke="currentColor" stroke-width="1"/>
  <text x="140" y="208" text-anchor="middle" font-size="11" fill="currentColor">θ₀−ε</text>
  <line x1="220" y1="186" x2="220" y2="194" stroke="currentColor" stroke-width="1"/>
  <text x="220" y="208" text-anchor="middle" font-size="11" fill="currentColor">θ₀+ε</text>
  <text x="34" y="30" font-size="12" fill="currentColor">μ(θ) = −D_KL(θ₀ ‖ θ)</text>
</svg>
<figcaption>The population objective is uniquely maximized at θ₀; outside any ball of radius ε
around θ₀ (shaded) it stays at or below a strictly negative level μ*ε. A uniform error
δₙ = ‖W̄ₙ − μ‖∞ smaller than half this gap is enough to force the sample maximizer back inside the
ball — this is the mechanism the consistency proof below turns on.</figcaption>
</figure>

## A law of large numbers for random functions

To get uniform convergence, the lecture states a uniform law of large numbers for functions valued
in a space of continuous functions on a compact set. For compact $K$, let $C(K) = \{f : K\to
\mathbb R,\ \text{continuous}\}$, with the sup norm $\|f\|_\infty = \sup_{t\in K}|f(t)|$; say
$f_n\to f$ in this norm if $\|f_n-f\|_\infty \to 0$.

**Theorem (LLN for random functions).** Let $K$ be compact and $W_1, W_2,\dots \in C(K)$ i.i.d.,
with $\mathbb E\|W_1\|_\infty < \infty$. Let $\mu(t) = \mathbb E W_1(t)$. Then $\mu\in C(K)$, and
$$\mathbb P\left(\left\|\frac1n\sum_i W_i - \mu\right\|_\infty > \varepsilon\right) \to 0,$$
i.e. $\bar W_n \overset{P}\to \mu$ in the sup norm.

This is the tool that upgrades the pointwise convergence $\bar W_n(\theta)\to\mu(\theta)$ from the
previous section into the uniform statement $\|\bar W_n - \mu\|_\infty \overset{P}\to 0$ that
consistency actually needs, once $W_i(\cdot)$ is continuous on a compact parameter space and has an
integrable sup.

## Theorem: consistency of the MLE on a compact parameter space

**Assumptions.** $\log p_\theta(x)$ continuous in $\theta$ for every $x$; $\Theta$ compact;
$\mathbb E_{\theta_0}\left[\sup_{\theta\in\Theta}|W_1(\theta)|\right] < \infty$; the model
identifiable.

**Conclusion.** If $\hat\theta_n \in \operatorname*{argmax}_\theta \ell_n(\theta;X)$, then
$\hat\theta_n \overset{P}\to \theta_0$.

**Proof.** $W_1,\dots \in C(\Theta)$ are i.i.d. with mean function $\mu(\theta) = -D_{\mathrm{KL}}
(\theta_0\|\theta)$, and by the previous section $\mu(\theta_0)=0$ while $\mu(\theta)<0$ for
$\theta\neq\theta_0$ — the truth is the unique maximizer of $\mu$. Let $\delta_n = \|\bar W_n -
\mu\|_\infty$, which $\overset{P}\to 0$ by the uniform LLN.

Fix $\varepsilon>0$; the goal is $\mathbb P(\|\hat\theta_n-\theta_0\|\ge\varepsilon)\to 0$. Let
$\widetilde\Theta_\varepsilon = \Theta \setminus B_\varepsilon(\theta_0) = \{\theta\in\Theta :
\|\theta-\theta_0\|\ge\varepsilon\}$, which is compact, and set
$$\mu_\varepsilon^* = \max_{\theta\in\widetilde\Theta_\varepsilon}\mu(\theta) < 0 = \mu(\theta_0),
\qquad W_\varepsilon^* = \max_{\theta\in\widetilde\Theta_\varepsilon} \bar W_n(\theta).$$
If $\hat\theta_n$ lands outside the $\varepsilon$-ball, then in particular $\bar W_n$ at $\hat
\theta_n$ — which is at least $\bar W_n(\theta_0)$, since $\hat\theta_n$ maximizes $\bar W_n$ over
all of $\Theta$ — is no larger than $W_\varepsilon^*$. So
$$\mathbb P_{\theta_0}(\|\hat\theta_n-\theta_0\|\ge\varepsilon) \le \mathbb P_{\theta_0}
\bigl(W_\varepsilon^* \ge \bar W_n(\theta_0)\bigr).$$
Now $W_\varepsilon^* \le \mu_\varepsilon^* + \delta_n$ (every value of $\bar W_n$ on
$\widetilde\Theta_\varepsilon$ is within $\delta_n$ of the corresponding value of $\mu$, which is
at most $\mu_\varepsilon^*$ there), and $\bar W_n(\theta_0) \ge \mu(\theta_0) - \delta_n =
-\delta_n$ (since $\mu(\theta_0)=0$). So the event $W_\varepsilon^*\ge \bar W_n(\theta_0)$ forces
$\mu_\varepsilon^* + \delta_n \ge -\delta_n$, i.e. $2\delta_n \ge -\mu_\varepsilon^*$, a fixed
positive number. Hence
$$\mathbb P_{\theta_0}(\|\hat\theta_n-\theta_0\|\ge\varepsilon) \le \mathbb P_{\theta_0}
\bigl(2\delta_n \ge -\mu_\varepsilon^*\bigr) \to 0,$$
since $\delta_n \overset{P}\to 0$ and $-\mu_\varepsilon^*>0$ is fixed. $\blacksquare$

**Corollary (non-compact $\Theta = \mathbb R^d$).** Keep the same assumptions, restricted to any
compact set, but now suppose there is some $R<\infty$ large enough that $\mathbb P_{\theta_0}(\|
\hat\theta_n - \theta_0\| > R) \to 0$ — i.e. the (unconstrained) MLE stays within a fixed ball with
probability tending to one. Then $\hat\theta_n \overset{P}\to \theta_0$ on the non-compact space
too.

*Proof.* Let $\widetilde\Theta = \{\theta : \|\theta-\theta_0\|\le R\}$ and $\widetilde\theta_n =
\operatorname*{argmax}_{\theta\in\widetilde\Theta} p_\theta(X)$, the MLE restricted to this
compact ball. The theorem gives $\widetilde\theta_n \overset{P}\to \theta_0$. Also $\mathbb P(\hat
\theta_n \neq \widetilde\theta_n) = \mathbb P_{\theta_0}(\hat\theta_n \notin \widetilde\Theta) \to
0$ by the tightness assumption. So $\hat\theta_n - \widetilde\theta_n \overset{P}\to 0$, and
$\hat\theta_n = \widetilde\theta_n + (\hat\theta_n - \widetilde\theta_n) \overset{P}\to \theta_0$.
$\blacksquare$

The corollary reduces the non-compact case entirely to a tail bound: the only way consistency can
fail on an unbounded parameter space is for $\hat\theta_n$ to wander off to a non-negligible
distance from $\theta_0$; ruling that out is the only extra work needed.

## Theorem: the asymptotic distribution of the MLE

This makes the heuristic Taylor argument rigorous, using consistency as the missing ingredient.

**Assumptions.** The model identifiable; $\Theta$ compact; $\mathbb E_{\theta_0}\left[\sup_{\theta
\in\Theta}|W_1(\theta)|\right]<\infty$; $\ell(\theta;x) = \log p_\theta(x)$ has two continuous
derivatives in $\theta$; $\mathbb E_{\theta_0}\sup_{\theta\in\Theta}\|\nabla^2\ell_1(\theta;X_i)\|
<\infty$; and the information matrix $J_1(\theta_0) = \mathbb E_{\theta_0}\nabla^2\ell_1(\theta_0;
X_i)$ is positive definite (so, in particular, invertible).

**Conclusion.** $\sqrt n(\hat\theta_n - \theta_0) \Rightarrow \mathcal N\bigl(0, J_1(\theta_0)^{-1}
\bigr)$.

**Proof.** Start from the Taylor identity derived earlier,
$$\sqrt n(\hat\theta_n-\theta_0) = \left(-\frac1n\nabla^2\ell_n(\tilde\theta_n)\right)^{-1}
\nabla\ell_n(\theta_0) \Big/ \sqrt n,$$
with $\tilde\theta_n$ between $\theta_0$ and $\hat\theta_n$. The compact-space theorem above gives
$\hat\theta_n\overset{P}\to \theta_0$, and since $\tilde\theta_n$ is sandwiched between $\theta_0$
and $\hat\theta_n$, $\tilde\theta_n \overset{P}\to \theta_0$ too.

Define $V_i(\theta) = -\nabla^2\ell_1(\theta;X_i) \in C(\Theta)$; by assumption $\mathbb E_{\theta_0}
\|V_1\|_\infty<\infty$, so the uniform LLN applies: with $v(\theta) = \mathbb E_{\theta_0}V_1(\theta)
\in C(\Theta)$ — note $v(\theta_0) = J_1(\theta_0)$ — and $\bar V_n(\theta) = \frac1n\sum_i V_i
(\theta)$,
$$\|\bar V_n - v\|_\infty \overset{P}\longrightarrow 0.$$
Now bound the quantity actually appearing in the Taylor identity by a triangle inequality that
splits it into a uniform-convergence term and a continuity term:
$$\left\|-\frac1n\nabla^2\ell_n(\tilde\theta_n) - J_1(\theta_0)\right\| \le \underbrace{\|\bar V_n
(\tilde\theta_n) - v(\tilde\theta_n)\|}_{\le\ \|\bar V_n - v\|_\infty\ \overset{P}\to\ 0} +
\underbrace{\|v(\tilde\theta_n) - v(\theta_0)\|}_{\overset{P}\to\ 0\ \text{since}\ v\ \text{cts.
and}\ \tilde\theta_n\overset{P}\to\theta_0}.$$
Both pieces vanish in probability — the first because $\tilde\theta_n$, wherever it lands, is
within the uniform error of $\bar V_n$; the second by continuity of $v$ composed with the
convergence of $\tilde\theta_n$ itself. So $-\frac1n\nabla^2\ell_n(\tilde\theta_n) \overset{P}\to
J_1(\theta_0)$, and since matrix inversion is continuous at the invertible matrix $J_1(\theta_0)$,
$$\left(-\frac1n\nabla^2\ell_n(\tilde\theta_n)\right)^{-1} \overset{P}\longrightarrow J_1(\theta_0)^
{-1}.$$
Combining this with $\frac{1}{\sqrt n}\nabla\ell_n(\theta_0) \Rightarrow \mathcal N(0,J_1(\theta_0))$
by Slutsky's theorem gives
$$\sqrt n(\hat\theta_n-\theta_0) \Longrightarrow \mathcal N_d\bigl(0, J_1(\theta_0)^{-1}\bigr).
\qquad\blacksquare$$

One honest caveat, flagged in the lecture itself: the uniform LLN above was stated for real-valued
($K\to\mathbb R$) random functions, so as given the argument is fully justified only for $d=1$. The
same proof goes through for $d>1$ with a version of the uniform LLN for matrix- or vector-valued
functions, but that extension is not spelled out here.

## The local picture near $\theta_0$

The Taylor argument has a geometric reading, sketched only briefly (and left unfinished) in the
notes: near $\theta_0$, expand $\ell_n(\theta) - \ell_n(\theta_0)$ to second order,
$$\ell_n(\theta) - \ell_n(\theta_0) \approx \dot\ell_n(\theta_0)(\theta-\theta_0) + \frac12
\ddot\ell_n(\theta_0)(\theta-\theta_0)^2.$$
This is a random parabola in $\theta$: its linear coefficient is the score $\dot\ell_n(\theta_0)$,
which by the CLT above is itself approximately $\mathcal N(0, nJ_1(\theta_0))$, and its curvature is
governed by the Hessian, which concentrates near $-nJ_1(\theta_0)$. The MLE is the peak of this
parabola, so its location relative to $\theta_0$ is driven by the size of the (random) linear term
divided by the (near-deterministic) curvature — the same ratio that appears in the Taylor identity
above. The source material breaks off mid-derivation at exactly this point in both later years'
notes, so this is recorded here only as the intuition behind the proof, not as a separate
derivation.

## Sources

- **Berkeley STAT 210A, Fall 2024**, handwritten lecture 22 ("MLE consistency"), reconstructed
  pages: `01-asymptotic-dist-of-mle.md` (the heuristic Taylor sketch and the observation that
  consistency must come first), `03-consistency-of-mle.md` (the KL-divergence argument for the
  population objective, and the statement of the uniform LLN for random functions),
  `04-theorem-consistency-of-mle-for-compact.md` (the compact-space consistency theorem and its
  non-compact corollary), and `05-theorem-asymptotic-distribution-of-mle.md` (the rigorous
  asymptotic normality theorem). This is the fullest of the three years' notes and forms the
  backbone of the chapter.
- **Berkeley STAT 210A, Fall 2025 and Fall 2026**, handwritten lecture 22, `lecture22-mle-
  consistency.md` (identical outlines in both years): supply the same heuristic Taylor sketch as
  the Fall 2024 notes, plus the start of a section titled "Asymptotic Picture ($d=1$)" giving the
  quadratic-approximation intuition used in the closing section above. Both transcriptions cut off
  mid-equation at exactly the same point, inside the display of $\dot\ell_n(\theta_0) \approx
  \mathcal N(0, nJ_1(\theta_0))$ — the rest of that section, and whatever picture it drew, is not
  present in any of the supplied material.
- All source pages are model reconstructions of handwritten PDF slides with no text layer, flagged
  in each source file as unverified equation-by-equation; the exposition, connective explanation
  and the diagram in this chapter are new, built to make the compressed handwritten
  equations readable as a continuous argument.
- No slides, transcript, or exercise set were supplied for this lecture.

---

[← 58. MLE: Consistency and Efficiency](58-mle-consistency-and-efficiency.md) · [Contents](index.md) · [60. Wald, Score, and Likelihood-Ratio Tests (part 1) →](60-wald-score-and-likelihood-ratio-tests-part-1.md)
