---
title: "5. Random Variables, PMFs, and Expectation"
course: "MIT 6.041SC"
chapter: 5
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 5. Random Variables, PMFs, and Expectation

## What this covers

This chapter opens the study of random variables, the central object for the rest of the course.
It answers three questions: what a random variable is, formally; how its possible values and their
likelihoods are recorded by a probability mass function (PMF); and how a random variable is
summarized by a single typical value (its expectation) and a measure of how spread out it is (its
variance). It builds directly on the sample-space, event and counting machinery of the earlier
lectures — in particular the coin-tossing and binomial-coefficient counting argument — and treats
only the discrete case; continuous random variables are taken up in a later lecture.

## Random variables

A **random variable** is a function from the sample space $\Omega$ to the real numbers. It assigns
a number to every possible outcome of an experiment. That is the whole definition — despite the
name, a random variable is neither random nor a variable in the algebraic sense; it is an ordinary
function, and all the randomness lives in *which* outcome $\omega \in \Omega$ occurs.

Standard notation keeps the function and its values apart: a capital letter such as $X$ denotes the
random variable — the function itself — and the corresponding lowercase letter $x$ denotes a
particular numerical value it can take. Concretely: pick a random student from the class (the
sample space $\Omega$) and measure their height $H$ in inches. $H$ is the function; a specific
student's height, say $60$ or $71$, is a value $h$ that $H$ takes. It helps to think of $H$ as a
subroutine: it takes a student as input, puts them on a scale, and returns a number as output. Fix
a student and the number is fixed; before that, all you have is the function.

A single experiment can carry several random variables at once. The same random student also has a
weight, so weight $W$ is a second function on the same $\Omega$ — unrelated in form to $H$, but
defined on the same underlying outcomes.

A function of a random variable is again a random variable. If $\bar H = cH$ converts height in
inches to height in centimeters, for some fixed conversion constant $c$, then $\bar H$ is itself a
function $\Omega \to \mathbb{R}$: once the outcome (the student) is fixed, $H$ is determined, and so
is $\bar H$. This point recurs constantly through the course: for any real function $g$, $g(X)$ is
a new random variable on the same sample space.

Random variables can be **discrete** (finitely or countably many possible values — height rounded
to the nearest inch) or **continuous** (a continuum of possible values — height measured with
unlimited precision). The course covers discrete random variables first, because the ideas are the
same but the bookkeeping is simpler, and returns to continuous random variables later once the
concepts here — PMF, expectation, variance — are secure.

## The probability mass function

The **probability mass function** (PMF) of a discrete random variable $X$ — also called its
probability law or probability distribution — records how likely each value is:

$$p_X(x) = P(X = x) = P\big(\{\omega \in \Omega : X(\omega) = x\}\big).$$

That is, $p_X(x)$ is the total probability of all outcomes that make $X$ equal to $x$. Two
properties follow immediately from the probability axioms:

$$p_X(x) \ge 0 \ \text{ for every } x, \qquad \sum_x p_X(x) = 1,$$

the second because every outcome maps to *some* value of $x$, and the events $\{X = x\}$ for
different $x$ partition $\Omega$.

**Computing a PMF** is always the same three-step procedure: for each candidate value $x$, collect
every outcome $\omega$ with $X(\omega) = x$, add up their probabilities, and repeat for every $x$.

### Example: the geometric PMF

Flip a coin, independently, with $P(H) = p > 0$ on each toss, until the first head appears, and let
$X$ be the toss number on which that first head occurs. The event $\{X = k\}$ happens in exactly
one way: the first $k - 1$ tosses are tails and the $k$-th is heads. By independence,

$$p_X(k) = P(\underbrace{TT\cdots T}_{k-1}H) = (1-p)^{k-1}p, \qquad k = 1, 2, \dots$$

This is the **geometric PMF**. Plotted as a bar graph it starts at $p$ when $k = 1$, and each
successive bar is smaller than the last by a factor of $1-p$ — the shape of a geometric sequence,
hence the name, and $X$ is called a geometric random variable. This case was easy because only one
outcome produced each value of $X$; in general many outcomes share a value, and all of their
probabilities must be added together.

### Example: the minimum of two die rolls

Roll a fair tetrahedral die (faces $1$–$4$) twice, independently. Let $F$ and $S$ be the first and
second roll — themselves random variables — and let $X = \min(F, S)$. There are $16$ equally likely
outcomes $(F, S)$, each with probability $1/16$. To find $p_X(2)$, collect every outcome where the
*smaller* of the two rolls is $2$:

<figure>
<svg viewBox="0 0 300 260" role="img" aria-label="Grid of the 16 equally likely outcomes for two tetrahedral die rolls, with the five outcomes where the minimum equals 2 shaded">
  <line x1="60" y1="20" x2="60" y2="220" stroke="currentColor" stroke-width="1"/>
  <line x1="110" y1="20" x2="110" y2="220" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="20" x2="160" y2="220" stroke="currentColor" stroke-width="1"/>
  <line x1="210" y1="20" x2="210" y2="220" stroke="currentColor" stroke-width="1"/>
  <line x1="260" y1="20" x2="260" y2="220" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="20" x2="260" y2="20" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="70" x2="260" y2="70" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="120" x2="260" y2="120" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="170" x2="260" y2="170" stroke="currentColor" stroke-width="1"/>
  <line x1="60" y1="220" x2="260" y2="220" stroke="currentColor" stroke-width="1"/>
  <rect x="110" y="20" width="50" height="50" fill="currentColor" fill-opacity="0.15"/>
  <rect x="110" y="70" width="50" height="50" fill="currentColor" fill-opacity="0.15"/>
  <rect x="110" y="120" width="50" height="50" fill="currentColor" fill-opacity="0.15"/>
  <rect x="160" y="120" width="50" height="50" fill="currentColor" fill-opacity="0.15"/>
  <rect x="210" y="120" width="50" height="50" fill="currentColor" fill-opacity="0.15"/>
  <text x="85" y="240" text-anchor="middle" font-size="12" fill="currentColor">F=1</text>
  <text x="135" y="240" text-anchor="middle" font-size="12" fill="currentColor">F=2</text>
  <text x="185" y="240" text-anchor="middle" font-size="12" fill="currentColor">F=3</text>
  <text x="235" y="240" text-anchor="middle" font-size="12" fill="currentColor">F=4</text>
  <text x="45" y="49" text-anchor="end" font-size="12" fill="currentColor">S=4</text>
  <text x="45" y="99" text-anchor="end" font-size="12" fill="currentColor">S=3</text>
  <text x="45" y="149" text-anchor="end" font-size="12" fill="currentColor">S=2</text>
  <text x="45" y="199" text-anchor="end" font-size="12" fill="currentColor">S=1</text>
  <text x="160" y="256" text-anchor="middle" font-size="11" fill="currentColor">each of the 16 cells has probability 1/16</text>
</svg>
<figcaption>The 16 equally likely outcomes of two independent tetrahedral die rolls. The five shaded
cells are exactly the outcomes where $\min(F,S)=2$, so $p_X(2) = 5/16$.</figcaption>
</figure>

There are five such outcomes — $(2,2), (2,3), (2,4), (3,2), (4,2)$ — so

$$p_X(2) = \frac{5}{16}.$$

The rest of the PMF, $p_X(1)$, $p_X(3)$, $p_X(4)$, is found the same way.

### Example: the binomial PMF

Toss a coin $n$ times, independently, with $P(H) = p$ on each toss, and let $X$ be the total number
of heads — the same counting problem as an earlier lecture, now written in PMF notation. For
$n = 4$, the event $\{X = 2\}$ is the union of the six equally-probable arrangements of two heads
and two tails ($HHTT, HTHT, HTTH, THHT, THTH, TTHH$), each with probability $p^2(1-p)^2$, so

$$p_X(2) = 6\,p^2(1-p)^2 = \binom{4}{2}p^2(1-p)^2.$$

The $6$ is exactly $\binom{4}{2}$, the number of ways to place $2$ heads among $4$ tosses, and in
general

$$p_X(k) = \binom{n}{k}p^k(1-p)^{n-k}, \qquad k = 0, 1, \dots, n.$$

This is the **binomial PMF**. Plotted for large $n$, it takes on a bell-shaped curve concentrated
around the middle values of $k$, with very few heads or very many heads both unlikely — a first
glimpse of a fact (the emergence of that bell shape) the course proves properly much later; for now
it is only worth noticing.

## Expectation

The **expectation** (or expected value, or mean) of a discrete random variable is

$$E[X] = \sum_x x\, p_X(x).$$

There are two useful ways to read this number. First, as a long-run average: if probabilities are
interpreted as the frequencies with which values occur over many independent repetitions of the
experiment, $E[X]$ is the average payoff per repetition. Second, and often faster for a quick
answer, as a **center of gravity**: place a mass $p_X(x)$ at position $x$ on the real line; $E[X]$
is the point where this system of masses balances.

<figure>
<svg viewBox="0 0 320 150" role="img" aria-label="Expectation as a center of gravity: point masses at 1, 2 and 4 dollars, weighted by their probabilities, balance at 2.5">
  <line x1="40" y1="90" x2="300" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="88" cy="90" r="10" fill="currentColor" fill-opacity="0.3"/>
  <circle cx="136" cy="90" r="16" fill="currentColor" fill-opacity="0.3"/>
  <circle cx="232" cy="90" r="13" fill="currentColor" fill-opacity="0.3"/>
  <text x="88" y="65" text-anchor="middle" font-size="12" fill="currentColor">$1, p=1/6</text>
  <text x="136" y="55" text-anchor="middle" font-size="12" fill="currentColor">$2, p=1/2</text>
  <text x="232" y="60" text-anchor="middle" font-size="12" fill="currentColor">$4, p=1/3</text>
  <line x1="160" y1="90" x2="160" y2="115" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="150,130 170,130 160,115" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="145" text-anchor="middle" font-size="12" fill="currentColor">E[X] = 2.5</text>
</svg>
<figcaption>The expectation is the point where the probability-weighted values balance, exactly like
the center of gravity of masses $1/6$, $1/2$ and $1/3$ placed at $1$, $2$ and $4$.</figcaption>
</figure>

For example, suppose a game pays $\$1$ with probability $1/6$, $\$2$ with probability $1/2$, and
$\$4$ with probability $1/3$. Then

$$E[X] = 1\cdot\frac16 + 2\cdot\frac12 + 4\cdot\frac13 = 2.5,$$

matching the point where the diagram above balances.

The center-of-gravity picture also gives quick answers by symmetry. Let $X$ be uniform on
$\{0, 1, \dots, n\}$, i.e. $p_X(x) = 1/(n+1)$ for each of these $n+1$ values. Rather than summing
$\sum_{k=0}^n k/(n+1)$ term by term, notice the PMF is symmetric about the midpoint of its range,
so the balance point — the expectation — must be that midpoint:

$$E[X] = \frac{n}{2}.$$

Whenever a PMF is symmetric about some point, that point is the expectation, with no calculation
needed.

## The expected value rule

Often what is wanted is not $E[X]$ itself but $E[Y]$ for some $Y = g(X)$ derived from it — say
$Y = X^2$, or a payoff that is some function of the number of heads. One route is the *hard* way:
find the PMF of $Y$ first, by grouping outcomes according to the value of $y$ they produce, then
apply the definition,

$$E[Y] = \sum_y y\, p_Y(y).$$

The *easy* way skips finding $p_Y$ entirely:

$$E[g(X)] = \sum_x g(x)\, p_X(x).$$

Both formulas add up exactly the same quantity — the probability of each outcome times the payoff
it produces — and differ only in how the terms are grouped: the first groups outcomes by the value
of $y$ they share before multiplying by $y$; the second runs over values of $x$ directly,
multiplying the probability of each $x$ by $g(x)$ without first bundling together outcomes that
happen to produce the same $y$. Because it feels so natural, this fact is often assumed to hold "by
definition" — it does not; it is a genuine claim that needs a proof (one of the exercises below),
which is why it carries a name: the **law of the unconscious statistician**. It is the single
most-used shortcut for computing expectations of derived quantities, because it lets you work
entirely with the PMF of $X$ you already have, never with the PMF of $Y$.

**A caution worth stating before using the rule at all**: in general,

$$E[g(X)] \ne g(E[X]).$$

Averaging and applying a function do not commute, and the course will produce many examples where
they disagree. The one broad exception is when $g$ is *linear*. For constants $\alpha, \beta$:

$$E[\alpha] = \alpha, \qquad E[\alpha X] = \alpha E[X], \qquad E[\alpha X + \beta] = \alpha E[X] + \beta.$$

The first says that a "random variable" which always equals $\alpha$ — a degenerate case with no
actual randomness — has expectation $\alpha$: the only term in the sum is $\alpha$ itself, with
probability $1$. The second follows from the expected value rule applied to $g(x) = \alpha x$:

$$E[\alpha X] = \sum_x (\alpha x)\, p_X(x) = \alpha \sum_x x\, p_X(x) = \alpha E[X],$$

and combining the two gives the third. Concretely: if $H$ is height in inches and $\bar H = cH$ is
height in centimeters, then $E[\bar H] = c\, E[H]$ — converting every student's height by the same
factor converts the average height by the same factor, exactly as intuition demands. This is the
one case where "reasoning on the average" is legitimate; the general caution above is the rule, and
linearity is the exception.

## Variance

Two more expectations are worth naming. The **second moment** of $X$ is
$E[X^2] = \sum_x x^2\, p_X(x)$, an instance of the expected value rule with $g(x) = x^2$. More
useful is the expectation of the *squared distance from the mean*,

$$\operatorname{var}(X) = E\big[(X - E[X])^2\big] = \sum_x (x - E[X])^2\, p_X(x),$$

called the **variance** of $X$. The quantity $(X - E[X])^2$ inside the outer expectation is itself
a random variable — a number is subtracted from $X$, and the result is squared — so this too is
just an application of the expected value rule, now to $g(x) = (x - E[X])^2$. Variance measures how
spread out the PMF is around its mean, with the squaring giving extra weight to values far from the
mean: a small variance means outcomes cluster tightly around $E[X]$; a large variance means the
bars of the PMF reach far to either side.

A shortcut formula, easier to compute with, is

$$\operatorname{var}(X) = E[X^2] - (E[X])^2$$

(its short derivation is one of the exercises below). Two basic properties:

$$\operatorname{var}(X) \ge 0$$

— immediate, since it is an average of non-negative quantities (squares) — and

$$\operatorname{var}(\alpha X + \beta) = \alpha^2 \operatorname{var}(X).$$

The plausibility of the second is worth seeing even before deriving it formally. Adding a constant
$\beta$ shifts every value of $X$, but it shifts the mean by exactly the same amount, so the
*distance* of any value from the mean — and hence the spread — is unchanged:
$\operatorname{var}(X + \beta) = \operatorname{var}(X)$. Multiplying by $\alpha$ instead stretches
both the values and the mean by $\alpha$, so a deviation that was $x - E[X]$ becomes
$\alpha(x - E[X])$; squaring that deviation multiplies it by $\alpha^2$, which is where the square
on $\alpha$ comes from. Combining the two: scaling by $\alpha$ and shifting by $\beta$ multiplies
the variance by $\alpha^2$, and the shift has no effect on it at all.

## Exercises

These are Recitation 5's problems, which work with exactly the material above.

1. (a) Derive the expected value rule (the law of the unconscious statistician): for $Y = g(X)$,
   show that $E[Y] = \sum_x g(x)\, p_X(x)$.
   (b) For $Y = aX + b$ with constants $a, b$, derive $E[Y] = aE[X] + b$ and
   $\operatorname{var}(Y) = a^2 \operatorname{var}(X)$.
   (c) Derive the shortcut formula $\operatorname{var}(X) = E[X^2] - (E[X])^2$.

2. A marksman takes $10$ shots at a target, hitting with probability $0.2$ on each shot,
   independently of all other shots. Let $X$ be the number of hits.
   (a) Find and sketch the PMF of $X$.
   (b) What is the probability that he scores no hits?
   (c) What is the probability that he scores more hits than misses?
   (d) Find $E[X]$ and $\operatorname{var}(X)$.
   (e) He must pay $\$3$ to enter the range and receives $\$2$ for every hit. Let $Y$ be his net
   profit. Find $E[Y]$ and $\operatorname{var}(Y)$.
   (f) Instead, suppose entry is free and his profit equals the *square* of his number of hits,
   $Z = X^2$. Find $E[Z]$.

3. Four buses carry $40$, $33$, $25$ and $50$ job-seeking students, respectively ($148$ students in
   total), to a job convention. One of the $148$ students is chosen at random; let $X$ be the
   number of students on that student's bus. Separately, one of the four bus drivers is chosen at
   random; let $Y$ be the number of students on that driver's bus.
   (a) Before calculating anything: which of $E[X]$ and $E[Y]$ do you expect to be larger? Explain
   your reasoning.
   (b) Compute $E[X]$ and $E[Y]$.

4. **St. Petersburg paradox.** You toss a fair coin repeatedly and independently until it first
   comes up tails. If the first tails occurs on toss $n$, you are paid $2^n$ dollars. What is the
   expected amount you receive? How much would you actually be willing to pay to play this game
   once? (Recitation 5's accompanying handout simulates this game over 20 and 200 plays; the
   running average behaves very differently from the usual law-of-large-numbers picture, which is
   worth keeping in mind while answering the second question.)

## Sources

- **Lecture 5 slides** (`lectures/05-slides.md`): the definition of a random variable, the PMF and
  its two defining properties, the geometric-PMF example, the tetrahedral-die-minimum table, the
  binomial PMF, the definition of expectation, the properties of expectation, and the definition
  and properties of variance. This file is a model reconstruction of a PDF with no text layer, so
  every displayed equation should be treated as unverified against the original slide.
- **Lecture 5 transcript** (`recordings/lectures/05.md`), by caption timestamp: random variables as
  functions, the height/weight example and the height-to-centimeters example ($00{:}00$–$11{:}04$);
  the PMF and the geometric-PMF derivation ($11{:}04$–$17{:}51$); the tetrahedral-die-minimum
  example ($17{:}51$–$20{:}00$); the binomial-PMF recap and the aside on the bell-shaped limiting
  curve ($21{:}02$–$24{:}20$); expectation, the frequency and center-of-gravity interpretations,
  the $\$1/\$2/\$4$ payoff example, and the uniform-symmetry argument ($24{:}20$–$30{:}59$); the
  expected value rule and the law of the unconscious statistician ($30{:}59$–$37{:}44$); linearity
  of expectation and the height-in-centimeters derivation ($37{:}44$–$42{:}24$); and variance, its
  shortcut formula, and the shift/scale argument for its properties ($42{:}24$–$50{:}15$).
- **Exercises**: Recitation 5 slides (`recitations/05-slides.md`, dated September 23, 2010),
  Problems 1–4, and the accompanying extra handout's simulation note for Problem 4.
- **Not used**: Problem Set 5 (`psets/05-questions/`, parts 01–03) and Tutorial 5
  (`tutorials/05-slides.md`) both work with continuous random variables and joint PDFs — material
  this lecture does not reach — so none of their problems are reproduced above.
- **Referred to but not contained here**: the lecturer points forward to the emergence of a
  bell-shaped (normal) curve for the binomial PMF at large $n$, promising a proof "in a couple of
  months"; that result is not covered in this lecture and is not reproduced beyond the observation
  itself.

---

[← 4. Counting Methods and Binomial Probabilities](04-counting-methods-and-binomial-probabilities.md) · [Contents](index.md) · [6. Conditional Expectation and Joint PMFs →](06-conditional-expectation-and-joint-pmfs.md)
