---
title: 03 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 03 slides

**Source:** `recitations/03-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

Recitation 3: September 16, 2010

1. Example 1.20, page 37 in the text.

Consider two independent fair coin tosses, in which all four possible outcomes are equally likely. Let


   - (a) Are the events H1 and H2 (unconditionally) independent?

   - (b) Given event D has occurred, are the events H1 and H2 (conditionally) independent?

2. Imagine a drunk tightrope walker, in the middle of a really long tightrope, who manages to keep his balance, but takes a step forward with probability p and takes a step back with probability (1 − p).

   - (a) What is the probability that after two steps the tightrope walker will be at the same place on the rope?

   - (b) What is the probability that after three steps, the tightrope walker will be one step forward from where he began?

   - (c) Given that after three steps he has managed to move ahead one step, what is the probability that the first step he took was a step forward?

3. Problem 1.31, page 60 in the text.

Communication through a noisy channel. A binary (0 or 1) message transmitted through a noisy communication channel is received incorrectly with probability ǫ0 and ǫ1, respectively (see the figure). Errors in different symbol transmissions are independent. The channel source transmits a 0 with probability p and transmits a 1 with probability 1 − p.


<!-- Start of picture text -->
 1-e0<br>0  0<br>e0<br>e1<br>1  1<br>1-e1<br><!-- End of picture text -->

Figure 1: Error probabilities in a binary communication channel.

- (a) What is the probability that a randomly chosen symbol is received correctly?

- (b) Suppose that the string of symbols 1011 is transmitted. What is the probability that all the symbols in the string are received correctly?

Page 1 of 2

Textbook problems are courtesy of Athena Scientific, and are used with permission.

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

   - (c) In an effort to improve reliability, each symbol is transmitted three times and the received symbol is decoded by majority rule. In other words, a 0 (or 1) is transmitted as 000 (or 111, respectively), and it is decoded at the receiver as a 0 (or 1) if and only if the received three-symbol string contains at least two 0s (or 1s, respectively). What is the probability that a transmitted 0 is correctly decoded?

   - (d) Suppose that the scheme of part (c) is used. What is the probability that a 0 was transmitted given that the received string is 101?

4. (a) Can an event A be independent of itself?

   - (b) Problem 1.43(a) on page 63 in text.

      - Let A and B be independent events. Use the definition of independence to prove that the events A and B<sup>c</sup> are independent.

   - (c) Problem 1.44 on page 64 in text.

Let A, B, and C be independent events, with P(C) > 0. Prove that A and B are condi­ tionally independent of C.

Page 2 of 2

Textbook problems are courtesy of Athena Scientific, and are used with permission.

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
