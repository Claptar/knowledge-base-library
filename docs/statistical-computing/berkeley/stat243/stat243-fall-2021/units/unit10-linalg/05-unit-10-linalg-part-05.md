---
title: Unit 10 — linalg Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 10 — linalg Part 05 —

**Source:** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This means we have no information about the overall level of _y_ . So how would we generate sample _y_ vectors? We can’t put infinite variance on the constant basis vector and still generate samples. Instead we use the pseudo-inverse and assign ZERO variance to the constant basis vector. This corresponds to generating realizations under the constraint that<sup>�</sup> _yi_ has no variation, i.e., � _yi_ = _y_ ¯ = 0 - you can see this by seeing that Var(Γ _⊤·i_<sup>_y_) = 0 when</sup><sup>_λi_= 0.</sup>

_# generate a realization_ e$values[1:4] <- 1 / e$values[1:4] y <- e$vec %*% ( **sqrt** (e$values) * **rnorm** (5)) **sum** (y) ## [1] -3.774758e-15

In the second order case, we have two non-identifiabilities: for the sum and for the linear component of the variation in _y_ (linear in the indices of _y_ ).

I could parameterize a statistical model as _µ_ + _y_ where _y_ has covariance that is the generalized inverse discussed above. Then I allow for both a non-zero mean and for smooth variation governed

10

by the autoregressive structure. In the second-order case, I would need to add a linear component as well, given the second non-identifiability.

### **2.5 Matrices arising in regression**

In regression, we work with _X_<sup>_⊤_</sup> _X_ . Some properties of this matrix are that it is symmetric and non-negative definite (hence our use of ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> in the OLS estimator). When is it not positive definite?

Fitted values are _Xβ_<sup>ˆ</sup> = _X_ ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ = _HY_ . The “hat” matrix, _H_ , projects _Y_ into the column space of _X_ . _H_ is idempotent: _HH_ = _H_ , which makes sense - once you’ve projected into the space, any subsequent projection just gives you the same thing back. _H_ is singular. Why? Also, under what special circumstance would it not be singular?

---

[← Unit 10 — linalg Part 04 —](04-unit-10-linalg-part-04.md) · [Up: contents](index.md) · [3 Computational issues →](06-3-computational-issues.md)
