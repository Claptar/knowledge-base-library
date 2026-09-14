---
title: Takis exercises Part 08 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 08 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Generalise the previous exercise, by replacing 5 by a general positive integer n. Find the expected number of steps to reach state n, when starting from state 1. Test your conjecture for several different values of n. Can you conjecture an estimate for the expected number of steps to reach state n, for large n?

Solution. The answer here is


We here recognise the harmonic series:


for large n, in the sense that the difference of the two sides converges to a constant. So,


when n is large.

20.

A gambler plays a game in which on each play he wins one dollar with probability p and loses one dollar with probability q = 1 − p. The Gambler’s Ruin Problem is the problem of finding


1. Show that this problem may be considered to be an absorbing Markov chain with states 0, 1, 2, . . . , b, with 0 and b absorbing states.

2. Write down the equations satisfied by ϕ(x).

3. If p = q = 1/2, show that


4. If p̸ = q, show that


Solution. 1. If the current fortune is x the next fortune will be either x + 1 or x − 1, with probability p or 1, respectively, as long as x is not b or x is not 0. We assume independence between games, so the next fortune will not depend on the previous

17

ones; whence the Markov property. If the fortune reaches 0 then the gambler must stop playing. So 0 is absorbing. If it reaches b then the gambler has reached the target hence the play stops again. So both 0 and T are absorbing states. The transition diagram is:


2. The equations are:


3. If p = q = 1/2, we have


This means that the point (x, ϕ(x)) in the plane is in the middle of the segment with endpoints (x − 1, ϕ(x − 1)), (x + 1, ϕ(x + 1)). Hence the graph of the function ϕ(x) must be on a straight line (Thales’ theorem):


In other words,


We determine the constants A, B from ϕ(0) = 0, ϕ(b) = 1. Thus, ϕ(x) = x/b.

4. If p̸ = q, then this nice linear property does not hold. However, if we substitute the given function to the equations, we see that they are satisfied.

21.

Consider the Markov chain with transition matrix


18

(a) Show that this is irreducible and aperiodic.

(b) The process is started in state 1; find the probability that it is in state 3 after two steps.

(c) Find the matrix which is the limit of P<sup>n</sup> as n →∞.

Solution


(a) Draw the transition diagram and observe that there is a path from every state to any other state. Hence it is irreducible. Now consider a state, say state i = 1 and the times n at which p<sup>(</sup> 1<sup>n</sup> ,1<sup>)> 0.Thesetimesare1, 2, 3, 4, 5, . . .andtheirgcdis1.Henceit</sup> is aperiodic. So the chain is regular.

(b)


(c) The limit exists because the chain is regular. It is given by


where π = (π(1), π(2), π(3)) is the stationary distribution which is found by solving the balance equations


together with


The balance equations are equivalent to


Solving the last 3 equations with 3 unknowns we find

Hence


19

22.

Show that a Markov chain with transition matrix


has more than one stationary distributions. Find the matrix that P<sup>n</sup> converges to, as n →∞, and verify that it is not a matrix all of whose rows are the same. You should work out this exercise by direct methods, without appealing to the general limiting theory of Markov chains–see lecture notes.

Solution. The transition diagram is:


Write the balance equations πP = π :


or


together with the normalisation condition<sup>�</sup> π(i) = 1, i.e.


and solve for π(1), π(2), π(3). Equation (1) gives


Equation (2) gives


i.e. it is useless. Equation (3) gives


again, obviously true. Equation (4) gives


Therefore, equations (1)–(4) are EQUIVALENT TO:


20

Hence we can set π(1) to ANY value we like between 0 and 1, say, π(1) ≡ p, and then let π(3) = 1 − p. Thus there is not just one stationary distribution but infinitely many. For each value of p ∈ [0, 1], any π of the form


is a stationary distribution.

To find the limit of P<sup>n</sup> as n →∞, we compute the entries of the matrix P<sup>n</sup> . Notice that the (i, j)-entry of P<sup>n</sup> equals


If i = 1 we have


because state 1 is absorbing. Similarly, state 3 is absorbing:


We thus know the first and third rows of P<sup>n</sup> :


We now compute the missing entries of the second row by simple observations, based on the fact that the chain, started in state 2, will remain at 2 for some time and then will leave it and either go to 1 or 3:

P2(Xn = 2) = P2(chain has stayed in state 2 for n consecutive steps) = (1/2)<sup>n</sup> .


Therefore,


Since 0.5<sup>n</sup> → 0 as n →∞, we have


21

23.

Toss a fair die repeatedly. Let Sn denote the total of the outcomes through the nth toss. Show that there is a limiting value for the proportion of the first n values of Sn that are divisible by 7, and compute the value for this limit.

Hint: The desired limit is a stationary distribution for an appropriate Markov chain with 7 states.

Solution. An integer k ≥ 1 is divisible by 7 if it leaves remainder 0 when divided by 7. When we divide an integer k ≥ 1 by 7, the possible remainders are


Let X1, X2, . . . be the outcomes of a fair die tossing. These are i.i.d. random variables uniformly distributed in {1, 2, 3, 4, 5, 6}. We are asked to consider the sum


Clearly, Sn is an integer. We are interested in the remainder of Sn when divided by 7. Call this Rn. So:


Note that the random variables R1, R2, R3, . . . form a Markov chain because if we know the value of Rn, all we have to do to find the next value Rn+1 is to add Xn to Rn, divide by 7, and take the remainder of this division, as in elementary-school arithmetic:


We need to find the transition probabilities


for this Markov chain, for all i, j ∈{0, 1, 2, 3, 4, 5, 6}. But Xn takes values in {1, 2, 3, 4, 5, 6} with equal probabilities 1/6. If to an i we add an x chosen from {1, 2, 3, 4, 5, 6} and then divide by 7 we are going to obtain any j in {0, 1, 2, 3, 4, 5, 6}. Therefore,


We are asked to consider the proportion of the first n values of Sn that are divisible by 7, namely the quantity


This quantity has a limit from the Strong Law of Large Numbers for Markov chains and the limit is the stationary distribution at state 0:


22

Therefore we need to compute π for the Markov chain (Rn). This is very easy. From symmetry, all states i must have the same π(i). Therefore


Hence


In other words, if you toss a fair die 10, 000 times then approximately 1667 times n you had a sum Sn that was divisible by 7, and this is true with probability very close to 1.

24.

(i) Consider a Markov chain on the vertices of a triangle: the chain moves from one vertex to another with probability 1/2. Find the probability that, in n steps, the chain returns to the vertex it started from.

(ii) Suppose that we alter the probabilities as follows:


Answer the same question as above.

Solution. (i) The transition matrix is


The characteristic polynomial is

whose roots are


Therefore,


C2 + C3 = 1 C2x2 + C3x3 = 0.

Solving, we find C2 = 1/3, C3 = 2/3. So


(ii) We now have


23

The characteristic polynomial is


Checking the divisors of the constant (1 or 2), we are lucky because we see that 1 is a zero:


So we divide f (x) with x − 1. Since


we have


Since


we have


Therefore,


So the other roots of f (x) = 0 are the roots of 3x<sup>2</sup> + 3x + 1 = 0. The discriminant of this quadratic is


so the roots are complex:


Letting x3 = 1 (the first root we found), we now have


We need to determine the constants C1, C2, C3. But we have


Solving for the constants, we find


24

25.

A certain experiment is believed to be described by a two-state Markov chain with the transition matrix P, where


and the parameter p is not known. When the experiment is performed many times, the chain ends in state one approximately 20 percent of the time and in state two approximately 80 percent of the time. Compute a sensible estimate for the unknown parameter p and explain how you found it.

Solution. If Xk is the position of the chain at time k, we are being told that when we perform the experiment (i.e. watch the chain), say, n times we see that approximately 20% of the time the chain is in state 1:


We know, from the Strong Law (=Theorem) of Large Numbers that


where π = (π(1), π(2)) is the stationary distribution. Combining the observation (5) with the Law of Large Numbers (6) we obtain


We can easily compute π because


and, of course,


whence


Solving 1+22p p<sup>= 0.2wefindp = 1/8.</sup>

26.

Here is a trick to try on your friends. Shuffle a deck of cards and deal out one at a time. Count the face cards each as ten. Ask your friend to at one of the first ten cards; if this card is a six, she is to look at the card turns up six cards later; if this card is a three, she is to look at the card turns up three cards later, and so forth. Eventually she will reach a where she is to look at a card that turns up x cards later but there are x cards left. You then tell her the last card that she looked at even though you did not know her starting point. You tell her you do this by watching her, and she cannot disguise the times that she looks at the cards. In fact just do the same procedure and,

25

even though you do not start at the point as she does, you will most likely end at the same point. Why?

Solution. Let Xn denote the value of the n-th card of the experiment when you start from the x-th card from the top. Let Yn denote the value of the n-th card of another experiment when you start from the y-th card from the top. You use exactly the same deck with the cards in the same order in both experiments. If, for some n and some m we have


then Xn+1 = Ym+1, Xn+2 = Ym+2, etc. The point is that the event


has a large probability. In fact, it has probability close to 1.

27.

You have N books on your shelf, labelled 1, 2, . . . , N . You pick a book j with probability 1/N . Then you place it on the left of all others on the shelf. You repeat the process, independently. Construct a Markov chain which takes values in the set of all N ! permutations of the books.

(i) Discuss the state space of the Markov chain. Think how many elements it has and how are its elements represented.

(ii) Show that the chain is regular (irreducible and aperiodic) and find its stationary distribution.

Hint: You can guess the stationary distribution before computing it.

Solution. (i) The state space is

S = {all function σ : {1, 2, . . . , N } →{1, 2, . . . , N } which are one-to-one and onto}.

These σ are called permutations and there are N ! of them:


Each σ can be represented by a the list of each values:


i.e. σ(i) is its values at i.

(ii) Let us find the transition probabilities. If σ is the current state and we pick the j-th book and place it in front, then the next state is the same if j = 1 or


if j̸ = 1. There are N possible next states and each occurs with probability 1/N . If we denote the next state obtained when picking the j-th book by σ<sup>(j)</sup> then we have


(For example, σ<sup>(1)</sup> = σ.) And, of course, pσ,τ = 0 if τ is not of the form σ<sup>(j)</sup> for some j. The chain is aperiodic because pσ,σ = 1/N for all σ. It is irreducible because, clearly,

26

it can move from any state (i.e. any arrangement of books) to any other. Hence it is regular.

It does not require a lot of thought to see that there is complete symmetry! Therefore all states must have the same stationary distribution, i.e.


You can easily verify that


i.e. the balance equations are satisfied and so our educated guess was correct.

28.

In unprofitable times corporations sometimes suspend dividend payments. Suppose that after a dividend has been paid the next one will be paid with probability 0.9, while after a dividend is suspended the next one will be suspended with probability 0.6. In the long run what is the fraction of dividends that will be paid?

Solution. We here have a Markov chain with two states: State 1: “dividend paid”

State 2: “dividend suspended”

We are given the following transition probabilities:


Hence


Let π be the stationary distribution. In the long run the fraction of dividends that will be paid equals π(1). But


and


whence


So, in the long run, 80% of the dividends will be paid.

---

[← Solution](07-solution.md) · [Up: contents](index.md) · [Takis exercises Part 09 — →](09-takis-exercises-part-09.md)
