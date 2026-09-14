---
title: Ps 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps7.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/ps7.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 07 —

**Source:** [`ps/ps7.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/ps7.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 7, Due Tuesday November 17

November 7, 2020

This covers Units 9 and 10.

It’s due **as PDF submitted to Gradescope** and submitted via GitHub at 10 am on Nov. 17. Comments:

1. The formatting requirements are the same as previous problem sets.

2. Please note my comments in the syllabus about when to ask for help and about working together. In particular, **please give the names of any other students that you worked with on the problem set and indicate in comments any ideas or code you borrowed from another student.**

## **Problems**

1. Suppose I have a statistical method that estimates a regression coefficient and its standard error. I develop a simulation study and have m = 1000 simulated datasets that each give me an estimate of the coefficent and its estimated standard error. How would I determine if the standard error provided by the statistical method properly characterizes the uncertainty of the estimated regression coefficient? You could answer this generally or by talking specifically about the SE columns in Table 1 of the Cao et al. paper. Note your answer can be as simple as a sentence or two describing what quantities to consider.

2. Experimenting with importance sampling.

   - (a) Use importance sampling to estimate the mean (i.e., _φ_ = _Ef X_ ) of a truncated _t_ distribution with 3 degrees of freedom, truncated such that _X <_ ( _−_ 4). Have your sampling density be a normal distribution centered at -4 and then truncated so you only sample values less than -4 (this is called a half-normal distribution). You should be able to do this without discarding any samples (how?). Use _m_ = 10000 samples. Create histograms of the weights _f_ ( _x_ ) _/g_ ( _x_ ) to get a sense for whether Var( _φ_<sup>ˆ</sup> ) is large. Note if there are any extreme weights that would have a very strong influence on _φ_<sup>ˆ</sup> . Estimate Var( _φ_<sup>ˆ</sup> ). Hint: remember that your _f_ ( _x_ ) needs to be appropriately normalized or you need to adjust the weights per the class notes.

   - (b) Now use importance sampling to estimate the mean of the same truncated _t_ distribution with 3 degrees of freedom, truncated such that _X <_ ( _−_ 4), but have your sampling density be a _t_ distribution, with 1 degree of freedom (not 3), centered at -4 and truncated so you only sample values less than -4. Again you shouldn’t have to discard any samples. Respond to the same questions as above in part (a). In addition, compute a 95% uncertainty interval for your estimate, using the Monte Carlo simulation error, �Varˆ (ˆ _µ_ ).

1

3. Suppose I need to compute the generalized least squares estimator, _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> Σ<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> Σ<sup>_−_1</sup> _Y_ , for _X n × p_ , Σ _n × n_ and assume that _n > p_ . Assume _n_ could be of order several thousand and _p_ of order in the hundreds. First write out in pseudo-code how you would do this in an efficient way - i.e., the particular linear algebra steps and the order of operations. Then write efficient R code in the form of a function, _gls()_ , to do this - you can rely on the various high-level functions for matrix decompositions and solving systems of equations, but you should not use any code that already exists for doing generalized least squares.

4. We’ve seen how to use Gaussian elimination (i.e., the LU decomposition) to solve _Ax_ = _b_ and that we can do the solution in _n_<sup>3</sup> _/_ 3 operations (plus lower-order terms). Suppose I want to know how inefficient it is to explicitly invert the matrix _A_ and then multiply, thereby finding _x_ = _A_<sup>_−_1</sup> _b_ via matrixvector multiplication. If we look at R’s _solve.default()_ , we see it solves the system _AZ_ = _I_ to find _Z_ = _A_<sup>_−_1</sup> . Next note that _help(solve)_ indicates it calls a Lapack routine DGESV (http://www.netlib.org/lapack/explorehtml/d7/d3b/group__double_g_esolve_ga5ee879032a8365897c3ba91e3dc8d512.html), which uses the LU decomposition.

Count the number of computations for

- (a) transforming _AZ_ = _I_ to _UZ_ = _I_<sup>_∗_</sup> (where _I_<sup>_∗_</sup> is no longer a diagonal matrix),

- (b) for solving for _Z_ given _UZ_ = _I_<sup>_∗_</sup> , and

- (c) for calculating _x_ = _Zb_ .

Then compare the total cost to the _n_<sup>3</sup> _/_ 3 cost of what we saw in the class notes and video.

Notes: In counting the computations you should be able to make use of various results we derived in class concerning the Gaussian elimination computations and computations involved in a backsolve, so your answer should be able to simply combine together results we’ve already discussed without any detailed new derivation.

Second note: Given that R’s call to _dgesv_ doesn’t take account of the special structure of _I_ on the right-hand side, you do not need to take account of the fact that because _I_ has zeroes and ones, one can actually save some computation. You can simply count the calculations as if _I_ were filled with arbitrary values. (Note: if we did actually try to be careful about making use of the structure of _I_ , it turns out we could save _n_<sup>3</sup> _/_ 3 calculations.)

5. Two-stage least squares (2SLS) is a way of implementing a causal inference method called instrumental variables that is commonly used in economics. Consider the following set of regression equations:

   - _X_ ˆ = _Z_ ( _Z_<sup>_⊤_</sup> _Z_ )<sup>_−_1</sup> _Z_<sup>_⊤_</sup> _X_ =

   - _β_ ˆ ( _X_<sup>ˆ</sup><sup>_⊤_</sup> _X_<sup>ˆ</sup> )<sup>_−_1</sup> _X_<sup>ˆ</sup><sup>_⊤_</sup> _y_

which can be interpreted as regressing _y_ on _X_ after filtering such that we only retain variation in _X_ that is correlated with the instrumental variable _Z_ . An economics graduate student asked how he could compute _β_<sup>ˆ</sup> if _Z_ is 60 million by 630, _X_ is 60 million by 600, and _y_ is 60 million by 1, but both _Z_ and _X_ are sparse matrices.

- (a) Describe briefly why I can’t do this calculation in two steps as given in the equations, even if I use the techniques for OLS discussed in class for each stage.

- (b) Figure out how to rewrite the equations such that you can actually calculate _β_<sup>ˆ</sup> on a computer without a huge amount of memory. You can assume that any matrix multiplications involving sparse matrices can be done on the computer (e.g., using the _spam_ package in R). Describe the specific steps of how you would do this and/or write out in pseudo-code.

2

Notes: (1) The product of two sparse matrices is not (in general) sparse and would not be sparse in this case. (2) As discussed in Section 6.2 of Unit 10, there are R packages (and software packages more generally) for efficiently storing (to save memory) and efficiently doing matrix manipulations (to save computation time) with sparse matrices.

6. **(Extra credit)** In class we saw that the condition number when solving a system of equations, _Ax_ = _b_ , is the ratio of the largest and smallest magnitude eigenvalues of _A_ . Show that _∥A∥_ 2 (i.e., the matrix norm induced by the usual L2 vector norm; see Section 1.6 of Unit 10) is the largest of the absolute values of the eigenvalues of _A_ for symmetric _A_ . To do so, find the following quantity,


If you’re not familiar with the notion of the supremum (the _sup_ here), just think of it as the maximum. It accounts for situations such as trying to find the maximum of the numbers in the open interval (0,1). The max is undefined in this case since there is always a number closer to 1 than any number you choose, but the _sup_ in this case is 1.

Hints: when you get to having the quantity Γ<sup>_⊤_</sup> _z_ for orthogonal Γ, set _y_ = Γ<sup>_⊤_</sup> _z_ and show that if _∥z∥_ 2 = 1 then _∥y∥_ 2 = 1. Finally, if you have the quantity _y_<sup>_⊤_</sup> _Dy_ , think about how this can be rewritten given the form of _D_ and think intuitively about how to maximize it if _∥y∥_ 2 = 1.

7. **(Extra credit)** In Unit 10 we discussed that having a 0 as an eigenvalue of a covariance matrix amounts to having a constraint (one of the eigenvectors has zero weight). In (optional) Section 2.4, I say a bit about having a zero eigenvalue of a precision matrix, where a precision matrix is the inverse of the covariance matrix.

   - (a) What is the relationship between the eigenvalues of a covariance matrix, Σ, and the eigenvalues of the corresponding precision matrix, Σ<sup>_−_1</sup> ?

   - (b) Consider the following autoregressive style model:


The likelihood (joint distribution for ( _y_ 1 _, . . . , yn_ )) is


which gives us the sum of squares:


We can equivalently represent the model as


where _Q_ = Σ<sup>_−_1</sup> is the precision matrix and looks like this (for the specific case of _n_ = 5):


3

Show that with the joint distribution based on the multivariate representation, _Y ∼ N_ (0 _, σ_<sup>2</sup> _Q_<sup>_−_1</sup> ), you get the same sum of squares as above.

- (c) Show that if you add a constant value to every _yi_ , the sum of squares is unchanged. This makes sense because we can see the sum of squares as involving contrasts (differences) of adjacent data values. The interpretation is that this model says nothing about the overall level of the _yi_ values, only about their contrasts.

- (d) For the _n_ = 100 case, create _Q_ and find the eigendecomposition in R and show that one of the eigenvalues is 0 and that the corresponding eigenvector is a vector with each value equal to 1 _/_<sup>_√_</sup> _<u>n</u>_ <u>.</u>

- (e) To generate a random vector _Y_ = ΓΛ<sup>1</sup><sup>_/_2</sup> _z_ , where Γ and Λ have the eigenvectors and eigenvalues of Σ, we would need to invert _Q_ . But we can’t do that because an eigenvalue is 0. Instead, we would use the pseudo-inverse described at the start of Section 2.4. For the case of _n_ = 100 carry out this algorithm and generate and plot a small number of random vectors _Y_ from this autoregressive model. You should see that the mean of each vector _Y_ is 0, which is consistent with having imposed a constraint by using the pseudo-inverse.

4

---

[Up: contents](../index.md)
