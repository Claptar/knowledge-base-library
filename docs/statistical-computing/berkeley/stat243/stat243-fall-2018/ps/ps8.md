---
title: Ps 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps8.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/ps/ps8.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 08 —

**Source:** [`ps/ps8.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps8.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 8, Due Fri. November 30

November 16, 2018

This covers Units 10 and 11.

It’s due **as PDF submitted to bCourses** and submitted via Github at 2 pm on Nov. 30. Some general guidelines on how to present your problem set solutions:

1. Please use Rmd/Rtex as in previous problem sets.

2. Your solution should not just be code - you should have text describing how you approached the problem and what the various steps were.

3. Your PDF submission should be the PDF produced from your Rmd/Rtex. Your Github submission should include the Rtex/Rmd file, any R code files containing chunks that you read into your Rtex/Rmd file, and the final PDF, all named according to the guidelines in _howtos/submitting-electronically.txt_ .

4. Your code should have comments indicating what each function or block of code does, and for any lines of code or code constructs that may be hard to understand, a comment indicating what that code does. You do not need to show exhaustive output but in general you should show short examples of what your code does to demonstrate its functionality.

5. Please note my comments in the syllabus about when to ask for help and about working together. In particular, **please give the names of any other students that you worked with on the problem set and indicate in comments any ideas or code you borrowed from another student.**

## **Problems**

1. Experimenting with importance sampling.

   - (a) Use importance sampling to estimate the mean (i.e., _φ_ = _Ef X_ ) of a truncated _t_ distribution with 3 degrees of freedom, truncated such that _X <_ ( _−_ 4). Have your sampling density be a normal distribution centered at -4 and then truncated so you only sample values less than -4 (this is called a half-normal distribution). You should be able to do this without discarding any samples (how?). Use _m_ = 10000 samples. Create histograms of the weights _f_ ( _x_ ) _/g_ ( _x_ ) to get a sense for whether Var( _φ_<sup>ˆ</sup> ) is large. Note if there are any extreme weights that would have a very strong influence on _φ_<sup>ˆ</sup> . Estimate Var( _φ_<sup>ˆ</sup> ). Hint: remember that your _f_ ( _x_ ) needs to be appropriately normalized or you need to adjust the weights per the class notes.

   - (b) Now use importance sampling to estimate the mean of the same truncated _t_ distribution with 3 degrees of freedom, truncated such that _X <_ ( _−_ 4), but have your sampling density be a _t_ distribution, with 1 degree of freedom (not 3), centered at -4 and truncated so you only sample values less than -4. Again you shouldn’t have to discard any samples. Respond to the same questions as above in part (a).

1

2. Consider the “helical valley” function (see the _ps8.R_ file in the repository). Plot slices of the function to get a sense for how it behaves (i.e., for a constant value of one of the inputs, plot as a 2-d function of the other two). Syntax for _image()_ , _contour()_ or _persp()_ (or the ggplot2 equivalents) from the R bootcamp materials will be helpful. Now try out _optim()_ and _nlm()_ for finding the minimum of this function (or use _optimx()_ ). Explore the possibility of multiple local minima by using different starting points.

3. Consider probit regression, which is an alternative to logistic regression for binary outcomes. The probit model is _Yi ∼_ Ber( _pi_ ) for _pi_ = _P_ ( _Yi_ = 1) = Φ( _Xi_<sup>_⊤β_) where Φ is the standard normal CDF.</sup> We can rewrite this model with latent variables, one latent variable, _zi_ , for each observation:


- (a) Design an EM algorithm to estimate _β_ , taking the complete data to be _{Y, Z}_ . You’ll need to make use the the mean and variance of truncated normal distributions (see hint below). Be careful that you carefully distinguish _β_ from the current value at iteration _t_ , _β_<sup>_t_</sup> , in writing out the expected log-likelihood and computing the expectation and that your maximization be with respect to _β_ (not _β_<sup>_t_</sup> ). Also be careful that your calculations respect the fact that for each _zi_ you know that it is either bigger or smaller than 0 based on its _yi_ . You should be able to analytically maximize the expected log likelihood. A couple hints:

   - i. From the Johnson and Kotz bibles on distributions, the mean and variance of the truncated normal distribution, _f_ ( _w_ ) _∝N_ ( _w_ ; _µ, σ_<sup>2</sup> ) _I_ ( _w > τ_ ), are:


where _φ_ ( _·_ ) is the standard normal density and Φ( _·_ ) is the standard normal CDF. Or see the Wikipedia page on the truncated normal distribution for more general formulae.

   - ii. You should recognize that your expected log-likelihood can be expressed as a regression of some new quantities (which you might denote as _mi_ , _i_ = 1 _, . . . , n_ , where the _mi_ are functions of _β_<sup>_t_</sup> and _yi_ ) on _X_ .

- (b) Propose reasonable starting values for _β_ .

- (c) Write an R function, with auxiliary functions as needed, to estimate the parameters. Make use of the initialization from part (b). You may use _lm()_ for the update steps. You’ll need to include criteria for deciding when to stop the optimization. Test your function using data simulated from the model, with say _β_ 0 _, β_ 1 _, β_ 2 _, β_ 3. Take _n_ = 100 and the parameters such that _β_<sup>ˆ</sup> 1 _/se_ ( _β_<sup>ˆ</sup> 1) _≈_ 2 and _β_ 2 = _β_ 3 = 0. (In other words, I want you to choose _β_ 1 such that the signal to noise ratio in the relationship between _x_ 1 and _y_ is moderately large.)

- (d) A different approach to this problem just directly maximizes the log-likelihood of the observed data. Estimate the parameters (and standard errors) for your test cases using _optim()_ with the BFGS option in R. Compare how many iterations EM and BFGS take.

2

---

[Up: contents](../index.md)
