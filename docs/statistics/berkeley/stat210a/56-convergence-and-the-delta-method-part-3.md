---
title: "56. Convergence and the Delta Method (part 3)"
course: "Berkeley Stat 210A Fall 2024"
chapter: 56
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 56. Convergence and the Delta Method (part 3)

## What this covers

Everything treated so far in the course computed exact, finite-sample quantities — often by
exploiting special structure such as an exponential family. This chapter starts the switch to
*asymptotics*: for a "generic" model, exact calculations can be intractable or impossible, so
instead the problem is replaced by a simpler one that is easy to compute with, typically a
Gaussian approximation obtained by letting the sample size $n \to \infty$. Making that precise
needs two notions of convergence and three tools built on top of them — the continuous mapping
theorem, Slutsky's theorem, and the delta method — that let a limit already established for one
quantity be transferred to a transformed one without repeating the analysis. It assumes
familiarity with expectations and cumulative distribution functions, and states the law of large
numbers and central limit theorem as known results rather than proving them.

## Why approximate at all

For a generic model, exact calculation of an estimator's distribution can be intractable or simply
impossible. The way out is to replace the exact problem with a simpler one, and accept the
resulting error as the price of tractability. The standard simpler problem is a Gaussian
approximation, obtained by taking the limit as the number of observations $n \to \infty$. This is
only useful if the approximation is already good at the sample sizes actually available — the
limit is a means, not the object of interest.

## Two notions of convergence

Let $X_1, X_2, \dots \in \mathbb{R}^d$ be a sequence of random vectors. Two kinds of statement about
its limiting behaviour matter for what follows.

**Convergence in probability.** $X_n \xrightarrow{p} c$ for a constant $c \in \mathbb{R}^d$ if
$$\mathbb{P}(\|X_n - c\| > \varepsilon) \to 0 \quad \text{for every } \varepsilon > 0.$$
Informally, $X_n \approx c$: the whole sequence eventually concentrates near a fixed point. (The
same definition makes sense with $c$ replaced by a random variable, and with $\|\cdot\|$ replaced
by any distance on any space $\mathcal{X}$, but a constant limit is all that is needed here.)

**Convergence in distribution.** $X_n \Rightarrow X$ (also written $X_n \xrightarrow{d} X$) if
$$\mathbb{E} f(X_n) \to \mathbb{E} f(X) \quad \text{for every bounded, continuous } f: \mathcal{X} \to \mathbb{R}.$$
Informally, $X_n \approx X$ in shape — this is the sense in which, later, $X_n \approx \mathcal{N}_d(0, I_d)$.

For real-valued sequences this has a familiar equivalent form. Write $F_n(x) = \mathbb{P}(X_n \le x)$
and $F(x) = \mathbb{P}(X \le x)$.

**Theorem.** $X_n \Rightarrow X$ if and only if $F_n(x) \to F(x)$ for every $x$ at which $F$ is
continuous.

Convergence in distribution is also called *weak convergence*, and the restriction to continuity
points of $F$ is not a technicality that can be dropped — the next example shows exactly where it
bites.

### Example: a sequence of point masses

Let $X_n \sim \delta_{1/n}$ (so $X_n = 1/n$ almost surely) and $X \sim \delta_0$. Then $X_n \Rightarrow X$:
for $x \ne 0$,
$$F_n(x) = \mathbf{1}\{1/n \le x\} \longrightarrow \mathbf{1}\{0 \le x\} = F(x),$$
but at $x = 0$ itself $F_n(0) = 0$ for every $n$ while $F(0) = 1$, so the convergence fails exactly
at the one point where it was allowed to.

<figure>
<svg viewBox="0 0 360 200" role="img" aria-label="Step functions F_n with a jump at 1/n converge to the step function F at 0 everywhere except at the point 0 itself">
  <line x1="30" y1="170" x2="340" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="200" y1="178" x2="200" y2="162" stroke="currentColor" stroke-width="1.2"/>
  <text x="200" y="195" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <polyline points="30,170 320,170 320,40 340,40" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.35"/>
  <polyline points="30,170 280,170 280,40 340,40" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.55"/>
  <polyline points="30,170 245,170 245,40 340,40" fill="none" stroke="currentColor" stroke-width="1.2" opacity="0.8"/>
  <polyline points="30,170 200,170 200,40 340,40" fill="none" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="325" y="35" font-size="11" fill="currentColor">F</text>
  <text x="317" y="55" font-size="11" fill="currentColor" opacity="0.7">F_n</text>
  <circle cx="200" cy="170" r="3.5" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <circle cx="200" cy="40" r="3.5" fill="currentColor"/>
</svg>
<figcaption>As n grows the jump in F_n (at 1/n) slides toward the jump in F (at 0); the open circle
marks F_n(0)=0 for every n, the filled circle marks the limit F(0)=1 — the one point where F_n(x)
does not converge to F(x).</figcaption>
</figure>

## Convergence in probability is a special case

**Proposition.** $X_n \xrightarrow{p} c$ if and only if $X_n \Rightarrow \delta_c$.

This says the two notions coincide once the limit is degenerate: a constant is the same thing as a
point mass, and "converging to a constant" is converging in distribution to that point mass.

**Proof.**

$(\Leftarrow)$ Apply the definition of convergence in distribution to the bounded, continuous
function $f_\varepsilon(x) = \min(1, \|x-c\|/\varepsilon)$, which satisfies
$f_\varepsilon(x) \ge \mathbf{1}\{\|x-c\|>\varepsilon\}$ pointwise. Then
$$\mathbb{P}(\|X_n-c\|>\varepsilon) \le \mathbb{E} f_\varepsilon(X_n) \to f_\varepsilon(c) = 0$$
for every $\varepsilon>0$, which is exactly convergence in probability.

$(\Rightarrow)$ Let $f$ be bounded and continuous; note $\mathbb{E} f(\delta_c) = f(c)$, so it must
be shown that $\mathbb{E} f(X_n) \to f(c)$. Fix $\varepsilon > 0$. By continuity of $f$ at $c$,
choose $d(\varepsilon)>0$ so that $\|x-c\|\le d(\varepsilon)$ implies $|f(x)-f(c)|\le \varepsilon$.
Splitting the expectation over the events $\{\|X_n-c\|\le d(\varepsilon)\}$ and its complement gives
$$|\mathbb{E} f(X_n) - f(c)| \le \varepsilon + \mathbb{P}(\|X_n-c\|>d(\varepsilon)) \cdot 2\sup_x |f(x)|.$$
The first term is as small as desired; the second term $\to 0$ as $n \to \infty$ because
$X_n \xrightarrow{p} c$, so the whole bound can be made arbitrarily small. $\blacksquare$

## Consistency

In a sequence of statistical models $\mathcal{P}_n = \{P_{n,\theta} : \theta \in \Theta\}$ with
$X_n \sim P_{n,\theta}$, an estimator $\delta_n(X_n)$ is **consistent** for $g(\theta)$ if
$\delta_n(X_n) \xrightarrow{p} g(\theta)$ under $P_\theta$, i.e.
$$P_\theta\big(\|\delta_n(X_n) - g(\theta)\| > \varepsilon\big) \to 0 \quad \text{for every } \varepsilon > 0 \text{ and every } \theta.$$
From here on the index $n$ is usually left implicit, with the sequence understood from context.

## The two classical limit theorems

Let $X_1, X_2, \dots$ be i.i.d. random vectors and write $\bar X_n = \frac{1}{n}\sum_{i=1}^n X_i$.

**Law of large numbers.** If $\mathbb{E}|X_i| < \infty$ and $\mathbb{E} X_i = \mu$, then
$\bar X_n \xrightarrow{p} \mu$ (in fact $\bar X_n$ converges to $\mu$ almost surely).

**Central limit theorem.** If $\mathbb{E} X = \mu \in \mathbb{R}^d$ and $\mathrm{Var}(X) = \Sigma$
is finite, then
$$\sqrt n (\bar X_n - \mu) \Rightarrow \mathcal N(0, \Sigma).$$

Stronger versions of both exist, but this pair is enough for what follows: the law of large numbers
says the average settles near a point, the central limit theorem describes the fluctuation around
that point at the $\sqrt n$ scale, as a Gaussian.

## Continuous mapping

The remaining three results all serve the same purpose: given a limit already established for
$X_n$, transfer it to some other quantity built from $X_n$, without redoing the analysis from
scratch.

**Theorem.** Let $g$ be continuous. Then
$$X_n \Rightarrow X \implies g(X_n) \Rightarrow g(X), \qquad X_n \xrightarrow{p} c \implies g(X_n) \xrightarrow{p} g(c).$$

**Proof.** If $f$ is bounded and continuous, so is $f \circ g$. If $X_n \Rightarrow X$, then
$\mathbb{E}[f(g(X_n))] \to \mathbb{E}[f(g(X))]$ for every such $f$, which is exactly
$g(X_n) \Rightarrow g(X)$. The convergence-in-probability statement is the special case
$X \sim \delta_c$, via the proposition above. $\blacksquare$

## Slutsky's theorem

Continuous mapping alone does not say how to combine a distributional limit with a second sequence
behaving independently of it. Slutsky's theorem covers exactly that case.

**Theorem.** Suppose $X_n \Rightarrow X$ and $Y_n \xrightarrow{p} c$. Then
$$X_n + Y_n \Rightarrow X + c, \qquad X_n Y_n \Rightarrow cX, \qquad X_n/Y_n \Rightarrow X/c \ \ (c \ne 0).$$

**Proof idea.** Show that the pair $(X_n, Y_n) \Rightarrow (X, c)$ jointly, then apply continuous
mapping to $(x,y)\mapsto x+y$, $(x,y) \mapsto xy$, or $(x,y)\mapsto x/y$ (continuous away from
$y=0$).

The reason this needs its own theorem, rather than following automatically from what has already
been proved, is that convergence in distribution does not combine coordinatewise:
$X_n \Rightarrow X$ and $Y_n \Rightarrow Y$ separately do *not* imply $(X_n, Y_n) \Rightarrow (X, Y)$
in general, because the joint distribution of the limit is not determined by the two marginals.
What makes Slutsky's theorem go through is that $Y_n$ converges to a *constant*: a degenerate
distribution leaves no dependence to specify, so the joint limit $(X,c)$ is unambiguous.

## The delta method

The delta method answers a natural question: if $X_n$ is asymptotically Gaussian around $\mu$ at
rate $\sqrt n$, what can be said about a smooth transformation $f(X_n)$?

**Theorem.** Suppose $\sqrt n (X_n - \mu) \Rightarrow \mathcal N(0,\sigma^2)$ and $f$ is
differentiable at $\mu$. Then
$$\sqrt n \big(f(X_n) - f(\mu)\big) \Rightarrow \mathcal N\big(0, \dot f(\mu)^2 \sigma^2\big).$$

Informally: if $X_n \approx \mathcal N(\mu, \sigma^2/n)$, then
$f(X_n) \approx \mathcal N\big(f(\mu), \dot f(\mu)^2 \sigma^2/n\big)$ — the transformation rescales
the asymptotic variance by the square of its own derivative at the point being expanded around,
exactly as a linear approximation would.

**Proof.** By differentiability of $f$ at $\mu$,
$$f(X_n) = f(\mu) + \dot f(\mu)(X_n - \mu) + o(X_n - \mu).$$
Multiplying through by $\sqrt n$,
$$\sqrt n\big(f(X_n) - f(\mu)\big) = \dot f(\mu)\cdot \sqrt n (X_n - \mu) + \underbrace{\sqrt n \cdot o(X_n - \mu)}_{\xrightarrow{p} 0}.$$
The first term converges in distribution to $\mathcal N(0, \dot f(\mu)^2\sigma^2)$ by continuous
mapping, since $x \mapsto \dot f(\mu) x$ is continuous. The remainder term goes to $0$ in
probability, because $\sqrt n (X_n - \mu)$ converging in distribution forces $X_n \xrightarrow{p} \mu$,
which makes the $o(\cdot)$ term shrink faster than $\sqrt n$ grows. Slutsky's theorem then combines
the two: adding a term that vanishes in probability to a term converging in distribution does not
change the limit. $\blacksquare$

**Multivariate case.** The notes open a multivariate version of the theorem — $\sqrt n(X_n - \mu)
\Rightarrow \mathcal N_d(0,\Sigma)$ with $f : \mathbb{R}^d \to \mathbb{R}^k$ — but break off
mid-sentence before stating the differentiability hypothesis or the conclusion, so it is not
reconstructed here; see Sources.

## Sources

- All content: handwritten lecture notes, `docs/statistics/berkeley/stat210a/fall-2024/handwritten/lecture19-F24.md`
  (source PDF `handwritten/lecture19-F24.pdf`, Berkeley STAT210A, Fall 2024, CC BY 4.0), dated
  11/2/2023 in the notes themselves. The lecture's own outline lists three parts — convergence in
  probability and in distribution, continuous mapping and Slutsky's theorem, and the delta method —
  which are followed in order above.
- The source markdown is itself a model's reconstruction of a handwritten PDF with no text layer
  ("fidelity: reconstructed"), and it flags every equation as unverified. Two passages here were
  cleaned up rather than copied literally because they were internally inconsistent as transcribed:
  the bounding function in the proof of $X_n \xrightarrow{p} c \iff X_n \Rightarrow \delta_c$ (given
  in the source as $\max(1,\|x-c\|/\varepsilon)$, which cannot be the bounded function the argument
  needs; presented above as the standard truncated-distance function $\min(1,\|x-c\|/\varepsilon)$),
  and the constants in the final display of that same proof.
- The multivariate delta method statement is cut off in the source right after introducing
  $f:\mathbb{R}^d\to\mathbb{R}^k$, before any hypothesis or conclusion is given; it is not
  reconstructed here rather than guessed at.
- No slides, transcript, or exercises were supplied alongside these notes.

---

[← 55. Convergence and the Delta Method (part 2)](55-convergence-and-the-delta-method-part-2.md) · [Contents](index.md) · [57. MLE in Exponential Families →](57-mle-in-exponential-families.md)
