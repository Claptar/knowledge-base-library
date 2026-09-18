---
title: "6. Conditional Expectation and Joint PMFs"
course: "MIT 6.041SC"
chapter: 6
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 6. Conditional Expectation and Joint PMFs

## What this covers

The previous lecture defined a random variable as a function from outcomes to numbers, and
introduced its probability mass function (PMF) and expectation. This chapter asks two questions
that follow immediately: *what happens to expectation once you're given partial information about
the experiment*, and *what do you do once there are two random variables in play, not one*. It
assumes the PMF, expectation and variance of a single random variable, and ordinary conditional
probability, are already familiar.

## Review: PMF, expectation, variance

For a discrete random variable $X$,

$$p_X(x) = \mathbf{P}(X = x), \qquad \mathbf{E}[X] = \sum_x x\,p_X(x), \qquad \mathbf{E}[g(X)] = \sum_x g(x)\,p_X(x).$$

Expectation is linear — $\mathbf{E}[\alpha X + \beta] = \alpha \mathbf{E}[X] + \beta$ — but that is a
special property of *linear* functions, not a general fact about expectation. In general
$\mathbf{E}[g(X)] \ne g(\mathbf{E}[X])$, and this failure is worth taking seriously before doing
anything else, because conditioning and joint distributions are both places where the temptation
to "reason on the average" reappears.

Variance measures the typical squared distance from the mean:

$$\text{var}(X) = \mathbf{E}\big[(X - \mathbf{E}[X])^2\big] = \mathbf{E}[X^2] - (\mathbf{E}[X])^2, \qquad \sigma_X = \sqrt{\text{var}(X)}.$$

(Note that $\mathbf{E}[X - \mathbf{E}[X]] = 0$ always — the signed distance from the mean averages
out, which is exactly why the *squared* distance, not the signed one, is the useful quantity.)

## A worked warning: you cannot reason on the average

Here is the example the lecture used to make the failure of $\mathbf{E}[g(X)]=g(\mathbf{E}[X])$
concrete, because it is easy to believe the equation is "morally true" until you compute both
sides.

You travel 200 miles at a constant but random speed $V$: with probability $1/2$ you go at $1$ mph,
and with probability $1/2$ you go at $200$ mph (a coin flip decides which). Then

$$\mathbf{E}[V] = \tfrac12(1) + \tfrac12(200) = 100.5, \qquad \text{var}(V) = \tfrac12(1-100.5)^2 + \tfrac12(200-100.5)^2 = 99.5^2 = 9900.25,$$

so $\sigma_V = 99.5$ — the two possible speeds sit almost symmetrically, about $100$ on either
side of the mean, and the standard deviation says so directly, unlike the variance which is in
mph².

Now let $T = 200/V$ be the travel time. $T$ is a function of $V$, so it is itself a random
variable, and its PMF comes for free: $V=1 \Rightarrow T=200$, and $V=200 \Rightarrow T=1$, each
with probability $1/2$. So

$$\mathbf{E}[T] = \tfrac12(200) + \tfrac12(1) = 100.5.$$

Three things are worth stopping on:

- $\mathbf{E}[T] \ne 200/\mathbf{E}[V]$: the right-hand side is $200/100.5 \approx 1.99$, nowhere
  near $100.5$. $T$ is a *nonlinear* function of $V$ ($1/V$), so pushing the expectation inside
  fails.
- $\mathbf{E}[TV] \ne \mathbf{E}[T]\,\mathbf{E}[V]$: in every single outcome, $T \cdot V = 200$
  exactly (it's the distance), so $\mathbf{E}[TV] = 200$. But $\mathbf{E}[T]\mathbf{E}[V] =
  100.5^2 \approx 10100$. The product of the averages is not the average of the product.
- Over many repeated trips, your average speed is about $100$ and your average time is about
  $100$ — but your average *distance* is not $100 \times 100$. It is $200$, always. Averaging and
  multiplying do not commute.

The moral: whenever a quantity is built nonlinearly from a random variable — a product, a
reciprocal, a square — you must go back to the definition of expectation and actually sum over
outcomes. There is no shortcut through "the average of the pieces."

## Conditional PMF and conditional expectation

Chapter 1 already has conditional probability: someone tells you an event $A$ has occurred, and
you revise your probabilities using it. Nothing changes when the object being assigned
probabilities is a random variable's numerical value rather than a bare event — you just get new
notation for an old idea:

$$p_{X\mid A}(x) = \mathbf{P}(X = x \mid A), \qquad \mathbf{E}[X \mid A] = \sum_x x\,p_{X\mid A}(x).$$

**Example.** Let $X$ be uniform on $\{1,2,3,4\}$, each value with probability $1/4$, and let
$A = \{X \ge 2\}$. Conditioning on $A$ removes the outcome $X=1$ and rescales what's left: the
three remaining values were equally likely before, so they stay equally likely, just renormalized
to sum to 1:

$$p_{X\mid A}(x) = \tfrac13 \text{ for } x = 2,3,4, \qquad \mathbf{E}[X\mid A] = \tfrac13(2+3+4) = 3.$$

That renormalize-but-keep-the-relative-shape move is the single idea underneath every conditional
PMF in this chapter — it will reappear, unchanged, when we condition the geometric PMF and again
when we slice a joint PMF.

The general point, worth internalizing rather than memorizing formula by formula: **a conditional
PMF is an ordinary PMF, just for a different (smaller) universe.** Every rule that holds for
ordinary probabilities and expectations therefore has a conditional counterpart, obtained by
writing $\mathbf{P}(\cdot \mid A)$ everywhere you had $\mathbf{P}(\cdot)$, and $\mathbf{E}[\cdot \mid A]$
everywhere you had $\mathbf{E}[\cdot]$ — for instance $\mathbf{E}[\alpha X + \beta \mid A] = \alpha\mathbf{E}[X\mid A] + \beta$,
because linearity of expectation didn't depend on which universe you were computing it in. There
is no separate formula to learn.

## The geometric distribution and its memoryless property

$X$ is the number of independent coin tosses, each landing heads with probability $p$, until the
first head appears:

$$p_X(k) = (1-p)^{k-1} p, \qquad k = 1, 2, 3, \dots$$

Now ask: given that the first two tosses were tails (i.e. given $X > 2$), what does the *remaining*
wait look like? Intuitively — and this is the argument, not just the algebra — coin tosses are
independent, so the two wasted tails carry no information about what comes next. It would be the
gambler's fallacy to think "two tails in a row, so a head is due." Formally: a person who has
already thrown two tails and is about to keep flipping faces exactly the same probabilistic
situation as someone starting fresh right now. So the remaining number of flips, $X - 2$, given
$X>2$, should have *the same* geometric PMF as $X$ itself:

$$p_{X-2 \mid X>2}(k) = p_X(k), \qquad k = 1,2,3,\dots$$

This is the **memoryless property** of the geometric distribution: past failures are forgotten.

The formal check is exactly the renormalize-but-keep-shape move from the previous section, run
twice. Conditioning on $X>2$ throws away $k=1,2$ and rescales the tail by $\mathbf{P}(X>2) =
(1-p)^2$:

$$p_{X\mid X>2}(k) = \frac{p_X(k)}{(1-p)^2} = (1-p)^{k-3}p, \qquad k=3,4,5,\dots$$

— which is just $p_X(k)$ shifted two steps to the right, not merely similar in shape but
*numerically identical*, since $(1-p)^{k-3}p = p_X(k-2)$. Re-indexing by $X-2$ then slides those
values back onto $k=1,2,3,\dots$, recovering $p_X$ exactly.

<figure>
<svg viewBox="0 0 520 210" role="img" aria-label="Bar chart comparing the geometric PMF to its conditional version given X greater than 2">
  <line x1="10" y1="175" x2="470" y2="175" stroke="currentColor" stroke-width="1.5"/>

  <rect x="140" y="12" width="14" height="10" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <text x="160" y="21" font-size="12" fill="currentColor">P(X = k)</text>
  <rect x="270" y="12" width="14" height="10" fill="orangered" fill-opacity="0.3" stroke="orangered"/>
  <text x="290" y="21" font-size="12" fill="currentColor">P(X = k | X &#62; 2)</text>

  <rect x="22" y="55" width="14" height="120" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="102" y="103" width="14" height="72" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="182" y="131.8" width="14" height="43.2" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="262" y="149.08" width="14" height="25.92" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="342" y="159.45" width="14" height="15.55" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="422" y="165.67" width="14" height="9.33" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>

  <rect x="204" y="55" width="14" height="120" fill="orangered" fill-opacity="0.3" stroke="orangered"/>
  <rect x="284" y="103" width="14" height="72" fill="orangered" fill-opacity="0.3" stroke="orangered"/>
  <rect x="364" y="131.8" width="14" height="43.2" fill="orangered" fill-opacity="0.3" stroke="orangered"/>
  <rect x="444" y="149.08" width="14" height="25.92" fill="orangered" fill-opacity="0.3" stroke="orangered"/>

  <line x1="36" y1="55" x2="204" y2="55" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="116" y1="103" x2="284" y2="103" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>

  <text x="40" y="190" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="120" y="190" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="200" y="190" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <text x="280" y="190" text-anchor="middle" font-size="12" fill="currentColor">4</text>
  <text x="360" y="190" text-anchor="middle" font-size="12" fill="currentColor">5</text>
  <text x="440" y="190" text-anchor="middle" font-size="12" fill="currentColor">6</text>
  <text x="490" y="190" text-anchor="middle" font-size="12" fill="currentColor">k</text>
</svg>
<figcaption>The geometric PMF (outline bars) decays as $p(1-p)^{k-1}$. Conditioning on $X>2$
discards $k=1,2$ and rescales the tail so it sums to 1 (filled bars) — and read from $k=3$ onward,
that rescaled tail has exactly the heights of the original PMF read from $k=1$ (dashed lines mark
equal heights, two steps apart). Nothing about the future depends on the two wasted tosses.</figcaption>
</figure>

The same argument works for conditioning on $X>n$ for any $n$, not only $n=2$ — the next section
uses the case $n=1$.

## Total expectation theorem

Recall the total probability theorem: if $A_1,\dots,A_n$ partition the sample space,

$$\mathbf{P}(B) = \mathbf{P}(A_1)\mathbf{P}(B\mid A_1) + \dots + \mathbf{P}(A_n)\mathbf{P}(B\mid A_n).$$

Apply this with $B = \{X=x\}$ and you get exactly the same statement written for a PMF instead of
a single event:

$$p_X(x) = \mathbf{P}(A_1)\,p_{X\mid A_1}(x) + \dots + \mathbf{P}(A_n)\,p_{X\mid A_n}(x).$$

Nothing new so far — it's the same fact in new notation. Now multiply both sides by $x$ and sum
over all $x$. The left side becomes $\mathbf{E}[X]$; on the right, $\sum_x x\, p_{X\mid A_i}(x)$ is
by definition $\mathbf{E}[X \mid A_i]$. That gives the **total expectation theorem**:

$$\mathbf{E}[X] = \mathbf{P}(A_1)\,\mathbf{E}[X\mid A_1] + \dots + \mathbf{P}(A_n)\,\mathbf{E}[X\mid A_n].$$

This is a genuine divide-and-conquer tool: split the sample space into cases, find the expectation
of $X$ *within* each case, then combine with weights equal to the probabilities of the cases.

**Finding $\mathbf{E}[X]$ for the geometric distribution, without summing the series.** The direct
route is $\mathbf{E}[X] = \sum_{k=1}^\infty k(1-p)^{k-1}p$, an infinite sum that needs an algebraic
trick to close. The total expectation theorem gives a shortcut that uses the memoryless property
instead. Split on the outcome of the first toss: $A_1 = \{X=1\}$ (first toss heads, probability
$p$) and $A_2 = \{X>1\}$ (first toss tails, probability $1-p$).

- $\mathbf{E}[X \mid X=1] = 1$ — if you're told $X=1$, $X$ is no longer random, it's just the
  number 1.
- $\mathbf{E}[X \mid X>1]$: write $X = (X-1) + 1$. Given $X>1$, the quantity $X-1$ is exactly "the
  number of further tosses until the first head, given the first toss was tails" — which, by
  memorylessness, has the *same* distribution as $X$ itself. So $\mathbf{E}[X-1\mid X>1] =
  \mathbf{E}[X]$, and therefore $\mathbf{E}[X\mid X>1] = \mathbf{E}[X] + 1$.

Substituting into the total expectation theorem:

$$\mathbf{E}[X] = p(1) + (1-p)\big(\mathbf{E}[X]+1\big) = p + (1-p)\mathbf{E}[X] + (1-p).$$

The only unknown here is $\mathbf{E}[X]$ itself, and the equation is linear in it:

$$\mathbf{E}[X] - (1-p)\mathbf{E}[X] = p + (1-p) = 1 \quad\Longrightarrow\quad p\,\mathbf{E}[X] = 1 \quad\Longrightarrow\quad \mathbf{E}[X] = \frac{1}{p}.$$

This matches intuition: if heads are rare ($p$ small), you expect to wait a long time.

## Joint PMFs of two random variables

A single PMF for $X$ and a single PMF for $Y$ say nothing about how $X$ and $Y$ relate to each
other — two students each have a height and a weight, and the individual distributions of height
and of weight say nothing about whether tall students also tend to be heavier. That relationship
lives in the **joint PMF**:

$$p_{X,Y}(x,y) = \mathbf{P}(X=x \text{ and } Y=y).$$

It is an ordinary probability of an ordinary (intersection) event, just indexed by a pair of
numbers instead of one. All the entries are nonnegative and sum to 1 over every $(x,y)$ pair.

**Example.** The following table gives $p_{X,Y}(x,y)$, entries out of 20ths, for $X,Y \in
\{1,2,3,4\}$ (blank cells are 0):

| $y \backslash x$ | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: |
| **4** | | 1/20 | 2/20 | 2/20 |
| **3** | 2/20 | 4/20 | 1/20 | 2/20 |
| **2** | | 1/20 | 3/20 | 1/20 |
| **1** | | | 1/20 | |

(Every entry is nonnegative and the twenty entries sum to $20/20=1$, as they must.)

**Marginal PMF.** If you only care about $X$, sum the joint PMF over all values of $Y$ — collapse
each column of the table:

$$p_X(x) = \sum_y p_{X,Y}(x,y).$$

Reading down the $x=3$ column of the table above: $p_X(3) = \frac{2}{20}+\frac1{20}+\frac3{20}+\frac1{20} = \frac{7}{20}$.
Knowing the joint PMF always lets you recover each individual ("marginal") PMF this way; the
converse is false — the two marginals alone cannot tell you the joint PMF, which is exactly why
the joint PMF carries strictly more information about the relationship between $X$ and $Y$.

**Conditional PMF.** Fixing $Y=y$ and asking about the distribution of $X$ *within that slice* is
ordinary conditioning, applied to the row $Y=y$ of the table:

$$p_{X\mid Y}(x \mid y) = \mathbf{P}(X=x \mid Y=y) = \frac{p_{X,Y}(x,y)}{p_Y(y)}.$$

Take $y=2$: the row reads $0, \tfrac1{20}, \tfrac3{20}, \tfrac1{20}$ for $x=1,2,3,4$, so
$p_Y(2) = \tfrac{5}{20} = \tfrac14$, and

$$p_{X\mid Y}(x\mid 2) = 0, \ \tfrac15, \ \tfrac35, \ \tfrac15 \quad \text{for } x=1,2,3,4.$$

This is the same renormalize-but-keep-the-shape operation as before: the row's numbers, $0,1,3,1$,
keep exactly the same proportions, just scaled up so they sum to 1 instead of $1/4$. Whatever you
condition on — an event, as with the geometric distribution, or the value of another random
variable, as here — a conditional PMF is a slice of the picture, rescaled, and it must sum to 1
regardless of what produced it.

## Exercises

The lecture itself stays with discrete joint PMFs. Problem Set 6 already reaches ahead to
continuous joint densities and to covariance — ideas the following lectures introduce — while the
recitation problems stay within what this chapter covers; both are reproduced below as the week's
assigned exercises.

**From the recitation.**

1. A fair four-sided die, with faces labeled $0,1,2,3$, is thrown once to determine how many times
   a fair coin is then flipped. Let $N$ be the die result and $K$ the total number of heads
   obtained in the $N$ flips.
   - (a) Find and sketch $p_N(n)$.
   - (b) Find and tabulate the joint PMF $p_{N,K}(n,k)$.
   - (c) Find and sketch the conditional PMF $p_{K\mid N}(k \mid 2)$.
   - (d) Find and sketch the conditional PMF $p_{N\mid K}(n \mid 2)$.

2. Eight equally likely outcomes, each with probability $1/8$, sit at the points $(1,1)$, $(1,3)$,
   $(3,1)$, $(3,2)$, $(4,0)$, $(4,1)$, $(4,2)$, $(4,3)$ in the $(x,y)$-plane.
   - (a) Which value(s) of $x$ maximize $\mathbf{E}[Y \mid X=x]$?
   - (b) Which value(s) of $y$ maximize $\text{var}(X \mid Y=y)$?
   - (c) Let $R = \min(X,Y)$. Sketch $p_R(r)$, fully labeled.
   - (d) Let $A$ be the event $X^2 \ge Y$. Find $\mathbf{E}[XY]$ and $\mathbf{E}[XY \mid A]$.

3. (Bertsekas & Tsitsiklis, Example 2.17.) You run a piece of software repeatedly; each attempt
   succeeds with probability $p$, independently of previous attempts. Let $X$ be the number of
   attempts until it first works. Find $\text{var}(X)$.

**From Problem Set 6.**

1. $X,Y$ have joint PDF $f_{X,Y}(x,y) = ax$ for $1 \le x \le 2$, $0 \le y \le x$, and $0$ otherwise.
   - (a) Find $a$.
   - (b) Find the marginal PDF $f_Y(y)$.
   - (c) Find $\mathbf{E}[1/X \mid Y = 3/2]$.
   - (d) With $Z = Y - X$, find the PDF $f_Z(z)$.

2. Independent $X, Y$ have $f_X(x) = \tfrac34(1-x^2)$ for $-1 \le x \le 1$, and $f_Y(y) = \tfrac13$
   for $0 \le y \le 1$, $\tfrac23$ for $2 \le y \le 3$, and $0$ otherwise. With $Z = X+Y$, find
   $f_Z(z)$.

3. $n$ independent tosses of a fair $k$-sided die; let $X_i$ be the number of tosses landing on
   face $i$.
   - (a) Are $X_1$ and $X_2$ uncorrelated, positively correlated, or negatively correlated? Give a
     one-line justification.
   - (b) Compute $\text{cov}(X_1, X_2)$.

4. $X,Y$ have joint PDF equal to the constant $0.1$ on a step-shaped region of the plane (wider,
   $-2 \le y \le 2$, for $-1 \le x \le 0$; narrower for $0 \le x \le 2$, as shown in the original
   figure), and $0$ elsewhere.
   - (a) Find the conditional PDFs $f_{Y\mid X}(y\mid x)$ and $f_{X\mid Y}(x\mid y)$.
   - (b) Find $\mathbf{E}[X \mid Y=y]$, $\mathbf{E}[X]$, and $\text{var}(X\mid Y=y)$; use these to
     find $\text{var}(X)$.
   - (c) Find $\mathbf{E}[Y \mid X=x]$, $\mathbf{E}[Y]$, and $\text{var}(Y\mid X=x)$; use these to
     find $\text{var}(Y)$.

5. The wombat club has $N$ members, where $N$ has PMF $p_N(n) = p^{n-1}(1-p)$ for
   $n=1,2,3,\dots$. On the second Tuesday of every month, each wombat independently attends the
   club meeting with probability $q$; every attendee brings an amount of money $M$ with PDF
   $f_M(m) = \lambda e^{-\lambda m}$ for $m \ge 0$. $N$, $M$, and attendance are all independent.
   - (a) Find the expectation and variance of the number of wombats who show up.
   - (b) Find the expectation and variance of the total money brought to the meeting.

G1$^\dagger$. (a) Let $X_1,\dots,X_n,X_{n+1},\dots,X_{2n}$ be i.i.d. Find
   $\mathbf{E}[X_1 \mid X_1+\dots+X_n = x_0]$ for a constant $x_0$.
   (b) With $S_k = X_1+\dots+X_k$ for $1\le k\le 2n$, find
   $\mathbf{E}[X_1 \mid S_n=s_n, S_{n+1}=s_{n+1},\dots,S_{2n}=s_{2n}]$ for constants
   $s_n,\dots,s_{2n}$.

   $^\dagger$Required for 6.431; optional for 6.041.

## Sources

- **Slides:** `lectures/06-slides.md` (Lecture 6) — review of PMF/expectation/variance; the
  random-speed example; conditional PMF and expectation; geometric PMF and memorylessness; total
  expectation theorem; joint PMF table. Readings given as Sections 2.4–2.6 of the course text
  (Bertsekas & Tsitsiklis, *Introduction to Probability*, not itself supplied).
- **Transcript:** `recordings/lectures/06.md` — the reasoning behind every derivation above:
  review and the speed/time example (00:00–17:13), conditional PMF and the "new universe" framing
  (17:13–23:55), the two-flippers story motivating memorylessness and its formal check
  (24:56–33:55), the total expectation theorem and the divide-and-conquer derivation of
  $\mathbf{E}[X]=1/p$ (33:55–40:37), and joint/marginal/conditional PMFs with the worked table
  (41:50–50:29). Boilerplate (funding notice) cut.
- **Exercises:** recitation `recitations/06-slides.md` (problems 1–3, including Example 2.17
  attributed to Bertsekas & Tsitsiklis via Athena Scientific) and problem set
  `psets/06-questions/01-06-questions-part-01.md` and `02-06-questions-part-02.md` (problems 1–5
  and G1). The recitation's second problem reconstructs a point-diagram from the original PDF;
  coordinates are a best-effort reading of that figure.
- Not supplied: the course textbook itself (Bertsekas & Tsitsiklis, *Introduction to Probability*),
  referenced by both the slides' reading list and the recitation's problem attribution.

---

[← 5. Random Variables, PMFs, and Expectation](05-random-variables-pmfs-and-expectation.md) · [Contents](index.md) · [7. Multiple Random Variables and Independence →](07-multiple-random-variables-and-independence.md)
