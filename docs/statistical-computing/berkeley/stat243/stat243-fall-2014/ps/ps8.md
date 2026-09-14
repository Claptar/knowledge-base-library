---
title: Ps 08 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps8.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/ps/ps8.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 08 —

**Source:** [`ps/ps8.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps8.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 8, Due Wednesday Dec. 3

November 17, 2014

Comments:

- This covers Units 12 and 13.

- It’s due at the start of class on Dec. 3.

- As usual, simply providing the raw code is not enough; make sure to describe how you approached the problem, the steps you took, and output illustrating what your code produces.

- Please note my comments in the syllabus about when to ask for help and about working together.

- As discussed in the syllabus, please turn in (1) a copy on paper, as this makes it easier for us to handle AND (2) an electronic copy through Git following Jarrod’s instructions. For problem 3a, you can write this by hand provided it is inserted in order with the remaining material that you turn in.

Note that while the Spark question on GLM fitting is extra credit, for those of you who will soon be on the job market and think that you will be applying for jobs that involve working with big datasets, I strongly recommend you do this problem. It may be a nice thing to be able to talk about in an interview. For those of you who got a 0 or a 1 on a previous problem set, I’ll also consider successful completion of this problem to offset a portion of that problem set.

## **Questions**

1. Experimenting with importance sampling.

   - (a) Use importance sampling to estimate the mean of a _t_ distribution with 3 degrees of freedom, truncated such that _X <_ ( _−_ 4). Have your sampling density be a normal distribution centered at -4 and then truncated so you only sample values less than -4 (this is called a half-normal distribution). You should be able to do this without discarding any samples (how?). Use _m_ = 10000 samples. Create histograms of _h_ ( _x_ ) _f_ ( _x_ ) _/g_ ( _x_ ) and of the weights _f_ ( _x_ ) _/g_ ( _x_ ) to get a sense for whether Var(ˆ _µ_ ) is large. Note if there are any extreme weights that would have a very strong influence on _µ_ ˆ. Hint: remember that your _f_ ( _x_ ) needs to be appropriately normalized or you need to adjust the weights per the class notes.

   - (b) Now use importance sampling to estimate the mean of a _t_ distribution with 3 degrees of freedom, truncated such that _X <_ ( _−_ 4), but have your sampling density be a _t_ distribution centered at -4 and truncated so you only sample values less than -4. Again you shouldn’t have to discard any samples. Respond to the same questions as above in part (a).

1

2. Consider the “helical valley” function (see the helical.R file in the repository). Plot slices of the function to get a sense for how it behaves (i.e., for a constant value of one of the inputs, plot as a 2-d function of the other two). Syntax for _image()_ , _contour()_ or _persp()_ from the graphics unit (Unit 15) will be helpful. Try out _optim()_ and _nlm()_ for finding the minimum of this function (or use _optimx()_ ). Explore the possibility of multiple local minima by using different starting points.

3. Consider a censored regression problem. We assume a simple linear regression model, _Yi ∼N_ ( _β_ 0 + _β_ 1 _xi, σ_<sup>2</sup> ). Suppose we have an iid sample, but that for any observation with _Y > τ_ , all we are told is that _Y_ exceeded the threshold and not its actual value. In a given sample, _c_ of the _n_ observations will (in a stochastic fashion) be censored, depending on how many exceed the fixed _τ_ . A real world example (but with truncation in the left tail) is in measuring pollutants, for which values below a threshold are reported as below the limit of detection.

   - (a) Design an EM algorithm to estimate the 3 parameters, _θ_ = ( _β_ 0 _, β_ 1 _, σ_<sup>2</sup> ), taking the complete data to be the available data plus the actual values of the truncated observations. You’ll need to make use of _E_ ( _Y |Y > τ_ ) and Var( _Y |Y > τ_ ) where _Y_ is normally distributed. Be careful that you carefully distinguish _θ_ from the current value at iteration _t_ , _θt_ , in writing out the expected log-likelihood and computing the expectation and that your maximization be with respect to _θ_ . You should be able to analytically maximize the expected log likelihood. A couple hints:

      - i. From the Johnson and Kotz bibles on distributions, the mean and variance of the truncated normal distribution, _f_ ( _Y_ ) _∝N_ ( _µ, σ_<sup>2</sup> ) _I_ ( _Y > τ_ ), are:


where _φ_ ( _·_ ) is the standard normal density and Φ( _·_ ) is the standard normal CDF.

   - ii. You should recognize that your expected log-likelihood can be expressed as a regression of _{Yobs, mt}_ on _{x}_ where _Yobs_ are the non-censored data and _{mi,t}, i_ = 1 _, . . . , c_ are used in place of the censored observations. Note that _{mi,t}_ will be functions of _θt_ and thus constant in terms of the maximization step. Your estimator for _σ_<sup>2</sup> should involve a ratio where the numerator involves the usual sum of squares for the non-censored data plus two additional terms that you should interpret statistically.

- (b) Propose reasonable starting values for the 3 parameters as functions of the observations.

- (c) Write an R function, with auxiliary functions as needed, to estimate the parameters. Make use of the initialization from part (b). You may use _lm()_ for updating _β_ . You’ll need to include criteria for deciding when to stop the optimization. Test your function using data simulated from the model with (a) a modest proportion of exceedances expected, say 20%, and (b) a high proportion, say 80%. Take _n_ = 100 and the parameters such that with complete data, _β_<sup>ˆ</sup> 1 _/se_ ( _β_<sup>ˆ</sup> 1) _≈_ 3. (In other words, you’ll need to figure out values of _β_ 1 and _σ_<sup>2</sup> such that the signal to noise ratio is 3.) You’ll also need to generate the _x_ s in some reasonable fashion.

- (d) A different approach to this problem just directly maximizes the log-likelihood of the observed data, which for the censored observations just involves the likelihood terms, _P_ ( _Yi > τ_ ). Estimate the parameters (and standard errors) for your test cases using _optim()_ with the BFGS option in R. You will want to consider reparameterization, and possibly use of the _parscale_ argument.

2

Compare how many iterations EM and BFGS take. Note that parts (c) and (d) together provide a nice test of your code.

4. (Extra credit) Write Spark code to implement IWLS for GLMs in parallel. You should be able to take the demo code from the end of Unit 9 and modify it for this purpose. Use your code to fit a logistic regression model for the binary outcome of whether a plane arrives 15 or more minutes late. You can take the covariates to be those I used in the in class demo (distance and day of week) or use other covariates you might be interested in. Your code for fitting the GLM should be general and apply to any set of covariates, but your code to create the _X_ matrix can just deal with the specific covariates you use in the airline model you fit.

3

---

[Up: contents](../index.md)
