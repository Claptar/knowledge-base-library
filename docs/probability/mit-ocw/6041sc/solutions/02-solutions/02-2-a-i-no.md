---
title: 2. (a) i. No
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. (a) i. No

**Source:** `solutions/02-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
total is 10<br>5<br>4<br>3<br>2<br>1<br>1 2 3 4 5<br>Die 1<br>Die 2<br><!-- End of picture text -->

Overall, there are 25 different outcomes in the sample space. For a total of 10, we should get a 5 on both rolls. Therefore A ⊂ B, and


Page 2 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

We observe that to get at least one 5 showing, we can have 5 on the first roll, 5 on the second roll, or 5 on both rolls, which corresponds to 9 distinct outcomes in the sample space. Therefore


- ii. No Given event A, we know that both roll outcomes must be 5. Therefore, we could not have event C occur, which would require at least one 1 showing. Formally, there are 9 outcomes in C, and


But


- (b) i. No Out of the total 25 outcomes, 5 outcomes correspond to equal numbers in the two rolls. In half of the remaining 20 outcomes, the second number is higher than the first one. In the other half, the first number is higher than the second. Therefore,


There are eight outcomes that belong to event E:


To find P(F |E), we need to compute the proportion of outcomes in E for which the second number is higher than the first one:


- ii. Yes Conditioning on event D reduces the sample space to just four outcomes


which are all equally likely. It is easy to see that


3. (a) Suppose we choose old widgets. Before we choose any widgets, there are 500 · 0.15 = 75 defective old widgets. The probability that we choose two defective widgets is


Now let’s consider the new widgets. Before we choose any widgets, there are 1500 · 0.05 = 75 defective old widgets. Similar to the calculations above,

P(two defective|new) = P(first is defective|new) · P(second is defective|first is defective, new) 75 74 = = 0.002568 1500 1499

Page 3 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

By the total probability law,


Note that this number is very close to what we would get if we ignored the effects of removing one defective widget before choosing the second widget:


(b) Using Bayes’ rule,


4. (a)

- P(find in A and in A) = P(in A) · P(find in A|in A) = 0.4 · 0.25 = 0.1

P(find in B and in B) = P(in B) · P(find in B|in B) = 0.6 · 0.15 = 0.09

Oscar should search in Forest A first.

(b) Using Bayes’ Rule,


- (c) Again, using Bayes’ Rule,


- (d) In order for Oscar to find the dog, it must be in Forest A, not found on the first day, alive, and found on the second day. Note that this calculation requires conditional independence of not finding the dog on different days and the dog staying alive.


Page 4 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

5. (a) We proceed as follows:


where the equality marked with ∗ follows from the independence of A, B, and C.

- (b) <u>Proof 1: If</u> A and B are independent, then A<sup>c</sup> and B<sup>c</sup> are also independent (see Problem 1.43, page 63 for the proof).

For any two independent events U and V , DeMorgan’s Law implies


We proceed to prove the statement by induction. Letting U = A1 and V = A2, the base case is proven above. Now we assume that the result holds for any n and show that it holds for n + 1. For independent {A1, . . . , An, An+1}, let B = ∪<sup>n</sup> i=1<sup>Ai. It is easy to show thatB</sup> and An+1 are independent. Therefore,


which completes the proof.

<u>Proof 2: Alternatively, we can use the version of the DeMorgan’s Law for</u> n events:


But we know that A<sup>c</sup> 1<sup>, Ac</sup> 2<sup>, . . . , Ac</sup> n<sup>are independent. Therefore</sup>


- G1<sup>†</sup> . (a) The figure below describes the sample space via an infinite tree. The leaves of this tree are exactly all finite tournament histories; in addition, the two infinite paths represent the two infinite tournament histories that are possible. Note that the winner of the first game is either Alice or Bob; from then on, the winner of a game is either the winner of the previous game (in which case we have reached a leaf and the tournament has ended) or the player that sat out the previous game.The outcomes of the sample space correspond to the finite histories (which are identified with the leafs of the tree) and the two infinite histories: ACBACB... and BCABCA...

Page 5 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


- (b) The probability of an event is 1/2<sup>k</sup> times the number of finite histories contained in the event. The probability of the event consisting of one or both infinite histories is 0. We have to show that this probability law satisfies the three probability axioms. It clearly satisfies nonnegativity and additivity. To check normalization, we have to verify that the probabilities of all tournament histories sum up to 1.

Start by noticing that two of the histories are infinite and have probability 0. Each one of the remaining histories has some finite length k ≥ 2 (and hence is represented by one of the two leaves of the tree of the figure above at depth k) and probability 1/2<sup>k</sup> . Hence, summing all probabilities we get


- (c) The probability that exactly 2 games will be played is the sum of the probabilities of the two leaves at depth 2; that is,


Similarly, the probability that exactly i games will be played, for i = 3, 4, 5, is


Hence, the probability that the tournament lasts no more than 5 games is


Hence, it’s pretty probable that the tournament will last at most that much.

The probability that Alice wins the tournament is the sum of the probabilities of the leaves of the tree that are labeled “A”; that is,


where the first summation includes all leaves from the upper part of the tree, while the second one takes care of the leaves on the lower part. Calculating, we have


Page 6 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

By symmetry (note the correspondence between the histories where Alice wins and the histories where Bob does), Bob’s probability of winning is 145 , as well. Then, since the outcomes where nobody wins (these are the two infinite tournament histories) have total <u>4</u> probability 0, Carol wins with probability 1 − 14<sup><u>5</u></sup> − 14<sup><u>5</u></sup> = 14 . Hence, by not participating in the first game, Carol enters the tournament with a disadvantage.

†Required for 6.431; optional for 6.041

Page 7 of 7

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Problem Set 2: Solutions Due September 22, 2010](01-problem-set-2-solutions-due-september-22-2010.md) · [Up: contents](index.md)
