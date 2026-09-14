---
title: 10 Independence
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/02-exam-quiz02-revi.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 Independence

**Source:** `exams/02-exam-quiz02-revi.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let X be a continuous RV and A be an event with P (A) > 0,

By definition,

X, Y independent ⇔ fX,Y (x, y) = fX (x)fY (y) ∀(x, y) If X and Y are independent:

- E[XY ]=E[X]E[Y ]

- g(X) and h(Y ) are independent

- E[g(X)h(Y )] = E[g(X)]E[h(Y )]

⎧ fX (x) if x ∈ A = P (X∈A) fX|A(x) ⎨ 0 otherwise ⎩ = P (X ∈ B|X ∈ A) fX|A(x)dx �B = E[X|A] xfX|A(x)dx �−∞∞ = E[g(X)|A] g(x)fX|A(x)dx �−∞∞

11

12

If A1, . . . , An are disjoint events that form a partition of the sample space, n = fX (x) � P (Ai)fX|Ai(x) (≈ total probability theorem) i=1 n = E[X] � P (Ai)E[X|Ai] (total expectation theorem) i=1 n E[g(X)] = � P (Ai)E[g(X)|Ai] i=1

13

Total Expectation Theorem:


14


<!-- Start of picture text -->
13 Continuous Bayes’ Rule<br>X, Y continuous RV, N discrete RV, A an event.<br>fX|Y (x|y) = fY |X ( y|x)f ∞ |X(y|x)fX (x)<br>fY (y) X (x) = �−∞ f YfY |X (y|t)fX (t)dt<br>= P (A)fY |A(y) P (A)fY |A(y)<br>P (A|Y = y)<br>fY (y) = fY |A(y)P (A) + fY |Ac(y)P (Ac)<br>P (N = n|Y = y) = pN (n f )f Y Y ( | y N ) (y|n) = � pN i p(Nn)(fi)Yf|YN|(Ny(|yn|)i)<br><!-- End of picture text -->

15

16

---

[← 11 Conditioning on an event](08-11-conditioning-on-an-event.md) · [Up: contents](index.md) · [14 Derived distributions 15 Convolution →](10-14-derived-distributions-15-convolution.md)
