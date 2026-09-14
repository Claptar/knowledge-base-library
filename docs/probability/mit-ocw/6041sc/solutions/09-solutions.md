---
title: 09 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/09-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 09 solutions

**Source:** `solutions/09-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Problem Set 9 Solutions

1. (a) Yes, to 0. Applying the weak law of large numbers, we have


Here µ = 0 since Xi ∼ U (−1.0, 1.0).

(b) Yes, to 1. Since Wi ≤ 1, we have for ǫ > 0,


(c) Yes, to 0.

|Vn| ≤ min{|X1|, |X2|, · · ·, |Xn|}

but min{|X1|, |X2|, ···, |Xn|} converges to 0 in probability. So, since |Vn| ≥ 0, |Vn| converges to 0 in probability. To see why min{|X1|, |X2|, · · ·, |Xn|} converges to 0 in probability, note that:


2. Consider a random variable X with PMF


The mean of X is µ, and the variance of X is 2pc<sup>2</sup> . To make the variance equal σ<sup>2</sup> , set p = 2<sup>σ</sup> c<sup>2</sup> 2<sup>.</sup> For this random variable, we have


and therefore the Chebyshev inequality is tight.

3. (a) Let ti be the expected time until the state HT is reached, starting in state i, i.e., the mean first passage time to reach state HT starting in state i. Note that tS is the expected number of tosses until first observing heads directly followed by tails. We have,


Page 1 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

and by solving these equations, we find that the expected number of tosses until first ob­ serving heads directly followed by tails is


- (b) To find the expected number of additional tosses necessary to again observe heads followed by tails, we recognize that this is the mean recurrence time t<sup>∗</sup> HT of state HT . This can be determined as


- (c) Let’s consider a Markov chain with states S, H, T, TT , where S is a starting state, H indi­ cates heads on the current toss, T indicates tails on the current toss (without tails on the previous toss), and TT indicates tails over the last two tosses. The transition probabilities for this Markov chain are illustrated below in the state transition diagram:


Let ti be the expected time until the state TT is reached, starting in state i, i.e., the mean first passage time to reach state TT starting in state i. Note that tS is the expected number of tosses until first observing tails directly followed by tails. We have,


and by solving these equations, we find that the expected number of tosses until first ob­ serving two consecutive tails is

tS = 6 .

- (d) To find the expected number of additional tosses necessary to again observe heads followed by tails, we recognize that this is the mean recurrence time t<sup>∗</sup> TT of state TT . This can be

Page 2 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

determined as


It may be surprising that the average number of tosses until the first two consecutive tails is greater than the average number of tosses until heads is directly followed by tails, considering that the mean recurrence time between pairs of tosses with heads directly followed by tails equals the mean recurrence time between pairs of tosses that are both tails (or equivalently, the long-term frequency of pairs of tosses with heads followed by tails equals the long-term frequency of pairs of tosses with two consecutive tails<sup>1</sup> ). This is a start-up artifact. Note that the distribution of the first passage time to reach state HT (or TT ) starting in state S is the same as the conditional distribution of the recurrence time of state HT (or TT ), given that it is greater than 1. Although in both cases the expected values of the recurrence times are equal (this is what parts (b) and (d) tell us), the conditional expected values of the recurrence time given that it is greater than 1 is not the same in both cases (possible, because the unconditional distributions are not equal).

4. (a) The long-term frequency of winning can be found as sum of the long-term frequency of transitions from 1 to 2 and 2 to 2. These can be found from the steady-state probabilities π1 and π2, which are known to exist as the chain is aperiodic and recurrent. The local balance and normalization equations are as follows:


Solving these we obtain,


The probability of winning, which is the long-term frequency of the transitions from 1 to 2 and 2 to 2, can now be found as


Note that from the balance equation for state 2,


the long-term probability of winning always equals π2.

- (b) This question is one of determining the probability of absorption into the recurrent class {1A, 2A}. This probability of absorption can be found by recognizing that it will be the ratio of probabilities


> 1See problem 7.34 on page 399 of the text for a detailed explanation of this correspondence between mean recurrence times and steady-state probabilities.

Page 3 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

More methodically, if we define ai as the probability of being absorbed into the class {1A, 2A}, starting in state i, we can solve for the ai by solving the system of equations


- (c) Let A, B be the events that Jack eventually plays with decks 1A & 2A, 1B & 2B, respectively, when starting in state 1. From part (b), we know that P(A) = a1 = 23 and P(B) = 1 − a1 = 13 . The probability of winning can be determined as

# P(winning) = P(winning|A)P(A) + P(winning|B)P(B) .

By considering the corresponding the appropriate recurrent class and solving a problem similar to part (a), P(winning|A) and P(winning|B) can be determined; in these cases, the steady-state probabilities of each recurrent class are defined under the assumption of being absorbed into that particular recurrent class. Let’s begin with P(winning|A). The local balance and normalization equations for the recurrent class {1A, 2A} are


Solving these we obtain,


and hence conclude that


Similarly, the local balance and normalization equations for the recurrent class {1B, 2B} are


Solving these we obtain,


and hence conclude that


Page 4 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Putting these pieces together, we have that


meaning that Jack substantially increases the odds to his favor by slipping additional cards into the decks.

- (d) The expected time until Jack slips cards into the deck is the same as the expected time until the Markov chain enters a recurrent state. Let µi be the expected amount of time until a recurrent state is reached from state i. We have the equations


which when solved, yields the expected time until Jack slips cards into the deck,


- (e) Let S be the number of times that the dealer switches from deck #2 to deck #1, which equals the number of times that he/she switches from deck #1 to deck #2. Let p be the probability that S = 0, which is the sum of the probability of all ways for the first change of state to be from state 1 to state 1A or state 1B,


Alternatively, p is the probability of absorption of the following modified chain into an absorbing state (1A or 1B), when started in state 1:


As P(S > 0) = 1 − p, and similarly, P(S > k + 1|S > k) = 1 − p, it should be clear that S will be a shifted geometric, and thus


Page 5 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (f) Note that S from part (e) is the total number of cycles from 1 to 2 and back to 1. During the ith cycle, the number of wins, Wi, is a geometric random variable with parameter q = 59 . Thus the total number of wins by Jack before he slips extra cards into the deck is


which is a random number of random variables, all of which are independent. Conditioned on S > 0, W is a geometric (with parameter p) number of geometric (with parameter q) random variables, all conditionally independent, and thus from the theory of splitting Bernoulli processes,


- (g) Let W be the total number of wins before slipping cards into the deck (as in part (f)), and similarly let L be the total number of losses before absorption. We know from part (d) that E[W + L] = µ1 = 9.2. From part (f) we can find E[W ] by total expectation,


because when conditioned on S > 0, the number of wins, W , is a geometric random variable with parameter pq = 16 . From linearity of expectation, we find


- (h) Using A to again denote the probability of being absorbed into the recurrent class {1A, 2A}, starting in state 1,


Note that the right hand side above equals p1A,2A, as clear from the local balance equation π1Ap1A,2A = π2Ap2A,1A.

Page 6 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

G1<sup>†</sup> . With a > 0 and c ≥ 0,


where the first inequality follows from the fact that a + c > 0, and the second inequality follows from the Markov inequality.

To tighten the bound, we treat (σ<sup>2</sup> + c<sup>2</sup> )/(a + c)<sup>2</sup> as a function of c, and find c such that the derivative is 0. The minimum occurs at c = σ<sup>2</sup> /a. Therefore,


†Required for 6.431; optional challenge problem for 6.041

Page 7 of 7

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
