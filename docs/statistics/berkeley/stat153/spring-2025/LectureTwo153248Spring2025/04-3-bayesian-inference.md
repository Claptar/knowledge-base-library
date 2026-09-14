---
title: 3 Bayesian Inference
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwo153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Bayesian Inference

**Source:** [`LectureTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwo153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The first step is to select a prior for the unknown parameters _β_ 0 _, β_ 1 _, σ_ . A reasonable prior reflecting ignorance is


for a large number _C_ (the exact value of _C_ will not matter in the following calculations). Note that as _σ_ is always positive, we have made the uniform assumption on log _σ_ (by the change of variable formula, the density of _σ_ would be given by _fσ_ ( _x_ ) = _f_ log _σ_ (log _x_ ) _x_<sup><u>1</u>=</sup> _I{−C<_ 2 _Cx_ log _x<C}_ =<sup>_I{e−C_</sup> 2<sup>_<x<e_</sup> _Cx_<sup>_C_</sup><sup>_<u>}</u>_</sup> .

The joint posterior for all the unknown parameters _β_ 0 _, β_ 1 _, σ_ is then given by (below we write the term “data” for _y_ 1 _, . . . , yn_ ):

_fβ_ 0 _,β_ 1 _,σ|_ data( _β_ 0 _, β_ 1 _, σ_ ) _∝ fy_ 1 _,...,yn|β_ 0 _,β_ 1 _,σ_ ( _y_ 1 _, . . . , yn_ ) _fβ_ 0 _,β_ 1 _,σ_ ( _β_ 0 _, β_ 1 _, σ_ ) _._

3

The two terms on the right hand side above are the likelihood:


and the prior:


We thus obtain


The above is the joint posterior over _β_ 0 _, β_ 1 _, σ_ . The posterior over only the main parameters _β_ 0 _, β_ 1 can be obtained by integrating (or marginalizing) the parameter _σ_ . We shall do this in the next lecture.

4

---

[← 2 Frequentist Inference](03-2-frequentist-inference.md) · [Up: contents](index.md)
