---
title: 02 solutions tut02 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-tut02-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 02 solutions tut02 sol

**Source:** `solutions/02-solutions-tut02-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

## Tutorial 2 Solutions September 23/24, 2010

1. A player is randomly dealt 13 cards from a standard 52-card deck.

   - (a) What is the probability the 13th card dealt is a king?

Answer:<sup>4</sup> .

52

Solution: Since we are not told anything about the first 12 cards that are dealt, the probability that the 13th card dealt is a King, is the same as the probability that the first card dealt, or in fact any particular card dealt is a King, and this equals: 524 .

- (b) What is the probability the 13th card dealt is the first king dealt? Answer: 131 · 4 �4812��/ 5213� .

Solution: The probability that the 13th card is the first king to be dealt is the probability that out of the first 13 cards to be dealt, exactly one was a king, and that the king was dealt last. Now, given that exactly one king was dealt in the first 13 cards, the probability that the king was dealt last is just 1/13, since each “position” is equally likely. Thus, it remains to calculate the probability that there was exactly one king in the first 13 cards dealt. To calculate this probability we count the “favorable” outcomes and divide by the total number of possible outcomes. We first count the favorable outcomes, namely those with exactly one king in the first 13 cards dealt. We can choose a particular king in 4 ways, and we can choose the other 12 cards in �� 4812<sup>ways, therefore there are 4·</sup> �� 1248<sup>favorable</sup> outcomes. There are �� 5213<sup>total outcomes, so the desired probability is</sup>

outcomes. There are


For an alternative solution, we argue as in Example 1.10. The probability that the first card is not a king is 48/52. Given that, the probability that the second is not a king is 47/51. We continue similarly until the 12th card. The probability that the 12th card is not a king, given that none of the preceding 11 was a king, is 37/41. (There are 52 − 11 = 41 cards left, and 48 − 11 = 37 of them are not kings.) Finally, the conditional probability that the 13th card is a king is 4/40. The desired probability is


2. Consider a random variable X such that


where a > 0 is a real parameter.

(a) Find a.

Page 1 of 2

# Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Solution. The sum of the values of the PMF of a random variable over all values that it takes with positive probability must be equal to 1. Hence, we have


which implies that a = 28.

- (b) What is the PMF of the random variable Z = X<sup>2</sup> ?

Solution. The following table shows the value of Z for a given value of X and the probability of that event.


We see that Z can take only three possible values with non-zero probability, namely 1,4, and 9. In addition, for each value, there correspond two values of X. So we have, for example, pZ(9) = P(Z = 9) = P(X = −3) + P(X = 3) = pX(−3) + pX(3). Hence the PMF of Z is given by


3. Suppose we label the classes A, B, and C. Now the probability that Joe and Jane will both be in class A is the number of possible combinations for class A that involve both Joe and Jane, divided by the total number of combinations for class A. Therefore the probability we are after is:


Since there are three classrooms, the probability that Joe and Jane end up in the same classroom is simply three times the answer we found above:

Another way of looking at the problem is described as follows,

Assume one of them pick first, say Joe. He can pick any one of the 90 available places. Then it’s Jane’s turn to pick. She has a probability of 89<sup>29</sup> of picking in the same class as Joe. Therefore, (<sup>88</sup> 28<sup>)</sup> 89 the overall probability is<sup>29</sup> , which is the same as 3 · (3090) .

4. Let A = event the 7 cards include exactly 3 aces.


Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
