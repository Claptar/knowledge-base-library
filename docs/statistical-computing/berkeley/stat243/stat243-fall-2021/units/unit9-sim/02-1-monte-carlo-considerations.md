---
title: 1 Monte Carlo considerations
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit9-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit9-sim.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Monte Carlo considerations

**Source:** [`units/unit9-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit9-sim.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Motivating example**

Let’s consider linear regression, with observations _Y_ = ( _y_ 1 _, y_ 2 _, . . . , yn_ ) where _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> _Y_ . If we know that we have _EY_ = _Xβ_ and Var( _Y_ ) = _σ_<sup>2</sup> _I_ , then we can determine analytically that we have


where _Y_<sup>_∗_</sup> is some new observation we’d like to predict given _X_<sup>_∗_</sup> .

But suppose that we’re interested in the properties of regression estimation when in reality the mean is not linear in _X_ or the properties of the errors are more complicated than having independent homoscedastic errors. Or suppose we have a modified procedure to produce _β_<sup>ˆ</sup> , such as a procedure that is robust to outliers. In those cases, we cannot compute the expectations above analytically.

Instead we decide to use a Monte Carlo estimate. To keep the notation more simple, let’s just consider one element of the vector _β_ (i.e., one of the regression coefficients) and continue to call that _β_ . If we randomly generate _m_ different datasets from some distribution _f_ , and _β_<sup>ˆ</sup> _i_ is the estimated coefficient based on the _i_ th dataset: _Yi_ = ( _yi_ 1 _, yi_ 2 _, . . . , yin_ ), then we can estimate _Eβ_<sup>ˆ</sup> under that distribution _f_ as


Or to estimate the variance, we have


In evaluating the performance of regression under non-standard conditions or the performance of

2

our robust regression procedure, what decisions do we have to make to be able to carry out our Monte Carlo procedure?

Next let’s think about Monte Carlo methods in general.

### **1.2 Monte Carlo basics**

#### **1.2.1 Monte Carlo overview**

The basic idea is that we often want to estimate _φ ≡ Ef_ ( _h_ ( _Y_ )) for _Y ∼ f_ . Note that if _h_ is an indicator function, this includes estimation of probabilities, e.g., for a scalar _Y_ , we have _p_ = _P_ ( _Y ≤ y_ ) = _F_ ( _y_ ) = � _−∞y_<sup>_f_(</sup><sup>_t_)</sup><sup>_dt_=</sup> � _I_ ( _t ≤ y_ ) _f_ ( _t_ ) _dt_ = _Ef_ ( _I_ ( _Y ≤ y_ )). We would estimate variances or MSEs by having _h_ involve squared terms.

We get an MC estimate of _φ_ based on an iid sample of a large number of values of _Y_ from _f_ :


which is justified by the Law of Large Numbers:


Note that in most simulation studies, _Y_ is an entire dataset, and the “iid sample” means generating _m_ different datasets from _f_ , i.e., _Yi ∈{Y_ 1 _, . . . , Ym}_ not _m_ different scalar values. If the dataset has _n_ observations, then _Yi_ = ( _Yi_ 1 _, . . . , Yin_ ).

**Back to the regression example** Let’s relate that back to our regression example. In that particular case, if we’re interested in whether the regression estimator is biased, we want to know:


We can use the Monte Carlo estimate of _φ_ :


For the variance, we have


3

and we can use the Monte Carlo estimate of _φ_ :


where


Finally note that we also need to use the Monte Carlo estimate of _Eβ_<sup>ˆ</sup> in the Monte Carlo estimation of the variance.

We might also be interested in the coverage of a confidence interval. In that case we have


and we can estimate the coverage as


Of course we want that _φ_<sup>ˆ</sup> _≈_ 1 _− α_ for a 100(1 _− α_ ) confidence interval. In the standard case of a 95% interval we want _φ_<sup>ˆ</sup> _≈_ 0 _._ 95.

#### **1.2.2 Simulation uncertainty**

Since _φ_<sup>ˆ</sup> is simply an average of _m_ identically-distributed values, _h_ ( _Y_ 1) _, . . . , h_ ( _Ym_ ), the simulation variance of _φ_<sup>ˆ</sup> is Var( _φ_<sup>ˆ</sup> ) = _σ_<sup>2</sup> _/m_ , with _σ_<sup>2</sup> = Var( _h_ ( _Y_ )). An estimator of _σ_<sup>2</sup> = _Ef_ (( _h_ ( _Y_ ) _− φ_ )<sup>2</sup> ) is


So our MC simulation error is based on


� Note that� this is particularly confusing if we have _φ_<sup>ˆ</sup> = Var( _β_<sup>ˆ</sup> ) because then we have Var<sup>�</sup> ( _φ_<sup>ˆ</sup> ) = Var�(Var( _β_<sup>ˆ</sup> ))!

The simulation variance is _O_ ( _m_<sup><u>1</u>)becausewehave</sup><sup>_m_2inthedenominatorandasumover</sup><sup>_m_</sup> terms in the numerator.

Note that in the simulation setting, the randomness in the system is very well-defined (as it is in survey sampling, but unlike in most other applications of statistics), because it comes from the

4

RNG that we perform as part of our attempt to estimate _φ_ . Happily, we are in control of _m_ , so in principle we can reduce the simulation error to as little as we desire. Unhappily, as usual, the standard error goes down with the square root of _m_ .

**Back to the regression example** Some examples of simulation variances we might be interested in in the regression example include:

-

- • Uncertainty in our estimate of bias: Var<sup>�</sup> ( _E_ ( _β_<sup>ˆ</sup> ) _− β_ ).

-

- • Uncertainty in the estimated variance of the estimated coefficient: Var<sup>�</sup> (Var( _β_<sup>ˆ</sup> ))

- Uncertainty in the estimated mean square prediction error: Var<sup>�</sup> (MSPE�( _Y_<sup>_∗_</sup> ))

In all cases we have to estimate the simulation variance, hence the Var<sup>�</sup> () notation.

#### **1.2.3 Final notes**

Sometimes the _Yi_ are generated in a dependent fashion (e.g., sequential MC or MCMC), in which case this variance estimator, Var<sup>�</sup> ( _φ_<sup>ˆ</sup> ) does not hold because the samples are not IID, but the estimator _φ_ ˆ is still a valid, unbiased estimator of _φ_ .

### **1.3 Variance reduction (optional)**

There are some tools for variance reduction in MC settings. One is importance sampling (see Section 3). Others are the use of control variates and antithetic sampling. I haven’t personally run across these latter in practice, so I’m not sure how widely used they are and won’t go into them here.

In some cases we can set up natural strata, for which we know the probability of being in each stratum. Then we would estimate _µ_ for each stratum and combine the estimates based on the probabilities. The intuition is that we remove the variability in sampling amongst the strata from our simulation.

Another strategy that comes up in MCMC contexts is _Rao-Blackwellization_ . Suppose we want to know _E_ ( _h_ ( _X_ )) where _X_ = _{X_ 1 _, X_ 2 _}_ . Iterated expectation tells us that _E_ ( _h_ ( _X_ )) = _E_ ( _E_ ( _h_ ( _X_ ) _|X_ 2). If we can compute _E_ ( _h_ ( _X_ ) _|X_ 2) = � _h_ ( _x_ 1 _, x_ 2) _f_ ( _x_ 1 _|x_ 2) _dx_ 1 then we should avoid introducing stochasticity related to the _X_ 1 draw (since we can analytically integrate over that) and only average over stochasticity from the _X_ 2 draw by estimating _EX_ 2( _E_ ( _h_ ( _X_ ) _|X_ 2). The estimator is


5

where we either draw from the marginal distribution of _X_ 2, or equivalently, draw _X_ , but only use _X_ 2. Our MC estimator averages over the simulated values of _X_ 2. This is called Rao-Blackwellization because it relates to the idea of conditioning on a sufficient statistic. It has lower variance because the variance of each term in the sum of the Rao-Blackwellized estimator is Var( _E_ ( _h_ ( _X_ ) _|X_ 2), which is less than the variance in the usual MC estimator, Var( _h_ ( _X_ )), based on the usual iterated variance formula: _V_ ( _X_ ) = _E_ ( _V_ ( _X|Y_ )) + _V_ ( _E_ ( _X|Y_ )) _⇒ V_ ( _E_ ( _X|Y_ )) _< V_ ( _X_ ).

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Design of simulation studies →](03-2-design-of-simulation-studies.md)
