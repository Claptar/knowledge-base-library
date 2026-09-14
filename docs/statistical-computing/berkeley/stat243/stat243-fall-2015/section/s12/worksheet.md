---
title: 'Stat243: section 12 practice problem'
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s12/worksheet.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/section/s12/worksheet.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: section 12 practice problem

**Source:** [`section/s12/worksheet.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/section/s12/worksheet.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## November 22, 2015

1. Consider a censored regression problem. We assume a simple linear regression model, _Yi ∼N_ ( _β_ 0 + _β_ 1 _xi, σ_<sup>2</sup> ). Suppose we have an iid sample, but that for any observation with _Y > τ_ , all we are told is that _Y_ exceeded the threshold and not its actual value. In a given sample, _c_ of the _n_ observations will (in a stochastic fashion) be censored, depending on how many exceed the fixed _τ_ . A real world example (but with truncation in the left tail) is in measuring pollutants, for which values below a threshold are reported as below the limit of detection.

   - (a) Design an EM algorithm to estimate the 3 parameters, _θ_ = ( _β_ 0 _, β_ 1 _, σ_<sup>2</sup> ), taking the complete data to be the available data plus the actual values of the truncated observations. You’ll need to make use of _E_ ( _Y |Y > τ_ ) and Var( _Y |Y > τ_ ) where _Y_ is normally distributed. Be careful that you carefully distinguish _θ_ from the current value at iteration _t_ , _θt_ , in writing out the expected log-likelihood and computing the expectation and that your maximization be with respect to _θ_ . You should be able to analytically maximize the expected log likelihood. A couple hints:

      - i. From the Johnson and Kotz bibles on distributions, the mean and variance of the truncated normal distribution, _f_ ( _Y_ ) _∝N_ ( _µ, σ_<sup>2</sup> ) _I_ ( _Y > τ_ ), are:


where _φ_ ( _·_ ) is the standard normal density and Φ( _·_ ) is the standard normal CDF.

   - ii. You should recognize that your expected log-likelihood can be expressed as a regression of _{Yobs, mt}_ on _{x}_ where _Yobs_ are the non-censored data and _{mi,t}, i_ = 1 _, . . . , c_ are used in place of the censored observations. Note that _{mi,t}_ will be functions of _θt_ and thus constant in terms of the maximization step. Your estimator for _σ_<sup>2</sup> should involve a ratio where the numerator involves the usual sum of squares for the non-censored data plus two additional terms that you should interpret statistically.

- (b) Propose reasonable starting values for the 3 parameters as functions of the observations.

- (c) Write an R function, with auxiliary functions as needed, to estimate the parameters. Make use of the initialization from part (b). You may use _lm()_ for updating _β_ . You’ll need to include criteria for deciding when to stop the optimization. Test your function using data simulated from the model with (a) a modest proportion of exceedances expected, say 20%, and (b) a high proportion, say 80%. Take _n_ = 100 and the parameters such that with complete data, _β_<sup>ˆ</sup> 1 _/se_ ( _β_<sup>ˆ</sup> 1) _≈_ 3. (In other words, you’ll need to figure out values of _β_ 1 and _σ_<sup>2</sup> such that the signal to noise ratio is 3.) You’ll also need to generate the _x_ s in some reasonable fashion.

1

- (d) A different approach to this problem just directly maximizes the log-likelihood of the observed data, which for the censored observations just involves the likelihood terms, _P_ ( _Yi > τ_ ). Estimate the parameters (and standard errors) for your test cases using _optim()_ with the BFGS option in R. You will want to consider reparameterization, and possibly use of the _parscale_ argument. Compare how many iterations EM and BFGS take. Note that parts (c) and (d) together provide a nice test of your code.

2

---

[Up: contents](../../index.md)
