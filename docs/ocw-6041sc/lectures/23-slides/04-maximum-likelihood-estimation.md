---
title: Maximum Likelihood Estimation
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Maximum Likelihood Estimation

**Source:** `lectures/23-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Model, with unknown parameter(s): _X ∼ pX_ ( _x_ ; _θ_ )

- Pick _θ_ that “makes data most likely” _θ_<sup>ˆ</sup> ML = arg max _pX_ ( _x_ ; _θ_ ) _θ_

- Compare to Bayesian MAP estimation: _θ_<sup>ˆ</sup> MAP = arg max _θ p_ Θ _|X_<sup>(</sup><sup>_θ| x_)</sup>


- **Example:** _X_ 1 _, . . . , Xn_ : i.i.d., exponential( _θ_ )


   - **Desirable properties of estimators (should hold FOR ALL** _θ_ **!!!)**

   - **Unbiased: E** [Θ<sup>ˆ</sup> _n_ ] = _θ_

-

- exponential example, with _n_ = 1: **E** [1 _/X_ 1] = _∞￿_ = _θ_ (biased)

- **Consistent:** Θ<sup>ˆ</sup> _n → θ_ (in probability)

-

- exponential example: ( _X_ 1 + _· · ·_ + _Xn_ ) _/n →_ **E** [ _X_ ] = 1 _/θ_

- can use this to show that: Θ<sup>ˆ</sup> _n_ = _n/_ ( _X_ 1 + _· · ·_ + _Xn_ ) _→_ 1 _/_ **E** [ _X_ ] = _θ_

- **“Small” mean squared error (MSE) E** [(Θ<sup>ˆ</sup> _− θ_ )<sup>2</sup> ] = var(Θ<sup>ˆ</sup> _− θ_ ) + ( **E** [Θ<sup>ˆ</sup> _− θ_ ])<sup>2</sup> = var(Θ<sup>ˆ</sup> ) + (bias)<sup>2</sup>

1

---

[← Problem types](03-problem-types.md) · [Up: contents](index.md) · [Estimate a mean →](05-estimate-a-mean.md)
