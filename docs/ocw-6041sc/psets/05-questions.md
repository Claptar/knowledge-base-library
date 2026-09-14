---
title: 05 questions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 05 questions

**Source:** `psets/05-questions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

Problem Set 5 Due October 18, 2010

1. Random variables X and Y are distributed according to the joint PDF


   - (a) Evaluate the constant a.

   - (b) Determine the marginal PDF fY (y).

   - (c) Determine the expected value of X1<sup>, given thatY=</sup> 2<sup>3.</sup>

2. Paul is vacationing in Monte Carlo. The amount X (in dollars) he takes to the casino each evening is a random variable with the PDF shown in the figure. At the end of each night, the amount Y that he has on leaving the casino is uniformly distributed between zero and twice the amount he took in.


<!-- Start of picture text -->
fX(x )<br>x (dollars)<br>40<br><!-- End of picture text -->

- (a) Determine the joint PDF fX,Y (x, y). Be sure to indicate what the sample space is.

- (b) What is the probability that on any given night Paul makes a positive profit at the casino? Justify your reasoning.

- (c) Find and sketch the probability density function of Paul’s profit on any particular night, Z = Y − X. What is E[Z]? Please label all axes on your sketch.

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

3. X and Y are continuous random variables. X takes on values between 0 and 2 while Y takes on values between 0 and 1. Their joint pdf is indicated below.


<!-- Start of picture text -->
1<br>0.8  fX,Y (x, y) = 2 1 fX,Y (x, y) = 2 3<br>0.6<br>0.4<br>0.2<br>0<br>0  0.2  0.4  0.6  0.8  1  1.2  1.4  1.6  1.8  2<br>x<br>y<br><!-- End of picture text -->

   - (a) Are X and Y independent? Present a convincing argument for your answer.

   - (b) Prepare neat, fully labelled plots for fX(x), fY |X(y | 0.5), and fX|Y (x | 0.5).

   - (c) Let R = XY and let A be the event X < 0.5. Evaluate E[R | A].

   - (d) Let W = Y − X and determine the cumulative distribution function (CDF) of W .

4. Signal Classification: Consider the communication of binary-valued messages over some transmission medium. Specifically, any message transmitted between locations is one of two possible symbols, 0 or 1. Each symbol occurs with equal probability. It is also known that any numerical value sent over this wire is subject to distortion; namely, if the value X is transmitted, the value Y received at the other end is described by Y = X + N where the random variable N represents additive noise that is independent of X. The noise N is normally distributed with mean µ = 0 and variance σ<sup>2</sup> = 4.

   - (a) Suppose the transmitter encodes the symbol 0 with the value X = −2 and the symbol 1 with the value X = 2. At the other end, the received message is decoded according to the following rules:

      - If Y ≥ 0, then conclude the symbol 1 was sent.

      - If Y < 0. then conclude the symbol 0 was sent.

Determine the probability of error for this encoding/decoding scheme. Reduce your calcu­ lations to a single numerical value.

- (b) In an effort to reduce the probability of error, the following modifications are made. The transmitter encodes the symbols with a repeated scheme. The symbol 0 is encoded with the vector X = [−2, −2, −2]<sup>⊺</sup> and the symbol 1 is encoded with the vector X = [2, 2, 2]<sup>⊺</sup> . The vector Y = [Y1, Y2, Y3]<sup>⊺</sup> received at the other end is described by Y = X + N . The vector N = [N1, N2, N3]<sup>⊺</sup> represents the noise vector where each Ni is a random variable assumed to be normally distributed with mean µ = 0 and variance σ<sup>2</sup> = 4. Assume each Ni is independent of each other and independent of the Xi’s. Each component value of Y is decoded with the same rule as in part (a). The receiver then uses a majority rule to determine which symbol was sent. The receiver’s decoding rules are:

   - If 2 or more components of Y are greater than 0, then conclude the symbol 1 was sent.

   - If 2 or more components of Y are less than 0, then conclude the symbol 0 was sent.

   - Determine the probability of error for this modified encoding/decoding scheme. Reduce your calculations to a single numerical value.

Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

5. The random variables X and Y are described by a joint PDF which is constant within the unit area quadrilateral with vertices (0, 0), (0, 1), (1, 2), and (1, 1).


<!-- Start of picture text -->
y<br>2<br>1<br>1  2<br>x<br>X  and  Y .  .<br>X  +  Y .  .<br>+  Y .  .<br>1 + sin(2πp),  if  p  ∈  [0, 1],<br>fP (p) =<br>� 0,  otherwise.<br><!-- End of picture text -->

   - (a) Are X and Y independent?

   - (b) Find the marginal PDFs of X and Y .  .

   - (c) Find the expected value of X + Y .  .

   - (d) Find the variance of X + Y .  .

6. A defective coin minting machine produces coins whose probability of heads is a random variable P with PDF

In essence, a specific coin produced by this machine will have a fixed probability P = p of giving heads, but you do not know initially what that probability is. A coin produced by this machine is selected and tossed repeatedly, with successive tosses assumed independent.

   - (a) Find the probability that the first coin toss results in heads.

   - (b) Given that the first coin toss resulted in heads, find the conditional PDF of P .

   - (c) Given that the first coin toss resulted in heads, find the conditional probability of heads on the second toss.

- G1<sup>†</sup> . Let C be the circle {(x, y) | x<sup>2</sup> +y<sup>2</sup> ≤ 1}. A point a is chosen randomly on the boundary of C and another point b is chosen randomly from the interior of C (these points are chosen independently and uniformly over their domains). Let R be the rectangle with sides parallel to the x- and y-axes with diagonal ab. What is the probability that no point of R lies outside of C?

†Required for 6.431; optional for 6.041

Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
