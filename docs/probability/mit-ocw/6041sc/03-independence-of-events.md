---
title: "3. Independence of Events"
course: "MIT 6.041SC"
chapter: 3
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. Independence of Events

## What this covers

This chapter answers a single question: when does knowing that one event happened tell you nothing
about another? It takes the conditional-probability toolkit from the previous lecture — the
definition of $P(A \mid B)$, the multiplication rule, the total probability theorem and Bayes' rule
— and uses it to build a formal definition of independence, first for two events, then for
conditional independence, and finally for a whole collection of events at once. It assumes you
already have sample spaces, events and conditional probability; none of that machinery is re-derived
here, only used.

## Review: the tools from conditional probability

Everything that follows leans on four facts about an event $B$ with $P(B) > 0$, all carried over from
the previous lecture:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

- **Multiplication rule:** $P(A \cap B) = P(B)\,P(A \mid B) = P(A)\,P(B \mid A)$.
- **Total probability theorem:** $P(B) = P(A)P(B \mid A) + P(A^c)P(B \mid A^c)$ — split a
  calculation into scenarios, find the probability of $B$ within each scenario, and add.
- **Bayes' rule:** $P(A_i \mid B) = \dfrac{P(A_i)P(B \mid A_i)}{P(B)}$ — invert the order of
  conditioning, going from a causal model (probabilities of an observation given a hypothesis) to an
  inference (probability of a hypothesis given the observation).

Conditional probability itself is left undefined when the conditioning event has probability zero.

## A running model: three tosses of a biased coin

A useful way to build a probability model is to describe it through a sequence of conditional
probabilities. Toss a coin with $P(H) = p$, $P(T) = 1-p$, three times. The experiment has eight
outcomes, strings of length 3 such as $HHH$ or $THT$. A branch of the outcome tree carries a label
that is a conditional probability: the label on the branch to the second toss being $H$ is the
probability that the second toss is $H$ *given* the result of the first; the label on the branch to
the third toss is the probability of $H$ *given* the first two results. In this particular model
those labels are always $p$ (for $H$) or $1-p$ (for $T$), no matter what came before — even if the
first toss was $T$, the second still has conditional probability $p$ of being $H$. That is a special
feature of this model, not a general fact about conditional probabilities, and it is the feature this
chapter is about to name.

Before naming it, the tree lets you exercise the three tools above on a single example.

**Multiplication rule.** The probability of a specific sequence is the product of the conditional
probabilities along the path to it:
$$P(THT) = (1-p)\cdot p \cdot (1-p).$$

**Total probability / enumeration.** The event "exactly one head" happens in three ways — $HTT$,
$THT$, $TTH$ — and each has the same probability $p(1-p)^2$, so
$$P(\text{1 head}) = 3\,p(1-p)^2.$$

**Bayes' rule.** Given that there was exactly one head, what is the probability it was the first
toss? Intuitively, by symmetry among the three positions, the answer should be $1/3$. Checking it:
$$P(\text{1st toss} = H \mid \text{1 head}) = \frac{P(HTT)}{P(\text{1 head})}
= \frac{p(1-p)^2}{3\,p(1-p)^2} = \frac13,$$
confirming the symmetry argument.

## Independence of two events

A first attempt at defining independence of $A$ and $B$ is to say that learning $A$ occurred does not
change your assessment of $B$:
$$P(B \mid A) = P(B).$$
This is the right intuition, but it has a technical flaw: it is only defined when $P(A) > 0$, and it
treats $A$ and $B$ asymmetrically even though the idea is meant to be symmetric. Substituting it into
the multiplication rule, $P(A \cap B) = P(A)P(B\mid A)$, gives a cleaner equivalent statement, and
this is the one taken as the actual definition:

$$A \text{ and } B \text{ are independent} \iff P(A \cap B) = P(A)\,P(B).$$

This version is symmetric in $A$ and $B$, is defined even when $P(A) = 0$, and (when both
conditional probabilities are defined) implies both $P(B\mid A) = P(B)$ and $P(A \mid B) = P(A)$. A
corollary of stating it this way: if $P(A) = 0$, then $A$ is independent of *every* event $B$,
because $P(A \cap B) \le P(A) = 0$ forces both sides of the definition to be $0$. This can feel odd
next to the everyday sense of "independent," but it follows directly from the definition.

Independence typically shows up in one of two ways. Most commonly it reflects two physically
separate mechanisms that do not interact — repeating an experiment at a different time or place, so
that whatever noise affects one run has nothing to do with the noise in the other. Occasionally,
though, two events that *are* physically linked will still happen to satisfy the product equation
exactly, as a numerical accident rather than for a structural reason; the definition does not care
which of the two is the cause.

## Independence is not disjointness

Two events drawn as separate regions in a picture can look "independent" simply because they don't
touch, but disjointness is close to the opposite of independence. If $A$ and $B$ are disjoint, then
learning $A$ occurred tells you for certain that $B$ did not — about as strong a piece of information
as $B$ could receive. Checking the definition confirms it: if $P(A) = 1/3$ and $P(B) = 1/4$ with $A$
and $B$ disjoint, then $P(A \cap B) = 0$ while $P(A)P(B) = 1/12 \ne 0$, so the two events are *not*
independent. Equivalently, $P(A \mid B) = 0 \ne 1/3 = P(A)$: being told $B$ occurred collapses your
belief about $A$ completely.

The general moral is that a Venn diagram by itself can never certify independence — it can suggest
disjointness or overlap, but independence is a statement about *numbers*, and those numbers have to
be checked.

## Conditioning may affect independence

Since conditional probabilities obey all the same rules as ordinary probabilities, independence has
a conditional version. $A$ and $B$ are **conditionally independent given $C$** if they are independent
under the probability law $P(\cdot \mid C)$, i.e.
$$P(A \cap B \mid C) = P(A \mid C)\,P(B \mid C).$$

Two things can go wrong (or right) when a condition $C$ is introduced: independence in the original
model need not survive conditioning, and conditional independence within a scenario need not add up
to independence overall.

**Conditioning can destroy independence.** Suppose $A$ is the left half of the sample space and $B$
is the top half, so that $P(A) = P(B) = 1/2$ and $P(A \cap B) = 1/4 = P(A)P(B)$: independent. Now
suppose you are told that $C$ occurred, where $C$ is the pair of quadrants in which *exactly one* of
$A, B$ holds.

<figure>
<svg viewBox="0 0 260 260" role="img" aria-label="A 2 by 2 grid showing independent events A and B that become dependent once conditioned on C">
  <rect x="30" y="30" width="200" height="200" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <rect x="130" y="30" width="100" height="100" fill="currentColor" fill-opacity="0.15"/>
  <rect x="30" y="130" width="100" height="100" fill="currentColor" fill-opacity="0.15"/>
  <line x1="130" y1="30" x2="130" y2="230" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="130" x2="230" y2="130" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="84" text-anchor="middle" font-size="12" fill="currentColor">A∩B</text>
  <text x="180" y="84" text-anchor="middle" font-size="12" fill="currentColor">B only</text>
  <text x="80" y="184" text-anchor="middle" font-size="12" fill="currentColor">A only</text>
  <text x="180" y="184" text-anchor="middle" font-size="12" fill="currentColor">neither</text>
</svg>
<figcaption>A is the left half of the square and B is the top half, so P(A) = P(B) = 1/2 and
P(A∩B) = 1/4: independent. The shaded quadrants are C, where exactly one of A, B holds. Given C,
A∩B is impossible, while A and B each still have conditional probability 1/2 — so A and B are
dependent once C is known.</figcaption>
</figure>

Inside $C$, $A \cap B$ is impossible, so $P(A \cap B \mid C) = 0$, while $P(A \mid C) = P(B \mid C) =
1/2$, so $P(A\mid C)P(B \mid C) = 1/4 \ne 0$. $A$ and $B$ are unconditionally independent but become
(strongly) dependent once $C$ is known.

**Conditional independence need not add up to unconditional independence.** Take two badly biased
coins — call them coin 1, with $P(H) = 0.9$, and coin 2, with $P(H) = 0.1$ — and pick one of them with
probability $1/2$ each, then toss it repeatedly. Restricted to "coin 1 was chosen," the tosses are
independent of each other, each with conditional probability $0.9$ of heads regardless of the
history; the same is true, conditionally, within "coin 2 was chosen." Yet the tosses are *not*
independent once the choice of coin is unknown. By the total probability theorem,
$$P(\text{toss } 11 = H) = \tfrac12(0.9) + \tfrac12(0.1) = \tfrac12,$$
by the obvious symmetry between the two equally-likely, oppositely-biased coins. But if you are told
that the first ten tosses were all heads, ten heads in a row is far more consistent with coin 1
($0.9^{10}$) than with coin 2 ($0.1^{10}$), so by Bayes' rule the posterior probability that coin 1
was chosen,
$$P(\text{coin 1} \mid \text{10 heads}) = \frac{0.9^{10}}{0.9^{10} + 0.1^{10}},$$
is extremely close to $1$, and so
$$P(\text{toss 11} = H \mid \text{10 heads}) \approx 0.9,$$
noticeably different from the unconditional $1/2$. Learning about the earlier tosses did change the
assessment of a later one, so the tosses are dependent overall, even though they are conditionally
independent inside each sub-model. The physical link causing the dependence is the shared, unknown
choice of coin: a hidden common cause can correlate observations that would be independent if the
cause were known.

The two examples run in opposite directions, and together they say the same thing: independence and
conditional independence are genuinely different properties, and neither can be inferred from the
other without checking.

## Independence of a collection of events

The idea generalises: information about some events in a collection should tell you nothing about
the rest, in any combination. Written out, that intuition says things like
$$P\big(A_1 \cap (A_2^c \cup A_3) \mid A_5 \cap A_6^c\big) = P\big(A_1 \cap (A_2^c \cup A_3)\big),$$
for any way of grouping the events into a "known" side and a "target" side. Turning that into a
workable definition directly, event by event, is awkward. The definition that actually works, and
from which relations like the one above follow, is:

> Events $A_1, \dots, A_n$ are **independent** if, for every collection of distinct indices $i, j,
> \dots, q$ chosen from $\{1, \dots, n\}$,
> $$P(A_i \cap A_j \cap \dots \cap A_q) = P(A_i)\,P(A_j)\cdots P(A_q).$$

The requirement must hold for *every* subcollection of the events, not only for the full collection
and not only pairwise.

## Pairwise independence is weaker than independence

Requiring the product rule only for pairs is a strictly weaker condition, and the gap is not a
technicality. Take two independent fair coin tosses, each of the four outcomes $HH, HT, TH, TT$
equally likely with probability $1/4$, and define
$$A = \{\text{1st toss} = H\}, \quad B = \{\text{2nd toss} = H\}, \quad C = \{\text{the two tosses
agree}\} = \{HH, TT\}.$$

Checking pairs: $P(A) = P(B) = P(C) = 1/2$, and $P(A \cap B) = P(HH) = 1/4 = P(A)P(B)$;
$P(A \cap C) = P(HH) = 1/4 = P(A)P(C)$; and by the symmetric roles of the two tosses, $B$ and $C$
satisfy the same relation. So $A, B, C$ are **pairwise independent**.

But the three together are not independent: $P(A \cap B \cap C) = P(HH) = 1/4$, whereas independence
would require $P(A)P(B)P(C) = 1/8$. The dependence is easy to see directly: $P(C \mid A \cap B) = 1$,
since knowing both tosses were heads makes it certain they agree, while $P(C) = 1/2$. Knowing $A$
alone says nothing about $C$, and knowing $B$ alone says nothing about $C$ — but knowing $A$ and $B$
*together* determines $C$ completely. That extra fact is exactly what the pairwise relations fail to
capture, and it is why the definition of independence for a collection needs the equation for every
subcollection, not just for pairs.

## Modeling assumptions matter: the king's sibling

A short puzzle makes the point that a probability calculation is only as good as the model behind it.
In a kingdom where boys take precedence, so that a family with at least one son always has a king
among its children, a particular royal family had two children, and one of them is the king. What is
the probability that the king's sibling is female?

The quick, tempting answer is $1/2$: the sibling is just another child, and childbirths are
independent, so it should be an even coin flip. A more careful calculation, assuming every child is
independently a boy or girl with probability $1/2$, sets up the sample space $\{BB, BG, GB, GG\}$,
each outcome equally likely. Being told there is a king rules out $GG$, leaving three equally likely
outcomes $\{BB, BG, GB\}$, in two of which the king's sibling is a girl. That gives
$$P(\text{sibling is female} \mid \text{there is a king}) = \frac23,$$
which looks like the "correct," less naive answer.

But the $2/3$ answer is not forced by the problem statement — it is forced by an unstated modeling
assumption, namely that the family decided in advance to have exactly two children, and it happened
that one was a boy. Change the process that generated the data and the answer changes completely.
If the family instead had children until the first boy arrived and then stopped, the fact that they
had a second child at all means the first was a girl, so the sibling is female with probability $1$.
If the custom of the kingdom is that a king strangles any brothers, the sibling is again certainly
female. The lesson is not that $2/3$ is "the" surprising right answer to memorize — it is that a
loosely worded problem hides a real choice about how the data was generated, and that choice has to
be pinned down before the probability calculation means anything.

## A worked example: breaking a stick into a triangle

A companion worked example applies the same idea — choosing things independently and uniformly at
random — to a continuous setting, using geometric probability (probability as area) rather than
counting outcomes. It goes beyond what this lecture itself develops, since it works with continuous,
jointly uniform random choices, but the reasoning about independence is the same.

Take a stick of length $1$ and choose two break points $x$ and $y$ independently and uniformly on
$[0, 1]$, giving three pieces. When can the three pieces be assembled into a triangle? Exactly when,
for every pair of pieces, their combined length exceeds the length of the third — otherwise the two
shorter pieces cannot reach each other.

Assume first that $x < y$, so the three pieces have lengths $x$, $y - x$, and $1 - y$. The three
triangle-inequality conditions,
$$x + (y-x) > 1-y, \qquad x + (1-y) > y - x, \qquad (y - x) + (1-y) > x,$$
simplify to
$$y > \tfrac12, \qquad y < x + \tfrac12, \qquad x < \tfrac12.$$

Because $x$ and $y$ are independent and uniform on $[0,1]$, the pair $(x,y)$ is uniformly distributed
over the unit square, so probability is just area. Restricted to $x < y$, the three conditions carve
out a triangular region:

<figure>
<svg viewBox="0 0 260 260" role="img" aria-label="Unit square of the two break points x and y, with the two shaded triangles where the three pieces satisfy the triangle inequality">
  <rect x="30" y="30" width="200" height="200" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="30" y1="230" x2="230" y2="30" stroke="currentColor" stroke-width="1"/>
  <line x1="130" y1="30" x2="130" y2="230" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <line x1="30" y1="130" x2="230" y2="130" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3"/>
  <polygon points="30,130 130,130 130,30" fill="currentColor" fill-opacity="0.15"/>
  <polygon points="130,230 230,130 130,130" fill="currentColor" fill-opacity="0.15"/>
  <text x="30" y="243" text-anchor="middle" font-size="11" fill="currentColor">0</text>
  <text x="130" y="243" text-anchor="middle" font-size="11" fill="currentColor">1/2</text>
  <text x="230" y="243" text-anchor="middle" font-size="11" fill="currentColor">1</text>
  <text x="230" y="257" text-anchor="end" font-size="12" fill="currentColor">x</text>
  <text x="24" y="234" text-anchor="end" font-size="11" fill="currentColor">0</text>
  <text x="24" y="134" text-anchor="end" font-size="11" fill="currentColor">1/2</text>
  <text x="24" y="34" text-anchor="end" font-size="11" fill="currentColor">1</text>
  <text x="14" y="18" text-anchor="start" font-size="12" fill="currentColor">y</text>
</svg>
<figcaption>x and y are the two break points, chosen independently and uniformly on [0,1], so (x,y)
is uniform on the square. The upper-left shaded triangle is where x &#60; y and the three pieces
satisfy the triangle inequality; the lower-right one is the mirror case x &#62; y. Each has area
1/8, for a total probability 1/4.</figcaption>
</figure>

with vertices at $(0, 1/2)$, $(1/2, 1/2)$ and $(1/2, 1)$, an area of $1/8$. The case $x > y$ is the
mirror image — swapping the roles of $x$ and $y$ swaps the three conditions in exactly the same way,
producing the second shaded triangle, also of area $1/8$, symmetric across the diagonal. Adding the
two symmetric pieces,
$$P(\text{the three pieces form a triangle}) = \frac18 + \frac18 = \frac14.$$

## Exercises

The independence problems in Recitation 3 are the closest match to this lecture. The problem set and
tutorial sheet from the same week are included too, for completeness; some of their later parts use
random variables and expectation, which belong to lectures after this one.

### From Recitation 3

1. Consider two independent fair coin tosses, with all four outcomes equally likely. Let
   $H_1 = \{\text{1st toss is heads}\}$, $H_2 = \{\text{2nd toss is heads}\}$, and
   $D = \{\text{the two tosses produced different results}\}$.
   (a) Are $H_1$ and $H_2$ (unconditionally) independent?
   (b) Given that $D$ has occurred, are $H_1$ and $H_2$ (conditionally) independent?

2. A drunk tightrope walker, in the middle of a very long rope, takes a step forward with probability
   $p$ and a step back with probability $1-p$ at each step.
   (a) What is the probability that after two steps he is back where he started?
   (b) What is the probability that after three steps he is one step ahead of where he started?
   (c) Given that after three steps he has ended up one step ahead, what is the probability that his
   first step was forward?

3. **Communication through a noisy channel.** A binary message ($0$ or $1$) sent through a noisy
   channel is received incorrectly with probability $\epsilon_0$ (if a $0$ was sent) or $\epsilon_1$
   (if a $1$ was sent); errors in different symbol transmissions are independent. The source sends a
   $0$ with probability $p$ and a $1$ with probability $1-p$.
   (a) What is the probability that a randomly chosen symbol is received correctly?
   (b) If the string $1011$ is sent, what is the probability every symbol is received correctly?
   (c) To improve reliability, each symbol is sent three times and decoded by majority rule (a $0$ is
   sent as $000$, a $1$ as $111$; the receiver decodes $0$ or $1$ according to whichever appears at
   least twice). What is the probability that a transmitted $0$ is decoded correctly?
   (d) Under the scheme in (c), what is the probability that a $0$ was sent given that the received
   string is $101$?

4. (a) Can an event $A$ be independent of itself? (b) If $A$ and $B$ are independent, use the
   definition of independence to show that $A$ and $B^c$ are independent. (c) If $A$, $B$, $C$ are
   independent and $P(C) > 0$, show that $A$ and $B$ are conditionally independent given $C$.

### From Problem Set 3

1. The hats of $n$ people are thrown into a box and each person picks one at random, every assignment
   of hats to people being equally likely. Find the probability that
   (a) everyone gets their own hat back;
   (b) the first $m$ people to pick get their own hats back;
   (c) everyone among the first $m$ people to pick gets a hat belonging to one of the last $m$ people
   to pick.
   Now suppose in addition that each hat, independently of everything else, has probability $p$ of
   being dirty. Find the probability that
   (d) the first $m$ people all pick up clean hats;
   (e) exactly $m$ people pick up clean hats.

2. Alice chooses 4 cards at random from a 52-card deck, memorizes them, and returns them to the deck.
   Bob then chooses 8 cards at random from the same deck. Alice wins if Bob's 8 cards include all 4 of
   hers. What is the probability that Alice wins?

3. (a) Let $X$ be a random variable taking nonnegative integer values. Show that
   $$E[X] = \sum_{k=1}^{\infty} P(X \ge k).$$
   (b) Use part (a) to find $E[Y]$ where $Y$ is uniform on $\{a, a+1, \dots, b\}$ for nonnegative
   integers $b > a$.

4. Two fair three-sided dice are rolled, and $X$ is the difference of the two rolls.
   (a) Find the PMF, expectation, and variance of $X$.
   (b) Find and plot the PMF of $X^2$.

5. For an integer $n \ge 2$, show that
   $$\sum_{k=2}^n k(k-1)\binom{n}{k} = n(n-1)2^{n-2}.$$

6. *(Required for 6.431; optional for 6.041.)* A candy factory packages jelly beans of eight colours
   into jars of $200$ beans each, with equal numbers of red and orange beans, equal numbers of yellow
   and green beans, one more black bean than blue beans, and three more violet beans than white beans.
   No two jars are allowed to have the same colour distribution. What is the largest number of jars
   the factory can produce?

### From Tutorial 3

1. $X$ and $Y$ are independent random variables, with mean $\mu_X$ and variance $\sigma_X^2$ for $X$,
   and mean $\mu_Y$ and variance $\sigma_Y^2$ for $Y$. Let $Z = 2X - 3Y$. Find the mean and variance
   of $Z$ in terms of the means and variances of $X$ and $Y$.

2. A professor grades every paper independently as one of $\{A, A-, B+, B, B-, C+\}$, each grade
   equally likely. How many papers do you expect to have to hand in before you have received every
   possible grade at least once?

3. The joint PMF of $X$ and $Y$ is given by:

   | | $x=1$ | $x=2$ | $x=3$ |
   | :--- | :---: | :---: | :---: |
   | $y=3$ | $c$ | $c$ | $2c$ |
   | $y=2$ | $2c$ | $0$ | $4c$ |
   | $y=1$ | $3c$ | $c$ | $6c$ |

   (a) Find $c$. (b) Find $p_Y(2)$. (c) Let $Z = YX^2$. Find $E[Z \mid Y=2]$. (d) Conditioned on
   $X \ne 2$, are $X$ and $Y$ independent? Justify in one line. (e) Find the conditional variance of
   $Y$ given $X = 2$.

## Sources

- **Lecture slides**, `lectures/03-slides.md` (Lecture 3: "Review" through "The king's sibling") — the
  four review formulas, the three-toss coin tree, the two statements of the definition of
  independence, the "conditioning may affect independence" prompts and the two-coin example, the
  intuitive and formal definitions of independence of a collection, the pairwise-independence table,
  and the king's-sibling prompt.
- **Lecture transcript**, `recordings/lectures/03.md`, captions [00:00]–[46:17] — the reasoning
  connecting the slides: why $P(B\mid A) = P(B)$ is replaced by the product definition
  ([13:08]–[16:24]), the disjointness-versus-independence discussion including the audience question
  ([17:38]–[20:53]), both directions of the conditioning-and-independence discussion together with the
  two-coin story ([22:01]–[30:06]), the full worked pairwise-vs-independence example on two coin
  tosses ([31:11]–[40:56]), and the king's-sibling discussion with its three variant assumptions
  ([40:56]–[46:17]).
- **Recitation 3**, `recitations/03-slides.md` — Exercises 1–4 above (the $H_1/H_2/D$ example, the
  tightrope walker, the noisy channel, and the two independence proofs). The channel figure referred
  to in Exercise 3 was not part of the supplied recitation text and is not reproduced here.
- **Problem Set 3**, `psets/03-questions.md` — Exercises 1–6 above. Exercises 3–5 use expectation and
  random variables, which this lecture has not yet introduced; they are included because they were
  assigned as part of the same problem set.
- **Tutorial 3**, `tutorials/03-slides.md` (the same content also appears in
  `tutorials/03-slides-tut03.md`) — Exercises 1–3 above, which likewise assume random variables, joint
  PMFs and variance from later material.
- **Worked example**, `recordings/worked-examples/probability-that-3-pieces-form-a-triangle.md`,
  captions [00:01]–[11:10] — the stick-breaking triangle example, included as supplementary material;
  it relies on continuous uniform random variables and geometric probability, which this lecture does
  not itself cover.
- **Referred to but not supplied:** the lecture's assigned reading, Section 1.5 of the course text;
  and the textbook problems cited by the recitation and tutorial (Example 1.20, p. 37; Problem 1.31,
  p. 60; Problems 1.43–1.44, pp. 63–64; Problem 2.40, p. 133), from Bertsekas and Tsitsiklis,
  *Introduction to Probability* (Athena Scientific) — the text itself was not among the supplied
  files.

---

[← 2. Conditional Probability and Bayes' Rule](02-conditional-probability-and-bayes-rule.md) · [Contents](index.md) · [4. Counting Methods and Binomial Probabilities →](04-counting-methods-and-binomial-probabilities.md)
