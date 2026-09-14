---
title: 13 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/13-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 13 slides

**Source:** `recitations/13-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

Recitation 13 October 21, 2010

For the problems below, recall the Law of Iterated Expectations and the Law of Total Variance:

E[X] = E [E[X|Y ]]

var(X) = E [var(X|Y )] + var (E[X|Y ]) .

1. Let X, Y , and Z be discrete random variables. Show the following generalizations of the law of iterated expectations.

   - (a) E[Z] = E�E[Z | X, Y ]�. (b) E[Z | X] = E�E[Z | X, Y ] | X�. (c) E[Z] = E�E�E[Z | X, Y ] | X��.

2. Example 4.17, page 223 in text.

We start with a stick of length ℓ. We break it at a point which is chosen randomly and uniformly over its length, and keep the piece that contains the left end of the stick. We then repeat the same process on the piece that we were left with.

   - (a) What is the expected value of the length of the piece that we are left with after breaking twice?

   - (b) What is the variance of the length of the piece that we are left with after breaking twice?

3. Widgets are stored in boxes, and then all boxes are assembled in a crate. Let X be the number of widgets in any particular box, and N be the number of boxes in a crate. Assume that X and N are independent integer-valued random variables, with expected value equal to 10, and variance equal to 16. Evaluate the expected value and variance of T , where T is the total number of widgets in a crate.

Textbook problems are courtesy of Athena Scientific, and are used with permission.

Page 1 of 1

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
