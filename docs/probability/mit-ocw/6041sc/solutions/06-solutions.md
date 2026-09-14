---
title: 06 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/06-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 solutions

**Source:** `solutions/06-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

Problem Set 6: Solutions

1. Let us draw the region where fX,Y (x, y) is nonzero:


Then,


(d) We use the technique of first finding the CDF and differentiating it to get the PDF.


Page 1 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

2. The PDF of Z, fZ(z), can be readily computed using the convolution integral:


For z ∈ [−1, 0],


For z ∈ [0, 1],

For z ∈ [1, 2],

For z ∈ [2, 3],


For z ∈ [3, 4],


A sketch of fZ (z) is provided below.

3. (a) X1 and X2 are negatively correlated. Intuitively, a large number of tosses that result in a 1 suggests a smaller number of tosses that result in a 2.

   - (b) Let At (respectively, Bt) be a Bernoulli random variable that is equal to 1 if and only if the tth toss resulted in 1 (respectively, 2). We have E[AtBt] = 0 (since At = 0 implies Bt = 0) and


Thus,


Page 2 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

and


The covariance of X1 and X2 is negative as expected.

4. (a) If X takes a value x between −1 and 1, the conditional PDF of Y is uniform between −2 and 2. If X takes a value x between 1 and 2, the conditional PDF of Y is uniform between −1 and 1.

Similarly, if Y takes a value y between −1 and 1, the conditional PDF of X is uniform between −1 and 2. If Y takes a value y between 1 and 2, or between −2 and −1, the conditional PDF of X is uniform between −1 and 1.

- (b) We have


and


It follows that E[X] = 3/10 and var(X) = 193/300.

- (c) By symmetry, we have E[Y | X] = 0 and E[Y ] = 0. Furthermore, var(Y | X = x) is the variance of a uniform PDF (whose range depends on x), and


Using the law of total variance, we obtain


5. First let us write out the properties of all of our random variables. Let us also define K to be the number of members attending a meeting and B to be the Bernoulli random variable describing whether or not a member attends a meeting.


- (a) Since K = B1 + B2 + · · · BN ,


Page 3 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

(b) Let G be the total money brought to the meeting. Then G = M1 + M2 + · · · + MK.


G1<sup>†</sup> . (a) Let X1, X2, . . . Xn be independent, identically distributed (IID) random variables. We note that


It follows from the linearity of expectations that


Because the Xi’s are identically distributed, we have the following relationship.

E[Xi | X1 + · · · + Xn = x0] = E[Xj | X1 + · · · + Xn = x0], for any 1 ≤ i ≤ n, 1 ≤ j ≤ n.

Therefore,


(b) Note that we can rewrite E[X1 | Sn = sn, Sn+1 = sn+1, . . . , S2n = s2n] as follows:


where the last equality holds due to the fact that the Xi’s are independent. We also note that


It follows from the linearity of expectations that


Because the Xi’s are identically distributed, we have the following relationship:


Therefore,


†Required for 6.431; optional for 6.041

Page 4 of 4

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
