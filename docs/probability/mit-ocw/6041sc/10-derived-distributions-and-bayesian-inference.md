---
title: "10. Derived Distributions and Bayesian Inference"
course: "MIT 6.041SC"
chapter: 10
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Derived Distributions and Bayesian Inference

## What this covers

Two questions, taken up in the order the lecture took them. First: given a joint model of an
unknown quantity $X$ and something you can actually observe, $Y$, how do you turn a known
conditional distribution "$Y$ given $X$" into the one you want, "$X$ given $Y$" — and does the
answer change when one variable is discrete and the other continuous? Second, and unrelated except
that it is the day's other piece of business: given the distribution of $X$ and a function $g$, how
do you find the distribution of $Y=g(X)$? This assumes the joint/conditional machinery for both
discrete and continuous random variables from earlier lectures — joint PMFs and PDFs, the
multiplication rule, and the CDF $F_X(x)=\mathbf P(X\le x)$.

## Where things stand: PMFs and PDFs run in parallel

For two discrete random variables, the joint PMF, the multiplication rule, and total probability
sit together as
$$
p_{X,Y}(x,y) = p_X(x)\,p_{Y\mid X}(y\mid x) = p_Y(y)\,p_{X\mid Y}(x\mid y), \qquad
p_X(x) = \sum_y p_{X,Y}(x,y).
$$
Every formula in the continuous world is the same formula with $p$'s replaced by $f$'s and sums by
integrals:
$$
f_{X,Y}(x,y) = f_X(x)\,f_{Y\mid X}(y\mid x) = f_Y(y)\,f_{X\mid Y}(x\mid y), \qquad
f_X(x) = \int f_{X,Y}(x,y)\,dy.
$$
The formulas match; the interpretation is subtler. A PDF is not a probability but a probability
*density* — mass per unit length, or for a joint density, mass per unit area. The conditional
density $f_{X\mid Y}(x\mid y)$ is the density of $X$ in the world where $Y$'s value is known. As a
function of $x$ with $y$ fixed, it is a slice of the joint density along $Y=y$, renormalised by the
constant $f_Y(y)$ so it integrates to $1$ over $x$. Expectations, variances, and CDFs carry over
from the discrete world unchanged in meaning.

## Bayesian inference: reversing the order of conditioning

Probability earns its keep by letting you reason about a quantity you cannot see directly from one
you can measure. The generic picture: an unknown random variable $X$ has a known distribution
(discrete: a PMF; continuous: a PDF), and a "measuring device" that, when the true state is $X$,
produces an observable $Y$ according to a known conditional law $p_{Y\mid X}$ or $f_{Y\mid X}$.
Having observed a value of $Y$, inference means finding the *posterior* — the full conditional
distribution of $X$ given that observation. Every version below starts from the same
multiplication-rule identity and ends by moving one factor across to reverse the conditioning; what
changes is only whether each variable is discrete or continuous.

### Both discrete

Familiar from earlier in the course — $X$ recording whether a plane is present, $Y$ whether the
radar beeped. Multiply $p_{X,Y}(x,y)$ two ways and equate:
$$
p_X(x)\,p_{Y\mid X}(y\mid x) = p_Y(y)\,p_{X\mid Y}(x\mid y)
\ \Longrightarrow\
p_{X\mid Y}(x\mid y) = \frac{p_X(x)\,p_{Y\mid X}(y\mid x)}{p_Y(y)}, \qquad
p_Y(y) = \sum_x p_X(x)\,p_{Y\mid X}(y\mid x).
$$

### Both continuous

Same argument, $p$'s replaced by $f$'s. Think of $X$ as a current through a resistor and $Y$ a
noisy analog measurement, $Y=X+(\text{Gaussian noise})$:
$$
f_{X\mid Y}(x\mid y) = \frac{f_X(x)\,f_{Y\mid X}(y\mid x)}{f_Y(y)}, \qquad
f_Y(y) = \int f_X(x)\,f_{Y\mid X}(y\mid x)\,dx.
$$
Bayes' rule survives unchanged in shape.

### Discrete unknown, continuous observation

Let $X$ be discrete and $Y$ continuous — the standard picture in communication: send one bit
$X\in\{0,1\}$ with prior $p_X(0), p_X(1)$, and a channel that adds Gaussian noise, so what arrives
is $Y=X+(\text{noise})$, continuous, with conditional density $f_{Y\mid X}(y\mid 0)$ differing from
$f_{Y\mid X}(y\mid 1)$. Neither formula above quite fits, since one side wants a $p$ and the other
an $f$; the formula has to be built by working with a short interval for $Y$ and only shrinking it
at the end.

Fix $x$ and small $\delta$, and write $\mathbf P(X=x,\ y\le Y\le y+\delta)$ two ways, using the
multiplication rule in each order:
$$
\mathbf P(X=x,\ y\le Y\le y+\delta) \approx p_X(x)\,f_{Y\mid X}(y\mid x)\,\delta
\quad\text{and}\quad
\approx f_Y(y)\,\delta\cdot p_{X\mid Y}(x\mid y),
$$
each approximation becoming exact as $\delta\to0$. The two describe the same probability, so
$\delta$ cancels, leaving a relation between one PMF and two PDFs:
$$
p_X(x)\,f_{Y\mid X}(y\mid x) = f_Y(y)\,p_{X\mid Y}(x\mid y)
\ \Longrightarrow\
p_{X\mid Y}(x\mid y) = \frac{p_X(x)\,f_{Y\mid X}(y\mid x)}{f_Y(y)}, \qquad
f_Y(y) = \sum_x p_X(x)\,f_{Y\mid X}(y\mid x).
$$

<figure>
<svg viewBox="0 0 340 210" role="img" aria-label="Two conditional densities of the observation Y, one for each value of a hidden bit X, with the observed value's height under each curve setting the posterior odds">
  <line x1="40" y1="160" x2="320" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <path d="M40,160 Q85,48 130,90 Q175,48 220,160 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <path d="M180,160 Q215,48 250,90 Q285,48 320,160 Z" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <text x="130" y="34" text-anchor="middle" font-size="12" fill="currentColor">X = 0</text>
  <text x="250" y="34" text-anchor="middle" font-size="12" fill="currentColor">X = 1</text>
  <line x1="200" y1="160" x2="200" y2="24" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="200" y="18" text-anchor="middle" font-size="11" fill="currentColor">observed y</text>
  <circle cx="200" cy="117.8" r="3" fill="currentColor"/>
  <circle cx="200" cy="108.6" r="3" fill="currentColor"/>
  <text x="330" y="164" text-anchor="end" font-size="11" fill="currentColor">y</text>
</svg>
<figcaption>The dashed line marks one observed value of Y. Its height under each curve is
$f_{Y\mid X}(y\mid 0)$ and $f_{Y\mid X}(y\mid 1)$; weighted by the priors, the ratio of these two
heights is exactly the posterior odds between X = 0 and X = 1 — no need to compute the normalising
$f_Y(y)$ just to compare the two hypotheses.</figcaption>
</figure>

### Continuous unknown, discrete observation

The remaining combination reverses the roles: $X$ continuous, $Y$ discrete. Example: a light source
driven by a current $X$ of unknown, continuous intensity; at low intensity, light arrives as
individual photons, so the instrument reports $Y$, a discrete photon count per second. The same
interval argument, roles swapped, gives
$$
f_{X\mid Y}(x\mid y) = \frac{f_X(x)\,p_{Y\mid X}(y\mid x)}{p_Y(y)}, \qquad
p_Y(y) = \int f_X(x)\,p_{Y\mid X}(y\mid x)\,dx.
$$

### The common shape, and why inference is still hard

All four formulas say the same thing: *posterior is proportional to prior times likelihood*, and
the denominator exists only to make the relevant marginal sum or integrate to one — it can always
be computed once the prior and the measuring-device model are known, so it is not itself a source
of difficulty. At the conceptual level, this one idea, applied according to which variable is which
type, is the whole of Bayesian inference. What makes inference hard in practice is not this
identity but choosing realistic models for $f_{Y\mid X}$ or $p_{Y\mid X}$, and then actually
carrying out the sum or integral in the denominator. The course returns to this in depth later in
the semester; what is established here is only the machinery.

## Derived distributions: the law of a function of a random variable

The rest of the lecture asks a purely mechanical question: given the distribution of $X$ and a
function $g$, find the distribution of $Y=g(X)$. This matters whenever a quantity of interest is
built out of another whose distribution is already known — a signal that is a function of a random
voltage, a travel time that is a function of a random speed, and so on. (A shortcut worth noting
first: if all that is wanted is $\mathbf E[g(X)]$, none of this is needed — that can be computed
directly from $f_X$ without ever finding the distribution of $Y$. Find $f_Y$ only when the whole
distribution, not just its mean, is actually wanted.)

### The discrete case is just relabelling

If $X$ is discrete with known PMF and $Y=g(X)$, then
$$
p_Y(y) = \mathbf P\big(g(X)=y\big) = \sum_{x\,:\,g(x)=y} p_X(x):
$$
the event $\{Y=y\}$ is, as a subset of the sample space, identical to the event that $X$ lands in
whichever set of $x$'s map to that $y$, so their probabilities agree, and the probability of a set
of $x$'s is the sum of the individual $p_X(x)$'s in it.

### Why the continuous case needs the CDF

The same argument on continuous variables gives nothing: $\{Y=y\}$ still equals the corresponding
event in $X$, but in the continuous world both events have probability zero, so the equality only
proves $0=0$. What is wanted is the *density* of $Y$, and a density is not reached by comparing
single points.

The fix is to work with the CDF instead: $\{Y\le y\}$ has positive probability, and the same
translation argument works on it — find the set of $x$'s for which $g(x)\le y$, and since
$\{Y\le y\}$ and that set are the same event,
$$
F_Y(y) = \mathbf P\big(g(X)\le y\big) = \mathbf P\big(X\in\{x : g(x)\le y\}\big),
$$
computable from the known distribution of $X$. Once $F_Y$ is known as a function of $y$ over its
*whole* range, differentiate: $f_Y(y) = \dfrac{d}{dy}F_Y(y)$. This is the two-step "cookbook"
procedure used below:

1. Write $F_Y(y)=\mathbf P(Y\le y)$, translate $\{Y\le y\}$ into an equivalent event about $X$
   using $Y=g(X)$, and evaluate its probability from the distribution of $X$ — tracking which
   range of $y$ the formula is valid for, since $Y$ typically does not range over all reals even
   when $X$ does.
2. Differentiate $F_Y$ to get $f_Y$, setting $f_Y(y)=0$ outside the range found in step 1.

### Worked example: the cube of a uniform random variable

Let $X\sim\text{Uniform}(0,2)$ and $Y=X^3$. Since $X$ ranges over $[0,2]$, $Y$ ranges over $[0,8]$.
A natural guess: since all values of $X$ are equally likely, perhaps all values of $Y$ are too. The
cookbook procedure checks this.

Step 1, for $y\in[0,8]$:
$$
F_Y(y) = \mathbf P(X^3\le y) = \mathbf P\big(X\le y^{1/3}\big),
$$
taking cube roots (an increasing function, so the inequality's direction is unchanged). Since $X$
is uniform on $[0,2]$ with density $\tfrac12$ there, this is the area under that density from $0$ to
$y^{1/3}$ — a rectangle of base $y^{1/3}$ and height $\tfrac12$ (forced by the total area under the
density equalling $1$ over a base of length $2$):
$$
F_Y(y) = \frac{y^{1/3}}{2}, \qquad 0\le y\le 8,
$$
with $F_Y(y)=0$ for $y<0$ and $F_Y(y)=1$ for $y>8$.

Step 2, differentiate on $(0,8)$:
$$
f_Y(y) = \frac{d}{dy}\left(\frac{y^{1/3}}{2}\right) = \frac{1}{6}\,y^{-2/3} = \frac{1}{6\,y^{2/3}},
\qquad 0<y<8,
$$
and $f_Y(y)=0$ elsewhere. The guess was wrong: $Y$ is not uniform. The density blows up as
$y\to0^+$ and decreases across $(0,8)$ — small values of $Y$ are far more crowded than large ones,
even though $X$ was perfectly uniform. Cubing stretches the map from $x$ to $y$ unevenly (a fixed
increment in $x$ near $0$ produces a far smaller increment in $y=x^3$ than the same increment near
$x=2$), and that uneven stretching reshapes a flat density into $1/(6y^{2/3})$.

### Worked example: travel time as a function of speed

Set the cruise control to a speed $V$, uniform on $[30,60]$, and drive a fixed distance of $200$.
The trip takes $T=200/V$. Find the distribution of $T$.

As $V$ ranges over $[30,60]$, $T=200/V$ ranges over $\left[\tfrac{200}{60},\tfrac{200}{30}\right] =
\left[\tfrac{10}{3}, \tfrac{20}{3}\right]$ — and since $200/v$ is *decreasing*, the smallest $v$
gives the largest $t$. This is the twist against the previous example: $X^3$ was increasing, so
translating $\{Y\le y\}$ kept the inequality's direction; $200/v$ is decreasing, so translating
$\{T\le t\}$ will flip it.

Step 1, for $t$ in the range above:
$$
F_T(t) = \mathbf P\!\left(\frac{200}{V}\le t\right) = \mathbf P\!\left(V \ge \frac{200}{t}\right):
$$
your travel time is below a threshold exactly when your speed is above the corresponding threshold.
This is again an area under the uniform density of $V$, from $200/t$ up to $60$ — height
$\tfrac{1}{30}$, base $60-\tfrac{200}{t}$:
$$
F_T(t) = \frac{60 - 200/t}{30}, \qquad \frac{10}{3}\le t\le \frac{20}{3},
$$
valid precisely when $200/t$ falls in $[30,60]$; $F_T(t)=0$ below the range and $1$ above it.

Step 2, differentiate:
$$
f_T(t) = \frac{d}{dt}\left(\frac{60-200/t}{30}\right) = \frac{1}{30}\cdot\frac{200}{t^2}
= \frac{20}{3\,t^2}, \qquad \frac{10}{3}<t<\frac{20}{3},
$$
zero elsewhere. General lesson: whenever $g$ is decreasing rather than increasing, some inequality
in step 1 has to flip, and it is easy to get this backwards under time pressure — re-derive the
direction from the definition of $g$ rather than guessing.

### Linear functions of a random variable

The most useful special case is $Y=aX+b$. Picture $X$ with some arbitrarily-shaped density on
$[-1,2]$, built up in two stages: first $2X$, then $2X+5$.

Multiplying by $2$ changes only the scale: everywhere $X$ could land, $2X$ lands at twice the value
with the same relative likelihoods, so the range doubles, from $[-1,2]$ to $[-2,4]$. As a picture,
this stretches the density horizontally by $2$ — replacing the argument $z$ by $z/2$ is what
stretches a graph by $2$ (not $2z$, which compresses it). But stretching horizontally without
changing height doubles the area underneath, and a density's area must stay at $1$, so the height
is halved too. Adding $5$ afterwards shifts every value up by $5$ without changing the shape at
all — it slides the graph $5$ units right, from $[-2,4]$ to $[3,9]$.

<figure>
<svg viewBox="0 0 340 270" role="img" aria-label="Stretching the density of X by a factor of two to get the density of 2X, then shifting it by five to get the density of 2X plus 5">
  <defs>
    <path id="bump" d="M0,0 C0.15,-0.1 0.25,-0.9 0.45,-0.95 C0.6,-1 0.7,-0.4 0.8,-0.15 C0.9,-0.05 0.95,-0.02 1,0 Z"/>
  </defs>
  <line x1="65.45" y1="100" x2="141.82" y2="100" stroke="currentColor" stroke-width="1.5"/>
  <use href="#bump" transform="translate(65.45,100) scale(76.36,45)" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke"/>
  <text x="6" y="98" font-size="12" fill="currentColor">X</text>
  <text x="65.45" y="114" text-anchor="middle" font-size="11" fill="currentColor">-1</text>
  <text x="141.82" y="114" text-anchor="middle" font-size="11" fill="currentColor">2</text>

  <line x1="40" y1="170" x2="192.73" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <use href="#bump" transform="translate(40,170) scale(152.73,22.5)" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke"/>
  <text x="6" y="168" font-size="12" fill="currentColor">2X</text>
  <text x="40" y="184" text-anchor="middle" font-size="11" fill="currentColor">-2</text>
  <text x="192.73" y="184" text-anchor="middle" font-size="11" fill="currentColor">4</text>

  <line x1="167.27" y1="240" x2="320" y2="240" stroke="currentColor" stroke-width="1.5"/>
  <use href="#bump" transform="translate(167.27,240) scale(152.73,22.5)" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke"/>
  <text x="6" y="238" font-size="12" fill="currentColor">2X + 5</text>
  <text x="167.27" y="254" text-anchor="middle" font-size="11" fill="currentColor">3</text>
  <text x="320" y="254" text-anchor="middle" font-size="11" fill="currentColor">9</text>
</svg>
<figcaption>Doubling a random variable stretches its density horizontally by 2 and halves its
height to keep the area at 1; adding 5 then slides the whole graph right without changing its
shape, from a range of [-2, 4] to a range of [3, 9].</figcaption>
</figure>

The picture is convincing, but the cookbook procedure gives the same answer without a drawing, and
is worth doing once because $a<0$ genuinely differs. Take $a>0$ first:
$$
F_Y(y) = \mathbf P(aX+b\le y) = \mathbf P\!\left(X\le \frac{y-b}{a}\right) = F_X\!\left(\frac{y-b}{a}\right),
$$
dividing by the positive $a$ leaves the inequality's direction alone. Differentiating by the chain
rule,
$$
f_Y(y) = f_X\!\left(\frac{y-b}{a}\right)\cdot\frac{1}{a}.
$$
Now $a<0$: this formula cannot be right, since a density is never negative while $a$ is. The
breaking step is dividing $aX+b\le y$ by $a$: dividing by a *negative* number reverses the
inequality, so
$$
F_Y(y) = \mathbf P\!\left(X\ge \frac{y-b}{a}\right) = 1 - F_X\!\left(\frac{y-b}{a}\right),
$$
and differentiating introduces a minus sign that cancels the one already carried by the negative
$a$:
$$
f_Y(y) = -f_X\!\left(\frac{y-b}{a}\right)\cdot\frac{1}{a} = f_X\!\left(\frac{y-b}{a}\right)\cdot\frac{1}{|a|}.
$$
The two cases combine into one formula, valid for any $a\neq0$:
$$
\boxed{f_Y(y) = \frac{1}{|a|}\,f_X\!\left(\frac{y-b}{a}\right)}, \qquad Y = aX+b.
$$
One consequence, stated without the algebra: substituting the normal density for $f_X$ shows that
$aX+b$ is again normal whenever $X$ is — the calculation that justifies the fact, used earlier in
the course without proof, that a linear function of a normal random variable is itself normal.

## Exercises

Transcribed from this week's problem set, recitation, and tutorial as supplied. Some of them (the
financial-parable and vote-counting problems, and the Markov chain problems) belong to the central
limit theorem and Markov chain material taught elsewhere in the course, not to this lecture; they
appear here only because they share its number in the source materials — see Sources.

### From Problem Set 10

**1. A financial parable.** An investment bank manages \$1 billion, invested in housing-related
assets. Because the money is borrowed, the bank's actual capital is only \$50 million (5%), so a
loss of more than 5% makes it insolvent.

(a) The bank considers a single asset whose one-year gain $R$ (percentage points) is normal with
mean $7$ and standard deviation $10$. Find the probability of insolvency. Would you accept this
risk?

(b) To diversify, the bank instead puts \$50 million into each of twenty assets, the $i$th having
gain $R_i$, again normal with mean $7$, standard deviation $10$, modelled as independent; overall
gain is $(R_1+\cdots+R_{20})/20$. Find the probability of insolvency under this model.

(c) In fact the $R_i$ are positively correlated, with $\rho(R_i,R_j)=1/2$ for every $i\neq j$. Find
the probability of insolvency now, assuming $(R_1+\cdots+R_{20})/20$ is normal.

**2.** The adult population of Nowhereville has 300 males and 196 females. Each male (respectively
female) votes independently with probability $0.4$ (respectively $0.5$). Find a good numerical
approximation for the probability that more males than females vote.

**3.** Let $S_n$ be the number of successes in $n$ independent Bernoulli$(1/2)$ trials. Give a
numerical value for the limit, as $n\to\infty$, of each of:

(a) $\mathbf P\!\left(\dfrac{n}{2}-10\le S_n\le \dfrac{n}{2}+10\right)$

(b) $\mathbf P\!\left(\dfrac{n}{2}-\dfrac{n}{10}\le S_n\le \dfrac{n}{2}+\dfrac{n}{10}\right)$

(c) $\mathbf P\!\left(\dfrac{n}{2}-\dfrac{\sqrt n}{2}\le S_n\le \dfrac{n}{2}+\dfrac{\sqrt n}{2}\right)$

**4.** Alice has two coins: the first shows heads with probability $1/3$, the second with
probability $2/3$, otherwise indistinguishable. She sends Bob a coin chosen at random, picking the
first coin with probability $p$. Bob flips the coin $3$ times, independently, and lets $Y$ be the
number of heads observed.

(a) Given $k$ heads observed, what is the probability Bob received the first coin?

(b) For which $k$ does observing $k$ heads out of $3$ tosses *increase* the probability that Bob
received the first coin, relative to the prior $p$? How does the answer change as $p$ increases?

(c) Design a decision rule for Bob, based on $k$, that minimises his probability of error.

(d) Take $p=2/3$.
   (i) Find the probability that the rule from (c) guesses correctly.
   (ii) Compare with the probability of guessing correctly before flipping the coin at all.

(e) How does increasing $p$ affect the rule from (c)?

(f) For which $p$ does the rule never decide "first coin", regardless of outcome?

(g) For which $p$ does the rule always decide "first coin", regardless of outcome?

**5.** Consider a Bernoulli process $X_1,X_2,X_3,\dots$ with unknown success probability $q$. Let
$Y_k$ be the time of the $k$th success and define inter-arrival times $T_1=Y_1$,
$T_k=Y_k-Y_{k-1}$ for $k\ge2$. This problem estimates $q$ from observed inter-arrival times
$t_1,t_2,\dots$.

You may use: for non-negative integers $k,m$, $\displaystyle\int_0^1 q^k(1-q)^m\,dq =
\frac{k!\,m!}{(k+m+1)!}$.

In parts (a)–(c), $q$ is the value of a random variable $Q$, uniform on $[0,1]$.

(a) Find the PMF of $T_1$, $p_{T_1}(t_1)$.

(b) Find the least-squares estimate (LSE) of $Q$ given $T_1=t_1$.

(c) Find the maximum a posteriori (MAP) estimate of $Q$ given $T_1=t_1,\dots,T_k=t_k$.

For part (d) only, $Q$ is instead uniform on $[0.5,1]$.

(d) Find the linear least-squares estimate (LLSE) of $T_2$ based on the observed $T_1=t_1$.

**6.** The joint PDF of $X$ and $Y$ is
$$
f_{X,Y}(x,y) = \begin{cases} c\,x\,y & 0<x\le1,\ 0<y\le1\\ 0 & \text{otherwise.}\end{cases}
$$

(a) Find the normalising constant $c$.

(b) Find the conditional expectation estimator of $X$ based on the observed value $Y=y$.

(c) Is this estimate different from what you would have guessed before observing $Y=y$? Explain.

(d) Repeat (b) and (c) for the MAP estimator.

### From Recitation 10

**Question 1.** For a probabilistic model with sample space $\Omega$, events $A,B$, and a discrete
random variable $X$ (all conditioning below is on events of positive probability): an identity is
*true* if it holds with no further assumptions, *false* if some counterexample exists.

1.1 Which one of the following is true?
(a) $\mathbf P(A\cap B)$ may be larger than $\mathbf P(A)$.
(b) The variance of $X$ may be larger than the variance of $2X$.
(c) If $A^c\cap B^c=\varnothing$, then $\mathbf P(A\cup B)=1$.
(d) If $A^c\cap B^c=\varnothing$, then $\mathbf P(A\cap B) = \mathbf P(A)\mathbf P(B)$.
(e) If $\mathbf P(A)>1/2$ and $\mathbf P(B)>1/2$, then $\mathbf P(A\cup B)=1$.

1.2 Which one of the following is true?
(a) If $\mathbf E[X]=0$, then $\mathbf P(X>0)=\mathbf P(X<0)$.
(b) $\mathbf P(A) = \mathbf P(A\mid B) + \mathbf P(A\mid B^c)$.
(c) $\mathbf P(B\mid A) + \mathbf P(B\mid A^c) = 1$.
(d) $\mathbf P(B\mid A) + \mathbf P(B^c\mid A^c) = 1$.
(e) $\mathbf P(B\mid A) + \mathbf P(B^c\mid A) = 1$.

**Question 2.** Heather and Taylor play a game with independent tosses of a coin that comes up
heads with probability $p$, $0<p<1$. Tossing continues until either heads has appeared twice
(Heather wins) or tails has appeared twice (Taylor wins); a full game takes $2$ or $3$ tosses.

2.1 List the outcomes of a full game (as head/tail sequences) with their probabilities.

2.2 What is the probability that Heather wins?

2.3 What is the conditional probability that Heather wins, given the first toss is heads?

2.4 What is the conditional probability that the first toss was heads, given that Heather wins?

**Question 3.** A casino offers a game with a fair four-sided die (faces $1,2,3,4$). The **basic
game** is one or two rolls: a first roll of $1,2,$ or $3$ wins that many dollars and ends the game;
a first roll of $4$ wins $2 plus one further ("bonus") roll. Let $X$ be the basic game's payoff.

3.1 Find the PMF of $X$, $p_X(x)$.

3.2 Find $\mathbf E[X]$.

3.3 Find the conditional PMF of the first roll given $X=3$ (state your notation clearly).

3.4 In an **extended game**, a roll of $1,2,$ or $3$ still wins that amount and ends the game, but
a roll of $4$ wins $2 *and* the game continues with another roll (possibly another $4$, and so on
indefinitely). Let $Y$ be the extended game's payoff. Find $\mathbf E[Y]$.

### From Tutorial 10

**1.** Let $X$ be the height, in metres, of a randomly selected Canadian (uniform selection), and
$h=\mathbf E[X]$. Bo, confident no Canadian exceeds $3$ metres, uses $1.5$ metres as a conservative
upper bound on the standard deviation of $X$. He estimates $h$ by averaging the heights of $n$
randomly selected Canadians, $H$.

(a) In terms of $h$ and Bo's bound, give the mean and standard deviation of $H$.

(b) Find the minimum $n$ guaranteeing the standard deviation of $H$ is below $0.01$ metres.

(c) Using Chebyshev's inequality, find the minimum $n$ for Bo to be $99\%$ sure his estimate is
within $5$ centimetres of the true average height.

(d) Given that no Canadian exceeds three metres, explain why $1.5$ metres is a valid upper bound on
the standard deviation of $X$.

**2.** In any week of taking 6.041, a student is up-to-date or behind. If up-to-date, she is
up-to-date the next week with probability $0.8$ (behind with $0.2$); if behind, up-to-date the next
week with probability $0.6$ (behind with $0.4$) — independent of earlier weeks. Model this as a
two-state Markov chain, State 1 = up-to-date, State 2 = behind.

(a) Find the mean first-passage time to State 1, starting from State 2.

(b) Find the mean recurrence time to State 1.

**3.** A Markov chain has steady-state probabilities $\pi_1=\tfrac{6}{31}$, $\pi_2=\tfrac{9}{31}$,
$\pi_3=\tfrac{6}{31}$, $\pi_4=\tfrac{10}{31}$. Suppose the process is in State 1 just before the
first transition.

(a) Find the mean and variance of $K$, the number of transitions up to and including the next
return to State 1.

(b) Find the probability that the state resulting from transition $1000$ differs from both the
state resulting from transition $999$ and the state resulting from transition $1001$.

## Sources

- Lecture 10 transcript, `recordings/lectures/10.md` ("10 captions"): 00:00–19:52 covers inference
  (PMF–PDF recap 01:02–03:06; the four discrete/continuous Bayes combinations 06:25–19:52,
  including the interval-based derivation of the mixed case at 12:04–16:31); 19:52–47:49 covers
  derived distributions (two-step method 20:56–26:40; the $Y=X^3$ example 26:40–32:17; the
  $T=200/V$ example 32:17–37:57; the linear-function formula, by picture and by the CDF method,
  37:57–47:49). The transcript is speech over an uncaptured blackboard; the formulas, the interval
  argument for mixed inference, and both derived-distribution examples were reconstructed from
  what the lecturer describes doing on the board, since no slide deck or board image exists for
  this lecture. The claim at 47:49 that this method also proves an earlier, unproved assertion —
  that a linear function of a normal random variable is normal — is reported in the same unproved
  form; the supporting algebra was not carried out on the board.
- Problem Set 10 (`psets/10-questions.md`), Questions 1–6, transcribed in full. Questions 1–3
  concern the central limit theorem, not this lecture; Questions 4–6 (the two-coin inference
  problem, the Bernoulli-process estimation problem, and the joint-density conditional/MAP
  estimator problem) directly exercise this lecture's inference formulas. Reconstructed by a model
  from a PDF with no text layer; its equations are unverified.
- Recitation 10 slides (`recitations/10-slides/01-10-slides-part-01.md`,
  `02-10-slides-part-02.md`), Questions 1–3, transcribed in full; general review of probability
  identities, conditional probability, and conditional PMFs, not specific to this lecture.
  Likewise reconstructed by a model from a PDF with no text layer.
- Tutorial 10 slides (`tutorials/10-slides.md`), Questions 1–3, transcribed in full; concerns
  Chebyshev's inequality and Markov chains, taught elsewhere in the course. Likewise reconstructed
  by a model from a PDF with no text layer; Question 3 refers to a Markov chain diagram not
  reproduced in the converted text.

---

[← 9. Joint and Conditional Continuous Densities](09-joint-and-conditional-continuous-densities.md) · [Contents](index.md) · [11. Derived Distributions, Convolutions, and Covariance →](11-derived-distributions-convolutions-and-covariance.md)
