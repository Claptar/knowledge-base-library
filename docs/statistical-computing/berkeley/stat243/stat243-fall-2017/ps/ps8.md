---
title: Ps 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps8.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/ps/ps8.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 08 —

**Source:** [`ps/ps8.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps8.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 8, Due Friday Dec. 1

November 20, 2017

Comments:

- This covers Units 10 and 11.

- It’s due at the start of class on Dec. 1.

## **Questions**

1. Let’s consider importance sampling and explore the need to have the sampling density have heavier tails than the density of interest. Assume that we want to estimate _φ_ = _EX_ and _φ_ = _E_ ( _X_<sup>2</sup> ) with respect to a density, _f_ . We’ll make use of the Pareto distribution, which has the pdf _p_ ( _x_ ) = _x_<sup>_<u>ββα</u>_+1</sup><sup>_β_for</sup> _α < x < ∞_ , _α >_ 0, _β >_ 0. The mean is _ββ−α_ 1<sup>for</sup><sup>_β>_1 and non-existent for</sup><sup>_β≤_1 and the variance</sup> _<u>βα</u>_<sup>2</sup>

is ( _β−_ 1)<sup><u>2</u></sup> ( _β−_ 2)<sup>for</sup><sup>_β>_2 and non-existent otherwise.</sup>

   - (a) Does the tail of the Pareto decay more quickly or more slowly than that of an exponential distribution?

   - (b) Suppose _f_ is an exponential density with parameter value equal to 1, shifted by two to the right so that _f_ ( _x_ ) = 0 for _x <_ 2 and our sampling density, _g_ , is a Pareto distribution with _α_ = 2 and _β_ = 3. Use _m_ = 10000 to estimate _EX_ and _E_ ( _X_<sup>2</sup> ). Recall that Var( _φ_<sup>ˆ</sup> ) _∝_ Var( _h_ ( _X_ ) _f_ ( _X_ ) _/g_ ( _X_ )). Create histograms of _h_ ( _x_ ) _f_ ( _x_ ) _/g_ ( _x_ ) and of the weights _f_ ( _x_ ) _/g_ ( _x_ ) to get an idea for whether Var( _φ_<sup>ˆ</sup> ) is large. Note if there are any extreme weights that would have a very strong influence on _µ_ ˆ.

   - (c) Now suppose _f_ is the Pareto distribution described above and our sampling density, _g_ , is the exponential described above. Respond to the same questions as for part (b).

2. Consider the “helical valley” function (see the _ps8.R_ file in the repository). Plot slices of the function to get a sense for how it behaves (i.e., for a constant value of one of the inputs, plot as a 2-d function of the other two). Syntax for _image()_ , _contour()_ or _persp()_ (or the ggplot2 equivalents) from the R bootcamp materials will be helpful. Now try out _optim()_ and _nlm()_ for finding the minimum of this function (or use _optimx()_ ). Explore the possibility of multiple local minima by using different starting points.

3. Consider a censored regression problem. We assume a simple linear regression model, _Yi ∼N_ ( _β_ 0 + _β_ 1 _xi, σ_<sup>2</sup> ). Suppose we have an iid sample, but that for any observation with _Y > τ_ , all we are told is that _Y_ exceeded the threshold and not its actual value. In a given sample, _c_ of the _n_ observations will (in a stochastic fashion) be censored, depending on how many exceed the fixed _τ_ . A real world example (but with censoring in the left tail) is in measuring pollutants, for which values below a threshold are reported as below the limit of detection. Another real world example is US tax revenue

1

data where the incomes of wealthy taxpayers may be reported as simply exceeding, say, 1 million dollars.

- (a) Design an EM algorithm to estimate the 3 parameters, _θ_ = ( _β_ 0 _, β_ 1 _, σ_<sup>2</sup> ), taking the complete data to be the available data plus the actual values of the censored observations. You’ll need to make use of _E_ ( _W |W > τ_ ) and Var( _W |W > τ_ ) where _W_ is normally distributed. Be careful that you carefully distinguish _θ_ from the current value at iteration _t_ , _θt_ , in writing out the expected log-likelihood and computing the expectation and that your maximization be with respect to _θ_ . You should be able to analytically maximize the expected log likelihood. A couple hints:

   - i. Considering the notation we used in class when discussing EM, it’s natural to think of _Z_ as the (unobserved) values of the censored observations. You can think of _c_ as being part of _X_ (in the sense of the meaning of _X_ in the class notes, not the _xi_ covariate values), along with the uncensored observations.

   - ii. From the Johnson and Kotz bibles on distributions, the mean and variance of the truncated normal distribution, _f_ ( _W_ ) _∝N_ ( _µ, σ_<sup>2</sup> ) _I_ ( _W > τ_ ), are:


      - where _φ_ ( _·_ ) is the standard normal density and Φ( _·_ ) is the standard normal CDF.

   - iii. You should recognize that your expected log-likelihood can be expressed as a regression of _{Yobs, mt}_ on _{x}_ where _Yobs_ are the non-censored data and _{mi,t}, i_ = 1 _, . . . , c_ are used in place of the censored observations. Note that _{mi,t}_ will be functions of _θt_ and thus constant in terms of the maximization step. Your estimator for _σ_<sup>2</sup> should involve a ratio where the numerator involves the usual sum of squares for the non-censored data plus two additional terms that you should interpret statistically.

- (b) Propose reasonable starting values for the 3 parameters as functions of the observations.

- (c) Write an R function, with auxiliary functions as needed, to estimate the parameters. Make use of the initialization from part (b). You may use _lm()_ for updating _β_ . You’ll need to include criteria for deciding when to stop the optimization. Test your function using data simulated based on the code in _ps8.R_ with (a) a modest proportion of exceedances expected, say 20%, and (b) a high proportion, say 80%.

- (d) A different approach to this problem just directly maximizes the log-likelihood of the observed data, which for the censored observations just involves the likelihood terms, _P_ ( _Yi > τ_ ). Estimate the parameters (and standard errors) for your test cases using _optim()_ with the BFGS option in R. You will want to consider reparameterization, and possibly use of the _parscale_ argument. Compare how many iterations EM and BFGS take. Note that parts (c) and (d) together provide a nice test of your EM derivation and code.

2

---

[Up: contents](../index.md)
