---
title: "10. Derived Distributions and Bayesian Inference"
course: "MIT 6.041SC"
chapter: 10
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. Derived Distributions and Bayesian Inference

## What this covers

Two questions, taken up in the order the lecture took them. First: given a joint model of an
unknown quantity $X$ and something you can actually observe, $Y$, how do you turn a known
conditional distribution "$Y$ given $X$" into the one you actually want, "$X$ given $Y$" — and
does the answer change when one of the two variables is discrete and the other continuous? Second,
and unrelated except that it is the day's other piece of business: given the distribution of a
random variable $X$ and a function $g$, how do you find the distribution of $Y=g(X)$? This assumes
the joint and conditional machinery for both discrete and continuous random variables from earlier
lectures — joint PMFs and PDFs, the multiplication rule, and the CDF $F_X(x)=\mathbf P(X\le x)$.

## Where things stand: PMFs and PDFs run in parallel

For two discrete random variables, the joint PMF, the multiplication rule, and total probability
sit together as
$$
p_{X,Y}(x,y) = p_X(x)\,p_{Y\mid X}(y\mid x) = p_Y(y)\,p_{X\mid Y}(x\mid y), \qquad
p_X(x) = \sum_y p_{X,Y}(x,y).
$$
Every formula in the continuous world is the same formula with $p$'s replaced by $f$'s and sums
replaced by integrals:
$$
f_{X,Y}(x,y) = f_X(x)\,f_{Y\mid X}(y\mid x) = f_Y(y)\,f_{X\mid Y}(x\mid y), \qquad
f_X(x) = \int f_{X,Y}(x,y)\,dy.
$$
The formulas look identical; the interpretation is the subtler thing. A PDF is not a probability —
it is a probability *density*, mass per unit length (or, for a joint density, mass per unit area).
The conditional density $f_{X\mid Y}(x\mid y)$ is the density of $X$ in the world where you have
been told the value of $Y$. As a function of $x$ with $y$ held fixed, it is just a slice of the
joint density along the line $Y=y$, renormalised by the constant $f_Y(y)$ so that it integrates to
$1$ over $x$. Expectations, variances, and CDFs carry over from the discrete world to the
continuous one without change of meaning.

## Bayesian inference: reversing the order of conditioning

Probability earns its keep by letting you reason about a quantity you cannot see directly from
one you can measure. The generic picture: there is an unknown random variable $X$ with a known
distribution (discrete: a PMF; continuous: a PDF), and a "measuring device" that, when the true
state is $X$, produces an observable $Y$ according to a known conditional law $p_{Y\mid X}$ or
$f_{Y\mid X}$. Having observed a particular value of $Y$, the inference problem is to find the
*posterior* — the full conditional distribution of $X$ given that observation, not just a single
guess. Every version of this problem starts from the same multiplication-rule identity and ends by
moving one factor to the other side to reverse the conditioning; what changes across the four
cases below is only whether each variable is discrete or continuous, hence whether it contributes
a $p$ or an $f$ to the formula.

### Both discrete

This is the case already familiar from earlier in the course — e.g. $X$ recording whether a plane
is present and $Y$ recording whether the radar beeped. Multiply $p_{X,Y}(x,y)$ two ways and equate:
$$
p_X(x)\,p_{Y\mid X}(y\mid x) = p_Y(y)\,p_{X\mid Y}(x\mid y)
\quad\Longrightarrow\quad
p_{X\mid Y}(x\mid y) = \frac{p_X(x)\,p_{Y\mid X}(y\mid x)}{p_Y(y)}, \qquad
p_Y(y) = \sum_x p_X(x)\,p_{Y\mid X}(y\mid x).
$$

### Both continuous

Same argument, $p$'s replaced by $f$'s. Think of $X$ as a current through a resistor and $Y$ as a
noisy analog measurement of it, say $Y=X+(\text{Gaussian noise})$:
$$
f_{X\mid Y}(x\mid y) = \frac{f_X(x)\,f_{Y\mid X}(y\mid x)}{f_Y(y)}, \qquad
f_Y(y) = \int f_X(x)\,f_{Y\mid X}(y\mid x)\,dx.
$$
Everything you know as "Bayes' rule" from the discrete case survives unchanged in shape.

### Discrete unknown, continuous observation

Now let $X$ be discrete and $Y$ continuous — the standard picture in communication: you send a
single bit $X\in\{0,1\}$ with prior $p_X(0), p_X(1)$, and the channel adds Gaussian noise, so what
arrives is $Y=X+(\text{noise})$, a continuous random variable whose conditional density
$f_{Y\mid X}(y\mid 0)$ differs in location (or shape) from $f_{Y\mid X}(y\mid 1)$. Neither of the
two formulas above quite applies, because one variable wants a $p$ and the other wants an $f$. The
formula has to be built from scratch, and the way to do it is to work with a short interval for $Y$
rather than a single value, and only take the interval to zero at the end.

Fix $x$ and a small $\delta$, and look at the event $\{X=x\}\cap\{y\le Y\le y+\delta\}$. Write its
probability two ways, using the multiplication rule in each order:
$$
\mathbf P(X=x,\ y\le Y\le y+\delta) = p_X(x)\cdot \mathbf P(y\le Y\le y+\delta\mid X=x)
\approx p_X(x)\,f_{Y\mid X}(y\mid x)\,\delta,
$$
$$
\mathbf P(X=x,\ y\le Y\le y+\delta) = \mathbf P(y\le Y\le y+\delta)\cdot \mathbf P(X=x\mid y\le Y\le y+\delta)
\approx f_Y(y)\,\delta\cdot p_{X\mid Y}(x\mid y).
$$
Both are approximations that become exact as $\delta\to0$; the two right-hand sides are describing
the same probability, so they are equal, and the common factor of $\delta$ cancels, leaving a clean
relation between a PMF and two PDFs:
$$
p_X(x)\,f_{Y\mid X}(y\mid x) = f_Y(y)\,p_{X\mid Y}(x\mid y).
$$
Moving the unwanted factor to the other side gives the inference formula for this mixed case:
$$
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
<figcaption>The vertical line marks one observed value of Y. Its height under each curve is
$f_{Y\mid X}(y\mid 0)$ and $f_{Y\mid X}(y\mid 1)$; weighted by the priors $p_X(0)$ and $p_X(1)$,
the ratio of these two heights is exactly the posterior odds between X = 0 and X = 1 — no need to
compute the normalising $f_Y(y)$ at all if only the comparison is wanted.</figcaption>
</figure>

### Continuous unknown, discrete observation

The remaining combination reverses the roles: $X$ continuous, $Y$ discrete. A physical example
from the lecture: a light source is driven by a current $X$ of unknown, continuous intensity, and
at low intensity the light arrives as individual photons, so the instrument reports $Y$, a discrete
photon count in one second. The same interval argument, with the roles of discrete and continuous
swapped, gives
$$
f_{X\mid Y}(x\mid y) = \frac{f_X(x)\,p_{Y\mid X}(y\mid x)}{p_Y(y)}, \qquad
p_Y(y) = \int f_X(x)\,p_{Y\mid X}(y\mid x)\,dx.
$$

### The common shape, and why inference is still hard

All four formulas say the same thing: *posterior is proportional to prior times likelihood*, and
whatever sits in the denominator is there only to make the appropriate marginal integrate or sum to
one — and that denominator can always be computed once the prior and the model of the measuring
device are known, so it never causes real difficulty on its own. At the conceptual level, this one
idea, applied four times according to which variable is which type, is the whole of Bayesian
inference. What makes inference a subject that people spend careers on is not this identity but
the practical part it hides: choosing realistic models for $f_{Y\mid X}$ or $p_{Y\mid X}$, and then
actually carrying out the sum or integral in the denominator, which can be difficult even when
every ingredient is explicit. The course returns to this in depth later in the semester with many
more worked examples; what is established here is only the machinery.

## Derived distributions: the law of a function of a random variable

The rest of the lecture is a different, purely mechanical, question: given the distribution of
$X$ and a function $g$, find the distribution of $Y=g(X)$. This matters whenever a quantity of
interest is built out of another one whose distribution you already know — a signal that is some
function of a random voltage, a travel time that is a function of a random speed, a ratio of two
random variables, and so on. (An important shortcut before starting: if all that is wanted is the
*expectation* $\mathbf E[g(X)]$, none of this machinery is needed — that can be computed directly
from $f_X$ without ever finding the distribution of $Y$ itself. The distribution of $Y$ is worth
finding only when the whole distribution, not just its mean, is actually wanted.)

### The discrete case is just relabelling

If $X$ is discrete with known PMF and $Y=g(X)$, then
$$
p_Y(y) = \mathbf P(Y=y) = \mathbf P\big(g(X)=y\big) = \sum_{x\,:\,g(x)=y} p_X(x):
$$
the event $\{Y=y\}$ is identical, as a subset of the sample space, to the event that $X$ lands in
whichever set of $x$'s map to that $y$, so their probabilities are equal, and the probability of a
set of $x$'s is just the sum of the individual $p_X(x)$'s in it.

### Why the continuous case needs the CDF

The same argument, tried verbatim on continuous variables, produces nothing useful: the event
$\{Y=y\}$ still equals the event that $X$ lies in the corresponding set, but in the continuous
world both of these events have probability zero, so equating them only proves $0=0$. What is
wanted is not the probability of a single value but the *density* of $Y$, and the density is not
reached by comparing single points.

The fix is to work with the cumulative distribution function instead of individual points, because
a CDF is built from an event of positive probability — an interval, or in practice a half-line
$\{Y\le y\}$ — for which the same translation argument does work: find the set of $x$'s for which
$g(x)\le y$, and since $\{Y\le y\}$ and that set of $x$'s are the same event,
$$
F_Y(y) = \mathbf P(Y\le y) = \mathbf P\big(g(X)\le y\big) = \mathbf P(X\in \{x : g(x)\le y\}),
$$
which can be computed from the known distribution of $X$. Once $F_Y$ is known as a function of $y$
over its *whole* range, the density follows by differentiating: $f_Y(y) = \dfrac{d}{dy}F_Y(y)$.
This is the two-step "cookbook" procedure used for every example below:

1. Write $F_Y(y)=\mathbf P(Y\le y)$, translate the event $\{Y\le y\}$ into an equivalent event
   about $X$ using $Y=g(X)$, and evaluate its probability from the distribution of $X$ — being
   careful to track which range of $y$ the resulting formula is valid for, since $Y$ typically does
   not range over all reals even when $X$ does.
2. Differentiate $F_Y$ with respect to $y$ to get $f_Y$, setting $f_Y(y)=0$ wherever $y$ falls
   outside the range found in step 1.

### Worked example: the cube of a uniform random variable

Let $X\sim\text{Uniform}(0,2)$ and $Y=X^3$. Since $X$ ranges over $[0,2]$, $Y$ ranges over $[0,8]$.
A natural guess is that, since all values of $X$ are equally likely, all values of $Y$ should be
too — cubing might seem to just relabel the outcomes without favouring any of them. The cookbook
procedure checks this.

Step 1: for $y\in[0,8]$,
$$
F_Y(y) = \mathbf P(X^3\le y) = \mathbf P\big(X\le y^{1/3}\big),
$$
taking cube roots of both sides of the inequality (a cube root is an increasing function, so the
direction of the inequality is unchanged). Since $X$ is uniform on $[0,2]$ with density $\tfrac12$
there, this probability is the area under that density from $0$ to $y^{1/3}$ — a rectangle of base
$y^{1/3}$ and height $\tfrac12$ (the height is forced to be $\tfrac12$ by the requirement that the
total area under the density equal $1$ over a base of length $2$):
$$
F_Y(y) = \frac{y^{1/3}}{2}, \qquad 0\le y\le 8,
$$
with $F_Y(y)=0$ for $y<0$ and $F_Y(y)=1$ for $y>8$.

Step 2: differentiate on $(0,8)$:
$$
f_Y(y) = \frac{d}{dy}\left(\frac{y^{1/3}}{2}\right) = \frac{1}{6}\,y^{-2/3} = \frac{1}{6\,y^{2/3}},
\qquad 0<y<8,
$$
and $f_Y(y)=0$ elsewhere. So the guess was wrong: $Y$ is not uniform at all. The density blows up
as $y\to0^+$ and decreases across $(0,8)$ — small values of $Y$ are, in a density sense, far more
crowded than large ones, even though the underlying $X$ was perfectly uniform. Cubing stretches
the mapping from $x$ to $y$ unevenly (a fixed increment in $x$ near $0$ produces a much smaller
increment in $y=x^3$ than the same increment near $x=2$), and that uneven stretching is exactly
what reshapes a flat density into $1/(6y^{2/3})$.

### Worked example: travel time as a function of speed

Set the cruise control to a speed $V$, uniformly distributed between $30$ and $60$, and drive a
fixed distance of $200$. The time the trip takes is $T = 200/V$. Find the distribution of $T$.

As $V$ ranges over $[30,60]$, $T=200/V$ ranges over $\left[\tfrac{200}{60},\tfrac{200}{30}\right]
= \left[\tfrac{10}{3}, \tfrac{20}{3}\right]$ — and because $200/v$ is a *decreasing* function of
$v$, the smallest $v$ gives the largest $t$ and vice versa. This reversal is the "twist" against
the previous example: $X^3$ was increasing, so translating $\{Y\le y\}$ kept the inequality
pointing the same way; $200/v$ is decreasing, so translating $\{T\le t\}$ will flip it.

Step 1: for $t$ in the range above,
$$
F_T(t) = \mathbf P\!\left(\frac{200}{V}\le t\right) = \mathbf P\!\left(V \ge \frac{200}{t}\right),
$$
where dividing the inequality $200\le tV$ by $t>0$ leaves the direction unchanged, but solving
$200/V\le t$ for $V$ requires dividing by $V$, and it is exactly this rearrangement that produces
the "$\ge$": your travel time is less than some threshold *exactly when* your speed is bigger than
the corresponding threshold. This probability is again an area under the uniform density of $V$,
now from $200/t$ up to $60$ — a rectangle of height $\tfrac{1}{30}$ (the height of the uniform
density on $[30,60]$) and base $60-\tfrac{200}{t}$:
$$
F_T(t) = \frac{60 - 200/t}{30}, \qquad \frac{10}{3}\le t\le \frac{20}{3},
$$
valid precisely for those $t$ for which $200/t$ actually falls in $[30,60]$, i.e. for $t$ in the
stated range; $F_T(t)=0$ below it and $F_T(t)=1$ above it.

Step 2: differentiate on the open interval:
$$
f_T(t) = \frac{d}{dt}\left(\frac{60-200/t}{30}\right) = \frac{1}{30}\cdot\frac{200}{t^2}
= \frac{20}{3\,t^2}, \qquad \frac{10}{3}<t<\frac{20}{3},
$$
and $f_T(t)=0$ elsewhere. The general lesson: whenever $g$ is monotonically decreasing rather than
increasing, some inequality in step 1 has to flip direction, and it is easy to get this backwards
under time pressure — always re-derive the direction from the definition of $g$ rather than
guessing.

### Linear functions of a random variable

The most useful special case is $Y=aX+b$. Picture $X$ with some given, arbitrarily-shaped density
on $[-1,2]$, and build $Y$ up in two stages: first $2X$, then $2X+5$.

Multiplying by $2$ changes only the scale on which the random variable is measured: everywhere $X$
could have landed, $2X$ lands at twice the value, with the same relative likelihoods, so the range
doubles too, from $[-1,2]$ to $[-2,4]$. As a picture, this stretches the density horizontally by a
factor of $2$ — replacing the argument $z$ of the density by $z/2$ is exactly what stretches a
graph by a factor of $2$ (not $2z$, which would compress it). But stretching a curve horizontally
by $2$ without changing its height doubles the area underneath it, and a density's area must stay
at $1$, so the height also has to be halved to compensate. Adding $5$ afterwards shifts every
possible value up by $5$ without changing the shape of the density at all — it slides the whole
graph $5$ units to the right, from $[-2,4]$ to $[3,9]$.

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
height to keep the area at 1; adding 5 then slides the whole graph to the right without changing
its shape, from a range of [-2, 4] to a range of [3, 9].</figcaption>
</figure>

That picture argument is convincing, but the cookbook procedure gives the same answer without
relying on a drawing, and it is worth doing once carefully because the case $a<0$ genuinely differs.
Take $a>0$ first. By definition,
$$
F_Y(y) = \mathbf P(aX+b\le y) = \mathbf P\!\left(X\le \frac{y-b}{a}\right) = F_X\!\left(\frac{y-b}{a}\right),
$$
where dividing by the positive number $a$ leaves the inequality's direction alone. Differentiating
with the chain rule,
$$
f_Y(y) = f_X\!\left(\frac{y-b}{a}\right)\cdot\frac{1}{a}.
$$
Now try $a<0$. The same formula cannot be right, since a density can never be negative while $a$ is.
The step that breaks is dividing the inequality $aX+b\le y$ by $a$: dividing by a *negative* number
reverses the inequality, so
$$
F_Y(y) = \mathbf P\!\left(X\ge \frac{y-b}{a}\right) = 1 - F_X\!\left(\frac{y-b}{a}\right),
$$
and differentiating introduces an extra minus sign that exactly cancels the one already carried by
the negative $a$:
$$
f_Y(y) = -f_X\!\left(\frac{y-b}{a}\right)\cdot\frac{1}{a} = f_X\!\left(\frac{y-b}{a}\right)\cdot\frac{1}{|a|}.
$$
The two cases combine into a single formula that holds for any $a\neq0$:
$$
\boxed{f_Y(y) = \frac{1}{|a|}\,f_X\!\left(\frac{y-b}{a}\right)}, \qquad Y = aX+b.
$$
One consequence, stated without carrying out the algebra here: substituting the normal density for
$f_X$ into this formula shows that $aX+b$ is again normal whenever $X$ is — the calculation that
finally justifies the fact, used earlier in the course without proof, that a linear function of a
normal random variable is itself normal.

## Exercises

The problems below are transcribed from this week's problem set, recitation, and tutorial exactly
as supplied. Several of them (the financial-parable and vote-counting problems, and the Markov
chain problems) belong to the central limit theorem and Markov chain material taught elsewhere in
the course rather than to this lecture's topics; they are included here only because they are
bundled with this lecture's number in the source materials — see Sources below.

### From Problem Set 10

**1. A financial parable.** An investment bank manages \$1 billion, invested in assets related to
the housing market. Because the money is borrowed, the bank's actual capital is only \$50 million
(5%), so a loss of more than 5% makes it insolvent.

(a) The bank considers a single asset whose one-year gain $R$ (in percentage points) is normal
with mean $7$ and standard deviation $10$. What is the probability the bank becomes insolvent?
Would you accept this level of risk?

(b) To diversify, the bank instead invests \$50 million in each of twenty assets, the $i$th having
gain $R_i$, again normal with mean $7$ and standard deviation $10$; the bank's overall gain is
$(R_1+\cdots+R_{20})/20$. The $R_i$ are modelled as independent. What is the probability of
insolvency under this model?

(c) In fact a global economic effect makes the $R_i$ positively correlated: for every $i\neq j$,
$\rho(R_i,R_j)=1/2$. What is the probability of insolvency now? You may assume
$(R_1+\cdots+R_{20})/20$ is normal.

**2.** The adult population of Nowhereville consists of 300 males and 196 females. Each male
(respectively, female) votes independently with probability $0.4$ (respectively, $0.5$). Find a
good numerical approximation for the probability that more males than females vote.

**3.** Let $S_n$ be the number of successes in $n$ independent Bernoulli$(1/2)$ trials. Give a
numerical value for the limit, as $n\to\infty$, of each of the following:

(a) $\mathbf P\!\left(\dfrac{n}{2}-10\le S_n\le \dfrac{n}{2}+10\right)$

(b) $\mathbf P\!\left(\dfrac{n}{2}-\dfrac{n}{10}\le S_n\le \dfrac{n}{2}+\dfrac{n}{10}\right)$

(c) $\mathbf P\!\left(\dfrac{n}{2}-\dfrac{\sqrt n}{2}\le S_n\le \dfrac{n}{2}+\dfrac{\sqrt n}{2}\right)$

**4.** Alice has two coins: the first shows heads with probability $1/3$, the second with
probability $2/3$; otherwise they are indistinguishable. She sends Bob a coin chosen at random,
choosing the first coin with probability $p$. Bob flips the coin he received $3$ times,
independently, and lets $Y$ be the number of heads he observes.

(a) Given that Bob observed $k$ heads, what is the probability he received the first coin?

(b) For which values of $k$ does observing $k$ heads out of 3 tosses *increase* the probability
that Bob received the first coin (compared with the prior $p$)? How does the answer change as $p$
increases?

(c) Help Bob design a decision rule, based on the number of heads $k$ observed in 3 tosses, that
minimises his probability of error.

(d) Take $p=2/3$.
   (i) Find the probability that Bob's rule from (c) guesses correctly.
   (ii) Compare this with the probability of guessing correctly *before* flipping the coin at all.

(e) How does increasing $p$ affect the decision rule from (c)?

(f) For which values of $p$ will Bob's rule never decide "first coin", regardless of the outcome?

(g) For which values of $p$ will Bob's rule always decide "first coin", regardless of the outcome?

**5.** Consider a Bernoulli process $X_1, X_2, X_3, \dots$ with unknown success probability $q$.
As usual let $Y_k$ be the time of the $k$th success and define the inter-arrival times
$T_1=Y_1$, $T_k = Y_k - Y_{k-1}$ for $k\ge2$. This problem studies estimating $q$ from observed
inter-arrival times $t_1, t_2, \dots$.

You may use: for non-negative integers $k,m$, $\displaystyle\int_0^1 q^k(1-q)^m\,dq =
\frac{k!\,m!}{(k+m+1)!}$.

Assume throughout parts (a)–(c) that $q$ is itself the value of a random variable $Q$, uniform on
$[0,1]$.

(a) Find the PMF of $T_1$, $p_{T_1}(t_1)$.

(b) Find the least-squares estimate (LSE) of $Q$ given the single observation $T_1=t_1$.

(c) Find the maximum a posteriori (MAP) estimate of $Q$ given $k$ observations
$T_1=t_1,\dots,T_k=t_k$.

For part (d) only, assume instead that $Q$ is uniform on $[0.5, 1]$.

(d) Find the linear least-squares estimate (LLSE) of the second inter-arrival time $T_2$, based on
the observed first inter-arrival time $T_1=t_1$.

**6.** The joint PDF of $X$ and $Y$ is
$$
f_{X,Y}(x,y) = \begin{cases} c\,x\,y & 0<x\le1,\ 0<y\le1\\ 0 & \text{otherwise.}\end{cases}
$$

(a) Find the normalising constant $c$.

(b) Find the conditional expectation estimator of $X$ based on the observed value $Y=y$.

(c) Is this estimate different from what you would have guessed before observing $Y=y$? Explain.

(d) Repeat (b) and (c) for the MAP estimator.

### From Recitation 10

**Question 1.** For a probabilistic model with sample space $\Omega$, events $A$ and $B$, and a
discrete random variable $X$ (all conditioning below is on events of positive probability): an
identity is *true* if it holds with no further assumptions, and *false* if some counterexample
exists.

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
heads with probability $p$, $0<p<1$. The coin is tossed until either heads has appeared twice (in
which case Heather wins) or tails has appeared twice (in which case Taylor wins). A full game takes
$2$ or $3$ tosses.

2.1 List the outcomes of a full game (as sequences of heads and tails) and their probabilities.

2.2 What is the probability that Heather wins?

2.3 What is the conditional probability that Heather wins given that the first toss is heads?

2.4 What is the conditional probability that the first toss was heads, given that Heather wins?

**Question 3.** A casino offers a game with a fair four-sided die (faces $1,2,3,4$). The **basic
game** involves one or two rolls: if the first roll is $1$, $2$, or $3$, the player wins that many
dollars and the game ends; if the first roll is $4$, the player wins $2 plus the amount of one
further ("bonus") roll. Let $X$ be the payoff of the basic game.

3.1 Find the PMF of $X$, $p_X(x)$.

3.2 Find $\mathbf E[X]$.

3.3 Find the conditional PMF of the result of the first die roll, given that $X=3$. (State clearly
what notation you use.)

3.4 In an **extended game**, any roll of $1$, $2$, or $3$ still wins that amount and ends the game,
but any roll of $4$ wins $2 *and* the game continues with another roll (which may again be a $4$,
and so on indefinitely). Let $Y$ be the payoff of the extended game. Find $\mathbf E[Y]$.

### From Tutorial 10

**1.** Let $X$ be the height, in metres, of a randomly selected Canadian (each Canadian equally
likely to be selected), and write $h=\mathbf E[X]$. Bo, who is confident no Canadian is taller than
$3$ metres, uses $1.5$ metres as a conservative upper bound on the standard deviation of $X$. He
estimates $h$ by averaging the heights of $n$ randomly selected Canadians, calling the result $H$.

(a) In terms of $h$ and Bo's bound of $1.5$, give the expected value and standard deviation of $H$.

(b) Find the minimum $n$ for which the standard deviation of $H$ is guaranteed to be below $0.01$
metres.

(c) Using the Chebyshev inequality, find the minimum $n$ needed for Bo to be $99\%$ sure his
estimate is within $5$ centimetres of the true average height.

(d) Given that no Canadian is taller than three metres, explain why $1.5$ metres is a valid upper
bound on the standard deviation of $X$.

**2.** In any given week of taking 6.041, a student is either up-to-date or behind. If up-to-date
in a given week, she is up-to-date the next week with probability $0.8$ (behind with probability
$0.2$); if behind, she is up-to-date the next week with probability $0.6$ (behind with probability
$0.4$), independent of earlier weeks — a two-state Markov chain with State 1 = up-to-date and
State 2 = behind.

(a) Find the mean first-passage time to State 1, starting from State 2.

(b) Find the mean recurrence time to State 1.

**3.** For a Markov chain with steady-state probabilities
$\pi_1=\tfrac{6}{31}$, $\pi_2=\tfrac{9}{31}$, $\pi_3=\tfrac{6}{31}$, $\pi_4=\tfrac{10}{31}$,
suppose the process is in State 1 just before the first transition.

(a) Find the mean and variance of $K$, the number of transitions up to and including the next
return of the process to State 1.

(b) Find the probability that the state resulting from transition $1000$ differs from both the
state resulting from transition $999$ and the state resulting from transition $1001$.

## Sources

- Lecture 10 transcript, `recordings/lectures/10.md` ("10 captions"), timestamps
  00:00–19:52 for the inference section (recap of joint/conditional PMF-PDF parallel at
  01:02–03:06; the four discrete/continuous combinations of Bayesian inference at 06:25–19:52,
  including the interval-based derivation of the mixed discrete–continuous formula at
  12:04–16:31) and 19:52–47:49 for derived distributions (general two-step method at
  20:56–26:40; the $Y=X^3$ example at 26:40–32:17; the $T=200/V$ example at 32:17–37:57; the
  linear-function formula, by picture and by the CDF method, at 37:57–47:49). The transcript is
  speech over an uncaptured blackboard; the mathematics above — the joint/conditional density
  formulas, the interval argument for the mixed inference case, and both worked derived-distribution
  examples — was reconstructed from what the lecturer describes doing on the board, since no slide
  deck or board image exists for this lecture. The claim that this formalises an earlier,
  unproved assertion that a linear function of a normal random variable is normal is stated at
  47:49 without the supporting algebra being carried out on the board, and is reported here in the
  same unproved form.
- Problem Set 10 (`psets/10-questions.md`), Questions 1–6, transcribed in full. Questions 1–3
  (the financial parable, the Nowhereville vote count, and the limits for $S_n$) concern the
  central limit theorem, not this lecture's material; Questions 4–6 (the two-coin inference
  problem, the Bernoulli-process inter-arrival-time estimation problem, and the joint-density
  conditional/MAP estimator problem) directly exercise this lecture's inference formulas. This
  source page notes it was reconstructed by a model from a PDF with no text layer and that its
  equations are unverified.
- Recitation 10 slides (`recitations/10-slides/01-10-slides-part-01.md` and
  `02-10-slides-part-02.md`), Questions 1–3, transcribed in full; general review material on
  probability identities, conditional probability, and conditional PMFs, not specific to this
  lecture's two topics. Also reconstructed by a model from a PDF with no text layer.
- Tutorial 10 slides (`tutorials/10-slides.md`), Questions 1–3, transcribed in full; concerns
  Chebyshev's inequality and Markov chains, taught elsewhere in the course. Also reconstructed by
  a model from a PDF with no text layer, and Question 3 refers to a Markov chain diagram that is
  not reproduced in the converted text.

---

[← 9. Joint and Conditional Continuous Densities](09-joint-and-conditional-continuous-densities.md) · [Contents](index.md) · [11. Derived Distributions, Convolutions, and Covariance →](11-derived-distributions-convolutions-and-covariance.md)
