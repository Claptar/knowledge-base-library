---
title: "58. MLE: Consistency and Efficiency"
course: "Berkeley Stat 210A Fall 2024"
chapter: 58
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 58. MLE: Consistency and Efficiency

## What this covers

This chapter derives the large-sample behaviour of the maximum likelihood estimator (MLE), first
exactly for one-parameter exponential families and then in the general smooth-model setting. It
assumes familiarity with exponential families (natural parameter, sufficient statistic, log-partition
function), the delta method, convergence in probability and in distribution, Slutsky's theorem, and
the Cramér–Rao lower bound (CRLB) and Fisher information.

## The maximum likelihood estimator

Given a dominated family $\mathcal{P} = \{P_\theta : \theta \in \Theta\}$ with densities $p_\theta$
(with respect to some common dominating measure), the maximum likelihood estimator is

$$\hat{\theta}_{\text{MLE}}(X) = \operatorname*{argmax}_{\theta \in \Theta} p_\theta(X) = \operatorname*{argmax}_{\theta \in \Theta} \ell(\theta; X),$$

where $\ell(\theta;X) = \log p_\theta(X)$ is the log-likelihood.

Two remarks worth keeping in mind before doing any asymptotics:

- The $\operatorname{argmax}$ need not exist, need not be unique, and — even when it exists and is
  unique — need not be computable in closed form.
- The MLE does not depend on how the model is parameterized or on the choice of dominating measure.
  In particular it is *equivariant*: the MLE of $g(\theta)$, for any function $g$, is
  $g(\hat{\theta}_{\text{MLE}})$.

## MLE in an exponential family

Take a one-observation exponential family in natural parameter $\eta$,

$$p_\eta(x) = e^{\eta' T(x) - A(\eta)} h(x),$$

so that

$$\ell(\eta; X) = \eta' T(X) - A(\eta) + \log h(X).$$

Differentiating, and using that $\nabla A(\eta) = \mathbb{E}_\eta T(X)$ for an exponential family,

$$\nabla \ell(\eta; X) = T(X) - \mathbb{E}_\eta T(X).$$

Setting the score to zero, the MLE $\hat\eta$ is the value that reproduces the observed sufficient
statistic as a mean: it solves

$$T(X) = \mathbb{E}_{\hat\eta}\, T(X),$$

if such an $\eta$ exists in $\Theta$.

There is at most one such solution. The Hessian of the log-likelihood is

$$\nabla^2 \ell(\eta; X) = -\operatorname{Var}_\eta(T),$$

which is negative definite unless some linear combination $v'T$ is almost surely constant — and in
that case the parameterization is redundant (some coordinate of $\eta$ is not identified) and can be
dropped. Away from that degenerate case the log-likelihood is strictly concave, so it has at most
one stationary point, and that point is the global maximum.

Write $\mu = \dot\psi(\eta) := \nabla A(\eta)$ for the mean-value parameterization. Then the moment
equation above reads $T = \dot\psi(\hat\eta)$, i.e.

$$\hat\eta = \dot\psi^{-1}(T).$$

## Asymptotic normality in the scalar case

Now let $X_1, \dots, X_n$ be iid from a *scalar* natural exponential family, $\eta \in \Xi \subseteq
\mathbb{R}$, and let $\bar{T} = \frac{1}{n}\sum_i T(X_i)$. By the equivariance of the MLE applied to
iid samples, $\hat\eta = \dot\psi^{-1}(\bar{T})$.

Assume $\eta$ lies in the interior $\Xi^\circ$ of the natural parameter space. There,
$\dot\psi(\eta) = \ddot{A}(\eta) > 0$ — the mean function is strictly increasing because it is the
variance of $T$, which is positive for a non-degenerate family. Hence $\dot\psi^{-1}$ is continuous
and differentiable, with, by the inverse function rule,

$$(\dot\psi^{-1})'(\mu) = \frac{1}{\dot\psi(\dot\psi^{-1}(\mu))} = \frac{1}{\ddot{A}(\eta)}.$$

**Consistency.** By the law of large numbers, $\bar{T} \xrightarrow{P_\eta} \mu$. Since $\dot\psi^{-1}$
is continuous, the continuous mapping theorem gives

$$\hat\eta = \dot\psi^{-1}(\bar{T}) \xrightarrow{P_\eta} \dot\psi^{-1}(\mu) = \eta.$$

**Asymptotic normality.** The central limit theorem gives

$$\sqrt{n}(\bar{T} - \mu) \Rightarrow N\big(0,\ \operatorname{Var}_\eta(T(X_1))\big) = N(0,\ \ddot{A}(\eta)).$$

(In the $\mu$-parameterization, the information from one observation is
$J_1(\mu) = \operatorname{Var}(T)^{-1} = \ddot{A}(\eta)^{-1}$ — information transforms by the square
of the reparameterization derivative, and $d\eta/d\mu = 1/\ddot{A}(\eta)$.)

Applying the delta method to $\hat\eta = \dot\psi^{-1}(\bar{T})$ with derivative $1/\ddot{A}(\eta)$,

$$\sqrt{n}(\hat\eta - \eta) \Rightarrow N\left(0,\ \frac{1}{\ddot{A}(\eta)^2} \cdot \ddot{A}(\eta)\right) = N\left(0, \frac{1}{\ddot{A}(\eta)}\right).$$

Since the Fisher information from a single observation in the natural parameterization is
$J_1(\eta) = \operatorname{Var}_\eta(T(X_i)) = \ddot{A}(\eta)$, this says

$$\hat\eta \approx N\left(\eta,\ \frac{1}{nJ_1(\eta)}\right).$$

The MLE is asymptotically unbiased, asymptotically Gaussian, and its asymptotic variance is exactly
the Cramér–Rao bound $1/(nJ_1(\eta))$ — it is *asymptotically efficient*. Equivalently,
$\operatorname{corr}(\bar{T}, \hat\eta) \to 1$: to first order $\hat\eta$ carries exactly the
information that $\bar{T}$ does.

## A warning: the Poisson example

The asymptotic picture above is clean, but it can coexist with badly-behaved finite-sample moments.
Take $X_1, \dots, X_n$ iid $\text{Pois}(\theta)$ and reparameterize by the natural parameter
$\eta = \log\theta$. By equivariance, $\hat\eta = \log\bar{X}$.

The CLT gives $\sqrt{n}(\bar{X} - \theta) \Rightarrow N(0,\theta)$, and the delta method with
$g(\theta) = \log\theta$, $g'(\theta) = 1/\theta$, gives

$$\sqrt{n}(\hat\eta - \eta) = \sqrt{n}(\log\bar{X} - \log\theta) \Rightarrow N\!\left(0,\ \theta \cdot \frac{1}{\theta^2}\right) = N(0, \theta^{-1}).$$

So far this matches the general result exactly. But for *every* finite $n$ and every $\theta > 0$,

$$P_\theta(\hat\eta = -\infty) = P_\theta(X_1 = 0)^n = e^{-\theta n} > 0,$$

since $\bar{X} = 0$ occurs with positive probability whenever every $X_i = 0$. Consequently

$$\mathbb{E}[\hat\eta] = -\infty, \qquad \operatorname{Var}(\hat\eta) = \infty$$

for every finite $n$ — the estimator's exact mean and variance are degenerate even though its
asymptotic distribution is a perfectly ordinary $N(\eta, 1/(n\theta))$. The MLE can have embarrassing
finite-sample performance despite being asymptotically optimal.

## Why this isn't a contradiction

The resolution is a general fact about convergence in distribution: it does not see what happens on
an event whose probability is going to zero, no matter how badly behaved the estimator is on that
event.

**Proposition.** If $P(B_n) \to 0$, $X_n \Rightarrow X$, and $Z_n$ is an arbitrary sequence of random
variables, then

$$X_n \mathbf{1}_{B_n^c} + Z_n \mathbf{1}_{B_n} \;\Rightarrow\; X.$$

**Proof.** For any $\varepsilon > 0$, $P(\|Z_n \mathbf{1}_{B_n}\| > \varepsilon) \le P(B_n) \to 0$, so
$Z_n \mathbf{1}_{B_n} \xrightarrow{P} 0$. Also $\mathbf{1}_{B_n^c} \xrightarrow{P} 1$. Slutsky's
theorem then gives the claim. $\blacksquare$

In the Poisson example, $B_n = \{\bar{X} = 0\}$ has $P_\theta(B_n) = e^{-\theta n} \to 0$, so however
badly $\hat\eta$ behaves on $B_n$ (it is $-\infty$ there), it contributes nothing to the limiting
distribution of $\sqrt{n}(\hat\eta - \eta)$. What it does wreck is any statement about the *exact*
mean or variance of $\hat\eta$, since those integrate over $B_n$ regardless of how small its
probability is. Convergence in distribution and convergence of moments are genuinely different
questions, and an estimator can be impeccable in the first sense while failing the second at every
finite $n$.

## Toward a general theory: setting up Fisher information

The exponential family computation above suggests that the MLE is asymptotically efficient whenever
the model is smooth enough. The general setup: $X_1, \dots, X_n$ iid $p_\theta$, $\theta \in \Theta
\subseteq \mathbb{R}^d$, with $p_\theta$ smooth in $\theta$ (for instance, two continuous, integrable
derivatives — a condition that can be relaxed).

Write $\ell_1(\theta; X_i) = \log p_\theta(X_i)$ for the per-observation log-likelihood and
$\ell_n(\theta; X) = \sum_{i=1}^n \ell_1(\theta; X_i)$ for the log-likelihood of the full sample. The
Fisher information from a single observation is

$$J_1(\theta) = \operatorname{Var}_\theta\big(\nabla \ell_1(\theta; X_i)\big) = -\mathbb{E}\big[\nabla^2 \ell_1(\theta; X_i)\big],$$

the two expressions being equal by the usual information identity. Information from the full sample
adds over independent observations, $J_n(\theta) = \operatorname{Var}_\theta(\nabla \ell_n(\theta;X))
= nJ_1(\theta)$ — the source notes break off mid-derivation at exactly this point, so the general
consistency and asymptotic-normality argument for $\hat\theta_{\text{MLE}}$ that this setup is
building toward is not covered here.

## Sources

- Both `handwritten/lecture21-mle.pdf` conversions — berkeley-stat210a fall-2025 and fall-2026 —
  contain identical content for this lecture (the course taught twice with the same material); this
  chapter draws on that one lecture, read once, from
  `docs/statistics/berkeley/stat210a/fall-2025/handwritten/lecture21-mle.md` (fall-2026 copy is
  identical).
- These are model reconstructions of a handwritten PDF with no text layer; per their banners, every
  displayed equation is unverified and the prose is a paraphrase of the handwriting. This chapter
  reproduces the equations as given in the reconstruction and does not independently re-derive or
  check them against the original PDF.
- The source excerpt ends mid-equation, inside the derivation of the additivity of Fisher information
  ($J_n(\theta) = nJ_1(\theta)$); the general treatment of asymptotic efficiency it is building toward
  (beyond the exponential-family case already covered) is not present in the supplied material.
- No slides, transcript, or exercises were supplied for this lecture.

---

[← 57. MLE in Exponential Families](57-mle-in-exponential-families.md) · [Contents](index.md) · [59. Asymptotic Distribution of the MLE →](59-asymptotic-distribution-of-the-mle.md)
