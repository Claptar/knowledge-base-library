---
title: "8. Continuous Random Variables and the Normal Distribution"
course: "MIT 6.041SC"
chapter: 8
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 8. Continuous Random Variables and the Normal Distribution

## What this covers

Every random variable so far has taken a discrete set of values, with probability sitting in
lumps at points. This chapter asks what changes when a random variable can take *any* real value —
a measurement, a waiting time, a location. It builds the continuous analogue of the probability
mass function (the density), redefines expectation and variance for it, introduces the cumulative
distribution function as a single notion that covers discrete, continuous, and mixed random
variables at once, and ends with the normal (Gaussian) random variable and the mechanics of
computing normal probabilities from a table. It assumes the discrete machinery — PMFs, expectation,
variance, independence — already in hand, since almost everything here is that machinery translated.

## Continuous random variables and densities

For a discrete random variable, one unit of probability is chopped into lumps and each lump sits on
a point: the PMF tells you how heavy each lump is. A continuous random variable spreads that same
unit of probability smoothly over the real line, and there is no lump left to put a number on: any
single point gets probability zero. What can be specified is how *densely* the probability is
packed at each point — thick here, thin there — and that is exactly what a **probability density
function** $f_X$ does.

A random variable $X$ is continuous if there is a function $f_X$, with $f_X(x)\ge 0$ for all $x$,
such that

$$P(a \le X \le b) = \int_a^b f_X(x)\,dx$$

for every interval $[a,b]$. Taking $a=b=x$ gives $P(X=x)=0$ for every single point $x$: the density
at a point does not tell you the probability of that point (which is always zero), it tells you
something else. Taking the whole line gives the normalization condition

$$\int_{-\infty}^{\infty} f_X(x)\,dx = 1,$$

which just says the total probability spread over the axis is one unit, no more.

The right way to read a density is through *short* intervals. If $\delta$ is small, $f_X$ barely
changes over $[x, x+\delta]$, so the integral is (to good approximation) base times height:

$$P(x \le X \le x+\delta) \approx f_X(x)\cdot \delta.$$

Rearranging, $f_X(x) \approx P(x\le X\le x+\delta)/\delta$: density is **probability per unit
length**, a rate at which probability accumulates, not a probability itself. That is why a density
is allowed to exceed $1$ — only the *area* under it is constrained to be $1$, the height is free to
spike as high as it likes, as long as it comes back down elsewhere. For a general "nice" set $B$
(built, say, from a union of disjoint intervals),

$$P(X \in B) = \int_B f_X(x)\,dx,$$

obtained by adding the integral over each piece — exactly as you would add PMF values over the
points of $B$ in the discrete case. This is the theme of the whole chapter: take a discrete-case
formula, replace sums with integrals and the PMF with the density, and it carries over.

## Expectation and variance, translated

The same substitution — $\sum \to \int$, $p_X \to f_X$ — gives expectation and variance directly:

$$\mathbf{E}[X] = \int_{-\infty}^{\infty} x\, f_X(x)\,dx,\qquad
\mathbf{E}[g(X)] = \int_{-\infty}^{\infty} g(x)\, f_X(x)\,dx,$$

$$\text{var}(X) = \sigma_X^2 = \int_{-\infty}^{\infty} (x-\mathbf{E}[X])^2 f_X(x)\,dx
= \mathbf{E}[X^2] - (\mathbf{E}[X])^2.$$

The expectation-of-a-function formula means you never have to find the density of $g(X)$ just to
average it — integrate $g$ against the density of $X$ directly, as in the discrete case. The
shortcut formula for variance survives unchanged too.

Two interpretations of $\mathbf{E}[X]$ that were already useful for discrete random variables
survive as well. It is the **center of gravity** of the mass distributed according to $f_X$ — the
same formula from freshman-physics moment calculations. And it is still the **long-run average**:
sample $X$ independently a huge number of times and the average of the samples converges to
$\mathbf{E}[X]$. That second claim is a genuine theorem (a law of large numbers), not proved here —
it is stated now and argued for properly later in the course.

## Worked example: the continuous uniform random variable

The simplest continuous random variable is uniform on an interval $[a,b]$: a density that is $0$
outside $[a,b]$ and constant on it. "Uniform" does not mean any individual point is more likely —
every point has probability zero regardless — it means that **two subintervals of $[a,b]$ of the
same length have the same probability**, no matter where in $[a,b]$ they sit. That is the sense in
which the random variable is "completely random" over its range.

The height of the constant is forced by normalization: the area under the density must be $1$, so

$$f_X(x) = \begin{cases}\dfrac{1}{b-a}, & a \le x \le b\\[4pt] 0, & \text{otherwise.}\end{cases}$$

The expectation can be found either by direct integration or, faster, from the center-of-gravity
picture: a uniform slab of mass on $[a,b]$ balances at its midpoint, so

$$\mathbf{E}[X] = \frac{a+b}{2}.$$

The variance needs the calculus, with no shortcut available:

$$\sigma_X^2 = \int_a^b \left(x - \frac{a+b}{2}\right)^2 \frac{1}{b-a}\,dx = \frac{(b-a)^2}{12}.$$

The standard deviation $\sigma_X = (b-a)/\sqrt{12}$ is proportional to the width of the interval —
exactly the intuition that standard deviation measures spread — and it carries the same units as
$X$ itself, unlike the variance.

## The cumulative distribution function

Writing discrete and continuous formulas side by side, with sums on one side and integrals on the
other, works, but any general argument about "random variables" would need to be made twice. The
fix is a single object that means the same thing in both cases: the **cumulative distribution
function**,

$$F_X(x) = P(X \le x).$$

It is computed differently in the two cases — by integrating for continuous random variables, by
summing for discrete ones —

$$F_X(x) = \int_{-\infty}^{x} f_X(t)\,dt \qquad\text{(continuous)}, \qquad
F_X(x) = \sum_{k\le x} p_X(k) \qquad\text{(discrete)},$$

but the concept, "probability of falling at or to the left of $x$", is identical, and $F_X$ is
always non-decreasing, running from $0$ at $-\infty$ to $1$ at $+\infty$.

The two cases look different once drawn. For a **continuous** random variable, $F_X$ is itself a
continuous function: it climbs smoothly wherever the density is positive and is flat wherever the
density is zero, because there is no point mass anywhere to produce a jump. Where $F_X$ has a
derivative, that derivative is the density,

$$f_X(x) = F_X'(x),$$

which is just the Fundamental Theorem of Calculus. At isolated corners of $F_X$ the derivative is
undefined, and correspondingly the density is ambiguous there — but since changing a density at a
single point never changes any integral, this ambiguity is harmless and can be resolved either way.

For a **discrete** random variable, $F_X$ is a staircase: flat between the points where the PMF
puts mass, with a jump of size $p_X(k)$ exactly at each point $k$ that carries positive probability.
Because the event is $X \le x$ (not $X < x$), at a jump point $x=k$ the correct value of $F_X$ is
the **upper** one — the jump has already happened by the time you are exactly at $k$, since $k$
itself counts. Jumps in $F_X$ correspond to point masses in the distribution; a continuous random
variable has no jumps because it has no point masses.

## Mixed random variables

Not every random variable is purely discrete or purely continuous. Suppose a game works like this:
flip a coin. With probability $1/2$ you are handed exactly $1/2$ a dollar. With probability $1/2$
you instead spin a wheel that pays a reward uniformly distributed on $[0,1]$. Call the payout $X$.

$X$ is not continuous, because the single point $x=1/2$ carries positive probability ($1/2$, from
the first branch of the coin flip) — a continuous random variable would give every point
probability zero. $X$ is not discrete either, because it can also take any value in a continuous
range (from the wheel). It is a **mixed** random variable: part point mass, part density, combined.
Nothing in the definition of $F_X$ required the random variable to be purely one or the other, so
$F_X$ is perfectly well defined regardless — this is exactly the flexibility the CDF buys.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="CDF of a mixed random variable: a straight rise, a jump, then another straight rise">
  <line x1="40" y1="190" x2="330" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="335" y="195" font-size="12" fill="currentColor">x</text>
  <line x1="20" y1="190" x2="40" y2="190" stroke="currentColor" stroke-width="2"/>
  <line x1="40" y1="190" x2="175" y2="150" stroke="currentColor" stroke-width="2"/>
  <line x1="175" y1="150" x2="175" y2="70" stroke="currentColor" stroke-width="2" stroke-dasharray="4 3"/>
  <circle cx="175" cy="150" r="3" fill="none" stroke="currentColor"/>
  <circle cx="175" cy="70" r="3" fill="currentColor"/>
  <line x1="175" y1="70" x2="310" y2="30" stroke="currentColor" stroke-width="2"/>
  <line x1="310" y1="30" x2="330" y2="30" stroke="currentColor" stroke-width="2"/>
  <line x1="40" y1="30" x2="330" y2="30" stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 3" opacity="0.4"/>
  <text x="45" y="27" font-size="11" fill="currentColor">1</text>
  <text x="170" y="207" text-anchor="middle" font-size="12" fill="currentColor">1/2</text>
  <text x="300" y="207" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="10" y="194" font-size="12" fill="currentColor">0</text>
</svg>
<figcaption>The CDF of the coin-and-wheel payout: it rises continuously where the uniform
wheel contributes probability, and jumps by 1/2 exactly at the point holding the coin's point
mass.</figcaption>
</figure>

Before the jump, probability accumulates only from the wheel's uniform density; at $x=1/2$ an
extra half unit of probability lands all at once, from the coin; afterwards the wheel resumes
contributing continuously until the total reaches $1$. The picture — mass in a lump at one point,
density spread over an interval, added together — is a genuine hybrid of a PMF and a PDF, and no
formal apparatus (an "impulse function," for instance) is needed to make sense of it: it is enough
to know how to read the resulting CDF.

## The normal (Gaussian) random variable

The **standard normal** random variable $N(0,1)$ has density

$$f_X(x) = \frac{1}{\sqrt{2\pi}}\,e^{-x^2/2}.$$

The shape comes from the exponent: $x^2/2$ is an upward parabola, so $-x^2/2$ is a downward one, and
$e^{-x^2/2}$ is largest (equal to $1$) at $x=0$ and falls off fast — exponentially fast — as $|x|$
grows, giving the familiar bell curve with thin tails. The constant $1/\sqrt{2\pi}$ is exactly what
is needed to make the total area equal $1$; getting that constant is a genuine calculus exercise
(polar coordinates and a second copy of the integral), not derived here. By the symmetry of the
curve about $0$, $\mathbf{E}[X]=0$; the variance takes another calculus computation, with no
shortcut, and comes out to $\text{var}(X)=1$.

The **general normal** $N(\mu,\sigma^2)$ is obtained by moving the center to $\mu$ and controlling
the width with a parameter $\sigma$:

$$f_X(x) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-(x-\mu)^2/2\sigma^2}.$$

A small $\sigma$ makes the exponent grow quickly away from $\mu$, so the density falls off fast and
is narrow; a large $\sigma$ spreads it out. It turns out that $\mathbf{E}[X]=\mu$ and
$\text{Var}(X)=\sigma^2$ — matching the roles $\mu$ and $\sigma$ visually play as center and width.

The normal shows up everywhere for a reason previewed here and proved later in the course: whenever
a measured quantity is really the sum of a large number of small, independent random contributions,
that sum turns out to be approximately normal, essentially regardless of the distribution of the
individual pieces. The binomial — a sum of many independent Bernoulli random variables — is a
special case of this, and starts to look normal once the number of trials is large. This is only a
preview; the precise statement and its proof come later.

## Linear transformations of normal random variables

Fix constants $a$ and $b$ and let $Y = aX+b$. Two facts about $\mathbf{E}[Y]$ and $\text{var}(Y)$
hold for *any* random variable $X$, normal or not:

$$\mathbf{E}[Y] = a\mathbf{E}[X]+b, \qquad \text{var}(Y) = a^2\,\text{var}(X).$$

The genuinely normal-specific fact is a third one: if $X$ is normal, then $Y$ is normal too,

$$X \sim N(\mu,\sigma^2) \implies Y = aX+b \sim N(a\mu+b,\ a^2\sigma^2).$$

Intuitively: "normal" means a specific bell shape, which can be centered anywhere and scaled to any
width. Multiplying $X$ by $a$ is just rescaling the axis — a bell shape stretched or compressed is
still a bell shape — and adding $b$ just slides the whole picture sideways. Under either operation a
bell shape stays a bell shape; only its center and width change. This is a genuine theorem with a
real proof, which is deferred to a few lectures later in the course — the argument above is only
the intuition for why it should be true.

## Calculating normal probabilities

There is no closed form for the normal CDF: the integral $\int_{-\infty}^{x} e^{-t^2/2}\,dt$ cannot
be written down in elementary functions. The practical fix is to tabulate it once, for the standard
normal only, and call the tabulated function $\Phi$:

$$\Phi(z) = P(Z\le z), \qquad Z \sim N(0,1).$$

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="shaded area under the standard normal curve to the left of z = 0.25">
  <defs>
    <clipPath id="tailclip">
      <rect x="0" y="0" width="170" height="200"/>
    </clipPath>
  </defs>
  <line x1="20" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <path d="M20,158 C60,158 80,40 160,40 C240,40 260,158 300,158" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <path d="M20,158 C60,158 80,40 160,40 C240,40 260,158 300,158 L300,160 L20,160 Z" fill="currentColor" fill-opacity="0.15" clip-path="url(#tailclip)" stroke="none"/>
  <line x1="170" y1="160" x2="170" y2="38" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="160" y="176" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <text x="170" y="193" text-anchor="middle" font-size="12" fill="currentColor">0.25</text>
</svg>
<figcaption>The shaded area is $\Phi(0.25) = P(Z \le 0.25)$ — exactly the number the table looks
up.</figcaption>
</figure>

There is no need to tabulate every possible $(\mu,\sigma^2)$, because of **standardizing**: given
$X \sim N(\mu,\sigma^2)$, define

$$Z = \frac{X-\mu}{\sigma}.$$

Subtracting $\mu$ removes the mean; dividing by $\sigma$ divides the variance by $\sigma^2$, leaving
variance $1$. And $Z$ is a linear function of a normal random variable, so by the fact of the
previous section, $Z$ is itself normal — hence $Z \sim N(0,1)$, a standard normal. The value of $Z$
is sometimes called a *normalized score*: it measures how many standard deviations $X$ sits above
(or, if negative, below) its mean — the same quantity behind reading a test score as "$1.5$ standard
deviations above average."

Standardizing turns any normal-probability question into a table lookup. For $X \sim N(\mu,\sigma^2)$,

$$P(X \le x) = P\!\left(\frac{X-\mu}{\sigma} \le \frac{x-\mu}{\sigma}\right)
= \Phi\!\left(\frac{x-\mu}{\sigma}\right).$$

**Worked example.** Let $X \sim N(2,16)$, so $\mu=2$ and $\sigma=4$. To find $P(X\le 3)$:

$$P(X\le 3) = P\!\left(\frac{X-2}{4} \le \frac{3-2}{4}\right) = \Phi(0.25).$$

Reading $\Phi(0.25)$ off the standard normal table (row $0.2$, column $.05$, since $0.2+0.05=0.25$):

| $z$ | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.0 | .5000 | .5040 | .5080 | .5120 | .5160 | .5199 | .5239 | .5279 | .5319 | .5359 |
| 0.1 | .5398 | .5438 | .5478 | .5517 | .5557 | .5596 | .5636 | .5675 | .5714 | .5753 |
| 0.2 | .5793 | .5832 | .5871 | .5910 | .5948 | **.5987** | .6026 | .6064 | .6103 | .6141 |
| 0.3 | .6179 | .6217 | .6255 | .6293 | .6331 | .6368 | .6406 | .6443 | .6480 | .6517 |

so $P(X\le 3) = \Phi(0.25) = 0.5987$. (A larger table, extending past $z=2.0$, is in the slides; only
the standard normal ever needs one.)

## The picture so far

The chapter's own summary is worth keeping as a dictionary, since it is exactly the correspondence
this chapter built and the gap it leaves open:

| Discrete | Continuous |
|---|---|
| $p_X(x)$ | $f_X(x)$ |
| $F_X(x) = \sum_{k\le x} p_X(k)$ | $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$ |
| $\mathbf{E}[X], \text{var}(X)$ — same formulas, sums vs. integrals | |
| $p_{X,Y}(x,y)$, $p_{X\mid Y}(x\mid y)$ | $f_{X,Y}(x,y)$, $f_{X\mid Y}(x\mid y)$ — not yet built |

Joint and conditional densities for continuous random variables are the natural next step, and are
not covered in this chapter.

## Exercises

1. Let $Z$ be a continuous random variable with density
   $$f_Z(z) = \begin{cases}\gamma(1+z^2), & -2 < z < 1,\\ 0, & \text{otherwise.}\end{cases}$$
   (a) For what value of $\gamma$ is this a valid probability density?
   (b) Find the cumulative distribution function of $Z$.

2. The taxi stand and the bus stop near Al's home are in the same location. Al arrives there at a
   fixed time. With probability $2/3$ a taxi is already waiting and he boards it immediately.
   Otherwise, he waits for whichever of a taxi or a bus arrives first: the next taxi arrives after a
   time uniformly distributed between $0$ and $10$ minutes, while the next bus arrives in exactly
   $5$ minutes. Find the CDF and the expected value of Al's waiting time.

3. Let $\lambda$ be a positive number. A continuous random variable $X$ is called **exponential**
   with parameter $\lambda$ if its density is
   $$f_X(x) = \begin{cases}\lambda e^{-\lambda x}, & x \ge 0,\\ 0, & \text{otherwise.}\end{cases}$$
   (a) Find the CDF of $X$.
   (b) Find $\mathbf{E}[X]$.
   (c) Find $\text{var}(X)$.
   (d) If $X_1, X_2, X_3$ are independent exponential random variables, each with parameter
   $\lambda$, find the density of $Z = \max\{X_1,X_2,X_3\}$.
   (e) Find the density of $W = \min\{X_1,X_2\}$.

## Sources

- **Slides:** `lectures/08-slides/01-lecture-8.md` (density, expectation/variance, the uniform
  example, the CDF, the mixed-distribution schematic, the normal density and the linear-function
  fact) and `02-calculating-normal-probabilities.md` (standardizing, the standard normal table, the
  closing discrete/continuous "constellation of concepts" summary). Course: MIT OCW 6.041SC,
  Lecture 8; readings given as Sections 3.1–3.3 of the course text.
- **Transcript:** `recordings/lectures/08.md` (John Tsitsiklis). Roughly: continuous random
  variables and the density [01:04]–[13:16]; expectation and variance translated [13:16]–[16:37];
  the uniform random variable [16:37]–[19:59]; the CDF, continuous and discrete [19:59]–[27:30]; the
  coin-and-wheel mixed random variable [27:30]–[31:42]; the normal density and its motivation
  [31:42]–[38:38]; linear transformations of normal random variables [38:38]–[40:57]; standardizing
  and the worked table example [41:00]–[48:42]; closing recap [48:42]–[49:51]. The transcript's
  spoken value for $\Phi(0.25)$ ("0.987") is corrected here to $0.5987$, the value the table in the
  slides actually gives for row $0.2$, column $.05$.
- **Exercises:** `recitations/08-slides.md`, problems 1–3, renumbered here. The supplied
  `psets/08-questions.md` (Markov chains) and `tutorials/08-slides.md` (Poisson processes) belong to
  a different point in the course's numbering than this lecture's topic and are not exercises for
  continuous random variables or the normal distribution, so they are not used in this chapter.
- **Referred to but not contained here:** the proof that a linear function of a normal random
  variable is normal (the transcript defers it "two or three lectures" ahead); the law-of-large-
  numbers justification of the long-run-average interpretation of expectation (deferred); joint and
  conditional densities for continuous random variables (the following lecture, per the closing
  recap).

---

[← 7. Multiple Random Variables and Independence](07-multiple-random-variables-and-independence.md) · [Contents](index.md) · [9. Joint and Conditional Continuous Densities →](09-joint-and-conditional-continuous-densities.md)
