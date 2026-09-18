---
title: "10. Bayes' Rule and Derived Distributions"
course: "MIT 6.041SC"
chapter: 10
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Bayes' Rule and Derived Distributions

## What this covers

This chapter answers two separate questions that the lecture treats back to back. First: how does
Bayes' rule — the tool for reversing a conditional probability — extend once one or both of the
random variables involved are continuous rather than discrete? Second: given the distribution of a
random variable $X$ and a function $g$, how do you find the distribution of $Y=g(X)$ itself, rather
than just a number like its mean? It assumes the joint, marginal and conditional PMFs and PDFs, the
cumulative distribution function, and the basic mechanics of expectation from earlier lectures.

## Bayes' rule, revisited

Recall the multiplication rule and the discrete Bayes' rule:

$$p_{X\mid Y}(x\mid y) = \frac{p_{X,Y}(x,y)}{p_Y(y)} = \frac{p_X(x)\,p_{Y\mid X}(y\mid x)}{p_Y(y)},
\qquad p_Y(y)=\sum_x p_X(x)\,p_{Y\mid X}(y\mid x).$$

This is the tool behind every inference problem in the course: there is some unknown quantity $X$
you cannot observe directly, distributed according to a **prior** $p_X$; there is a noisy
measuring device that produces an observable $Y$ according to a known model $p_{Y\mid X}$; and
having observed a specific value of $Y$, you want the **posterior** distribution of $X$, i.e.
$p_{X\mid Y}(\cdot\mid y)$. The stock example is an airplane and a radar: $X\in\{0,1\}$ records
whether a plane is present, $Y\in\{0,1\}$ records whether the radar beeped, and $p_{Y\mid X}$ is the
(imperfect) model of the radar.

Word for word the same formula holds when both variables are continuous, with every $p$ replaced by
an $f$:

$$f_{X\mid Y}(x\mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)} = \frac{f_X(x)\,f_{Y\mid X}(y\mid x)}{f_Y(y)},
\qquad f_Y(y)=\int f_X(x)\,f_{Y\mid X}(y\mid x)\,dx.$$

The typical picture: $X$ is a signal — say the current through a resistor — with a prior density
$f_X$, and $Y$ is what an analog instrument reports once the signal has been corrupted by noise
(Gaussian, say); $f_{Y\mid X}$ is the noise model. Given a reading $y$, the formula above produces
the entire posterior density of $X$ — a function of $x$ you could plot, not just a single number.

## The two mixed cases, derived from scratch

The slides simply state the two mixed formulas; it is worth seeing where they come from, because
the argument is one you can rerun whenever a new mixed case shows up.

Take $X$ discrete and $Y$ continuous — the standard example is a single transmitted bit
$X\in\{0,1\}$ observed through Gaussian noise, $Y = X + \text{noise}$. $X$ has a prior PMF $p_X$;
for each value $x$, the conditional density $f_{Y\mid X}(\cdot\mid x)$ is a (shifted) Gaussian
bump. We want $p_{X\mid Y}(x\mid y)$.

Start from the multiplication rule applied to the event "$X=x$ and $Y$ lands in a short interval
$(y,y+\delta]$", written two ways:

$$P(X=x,\ y<Y\le y+\delta) = P(X=x)\,P(y<Y\le y+\delta\mid X=x) = P(y<Y\le y+\delta)\,P(X=x\mid y<Y\le y+\delta).$$

For small $\delta$, the probability of landing in a length-$\delta$ interval is density times
$\delta$, so

$$p_X(x)\cdot f_{Y\mid X}(y\mid x)\,\delta \ \approx\ f_Y(y)\,\delta\cdot p_{X\mid Y}(x\mid y).$$

Cancelling the $\delta$'s (exact as $\delta\to0$) and solving for the posterior gives

$$p_{X\mid Y}(x\mid y) = \frac{p_X(x)\,f_{Y\mid X}(y\mid x)}{f_Y(y)}, \qquad
f_Y(y) = \sum_x p_X(x)\,f_{Y\mid X}(y\mid x).$$

The marginal on the right is exactly what you would expect: the density of $Y$ is a $p_X$-weighted
mixture of the conditional densities $f_{Y\mid X}(\cdot\mid x)$, one bump per possible value of
$x$. If the prior over the two values of $X$ is uniform, the posterior is simply proportional to
$f_{Y\mid X}(y\mid x)$ — to the height of the $x$-th bump at the observed $y$ — so the ratio of the
two heights at $y$ gives the relative posterior odds of $x=1$ against $x=0$.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Two conditional densities of the noisy measurement Y, one for each value of the discrete signal X, with the observed value falling under both curves">
  <line x1="30" y1="170" x2="320" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 40 168 C 70 168 100 55 130 55 C 160 55 190 168 220 168" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 120 168 C 150 168 180 90 210 90 C 240 90 270 168 300 168" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="175" y1="20" x2="175" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="70" y="48" font-size="12" fill="currentColor">f(y | X=0)</text>
  <text x="222" y="80" font-size="12" fill="currentColor">f(y | X=1)</text>
  <text x="180" y="16" font-size="12" fill="currentColor">y observed</text>
  <text x="315" y="185" text-anchor="end" font-size="12" fill="currentColor">y</text>
</svg>
<figcaption>Discrete X, continuous Y: each value of X gives a different conditional density of the
measurement Y. With a uniform prior on X, the posterior odds of the two values, given an observed
y, equal the ratio of the two curves' heights at that y.</figcaption>
</figure>

The remaining case — $X$ continuous, $Y$ discrete — runs the identical argument with the roles of
$p$ and $f$ swapped, and gives

$$f_{X\mid Y}(x\mid y) = \frac{f_X(x)\,p_{Y\mid X}(y\mid x)}{p_Y(y)}, \qquad
p_Y(y) = \int f_X(x)\,p_{Y\mid X}(y\mid x)\,dx.$$

Its standard example: a light source emits at some unknown, continuously distributed intensity $X$;
you don't observe the intensity but the discrete count $Y$ of photons registered in a fixed
interval, whose distribution given $X=x$ is some known counting law $p_{Y\mid X}(\cdot\mid x)$. The
formula turns a photon count into a posterior density over the intensity that produced it.

Four cases, one shape: prior times likelihood, over a marginal that is always "sum or integrate out
the unknown, weighted by its prior." What changes case to case is only whether each slot holds a
PMF or a PDF. The lecture does not work these last two cases with numbers here — it returns to
worked Bayesian-inference examples at the end of the course — but the formulas are already usable
as they stand; see the exercises.

## What a derived distribution is, and when you don't need one

If $X$ (or a pair $X,Y$) has a known distribution and $g$ is some function, then $g(X)$ or
$g(X,Y)$ is itself a random variable, and its PMF or PDF is called a **derived distribution**. A
standard instance: given the joint density of $X$ and $Y$, find the density of the ratio
$g(X,Y) = Y/X$.

One case lets you skip this entirely: if all you want is $E[g(X,Y)]$, the law of the unconscious
statistician gives it directly from the distribution you already have,

$$E[g(X,Y)] = \iint g(x,y)\,f_{X,Y}(x,y)\,dx\,dy,$$

with no need to ever find the distribution of $g(X,Y)$ itself. Reach for a derived distribution
only when the distribution — not just its mean — is actually wanted.

## Finding the distribution of $Y = g(X)$

**Discrete case.** If $X$ is discrete, the event $\{Y=y\}$ is exactly the event that $X$ lands in
the set of $x$'s that $g$ sends to $y$, so

$$p_Y(y) = P(g(X)=y) = \sum_{x\,:\,g(x)=y} p_X(x).$$

**Continuous case.** The same idea — match an event for $Y$ to an event for $X$ — is useless if
applied to a single value: $P(Y=y)=0$ for every $y$ once $Y$ is continuous, and matching it to
$P(X=x)=0$ tells you nothing. Work instead with the cumulative distribution function, whose events
are half-lines rather than points and so carry nonzero probability. That gives the standard
two-step recipe:

1. Find $F_Y(y) = P(Y\le y)$ by rewriting the event $\{Y\le y\}$ as an equivalent event about $X$
   (whose distribution is known), and computing its probability from $F_X$.
2. Differentiate: $f_Y(y) = \dfrac{dF_Y}{dy}(y)$.

Step 1 has to be done for *every* $y$ — the whole function $F_Y$, not its value at one point —
before you can differentiate.

## Worked example: the cube of a uniform random variable

Let $X\sim\text{Uniform}[0,2]$ and $Y=X^3$. Since $X$ ranges over $[0,2]$, $Y$ ranges over $[0,8]$;
a tempting guess is that, since $X$ was uniform, $Y$ should be too. Running the recipe shows this
is wrong.

Step 1:

$$F_Y(y) = P(Y\le y) = P(X^3\le y) = P(X\le y^{1/3}).$$

For $X$ uniform on $[0,2]$ (density $1/2$), $P(X\le y^{1/3})$ is the area under that density from
$0$ to $y^{1/3}$:

$$F_Y(y) = \frac12\,y^{1/3}, \qquad 0\le y\le 8.$$

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Area under the uniform density of X between 0 and the cube root of y, used to find the CDF of Y equals X cubed">
  <line x1="40" y1="170" x2="290" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="170" x2="40" y2="100" stroke="currentColor" stroke-width="1"/>
  <line x1="270" y1="170" x2="270" y2="100" stroke="currentColor" stroke-width="1"/>
  <rect x="40" y="100" width="120" height="70" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <line x1="40" y1="100" x2="270" y2="100" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="100" x2="160" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="40" y="186" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="270" y="186" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="160" y="186" text-anchor="middle" font-size="12" fill="currentColor">y^(1/3)</text>
  <text x="30" y="104" text-anchor="end" font-size="12" fill="currentColor">1/2</text>
  <text x="60" y="93" font-size="12" fill="currentColor">f_X(x)</text>
  <text x="292" y="167" font-size="12" fill="currentColor">x</text>
</svg>
<figcaption>The density of X, uniform on [0,2] at height 1/2; the shaded area up to x = y^(1/3) is
F_Y(y) = P(X &#8804; y^(1/3)).</figcaption>
</figure>

Step 2, differentiate:

$$f_Y(y) = \frac{d}{dy}\left(\frac12\,y^{1/3}\right) = \frac16\,y^{-2/3} = \frac{1}{6y^{2/3}},
\qquad 0<y<8,$$

and $f_Y(y)=0$ outside $[0,8]$ — the formula for $F_Y$ only holds while $y^{1/3}$ stays inside
$[0,2]$, i.e. while $y\in[0,8]$; no other value of $Y$ is possible.

$f_Y$ blows up as $y\to0^+$ and shrinks toward $y=8$: $Y$ is *not* uniform. The reason is visible in
the map itself. Near $x=0$, cubing is nearly flat ($dy/dx=3x^2\to0$), so a fixed stretch of
$x$-probability is squeezed into a short stretch of $y$, raising the density there; near $x=2$ the
map is steep, so the same $x$-probability is spread over a longer stretch of $y$, lowering the
density.

## Worked example: travel time from a uniform speed

Joan drives from Boston to New York, a distance of $200$ miles, at a speed $V$ she sets on cruise
control and holds constant; $V\sim\text{Uniform}[30,60]$. The duration of the trip is $T=200/V$;
find $f_T$.

Apply the same recipe. Because $T$ is a *decreasing* function of $V$ (small speed means a long
trip), the inequality flips when the event is translated:

$$F_T(t) = P(T\le t) = P\!\left(\frac{200}{V}\le t\right) = P\!\left(V\ge \frac{200}{t}\right).$$

This makes sense only while $200/t$ falls inside $[30,60]$, i.e. while
$t\in\left[\frac{200}{60},\frac{200}{30}\right] = \left[\frac{10}{3},\frac{20}{3}\right]$ — outside
that range $T$ cannot occur at all. On that range, since $V$ is uniform with density $1/30$,

$$P\!\left(V\ge \frac{200}{t}\right) = \frac{1}{30}\left(60-\frac{200}{t}\right).$$

Differentiating,

$$f_T(t) = \frac{d}{dt}\left[\frac{1}{30}\left(60-\frac{200}{t}\right)\right]
= \frac{1}{30}\cdot\frac{200}{t^2} = \frac{20}{3t^2}, \qquad \frac{10}{3}\le t\le \frac{20}{3}.$$

The point of this example, next to the last one, is the reversal: for an increasing function of $X$
the event $\{Y\le y\}$ turns directly into $\{X\le \text{something}\}$; for a decreasing one it
turns into $\{X\ge \text{something}\}$, and forgetting to flip the inequality is the standard
mistake.

## Linear functions of a random variable

The single most useful derived distribution is the affine one, $Y=aX+b$. Take $a=2$, $b=5$, and
let $X$ have some given (not necessarily symmetric) density on, say, $[-1,2]$.

Build it up in two moves. $2X$ ranges over $[-2,4]$ — twice as wide — and multiplying by 2 is just a
change of scale, so its density should have the same shape as $f_X$'s, stretched horizontally by a
factor of 2. Stretching the shape alone, with no other change, would give $f_X(z/2)$ as a function
of the new variable $z$ — but stretching a curve horizontally by 2 doubles the area underneath it,
and a density must still integrate to 1, so the stretched shape also has to be squashed down by the
same factor:

$$f_{2X}(z) = \frac12\,f_X(z/2).$$

Adding 5 then slides the whole picture 5 units to the right, with no further change of shape or
height:

$$f_{2X+5}(y) = \frac12\,f_X\!\left(\frac{y-5}{2}\right), \qquad \text{range } [3,9].$$

<figure>
<svg viewBox="0 0 280 190" role="img" aria-label="The density of X stretched to twice its width and half its height, then shifted, to give the density of Y equals 2X plus 5">
  <line x1="15" y1="170" x2="255" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 40 170 L 70 70 L 100 170 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <path d="M 120 170 L 180 120 L 240 170 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="70" y1="70" x2="70" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="180" y1="120" x2="180" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="30" y="65" font-size="12" fill="currentColor">h</text>
  <text x="185" y="115" font-size="12" fill="currentColor">h/2</text>
  <text x="40" y="184" text-anchor="middle" font-size="12" fill="currentColor">-1</text>
  <text x="100" y="184" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="120" y="184" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <text x="240" y="184" text-anchor="middle" font-size="12" fill="currentColor">9</text>
  <text x="45" y="58" font-size="12" fill="currentColor">f_X(x)</text>
  <text x="188" y="108" font-size="12" fill="currentColor">f_Y(y), Y=2X+5</text>
</svg>
<figcaption>Multiplying X by 2 doubles the width of its density and halves its height, to keep the
area at 1; adding 5 then shifts the whole picture along the same axis without changing its shape.</figcaption>
</figure>

That is the picture argument. The same conclusion falls out of the two-step recipe, and it is worth
doing once formally, because it is what settles the sign of $a$. Take $a>0$ first:

$$F_Y(y) = P(aX+b\le y) = P\!\left(X\le \frac{y-b}{a}\right) = F_X\!\left(\frac{y-b}{a}\right).$$

Differentiating by the chain rule,

$$f_Y(y) = f_X\!\left(\frac{y-b}{a}\right)\cdot\frac1a.$$

If $a<0$, dividing the inequality $aX\le y-b$ by $a$ reverses it, so instead

$$F_Y(y) = P\!\left(X\ge \frac{y-b}{a}\right) = 1-F_X\!\left(\frac{y-b}{a}\right),$$

and differentiating brings down an extra minus sign, which combines with the negative $a$ to give a
positive factor $-1/a = 1/|a|$. Either sign of $a$ is covered by one formula:

$$f_Y(y) = \frac{1}{|a|}\,f_X\!\left(\frac{y-b}{a}\right).$$

Reach for this formula whenever a random variable is rescaled and shifted — including, as a check
worth doing by hand, to confirm that an affine function of a normal random variable is again
normal.

## Exercises

**1.** Alice has two coins: the first comes up heads with probability $1/3$, the second with
probability $2/3$; the coins are otherwise indistinguishable. Alice picks one of the two at random
and sends it to Bob — write $p$ for the probability that she sent the first coin. Bob flips the
coin he receives 3 times, independently, and lets $Y$ be the number of heads he sees.

  (a) Given that Bob observed $k$ heads, what is the probability that he received the first coin?

  (b) For which values of $k$ does observing $k$ heads *raise* the probability that the first coin
  was sent, i.e. make the posterior larger than $p$? If $p$ itself is increased, how does your
  answer change?

  (c) Bob wants a rule, based only on the number of heads $k$ he observes, for guessing which coin
  he received, chosen to minimize his probability of error. What is that rule?

  (d) Take $p=2/3$.
      i. Under the rule from (c), what is Bob's probability of guessing correctly?
      ii. How does that compare with the probability of guessing correctly with no coin flips at
      all — i.e. guessing before observing anything?

  (e) How does increasing $p$ change the rule from (c)?

  (f) For which values of $p$ does Bob's rule never guess "first coin," no matter what he observes?

  (g) For which values of $p$ does Bob's rule always guess "first coin," no matter what he
  observes?

**2.** Consider a Bernoulli process $X_1, X_2, X_3, \dots$ with unknown success probability $q$.
Write $Y_k$ for the time of the $k$th success, and let $T_1 = Y_1$, $T_k = Y_k - Y_{k-1}$ for
$k\ge2$ be the inter-arrival times. Suppose $q$ is itself the value of a random variable $Q$; you
may find the following useful, for non-negative integers $k,m$:

  $$\int_0^1 q^k(1-q)^m\,dq = \frac{k!\,m!}{(k+m+1)!}.$$

  For parts (a)-(c), take $Q\sim\text{Uniform}[0,1]$.

  (a) Find the PMF of $T_1$, $p_{T_1}(t_1)$.

  (b) Find the least-squares estimate of $Q$ given the single observation $T_1=t_1$.

  (c) Find the maximum a posteriori estimate of $Q$ given $k$ observed inter-arrival times
  $T_1=t_1,\dots,T_k=t_k$.

  For part (d) only, take $Q\sim\text{Uniform}[0.5,1]$ instead.

  (d) Find the linear least-squares estimate of the second inter-arrival time $T_2$ from the
  observed first inter-arrival time $T_1=t_1$.

**3.** The joint density of $X$ and $Y$ is

  $$f_{X,Y}(x,y) = \begin{cases} cxy & 0<x\le1,\ 0<y\le1 \\ 0 & \text{otherwise.}\end{cases}$$

  (a) Find the normalizing constant $c$.

  (b) Find the conditional expectation of $X$ given the observed value $Y=y$.

  (c) Is the estimate in (b) different from what you would have guessed about $X$ before observing
  $Y$? Explain.

  (d) Repeat (b) and (c) for the maximum a posteriori estimate.

## Sources

- Slides: `probability/mit-ocw/6041sc/lectures/10-slides.md` ("LECTURE 10: Continuous Bayes rule;
  Derived distributions") — the four Bayes-rule cases, the definition of, and "when not to find",
  a derived distribution, the discrete-case formula, the two-step continuous recipe, both worked
  examples ($Y=X^3$ and Joan's drive), and the $Y=aX+b$ formula.
- Transcript: `probability/mit-ocw/6041sc/recordings/lectures/10.md`, throughout — the framing of
  inference as an unknown $X$ observed through a noisy measuring device producing $Y$ ([03:06]-[05:15]);
  the delta-interval derivation of the two mixed Bayes formulas ([12:04]-[16:31]); the airplane/radar,
  resistor-current, single-bit-plus-Gaussian-noise, and photon-counting examples ([06:25]-[19:52]);
  and the full walk-through of both derived-distribution worked examples and of $Y=aX+b$
  ([26:40]-[47:49]).
- Exercises: `probability/mit-ocw/6041sc/psets/10-questions.md`, Problems 4-6 — the coin-bias
  inference problem, the Bernoulli-process inter-arrival-time estimation problem, and the joint-density
  conditional/MAP-estimate problem, which turn on this lecture's Bayes-rule variations. Problems 1-3 of
  the same problem set (central limit theorem and normal approximation) belong to a different lecture
  and are not used here.
- Not used: `probability/mit-ocw/6041sc/recitations/10-slides/` (basic probability identities and a
  coin-tossing game) and `probability/mit-ocw/6041sc/tutorials/10-slides.md` (Chebyshev's inequality
  and Markov chains) are catalogued under the same lecture number but cover different material;
  nothing from them appears in this chapter.
- Not covered here: the transcript notes that worked, numerical Bayesian-inference examples are
  deferred to later in the course ("we're going to revisit at the end of the semester" [00:00],
  [19:52]); that material is outside this chapter.

---

[← 9. Joint and Conditional Continuous Densities](09-joint-and-conditional-continuous-densities.md) · [Contents](index.md) · [11. Derived Distributions, Convolutions, and Covariance →](11-derived-distributions-convolutions-and-covariance.md)
