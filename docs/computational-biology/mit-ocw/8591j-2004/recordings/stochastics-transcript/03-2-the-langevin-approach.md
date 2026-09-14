---
title: 2. THE LANGEVIN APPROACH
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/stochastics-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. THE LANGEVIN APPROACH

**Source:** `recordings/stochastics-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

An alternate approach that allows for a more straightforward interpretation and scales easily to different levels of detail is the use of a Langevin equation. The Langevin approach consists essentially of adding a noise term to the deterministic equations. This noise term can represent the effect of the intrinsic fluctuations [20] or the external inputs of the system [21].

For _x_ , the concentration of some chemical species,

_x_ & = _f_ ( _x_ ) → _x_ & = _f_ ( _x_ ) + _q_ ( _x_ )ε( _t_ ) ,

where the random variable ε( _t_ )  is determined by its statistical properties. Formally, this can be any random process, but in practice we assume white-noise statistics, which will give approximate values for the first two moments. The conditions for white noise are:


where denotes an ensemble average. Since we are interested in the steady state fluctuations, we will assume the coefficient of the noise term to be constant<sup>3</sup> , i.e. evaluated at _x_ .

_ss_ .

For the case of our basic model of the single gene, we have two macroscopic equations representing mRNA and protein creation, respectively:


> 2 This can be summarized in a very practical way [13] in terms of the logarithmic gains to obtain an equation which reflects the resulting components of the noise.

> 3 For the case where _q(x)_ is not constant, the stochastic differential equation will be understood to follow the Stratonovich interpretation [19,22]. This allows a general Fokker-Planck equation to be written in this form, but will not be necessary in the cases of interest.

8

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

where the coefficients of the noise terms are to be determined. Clearly, _r_ = _k R_ /γ _R_ and _p_ = _k P r_ /γ _P_ from the condition of zero mean for the noise term.

The difference with the steady state δ _r_ = _r_ − _r_ follows the equation


Fourier transforming, we obtain


so after multiplying by the complex conjugate and taking the average,


The steady state fluctuations are given by the inverse Fourier transform with _t_ = 0<sup>4</sup> :


But since the production of mRNA is in this model a single step, independent random process, it has a Poisson distribution, so the variance equals the mean, which implies


For the number of proteins, we have


ˆ<sup>*</sup> ˆ* but in this case we also need to notice that δ _r_ ˆ( _w_ )ε _p_ = δ _r_ ˆ( _w_ ) ε _p_ = 0 , since these are two independent random processes with zero mean. So in this case,


4 From the Wiener-Khintchine theorem; see [23].

9

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004

Using _q r_ 2 = 2 _k R_ and _q p_ 2 = 2 _k_<sup>_k_</sup> _<u>R</u>_ , (since this represents the internal noise and for a _p_ γ _R_ fixed number of mRNAs the production of proteins is also a Poissonian process). Performing the inverse transform<sup>5</sup> ,


This is identical to the result obtained by the master equation. This method can be readily generalized for many interacting genes when the system is fluctuating around a steady state. As an example, we will analyze the case where one gene represses a second gene. Let _y0_ , _y1_ be the protein numbers of each gene, and let _f( y0)_ be the rate of creation of the second protein as a function of the first. This means that the equations describing this system are


Note that the equations include the entire process of producing a protein, so mRNA levels are no longer explicitly calculated. Including the Langevin noise term and looking at the fluctuations from steady state,


linearization is valid at each stable point, but not for transitions between different stable points or for limit cycles. For very small numbers _n_ of chemicals this also breaks down, because since this processes are mostly Poissonian, the fluctuations are of order _n_ so a Taylor expansion might not be valid. Fourier transforming and taking the square and the average as before, we get


10

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004


The correlation between the genes can also be calculated, from


where the term εˆ1 δ _y_ ˆ 0 * vanishes because the fluctuations in the first gene are

independent from the internal fluctuations in the second gene. In many cases, the decay time will be determined primarily by the dilution time, so it will be the same for all genes. This assumption simplifies the expressions that are obtained upon transforming back:


where the irrational part of the integral vanishes because of parity. From our previous results we know that for a single gene,


where _bi_ is the burst size for gene _i._ For basic Hill-type repression,


where _k1+B1_ is the maximum creation rate, _Y1/2_ is the half induction point, _h_ is the Hill coefficient and _B1_ is the basal transcription level. Assuming that the internal noise for the second gene alone has the same form,

11

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden and Mukund Thattai – MIT– October 2004


the variance and correlation can be explicitly written as


Note that we need the parameters of the macroscopic equations plus an “internal” parameter for each gene, _bi_ = _k Pi_ /γ _Ri_ which depends on the parameters of the macroscopic equations for each gene.

12

---

[← Degradation](02-degradation.md) · [Up: contents](index.md)
