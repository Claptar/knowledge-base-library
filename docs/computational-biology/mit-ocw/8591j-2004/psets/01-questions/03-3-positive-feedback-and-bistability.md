---
title: 3. Positive feedback and bistability
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Positive feedback and bistability

**Source:** `psets/01-questions.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose the protein _X_ be a transcriptional activator, and _D_ a promoter which is activated by the binding of _X_ . If the downstream gene happens to code for _X_ itself, the resulting positive feedback can lead to bistability.


<!-- Start of picture text -->
X  X<br>v1  v0<br>DXAXB  D<br><!-- End of picture text -->

- (10) _a._ Let _v1_ be the rate of expression from bound DNA ( _DXAXB_ ), and _v0_ < _v1_ the rate of expression from free DNA ( _D_ ). Use the results of Problems 1 and 2 to show that the time-evolution of the concentration _x_ ≡ [ _X_ ] may be written in the following form:


(30) _b._ Steady state solutions occur at those values of _x_ for which the rates of generation ( _f(x)_ ) and degradation ( _g(x)_ ) are equal. Set γ = 1 and _K1K2_ = 1, and use the accompanying MATLAB file ps1.m to explore the intersections of _f(x)_ and _g(x)_ as the parameters _v0_ and _v1_ are varied. The figures (i) through (v) show schematically the types of behaviors that can occur. Plot an example each of types (i), (iii) and (v), indicating the parameter values that generated them. Label those values of _x_ for which _f(x)_ > _g(x)_ with a rightward arrow, and those for which _f(x)_ < _g(x)_ with a leftward arrow. Which solutions are stable?


<!-- Start of picture text -->
•<br>•  •<br>•<br>•  •<br>•  •  •<br>(i)  (ii)  (iii)  (iv)  (v)<br><!-- End of picture text -->

(10) _c._ The boundary between bistability and monostability is given by parameters for which the system has precisely two fixed points (types (ii) and (iv)). Setting γ = 1 and _K1K2_ = 1, rewrite the condition _f(x) = g(x)_ as a cubic equation of the form _x_<sup>_3_</sup> _+ c2 x  + c2 1 x + c0 =_ 0. Any cubic can always be factorised as _(x - a1)(x - a2)(x - a3)_ . What are the conditions on the roots that would lead to type (ii) or type (iv) behavior? Apply this condition and compare coefficients to obtain parametrized equations for _v1_ and _v0_ . Show on a graph of _v1_ vs. _v0_ the region over which the system is bistable.

**_FA04_**

2

---

[← 2. Dilution of proteins due to cell growth.](02-2-dilution-of-proteins-due-to-cell-growth.md) · [Up: contents](index.md)
