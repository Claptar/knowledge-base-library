---
title: Convergence in Distribution
source: https://vanderlaan-lab.org/teach-files/stat210b.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/stat210b.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Convergence in Distribution

**Source:** [`stat210b.pdf`](https://vanderlaan-lab.org/teach-files/stat210b.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that the Glivenko-Cantelli property can be thought of as a uniform law of large numbers over _F_ . Once we have established a uniform law of large numbers, we might also wonder if we can establish a uniform version of the Central Limit Theorem, but first we have to talk about what that could even mean.

For a single random variable _f_ ( _O_ ) _∈ L_<sup>2</sup> ( _P_ ), the Central Limit Theorem teaches us that<sup>_√_</sup> _<u>n</u>_ <u>(</u> _n_<sup><u>1</u></sup> � _f_ ( _Oi_ ) _− EP f_ ) = _⇒ N_ (0 _, varP_ ( _f_ )), but what does it mean for this to hold uniformly over _F_ . In empirical process theory, we are interested in showing that _Gn_ = _⇒ G_ in ( _l_<sup>_∞_</sup> ( _F_ ) _, ∥· ∥F_ ), which says that the empirical process converges to the _P_ -Brownian Bridge, when both are viewed as random functions from _F_ to _R_ .

A naive way of defining convergence in distribution would be to say that _Gn_ = _⇒ G_ if the finite-dimensional distributions ( _Gn_ ( _f_ 1) _, ..., Gn_ ( _fk_ )) converged in distribution to ( _G_ ( _f_ 1) _, ..., G_ ( _fk_ )) for all ( _f_ 1 _, ..., fk_ ) _∈F_ . However, there are many properties of a random function that are not determined by its finite dimensional distributions, so this naive definition is insufficient. Instead, we define convergence in distribution as follows, in a way that generalizes the usual definition for real-valued random variables.

_Definition_ : If _Xn, X_ are random elements of a normed space ( _D, ∥· ∥_ ), we say that _Xn_ converges in distribution to _X_ (denoted _Xn_ = _⇒ X_ ) if for every bounded continuous function _g_ from ( _D, ∥· ∥_ ) to _R_ , _E_ [ _g_ ( _Xn_ )] _→ E_ [ _g_ ( _X_ )].

---

[← Glivenko-Cantelli Classes](02-glivenko-cantelli-classes.md) · [Up: contents](index.md) · [Donsker Classes →](04-donsker-classes.md)
