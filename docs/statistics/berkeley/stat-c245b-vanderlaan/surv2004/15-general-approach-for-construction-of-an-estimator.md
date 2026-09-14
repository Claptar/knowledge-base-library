---
title: General Approach for Construction of an Estimator
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# General Approach for Construction of an Estimator

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **Our Model**

We observe _X_ 1 _, . . . , Xn_ i.i.d. observations of _X ∼ P ∈M_ .

The parameter of interest is a function of the actual distribution of the data. In other words, a parameter of the distribution of the data mapped from the model to the outcome space.

_θ ◦M → D_ (e.g., _D_ might be the euclidean space)

So in particular, we can ask – what is the parameter value of the Truth?

_θ_ 0 = _θ_ ( _P_ 0) (10)

But we already have a mapping from the data generating distribution to the truth so we can use the empirical distribution.

Let _Pn_ be the empirical distribution. Let _φ_ be a mapping defined on any P, in particular _Pn_ s.t.

_φ_ ( _P_ ) = _θ_ ( _p_ ) _, P ∈M_

22

We wish to find an extension of that parameter s.t. it applies to the empirical distribution. Now we can estimate _θ_ 0 with substitution estimator


### **Example**

Suppose _X ∼ fθ_ 0, _θ_ 0 _∈_ Θ _⊂_ IR<sup>_K_</sup> . For model identifiability, let _θ_ 0 be a parameter of interest of _fθ_ 0. Define _θ_ ( _P_ ) = arg max _θ∈_ Θ � _Logfθ_ ( _x_ ) _dP_ ( _x_ ).

Note: if we plug in

---

[← 1 Censored Data and Model Selection](14-1-censored-data-and-model-selection.md) · [Up: contents](index.md) · [Log Likelihood – Maximum Likelihood →](16-log-likelihood-maximum-likelihood.md)
