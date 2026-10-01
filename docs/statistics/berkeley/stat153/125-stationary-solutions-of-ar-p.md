---
title: "125. Stationary Solutions of AR(p)"
course: "Berkeley Stat 153"
chapter: 125
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 125. Stationary Solutions of AR(p)

## What this covers

This chapter answers a single question about the autoregressive model: given the defining
equation of an $\text{AR}(p)$ process, when does a *stationary* solution to it exist, and when it
exists, is it expressible in terms of past noise (causal) or does it require future noise
(non-causal)? It assumes the reader already knows the $\text{MA}(q)$ and $\text{AR}(p)$ model
definitions, the notion of a stationary process, and the autocorrelation function (ACF). The tool
developed to answer the question is the backshift operator, used to turn the AR difference
equation into an algebraic equation that can be "solved" like $y_t = \phi(B)^{-1}\epsilon_t$.

## Review: $\text{MA}(q)$

The moving-average model of order $q$ is
$$y_t = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \dots + \theta_q \epsilon_{t-q},$$
with $\epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2)$. Because $y_t$ is an explicit finite
sum of the $\epsilon$'s, this process is always stationary — no condition on the $\theta_j$ is
needed. Its ACF $\rho(h)$ vanishes for every $|h| > q$: correlation between $y_t$ and $y_{t-h}$ is
only possible while the two share a common $\epsilon$ in their sums, and once the lag exceeds $q$
they no longer do. This "cutting off" of the ACF after lag $q$ is the diagnostic signature of an
$\text{MA}(q)$ model: if the sample ACF of a dataset looks negligible past some lag $q$, that is
evidence for fitting an $\text{MA}(q)$.

## The $\text{AR}(p)$ equation is only implicit

The autoregressive model of order $p$ is defined by the equation
$$y_t - \phi_1 y_{t-1} - \dots - \phi_p y_{t-p} = \phi_0 + \epsilon_t. \tag{1}$$

Unlike the $\text{MA}(q)$ case, this does not *hand you* $y_t$: it is an implicit definition, and
$y_t$ is any collection of random variables satisfying (1). It turns out (1) can have more than one
solution, and whether a given solution is stationary depends both on the parameters
$\phi_1,\dots,\phi_p$ and on *which* solution is being considered. Working this out is the content
of the rest of the chapter.

## $\text{AR}(1)$: the model where everything can be checked by hand

Take $p=1$:
$$y_t - \phi_1 y_{t-1} = \phi_0 + \epsilon_t. \tag{2}$$

There are three regimes, according to $|\phi_1|$.

**$|\phi_1| < 1$.** Equation (2) has a unique stationary solution
$$y_t = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty \phi_1^j \epsilon_{t-j}. \tag{3}$$
The infinite sum makes sense because $|\phi_1|<1$ forces $\phi_1^j \to 0$ rapidly. In this solution
$\epsilon_t$ is independent of $y_{t-1}, y_{t-2}, \dots$ — the noise at time $t$ has not yet acted on
the past values of $y$. This is the **causal stationary $\text{AR}(1)$**: $y_t$ is written purely in
terms of present and past noise.

**$|\phi_1| > 1$.** Equation (2) again has a unique stationary solution, but now
$$y_t = \frac{\phi_0}{1-\phi_1} - \sum_{j=0}^\infty \frac{\epsilon_{t+j}}{\phi_1^j}. \tag{4}$$
This series converges because $|\phi_1|>1$ makes $\phi_1^{-j}\to 0$ rapidly. Here it is *not* true
that $\epsilon_t$ is independent of the past of $y$; instead $\epsilon_t$ is independent of
$y_{t+1}, y_{t+2}, \dots$. This is the **non-causal stationary $\text{AR}(1)$**: writing down $y_t$
requires noise that has not happened yet.

**$|\phi_1| = 1$.** No stationary solution exists. The more commonly used case is $\phi_1 = 1$,
where (2) becomes
$$y_t - y_{t-1} = \phi_0 + \epsilon_t. \tag{5}$$
The differenced series $y_t - y_{t-1}$ is (a constant plus) Gaussian white noise. When $\phi_0=0$,
(5) is exactly the random walk.

### Solving (2) with the backshift operator

The three regimes above can be *derived*, not just stated, using the backshift operator $B$, which
satisfies $B^k y_t = y_{t-k}$ for any integer $k$ (with $B^0 = 1$ the identity). Equation (2) becomes
$$\phi(B) y_t = \phi_0 + \epsilon_t, \qquad \phi(z) = 1 - \phi_1 z,$$
so formally
$$y_t = \frac{1}{\phi(B)}(\phi_0 + \epsilon_t).$$
The content of the argument is making sense of $1/\phi(B)$, and there are two candidate expansions
of $1/(1-r)$ as a power series:
$$\frac{1}{1-r} = 1 + r + r^2 + \dots \qquad \text{and} \qquad \frac{1}{1-r} = -\frac{1}{r}\left(1 + \frac1r + \frac{1}{r^2} + \dots\right) = -\sum_{j=1}^\infty r^{-j}. \tag{6}$$
The first is the usual geometric series and converges for $|r|<1$; the second is obtained by
factoring $-1/r$ out and expanding in $1/r$ instead, and converges for $|r|>1$. Substituting
$r = \phi_1 B$:
$$\frac{1}{1-\phi_1 B} = \sum_{j=0}^\infty \phi_1^j B^j \quad (\text{use when } |\phi_1|<1), \qquad \frac{1}{1-\phi_1B} = -\sum_{j=1}^\infty \frac{B^{-j}}{\phi_1^j} \quad (\text{use when } |\phi_1|>1).$$
Applying the first to $\phi_0 + \epsilon_t$ and using $B^j \epsilon_t = \epsilon_{t-j}$ recovers (3)
exactly; applying the second recovers (4). The rule for which expansion to use is simply: pick
whichever one produces rapidly decaying coefficients. When $|\phi_1| = 1$, neither expansion decays,
which is the algebraic reflection of the fact that (2) has no stationary solution in that case.

## General $\text{AR}(p)$: factor, then apply the same two formulae

The backshift method extends to every $p \ge 1$. Writing (1) as $\phi(B)y_t = \phi_0 + \epsilon_t$
with
$$\phi(B) = 1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p,$$
the strategy is to factor the polynomial into monomials and handle each factor separately with (6).
Write
$$\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p = (1-a_1z)\cdots(1-a_pz), \tag{7}$$
so that $\phi(B) = (1-a_1B)\cdots(1-a_pB)$. The numbers $a_1,\dots,a_p$ are the *reciprocals* of the
roots of $\phi(z)$: if $\phi(z)$ has roots $z_1,\dots,z_p$, then $a_j = 1/z_j$. Some $a_j$ can be
complex, since a real-coefficient polynomial can have complex roots (in conjugate pairs); $|a_j|$
then means the modulus.

Then
$$y_t = \prod_{k=1}^p \frac{1}{1-a_kB}\,(\phi_0+\epsilon_t),$$
and for each factor $1/(1-a_kB)$ the same rule as before applies: use the forward expansion
$\sum_j a_k^j B^j$ when $|a_k| < 1$, and the backward expansion $-\sum_j B^{-j}/a_k^j$ when
$|a_k| > 1$. So
$$y_t = \prod_{k:\,|a_k|<1}\left(\sum_{j=0}^\infty a_k^j B^j\right)\prod_{k:\,|a_k|>1}\left(\sum_{j=1}^\infty \frac{B^{-j}}{a_k^j}\right)(\phi_0+\epsilon_t). \tag{8}$$

**All $|a_k| < 1$.** Every factor uses the forward expansion, and multiplying them out gives
$$y_t = \phi_0\sum_{j_1,\dots,j_p \ge 0} a_1^{j_1}\cdots a_p^{j_p} \;+\; \sum_{j_1,\dots,j_p\ge0} a_1^{j_1}\cdots a_p^{j_p}\,\epsilon_{t-j_1-\dots-j_p}.$$
Every $a_k$ has modulus below 1, so the multiple sum converges. Collecting terms by
$j=j_1+\dots+j_p$ writes this as
$$y_t = \mu + \sum_{j=0}^\infty \psi_j \epsilon_{t-j}$$
for some constant $\mu$ and coefficients $\psi_0,\psi_1,\dots$ — an expression purely in present and
past noise. This is the **causal stationary $\text{AR}(p)$** solution, generalizing (3).

**Some $|a_k| > 1$.** As soon as one factor needs the backward expansion, the product in (8) mixes
positive and negative powers of $B$, and expanding gives
$$y_t = \mu + \sum_{j=-\infty}^{\infty} \psi_j \epsilon_{t-j}$$
for coefficients $\psi_j$ now indexed over all integers. Because this involves $\epsilon_{t-j}$ for
negative $j$ — i.e. future noise — this is a **non-causal stationary** solution, generalizing (4).

**Some $|a_k| = 1$.** Neither formula in (6) applies to that factor, so (8) cannot be made sense of.
As in the $\text{AR}(1)$ case, this is the signal that a stationary solution fails to exist.

<figure>
<svg viewBox="0 0 320 240" role="img" aria-label="Unit circle in the complex plane with a root reciprocal inside contributing a causal, past-noise expansion and one outside contributing a non-causal, future-noise expansion">
  <circle cx="160" cy="120" r="80" fill="none" stroke="currentColor" stroke-width="1.25" stroke-dasharray="4 3"/>
  <line x1="160" y1="30" x2="160" y2="210" stroke="currentColor" stroke-width="0.75" stroke-opacity="0.4"/>
  <line x1="70" y1="120" x2="270" y2="120" stroke="currentColor" stroke-width="0.75" stroke-opacity="0.4"/>
  <circle cx="188" cy="98" r="4" fill="currentColor"/>
  <text x="196" y="90" font-size="12" fill="currentColor">$a_k$, $|a_k|&#60;1$</text>
  <text x="196" y="104" font-size="11" fill="currentColor">causal: past $\epsilon_{t-j}$</text>
  <circle cx="245" cy="65" r="4" fill="currentColor"/>
  <text x="222" y="50" font-size="12" fill="currentColor">$a_k$, $|a_k|&#62;1$</text>
  <text x="222" y="64" font-size="11" fill="currentColor">non-causal: future $\epsilon_{t+j}$</text>
  <text x="160" y="26" text-anchor="middle" font-size="11" fill="currentColor">unit circle</text>
</svg>
<figcaption>Each reciprocal root $a_k$ of $\phi(z)$ contributes a forward (past-noise) or backward
(future-noise) expansion to $y_t$ according to whether it sits inside or outside the unit circle;
a root exactly on the circle blocks both expansions and stationarity fails.</figcaption>
</figure>

## Summary

To determine the nature of the solutions of the $\text{AR}(p)$ equation (1):

1. Compute the roots $z_1,\dots,z_p$ of $\phi(z) = 1 - \phi_1 z - \dots - \phi_p z^p$ and set
   $a_j = 1/z_j$.
2. If no $a_j$ has modulus exactly $1$ (equivalently, no root $z_j$ has modulus exactly $1$), there
   is a unique stationary solution to (1) — causal if every $|a_j|<1$, non-causal if at least one
   $|a_j|>1$.

The lecture's source material breaks off at this point, mid-list, before stating the remaining case
explicitly (some $|a_j|=1$, where no stationary solution exists) — that case was already worked out
above from (8) and matches the $\text{AR}(1)$ boundary case $|\phi_1|=1$.

## Sources

- Notes: `docs/statistics/berkeley/stat153/spring-2025/LectureTwentyTwo153248Spring2025.md`
  (STAT 153 & 248, UC Berkeley, Spring 2025, Lecture 22, Aditya Guntuboyina, April 15 2025) — the
  entire chapter, including the $\text{MA}(q)$ review, the $\text{AR}(p)$ definition, the
  $\text{AR}(1)$ regimes, the backshift-operator derivations, and the general $\text{AR}(p)$
  factorization argument.
- This source note is itself a model reconstruction of a PDF with no text layer ("fidelity:
  reconstructed"); its own header warns that the prose is paraphrased in places and every equation
  is unverified against the original slides. Nothing has been added beyond what that reconstruction
  contains, but the equations should be treated as unverified against the original lecture material
  the note was built from.
- The source note ends mid-sentence within the final summary list (item 1 of what was evidently a
  multi-item list); the concluding case for $|a_j|=1$ is not present in the supplied material and is
  only reconstructed here as a direct consequence of the argument already given, not copied from a
  missing final item.
- No slides, transcript, or exercises were supplied for this lecture.

---

[← 124. Box-Jenkins Strategy and SARIMA Models](124-box-jenkins-strategy-and-sarima-models.md) · [Contents](index.md) · [126. Simple Linear Regression →](126-simple-linear-regression.md)
