---
title: Nussinov Algorithm Example
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Nussinov Algorithm Example

**Source:** `recitations/2014-03-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We want to fold the following RNA   sequence: **AAGUUCG**

- (1) Write the sequence along the top and le= side of the matrix

- (2) IniLalize the diagonal of the matrix and one-­‐below to zero

- (3) Fill in _i,   j_<sup>th</sup> entries according to

_S_ ( _i_ + 1, _j_ – 1) +1 [if _i_ , _j_ base pair] _S_ ( _i_ + 1, _j_ ) _S_ ( _i_ , _j_ ) = max S( _i_ , _j_ – 1) max **_i_ <** **_k_ <** **_j_** _S_ ( _i_ , _k_ ) + _S_ ( _k_ + 1, _j_ )

23

---

[← Nussinov algorithm](18-nussinov-algorithm.md) · [Up: contents](index.md) · [Nussinov Algorithm -­‐ iniLalizaLon →](20-nussinov-algorithm---inilalizalon.md)
