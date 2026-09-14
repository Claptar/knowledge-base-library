---
title: Variance
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/01-exam-quiz01-revi.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Variance

**Source:** `exams/01-exam-quiz01-revi.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The expected value of a derived random variable _g_ ( _X_ ) is **E** [ _g_ ( _X_ )] = � _g_ ( _x_ ) _pX_ ( _x_ ) _x_

The variance of _X_ is calculated as _• var_ ( _X_ ) = **E** [( _X −_ **E** [ _X_ ])<sup>2</sup> ] = � _x_ ( _x −_ **E** [ _X_ ])<sup>2</sup> _pX_ ( _x_ ) _• var_ ( _X_ ) = **E** [ _X_<sup>2</sup> ] _−_ **E** [ _X_ ]<sup>2</sup> _• var_ ( _aX_ + _b_ ) = _a_<sup>2</sup> _var_ ( _X_ ) Note that _var_ ( _x_ ) _≥_ 0

18 / 26

Quiz I Review

Multiple Random Variables Let _X_ and _Y_ denote random variables defined on a sample space Ω.


<!-- Start of picture text -->
• The joint PMF of X and Y is denoted by<br>pX ,Y ( x, y ) = P � {X = x} ∩{Y = y } �<br>• The marginal PMFs of X and Y are given<br>respectively as<br>pX ( x ) = � pX ,Y ( x, y )<br>y<br>pY ( y ) = � pX ,Y ( x, y )<br>x<br><!-- End of picture text -->

19 / 26

Quiz I Review

Functions of Multiple Random Variables Let _Z_ = _g_ ( _X , Y_ ) be a function of two random variables _•_ **PMF:**


_•_ **Expectation:**


_•_ **Linearity:** Suppose _g_ ( _X , Y_ ) = _aX_ + _bY_ + _c_ . **E** [ _g_ ( _X , Y_ )] = _a_ **E** [ _X_ ] + _b_ **E** [ _Y_ ] + _c_

20 / 26

Quiz I Review

---

[← Expectation](17-expectation.md) · [Up: contents](index.md) · [Conditioned Random Variables →](19-conditioned-random-variables.md)
