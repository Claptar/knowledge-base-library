---
title: 1.1 t -densities
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureThree153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.1 t -densities

**Source:** [`LectureThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThree153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We first look at the univariate case.

#### **1.1.1 Univariate** _t_ **-density**

The _t_ -density is obtained by changing the scale of a normally distributed random variable through an independent chi-squared distributed random variable. More precisely, suppose _X_ has the _N_ ( _µ, σ_<sup>2</sup> ) distribution. First write

_X_ = _µ_ + ( _X − µ_ ) _._

3

Now consider an independent random variable _V_ such that


Recall that _χ_<sup>2</sup> _v_<sup>isthesameastheGamma(</sup><sup>_v/_2</sup><sup>_,_1</sup><sup>_/_2)distributionsothat</sup>


We now change the scale of _X_ using _V_ to create a new random variable _T_ by


The distribution of _T_ will be denoted by _tv_ ( _µ.σ_<sup>2</sup> ) (here _v_ is known as the degrees of freedom). The density of _T_ can be derived as follows:


Observe now that

so that

As a result

The change of variable

now leads to

Therefore the density corresponding to the _tv_ ( _µ, σ_<sup>2</sup> ) distribution is proportional to


It is useful to note that when the degrees of freedom _v_ is large, the distribution _tv_ ( _µ, σ_<sup>2</sup> ) is very close to the normal distribution _N_ ( _µ, σ_<sup>2</sup> ). There are many ways of seeing this. One way is to note that the mean and variance of _V ∼ χ_<sup>2</sup> _v_<sup>aregivenby</sup><sup>_v_and2</sup><sup>_v_respectively.</sup> This implies that


Thus when _v_ is large, the random variable<sup>_<u>V</u>_</sup> _v_<sup>hasmean1andverysmallvariancesothat</sup><sup>_<u>V</u>_</sup> _v_ will be very close to 1 with very high probability. As a result, the scale change by ~~�~~ _V/v_ in (4) has little effect so that _T_ will have the same distribution as _X ∼ N_ ( _µ, σ_<sup>2</sup> ).

4

---

[← Spring 2025, UC Berkeley](01-spring-2025-uc-berkeley.md) · [Up: contents](index.md)
