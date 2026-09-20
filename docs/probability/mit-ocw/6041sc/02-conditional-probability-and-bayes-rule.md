---
title: "2. Conditional Probability and Bayes' Rule"
course: "MIT 6.041SC"
chapter: 2
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 2. Conditional Probability and Bayes' Rule

## What this covers

Once a probability model is set up — a sample space, events, and a law obeying the axioms —
the natural next question is: what happens to that law when you learn a little more about the
outcome? This chapter defines **conditional probability** and develops the three tools built on
it that the rest of the course leans on: the **multiplication rule**, the **total probability
theorem**, and **Bayes' rule**. Together they are "divide and conquer" methods — ways of breaking
a hard probability calculation into easy pieces, and, in the case of Bayes' rule, of running that
breakdown backwards to infer a cause from an observed effect. The chapter assumes the material of
the previous lecture: sample space, event, and the axioms of a probability law.

## Recap: sample space, events, and the axioms

A probability model has three ingredients:

- a **sample space** $\Omega$ — the list of possible outcomes of the experiment, chosen to be
  mutually exclusive, collectively exhaustive, and at the right level of detail;
- **events** — subsets of $\Omega$;
- a **probability law**, assigning a number $\mathbf{P}(A)$ to every event $A$, subject to
  1. $\mathbf{P}(A) \geq 0$,
  2. $\mathbf{P}(\Omega) = 1$,
  3. if $A \cap B = \emptyset$ then $\mathbf{P}(A \cup B) = \mathbf{P}(A) + \mathbf{P}(B)$, and,
     more generally, for a *sequence* of disjoint events $A_1, A_2, \dots$,
     $$\mathbf{P}(A_1 \cup A_2 \cup \cdots) = \mathbf{P}(A_1) + \mathbf{P}(A_2) + \cdots.$$

Once the model is in place, solving a problem is usually a matter of specifying the sample space,
writing down the probability law, identifying the event of interest, and calculating.

### Aside: why the axiom says "sequence"

It is worth pausing on the word *sequence* in axiom 3′, because skipping past it lets you prove
something false. Take $\Omega$ to be the unit square, with $\mathbf{P}$ of a region equal to its
area — the model used for two independent numbers drawn uniformly from $[0,1]$. Every single point
$\{(x,y)\}$ has probability zero, since a point has zero area. The whole square is the union of all
of its points. If axiom 3′ applied to that union, it would give
$$\mathbf{P}(\Omega) = \sum_{(x,y)} \mathbf{P}(\{(x,y)\}) = \sum_{(x,y)} 0 = 0,$$
contradicting $\mathbf{P}(\Omega) = 1$. Either probability theory is broken, or the derivation has
a mistake — and the mistake is real. Axiom 3′ applies only to a *sequence* $A_1, A_2, \dots$: a
countable union. The unit square cannot be built by listing its points in a sequence and taking
their union, because it has strictly more points than there are integers — it is *uncountable*.
So the axiom simply does not apply to this union, and there is no contradiction; the calculation
that "proved" $1=0$ used a tool outside its stated range.

The moral carries forward into every continuous model used later in the course: an individual
outcome typically has probability zero, and yet the experiment produces one anyway. **Zero
probability does not mean impossible** — only "vanishingly unlikely" — and symmetrically,
probability one does not mean *certain*: in the unit-square model, $\mathbf{P}\big((X,Y) \neq
(0,0)\big) = 1$, yet $(0,0)$ remains a possible outcome. The bumper-sticker version: expect the
unexpected.

## Conditional probability

You know something about the world, and on that basis you set up a probability model — a law over
$\Omega$ describing what you consider likely and unlikely. Then someone hands you a piece of
information: not the full outcome, only that it lies in some event $B$. That should change your
beliefs, and the revised probabilities are called **conditional probabilities**, written
$\mathbf{P}(A \mid B)$: the probability that $A$ occurs, given that $B$ is known to have occurred.

**Definition.** For events $A$ and $B$ with $\mathbf{P}(B) \neq 0$,
$$\mathbf{P}(A \mid B) = \frac{\mathbf{P}(A \cap B)}{\mathbf{P}(B)}.$$
If $\mathbf{P}(B) = 0$, $\mathbf{P}(A \mid B)$ is left undefined — there is nothing to divide by.

Once you are told $B$ occurred, $B$ effectively becomes the new sample space: you are certain the
outcome lies in $B$, so $\mathbf{P}(B \mid B) = 1$, and probability inside $B$ is redistributed in
the same relative proportions it had before.

**A numeric example.** Suppose $\Omega$ is split into three pieces: outside $B$ entirely, an
overlap $A \cap B$, and the rest of $B$ outside $A$, with original probabilities $3/6$, $2/6$, and
$1/6$ respectively.

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A sample space split into three regions, showing how conditioning on B rescales the two pieces inside it while keeping their ratio.">
  <rect x="20" y="20" width="300" height="160" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="30" y="35" font-size="12" fill="currentColor">&#937;</text>
  <ellipse cx="190" cy="100" rx="110" ry="70" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-width="1.5"/>
  <text x="225" y="40" font-size="12" text-anchor="end" fill="currentColor">B</text>
  <line x1="230" y1="34" x2="230" y2="166" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="96" font-size="12" text-anchor="middle" fill="currentColor">A ∩ B</text>
  <text x="160" y="112" font-size="12" text-anchor="middle" fill="currentColor">2/6</text>
  <text x="270" y="96" font-size="12" text-anchor="middle" fill="currentColor">B \ A</text>
  <text x="270" y="112" font-size="12" text-anchor="middle" fill="currentColor">1/6</text>
  <text x="55" y="96" font-size="12" text-anchor="middle" fill="currentColor">Ω \ B</text>
  <text x="55" y="112" font-size="12" text-anchor="middle" fill="currentColor">3/6</text>
</svg>
<figcaption>The region B splits into A ∩ B (twice as likely) and B \ A. Conditioning on B rescales
2/6 and 1/6 to 2/3 and 1/3, preserving their 2-to-1 ratio.</figcaption>
</figure>

Originally $\mathbf{P}(B) = 2/6 + 1/6 = 3/6$. Told that $B$ occurred, the piece $A \cap B$ was
twice as likely as the piece $B \setminus A$ before the news arrived, so the two pieces should stay
in a 2-to-1 ratio afterward — giving $2/3$ and $1/3$. The definition agrees:
$$\mathbf{P}(A \mid B) = \frac{\mathbf{P}(A \cap B)}{\mathbf{P}(B)} = \frac{2/6}{3/6} = \frac{2}{3}.$$

Turning the definition around gives the **multiplication form**,
$$\mathbf{P}(A \cap B) = \mathbf{P}(B)\,\mathbf{P}(A \mid B) = \mathbf{P}(A)\,\mathbf{P}(B \mid A),$$
which has a frequency reading: run the experiment many times; among the trials on which $B$
happens, the fraction on which $A$ *also* happens is $\mathbf{P}(A \mid B)$.

**Conditional probabilities are still probabilities.** Fix $B$ with $\mathbf{P}(B) \neq 0$. Then
$\mathbf{P}(\cdot \mid B)$, viewed as a function of the first argument, satisfies all the same
axioms as an ordinary probability law: it is non-negative, $\mathbf{P}(B \mid B) = 1$, and it is
additive over events that are disjoint (as subsets of $B$). It does not taste or smell any
different from an ordinary probability law — it is just the law that applies in the new universe
where $B$ is known to have happened.

### Example: two rolls of a die, conditioned

Recall the earlier example of two independent rolls of a die, each pair of outcomes equally
likely. The specific numbers in this example only work out if the die has four faces: sixteen
equally likely pairs, each with probability $1/16$. Let $B$ be the event $\min(X,Y) = 2$, and let
$M = \max(X, Y)$.

<figure>
<svg viewBox="0 0 300 300" role="img" aria-label="A 4 by 4 grid of dice outcomes with the five points of min(X,Y)=2 filled in, and the one point also satisfying max(X,Y)=2 ringed.">
  <line x1="40" y1="20" x2="40" y2="260" stroke="currentColor" stroke-width="1"/>
  <line x1="100" y1="20" x2="100" y2="260" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="20" x2="160" y2="260" stroke="currentColor" stroke-width="1"/>
  <line x1="220" y1="20" x2="220" y2="260" stroke="currentColor" stroke-width="1"/>
  <line x1="280" y1="20" x2="280" y2="260" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="20" x2="280" y2="20" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="80" x2="280" y2="80" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="140" x2="280" y2="140" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="200" x2="280" y2="200" stroke="currentColor" stroke-width="1"/>
  <line x1="40" y1="260" x2="280" y2="260" stroke="currentColor" stroke-width="1"/>
  <circle cx="70" cy="230" r="4" fill="none" stroke="currentColor"/>
  <circle cx="130" cy="230" r="4" fill="none" stroke="currentColor"/>
  <circle cx="190" cy="230" r="4" fill="none" stroke="currentColor"/>
  <circle cx="250" cy="230" r="4" fill="none" stroke="currentColor"/>
  <circle cx="70" cy="170" r="4" fill="none" stroke="currentColor"/>
  <circle cx="190" cy="170" r="4" fill="none" stroke="currentColor"/>
  <circle cx="250" cy="170" r="4" fill="none" stroke="currentColor"/>
  <circle cx="70" cy="110" r="4" fill="none" stroke="currentColor"/>
  <circle cx="70" cy="50" r="4" fill="none" stroke="currentColor"/>
  <circle cx="130" cy="170" r="6" fill="currentColor"/>
  <circle cx="130" cy="110" r="6" fill="currentColor"/>
  <circle cx="130" cy="50" r="6" fill="currentColor"/>
  <circle cx="190" cy="170" r="6" fill="currentColor"/>
  <circle cx="250" cy="170" r="6" fill="currentColor"/>
  <circle cx="130" cy="170" r="10" fill="none" stroke="#d9480f" stroke-width="2"/>
  <text x="70" y="278" font-size="12" text-anchor="middle" fill="currentColor">1</text>
  <text x="130" y="278" font-size="12" text-anchor="middle" fill="currentColor">2</text>
  <text x="190" y="278" font-size="12" text-anchor="middle" fill="currentColor">3</text>
  <text x="250" y="278" font-size="12" text-anchor="middle" fill="currentColor">4</text>
  <text x="160" y="295" font-size="12" text-anchor="middle" fill="currentColor">X</text>
  <text x="28" y="234" font-size="12" text-anchor="middle" fill="currentColor">1</text>
  <text x="28" y="174" font-size="12" text-anchor="middle" fill="currentColor">2</text>
  <text x="28" y="114" font-size="12" text-anchor="middle" fill="currentColor">3</text>
  <text x="28" y="54" font-size="12" text-anchor="middle" fill="currentColor">4</text>
  <text x="14" y="140" font-size="12" text-anchor="middle" fill="currentColor">Y</text>
</svg>
<figcaption>The five filled points are B: min(X,Y) = 2. The ringed point (2,2) is the only one of
those five where the maximum is also 2, giving P(M = 2 | B) = 1/5.</figcaption>
</figure>

Since $B$ requires both rolls to be at least 2, $M$ cannot equal 1 once $B$ has occurred, so
$\mathbf{P}(M = 1 \mid B) = 0$ outright. For $\mathbf{P}(M = 2 \mid B)$, the intersection of $B$
with $\{M = 2\}$ is the single point $(2,2)$, so
$$\mathbf{P}(M = 2 \mid B) = \frac{\mathbf{P}(M=2, B)}{\mathbf{P}(B)} = \frac{1/16}{5/16} = \frac15.$$
There is a shortcut that gets the same answer without ever writing down the definition: all five
outcomes in $B$ were equally likely before the news arrived, so — since conditioning only rescales
probabilities inside $B$, keeping their ratios fixed — they remain equally likely afterward. So
each one, including $(2,2)$, simply gets probability $1/5$. **More generally, conditioning a
uniform distribution on an event produces a new uniform distribution on that event.**

## Building a model from conditional probabilities: the radar example

So far, conditional probabilities have been *computed* from an existing law. They can also be used
to *build* a law in the first place — often the natural way a model is specified, since the pieces
of information available are themselves conditional statements.

Suppose event $A$ is "a plane is flying in a particular sector of sky you are watching", and from
experience you know $\mathbf{P}(A) = 0.05$ (so $\mathbf{P}(A^c) = 0.95$). You have a radar; event
$B$ is "the radar registers a blip." The manufacturer's specification tells you, conditionally: if
a plane is there, the radar detects it with probability $0.99$ and misses it with probability
$0.01$; if no plane is there, the radar false-alarms with probability $0.10$ and stays quiet,
correctly, with probability $0.90$. Each of these is a self-contained probability model *given*
that the corresponding scenario holds — a piece of a larger model built entirely from conditional
probabilities.

<figure>
<svg viewBox="0 0 480 260" role="img" aria-label="A tree diagram for the radar example: a branch for plane or no plane, each splitting into detect or not, with probabilities multiplied along each path.">
  <circle cx="30" cy="130" r="3" fill="currentColor"/>
  <line x1="30" y1="130" x2="170" y2="60" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="130" x2="170" y2="200" stroke="currentColor" stroke-width="1.5"/>
  <text x="90" y="85" font-size="12" fill="currentColor">0.05</text>
  <text x="90" y="185" font-size="12" fill="currentColor">0.95</text>
  <circle cx="170" cy="60" r="3" fill="currentColor"/>
  <circle cx="170" cy="200" r="3" fill="currentColor"/>
  <text x="175" y="48" font-size="12" fill="currentColor">A: plane</text>
  <text x="175" y="222" font-size="12" fill="currentColor">Aᶜ: no plane</text>
  <line x1="170" y1="60" x2="340" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <line x1="170" y1="60" x2="340" y2="90" stroke="currentColor" stroke-width="1.5"/>
  <line x1="170" y1="200" x2="340" y2="170" stroke="currentColor" stroke-width="1.5"/>
  <line x1="170" y1="200" x2="340" y2="230" stroke="currentColor" stroke-width="1.5"/>
  <text x="240" y="38" font-size="12" fill="currentColor">0.99</text>
  <text x="240" y="88" font-size="12" fill="currentColor">0.01</text>
  <text x="240" y="178" font-size="12" fill="currentColor">0.10</text>
  <text x="240" y="228" font-size="12" fill="currentColor">0.90</text>
  <text x="348" y="33" font-size="12" fill="currentColor">B: 0.0495</text>
  <text x="348" y="93" font-size="12" fill="currentColor">Bᶜ: 0.0005</text>
  <text x="348" y="173" font-size="12" fill="currentColor">B: 0.0950</text>
  <text x="348" y="233" font-size="12" fill="currentColor">Bᶜ: 0.8550</text>
</svg>
<figcaption>Multiplying along a branch gives the probability of that leaf: P(A ∩ B) = P(A)P(B∣A) =
0.05 × 0.99 = 0.0495, and similarly for the other three leaves.</figcaption>
</figure>

Multiplying along the branches gives the probability of each leaf, e.g.
$\mathbf{P}(A \cap B) = \mathbf{P}(A)\,\mathbf{P}(B \mid A) = 0.05 \times 0.99 = 0.0495$. Adding
the two leaves where the radar registers something gives the overall chance it does so at all:
$$\mathbf{P}(B) = \mathbf{P}(A \cap B) + \mathbf{P}(A^c \cap B) = 0.0495 + 0.95\times0.10 = 0.1445.$$
Now the interesting question: *given* that the radar registered something, how likely is it that a
plane is really there?
$$\mathbf{P}(A \mid B) = \frac{\mathbf{P}(A \cap B)}{\mathbf{P}(B)} = \frac{0.0495}{0.1445} \approx 0.34.$$
This is worth sitting with: the radar's specifications look good — it catches a real plane 99% of
the time and stays quiet 90% of the time when there is nothing there — and yet, told only that it
registered something, there is barely a one-in-three chance a plane is actually there. The reason
is that false alarms are common relative to true detections: a false alarm occurs with probability
around $0.10$, while a true detection occurs with probability around $0.05$, so a blip is *more
likely* to be a false alarm than a real plane. The same reasoning applies to a medical test for a
rare disease: a test can be quite accurate and still be more often wrong than right about any
individual positive result, once the disease is rare enough in the population being tested.

## Abstracting the three tools

The radar example did three calculations in sequence — multiply along a branch, add branches to
get a total, then invert to compute $\mathbf{P}(A\mid B)$ from $\mathbf{P}(B\mid A)$ — and each of
those calculations is itself a general, reusable tool.

### The multiplication rule

For three events,
$$\mathbf{P}(A \cap B \cap C) = \mathbf{P}(A)\,\mathbf{P}(B \mid A)\,\mathbf{P}(C \mid A \cap B),$$
and the same idea extends to any number of events: given a tree in which, at each stage, some
event either happens or does not, and you are told the conditional probability of each branch
given everything that happened on the way there, the probability of any leaf is the product of the
probabilities along the path to it. The proof is just the definition of conditional probability,
applied twice: write $\mathbf{P}(A \cap B \cap C)$ as $\mathbf{P}\big((A\cap B) \cap C\big)$, apply
the definition to peel off $\mathbf{P}(C \mid A \cap B)$, then apply it again to
$\mathbf{P}(A \cap B)$ itself. Nothing stops this from continuing to four, five, or more events —
$$\mathbf{P}(A_1 \cap \cdots \cap A_n) = \mathbf{P}(A_1)\,\mathbf{P}(A_2 \mid A_1)\,\mathbf{P}(A_3 \mid A_1 \cap A_2)\cdots \mathbf{P}(A_n \mid A_1 \cap \cdots \cap A_{n-1}).$$
In frequency terms: of the trials on which $A_1$ happens, some fraction also have $A_2$ happen;
of *those*, some fraction also have $A_3$ happen; and multiplying the fractions together gives the
fraction of all trials on which everything happens.

### The total probability theorem

Suppose $A_1, A_2, A_3$ partition the sample space — mutually exclusive scenarios that cover every
possibility — and you know $\mathbf{P}(B \mid A_i)$ for each $i$. Then $B$ happens in exactly one
of three mutually exclusive ways, $B \cap A_1$, $B \cap A_2$, or $B \cap A_3$, so by additivity and
the multiplication rule,
$$\mathbf{P}(B) = \mathbf{P}(A_1)\mathbf{P}(B \mid A_1) + \mathbf{P}(A_2)\mathbf{P}(B \mid A_2) + \mathbf{P}(A_3)\mathbf{P}(B \mid A_3).$$
This is "divide and conquer": break $B$ up by scenario, solve the easy conditional problem in each
scenario, and recombine, weighting each scenario's contribution by how likely that scenario is —
since $\sum_i \mathbf{P}(A_i) = 1$, this is a weighted average of $\mathbf{P}(B \mid A_i)$ across
the scenarios. If the scenarios happen to be equally likely, it reduces to a plain average. The
argument does not depend on there being only three scenarios or even finitely many — it works for
any partition, finite or countably infinite.

### Bayes' rule

The last step reverses the order of conditioning. You start with **prior probabilities**
$\mathbf{P}(A_i)$ — initial beliefs about which scenario holds — and a causal model
$\mathbf{P}(B \mid A_i)$ telling you, for each scenario, how likely the observation $B$ is. Having
then observed $B$, you want the **posterior**: the revised belief $\mathbf{P}(A_i \mid B)$ about
which scenario actually holds. Two applications of the definition of conditional probability, plus
the total probability theorem to handle the denominator, give
$$\mathbf{P}(A_i \mid B) = \frac{\mathbf{P}(A_i \cap B)}{\mathbf{P}(B)} = \frac{\mathbf{P}(A_i)\mathbf{P}(B \mid A_i)}{\sum_j \mathbf{P}(A_j)\mathbf{P}(B \mid A_j)}.$$
In the radar example this is exactly the calculation that turned $\mathbf{P}(A) = 0.05$ into
$\mathbf{P}(A \mid B) \approx 0.34$: a model of *cause producing effect* — a plane may or may not
cause a blip — run backwards to answer a question about *effect implying cause* — given the blip,
how likely is the plane? This reversal is the basic move behind almost any inference from partial
data: a scenario, or parameter, or hypothesis produces observations with some probability, and
Bayes' rule turns an observation into a revised belief about the scenario that produced it. The
rule is named for Thomas Bayes, a British theologian working in the 1700s, and the underlying
question — whether there is a systematic way to update beliefs in light of new evidence — was a
live philosophical problem of his time, not just a computational trick.

## Exercises

**From Problem Set 2.**

1. Most mornings, Victor checks the weather forecast before deciding whether to carry an umbrella.
   If the forecast says "rain," the probability that it actually rains that day is 80%; if the
   forecast says "no rain," the probability it actually rains is 10%. During fall and winter the
   forecast says "rain" 70% of the time; during summer and spring it says "rain" 20% of the time.
   1. One day Victor missed the forecast, and it rained. What is the probability that the forecast
      had said "rain," given that it was winter? Given that it was summer?
   2. Victor misses the forecast with probability 0.2 on any day of the year, independent of
      season. When he misses it, he flips a fair coin to decide whether to carry an umbrella. On
      any day he does see the forecast, he carries an umbrella exactly when the forecast says
      "rain." Are the events "Victor is carrying an umbrella" and "the forecast said no rain"
      independent? Does the answer depend on the season?
   3. Victor is carrying an umbrella and it is not raining. What is the probability that he saw
      the forecast that day? Does it depend on the season?

2. A fair five-sided die, with faces numbered 1 through 5, is rolled twice, independently.
   1. Let $A$ be "the total of the two rolls is 10," $B$ be "at least one roll is a 5," and $C$ be
      "at least one roll is a 1." Is $A$ independent of $B$? Is $A$ independent of $C$?
   2. Let $D$ be "the total of the two rolls is 7," $E$ be "the two rolls differ by exactly 1,"
      and $F$ be "the second roll is higher than the first." Are $E$ and $F$ independent? Are they
      independent given $D$?

3. A widget factory has 500 old widgets and 1500 new widgets in stock for a sale; 15% of the old
   widgets are defective and 5% of the new ones are defective. Widgets are chosen at random from
   the relevant stock when an order comes in, and you are the first customer.
   1. You flip a fair coin to decide whether to order old or new widgets, then order two widgets
      of that type. What is the probability both are defective?
   2. Given that both widgets turn out to be defective, what is the probability they were old?

4. Oscar has lost his dog in forest $A$ (prior probability 0.4) or forest $B$ (prior probability
   0.6); the dog cannot move between forests. If the dog is in $A$ and Oscar spends a day searching
   there, he finds it that day with probability 0.25; if the dog is in $B$ and he searches there,
   he finds it with probability 0.15. Oscar can search only during the day and can travel between
   forests only at night.
   1. Which forest should Oscar search first, to maximize the chance of finding the dog on day 1?
   2. Given that Oscar searched $A$ on day 1 and did not find the dog, what is the probability the
      dog is in $A$?
   3. If instead Oscar flips a fair coin to choose where to search on day 1, and he finds the dog
      that day, what is the probability he had searched $A$?
   4. If the dog is alive but unfound by the end of day $N$, it dies that night with probability
      $N/(N+2)$. Oscar plans to search $A$ on both of the first two days. What is the probability
      that he finds a live dog for the first time on day 2?

**From Recitation 2.**

5. A coin is tossed twice. Alice claims that the event "both tosses are heads" is at least as
   likely conditioned on "the first toss is a head" as it is conditioned on "at least one toss is
   a head." Is she right? Does it matter whether the coin is fair? How would you state Alice's
   reasoning in general?

6. Two fair six-sided dice are rolled; all 36 outcomes are equally likely.
   1. Find the probability that doubles are rolled.
   2. Given that the sum of the two rolls is 4 or less, find the conditional probability of
      doubles.
   3. Find the probability that at least one die shows a 6.
   4. Given that the two dice show different numbers, find the conditional probability that at
      least one die shows a 6.

7. In a chess tournament, your probability of winning a game is 0.3 against half the field (type 1
   opponents), 0.4 against a quarter of the field (type 2), and 0.5 against the remaining quarter
   (type 3). You play one game against a randomly chosen opponent.
   1. What is your probability of winning?
   2. Given that you won, what is the probability your opponent was type 1?

8. **The Monty Hall problem.** A prize is equally likely to be behind any of three closed doors.
   You point to one door. A friend, who knows where the prize is, opens one of the other two doors
   and reveals that it does not have the prize. You may then stick with your original door or
   switch to the remaining unopened one. Compare these three strategies and determine which gives
   the best chance of winning:
   1. Always stick with the original choice.
   2. Always switch to the other unopened door.
   3. Point to door 1 first; if door 2 is then opened, do not switch; if door 3 is opened, switch.

## Sources

- **Slides**: `lectures/02-slides.md` — the outline (review, conditional probability, multiplication
  rule, total probability theorem, Bayes' rule), the definition of conditional probability, the
  fill-in-the-blank die-roll and radar exercises, and the boxed formulas for the multiplication
  rule, total probability theorem, and Bayes' rule.
- **Transcript**: `recordings/lectures/02.md` — all worked reasoning and running commentary: the
  axioms recap (00:00–04:36), the unit-square "$1=0$" paradox and its resolution via countable vs.
  uncountable unions (04:36–11:01), the motivation for conditional probability and the 3/6-2/6-1/6
  numeric example (12:06–17:57), the die-roll conditioning example (20:03–24:32), the full radar
  worked example including the 0.34 posterior and the false-alarm / medical-test discussion
  (24:32–33:28), the general tree argument and proof of the multiplication rule (33:28–37:45), the
  general total probability argument including the equal-likelihood special case and the note that
  it holds for infinite partitions (37:45–44:58), the derivation and cause/effect framing of Bayes'
  rule, and the closing remark on Thomas Bayes (44:58–end).
- **Exercises**: `psets/02-questions.md` (Problem Set 2, problems 1–4) and `recitations/02-slides.md`
  (Recitation 2, textbook problems 1.14, 1.15, the chess example, and the Monty Hall problem).
  Problem 5 and the optional chess-tournament problem (G1) from Problem Set 2 are about
  independence and infinite sequential sample spaces rather than this lecture's tools, and are
  left for the chapter where independence is introduced.
- **Not used**: the Quiz 2 materials (`exams/02-exam.md`, `exams/02-exam-quiz02-f09/`,
  `exams/02-exam-quiz02-s08/`, `exams/02-exam-quiz02-revi.md`), Tutorial 2
  (`tutorials/02-slides.md`, `tutorials/02-slides-tut02.md`), and the two worked-example recordings
  (`recordings/worked-examples/inferring-a-parameter-of-uniform-part-2.md` and
  `recordings/worked-examples/the-difference-of-2-independent-exponential-random-variables.md`) were
  supplied for this lecture but cover material from much later in the course — continuous random
  variables, joint and conditional PDFs, convolution, and Bayesian point estimation — and are not
  part of Lecture 2's content. The lecture's stated readings, Sections 1.3–1.4 of the course
  textbook, were not supplied and are not used here.

---

[← 1. Sample Spaces and the Axioms of Probability](01-sample-spaces-and-the-axioms-of-probability.md) · [Contents](index.md) · [3. Independence of Events →](03-independence-of-events.md)
