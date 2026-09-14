---
title: 3 AR Models for the Sunspots Data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSixteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 AR Models for the Sunspots Data

**Source:** [`LectureSixteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSixteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For the sunspots dataset, we previously employed the model


We used a Bayesian method to infer the frequency parameter _f_ (which is the main parameter of interest) and this led to an estimated period of close to 11 years (which is often cited as the period of the solar cycle). Note however that (2) is not ideal for the sunspots dataset for at least two reasons: (a) the fit to the data is not very good (some of the oscillations have a much higher amplitude than that explained by the single sinusoid), (b) data generated from the model (2) look much more “noisy” compared to the actual sunspots data. Starting with these observations, Yule [1] proposed an alternative model that is also based on a single sinuosoid. This alternative model is based on the idea of AR modeling.

Yule started with the following basic observation. Let _st_ denote the sinusoid:


The same sinusoid can be understood as the solution to a specific _difference equation_ . To derive the difference equation, let us first note that, in continuous time, _s_ ( _t_ ) satisfies


In discrete time (where _t ∈{. . . , −_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _, . . . }_ ), the sequence (3) satisfies the following difference equation that is analogous to (4):


2

To see this, note that (below we take _ω_ = 2 _πf_ for notational simplicity)


Writing _A_ = _ω_ ( _t −_ 1) and _B_ = _ω_ , we get

cos( _ωt_ ) _−_ 2 cos( _ω_ ( _t −_ 1)) + cos( _ω_ ( _t −_ 2)) = cos( _A_ + _B_ ) _−_ 2 cos _A_ + cos( _A − B_ )


and similarly

sin( _ωt_ ) _−_ 2 sin( _ω_ ( _t −_ 1)) + sin( _ω_ ( _t −_ 2)) = 2(cos _ω −_ 1) sin( _ω_ ( _t −_ 1)) _._

This proves


thereby establishing (5).

The converse is also true in the sense that every solution _{st}_ to the difference equation (5) say, for _t_ = 1 _,_ 2 _,_ 3 _, . . ._ , with given values of _s_ 1 and _s_ 2 (initial conditions) is of the form (3) for some _β_ 1 and _β_ 2. To see this, let _gt_ = _st − β_ 0 and note that _{gt}_ satisfies


We find _β_ 1 and _β_ 2 such that (note again that _ω_ = 2 _πf_ )


matches _gt_ for _t_ = 1 _,_ 2. Now if _gt−_ 1 = _ht−_ 1 and _gt−_ 2 = _ht−_ 2, then


Verify that


and


which gives


We thus proved that if _gt−_ 1 = _ht−_ 1 and _gt−_ 2 = _ht−_ 2, then _gt_ = _ht_ . Using this for _t_ = 1 _,_ 2 _, . . ._ proves that (3) is the unique solution to (5).

To summarize, an alternative way of describing a sinusoid of frequency _ω_ = 2 _πf_ is via the difference equation (5) which is equivalent to


3

Based on this equation, Yule proposed the model:


i.i.d with two parameters _ϕ_ 0 and _ϕ_ 1 (and the additional noise parameter _σ_ in _ϵt ∼ N_ (0 _, σ_<sup>2</sup> )). Note that (6) is also a single sinusoid plus noise model but now the noise is in a different place.

To better understand the difference between (6) and the earlier model (2), consider the following physical situation where sinusoids naturally arise (see e.g., page 2 of the Fourier Analysis book by Stein and Shakarchi). Consider a mass _m_ that is attached to a horizontal spring, which itself is attached to fixed wall, and assume that the system lies on a frictionless surface. Suppose that _β_ 0 is the location of the center of the mass when the spring is neither compressed or stretched. When the spring is compressed or stretched and released, the mass undergoes simple harmonic motion.

Let _s_ ( _t_ ) denote the position of the mass at time _t_ . Hooke’s law says that the force exerted by the spring on the mass is given by _F_ = _−κ_ ( _s_ ( _t_ ) _− β_ 0) where _κ >_ 0 is the spring constant. By Newton’s law (note that the acceleration is given by _s_<sup>_′′_</sup> ( _t_ )), we have


This is same as


whose general solution is the sinusoid _s_ ( _t_ ) = _β_ 0+ _β_ 1 cos( _ωt_ )+ _β_ 2 sin( _ωt_ ). In the context of this physical situation, the two different noisy sinusoid models ((2) and (6)) can be understood as follows. We are taking measurements of the displacement _yt_ at various times _t_ .

**Model** (2): Here our measurements are noisy and every measurement is corrupted by an unknown noise which we are terming _ϵt_ and modeling as _N_ (0 _, σ_<sup>2</sup> ).

**Model** (6): Here there is no measurement error and our measurement mechanism is perfect. However the actual oscillation of the mass is not perfectly sinusoidal and is affected by noise. For example, imagine, as Yule put it, that some kids are randomly throwing stones at the mass (sometimes from the left and sometimes from the right) while it is oscillating.

It is very interesting to note that observations generated from Model (6) are much smoother compared to observations generated from Model (2). Yule used this to argue that (6) is a better model for the sunspots data compared to (2).

The AR(2) model is:


(6) can be seen as a simpler version of the above model where the _ϕ_ 2 parameter is set to the value _−_ 1. Yule fit both models ((6) and (7)) to the sunspots dataset. It is interesting that these two models give different predictions for future sunspots values: (6) gives sinusoidal predictions while (7) gives _damped_ sinusoidal predictions. In the coming lectures, we shall discuss how different parameter settings for AR models lead to different predictions.

A very nice account of Yule’s influential 1927 paper is Chapter 6 of the 2011 book “The Foundations of Modern Time Series Analysis” by T. C. Mills. (available for free from the library website). Yule’s paper [1] itself is available freely online.

4

---

[← 2 AR (Auto-Regressive) Models](02-2-ar-auto-regressive-models.md) · [Up: contents](index.md) · [References →](04-references.md)
