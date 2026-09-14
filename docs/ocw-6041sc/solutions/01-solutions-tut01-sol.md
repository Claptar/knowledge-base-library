---
title: 01 solutions tut01 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/01-solutions-tut01-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 solutions tut01 sol

**Source:** `solutions/01-solutions-tut01-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Tutorial 1 Solutions September 16/17, 2010

1. If A ⊂ B, then P(B ∩ A) = P(A) But we know that in order for A and B to be independent, P(B∩A) = P(A)P(B). Therefore, A and B are independent if and only if P(B) = 1 or P(A) = 0. This could happen, for example, if B is the universe or if A is empty.

2. This problem is similar in nature to Example 1.24, page 40. In order to compute the success probability of individual sub-systems, we make use of the following two properties, derived in that example:

   - If a serial sub-system contains m components with success probabilities p1, p2...pm, then the probability of success of the entire sub-system is given by

P(whole system succeeds) = p1p2p3...pm

- If a parallel sub-system contains m components with success probabilities p1, p2...pm, then the probability of success of the entire sub-system is given by

P(whole system succeeds) = 1 − (1 − p1)(1 − p2)(1 − p3)...(1 − pm)


Let P(X → Y ) denote the probability of a successful connection between node X and Y. Then,


The probabilities P(C → D), P(D → E) can be similarly computed as


The probability of success of the entire system can be obtained by substituting the subsystem success probabilities:


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

3. The Chess Problem.

   - (a) i. P(2nd Rnd Req) = (0.6)<sup>2</sup> + (0.4)<sup>2</sup> = 0.52 ii. P(Bo Wins 1st Rnd) = (0.6)<sup>2</sup> = 0.36

      - iii. P(Al Champ) = 1 − P(Bo Champ) − P(Ci Champ) = 1 − (0.6)<sup>2</sup> ∗ (0.5)<sup>2</sup> − (0.4)<sup>2</sup> ∗ (0.3)<sup>2</sup> = 0.8956

   - (b) i. P(Bo Challenger|2nd Rnd Req) =<sup><u>(</u></sup> 0<sup>0</sup> .<sup>.</sup> 52<sup>6)2</sup> = 0<sup><u>0</u></sup> .<sup><u>.36</u></sup> 52 = 0.6923 ii. P(Al Champ|2nd Rnd Req)

         - = P(Al Champ|Bo Challenger, 2nd Rnd Req) × P(Bo Challenger|2nd Rnd Req) + P(Al Champ|Ci Challenger, 2nd Rnd Req) × P(Ci Challenger|2nd Rnd Req)

         - = (1 − (0.5)<sup>2</sup> ) × 0.6923 + (1 − (0.3)<sup>2</sup> ) × 0.3077 = 0.7992

   - <u>(0.6)</u><sup>2</sup> ∗(0.5)

   - (c) P((Bo Challenger)|{(2nd Rnd Req) ∩ (One Game)}) = (0.6)2∗(0.5)+(0.4)2∗(0.7) = <u>(0.6)</u><sup>2</sup> <u>(0.5)</u> = 0.6164 0.2920

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
