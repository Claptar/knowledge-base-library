---
title: Classification tree with different impurity measures
source: https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/PH240C-Lab02.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Classification tree with different impurity measures

**Source:** [`notes/PH240C-Lab02.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/PH240C-Lab02.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Suppose _Y_ 1 _, . . . , Yn_ are the binary responses in a classification tree;

- We consider a simple scenario that we split the parent node _R_ into two child nodes _R_ 1 and _R_ 2;

- Define the proportion:


- Possible impurity functions calculated in each node, for _j_ = 1 _,_ 2:

   - Entropy function: _E_ ( _Rj_ ) = _−p_ 0( _Rj_ ) log _p_ 0( _Rj_ ) _− p_ 1( _Rj_ ) log _p_ 1( _Rj_ );

   - Gini index: _G_ ( _Rj_ ) = _p_ 0( _Rj_ )(1 _− p_ 0( _Rj_ )) + _p_ 1( _Rj_ )(1 _− p_ 1( _Rj_ ))

- Then the split impurity is calculated via, take Entropy for example:

---

[← Classification and Regression Trees (CART)](02-classification-and-regression-trees-cart.md) · [Up: contents](index.md) · [What if we have some missing values in the response? →](04-what-if-we-have-some-missing-values-in-the-response.md)
