---
title: 04 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/04-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 04 solutions

**Source:** `solutions/04-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Problem Set 4: Solutions

1. (a) From the joint PMF, there are six (x, y) coordinate pairs with nonzero probabilities of occurring. These pairs are (1, 1), (1, 3), (2, 1), (2, 3), (4, 1), and (4, 3). The probability of a pair is proportional to the sum of the squares of the coordinates of the pair, x<sup>2</sup> + y<sup>2</sup> . Because the probability of the entire sample space must equal 1, we have:

(1 + 1)c + (1 + 9)c + (4 + 1)c + (4 + 9)c + (16 + 1)c + (16 + 9)c = 1.

Solving for c, we get c = 721<sup>.</sup>

- (b) There are three sample points for which y < x:


- (c) There are two sample points for which y > x:


- (d) There is only one sample point for which y = x:


Notice that, using the above two parts,


as expected.

- (e) There are three sample points for which y = 3:


- (f) In general, for two discrete random variable X and Y for which a joint PMF is defined, we have

In this problem the ranges of X and Y are quite restricted so we can determine the marginal PMFs by enumeration. For example,


Overall, we get:


Page 1 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

(g) In general, the expected value of any discrete random variable X equals

For this problem,


and


To compute E[XY ], note that pX,Y (x, y) ≠ pX(x)pY (y). Therefore, X and Y are not inde­ pendent and we cannot assume E[XY ] = E[X]E[Y ]. Thus, we have


(h) The variance of a random variable X can be computed as E[X<sup>2</sup> ]−E[X]<sup>2</sup> or as E[(X −E[X])<sup>2</sup> ]. We use the second approach here because X and Y take on such limited ranges. We have


and


X and Y are not independent, so we cannot assume var(X + Y ) = var(X) + var(Y ). The variance of X +Y will be computed using var(X +Y ) = E[(X +Y )<sup>2</sup> ]−(E[X +Y ])<sup>2</sup> . Therefore, we have

Therefore,


- (i) There are four (x, y) coordinate pairs in A : (1,1), (2,1), (4,1), and (4,3). Therefore, P(A) = 721 (2 + 5 + 17 + 25) = 4972 . To find E[X | A] and var(X | A), pX|A(x) must be calculated. We have


Page 2 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)


2. Consider a sequence of six independent rolls of this die, and let Xi be the random variable corresponding to the ith roll.

   - (a) What is the probability that exactly three of the rolls have result equal to 3? Each roll Xi can either be a 3 with probability 1/4 or not a 3 with probability 3/4. There are �63<sup>�</sup> ways of placing the 3’s in the sequence of six rolls. After we require that a 3 go in each of these spots, which has probability (1/4)<sup>3</sup> , our only remaining condition is that either a 1 or a 2 go in the other three spots, which has probability (3/4)<sup>3</sup> . So the probability of exactly three 1 3

   - rolls of 3 in a sequence of six independent rolls is �63�( 4 )<sup>3</sup> ( 4 )<sup>3</sup> .

   - (b) What is the probability that the first roll is 1, given that exactly two of the six rolls have result of 1? The probability of obtaining a 1 on a single roll is 1/2, and the probability of obtaining a 2 or 3 on a single roll is also 1/2. For the purposes of solving this problem we treat obtaining a 2 or 3 as an equivalent result. We know that there are �26<sup>�</sup> ways of rolling exactly two 1’s. Of these �26� ways, exactly �15� = 5 ways result in a 1 in the first roll, since we can place the remaining 1 in any of the five remaining rolls. The rest of the rolls must be either 2 or 3. Thus, the probability that the first roll is a 1 given exactly two rolls had 5

   - an outcome of 1 is . (<sup>6</sup> 2<sup>)</sup>

   - (c) We are now told that exactly three of the rolls resulted in 1 and exactly three resulted in 2. What is the probability of the sequence 121212? We want to find


Any particular sequence of three 1’s and three 2’s will have the same probability: (1/2)<sup>3</sup> (1/4)<sup>3</sup> . There are �63� possible rolls with exactly three 1’s and three 2’s. Therefore,


- (d) Conditioned on the event that at least one roll resulted in 3, find the conditional PMF of the number of 3’s. Let A be the event that at least one roll results in a 3. Then


Page 3 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

# (Fall 2010)

We find the conditional PMF pk|A(k | A) using the definition of conditional probability:


Thus we obtain


Note that pK|A(0 | A) = 0 because the event {K = 0} and the event A are mutually exclusive. Thus the probability of their intersection, which appears in the numerator in the definition of the conditional PMF, is zero.

3. By the definition of conditional probability,


The event {X = i} ∩{X + Y = n} in the numerator is equivalent to {X = i} ∩{Y = n − i}. Combining this with the independence of X and Y ,


In the denominator, P(X + Y = n) can be expanded using the total probability theorem and the independence of X and Y :


Note that we only get non-zero probability for i = 1, . . . , n − 1 since X and Y are geometric random variables.

The desired result is obtained by combining the computations above and using the geometric

Page 4 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

PMF explicitly:


4. (a) Since P(A) > 0, we can show independence through P(B) = P(B | A):


Therefore, A and B are independent.

- (b) Let C be the event “3 heads in the first 4 tosses” and let D be the event “2 heads in the last 3 tosses”. Since there are no overlap in tosses in C and D, they are independent:


- (c) Let E be the event “4 heads in the first 7 tosses” and let F be the event “2nd head occurred during 4th trial”. We are asked to find P(F | E) = P(F ∩ E)/P(E). The event F ∩ E occurs if there is 1 head in the first 3 trials, 1 head on the 4th trial, and 2 heads in the last 3 trials. Thus, we have


Alternatively, we can solve this by counting. We are given that 4 heads occurred in the first 7 tosses. Each sequence of 7 trials with 4 heads is equally probable, the discrete uniform

Page 5 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

probability law can be used here. There are �47<sup>�</sup> outcomes in E. For the event E ∩ F , there are �13� ways to arrange 1 head in the first 3 trials, 1 way to arrange the 2nd head in the 4th trial and �23<sup>�</sup> ways to arrange 2 heads in the first 3 trials. Therefore,


- (d) Let G be the event “5 heads in the first 8 tosses” and let H be the event “3 heads in the last 5 tosses”. These two events are not independent as there is some overlap in the tosses (the 6th, 7th, and 8th tosses). To compute the probability of interest, we carefully count all the disjoint, possible outcomes in the set G ∩ H by conditioning on the number of heads in the 6th, 7th, and the 8th tosses. We have

   - P(G ∩ H) = P(G ∩ H | 1 head in tosses 6–8)P(1 head in tosses 6–8) + P(G ∩ H | 2 heads in tosses 6–8)P(2 heads in tosses 6–8) + P(G ∩ H | 3 heads in tosses 6–8)P(3 heads in tosses 6–8)


5. Let Ik be the reward paid at time k. We have


Computing E[R] is immediate because


The variance calculation is not as easy because the Iks are not all independent:


Page 6 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)


G1<sup>†</sup> . (a) We know that IA is a random variable that maps a 1 to the real number line if ω occurs within an event A and maps a 0 to the real number line if ω occurs outside of event A. A similar argument holds for event B. Thus we have,


If the random variables, A and B, are independent, we have P(A ∩ B) = P(A)P(B). The indicator random variables, IA and IB, are independent if, PIA,IB (x, y) = PIA(x)PIB (y) We know that the intersection of A and B yields.


We also have,


(b) If X = IA, we know that


†Required for 6.431; optional for 6.041

Page 7 of 7

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
