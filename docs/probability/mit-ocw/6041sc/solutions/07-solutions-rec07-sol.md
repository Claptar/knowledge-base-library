---
title: 07 solutions rec07 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/07-solutions-rec07-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 07 solutions rec07 sol

**Source:** `solutions/07-solutions-rec07-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 7 Solutions September 30, 2010

1. See the textbook, Problem 2.35, page 130.

2. (a)


(b) The solution is a sketch of the following conditional PMF:


(c) E[Y | X = 1] =<sup>�</sup> 3y=1<sup>y pY</sup><sup>`|`X(y| 1) = 1 ·</sup> 4<sup>1+ 2·</sup> 2<sup>1+ 3·1</sup> 4<sup>= 2</sup>

- (d) Assume that X and Y are independent. Because pX,Y (3, 1) = 0 and pY (1) = 1/4, pX(3) must equal zero. This further implies pX,Y (3, 2) = 0 and pX,Y (3, 3) = 0. All the remaining probability mass must go to (X, Y ) = (2, 2), making pX,Y (2, 2) = 5/12, pX(2) = 8/12, and pY (2) = 7/12. However, pX,Y (2, 2) = pX(2) · pY (2), contradicting the assumption; thus X and Y are not independent.

   - A simpler explanation uses only two X values and two Y values for which all four (X, Y ) pairs have specified probabilities. Note that if X and Y are independent, then pX,Y (1, 3)/pX,Y (1, 1) and pX,Y (2, 3)/pX,Y (2, 1) must be equal because they must both equal pY (3)/pY (1). This necessary equality does not hold, so X and Y are not independent.

- (e) Knowing that X and Y are conditionally independent given B, we must have


since the (X, Y ) pairs in the equality are all in B. Thus


(f) Since P(B) = 9/12 = 3/4, we normalize to obtain pX,Y `|` B(2, 2) =<sup>pX,Y</sup> P(B<sup>(2</sup> )<sup>,2)</sup> = 4/9.

3. See the textbook, Problem 2.33, page 128.

Page 1 of 1

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
