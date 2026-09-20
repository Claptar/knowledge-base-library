---
title: "1. Sample Spaces and the Axioms of Probability"
course: "MIT 6.041SC"
chapter: 1
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 1. Sample Spaces and the Axioms of Probability

## What this covers

A random experiment needs two things before you can say anything quantitative about it: a
description of everything that could happen, and a rule for how likely each possibility is. This
chapter builds both pieces from scratch — the **sample space** and the **probability law** — and
states the three **axioms** that any probability law must obey, together with the first few facts
that follow from them. It assumes only familiarity with sets (unions, intersections, complements)
and covers the reading in Bertsekas & Tsitsiklis §1.1–1.2.

## Setting up a sample space

The sample space $\Omega$ of an experiment is the list — formally, the set — of all possible
outcomes. "Experiment" is used loosely: it just means something happens, with an uncertain result.
Two requirements on the list are non-negotiable:

- **Collectively exhaustive**: whatever happens, it is one of the outcomes listed. Nothing has been
  left out.
- **Mutually exclusive**: at the end of the experiment you can point to exactly one outcome and say
  "this is what happened." No two listed outcomes can happen together.

Beyond that, there is real freedom, and choosing well is described as an art rather than a
calculation. Take flipping a coin once. $\Omega = \{H, T\}$ is the obvious choice. But
$\{H,\ \text{T and raining},\ \text{T and not raining}\}$ is also mutually exclusive and
collectively exhaustive, and so is a perfectly legitimate sample space for the same experiment. It
is just not a *useful* one, unless you have some superstitious reason to think the weather affects
your coin. Every model of a real situation drops some details as irrelevant and keeps others; which
ones to keep is judgment, not mathematics.

**A discrete example.** Roll a four-sided (tetrahedral) die twice. This is *one* experiment with two
stages, not two repetitions of a smaller experiment. An outcome is the pair of results, e.g. "a two
followed by a three," written $(2,3)$. This is different from $(3,2)$: even though the two would be
indistinguishable in backgammon, a model that wants to track everything that can happen has to keep
them apart. The word "result" is reserved here for what happens at one stage; "outcome" is reserved
for the pair that describes the whole experiment. $\Omega$ has $4\times 4 = 16$ elements. The same
sample space can be pictured two ways: as a $4\times 4$ grid of pairs, or as a tree that branches
four ways at the first stage and, from each of those branches, four ways again at the second — a
path from root to leaf is one outcome, and there are 16 leaves, matching the 16 grid cells.

**A continuous example.** Throw a dart at a square target, landing uniformly inside it — you're
skilled enough never to miss the square, but you don't control exactly where inside it the dart
lands. An outcome is a pair of real numbers $(x,y)$ with $0 \le x, y \le 1$, so
$\Omega = \{(x,y) \mid 0 \le x,y \le 1\}$ is infinite (in fact uncountable).

## From outcomes to events: why probability lives on sets

Before writing down rules for assigning likelihoods, it helps to see why those likelihoods are
attached to *sets* of outcomes rather than to individual outcomes. Go back to the dart: what should
the probability be that the dart lands at one exact point, to infinite precision? Intuitively, zero
— and the same is true of any single point in a reasonable model of that experiment. Telling you
that every individual outcome has probability zero gives you nothing to work with. So instead,
probabilities are assigned to subsets of $\Omega$, called **events**. If $A \subseteq \Omega$ is an
event, the outcome that actually occurs either lands inside $A$ — in which case $A$ *occurred* — or
outside it, in which case $A$ *did not occur*.

## The axioms of probability

A probability law assigns a number $\mathbf{P}(A)$ to every event $A$, meant to capture how likely
$A$ is relative to other events. There is more than one legitimate way to do this for a given
sample space, but every legitimate way has to satisfy three consistency requirements, the **axioms
of probability**:

1. **Nonnegativity.** $\mathbf{P}(A) \ge 0$ for every event $A$.
2. **Normalization.** $\mathbf{P}(\Omega) = 1$. This is certainty: since $\Omega$ is collectively
   exhaustive, the actual outcome is guaranteed to land in it.
3. **Additivity.** If $A \cap B = \varnothing$ (the events are disjoint — they share no outcomes),
   then
   $$\mathbf{P}(A \cup B) = \mathbf{P}(A) + \mathbf{P}(B).$$

A useful picture for additivity: think of total probability as one pound of cream cheese spread
over $\Omega$. $\mathbf{P}(A)$ is how much sits on top of $A$; if $A$ and $B$ don't overlap, the
cream cheese on $A \cup B$ is just the cream cheese on $A$ plus the cream cheese on $B$. Probability
behaves like mass.

There is no explicit axiom saying $\mathbf{P}(A) \le 1$ — not because it isn't true, but because it
follows from the three above, and axiom-writers don't state what they don't have to.

**A first consequence.** Since $A$ and its complement $A^c$ partition $\Omega$ (they are disjoint
and their union is $\Omega$),
$$1 = \mathbf{P}(\Omega) = \mathbf{P}(A \cup A^c) = \mathbf{P}(A) + \mathbf{P}(A^c) \ge \mathbf{P}(A),$$
using normalization, then additivity (axiom 3, since $A, A^c$ are disjoint), then nonnegativity
(axiom 1, applied to $\mathbf{P}(A^c)$). So $\mathbf{P}(A) \le 1$ for every event $A$ — a short
argument, but one that genuinely uses all three axioms.

## Extending additivity beyond two sets

Axiom 3 is stated for two disjoint events, but three-way (and $n$-way) disjoint unions come up
constantly. The extension is by a short induction, not a fourth axiom. For three pairwise disjoint
events $A, B, C$:
$$\mathbf{P}(A \cup B \cup C) = \mathbf{P}\big((A \cup B) \cup C\big)
= \mathbf{P}(A \cup B) + \mathbf{P}(C) = \mathbf{P}(A) + \mathbf{P}(B) + \mathbf{P}(C),$$
where the middle step uses additivity on $A \cup B$ and $C$ (disjoint, since $A, B, C$ are), and the
last step uses additivity again on $A$ and $B$. The same trick handles any finite number of
pairwise disjoint sets: if $A_1, \dots, A_n$ are pairwise disjoint,
$$\mathbf{P}(A_1 \cup \cdots \cup A_n) = \mathbf{P}(A_1) + \cdots + \mathbf{P}(A_n).$$

A useful special case: if $\Omega$ is finite and $A = \{s_1, \dots, s_k\}$, then $A$ is the union of
$k$ disjoint singletons, so
$$\mathbf{P}(A) = \mathbf{P}(\{s_1\}) + \cdots + \mathbf{P}(\{s_k\}).$$
Writing $\mathbf{P}(\{s_i\})$ every time is tedious, so it's standard (if a slight abuse of
notation, since probabilities are formally assigned to sets, not points) to drop the braces and
write $\mathbf{P}(s_i)$.

*A fine point, safely set aside.* Not every subset of an infinite sample space like the dart's
square can be assigned a probability consistent with the axioms — there exist genuinely pathological
("non-measurable") subsets for which no consistent assignment exists. This never comes up in this
course or in any application encountered here; it belongs to the doctoral-level foundations of the
subject and can be forgotten immediately.

## The discrete uniform law

Return to the two-dice example, $\Omega = \{1,2,3,4\}^2$, and adopt the simplest probability law:
every one of the 16 outcomes gets probability $1/16$. (One motivation: well-manufactured dice
behave this way empirically — though nothing forces the model to be this simple; a die could be
weighted so that some pairs are more likely than others.) With that law in hand, any question about
the experiment reduces to identifying an event in the picture and counting cells.

- $\mathbf{P}(\{(1,1),(1,2)\}) = 2/16$ — two outcomes, each with probability $1/16$.
- $\mathbf{P}(X = 1) = 4/16$ — the column where the first roll is 1 has four cells.
- $\mathbf{P}(X + Y \text{ odd}) = 8/16$ — count the cells where the sum is odd.
- $\mathbf{P}(\min(X,Y) = 2)$: harder to see without a picture. The minimum is 2 exactly when both
  rolls are 2, or one roll is 2 and the other is larger — five cells in total, so the probability is
  $5/16$.

<figure>
<svg viewBox="0 0 320 320" role="img" aria-label="Grid of the 16 outcomes of two die rolls with the event that the minimum of the two rolls equals 2 shaded">
  <line x1="50" y1="30" x2="50" y2="270" stroke="currentColor" stroke-width="1"/>
  <line x1="110" y1="30" x2="110" y2="270" stroke="currentColor" stroke-width="1"/>
  <line x1="170" y1="30" x2="170" y2="270" stroke="currentColor" stroke-width="1"/>
  <line x1="230" y1="30" x2="230" y2="270" stroke="currentColor" stroke-width="1"/>
  <line x1="290" y1="30" x2="290" y2="270" stroke="currentColor" stroke-width="1"/>
  <line x1="50" y1="30" x2="290" y2="30" stroke="currentColor" stroke-width="1"/>
  <line x1="50" y1="90" x2="290" y2="90" stroke="currentColor" stroke-width="1"/>
  <line x1="50" y1="150" x2="290" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="50" y1="210" x2="290" y2="210" stroke="currentColor" stroke-width="1"/>
  <line x1="50" y1="270" x2="290" y2="270" stroke="currentColor" stroke-width="1"/>
  <rect x="110" y="150" width="60" height="60" fill="currentColor" fill-opacity="0.15"/>
  <rect x="110" y="90" width="60" height="60" fill="currentColor" fill-opacity="0.15"/>
  <rect x="110" y="30" width="60" height="60" fill="currentColor" fill-opacity="0.15"/>
  <rect x="170" y="150" width="60" height="60" fill="currentColor" fill-opacity="0.15"/>
  <rect x="230" y="150" width="60" height="60" fill="currentColor" fill-opacity="0.15"/>
  <text x="80" y="285" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="140" y="285" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="200" y="285" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <text x="260" y="285" text-anchor="middle" font-size="12" fill="currentColor">4</text>
  <text x="170" y="305" text-anchor="middle" font-size="12" fill="currentColor">X (first roll)</text>
  <text x="38" y="244" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="38" y="184" text-anchor="middle" font-size="12" fill="currentColor">2</text>
  <text x="38" y="124" text-anchor="middle" font-size="12" fill="currentColor">3</text>
  <text x="38" y="64" text-anchor="middle" font-size="12" fill="currentColor">4</text>
  <text x="15" y="150" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 15,150)">Y (second roll)</text>
</svg>
<figcaption>The 16 equally likely outcomes of two rolls of a four-sided die. The shaded cells are the
event that the minimum of the two rolls equals 2 — five cells, probability 5/16.</figcaption>
</figure>

This example is a special case of the **discrete uniform law**: if $\Omega$ has $N$ equally likely
outcomes and $A$ has $n$ of them, then
$$\mathbf{P}(A) = \frac{n}{N} = \frac{\text{number of elements of } A}{\text{total number of sample points}}.$$
This is the law behind fair coins, fair dice, and well-shuffled card decks. It also means that,
whenever the uniform law applies, *computing probabilities is the same problem as counting* — how
many outcomes are in $\Omega$, and how many are in $A$. Counting is easy here, but it is not always;
a later lecture is devoted entirely to counting systematically.

## The continuous uniform law

The same procedure — picture the event, then measure it — works for continuous sample spaces, with
area playing the role that counting played above. Go back to the two "random" numbers $X, Y$ in
$[0,1]$, and postulate the **uniform law**: $\mathbf{P}(A) = \text{area}(A)$. This says two regions
of equal area are equally likely, which is the natural model when there's no reason to prefer one
part of the square over another (the law doesn't *have* to be this way — it's a modeling choice, as
was the discrete uniform law above).

Consistent with the earlier motivation for assigning probability to sets rather than points: the
probability that $(X,Y)$ equals one exact point is zero, since a point has zero area.

For a genuine computation, take the event $X + Y \le 1/2$. Sketching it in the square shows it's the
triangle below the line $x+y=\tfrac12$, with legs of length $\tfrac12$:

<figure>
<svg viewBox="0 0 260 260" role="img" aria-label="Unit square sample space with the triangular region where X plus Y is at most one half shaded">
  <path d="M50,210 L230,210 L230,30 L50,30 Z" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <path d="M50,210 L140,210 L50,120 Z" fill="currentColor" fill-opacity="0.15"/>
  <line x1="50" y1="120" x2="140" y2="210" stroke="currentColor" stroke-width="1.5"/>
  <text x="145" y="225" text-anchor="middle" font-size="12" fill="currentColor">1/2</text>
  <text x="230" y="225" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="140" y="240" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="32" y="124" text-anchor="middle" font-size="12" fill="currentColor">1/2</text>
  <text x="32" y="34" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="15" y="120" text-anchor="middle" font-size="12" fill="currentColor" transform="rotate(-90 15,120)">y</text>
</svg>
<figcaption>The unit square sample space for two numbers chosen uniformly in [0,1]. The shaded
triangle is the event X + Y &#8804; 1/2; since probability equals area, this event has probability
1/8.</figcaption>
</figure>

Its area is $\tfrac12 \cdot \tfrac12 \cdot \tfrac12 = \tfrac18$, so $\mathbf{P}(X+Y \le 1/2) = 1/8$.
The moral of both examples — dice and darts — is the same: once a picture identifies the event,
finding its probability is "just" a matter of counting or measuring; how hard that calculation is
belongs to combinatorics or calculus, not to probability theory itself.

## Countable additivity: when finite reasoning runs out

Here is a case where the axioms above are not quite enough. Flip a coin repeatedly and wait for the
first head. The sample space is $\Omega = \{1, 2, 3, \dots\}$ (the flip number on which the first
head appears), and suppose you're told $\mathbf{P}(n) = 2^{-n}$. What is the probability that this
number is even?

Any reasonable person adds up the probabilities of the individual even outcomes:
$$\mathbf{P}(\{2,4,6,\dots\}) = \mathbf{P}(2) + \mathbf{P}(4) + \mathbf{P}(6) + \cdots
= \frac{1}{2^2} + \frac{1}{2^4} + \frac{1}{2^6} + \cdots = \frac{1}{3}.$$

But nothing so far licenses that step. Additivity, and its extension to finitely many disjoint
sets, says nothing about summing infinitely many probabilities. To justify it, one more rule is
needed:

> **Countable additivity axiom.** If $A_1, A_2, \dots$ is a *sequence* of pairwise disjoint events
> (that is, they can be listed first, second, third, and so on), then
> $$\mathbf{P}(A_1 \cup A_2 \cup \cdots) = \mathbf{P}(A_1) + \mathbf{P}(A_2) + \cdots.$$

This is strictly stronger than ordinary (finite) additivity, and the requirement that the events be
arranged in a sequence — countably many of them, indexed by $1, 2, 3, \dots$ — is doing real work,
not decoration. This subtlety is picked up again at the start of the next lecture.

## Exercises

**Events and set operations**

1. Express each of the following events in terms of $A$, $B$, $C$ and the operations of
   complementation, union, and intersection, and draw the corresponding Venn diagram in each case:
   (a) at least one of $A, B, C$ occurs; (b) at most one occurs; (c) none occurs; (d) all three
   occur; (e) exactly one occurs; (f) $A$ and $B$ occur but not $C$; (g) either $A$ occurs, or, if
   not, then $B$ does not occur either.

2. Derive, using only the axioms of probability (naming which axiom justifies each step),
   $$\mathbf{P}\big((A \cap B^c) \cup (A^c \cap B)\big) = \mathbf{P}(A) + \mathbf{P}(B) - 2\,\mathbf{P}(A \cap B).$$

3. Show that for any three events $A$, $B$, $C$,
   $$\mathbf{P}(A \cap B \cap C) \ge \mathbf{P}(A) + \mathbf{P}(B) + \mathbf{P}(C) - 2.$$

**Discrete probability laws**

4. A fair coin is flipped three times, with all eight sequences equally likely. Find the probability
   of: (a) HHH; (b) the specific sequence HTH; (c) any sequence with exactly two heads and one tail;
   (d) any sequence with at least as many heads as tails.

5. A six-sided die is loaded so that each even face is twice as likely as each odd face. Build a
   probabilistic model for a single roll, and find the probability that a 1, 2, or 3 comes up.

6. Bob has a peculiar pair of four-sided dice: the probability of any particular outcome (a pair of
   results) is proportional to the sum of the two dice, and all outcomes sharing the same sum are
   equally likely. Find (a) the probability that the sum is even; (b) the probability of rolling a 2
   and a 3, in either order.

7. In a class, 60% of the students are geniuses, 70% love chocolate, and 40% are both. Find the
   probability that a randomly chosen student is neither a genius nor a chocolate lover.

**Continuous probability laws**

8. Romeo and Juliet have a date. Each arrives with a delay, uniform between 0 and 1 hour, and the
   two delays are independent (all pairs of delays equally likely). Whoever arrives first waits 15
   minutes for the other before leaving. What is the probability that they meet?

9. Alice and Bob each choose a number at random in $[0,2]$, with probability proportional to area.
   Let $A$ be the event that the two numbers differ in magnitude by more than $1/3$, $B$ the event
   that at least one of the numbers exceeds $1/3$, $C$ the event that the two numbers are equal, and
   $D$ the event that Alice's number exceeds $1/3$. Find $\mathbf{P}(B)$, $\mathbf{P}(C)$, and
   $\mathbf{P}(A \cap D)$.

10. A circular dartboard of radius 10 in. scores 50 points within 1 in. of the center, 30 points
    between 1 and 3 in., 20 points between 3 and 5 in., and 10 points beyond 5 in. Mike's dart lands
    uniformly at random on the board. Find the probability that he scores 50 points, and the
    probability that he scores 30 points. Now suppose John is twice as likely to land in the right
    half of the board as in the left half, but uniformly distributed within each half; answer the
    same two questions for John's throw.

**Countable additivity**

11. Let $\Omega = \mathbb{R}$. (a) Suppose $\{a_n\}$ increases to a limit $a$ and $\{b_n\}$ decreases
    to a limit $b$. Show, using the axioms of probability rather than intuition, that
    $\lim_{n\to\infty} \mathbf{P}([a_n,b_n]) = \mathbf{P}([a,b])$. (b) Does the same conclusion hold
    if instead $\{a_n\}$ decreases to $a$ and $\{b_n\}$ increases to $b$?

12. (Continuity of probability.) (a) Let $A_1 \subset A_2 \subset \cdots$ be an increasing sequence
    of events and $A = \bigcup_{n=1}^\infty A_n$. Show that $\mathbf{P}(A) = \lim_{n\to\infty}
    \mathbf{P}(A_n)$. (b) Let $A_1 \supset A_2 \supset \cdots$ be a decreasing sequence and
    $A = \bigcap_{n=1}^\infty A_n$. Show that $\mathbf{P}(A) = \lim_{n\to\infty} \mathbf{P}(A_n)$.
    (c) Deduce that for a sample space $\Omega = \mathbb{R}$,
    $\mathbf{P}([0,\infty)) = \lim_{n\to\infty} \mathbf{P}([0,n])$ and
    $\lim_{n\to\infty} \mathbf{P}([n,\infty)) = 0$.

## Sources

- **Slides**: `lectures/01-slides.md` — outline, sample space definition and examples, the axioms,
  the finite and countably-infinite probability-law examples.
- **Transcript**: `recordings/lectures/01.md` — all worked reasoning and examples not on the slides:
  the coin-and-rain illustration of sample-space granularity (13:10–14:18), the outcome-vs-result
  distinction and tree/grid description for the two-dice example (15:23–19:43), the motivation for
  assigning probability to sets rather than points (20:48–23:03), the cream-cheese reading of
  additivity and the derivation that $\mathbf{P}(A) \le 1$ (26:22–30:38), the induction extending
  additivity to $n$ disjoint sets (31:44–35:12), the aside on non-measurable sets (35:12–37:22), the
  worked discrete- and continuous-uniform computations (37:22–46:20), and the countable-additivity
  example and axiom (46:20–50:38). Administrative remarks and course-logistics discussion at the
  start of the recording (00:00–09:40) are omitted as boilerplate.
- **Exercises**: `psets/01-questions.md` Q1, Q2, Q3, Q4, Q5, Q6; `recitations/01-slides.md` Q1, Q2,
  Q3, Q4 and item G1; both problem sets are attributed there to the course textbook (Bertsekas &
  Tsitsiklis), with Recitation 1's problems given as its own page references into that text.
- **Not used**: `tutorials/01-slides.md` / `01-slides-tut01.md` (independence and conditional
  probability — later material); the Fall 2010, Fall 2009 and Spring 2009 Quiz 1 exams and the Quiz
  I review sheet (binomial, geometric, conditional probability, Bayes' rule — cover Lectures 1–7);
  and the worked example `recordings/worked-examples/inferring-a-parameter-of-uniform-part-1.md`,
  which is explicit that it draws on Bayesian inference from later in the course ("chapter eight").
  None of these are about sample spaces or the axioms, so nothing from them appears above.

---

[Contents](index.md) · [2. Conditional Probability and Bayes' Rule →](02-conditional-probability-and-bayes-rule.md)
