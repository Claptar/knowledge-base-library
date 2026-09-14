---
title: 03 solutions tut03 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/03-solutions-tut03-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 03 solutions tut03 sol

**Source:** `solutions/03-solutions-tut03-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Tutorial 3: Solutions

1. In general we have that E[aX + bY + c] = aE[X] + bE[Y ] + c. Therefore,


For the case of independent random variables, we have that if Z = a · X + b · Y , then


Therefore, var(Z) = 4 · var(X) + 9 · var(Y ).

2. See online solutions.

3. (a) We can find c knowing that the probability of the entire sample space must equal 1.


Therefore, c = 201 . (b) pY (2) = �3x=1<sup>pX,Y(x,2) = 2c+ 0 + 4c= 6c=</sup> 103<sup>.</sup> (c) Z = Y X<sup>2</sup>


pX `|` Y (x | 2) =<sup>pX,Y</sup> pY (2)<sup>(x,2)</sup> . Therefore,


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (d) Yes. Given X ̸ = 2, the distribution of X is the same given Y = y. P(X = x | Y = y, X ̸ = 2) = P(X = x | X ̸ = 2). For example,

   - 1

   - P(X = 1 | Y = 1, X ̸ = 2) = P(X = 1 | Y = 3, X ̸ = 2) = P(X = 1 | X ≠ 2) = 3


Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
