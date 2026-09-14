---
title: 'Stat243: Problem Set 7, Due Wednesday November 17'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/ps7.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/ps/ps7.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: Problem Set 7, Due Wednesday November 17

**Source:** [`ps/ps7.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/ps7.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

November 11, 2021

This covers Units 9 and 10.

It’s due **as PDF submitted to Gradescope** and submitted via GitHub at 10 am on Nov. 17. Comments:

1. The formatting requirements are the same as previous problem sets.

2. Please note my comments in the syllabus about when to ask for help and about working together. In particular, **please give the names of any other students that you worked with on the problem set and indicate in comments any ideas or code you borrowed from another student.**

## **Problems**

1. Compare the speed of _x_ = _A_<sup>_−_1</sup> _b_ using: (i) solve(A)%*%b, (ii) solve(A,b), and (iii) Cholesky decomposition followed by solving triangular systems. To ensure that _A_ is invertible, you can construct a matrix _A_ as _A_ = _W_<sup>_⊤_</sup> _W_ where the elements of the _n × n_ matrix _W_ are generated independently using _rnorm()_ . Take _n_ = 5000. Note, if your R installation is not using a fast BLAS package, all three of these approaches will likely take a lot longer than if you are using a fast BLAS (e.g., on the SCF). See Section 6.1 of Unit 10 and/or Section 4.1.2 of Unit 8.

   - (a) **Using a single thread** , how do the timing and relative ordering amongst methods compare to the order of computations we discussed in class and the notes? Note that if one works out the complexity of the full inversion using the LU decomposition, it is 4 _n_<sup>3</sup> _/_ 3.

   - (b) Are the results for _x_ the same numerically for methods (ii) and (iii) (up to machine precision)? Comment on how many digits in the elements of _x_ agree, and relate this to the condition number of the calculation. (Note: you may want to compute the condition number on an SCF machine as it can take a few minutes to do the eigendecomposition for a matrix of this size.)

2. The following calculation arises in solving a least squares regression problem where the coefficients are subject to an equality constraint, in particular, we want to minimize ( _Y − Xβ_ )<sup>_⊤_</sup> ( _Y − Xβ_ ) with respect to _β_ subject to the _m_ constraints _Aβ_ = _b_ for an _m_ by _p_ matrix _A_ . (Each row of _A_ represents a constraint that that linear combination of _β_ equals the corresponding element of _b_ .) Solving this problem is a form of optimization called quadratic programming. Some derivation using the Lagrange multiplier approach gives the following solution:

_β_ ˆ = _C_<sup>_−_1</sup> _d_ + _C_<sup>_−_1</sup> _A_<sup>_⊤_</sup> ( _AC_<sup>_−_1</sup> _A_<sup>_⊤_</sup> )<sup>_−_1</sup> ( _−AC_<sup>_−_1</sup> _d_ + _b_ )

where _C_ = _X_<sup>_⊤_</sup> _X_ and _d_ = _X_<sup>_⊤_</sup> _Y_ . _X_ is _n_ by _p_ .

1

   - (a) Describe how you would implement this in pseudo-code, taking account of the principles discussed in class in terms of matrix inverses and factorizations

   - (b) Write an R function to efficiently compute _β_<sup>ˆ</sup> , taking account of the principles discussed in class in terms of matrix inverses and factorizations. Note: you can use any of R’s matrix manipulation functions that you want - I’m not expecting you to code up any algorithms from scratch. Note: in reality a very efficient solution is only important when the number of regression coefficients, _p_ , is large.

3. Details of the Cholesky decomposition presented in Unit 10. Work out the operation count (total number of multiplications plus divisions) for the Cholesky decomposition, including the constant _c_ , not just the order, for terms involving _n_<sup>3</sup> or _n_<sup>2</sup> (e.g., 5 _n_<sup>3</sup> _/_ 2 + 8 _n_<sup>2</sup> , not _O_ ( _n_<sup>3</sup> )). You can ignore the square root and any additions/subtractions. You can ignore pivoting for the purpose of this problem. Remember not to count any steps that involve multiplying by 0 or 1. Compare your result to that given in the notes.

4. **(Extra credit)** In class we saw that the condition number when solving a system of equations, _Ax_ = _b_ , is the ratio of the absolute values of the largest and smallest magnitude eigenvalues of _A_ . Show that _∥A∥_ 2 (i.e., the matrix norm induced by the usual L2 vector norm; see Section 1.6 of Unit 10) is the largest of the absolute values of the eigenvalues of _A_ for symmetric _A_ . To do so, find the following quantity,


If you’re not familiar with the notion of the supremum (the _sup_ here), just think of it as the maximum. It accounts for situations such as trying to find the maximum of the numbers in the open interval (0,1). The max is undefined in this case since there is always a number closer to 1 than any number you choose, but the _sup_ in this case is 1.

Hints: when you get to having the quantity Γ<sup>_⊤_</sup> _z_ for orthogonal Γ, set _y_ = Γ<sup>_⊤_</sup> _z_ and show that if _∥z∥_ 2 = 1 then _∥y∥_ 2 = 1. Finally, if you have the quantity _y_<sup>_⊤_</sup> _Dy_ , think about how this can be rewritten given the form of _D_ and think intuitively about how to maximize it if _∥y∥_ 2 = 1.

2

---

[Up: contents](../index.md)
