---
title: 3. Gradient sensing
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. Gradient sensing

**Source:** `psets/05-questions.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In problems 1 and 2, we argued that the concentration distribution along the surface of a cell in a linear chemical gradient has the general form _c_ ( θ) = _c_ 0 + _c_ 1 cos(θ ) , with the angle θ measured from the cell’s leading edge. We now calculate how the cell might respond to such a stimulus, based on the receptor activation/inactivation model of Levchenko and Iglesias.

This model assumes that two biochemical species, _A_ and _I_ , are produced in the cell membrane at rates linearly proportional to the extracellular signal concentration _c_ (θ ). The levels of these biochemicals are “read out” by a receptor _R_ whose steady state concentration is given by _rss_ ≈ _a_ / _i_ (where lower case letters represent normalized concentrations). Both _A_ and _I_ undergo first-order decay, and both diffuse along the membrane. The equations describing this system are:


- (15) _a._ First assume a uniform concentration situation: _c_ ( θ) = _c_ 0 . In this case, _a_ and _i_ will be independent of θ . Calculate the steady state values of _a_ , _i_ , and _rss_ = _a_ / _i_ . Now suddenly double the signal concentration to 2 _c0_ . Show that the following expressions satisfy the dynamical equations with the correct initial conditions:


For γ _a_ = 5 and γ _i_ = 1, plot _rss_ ( _t_ ) _= a_ ( _t_ )/ _i_ ( _t_ ). Is the system perfectly adapting?

- (20) _b._ Now assume a linear concentration gradient, so _c_ ( θ) = _c_ 0 + _c_ 1 cos(θ ) . Guess a solution of the form


Substitute these guesses into the dynamical equations and calculate the steady state values of β _a_ and β _i_ . Also write down an expression for _rss_ (θ ).

- (10) _c._ Suppose that _A_ diffuses very slowly, while _I_ diffuses fast. That is,


What is _rss_ (θ ) in this limit?

- (5) _d._ These calculations show that the system is perfectly adapting in uniform concentrations, but polarized in a concentration gradient, matching expeirmental observations. Explain in words how this behavior comes about.

3

FA04

---

[← 2. Cell in a linear concentration gradient](03-2-cell-in-a-linear-concentration-gradient.md) · [Up: contents](index.md)
