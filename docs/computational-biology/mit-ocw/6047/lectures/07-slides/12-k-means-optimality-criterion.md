---
title: K-means Optimality Criterion
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# K-means Optimality Criterion

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**We can think of K-means as trying to create clusters that minimize a cost criterion associated with the size of the cluster** 2 m **1** m **3** COST  **x** 1, **x** 2, **x** 3,..., **x** n     **x** i  **μ** _k_  **μ** _k_ **x** _i_ with label k m **2 To achieve this, minimize each cluster term separately:** 2 2 2 2 _k_ 2   **x** i  **μ** _k_    **x** i  2 **x u** _i k_  **μ** _k_   **x** i  **u** _k_  2 **x** _i_  **x u** _k_ **x** _i_ with label k **x** _i_ with label k

**x** _<u>i</u>_ Optimum **u** _k_ =  _k_ , the centroid **x** _i_ with label k **x**

**However: Some points can be almost halfway between two centers**  **Assign partial weights**

**Fuzzy K-means**

18

---

[← K-means update rules](11-k-means-update-rules.md) · [Up: contents](index.md) · [Fuzzy K-means update rule →](13-fuzzy-k-means-update-rule.md)
