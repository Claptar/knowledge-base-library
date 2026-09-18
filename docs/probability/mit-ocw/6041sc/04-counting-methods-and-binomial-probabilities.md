---
title: "4. Counting Methods and Binomial Probabilities"
course: "MIT 6.041SC"
chapter: 4
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Counting Methods and Binomial Probabilities

## What this covers

This chapter answers a question that looks purely mechanical but underlies a large fraction of
probability calculations: given a sample space in which every outcome is equally likely, how do you
actually *count* the size of an event? It assumes the discrete uniform law from earlier lectures,
$P(A) = |A|/|\Omega|$, together with independence and conditional probability, and it develops the
standard toolkit for turning "count the outcomes" into a closed-form answer: the basic counting
principle, permutations, subsets, combinations, binomial probabilities, and partitions.

## Probability is counting, once outcomes are equally likely

Recall the discrete uniform law: if every point of a finite sample space $\Omega$ is equally likely,
then for any event $A$,
$$P(A) = \frac{|A|}{|\Omega|},$$
the number of outcomes in $A$ divided by the total number of outcomes. Once this applies, nothing
about probability is left to do — the whole problem reduces to counting two sets. The rest of this
lecture develops reliable ways of counting sets that are described *implicitly* ("all sequences with
exactly $k$ heads", "all ways of dealing 52 cards into four hands") rather than by an explicit list.

## The basic counting principle

The single idea behind almost everything that follows: describe the construction of an outcome as a
sequence of stages, where stage $i$ offers $n_i$ choices *no matter what happened at the earlier
stages*. Then the total number of outcomes is the product
$$n_1 \cdot n_2 \cdots n_r.$$

The reason is the picture of a tree: at the end of stage 1 there are $n_1$ branches; from each of
those, stage 2 adds $n_2$ further branches, giving $n_1 n_2$ paths so far; and so on. Counting the
leaves of the tree is counting the choices multiplied together.

<figure>
<svg viewBox="0 0 380 230" role="img" aria-label="A branching tree showing a two-stage choice process, with the number of leaves equal to the product of the choices at each stage">
  <circle cx="190" cy="20" r="4" fill="currentColor"/>
  <line x1="190" y1="20" x2="70" y2="90" stroke="currentColor" stroke-width="1.2"/>
  <line x1="190" y1="20" x2="190" y2="90" stroke="currentColor" stroke-width="1.2"/>
  <line x1="190" y1="20" x2="310" y2="90" stroke="currentColor" stroke-width="1.2"/>
  <circle cx="70" cy="90" r="4" fill="currentColor"/>
  <circle cx="190" cy="90" r="4" fill="currentColor"/>
  <circle cx="310" cy="90" r="4" fill="currentColor"/>
  <line x1="70" y1="90" x2="40" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="70" y1="90" x2="100" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="190" y1="90" x2="160" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="190" y1="90" x2="220" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="310" y1="90" x2="280" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <line x1="310" y1="90" x2="340" y2="170" stroke="currentColor" stroke-width="1.2"/>
  <circle cx="40" cy="170" r="3.5" fill="currentColor"/>
  <circle cx="100" cy="170" r="3.5" fill="currentColor"/>
  <circle cx="160" cy="170" r="3.5" fill="currentColor"/>
  <circle cx="220" cy="170" r="3.5" fill="currentColor"/>
  <circle cx="280" cy="170" r="3.5" fill="currentColor"/>
  <circle cx="340" cy="170" r="3.5" fill="currentColor"/>
  <text x="225" y="55" font-size="12" fill="currentColor">n&#8321; choices</text>
  <text x="265" y="132" font-size="12" fill="currentColor">n&#8322; choices</text>
  <text x="190" y="205" text-anchor="middle" font-size="12" fill="currentColor">6 leaves in all: n&#8321;&#183;n&#8322;</text>
</svg>
<figcaption>The counting principle as a tree: whatever happened at stage 1, stage 2 always offers the
same number of further choices, so the number of complete outcomes is the product of the choices at
each stage. Drawn here with 3 and 2 branches for legibility; the lecture's own example used three
stages with 4, 3, and 2 choices, for $4 \cdot 3 \cdot 2 = 24$ outcomes.</figcaption>
</figure>

**License plates.** How many plates can you make with 3 letters followed by 4 digits? Each of the
three letter-slots has 26 choices and each of the four digit-slots has 10, independently of the
others, so the counting principle gives
$$26^3 \cdot 10^4.$$
If instead no letter and no digit may repeat, the number of choices shrinks at each stage because one
option has already been used up: 26 choices for the first letter, then 25, then 24; 10 choices for
the first digit, then 9, 8, 7:
$$26 \cdot 25 \cdot 24 \cdot 10 \cdot 9 \cdot 8 \cdot 7.$$

**Permutations.** Take $n$ distinct elements and ask in how many ways they can be arranged in a
sequence — any such arrangement is called a *permutation*. Building the sequence one slot at a time,
there are $n$ choices for the first slot, $n-1$ remaining choices for the second (one element has
been used), $n-2$ for the third, and so on down to a single forced choice for the last slot. By the
counting principle, the number of permutations of $n$ elements is
$$n! = n(n-1)(n-2)\cdots 1.$$

**Subsets.** How many subsets does a set of $n$ elements have? Building a subset is also a
multi-stage process: go through the elements one at a time and decide, for each, whether it goes in
or stays out. That is a binary choice repeated $n$ times, so the counting principle gives $2^n$
subsets. Check the smallest case: a one-element set has two subsets, the set itself and the empty
set — $2^1 = 2$, as it should.

## Worked example: six rolls of a die

Roll a fair, six-sided die six times, independently. What is the probability that all six rolls come
out different? Because the rolls are independent and the die is fair, every specific outcome — every
sequence of six numbers from 1 to 6 — has the same probability, $(1/6)^6$, so the discrete uniform
law applies to the whole sample space and the problem reduces to counting.

- **Size of the sample space.** Six independent rolls, six choices each: $|\Omega| = 6^6$.
- **Size of the event.** An outcome with all six rolls different must use each of the numbers 1
  through 6 exactly once, in some order — it is a permutation of $\{1,\dots,6\}$. The number of such
  outcomes is $6!$.

So
$$P(\text{all six rolls different}) = \frac{6!}{6^6}.$$

## Combinations: choosing $k$ out of $n$

Write $\binom{n}{k}$ for the number of $k$-element subsets of an $n$-element set — equivalently, the
number of ways to pick a committee of $k$ people out of a group of $n$, without regard to order. The
formula for $\binom{n}{k}$ comes from counting the same thing, an ordered list of $k$ distinct items
drawn from the $n$, in two different ways.

*First way — build the list directly.* Choose the items one at a time: $n$ choices for the first
slot, $n-1$ for the second, down to $n-k+1$ for the $k$th, giving
$$n(n-1)\cdots(n-k+1) = \frac{n!}{(n-k)!}$$
ordered lists.

*Second way — choose the set, then order it.* First pick which $k$ elements will appear, in
$\binom{n}{k}$ ways; then arrange those $k$ elements into a sequence, in $k!$ ways. This also builds
every ordered list, so it counts the same total: $\binom{n}{k} \cdot k!$.

Since both routes count exactly the same set of ordered lists,
$$\binom{n}{k} \cdot k! = \frac{n!}{(n-k)!} \quad\Longrightarrow\quad \binom{n}{k} = \frac{n!}{k!\,(n-k)!}.$$

Two extreme cases check the formula. Taking $k=n$: there is exactly one $n$-element subset of an
$n$-element set, namely the whole set, so $\binom{n}{n}$ must equal 1. The formula gives
$\binom{n}{n} = n!/(n!\cdot 0!)$, which forces the convention $0! = 1$. Taking $k=0$: with that same
convention, $\binom{n}{0} = n!/(0!\,n!) = 1$, matching the fact that there is exactly one 0-element
subset, the empty set.

A further identity is easy to guess once you think about what it counts, and painful to prove by
pushing symbols around:
$$\sum_{k=0}^n \binom{n}{k} = 2^n.$$
The left side adds up the number of 0-element subsets, plus the number of 1-element subsets, plus the
number of 2-element subsets, and so on through $n$-element subsets — that is, it counts *every*
subset exactly once, sorted by size. The total is therefore the number of subsets of an $n$-element
set, which is $2^n$.

## Binomial probabilities

Toss a coin $n$ times, independently, with $P(H) = p$ on each toss. Any *specific* sequence of heads
and tails has a probability that depends only on how many heads it contains, not on where they fall:
by independence, the probability of a sequence multiplies one factor of $p$ per head and one factor
of $(1-p)$ per tail, so every sequence with exactly $k$ heads, in any order, has the same probability,
$$p^k (1-p)^{n-k}.$$

The event "exactly $k$ heads" is the union of all such sequences, so its probability is that common
value times the number of them:
$$P(k \text{ heads}) = (\text{number of } k\text{-head sequences}) \cdot p^k(1-p)^{n-k}.$$
Specifying which sequence occurs, given that it has exactly $k$ heads, amounts to choosing which $k$
of the $n$ toss-slots are heads — exactly the combinations problem above. So the number of $k$-head
sequences is $\binom{n}{k}$, and
$$P(k \text{ heads}) = \binom{n}{k}\, p^k (1-p)^{n-k}, \qquad k = 0, 1, \dots, n$$
(the probability is 0 for $k$ outside this range, since $n$ tosses cannot produce more than $n$ or
fewer than 0 heads). As with the subset-counting identity above, summing over all possible counts
must exhaust the sample space:
$$\sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} = 1,$$
because the events "0 heads", "1 head", ..., "$n$ heads" are disjoint and their union is everything
that can happen.

## A conditional probability made easy by counting

Ten coin tosses, independent, with an unknown but fixed bias $P(H) = p$. Let $B$ be the event that
exactly 3 of the 10 tosses were heads. Given that $B$ occurred, what is the conditional probability
that the *first two* tosses were heads?

The sample space here is not uniform — with a biased coin, HHTTTTTTTT and TTTTTTTTHH do not have the
same probability in general, so the discrete uniform law does not apply to $\Omega$ directly. But
look inside $B$: every sequence with exactly 3 heads out of 10, whatever the positions of those
heads, has probability $p^3(1-p)^7$ — the same argument as in the previous section. So the outcomes
inside $B$ *are* equally likely as each other, and conditioning on $B$ preserves that: the
conditional probability law, restricted to $B$, is uniform over $B$. That licenses exactly the same
counting shortcut as before, applied inside the smaller universe $B$ instead of the whole of
$\Omega$:
$$P(A \mid B) = \frac{|A \cap B|}{|B|}.$$

- $|B|$: the number of 10-toss sequences with exactly 3 heads is $\binom{10}{3}$.
- $|A \cap B|$: sequences in $B$ that also start with two heads. If the first two tosses are both
  heads, the only remaining freedom is where the third head falls among the other 8 tosses — 8
  possibilities.

So
$$P(\text{first two tosses heads} \mid B) = \frac{8}{\binom{10}{3}}.$$

The general point is worth keeping: the discrete uniform law does not need the *whole* sample space
to be uniform. It is enough that the outcomes making up the conditioning event are equally likely
among themselves — conditioning never disturbs the relative proportions between them, so the
sub-experiment restricted to that event is uniform even when the full experiment is not.

## Partitions: dealing cards into several hands

Choosing a $k$-element subset out of $n$ is really splitting the $n$ elements into two groups: the
$k$ chosen and the $n-k$ left over. The natural generalization is to split $n$ elements into
*several* groups of prescribed sizes at once — a *partition*.

**Setting.** A 52-card deck is dealt to 4 players, 13 cards each, as in bridge. An outcome of this
experiment is which 13 cards each player ends up holding — a partition of the 52 cards into four
labeled groups of 13 — and, assuming a well-shuffled deck, every such partition is equally likely.
Once again the problem is to count.

**Size of the sample space.** Deal sequentially: choose 13 of the 52 cards for the first player
($\binom{52}{13}$ ways), then 13 of the remaining 39 for the second player ($\binom{39}{13}$ ways),
then 13 of the remaining 26 for the third ($\binom{26}{13}$ ways), leaving the last 13 forced on the
fourth player. Multiplying and cancelling the factorials,
$$\binom{52}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13} = \frac{52!}{13!\,13!\,13!\,13!}.$$

This is the general pattern: partitioning $n$ objects into groups of prescribed sizes
$n_1, n_2, \dots, n_r$ (with $n_1 + \cdots + n_r = n$) can be done in
$$\frac{n!}{n_1!\, n_2! \cdots n_r!}$$
ways — the *multinomial coefficient*, of which $\binom{n}{k}$ (the case $r=2$) is a special case.

**The event: each player gets exactly one ace.** Count the favorable deals in two stages.

- *Distribute the 4 aces, one per player.* Give the first ace to one of the 4 players, the second
  ace to one of the remaining 3 (who has no ace yet), the third to one of the remaining 2, and the
  last ace is forced: $4 \cdot 3 \cdot 2 \cdot 1 = 4!$ ways. (This is itself a partition — of the 4
  aces into four groups of size 1 — and the multinomial formula agrees: $4!/(1!1!1!1!) = 4!$.)
- *Distribute the remaining 48 cards, 12 to each player.* Exactly the same partition problem as
  before, at smaller numbers: $\dfrac{48!}{12!\,12!\,12!\,12!}$ ways.

Multiplying these and dividing by the size of the sample space gives
$$P(\text{each player gets an ace}) = \frac{4! \cdot \dfrac{48!}{12!\,12!\,12!\,12!}}{\dfrac{52!}{13!\,13!\,13!\,13!}}.$$
The expression looks unwieldy, but it does simplify considerably with more algebra than there is room
for here.

## Exercises

These are drawn from Recitation 4 of the course, which practices the same counting techniques on
further problems.

1. **The birthday problem.** $n$ people are at a party. Assume every person is equally likely to be
   born on any of the 365 days of the year, independently of everyone else (ignore February 29).
   What is the probability that all $n$ people have distinct birthdays?

2. **Rooks on a chessboard.** Eight rooks are placed at random on a chessboard. Find the probability
   that no two rooks share a row or a column — that all the rooks are "safe" from one another.

3. **Hypergeometric probabilities.** An urn contains $n$ balls, of which exactly $m$ are red. Draw
   $k$ balls at random, without replacement. What is the probability that exactly $i$ of the drawn
   balls are red?

4. **Multinomial coefficient, a second derivation.** Give a different argument from the one in this
   chapter for the number of ways of partitioning $n$ distinct items into groups of sizes
   $n_1, \dots, n_r$: arrange the $n$ items into $n$ slots in a row, and cut the row of slots into
   consecutive segments of lengths $n_1, \dots, n_r$. Count how many distinct partitions arise this
   way, and relate that count to the number of *arrangements* of the $n$ items into the $n$ slots.

5. **Multinomial probabilities.** At each of $n$ independent draws, the outcome is color $i$ (for
   $i = 1, \dots, r$) with probability $p_i$. What is the probability of obtaining exactly $n_i$
   draws of color $i$, for each $i$, given numbers $n_1, \dots, n_r$ summing to $n$?

## Sources

- **Slides**: `lectures/04-slides.md` — the lecture outline (discrete uniform law, basic counting
  principle, permutations, combinations, binomial probabilities, the coin-tossing problem,
  partitions) and the displayed equations for combinations, binomial probabilities, and the
  card-dealing partition. The slides list "Readings: Section 1.6", pointing to the course textbook,
  which was not supplied here.
- **Transcript**: `recordings/lectures/04.md` — the reasoning behind every derivation above: the
  tree picture for the counting principle (00:03:24–00:04:35), the license-plate examples
  (00:04:35–00:06:50), permutations and subset counting with the $n=1$ sanity check
  (00:06:50–00:10:22), the six-die-rolls example (00:10:22–00:16:02), the two-derivation argument
  for $\binom{n}{k}$ and its extreme-case checks (00:16:02–00:26:15), the combinatorial reading of
  $\sum_k \binom{n}{k} = 2^n$ (00:26:15–00:28:22), binomial probabilities and their normalization
  (00:28:22–00:36:23), the conditional-probability coin problem and the "uniform inside $B$"
  argument (00:36:23–00:41:57), and the card-partitioning problem (00:43:00–00:50:45).
- **Exercises**: `recitations/04-slides.md`, Recitation 4 (September 21, 2010), problems 1–5 — the
  birthday problem (Bertsekas & Tsitsiklis problem 1.50), chessboard rooks, hypergeometric
  probabilities (problem 1.61), and the two multinomial exercises. The recitation's page references
  point into Bertsekas & Tsitsiklis, *Introduction to Probability*, which was not itself supplied.
- **Not used**: `psets/04-questions/01-04-questions-part-01.md` and `02-04-questions-part-02.md`
  (Problem Set 4, due October 6, 2010) and `tutorials/04-slides.md` (Tutorial 4, October 7/8, 2010)
  were supplied for this slot, but their problems — joint PMFs, expectation and variance, geometric
  random variables, Gaussian and exponential random variables — belong to later material in the
  course's own sequence, not to this counting lecture, and so are not reproduced here.

---

[← 3. Independence of Events](03-independence-of-events.md) · [Contents](index.md) · [5. Random Variables, PMFs, and Expectation →](05-random-variables-pmfs-and-expectation.md)
