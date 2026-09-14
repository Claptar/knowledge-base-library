---
title: 'Special setting: Doubly stochastic chains'
source: https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_8_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Special setting: Doubly stochastic chains

**Source:** [`lecture_8_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_8_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

By definition a transition matrix **P** has the property _pij ≥_ 0 _∀i, j_ and the _stochastic matrix_ property


A matrix that has the extra property


is called **doubly stochastic** . Given a doubly stochastic transition matrix on _n_ states, it is clear that the uniform distribution _πi_ = 1 _/n ∀i_ is a stationary distribution.

**Example: asymmetric RW on** _n_ **-cycle.** [board]

**Example: card-shuffling models.** [board]

David Aldous Lecture 8


**Special setting: success runs.** Here the states are _{_ 0 _,_ 1 _,_ 2 _, . . .}_ and the transition probabilities are of the form _pi,i_ +1 = _qi , pi,_ 0 = 1 _− qi_

where 0 _< qi <_ 1.

Here we calculate [board]


Here we are assuming<sup>�</sup><sup>_∞_</sup> _j_ =0<sup>_sj< ∞_.</sup>

David Aldous Lecture 8

---

[← Stationary distributions](02-stationary-distributions.md) · [Up: contents](index.md) · [Special setting: detailed balance. →](04-special-setting-detailed-balance.md)
