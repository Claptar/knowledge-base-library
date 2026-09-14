---
title: 4 Lecture Four
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Lecture Four

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last class, we studied the model


for the sunspots dataset. We used a Bayesian method to infer the frequency parameter _ω_ (which is the main parameter of interest) and this led to an estimated period of close to 11 (which is often cited as the period of the solar cycle). Note however that (13) is not ideal for the sunspots dataset for at least two reasons: (a) the fit to the data is not very good (some of the oscillations have a much higher amplitude than that explained by the single sinusoid), (b) data generated from the model (13) look much more “noisy” compared to the actual sunspots data. Starting with these observations, Yule (1927) proposed an alternative model that is also based on a single sinuosoid. This is the topic of this lecture.

Yule started with the following basic observation. Let _st_ denote the sinusoid:


The same sinusoid can be understood as the solution to a specific difference equation. To derive the difference equation, let us first note that, in continuous time, _s_ ( _t_ ) satisfies


In discrete time (where _t ∈{. . . , −_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _, . . . }_ ), the sequence (14) satisfies the following difference equation that is analogous to (15):


To see this, note that

_st_ +2 _−_ 2 _st_ +1 + _st_

= _α_ 1 (cos( _ω_ ( _t_ + 2)) _−_ 2 cos( _ω_ ( _t_ + 1)) + cos( _ωt_ )) + _α_ 2 (sin( _ω_ ( _t_ + 2)) _−_ 2 sin( _ω_ ( _t_ + 1)) + sin( _ωt_ )) Writing _A_ = _ω_ ( _t_ + 1) and _B_ = _ω_ , we get

cos( _ω_ ( _t_ + 2)) _−_ 2 cos( _ω_ ( _t_ + 1)) + cos( _ωt_ ) = cos( _A_ + _B_ ) _−_ 2 cos _A_ + cos( _A − B_ )


and similarly

sin( _ω_ ( _t_ + 2)) _−_ 2 sin( _ω_ ( _t_ + 1)) + sin( _ωt_ ) = 2(cos _ω −_ 1) sin( _ω_ ( _t_ + 1))

This proves

_st_ +2 _−_ 2 _st_ +1 + _st_ = 2(cos _ω −_ 1) ( _α_ 1 cos( _ω_ ( _t_ + 1)) + _α_ 2 sin( _ω_ ( _t_ + 1))) = 2(cos _ω −_ 1)( _st_ +1 _− µ_ ) and this proves (16).

17

The converse is also true in the sense that every solution _{st}_ to the difference equation (16) say, for _t_ = 0 _,_ 1 _,_ 2 _, . . ._ , with given values of _s_ 0 and _s_ 1 (initial conditions) is of the form (14) for some _α_ 1 and _α_ 2. To see this, let _gt_ = _st − µ_ and note that _{gt}_ satisfies


We find _α_ 1 and _α_ 2 such that


matches _gt_ for _t_ = 0 _,_ 1. Now if _gt_ = _ht_ and _gt_ +1 = _ht_ +1, then


Using this for _t_ = 0 _,_ 1 _,_ 2 _, . . ._ proves that (14) is the unique solution to (16).

To summarize, an alternative way of describing a sinusoid of frequency _ω_ is via the difference equation (16) which is equivalent to


Based on this equation, Yule proposed the model:


with two parameters _θ_ and _c_ (and the additional noise parameter _σ_ in _Zt_ +2 i.i.d _∼ N_ (0 _, σ_<sup>2</sup> )). Note that this is also a single sinusoid plus noise model but now the noise is in a different place. To better understand the difference between (17) and the earlier model:


consider the following physical situation where sinusoids naturally arise (see e.g., page 2 of the Fourier Analysis book by Stein and Shakarchi). Consider a mass _m_ that is attached to a horizontal spring, which itself is attached to fixed wall, and assume that the system lies on a frictionless surface. Choose an axis whose origin coincides with the center of the mass when the spring is neither compressed or stretched. When the spring is compressed or stretched and released, the mass undergoes simple harmonic motion.

Let _y_ ( _t_ ) denote the displacement of the mass at time _t_ . Hooke’s law says that the force exerted by the spring on the mass is given by _F_ = _−κy_ ( _t_ ) where _κ >_ 0 is the spring constant. By Newton’s law (note that the acceleration is given by _y_<sup>_′′_</sup> ( _t_ )), we have


This is same as


18

whose general solution is the sinusoid _α_ 1 cos( _ωt_ ) + _α_ 2 sin( _ωt_ ). In the context of this physical situation, the two different sinusoid plus models ((18) and (17)) can be understood as follows. We are taking measurements of the displacement _Yt_ at various times _t_ .

**Model** (18): Here our measurements are noisy and every measurement is corrupted by an unknown noise which we are terming _ϵt_ and modeling as _N_ (0 _, σ_<sup>2</sup> ).

**Model** (17): Here there is no measurement error and our measurement mechanism is perfect. However the actual oscillation of the mass is not perfectly sinusoidal and is affected by noise. For example, imagine, as Yule put it, that some kids are randomly throwing stones at the mass (sometimes from the left and sometimes from the right) while it is oscillating.

It is very interesting to note that observations generated from Model (17) are much smoother compared to observations generated from Model (18). Yule used this to argue that (17) is a better model for the sunspots data compared to (18).

It is natural to wonder if it makes sense to incorporate both kinds of errors simultaneously (measurement errors and errors affecting the oscillation). This leads to the model:


This is a state space model if we take the state variable to be


because the state evolution


is Markov, and the observations are


### **4.1 The Autoregressive Model**

Yule (1927) also fit models to the sunspots dataset that are more complicated compared to (17) and introduced the Autoregressive Model (of order 2) in this process. The AR(2) model is given by


Note that (17) can be seen as a simpler version of the above model where the _φ_ 2 parameter is set to the value _−_ 1. We can fit this model to the observed sunspots data _y_ 1 _, . . . , yT_ to obtain parameter estimates _c,_ ˆ _φ_<sup>ˆ</sup> 1 _, φ_<sup>ˆ</sup> 2 and _σ_ ˆ of the model parameters. Using the fitted model, future values can be predicted by recursing the equation:


with _YT_ and _YT −_ 1 set to the observed values _yT_ and _yT −_ 1 respectively. For the sunspots data, these predictions follow a _damped_ sinusoid. Indeed, fitting the AR(2) model to the sunspots data for the time period 1700 _−_ 1969 led to the model:


19

which gives the prediction equation:


for the future values of sunspot numbers from 1970 onwards. This equation can also be written as


Thus the predictions for _Ut_ := _Yt −_ 77 _._ 16 are given by recursing the equation:


for _t_ = _T_ +1 _, T_ +2 _, . . ._ (note that _UT −_ 1 and _UT_ are observed from the data). It follows from the following fact that the general solution of (20) is of the form:


for two constants _c_ 1 and _c_ 2. The above is clearly a damped sinusoid (the sinusoid cos (0 _._ 59 _t_ + _c_ 2) is damped by the factor (1 _._ 2)<sup>_−t_</sup> ).

**Fact 4.1.** _Consider the difference equation_


_with initial conditions Uk−_ 1 = _α and Uk_ = _β. Suppose that the quadratic polynomial_


_has complex roots z_ 1 _and z_ 2 _. As φ_ 1 _and φ_ 2 _are real, z_ 1 _and z_ 2 _must be complex conjugates of each other so they can be written as re_<sup>_iθ_</sup> _and re_<sup>_−iθ_</sup> _for some r >_ 0 _and θ ∈_ R _(here i_ =<sup>_√_</sup> _−_ 1 _). Then the solution to_ (21) _is of the form:_


_for some constants c_ 1 _and c_ 2 _._

_Proof._ Let _Ht_ = _c_ 1 _r_<sup>_−t_</sup> cos ( _θt_ + _c_ 2). We find _c_ 1 and _c_ 2 such that _Ht_ = _Ut_ for _t_ = _k −_ 1 and _t_ = _k_ . Then observe that


This gives


because 1 _− φ_ 1 _z_ 1 _− φ_ 2 _z_ 1<sup>2=1</sup><sup>_−φ_1</sup><sup>_z_2</sup><sup>_−φ_2</sup><sup>_z_</sup> 2<sup>2=0as</sup><sup>_z_1and</sup><sup>_z_2arerootsofthepolynomial</sup> 1 _−φ_ 1 _z−φ_ 2 _z_<sup>2</sup> . Thus _Ht_ satisfies the given difference equation and it matches _Ut_ for _t_ = _k−_ 1 _, k_ which implies that it matches _Ut_ for all _t ≥ k_ + 1.

20

### **4.2 Recommended Reading for Today**

1. A very nice account of Yule’s influential 1927 paper is Chapter 6 of the 2011 book “The Foundations of Modern Time Series Analysis” by T. C. Mills. (available for free from the library website).

2. Section 3.4 of the Durbin-Koopman book writes ARMA and ARIMA models in state space form.

---

[← 3 Lecture Three](04-3-lecture-three.md) · [Up: contents](index.md) · [5 Lecture Five →](06-5-lecture-five.md)
