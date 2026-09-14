---
title: 02 solutions rec02 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-rec02-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 02 solutions rec02 sol

**Source:** `solutions/02-solutions-rec02-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 2: Solutions September 14, 2010

1. Let A be the event that the first toss is a head and let B be the event that the second toss is a head. We must compare the conditional probabilities P(A ∩ B|A) and P(A ∩ B|A ∪ B). We have


and


Since P(A ∪ B) ≥ P(A), the first conditional probability above is at least as large, so Alice is right, regardless of whether the coin is fair or not. In the case where the coin is fair, that is, if all four outcomes HH, HT, T H, T T are equally likey, we have


A generalization of Alice’s reasoning is that if A, B, and C are events such that B ⊂ C and A ∩ B = A ∩ C (for example, if A ⊂ B ⊂ C), then the event A is at least as likely if we know that B has occurred than if we know that C has occurred. Alice’s reasoning corresponds to the special case where C = A ∪ B.

2. (a) Each possible outcome has probability 1/36. There are 6 possible outcomes that are doubles, so the probability of doubles is 6/36 = 1/6.

   - (b) The conditioning event (sum is 4 or less) consists of the 6 outcomes

{(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (3, 1)},

2 of which are doubles, so the conditional probability of doubles is 2/6 = 1/3.

   - (c) There are 11 possible outcomes with at least one 6, namely, (6, 6), (6, i), and (i, 6), for i = 1, 2, . . . , 5. Thus, the probability that at least one die is a 6 is 11/36.

   - (d) There are 30 possible outcomes where the dice land on different numbers. Out of these, there are 10 outcomes in which at least one of the rolls is a 6. Thus, the desired conditional probability is 10/30 = 1/3.

3. (a) See the textbook, Example 1.13, page 29.

   - (b) See the textbook, Example 1.17, page 33.

4. See the textbook, Example 1.12 (The Monty Hall Problem), page 27.

An alternative solution is given below:

Let Pi denote the event where the prize is behind door i, Ci denote the event where you initially choose door i, and Oi denote the event where your friend opens door i. The corresponding prob­ ability tree is:

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)


<!-- Start of picture text -->
O2<br>C1<br>O3<br>P (C2 | P1) 1<br>P1<br>O3<br>C2<br>C3 1<br>O2<br>C1 1 O3<br>O1<br>P (P 2 ) P 2 P (C2 | P2)<br>C2<br>O3<br>C3 1<br>O1<br>O2<br>C1 1<br>P (C2 | P3) 1<br>O1<br>P3<br>C2<br>O2<br>C3<br>O1<br>P (O3| P1 ∩C1)<br>P (O3| P2 ∩C2)<br>P (O2| P3 ∩C<br>3)<br>P (O2| P1 ∩C1)<br>P (O1| P2 ∩C2)<br>P (O1| P3 ∩C3)<br>P (C3| P2)<br>P (C1| P2)<br>P (C3| P1)<br>P (C1| P)1<br>P (C1| P)3<br>P (C3| P3)<br>P (P)1<br>P (P3)<br><!-- End of picture text -->

Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (a) The probability of winning when not switching from your initial choice is the probability that the prize is behind the door you initially chose:

P(Win when not switching) = P(P1 ∩ C1) + P(P2 ∩ C2) + P(P3 ∩ C3)

   - = P(P1)P(C1|P1) + P(P2)P(C2|P2) + P(P3)P(C3|P3)

   - = P(P1)P(C1) + P(P2)P(C2) + P(P3)P(C3)

   - = 1/3 · (P(C1) + P(C2) + P(C3))

   - = 1/3

- (b) The probability of winning when switching from your initial choice is the probability that the prize is behind the remaining (unopened) door:


- (c) Given C1, that you first choose door 1, with the new strategy of switching only if door 3 is opened, you win if the prize behind door 1 and door 2 is opened or if the prize is behind door 2 and door 3 is opened.


Given that your initial choice is door 1, the probability of winning under this new strategy is dependent on how your friend decides which of doors 2 or 3 to open if the prize also lies be­ hind door 1. If he always picks door 2, then P(O2|P1∩C1) = 1 and P(Win with new strategy|C1) = 2/3. If he picks between doors 2 and 3 with equal probability then P(O2|P1 ∩ C1) = 1/2 and P(Win with new strategy|C1) = 1/2.

Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
