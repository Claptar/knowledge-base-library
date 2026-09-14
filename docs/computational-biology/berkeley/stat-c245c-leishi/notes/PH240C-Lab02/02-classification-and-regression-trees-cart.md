---
title: Classification and Regression Trees (CART)
source: https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/PH240C-Lab02.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Classification and Regression Trees (CART)

**Source:** [`notes/PH240C-Lab02.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **univariate covariate**

**1.** Suppose we have i.i.d. sample with pairs ( _Yi, Xi_ ), _i_ = 1 _, . . . , n_ , and _Xi_ lives in a discrete sample space _Xi ∈X_ = _{x_ 1 _, . . . , xd}_ ;

**2.** For _j_ = 1 : _d_

   - **2.1** Split the data set into two groups:


   - **2.2** Calculate the within group “measure of similarity”:

      - Sum of squares for regression trees (RSS), _s_<sup>2</sup> left<sup>(</sup><sup>_j_)and</sup><sup>_s_2</sup> right<sup>(</sup><sup>_j_);</sup>

      - ▶ Impurity measure for classification trees.

   - **2.3** Calculate the split “quality”:

      - Regression tree – the split total RSS: _s_<sup>2</sup> ( _j_ ) = _<u>|G</u>_ <u>left</u> _n_ <u>(</u> _j_ <u>)</u> _<u>|</u> s_<sup>2</sup> left<sup>(</sup><sup>_j_) +</sup> _|G_ rig _n_ ht( _j_ ) _| s_<sup>2</sup> right<sup>(</sup><sup>_j_);</sup>

      - ▶ Classification tree – the split total weighted impurity;

**3.** Split the data into two groups with threshold that maximize between nodes difference and the within node similarly;

**4.** Keep splitting with in each group following Step 2.

---

[← Classification and Regression Trees (with missingness)](01-classification-and-regression-trees-with-missingness.md) · [Up: contents](index.md) · [Classification tree with different impurity measures →](03-classification-tree-with-different-impurity-measures.md)
