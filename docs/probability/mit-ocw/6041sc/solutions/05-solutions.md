---
title: 05 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/05-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 05 solutions

**Source:** `solutions/05-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

Problem Set 5: Solutions

1. (a) Because of the required normalization property of any joint PDF,


so a = 3/2.


and fY (y) = 0 otherwise.

(c) First notice that for 1 ≤ x ≤ 3/2,


Therefore,


2. (a) By definition fX,Y (x, y) = fX(x)fY |X(y | x). fX(x) = ax as shown in the graph. We have that


So fX(x) = x/800. From the problem statement fY |X(y | x) = 21x<sup>fory∈[0, 2x]. Therefore,</sup>


- (b) Paul makes a positive profit if Y > X. This occurs with probability


We could have also arrived at this answer by realizing that for each possible value of X, there is a 1/2 probability that Y > X.

- (c) The joint density function satisfies fX,Z(x, z) = fX(x) fZ|X(z|x). Since Z is conditionally uniformly distributed given X, fZ|X(z | x) = 21x<sup>for−x≤z≤x. Therefore,fX,Z(x, z)=</sup> 1/1600 for 0 ≤ x ≤ 40 and −x ≤ z ≤ x. The marginal density fz(z) is calculated as


Page 1 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

3. (a) In order for X and Y to be independent, any observation of X should not give any information on Y . If X is observed to be equal to 0, then Y must be 0.

   - In other words, fY |{X=0}(y | 0) = fY (y). Therefore, X and Y are not independent.


<!-- Start of picture text -->
1.5<br>1<br>0.5<br>0<br>0  0.2  0.4  0.6  0.8  1  1.2  1.4  1.6  1.8  2<br>x<br>2<br>1.8<br>1.6<br>1.4<br>1.2<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1<br>y<br>1.5<br>1<br>0.5<br>0<br>0  0.2  0.4  0.6  0.8  1  1.2  1.4  1.6  1.8  2<br>x<br>()f xX<br>(| 5)f 0y |YX.<br>(| 5)f 0x |XY.<br><!-- End of picture text -->

- (c) The event A leaves us with a right triangle with a constant height. The conditional PDF is then 1/area = 8. The conditional expectation yields:


- (d) The CDF of W is FW (w) = P(W ≤ w) = P(Y − X ≤ w) = P(Y ≤ X + w). P(Y ≤ X + w) can be computed by integrating the area below the line Y = X + w for all possible values of w. The lines Y = X + w are shown below for w = 0, w = −1/2, w = −1 and w = −3/2. The probabilities of interest can be calculated by taking advantage of the uniform PDF over the two triangles. Remember to multiply the areas by the appropriate joint density fX,Y (x, y)! Take note that there are 4 regions of interest: w < −2, −2 ≤ w ≤−1, −1 < w ≤ 0 and w > 0.

Page 2 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)


<!-- Start of picture text -->
1.2  w  = 0 y  = 2 − x<br>1<br>w  ∈  (−1, 0)<br>0.8 y  = x −w  −2w w  = −1<br>0.6<br>w  ∈  (−2, −1)<br>0.4<br>1 + w<br>0.2<br>2+w<br>2<br>0<br>1 + w  2 + w<br>−0.2<br>0  0.2  0.4  0.6  0.8  1  1.2  1.4  1.6  1.8  2<br>x<br>y<br><!-- End of picture text -->

The CDF of W is


As a sanity check, FW (−∞) = 0 and FW (+∞) = 1. Also, FW (w) is continuous at w = −2 and at w = −1.

4. (a) If the transmitter sends the 0 symbol, the received signal is a normal random variable with a mean of −2 and a variance of 4. In other words, fY |X(y | −2) = N (−2, 4). Also, fY |X(y | 2) = N (2, 4) These conditional pdfs are shown in the graph below.

Page 3 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)


<!-- Start of picture text -->
0.25<br>fY |X (y  | −2) fY |X (y  | 2)<br>0.2  P(error | X  = −2)<br>P(error | X  = 2)<br>0.15<br>0.1<br>0.05<br>0<br>−8  −6  −4  −2  0  2  4  6  8<br><!-- End of picture text -->

The probability of error can be found using the total probability theorem.


- (b) With 3 components, the probability of error given an obervation of X is the probability of decoding 2 or 3 of the components incorrectly. For each component, the probability of error is 0.1587. Therefore,


By symmetry, P(error | sent 1) = P(error | sent 0).

Therefore, P(error) = P(error | sent 0)P(sent 0) + P(error | sent 1)P(sent 1) = 0.0676.

5. (a) There are many ways to show that X and Y are not independent. One of the most intuitive arguments is that knowing the value of X limits the range of Y , and vice versa. For instance, if it is known in a particular trial that X ≥ 1/2, the value of Y in that trial cannot be smaller

Page 4 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

than 1/2. Another way to prove that the two are not independent is to calculate the product of their expectations, and show that this is not equal to E[XY ].

(b) Applying the definition of a marginal PDF,

for 0 ≤ x ≤ 1,


for 0 ≤ y ≤ 1,


and for 1 ≤ y ≤ 2,


<!-- Start of picture text -->
1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0  0.2  0.4  0.6  0.8  1<br>x<br>()f xX<br><!-- End of picture text -->


<!-- Start of picture text -->
1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0  0.2  0.4  0.6  0.8  1  1.2  1.4  1.6  1.8  2<br>y<br>()f yY<br><!-- End of picture text -->

- (c) By linearity of expectation, the expected value of a sum is the sum of the expected values. By inspection, E[X] = 1/2 and E[Y ] = 1.

Thus, E[X + Y ] = E[X] + E[Y ] = 3/2.

Page 5 of 7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

(d) The variance of X + Y is


In part (c), E[X+Y ] was computed, so only the other three expressions need to be calculated. First, the expected value of X<sup>2</sup> :


Also, the expected value of Y<sup>2</sup> is


Finally, the expected value of XY is


Substituting these into (1), we get var(X + Y ) = 1/3 + 7/6 + 7/6 − 9/4 = 5/12.

*Alternative (shortcut) solution to parts (c) and (d)*

Given any value of X (in ([0,1]), we observe that Y − X takes values between 0 and 1, and is uniformly distributed. Since the conditional distribution of Y − X is the same for every value of X in [0,1], we see that Y − X independent of X. Thus: (a) X is uniform, and (b) Y = X + U , where U is also uniform and independent of X. It follows that E[X + Y ] = E[2X + U ] = 3/2. Furthermore, var(X + Y ) = 4 var(X) + var(U ) = 5/12.

6. (a) Let A be the event that the first coin toss resulted in heads. To calculate the probability P(A), we use the continuous version of the total probability theorem:


which after some calculation yields


(b) Using Bayes rule,


Page 6 of 7

# Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

(c) Let B be the event that the second toss resulted in heads. We have


After some calculation, this yields


G1<sup>†</sup> . Let a = (cos θ, sin θ) and b = (bx, by). We will show that no point of R lies outside C if and only if


The other two vertices of R are (cos θ, by) and (bx, sin θ). If |bx| ≤| cos θ| and |by| ≤| sin θ|, then each vertex (x, y) of R satisfies x<sup>2</sup> + y<sup>2</sup> ≤ cos<sup>2</sup> θ + sin<sup>2</sup> θ = 1 and no points of R can lie outside of C. Conversely if no points of R lie outside C, then applying this to the two vertices other than a and b, we find


which is equivalent to 2.

These conditions imply that (bx, by) lies inside or on C, so for any given θ, the probability that the random point b = (bx, by) satisfies (2) is


and the overall probability is


†Required for 6.431; optional for 6.041

Page 7 of 7

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
