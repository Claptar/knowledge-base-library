---
title: 01 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/01-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 solutions

**Source:** `solutions/01-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

Problem Set 1: Solutions

Due: September 15, 2010

1. (a) A ∪ B ∪ C

   - (b) (A ∩ B<sup>c</sup> ∩ C<sup>c</sup> ) ∪ (A<sup>c</sup> ∩ B ∩ C<sup>c</sup> ) ∪ (A<sup>c</sup> ∩ B<sup>c</sup> ∩ C) ∪ (A<sup>c</sup> ∩ B<sup>c</sup> ∩ C<sup>c</sup> )

   - (c) (A ∪ B ∪ C)<sup>c</sup> = A<sup>c</sup> ∩ B<sup>c</sup> ∩ C<sup>c</sup>

   - (d) A ∩ B ∩ C

   - (e) (A ∩ B<sup>c</sup> ∩ C<sup>c</sup> ) ∪ (A<sup>c</sup> ∩ B ∩ C<sup>c</sup> ) ∪ (A<sup>c</sup> ∩ B<sup>c</sup> ∩ C)

   - (f) A ∩ B ∩ C<sup>c</sup>

   - (g) A ∪ (A<sup>c</sup> ∩ B<sup>c</sup> )


<!-- Start of picture text -->
Ω  00000001111111 0000000 111111100000001111111 Ω  Ω  Ω<br>0000000111111100000001111111 A  0000000 111111100000001111111 0000000 111111100000001111111 B  A  B  A  B  A  B<br>0000000111111100000001111111 0000000 111111100000001111111<br>0000000111111100000001111111 0000000 111111100000001111111<br>0000000111111100000001111111 0000000 111111100000001111111<br>0000000111111100000001111111 0000000 111111100000001111111<br>0000000 1111111 0000000 1111111 C  C  C  C<br>0000000 1111111<br>(a)  (b)  (c)  (d)<br>Ω  Ω  Ω<br>A  B  A  B<br>A  B<br>C  C<br>(e)  (f)  (g)<br><!-- End of picture text -->

2. Since all outcomes are equally likely we apply the discrete uniform probability law to solve the problem. To solve for any event we simply count the number of elements in the event and divide by the total number of elements in the sample space.

There are 2 possible outcomes for each flip, and 3 flips. Thus there are 2<sup>3</sup> = 8 elements (or sequences) in the sample space.

   - (a) Any sequence has probability of 1/8. Therefore P({H, H, H}) = 1/8 .

   - (b) This is still a single sequence, thus P({H, T, H}) = 1/8 .

   - (c) The event of interest has 3 unique sequences, thus P({HHT, HTH, THH}) = 3/8 .

   - (d) The sequences where there are more heads than tails are A : {HHH, HHT, HTH, THH}. 4 unique sequences gives us P(A) = 1/2 .

3. The easiest way to solve this problem is to make a table of some sort, similar to the one below.

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

|Die 1|Die 2|Sum|P(Sum)|
|---|---|---|---|
|1|1|2|2p|
|1|2|3|3p|
|1|3|4|4p|
|1|4|5|5p|
|2|1|3|3p|
|2|2|4|4p|
|2|3|5|5p|
|2|4|6|6p|
|3|1|4|4p|
|3|2|5|5p|
|3|3|6|6p|
|3|4|7|7p|
|4|1|5|5p|
|4|2|6|6p|
|4|3|7|7p|
|4|4|8|8p|
|||Total|80p|


P(All outcomes) = 80p (Total from the table)

and therefore


(a)

P(Even sum) = 2p + 4p + 4p + 6p + 4p + 6p + 6p + 8p = 40p = 1/2

(b)


## 4. P(B)

The shaded area in the following figure is the union of Alice’s pick being greater than 1/3 and Bob’s pick being greater than 1/3.


<!-- Start of picture text -->
Bob<br><!-- End of picture text -->


<!-- Start of picture text -->
2<br>1<br>1/3<br>0  1/3  1  2  Alice<br>2<br><!-- End of picture text -->

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


P(C)

In the following figure, the diagonal line represents the set of points where the two selected numbers are equal.


<!-- Start of picture text -->
Bob<br>2<br>1<br>1/3<br>0  1/3  1  2  Alice<br><!-- End of picture text -->

The line has an area of 0. Thus,


Overlapping the diagrams we would get for P(A) and P(D),


<!-- Start of picture text -->
Bob<br>2  000000000111111111 000000000111111111 000000000111111111 000000000000000001111111111111111100000001111111 000000000000000001111111111111111100000001111111<br>000000000111111111000000000111111111000000000000000001111111111111111100000001111111<br>010000000011111111000000000111111111<br>01 0000000011111111000000000000000001111111111111111100000001111111<br>000000000111111111000000000111111111<br>000000000111111111000000000000000001111111111111111100000001111111<br>000000000111111111000000000111111111<br>1  01 01 00000000111111110000000011111111000000000000000001111111111111111100000001111111000000000111111111<br>000000000111111111000000000000000001111111111111111100000001111111<br>000000000111111111000000000111111111<br>000000000111111111000000000000000001111111111111111100000001111111<br>000000000111111111000000000111111111<br>0000000001111111110000000000000000011111111111111111<br>1/3  0000000001111111110000000001111111110000000000000000011111111111111111<br>000000000111111111<br>0000000000000000011111111111111111<br>000000000111111111<br>0  1/3  0000000000000000011111111111111111 1  2  Alice<br><!-- End of picture text -->

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

double shaded area


5. (a) The probability of Mike scoring 50 points is proportional to the area of the inner disk. Hence, it is equal to απR<sup>2</sup> = απ, where α is a constant to be determined. Since the probability of landing the dart on the board is equal to one, απ10<sup>2</sup> = 1, which implies that α = 1/(100π).

Therefore, the probability that Mike scores 50 points is equal to π/(100π) = 0.01

- (b) In order to score exactly 30 points, Mike needs to place the dart between 1 and 3 inches from the origin. An easy way to compute this probability is to look first at that of scoring more than 30 points, which is equal to απ3<sup>2</sup> = 0.09.

Next, since the 30 points ring is disjoint from the 50 points disc, probability of scoring more than 30 points is equal to the probability of scoring 50 points plus that of scoring exactly 30 points. Hence, the probability of Mike scoring exactly 30 points is equal to 0.09 − 0.01 = 0.08

- (c) For the part (a) question. The probability of John scoring 50 points is equal to the probability of throwing in the right half of the board and scoring 50 points plus that of throwing in the left half and scoring 50 points.

The first term in the sum is proportional to the area of the right half of the inner disk and is equal to απR<sup>2</sup> /2 = απ/2, where α is a constant to be determined. Similarly, the probability of him throwing in the left half of the board and scoring 50 points is equal to βπ/2, where β is a constant (not necessarily equal to α).

In order to determine α and β, let us compute the probability of throwing the dart in the right half of the board. This probability is equal to


Since that probability is equal to 2/3, α = 1/(75π). In a similar fashion, β can be determined to be 1/(150π). Consequently, the total probability is equal to 1/150 + 1/300 = 0.01

For the part (b), The probability of scoring exactly 30 points is equal to that of scoring more than 30 points minus that of scoring exactly 50. By applying the same type of analysis as in (b) above, the probability is found to be equal to 0.08

These numbers suggest that John and Mike have similar skills, and are equally likely to win the game. The fact that Mike’s better control (or worst, depending on how you look at it) of the direction of his throw does not increase his chances of winning can be explained by the observation that both players’ control over the distance from the origin is identical.

   6. See the textbook, Problem 1.11 page 55, which proves the general version of Bonferroni’s inequality.

- G1<sup>†</sup> . (a) If we define An = [an, bn] for all n, it is easy to see that the sequence A1, A2, . . . is “monotonically decreasing,” i.e., An+1 ⊂ An for all n:

4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


<!-- Start of picture text -->
Omega<br>A1<br>A2<br>A3<br>. . .  An<br><!-- End of picture text -->

Furthermore, ∩<sup>∞</sup> n<sup>An= [a, b].</sup>

By the continuity property of probabilities (see Problem 1.13, page 56 of the text),

lim P([an, bn]) = P([a, b]). n→∞

- (b) No. Consider the following example. Let an = a + n1 , bn = b − n1 for all n. Then {an} is a decreasing sequence that converges to a, and {bn} is an increasing sequence that converges to b. If we define a probability law that places non-zero probability only on points a and b, then limn→∞ P([an, bn]) = 0, but P([a, b]) = 1.

This example is closely related to the continuity property of probabilities. In this case, if we define An = [an, bn], then A1, A2, . . . is “monotonically increasing,” i.e., An ⊂ An+1, but A = (∪<sup>∞</sup> n<sup>An) =(a, b), which is an open interval whose probability is 0 under our</sup> probability law.

5

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
