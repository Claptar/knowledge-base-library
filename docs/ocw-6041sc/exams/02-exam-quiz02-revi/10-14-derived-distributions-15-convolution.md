---
title: 14 Derived distributions 15 Convolution
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/02-exam-quiz02-revi.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 Derived distributions 15 Convolution

**Source:** `exams/02-exam-quiz02-revi.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Def: PDF of a function of a RV X with known PDF: Y = g(X). Method:


<!-- Start of picture text -->
• Get the CDF:<br>FY (y) = P (Y ≤ y) = P (g(X) ≤ y) = fX (x)dx<br>�x|g(x)≤y<br>• Differentiate: fY (y) = dF dy Y (y)<br>Special case: if Y = g(X) = aX + b, fY (y) = |a 1 | fX ( x− a b )<br><!-- End of picture text -->

W = X + Y , with X, Y independent.

• Discrete case: pW (w) = � pX(x)pY (w − x) x • Continuous case: ∞ fW (w) = fX (x)fY (w − x) dx �−∞

17

18

---

[← 10 Independence](09-10-independence.md) · [Up: contents](index.md) · [16 Law of iterated expectations →](11-16-law-of-iterated-expectations.md)
