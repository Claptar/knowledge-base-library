---
title: Ps 07 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps7.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/ps/ps7.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ps 07 —

**Source:** [`ps/ps7.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps7.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Stat243: Problem Set 7, Due Fri. November 17

### November 2, 2017

This covers Units 9 and 10.

It’s due **on paper** and submitted via Github at the start of class Some general guidelines on how to present your problem set solutions:

1. Please use your Rtex/Rnw/Rmd solution from PS1, problem 4 as your template for how to format your solutions (only non-Statistics students are allowed to use R Markdown).

2. As usual, your solution should mix textual description of your solution, code, and example output. And your code should be commented.

3. Your paper submission should be the printout of the PDF produced from your Rtex/Rnw/Rmd file. Your Github submission should include the Rtex/Rnw/Rmd file, any R or bash code files containing chunks that you read into your Rtex/Rnw/Rmd file, and the final PDF.

4. Use functions as much as possible, in particular for any repeated tasks. We will grade in part based on the modularity of your code and your use of functions.

5. Please note my comments in the syllabus about when to ask for help and about working together.

6. Please give the names of any other students that you worked with on the problem set.

## **Problems**

1. Suppose I have a statistical method that estimates a regression coefficient and its standard error. I develop a simulation study and have _m_ = 1000 simulated datasets that each give me an estimate of the coefficent and its standard error. How would I determine if the standard error properly characterizes the uncertainty of the estimated regression coefficient? Note your answer could be as simple as a sentence or two describing what quantities to consider.

2. Show that _∥A∥_ 2 is the largest of the absolute values of the eigenvalues of _A_ for symmetric _A_ . To do so, find the following quantity,


If you’re not familiar with the notion of the supremum (the ’sup’ here), just think of it as the maximum.

Hints: when you get to having the quantity Γ<sup>_⊤_</sup> _z_ for orthogonal Γ, set _y_ = Γ<sup>_⊤_</sup> _z_ and show that if _∥z∥_ 2 = 1 then _∥y∥_ 2 = 1. Finally, if you have the quantity _y_<sup>_⊤_</sup> _Dy_ for diagonal matrix _D_ , express this as a sum and think intuitively about how to maximize it if _∥y∥_ 2 = 1.

1

3. Some practice with matrix manipulations.

   - (a) Consider a rectangular matrix, _X_ , with dimensions _n×p_ and _n > p_ . Show that the right singular vectors of _X_ are the eigenvectors of the matrix _X_<sup>_⊤_</sup> _X_ and that the eigenvalues of _X_<sup>_⊤_</sup> _X_ are the squares of the singular values of _X_ . Also show that _X_<sup>_⊤_</sup> _X_ is positive semi-definite (which is good because _X_<sup>_⊤_</sup> _X_ is essentially an empirical covariance matrix, up to scaling and shifting). (Sidenote: as I mentioned in class, since the condition number of X is the ratio of the largest and smallest magnitude singular values, this shows why the condition number for using the Cholesky for regression is the square of the condition number for using the QR, and hence why the QR might be preferred to the Cholesky for doing OLS.)

   - (b) Consider an _n × n_ positive semi-definite matrix Σ and assume you have already computed the eigendecomposition of Σ. How can you compute the eigenvalues of _Z_ = Σ + _cI_ in _O_ ( _n_ ) arithmetic calculations (including any additions or multiplications), where _c_ is a scalar and _I_ is the identity matrix?

4. The following calculation arises in solving a least squares regression problem where the coefficients are subject to an equality constraint, in particular, we want to minimize ( _Y − Xβ_ )<sup>_⊤_</sup> ( _Y − Xβ_ ) subject to the _m_ constraints _Aβ_ = _b_ for an _m_ by _p_ matrix _A_ . (Each row of _A_ represents a constraint that that linear combination of _β_ equals the corresponding element of _b_ . Solving this problem is a form of optimization called quadratic programming. Some derivation using the Lagrange multiplier approach gives the following solution:


where _C_ = _X_<sup>_⊤_</sup> _X_ and _d_ = _X_<sup>_⊤_</sup> _Y_ . _X_ is _n_ by _p_ .

   - (a) Describe how you would implement this in pseudo-code.

   - (b) Write an R function to efficiently compute _β_<sup>ˆ</sup> , taking account of the principles discussed in class in terms of matrix inverses and factorizations. Note: you can use any of R’s matrix manipulation functions that you want - I’m not expecting you to code up any algorithms from scratch. Note: in reality an efficient solution is only important when the number of regression coefficients, _p_ , is large.

5. Two-stage least squares (2SLS) is a way of implementing an causal estimation method called instrumental variables that is commonly used in economics. Consider the following set of regression equations:


which can be intepreted as regressing _y_ on _X_ after filtering so that we only retain variation in _X_ that is correlated with the instrumental variable _Z_ . An economics graduate student asked how he could compute _β_<sup>ˆ</sup> if _Z_ is 60 million by 630, _X_ is 60 million by 600, and _y_ is 60 million by 1, but both _Z_ and _X_ are sparse.

- (a) Describe briefly why I can’t do this calculation in two stages as given in the equation, even if I use the techniques for OLS discussed in class for each stage.

2

   - (b) Figure out how to rewrite the equations such that you can actually calculate _β_<sup>ˆ</sup> on a computer without a huge amount of memory. You can assume that any matrix multiplications involving sparse matrices can be done on the computer (e.g., using the spam package in R). Describe the specific steps of how you would do this and/or write out in pseudo-code.

6. (Extra credit) For this problem, your task is to empirically explore the condition number of the eigendecomposition. First create a set of eigenvectors. An easy way to do this is to find the eigenvectors of _A_ = _Z_<sup>_⊤_</sup> _Z_ for arbitrary _Z_ , throwing away the eigenvalues. Now explore creating positive eigenvalues of different magnitudes and creating ΓΛΓ<sup>_⊤_</sup> from the Γ you got for _A_ and your chosen eigenvalues. Use _eigen()_ and see how close the computed eigenvalues are to the actual eigenvalues. I would use _n_ = 100 and let the eigenvalues vary between all being equal and having a range of values from very large to very small. At what condition number do you empirically see that your matrix is not numerically positive definite? How does the error in the estimated eigenvalues relative to the known true values vary with the condition number and the magnitude of the eigenvalues?

3

---

[Up: contents](../index.md)
