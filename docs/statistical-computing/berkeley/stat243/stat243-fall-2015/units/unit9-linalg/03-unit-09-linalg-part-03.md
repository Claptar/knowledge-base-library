---
title: Unit 09 — linalg Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit9-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit9-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — linalg Part 03 —

**Source:** [`units/unit9-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit9-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This means we have no information about the overall level of _y_ . So how would we generate sample _y_ vectors? We can’t put infinite variance on the constant basis vector and still generate samples. Instead we use the pseudo-inverse and assign ZERO variance to the constant basis vector. This corresponds to generating realizations under the constraint that � _yi_ has no variation, i.e., � _yi_ = _y_ ¯ = 0 - you can see this by seeing that Var(Γ _⊤·i_<sup>_y_) = 0 when</sup><sup>_λi_= 0.</sup>

_# generate a realization_ e$values[1:4] <- 1 / e$values[1:4] y <- e$vec %*% ( **sqrt** (e$values) * **rnorm** (5)) **sum** (y) ## [1] 6.106227e-15

In the second order case, we have two non-identifiabilities: for the sum and for the linear component of the variation in _y_ (linear in the indices of _y_ ).

I could parameterize a statistical model as _µ_ + _y_ where _y_ has covariance that is the generalized inverse discussed above. Then I allow for both a non-zero mean and for smooth variation governed by the autoregressive structure. In the second-order case, I would need to add a linear component as well, given the second non-identifiability.

### **1.12 Matrices arising in regression**

In regression, we work with _X_<sup>_⊤_</sup> _X_ . Some properties of this matrix are that it is symmetric and non-negative definite (hence our use of ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> in the OLS estimator). When is it not positive definite?

Fitted values are _Xβ_<sup>ˆ</sup> = _X_ ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ = _HY_ . The “hat” matrix, _H_ , projects _Y_ into the column space of _X_ . _H_ is idempotent: _HH_ = _H_ , which makes sense - once you’ve projected into the space, any subsequent projection just gives you the same thing back. _H_ is singular. Why? Also, under what special circumstance would it not be singular?

9

---

[← 1 Preliminaries](02-1-preliminaries.md) · [Up: contents](index.md) · [2 Computational issues →](04-2-computational-issues.md)
