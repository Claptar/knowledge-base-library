---
title: Regression-based models
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Regression-based models

**Source:** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
M N<br>2<br>= −<br>= RSS X Y<br>Y X + ε ( )<br>g ∑ β t , g t ∑∑ i , j i , j<br>t ∈ T j = 1 i = 1<br>g<br>Problems:<br><!-- End of picture text -->

Standard regression will produce many very small values of β, which makes interpretation difficult

β values can be unstable to changes in training data Solutions:

Subset Selection and Coefficient Shrinkage •see Section 3.4 of Hastie Tibshirani and Friedman “The elements of statistical learning” for  general approaches and “TIGRESS: Trustful Inference of Gene REgulation using Stability Selection” for a successful DREAM challenge doi: 10.1186/17520509-6-145.

118

---

[← Regression-based models](51-regression-based-models.md) · [Up: contents](index.md) · [Outline →](53-outline.md)
