---
title: "122. Stationarity and Causality of AR(p)"
course: "Berkeley Stat 153"
chapter: 122
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 122. Stationarity and Causality of AR(p)

## What this covers

An $\text{AR}(1)$ or $\text{AR}(p)$ difference equation looks like it defines a time series, but a
recursion alone does not pin one down — infinitely many processes satisfy it, and most of them are
not stationary. This chapter answers: for which parameter values does a stationary solution exist,
is it unique, and does it depend only on the past ($\text{causal}$) or also on the future
($\text{non-causal}$)? It assumes the reader already knows the $\text{AR}(p)$ model, weak
stationarity (constant mean, autocovariance depending only on lag), the ACVF and ACF, and how
$\text{AR}(1)$ parameters are normally estimated by treating $\epsilon_t$ as independent of the
past.

## The AR(1) equation does not determine a unique process

The $\text{AR}(1)$ equation is
$$
y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t. \tag{1}
$$
This is only a recursion: it says how $y_t$ relates to $y_{t-1}$ and noise, but it does not by
itself say which process $\{y_t\}$ is. Many different time series satisfy (1).

Here is one that is not stationary. Fix $y_0 = 10$. Define $y_1, y_2, y_3, \dots$ forward using (1)
directly, and define $y_{-1}, y_{-2}, \dots$ backward using (1) rearranged with $y_{t-1}$ on the
left:
$$
y_{t-1} = -\frac{\phi_0}{\phi_1} + \frac{y_t}{\phi_1} - \frac{\epsilon_t}{\phi_1}. \tag{2}
$$
Equation (2) is nothing but (1) solved for the earlier value, so the resulting $\{y_t\}$ still
satisfies (1) for every $t$. But it is not stationary, because
$$
\text{var}(y_0) = 0 \qquad \text{while} \qquad \text{var}(y_1) = \text{var}(\phi_0 + \phi_1 y_0 +
\epsilon_1) = \text{var}(\epsilon_1) = \sigma^2.
$$
The variance is not even constant in $t$, let alone the rest of stationarity. This construction
works for any $\phi_1$: fixing an arbitrary starting value and running the recursion both ways
always produces *a* solution of (1), and it is essentially never stationary. So "solving" the
$\text{AR}(1)$ equation for a stationary process is a real question, and its answer depends on
$\phi_1$.

## The causal stationary solution, when $|\phi_1| < 1$

Suppose $|\phi_1| < 1$ and define
$$
y_t = \frac{\phi_0}{1 - \phi_1} + \sum_{j=0}^{\infty} \phi_1^j \epsilon_{t-j}. \tag{3}
$$
The sum is infinite, so convergence needs checking; because $|\phi_1| < 1$ the coefficients
$\phi_1^j$ decay geometrically, which is enough to make the series well-defined.

**This satisfies (1).** Peel off the first term and re-index:
$$
\begin{aligned}
y_t &= \frac{\phi_0}{1-\phi_1} + \epsilon_t + \phi_1\epsilon_{t-1} + \phi_1^2 \epsilon_{t-2} + \cdots
\\
&= \frac{\phi_0}{1-\phi_1} + \epsilon_t + \phi_1\big(\epsilon_{t-1} + \phi_1 \epsilon_{t-2} +
\phi_1^2\epsilon_{t-3} + \cdots\big) \\
&= \frac{\phi_0}{1-\phi_1} + \epsilon_t + \phi_1\left(y_{t-1} - \frac{\phi_0}{1-\phi_1}\right) =
\phi_0 + \phi_1 y_{t-1} + \epsilon_t.
\end{aligned}
$$

**This is stationary.** The mean is constant, $\mathbb{E}y_t = \phi_0/(1-\phi_1)$ for every $t$, and
for $h \geq 0$,
$$
\text{cov}(y_t, y_{t+h}) = \text{cov}\left(\sum_{j=0}^\infty \phi_1^j \epsilon_{t-j},\
\sum_{k=0}^\infty \phi_1^k \epsilon_{t+h-k}\right) = \sum_{j=0}^\infty\sum_{k=0}^\infty
\phi_1^{j+k}\,\text{cov}(\epsilon_{t-j}, \epsilon_{t+h-k}).
$$
The noise terms are uncorrelated except with themselves, so $\text{cov}(\epsilon_{t-j},
\epsilon_{t+h-k}) = \sigma^2$ exactly when $t - j = t+h-k$, i.e. $k = j+h$. Only those terms survive:
$$
\text{cov}(y_t, y_{t+h}) = \sigma^2\sum_{j=0}^\infty \phi_1^{2j+h} = \sigma^2\,\frac{\phi_1^h}{1 -
\phi_1^2}.
$$
This depends only on $h$, so $\{y_t\}$ is stationary, with
$$
\gamma(h) = \sigma^2\,\frac{\phi_1^{|h|}}{1-\phi_1^2}, \qquad \rho(h) = \frac{\gamma(h)}{\gamma(0)} =
\phi_1^{|h|}.
$$

It turns out — the proof is skipped here — that (3) is not just *a* stationary solution but *the*
only one when $|\phi_1|<1$. It is called the **causal stationary $\text{AR}(1)$ model**: causal
because $y_t$ is built entirely out of present and past noise, $\epsilon_t, \epsilon_{t-1},
\epsilon_{t-2}, \dots$, never future noise.

## The non-causal stationary solution, when $|\phi_1| > 1$

Now suppose $|\phi_1| > 1$ and define instead
$$
y_t = \frac{\phi_0}{1-\phi_1} - \sum_{j=1}^\infty \frac{\epsilon_{t+j}}{\phi_1^j}. \tag{4}
$$
This time the coefficients $\phi_1^{-j}$ are what decay geometrically (since $|\phi_1|>1$), so the
sum is well-defined even though it now runs over *future* noise terms. A calculation exactly
parallel to the one above shows (4) satisfies the $\text{AR}(1)$ equation and is stationary, and it
is again the unique stationary solution for $|\phi_1|>1$. It is called the **non-causal, stationary
$\text{AR}(1)$ model**, because $y_t$ depends on $\epsilon_{t+1}, \epsilon_{t+2}, \dots$ — noise that
has not happened yet relative to time $t$.

This is not just a labelling curiosity. In model (4), $\epsilon_t$ is *not* independent of the past
$y_{t-1}, y_{t-2}, \dots$ — the independence that the usual $\text{AR}(1)$ likelihood/least-squares
estimation procedure relies on. So if the data were actually generated by the non-causal model and
fit with the standard method, the estimate of $\phi_1$ comes out wrong. (See Examples 3.3 and 3.4 in
Shumway & Stoffer, 4th edition, for the details — not covered in this lecture.)

## No stationary solution at all, when $|\phi_1| = 1$

When $\phi_1 = 1$ or $\phi_1 = -1$, neither series (3) nor (4) converges, and in fact no stationary
solution exists. Take $\phi_1 = 1$ (the case $\phi_1=-1$ is similar):
$$
y_t = \phi_0 + y_{t-1} + \epsilon_t \quad\Longrightarrow\quad y_t - y_0 = t\phi_0 + \epsilon_1 +
\cdots + \epsilon_t \quad \text{for } t \geq 1.
$$
If $\phi_0 \neq 0$, the mean of $y_t$ drifts with $t$ ($\mathbb{E}y_t = \mathbb{E}y_0 + t\phi_0$), so
stationarity already fails. If $\phi_0 = 0$, the mean is fine, but
$$
\text{var}(y_t - y_0) = \text{var}(\epsilon_1 + \cdots + \epsilon_t) = t\sigma^2 \to \infty \text{ as
} t \to \infty.
$$
That is impossible for a stationary process: stationarity would force $\text{var}(y_t)$ and
$\text{var}(y_0)$ to be the same finite constant, giving
$$
\text{var}(y_t - y_0) \leq 2\,\text{var}(y_t) + 2\,\text{var}(y_0) \leq \text{a fixed constant},
$$
which contradicts $t\sigma^2 \to \infty$. So $|\phi_1|=1$ rules out stationarity entirely.

Putting the three regimes together: **stationarity of $\text{AR}(1)$ requires $|\phi_1| \neq 1$**,
and when it holds it is causal for $|\phi_1|<1$ and non-causal for $|\phi_1|>1$ — with exactly one
stationary solution in each case, alongside the many non-stationary solutions that always exist (as
in the first section).

## The backshift operator

Both formulae above can be derived, rather than just checked after the fact, using a formal piece of
notation: the **backshift operator** $B$, defined by
$$
By_t = y_{t-1}, \quad B^2 y_t = y_{t-2}, \quad B^3 y_t = y_{t-3}, \ \dots
$$
and likewise $B\epsilon_t = \epsilon_{t-1}$, etc. Let $I$ be the identity operator, $Iy_t = y_t$.
Polynomials in $B$ act termwise: for instance
$$
(I + B + 3B^2)y_t = y_t + y_{t-1} + 3y_{t-2}.
$$
More generally $f(B)$ makes sense for any polynomial $f(z)$. Negative powers of $B$ are allowed too,
and correspond to *forward* shifts: $B^{-1}y_t = y_{t+1}$, $B^{-5}y_t = y_{t+5}$, and so
$(B^3 + 9B^{-2})y_t = y_{t-3} + 9y_{t+2}$.

In this notation the $\text{AR}(p)$ equation $y_t = \phi_0 + \phi_1 y_{t-1} + \cdots + \phi_p
y_{t-p} + \epsilon_t$ becomes
$$
\phi(B)y_t = \phi_0 + \epsilon_t, \qquad \phi(z) := 1 - \phi_1 z - \phi_2 z^2 - \cdots - \phi_p z^p,
$$
and an $\text{MA}(q)$ equation $y_t = \epsilon_t + \theta_1\epsilon_{t-1} + \cdots +
\theta_q\epsilon_{t-q}$ becomes $y_t = \theta(B)\epsilon_t$ with $\theta(z) := 1 + \theta_1 z +
\cdots + \theta_q z^q$.

## Recovering the two formulas by backshift calculus

The point of the notation is that it lets you "solve" the difference equation formally, the way one
solves a linear equation for an unknown. Write the $\text{AR}(1)$ equation as $\phi(B)y_t = \phi_0 +
\epsilon_t$ with $\phi(z) = 1 - \phi_1 z$, and formally invert:
$$
y_t = \frac{1}{\phi(B)}(\phi_0 + \epsilon_t).
$$
This is only meaningful once $1/\phi(z)$ is expanded as a power series, and there are two different
expansions depending on the size of $\phi_1$ — matching the two stationary regimes exactly.

**Expansion valid for $|\phi_1|<1$.** Using the geometric series $\frac{1}{1-\phi_1 z} = 1 + \phi_1
z + \phi_1^2 z^2 + \cdots$ (which converges for $|z|=1$ precisely because $|\phi_1|<1$),
$$
y_t = (I + \phi_1 B + \phi_1^2 B^2 + \cdots)(\phi_0 + \epsilon_t) = (1+\phi_1+\phi_1^2+\cdots)\phi_0 +
\sum_{j=0}^\infty \phi_1^j \epsilon_{t-j} = \frac{\phi_0}{1-\phi_1} + \sum_{j=0}^\infty \phi_1^j
\epsilon_{t-j},
$$
recovering (3).

**Expansion valid for $|\phi_1|>1$.** Now the series above diverges, so expand $1/\phi(z)$ around
$z=\infty$ instead:
$$
\frac{1}{1-\phi_1 z} = \frac{-1}{\phi_1 z}\left(1 - \frac{1}{\phi_1 z}\right)^{-1} = \frac{-1}{\phi_1
z}\left(1 + \frac{1}{\phi_1 z} + \frac{1}{\phi_1^2 z^2} + \cdots\right) = -\frac{z^{-1}}{\phi_1} -
\frac{z^{-2}}{\phi_1^2} - \cdots,
$$
so that
$$
y_t = \left(-\frac{B^{-1}}{\phi_1} - \frac{B^{-2}}{\phi_1^2} - \cdots\right)(\phi_0+\epsilon_t) =
\frac{\phi_0}{1-\phi_1} - \sum_{j=1}^\infty \frac{\epsilon_{t+j}}{\phi_1^j},
$$
recovering (4). This procedure — expand $1/\phi(z)$ as whichever power series converges, then read
off the coefficients as an $\text{MA}(\infty)$ representation — is called **backshift calculus**. It
is formal (a rigorous justification is in Brockwell & Davis, *Time Series: Theory and Methods*, not
given in this lecture), but it is what generalizes cleanly to $\text{AR}(p)$.

## Stationarity and causality for general AR(p)

Write the $\text{AR}(p)$ equation as $\phi(B)y_t = \phi_0 + \epsilon_t$ with characteristic
polynomial
$$
\phi(z) = 1 - \phi_1 z - \phi_2 z^2 - \cdots - \phi_p z^p,
$$
which has $p$ roots $z_1, \dots, z_p$ (possibly complex, possibly repeated). Everything about
stationarity and causality is decided by where these roots sit relative to the unit circle
$|z|=1$:

1. If every root has $|z_i| \neq 1$, there is a **unique stationary solution**. (Backshift calculus
   extends to write it out explicitly, expanding $1/\phi(z)$ near each root as in the $\text{AR}(1)$
   case — left for the next lecture.)
2. If every root satisfies $|z_i| > 1$, the stationary solution is **causal**: $y_t = \mu +
   \sum_{j=0}^\infty \psi_j \epsilon_{t-j}$ for some constant $\mu$ and coefficients $\{\psi_j\}$ —
   built only from present and past noise.
3. If at least one root has $|z_i| < 1$ while every other root has modulus $> 1$, the stationary
   solution is **non-causal**: $y_t = \mu + \sum_{j=-\infty}^\infty \psi_j \epsilon_{t-j}$, now
   drawing on noise from both the past and the future.
4. If any root has $|z_i| = 1$, **no stationary solution exists**.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Roots of the AR(p) characteristic polynomial located inside, on, and outside the unit circle in the complex plane">
  <line x1="20" y1="110" x2="300" y2="110" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="10" x2="160" y2="210" stroke="currentColor" stroke-width="1"/>
  <circle cx="160" cy="110" r="70" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="34" text-anchor="middle" font-size="12" fill="currentColor">|z| = 1</text>
  <circle cx="248" cy="70" r="4" fill="currentColor"/>
  <text x="252" y="58" font-size="11" fill="currentColor">root, |z|&#62;1</text>
  <text x="252" y="72" font-size="11" fill="currentColor">causal (past ε)</text>
  <circle cx="140" cy="128" r="4" fill="currentColor"/>
  <text x="60" y="150" font-size="11" fill="currentColor">root, |z|&#60;1</text>
  <text x="55" y="163" font-size="11" fill="currentColor">non-causal (future ε)</text>
  <circle cx="160" cy="180" r="4" fill="currentColor"/>
  <text x="168" y="184" font-size="11" fill="currentColor">root, |z|=1: no stationary solution</text>
</svg>
<figcaption>Where the characteristic polynomial's roots sit relative to the unit circle decides
stationarity and causality: all roots outside gives a causal solution, a root inside paired with the
rest outside gives a non-causal one mixing past and future noise, and any root exactly on the circle
rules out stationarity.</figcaption>
</figure>

This is exactly the $\text{AR}(1)$ picture from before, stated for general $p$: when $p=1$, $\phi(z)
= 1-\phi_1 z$ has the single root $z=1/\phi_1$, and $|1/\phi_1|>1$ is the same condition as
$|\phi_1|<1$. So case 2 above is the causal $\text{AR}(1)$ regime, case 3 (with a single root) is the
non-causal regime, and case 4 is the $|\phi_1|=1$ unit-root case.

## Sources

- All of this chapter is from three lecture-note files converted from a single lecture PDF,
  *Lecture Twenty One*, UC Berkeley Stat 153, Spring 2025, Aditya Guntuboyina, April 10, 2025
  (`berkeley-stat153/spring-2025/LectureTwentyOne153248Spring2025.pdf`, CC BY 4.0):
  - "The AR(1) equation does not determine a unique process" through "No stationary solution at
    all" draw on `01-1-stationarity-of-ar-1.md` (source's §1, equations (1)–(4) and the $|\phi_1|=1$
    argument).
  - "The backshift operator" and "Recovering the two formulas by backshift calculus" draw on
    `02-2-on-the-formulae-for-stationary-ar-1.md` (source's §2.1–2.2).
  - "Stationarity and causality for general AR(p)" draws on
    `03-3-stationary-and-causality-for-ar-p.md` (source's §3).
- No slide deck, transcript, or problem set was supplied for this lecture — only these three note
  files, which are themselves a model's reconstruction of a PDF with no extractable text layer; their
  own header flags every equation in them as unverified, which is why the algebra above is worth
  checking against a primary source before relying on it.
- The lecture explicitly points to material it does not itself contain: Shumway & Stoffer, *Time
  Series Analysis and Its Applications*, 4th edition, Examples 3.3–3.4 (consequence of fitting the
  non-causal $\text{AR}(1)$ model with the standard estimator) and §§3.1–3.3 (optional reading); and
  Brockwell & Davis, *Time Series: Theory and Methods* (rigorous justification of backshift
  calculus). The explicit construction of the stationary $\text{AR}(p)$ solution via backshift
  calculus, and the uniqueness proofs skipped for $\text{AR}(1)$, are deferred to the following
  lecture and are not in this material.

---

[← 121. From Regression to RNNs](121-from-regression-to-rnns.md) · [Contents](index.md) · [123. From AR to LSTM →](123-from-ar-to-lstm.md)
