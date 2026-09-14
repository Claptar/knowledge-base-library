---
title: Takis exercises Part 04 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 04 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

I have 4 umbrellas, some at home, some in the office. I keep moving between home and office. I take an umbrella with me only if it rains. If it does not rain I leave the umbrella behind (at home or in the office). It may happen that all umbrellas are in one place, I am at the other, it starts raining and must leave, so I get wet.

1. If the probability of rain is p, what is the probability that I get wet?

2. Current estimates show that p = 0.6 in Edinburgh. How many umbrellas should I have so that, if I follow the strategy above, the probability I get wet is less than 0.1?

Solution. To solve the problem, consider a Markov chain taking values in the set S = {i : i = 0, 1, 2, 3, 4}, where i represents the number of umbrellas in the place where I am currently at (home or office). If i = 1 and it rains then I take the umbrella, move to the other place, where there are already 3 umbrellas, and, including the one I bring, I have next 4 umbrellas. Thus,


because p is the probability of rain. If i = 1 but does not rain then I do not take the umbrella, I go to the other place and find 3 umbrellas. Thus,


Continuing in the same manner, I form a Markov chain with the following diagram:


<!-- Start of picture text -->
1<br>q p<br>p<br>0 1 q 2 3 4<br>p<br>p q<br>q<br><!-- End of picture text -->

4

But this does not look very nice. So let’s redraw it:


Let us find the stationary distribution. By equating fluxes, we have:


Also,


Expressing all probabilities in terms of π(4) and inserting in this last equation, we find


or


I get wet every time I happen to be in state 0 and it rains. The chance I am in state 0 is π(0). The chance it rains is p. Hence


With p = 0.6, i.e. q = 0.4, we have


less than 6%. That’s nice.

If I want the chance to be less than 1% then, clearly, I need more umbrellas. So, suppose I need N umbrellas. Set up the Markov chain as above. It is clear that


Inserting in<sup>�N</sup> i=0<sup>π(i)wefind</sup>


and so


We want P (WET ) = 1/100, or q + N > 100pq, or


So to reduce the chance of getting wet from 6% to less than 1% I need 24 umbrellas instead of 4. That’s too much. I’d rather get wet.

5

6.

Suppose that ξ0, ξ1, ξ2, . . . are independent random variables with common probability function f (k) = P (ξ0 = k) where k belongs, say, to the integers. Let S = {1, . . . , N }. Let X0 be another random variable, independent of the sequence (ξn), taking values in S and let f : S ×Z → S be a certain function. Define new random variables X1, X2, . . . by


(i) Show that the Xn form a Markov chain.

(ii) Find its transition probabilities.

Solution. (i) Fix a time n ≥ 1. Suppose that you know that Xn = x. The goal is to show that PAST=(X0, . . . , Xn−1) is independent of FUTURE=(Xn+1, Xn+2, . . .). The variables in the PAST are functions of


The variables in the FUTURE are functions of


But X0, ξ1, . . . , ξn−2 are independent of ξn, ξn+1, . . .. Therefore, the PAST and the FUTURE are independent.

(ii)


where


7.

Discuss the topological properties of the graphs of the following Markov chains:


Solution. Draw the transition diagram for each case.

(a) Irreducible? YES because there is a path from every state to any other state. Aperiodic? YES because the times n for which p<sup>(</sup> 1<sup>n</sup> ,1<sup>)>0are1, 2, 3, 4, 5, . . .andtheir</sup> gcd is 1.

(b) Irreducible? YES because there is a path from every state to any other state. Aperiodic? YES because the times n for which p<sup>(</sup> 1<sup>n</sup> ,1<sup>)>0are1, 2, 3, 4, 5, . . .andtheir</sup> gcd is 1.

(c) Irreducible? NO because starting from state 2 it remains at 2 forever. However, it

6

can be checked that all states have period 1, simply because pi,i > 0 for all i = 1, 2, 3. (d) Irreducible? YES because there is a path from every state to any other state. Aperiodic? NO because the times n for which p<sup>(</sup> 1<sup>n</sup> ,1<sup>)> 0are2, 4, 6, . . .andtheirgcdis</sup> 2.

(e) Irreducible? YES because there is a path from every state to any other state. Aperiodic? YES because the times n for which p<sup>(</sup> 1<sup>n</sup> ,1<sup>)>0are1, 2, 3, 4, 5, . . .andtheir</sup> gcd is 1.

8.

Consider the knight’s tour on a chess board: A knight selects one of the next positions at random independently of the past.

- (i) Why is this process a Markov chain?

- (ii) What is the state space?

(iii) Is it irreducible? Is it aperiodic?

(iv) Find the stationary distribution. Give an interpretation of it: what does it mean, physically?

(v) Which are the most likely states in steady-state? Which are the least likely ones? Solution. (i) Part of the problem is to set it up correctly in mathematical terms. When we say that the “knight selects one of the next positions at random independently of the past” we mean that the next position Xn+1 is a function of the current position Xn and a random choice ξn of a neighbour. Hence the problem is in the same form as the one above. Hence (Xn) is a Markov chain.

(ii) The state space is the set of the squares of the chess board. There are 8 × 8 = 64 squares. We can label them by a pair of integers. Hence the state space is

S = {(i1, i2) : 1 ≤ i1 ≤ 8, 1 ≤ i2 ≤ 8} = {1, 2, 3, 4, 5, 6, 7, 8} × {1, 2, 3, 4, 5, 6, 7, 8}.

(iii) The best way to see if it is irreducible is to take a knight and move it on a chess board. You will, indeed, realise that you can find a path that takes the knight from any square to any other square. Hence every state communicates with every other state, i.e. it is irreducible.

To see what the period is, find the period for a specific state, e.g. from (1, 1). You can see that, if you start the knight from (1, 1) you can return it to (1, 1) only in even number of steps. Hence the period is 2. So the answer is that the chain is not aperiodic.

(iv) You have no chance in solving a set of 64 equations with 64 unknowns, unless you make an educated guess. First, there is a lot of symmetry. So squares (states) that are symmetric with respect to the centre of the chess board must have the probability under the stationary distribution. So, for example, states (1, 1), (8, 1), (1, 8), (8, 8) have the same probability. And so on. Second, you should realise that (1, 1) must be less likely than a square closer to the centre, e.g. (4, 4). The reason is that (1, 1) has fewer next states (exactly 2) than (4, 4) (which has 8 next states). So let us make the guess that if x = (i1, i2), then π(x) is proportional to the number N (x) of the possible next states of the square x:

π(x) = CN (x).

But we must SHOW that this choice is correct. Let us say that y us a NEIGHBOUR of x if y is a possible next state of x (if it is possible to move the knight from x to y

7

in one step). So we must show that such a π satisfies the balance equations:


Equivalently, by cancelling C from both sides, we wonder whether


holds true. But the sum on the right is zero unless x is a NEIGHBOUR of y:


But the rule of motion is to choose on of the neighbours with equal probability:


Which means that the previous equation becomes


where in the last equality we used the obvious fact that x is a neighbour of y if and only if y is a neighbour of x (symmetry of the relation) and so the last sum equals, indeed, N (x). So our guess is correct!

Therefore, all we have to do is count the neighbours of each square x. Here we go:


We have

2 × 4 + 3 × 8 + 4 × 20 + 6 × 16 + 8 × 16 = 336.


8

etc.

Meaning of π. If we start with


then, for all times n ≥ 1,


(v) The corner ones are the least likely: 2/336. The 16 middle ones are the most likely: 8/336.

---

[← Takis exercises Part 03 —](03-takis-exercises-part-03.md) · [Up: contents](index.md) · [Takis exercises Part 05 — →](05-takis-exercises-part-05.md)
