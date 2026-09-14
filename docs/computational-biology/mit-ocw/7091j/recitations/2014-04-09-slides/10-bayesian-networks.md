---
title: Bayesian Networks
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bayesian Networks

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_P_ ( _Ro_ = 1) = 0 _._ 1 Ro Pa **Ro** _P_ ( _Pa_ = 1) = 0 _._ 3 **0 1** 0 _._ 3 **0** _P_ ( _Ti_ = 1 _|Ro, Pa_ ) = **Pa** 0 _._ 5 0 _._ 9 Co Ti 0 _._ 1 � **1 0**<sup>**Ro**</sup> **1** _P_ ( _Co_ = 1 _|Ro_ ) = ⇥0 _._ 1 0 _._ 5⇤ **0**<sup>**Co**</sup> **1** 0 _._ 8 EF _P_ ( _EF_ = 1 _|Ti, Co_ ) = **0   Ti** 0 _._ 4 0 _._ 9 **1** 0 _._ 1 �

What   is   the   probability   that   your   experiment   will   fail   given   that   there   is   a   new   rota'on student,   but   there   was   no   party   last   night?   What   is _P_ ( _EF_ = 1 _|Ro_ = 1 _, Pa_ = 0)   ? _P_ ( _EF_ = 1 _|Ro_ = 1 _, Pa_ = 0) = _P_ ( _EF_ = 1 _, Ti, Co|Ro_ = 1 _, Pa_ = 0) X _T i,Co_ = From   graph _P_ ( _EF_ = 1 _|Ti, Co_ ) _P_ ( _Ti|Ro_ = 1 _, Pa_ = 0) _P_ ( _Co|Ro_ = 1) X structure: _T i,Co_

From   graph structure:

---

[← Bayesian Networks](09-bayesian-networks.md) · [Up: contents](index.md) · [Bayesian Networks →](11-bayesian-networks.md)
