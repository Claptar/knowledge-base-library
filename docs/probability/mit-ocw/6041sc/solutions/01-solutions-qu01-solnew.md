---
title: 01 solutions qu01 solnew
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/01-solutions-qu01-solnew.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 solutions qu01 solnew

**Source:** `solutions/01-solutions-qu01-solnew.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2009)

Quiz 1 Solutions: October 13, 2009

1. (10 points) We start first by listing the following probabilities:


The probability that Bob ate a ripe gala is:


2. (a) (10 points) If K is the number of gala apples selected from the n apples, then K is a binomial random variable. The probability that K = k is:


- (b) i. (12 points) Among the n + 1 apples, his bounty includes: 1 ripe gala from Caleb, k gala, n − k honey crisp. We can compute the probability of eating a ripe apple conditioned on Bob selecting an apple from each of the three disjoint cases listed above. The total probability theorem allows us to then find the probability of Bob eating a ripe apple.


ii. (12 points) Using Bayes’ Rule:


We can compute the P(ripe ∩ gala) as such:

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2009)


Combining this result with that of (i),


- (c) (10 points) Let A be the event that the first 10 apples picked were all gala and let B be the event that exactly 10 gala apples were picked out of the 20 apples.


The probability of the event B can be computed by using the result in (a), where n = 20 and k = 10. P(B) = �2010�p<sup>10</sup> (1 − p)<sup>10</sup> . P(A ∩ B) can be computed by seperating the event of A and B into disjoint events. The event {A ∩ B} = {1st 10 apples picked are gala and the last 10 apples are honey crisp}. P(A ∩ B) = p<sup>10</sup> (1 − p)<sup>10</sup> . Therefore,


3. (a) (10 points) Bob picks apples from each tree until he finds one that is not ripe, and so if we think of the event “picking an unripe apple” as a “success”, then Xi is the number of apples picked (i.e. trials) until we get our first success. Therefore Xi is a geometrically distributed random variable with probability of success 1 − g.

   - Since each tree has a random collection of apples, the apples Bob picks from the first tree are independent of the apples he picks from the second tree, and therefore X1 and X2 are independent and identically distributed random variables. The PMF of Xi is


the expectation of Xi is


and the variance of Xi is


Page 2 of 3

# Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2009)

- (b) (12 points) Given that Y2 = (X1 − 1) + (X2 − 1), we can use the linearity property of expectations to find the expectation of Y2.


Since adding or subtracting a constant from a random variable has no effect on its variance, and since X1 and X2 are independent, we have


- (c) (12 points)

Let k ≥ 0 and ℓ ≥ k. The event “Y1 = k and Y2 = ℓ” is identical to the event “X1 = k + 1 and X2 = ℓ − k + 1”. Since X1 and X2 are independent, the desired probability is (1 − g)g<sup>k+1</sup><sup>`−`1</sup> (1 − g)g<sup>ℓ</sup><sup>`−`k+1</sup><sup>`−`1</sup> = (1 − g)<sup>2</sup> g<sup>ℓ</sup> , when 0 ≤ k ≤ ℓ, and zero otherwise.


Note that we can interpret this result as the probability of ℓ failures (i.e. picking ℓ ripe apples) and two successes (i.e. the two unripe apples that cause Bob to stop at each tree). Note also that although the expression for the joint PMF doesn’t depend on k, the sample space does depend on k because ℓ ≥ k: Bob cannot pick more ripe apples in the first tree than he does in the first two trees combined.

- (d) (i) (5 points) No. X1 and Y2 are not independent because Y2 ≥ X1 − 1 and so knowing X1 gives us information about Y2. Specifically, if we know that Bob picked 10 total apples from the first tree (i.e. X1 = 10), then we also know that Bob must have picked at least 9 ripe apples from the first two trees combined (i.e. Y2 ≥ 9).

   - (ii) (5 points) Yes. X2 relates only to the second tree and Y1 relates only to the first tree, and since the picking of apples is independent across trees, the two random variables are independent.

Page 3 of 3

---

[Up: contents](../index.md)
