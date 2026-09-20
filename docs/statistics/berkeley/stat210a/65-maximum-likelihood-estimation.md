---
title: "65. Maximum Likelihood Estimation"
course: "Berkeley Stat 210A Fall 2024"
chapter: 65
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 65. Maximum Likelihood Estimation

## What this covers

This chapter covers the maximum likelihood estimator (MLE): how it is defined for a general
dominated statistical family, what it looks like for the exponential family and two of its
standard members, and the two asymptotic properties that make it the default estimator of choice —
asymptotic efficiency (matching the Cramér–Rao bound in the limit) and consistency (converging to
the true parameter as $n\to\infty$). It assumes exponential families, the delta method, the CLT and
LLN, convergence in probability and in distribution, Slutsky's theorem, and Fisher information.

## The maximum likelihood estimator

For a dominated family $\mathcal P = \{P_\theta : \theta \in \Theta\}$ with densities $f_\theta$
(with respect to some common dominating measure), the maximum likelihood estimator maximizes the
joint density of the data over $\theta$:

$$
\hat\theta_{\mathrm{MLE}}(X) = \arg\max_{\theta\in\Theta} p_\theta(X)
 = \arg\max_{\theta \in \Theta}\prod_{i=1}^n f_\theta(X_i)
 = \arg\max_{\theta\in\Theta} \ell_n(\theta; X),
$$

where $\ell_n(\theta;X) = \sum_{i=1}^n \log f_\theta(X_i)$ is the log-likelihood: maximizing the
product is the same as maximizing its logarithm, which is what turns the problem into a sum and
makes the law of large numbers available later on.

Two remarks matter before doing anything further with this definition.

1. The $\arg\max$ need not exist, need not be unique, and need not be computable in closed form —
   nothing in the definition guarantees any of the three.
2. The MLE does not depend on how the family is parameterized or on which dominating measure the
   density is written against, and it is *equivariant*: the MLE of $g(\theta)$ is
   $g(\hat\theta_{\mathrm{MLE}})$ for any function $g$. Maximizing $p_\theta(X)$ over $\theta$ and
   then applying $g$ gives the same answer as re-expressing the likelihood in terms of $g(\theta)$
   and maximizing that directly.

## Examples in the exponential family

### Uniqueness of the MLE

Write a natural exponential family as

$$
\ell(\eta; X) = \eta^{\mathsf T} T(X) - A(\eta) + \log h(X).
$$

For $n$ iid observations, the score equation $\nabla_\eta \ell_n(\eta) = 0$ reduces to a moment
condition. Writing $m(\eta) = \nabla A(\eta) = \mathbb E_\eta[T(X)]$ for the mean-value map, the MLE
(if it exists) solves

$$
m(\hat\eta) = \overline{T(X)},
$$

i.e. it sets the population mean of the sufficient statistic, as a function of $\eta$, equal to its
observed sample average. Since $\ell''(\eta;X) = -\mathrm{Var}_\eta[T(X)]$ is negative
*semi*definite, and strictly negative definite unless $T(X)$ is almost surely constant (in which
case the parameterization was redundant to begin with), the log-likelihood is strictly concave in
the non-degenerate case. A strictly concave function has at most one stationary point, so **at most
one solution to the score equation exists** — existence is a separate question (the moment equation
can fail to have a solution at all), but uniqueness, when a solution exists, is automatic.

### Normal distribution

Let $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} N(\theta,\sigma^2)$ with $\sigma^2$ known. Write this
as a natural exponential family with natural parameter $\eta = \theta/\sigma^2$, sufficient
statistic $T(X) = X$, and $h(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-x^2/2\sigma^2}$; the mean-value
map is $m(\eta) = \mathbb E_\eta[T(X)] = \sigma^2\eta$, so $m^{-1}(\theta) = \theta/\sigma^2$ and the
MLE of $\eta$ is $\hat\eta_n = \bar X/\sigma^2$.

Two facts pin down its asymptotic behavior:

- **Consistency.** $\bar X \xrightarrow{p} \theta$ by the law of large numbers, so by the continuous
  mapping theorem $\hat\eta_n = m^{-1}(\bar X) \xrightarrow{p} \theta/\sigma^2 = \eta$.
- **Asymptotic normality.** Since $\sqrt n(\bar X - \theta) \xrightarrow{d} N(0,\sigma^2)$ (the
  ordinary CLT, as $\mathrm{Var}(X)=\sigma^2$), the delta method applied to $m^{-1}$ gives
$$
\sqrt n(\hat\eta_n - \eta) \xrightarrow{d} N\!\left(0, \big[m^{-1\prime}(\theta)\big]^2\sigma^2\right)
 = N(0, 1/\sigma^2).
$$

The Fisher information in the natural parameterization is $J(\eta) = \mathrm{Var}_\eta[T(X)] =
\sigma^2$, so this asymptotic variance is exactly $J(\eta)^{-1}$: the MLE is asymptotically an
unbiased Gaussian estimator that **achieves the Cramér–Rao lower bound**.

### Poisson distribution — a cautionary tale

Let $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} \mathrm{Poisson}(\theta)$, natural parameter
$\eta = \log\theta$, $T(X) = X$. Since $\mathbb E[X] = \mathrm{Var}(X) = \theta$, the CLT gives
$\sqrt n(\bar X - \theta) \xrightarrow{d} N(0,\theta)$, and by equivariance $\hat\eta_n =
\log\bar X$. The delta method (with $g(\theta)=\log\theta$, $g'(\theta) = 1/\theta$) gives

$$
\sqrt n(\log\bar X - \log\theta) \xrightarrow{d} N(0, \theta^{-1}),
$$

again exactly the inverse Fisher information — the MLE of $\eta$ is asymptotically efficient here
too. But look at what happens at any *finite* $n$: since a Poisson variable can equal $0$,

$$
\mathbb P(\bar X = 0) = \mathbb P(X_1 = 0)^n = e^{-n\theta} > 0.
$$

With this small but positive probability, $\hat\eta_n = \log 0 = -\infty$: the estimator of $\eta$
is not even finite. **The MLE can have embarrassingly bad finite-sample performance despite being
asymptotically optimal.** Asymptotic efficiency is a statement about the limit, not a guarantee
about any particular $n$.

## A lemma for handling bad events

The Poisson example raises a real question: if $\hat\eta_n$ is occasionally undefined, in what
sense is it still "asymptotically normal"? The following lemma makes statements like that precise,
by showing that a rare bad event can be patched over without touching the limit.

> **Lemma.** If $\mathbb P(B_n) \to 1$, $X_n \xrightarrow{d} X$, and $Z_n$ is an arbitrary sequence
> of random variables, then $X_n 1_{B_n} + Z_n 1_{B_n^c} \xrightarrow{d} X$.

*Why it holds.* Since $\mathbb P(\|Z_n 1_{B_n^c}\| > \epsilon) \le \mathbb P(B_n^c) \to 0$, we get
$Z_n 1_{B_n^c} \xrightarrow{p} 0$; also $1_{B_n} \xrightarrow{p} 1$. Slutsky's theorem then combines
these facts with $X_n \xrightarrow{d} X$ to give the claim. In words: **any zany behavior on an
event whose probability vanishes has no effect on convergence in distribution** — the estimator can
be defined arbitrarily ($Z_n$) on the bad event $B_n^c$, and the limiting distribution only sees
the good event.

## Asymptotic efficiency

The exponential-family computations above generalize to a much broader class of models. Let
$X_1,\dots,X_n \stackrel{\text{iid}}{\sim} p_\theta$, $\theta \in \mathbb R^d$, with $p_\theta$
smooth in $\theta$ (two continuous, integrable derivatives is enough; this can be relaxed). Write
$\ell_i(\theta;X) = \log p_\theta(X_i)$ for the per-observation log-likelihood,
$\ell_n(\theta;X) = \sum_{i=1}^n \ell_i(\theta;X)$, the **score** $S_n(\theta) =
\nabla_\theta \ell_n(\theta;X)$, and the Fisher information $J_n(\theta) =
\mathrm{Var}_\theta[S_n(\theta)] = n J_1(\theta)$ (information adds over independent observations).

An estimator sequence $\hat\theta_n$ is **asymptotically efficient** if

$$
\sqrt n(\hat\theta_n - \theta) \xrightarrow{d} N\big(0, J_1(\theta)^{-1}\big),
$$

i.e. its limiting variance matches the per-observation inverse Fisher information — the Cramér–Rao
bound, attained in the limit. This carries over to any differentiable functional of $\theta$ by the
delta method: if $g$ is differentiable at $\theta$,

$$
\sqrt n\big(g(\hat\theta_n) - g(\theta)\big) \xrightarrow{d}
 N\!\left(0, \nabla g(\theta)^{\mathsf T} J_1(\theta)^{-1} \nabla g(\theta)\right),
$$

and $g(\hat\theta_n)$ also achieves the transformed Cramér–Rao bound whenever $\hat\theta_n$ does.

## The asymptotic distribution of the MLE

Now specialize $\hat\theta_n$ to the MLE itself, and ask whether it is asymptotically efficient in
general — not just in the exponential family. Write $\theta_0$ for the true value generating the
data. Two facts about the score at the truth follow from the usual regularity conditions
(differentiating $\int p_\theta = 1$ under the integral sign):

$$
\mathbb E_{\theta_0}[S_n(\theta_0;X)] = n\,\mathbb E_{\theta_0}[\nabla \ell_i(\theta_0;X_i)] = 0,
\qquad
\mathbb E_{\theta_0}[-\nabla^2 \ell_n(\theta_0;X)] = J_n(\theta_0),
$$

the second being the **information identity**: the Fisher information can be computed either as the
variance of the score or as the expected negative curvature of the log-likelihood. Because
$S_n(\theta_0;X)$ is a sum of $n$ iid mean-zero terms with covariance $J_n(\theta_0)$, the ordinary
CLT gives $S_n(\theta_0;X)/\sqrt n \xrightarrow{d} N(0, J_1(\theta_0))$.

**Informal argument.** The MLE satisfies the first-order condition $S_n(\hat\theta_n;X) = 0$.
Taylor-expanding the score around $\theta_0$,

$$
0 = S_n(\hat\theta_n;X) \approx S_n(\theta_0;X) + \nabla S_n(\theta_0;X)(\hat\theta_n - \theta_0),
$$

and replacing the random Hessian $\nabla S_n(\theta_0;X)$ by its expectation $-J_n(\theta_0)$ gives
$\hat\theta_n - \theta_0 \approx J_n(\theta_0)^{-1}S_n(\theta_0;X)$, hence

$$
\sqrt n(\hat\theta_n - \theta_0) \approx J_1(\theta_0)^{-1}\,\frac{S_n(\theta_0;X)}{\sqrt n}
 \xrightarrow{d} N\big(0, J_1(\theta_0)^{-1}\big).
$$

The MLE is, informally, asymptotically efficient. The argument is only informal for a reason worth
stating plainly: it Taylor-expands around $\theta_0$ and then treats $\hat\theta_n$ as already close
to $\theta_0$ — which is exactly the **consistency** of the MLE, a fact that has not yet been
established and is needed to justify the expansion in the first place. A rigorous version of the
argument has to establish consistency first; that is what the last part of this chapter does.

### Quadratic approximation of the log-likelihood

The same expansion, kept one order further, describes the *shape* of the log-likelihood surface
near $\theta_0$ rather than just the location of its maximizer:

$$
\ell_n(\theta) \approx \ell_n(\theta_0) + (\theta-\theta_0)^{\mathsf T} S_n(\theta_0)
 - \tfrac12(\theta-\theta_0)^{\mathsf T} J_n(\theta_0)(\theta-\theta_0).
$$

This is a random quadratic in $\theta$: a Gaussian linear term (since $S_n(\theta_0)$ is
asymptotically normal) plus a deterministic curvature term set by $J_n(\theta_0)$. Completing the
square shows it has exactly the shape of a Gaussian log-density,

$$
N\big(J_n(\theta_0)^{-1}S_n(\theta_0),\ J_n(\theta_0)^{-1}\big).
$$

Re-expressing the same quadratic around its own maximizer $\hat\theta_n$ instead of $\theta_0$,

$$
\ell_n(\theta) - \ell_n(\theta_0) \approx -\frac n2 (\theta - \hat\theta_n)^{\mathsf T} J_1(\theta_0)
 (\theta - \hat\theta_n) + \text{const},
$$

which is the same fact seen from the other end: near its peak, the log-likelihood looks like a
downward paraboloid centered at $\hat\theta_n$ with curvature $nJ_1(\theta_0)$ — the source of the
Gaussian shape derived above.

## Consistency of the MLE

Let $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} f_{\theta_0}$ and let $\theta_n$ be any (near-)
maximizer of $\ell_n(\theta;X)$ over $\Theta$; it is enough for $\theta_n$ to come close to
maximizing $\ell_n$, since an exact maximizer need not exist. The natural question is: when does
$\ell_n \to \ell$ in a strong enough sense that its maximizer tracks the maximizer of the limit?

Assume the model is **identifiable**: $P_\theta \ne P_{\theta_0}$ for $\theta \ne \theta_0$. Recall
the Kullback–Leibler divergence, $D(g\|f) = \mathbb E_g\big[\log \frac{g(X)}{f(X)}\big]$, and the
elementary inequality $\log(g/f) \ge 1 - f/g$ (from $\log x \ge 1-1/x$), strict unless $f=g$.

Define, for each observation, the log-likelihood-ratio contribution $W_i(\theta) =
\ell_i(\theta;X_i) - \ell_i(\theta_0;X_i)$ and its population mean $W(\theta) =
\mathbb E_{\theta_0}[W_i(\theta)]$ — the re-centered population log-likelihood. Trivially
$W(\theta_0) = 0$, and for any other $\theta$,

$$
W(\theta) = -\mathbb E_{\theta_0}\!\left[\log\frac{f_{\theta_0}(X)}{f_\theta(X)}\right]
 = -D(f_{\theta_0}\|f_\theta) \le 0,
$$

with equality iff $f_\theta = f_{\theta_0}$ a.e., i.e. (by identifiability) iff $\theta=\theta_0$.
So **$\theta_0$ is the unique maximizer of the population log-likelihood** $W$ — the population
version of "the MLE targets the truth."

### Why pointwise convergence isn't enough

The sample log-likelihood ratio $\bar W_n(\theta) = \frac1n\sum_i W_i(\theta)$ is an average of iid
terms, so for each *fixed* $\theta$ the ordinary law of large numbers gives $\bar W_n(\theta)
\xrightarrow{p} W(\theta)$. That is not enough to conclude $\hat\theta_n \xrightarrow{p} \theta_0$,
for two reasons: (1) $\hat\theta_n$ depends on the entire random function $\theta \mapsto
\ell_n(\theta)$, not on its value at any single point, and (2) what is needed is convergence of
$\bar W_n$ to $W$ *uniformly* in $\theta$, not merely at each $\theta$ separately — the same gap
that separates a pointwise law of large numbers from a Glivenko–Cantelli-type uniform statement.

**Compact convergence.** For a compact set $K$, let $C(K)$ be the continuous real functions on $K$
with the sup norm $\|f\| = \sup_{x\in K}|f(x)|$; say $f_n \to f$ in this norm if $\|f_n - f\| \to 0$
— uniform convergence on $K$.

**Uniform LLN for random functions.** If $K$ is compact and $W_1, W_2,\dots \in C(K)$ are iid with
$\mathbb E\|W_1\| < \infty$ and $\mathbb E[W_i(\theta)] = W(\theta)$, then $\bar W_n \in C(K)$ and
$\mathbb P(\|\bar W_n - W\| > \epsilon) \to 0$ for every $\epsilon > 0$: the sample log-likelihood
converges to the population log-likelihood uniformly on $K$, in probability.

### The argmax theorem

Uniform convergence of the objective is exactly what is needed to transfer convergence of a
function to convergence of its maximizer — a general fact about maximizing random functions
("M-estimation"), not specific to likelihoods:

> **Theorem (Keener 9.4).** Let $G_n$ be random and $g$ fixed, both continuous on a compact $K$.
> If $G_n \to g$ uniformly on $K$ in probability, and $g$ has a **unique** maximizer $t^*$ on $K$,
> then any maximizer $t_n$ of $G_n$ over $K$ satisfies $t_n \xrightarrow{p} t^*$.

*Why it holds.* Fix $\epsilon > 0$ and let $B_\epsilon = \{t : \|t-t^*\| < \epsilon\}$,
$K_\epsilon = K \setminus B_\epsilon$ — still compact, since $K$ is compact and $B_\epsilon$ is open.
Because $t^*$ is the *unique* maximizer of $g$ and $K_\epsilon$ excludes it, $g$ attains a strictly
smaller maximum there: let $\delta = g(t^*) - \max_{t\in K_\epsilon} g(t) > 0$.

Suppose $t_n \in K_\epsilon$ (the sample maximizer has strayed at least $\epsilon$ from $t^*$). Since
$t_n$ maximizes $G_n$ over all of $K$, $G_n(t_n) \ge G_n(t^*)$. On the event $\|G_n - g\| < \delta/2$,

$$
G_n(t^*) > g(t^*) - \tfrac\delta2, \qquad
G_n(t_n) < g(t_n) + \tfrac\delta2 \le \max_{K_\epsilon} g + \tfrac\delta2 = g(t^*) - \tfrac\delta2,
$$

which forces $G_n(t_n) < g(t^*) - \delta/2 < G_n(t^*) \le G_n(t_n)$ — a contradiction. So the event
$t_n \in K_\epsilon$ can only happen when $\|G_n-g\| \ge \delta/2$, i.e.

$$
\mathbb P(t_n \in K_\epsilon) \le \mathbb P\big(\|G_n - g\|_\infty \ge \tfrac\delta2\big) \to 0.
$$

Since $\epsilon$ was arbitrary, $t_n \xrightarrow{p} t^*$ — the same mechanism as $\bar X_n
\xrightarrow{p}\mu$, but for the location of a maximum rather than a mean.

<figure>
<svg viewBox="0 0 420 240" role="img" aria-label="Why the sample maximizer of a uniformly converging objective cannot stray from the population maximizer">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <polygon points="0 0, 10 5, 0 10" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="20" y1="200" x2="400" y2="200" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="405" y="205" font-size="12" fill="currentColor">t</text>
  <rect x="170" y="40" width="60" height="160" fill="currentColor" fill-opacity="0.15"/>
  <text x="200" y="192" text-anchor="middle" font-size="11" fill="currentColor">B&#x3b5;(t*)</text>
  <path d="M 30 170 C 80 130 130 105 170 100 C 185 97 190 40 200 40 C 210 40 215 97 230 100 C 270 105 320 130 370 170" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="200" y1="40" x2="200" y2="200" stroke="currentColor" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="200" y="215" text-anchor="middle" font-size="12" fill="currentColor">t*</text>
  <circle cx="200" cy="40" r="3" fill="currentColor"/>
  <text x="200" y="30" text-anchor="middle" font-size="11" fill="currentColor">g(t*)</text>
  <circle cx="170" cy="100" r="3" fill="currentColor"/>
  <circle cx="230" cy="100" r="3" fill="currentColor"/>
  <line x1="20" y1="100" x2="400" y2="100" stroke="currentColor" stroke-width="1" stroke-dasharray="4,3"/>
  <text x="240" y="95" font-size="11" fill="currentColor">max over K&#x3b5; = g(t*) &#8722; &#x3b4;</text>
  <line x1="20" y1="70" x2="400" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="2,3"/>
  <text x="240" y="65" font-size="11" fill="currentColor">g(t*) &#8722; &#x3b4;/2</text>
  <line x1="355" y1="40" x2="355" y2="100" stroke="currentColor" stroke-width="1"/>
  <line x1="349" y1="40" x2="361" y2="40" stroke="currentColor" stroke-width="1"/>
  <line x1="349" y1="100" x2="361" y2="100" stroke="currentColor" stroke-width="1"/>
  <text x="363" y="73" font-size="12" fill="currentColor">&#x3b4;</text>
</svg>
<figcaption>The compactness argument behind the argmax theorem. Since $g$ is uniquely maximized at
$t^*$, its values on $K_\epsilon = K \setminus B_\epsilon(t^*)$ stay below $g(t^*) - \delta$. Once
$G_n$ is uniformly within $\delta/2$ of $g$, a maximizer of $G_n$ cannot land in $K_\epsilon$
without beating $G_n(t^*)$, which it cannot do — so the sample maximizer is trapped inside the
shrinking ball around $t^*$.</figcaption>
</figure>

### Consistency of the MLE, assembled

> **Theorem.** Let $X_1,\dots,X_n \stackrel{\text{iid}}{\sim} f_{\theta_0}$, with densities
> $p_\theta$, $\theta\in\Theta$. Assume: (1) $p_\theta$ continuous in $\theta$; (2) $\Theta$
> compact; (3) $\mathbb E_{\theta_0}\big[\sup_\theta |f_\theta(X)/f_{\theta_0}(X)|\big] < \infty$;
> (4) $\mathbb E_{\theta_0}\big[\sup_\theta |W_i(\theta)|\big] < \infty$; (5) the model is
> identifiable. Then $\hat\theta_n \xrightarrow{p} \theta_0$.

This assembles the pieces above exactly: identifiability plus the Kullback–Leibler computation
gives a unique population maximizer $\theta_0$; the envelope conditions (3)–(4) supply the
domination $\mathbb E\|W_i\| < \infty$ that the uniform law of large numbers needs, so $\bar W_n \to
W$ uniformly on the compact $\Theta$; the argmax theorem then transfers this to $\hat\theta_n
\xrightarrow{p} \theta_0$.

The source material breaks off mid-sentence at exactly this point (see Sources), so this is also
where this chapter's account of consistency ends: the theorem is stated and its proof strategy
assembled from the pieces built above, but the final clause of the theorem's proof is not present
in the notes and is not reconstructed here.

## Sources

No slides, transcript or problem set were supplied for this chapter — only converted reader pages.
The same three-chapter reader (Maximum Likelihood Estimation / Asymptotic Distribution of the MLE /
Consistency of the MLE) appears four times in the input list, once per year the course was taught,
and the copies agree apart from formatting:

- `fall-2024/reader/maximum-likelihood/01-maximum-likelihood-estimation.md`,
  `02-asymptotic-distribution-of-mle.md`, `03-consistency-of-mle.md` — converted via the lossless
  `markdown` route (numbered lists preserved), used as the primary source below.
- `fall-2026/reader/maximum-likelihood/{01,02,03}-...md` — byte-identical in content to the
  fall-2024 copy.
- `fall-2025/reader/maximum-likelihood/{01,02,03}-...md` and the duplicate
  `fall-2025/units/reader/maximum-likelihood/{01,02,03}-...md` — converted via the `pandoc-html`
  route, same content with numbered lists collapsed into run-on sentences and section numbers
  1–1.4, 2, 3, 4 attached to the headings.

Section-by-section:

- "The maximum likelihood estimator" through "Poisson distribution": `01-maximum-likelihood-
  estimation.md`, from the opening definition through the Poisson example (§1–§1.3 in the
  fall-2025 numbering).
- "A lemma for handling bad events": same file, the convergence-in-distribution lemma (§1.4).
- "Asymptotic efficiency": same file, final section (§2).
- "The asymptotic distribution of the MLE" and "Quadratic approximation of the log-likelihood":
  `02-asymptotic-distribution-of-mle.md`, in full.
- "Consistency of the MLE" through "The argmax theorem": `03-consistency-of-mle.md`, from the
  identifiability/KL argument through the proof sketch of the Keener 9.4 argmax theorem.
- "Consistency of the MLE, assembled": same file, closing theorem. **The source itself ends
  mid-sentence** — all four copies stop at "Then $\hat\theta_n \xrightarrow{p}\theta_0$ if ..."
  without completing the clause, so that ending is not reproduced here.
- The textbook reference "Keener 9.4" (Robert Keener, *Theoretical Statistics*) is named in the
  source as the origin of the argmax theorem but the book itself was not supplied as input.

---

[← 64. Wald and Score Tests](64-wald-and-score-tests.md) · [Contents](index.md) · [66. Measure Theory for Probability →](66-measure-theory-for-probability.md)
