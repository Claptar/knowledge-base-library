---
title: Bayesian Networks
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bayesian Networks

**Source:** `lectures/14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Complete joint probability tables are large and often unknown

- N binary variables = 2<sup>N</sup> states

– only one constraint (sum of all probabilities =1)

=> 2<sup>N</sup> - 1 parameters

77

Graphical Structure Expresses our Beliefs


<!-- Start of picture text -->
P1-P2<br>REAL<br><!-- End of picture text -->

Cause  (often “hidden”)


<!-- Start of picture text -->
Detected  Detected<br>…<br>by X1  by Xn  Effects (observed)<br><!-- End of picture text -->

78


<!-- Start of picture text -->
Graphical Structure Expresses our<br>P1-P2  P1-P2<br>Beliefs<br>REAL  REAL<br>Highly<br>Membrane<br>expressed<br>Detected  Detected<br>…<br>by X1  by Xn<br>Detected  Detected  Detected  Detected<br>by X1  …  by Xj  by Xj+1  …  by Xn<br><!-- End of picture text -->

79


<!-- Start of picture text -->
Graphical Structure Expresses our<br>P1-P2  P1-P2<br>Beliefs<br>REAL  REAL<br>Highly<br>Membrane<br>expressed<br>Detected  Detected<br>…<br>by X1  by Xn<br>Detected  Detected  Detected  Detected<br>by X1  …  by Xj  by Xj+1  …  by Xn<br>Naïve Bayes assumes all  But some observations<br>observations are  may be coupled.<br>independent<br><!-- End of picture text -->


80

Graphical Structure Expresses our **P1-P2 P1-P2** Beliefs **REAL REAL**

**P1-P2 REAL** Highly Membrane expressed **Detected Detected Detected Detected by X1 … by Xj by Xj+1 … by Xn**


**Detected Detected … by X1 by Xn**

• The graphical structure can be decided in advance based on knowledge of the system or learned from the data.

81

---

[← Bayesian Networks](38-bayesian-networks.md) · [Up: contents](index.md) · [Graphical Structure →](40-graphical-structure.md)
