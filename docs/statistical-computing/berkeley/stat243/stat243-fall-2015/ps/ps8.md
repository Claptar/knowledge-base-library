---
title: Ps 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps8.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/ps/ps8.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 08 —

**Source:** [`ps/ps8.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps8.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 8, Due Dec. 4

November 17, 2015

Comments:

- This covers Units 10 and 11.

- It’s due at the start of class on Friday Dec. 4.

- As usual, your solution should mix textual description of your solution, code, and example output. Feel free to write out answers to the mathematical problems by hand if you like. If you do so, please staple them into any PDF pages in the correct order to avoid having Harold have to hunt around for what problem solution is where.

- Please note my comments in the syllabus about when to ask for help and about working together.

- Please give the names of any other students that you worked with on the problem set.

## **Problems**

1. Describe the process of carrying out a simulation study for the following scenario. You are interested in how regression methods perform when there are outlying values, in particular in comparing a new method that is supposedly robust to outliers to standard linear regression. In particular you’re interested in absolute prediction error and in the coverage of prediction intervals for new observations, where the prediction intervals are based on using the nonparametric bootstrap.

   - (a) Describe (in text, formulas and/or with pseudo-code as helpful) the steps involved in the simulation study and how you would estimate the prediction error and coverage and compare the two methods. Be precise in your notation about the various sample sizes involved, where and how random values are generated, and where loops are involved and the indexing of those loops. You don’t need to describe in detail how the bootstrap calculations are done (you can treat it as a black box), but be clear what values are the inputs to and outputs from the bootstrap calculations and any looping involved in the bootstrapping.

   - (b) Provide a concrete example using specific numerical values and a specific strategy for generating the simulated datasets.

2. Let’s consider importance sampling and explore the need to have the sampling density have heavier tails than the density of interest. Assume that we want to estimate _EX_ and _E_ ( _X_<sup>2</sup> ) with respect to a density, _f_ . We’ll make use of the Pareto distribution, which has the pdf _p_ ( _x_ ) = _x_<sup>_<u>ββα</u>_+1</sup><sup>_β_for</sup><sup>_α < x < ∞_,</sup> _α >_ 0, _β >_ 0. The mean is _ββ−α_ 1<sup>for</sup><sup>_β>_1 and non-existent for</sup><sup>_β≤_1 and the variance is</sup> ( _β−_ 1) _<u>βα</u>_<sup><u>2</u></sup> (<sup>2</sup> _β−_ 2) for _β >_ 2 and non-existent otherwise.

1

   - (a) Does the tail of the Pareto decay more quickly or more slowly than that of an exponential distribution?

   - (b) Suppose _f_ is an exponential density with parameter value equal to 1, shifted by two to the right so that _f_ ( _x_ ) = 0 for _x <_ 2 and our sampling density, _g_ , is a Pareto distribution with _α_ = 2 and _β_ = 3. Use _m_ = 10000 to estimate _EX_ and _E_ ( _X_<sup>2</sup> ). Recall that Var(ˆ _µ_ ) _∝_ Var( _h_ ( _X_ ) _f_ ( _X_ ) _/g_ ( _X_ )). Create histograms of _h_ ( _x_ ) _f_ ( _x_ ) _/g_ ( _x_ ) and of the weights _f_ ( _x_ ) _/g_ ( _x_ ) to get an idea for whether Var(ˆ _µ_ ) is large. Note if there are any extreme weights that would have a very strong influence on _µ_ ˆ.

   - (c) Now suppose _f_ is the Pareto distribution described above and our sampling density, _g_ , is the exponential described above. Respond to the same questions as for part (b).

3. Consider probit regression, which is an alternative to logistic regression for binary outcomes. The probit model is _P_ ( _Yi_ = 1) = Φ( _Xi_<sup>_⊤β_)whereΦisthestandardnormalCDF.Wecanrewritethis</sup> model with latent variables, one latent variable for each observation:


- (a) Design an EM algorithm to estimate _β_ , taking the complete data to be _{Y, Z}_ . You’ll need to make use of _E_ ( _W |W > τ_ ) and Var( _W |W > τ_ ) where _W_ is normally distributed. Be careful that you carefully distinguish _β_ from the current value at iteration _t_ , _β_<sup>_t_</sup> , in writing out the expected log-likelihood and computing the expectation and that your maximization be with respect to _β_ (not _β_<sup>_t_</sup> ). Also be careful that your calculations respect the fact that for each _zi_ you know that it is either bigger or smaller than 0 based on its _yi_ . You should be able to analytically maximize the expected log likelihood. A couple hints:

   - i. From the Johnson and Kotz bibles on distributions, the mean and variance of the truncated normal distribution, _f_ ( _w_ ) _∝N_ ( _w_ ; _µ, σ_<sup>2</sup> ) _I_ ( _w > τ_ ), are:


where _φ_ ( _·_ ) is the standard normal density and Φ( _·_ ) is the standard normal CDF. Or see the Wikipedia page on the truncated normal distribution for more general formulae.

   - ii. You should recognize that your expected log-likelihood can be expressed as a regression of some new quantities (which you might denote as _mi_ , _i_ = 1 _, . . . , n_ , where the _mi_ are functions of _β_<sup>_t_</sup> and _yi_ ) on _X_ .

- (b) Propose reasonable starting values for _β_ .

- (c) Write an R function, with auxiliary functions as needed, to estimate the parameters. Make use of the initialization from part (b). You may use _lm()_ for the update steps. You’ll need to include criteria for deciding when to stop the optimization. Test your function using data simulated from the model, with say _β_ 0 _, β_ 1 _, β_ 2 _, β_ 3. Take _n_ = 100 and the parameters such that _β_<sup>ˆ</sup> 1 _/se_ ( _β_<sup>ˆ</sup> 1) _≈_ 2 and _β_ 2 = _β_ 3 = 0. (In other words, I want you to choose _β_ 1 such that the signal to noise ratio in the relationship between _x_ 1 and _y_ is moderately large.

2

   - (d) A different approach to this problem just directly maximizes the log-likelihood of the observed data. Estimate the parameters (and standard errors) for your test cases using _optim()_ with the BFGS option in R. Compare how many iterations EM and BFGS take.

4. Consider the “helical valley” function (see the _helical.R_ file in the repository). Plot slices of the function to get a sense for how it behaves (i.e., for a constant value of one of the inputs, plot as a 2-d function of the other two). Syntax for _image()_ , _contour()_ or _persp()_ from the graphics unit (Unit 13) will be helpful. Try out _optim()_ and _nlm()_ for finding the minimum of this function (or use _optimx()_ ). Explore the possibility of multiple local minima by using different starting points.

5. (Extra credit) Write Spark code to implement IWLS for GLMs in parallel, in particular for logistic regression. You should be able to take the demo code from the end of Unit 7 and modify it for this purpose. Use your code to fit a logistic regression model for the binary outcome of whether a plane arrives 15 or more minutes late. You can take the covariates to be those I used in the in class demo (distance and day of week) or use other covariates you might be interested in. Your code for fitting the GLM should be general and apply to any set of covariates, but your code to create the X matrix can just deal with the specific covariates you use in the airline model you fit. Given our limited credits on AWS, please do your development for this problem using only two Spark worker nodes with a subset of the airline dataset.

3

---

[Up: contents](../index.md)
