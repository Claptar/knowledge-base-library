---
title: 'Stat243: Problem Set 7, Due Friday Nov. 14'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps7.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/ps/ps7.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: Problem Set 7, Due Friday Nov. 14

**Source:** [`ps/ps7.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps7.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

November 8, 2014

Comments:

- This covers Units 11 and 12.

- It’s due at the start of class on Nov. 14.

- As usual, simply providing the raw code is not enough; make sure to describe how you approached the problem, the steps you took, and output illustrating what your code produces.

- Please note my comments in the syllabus about when to ask for help and about working together.

- As discussed in the syllabus, please turn in (1) a copy on paper, as this makes it easier for us to handle AND (2) an electronic copy through Git following Jarrod’s instructions.

## **Questions**

1. Per the Piazza announcement, please read the Chen et al. paper in the section directory of the class repository and respond to 3 of the 7 questions we have posed. Note that this is/was due to Jarrod via Github Monday Nov. 10 at 2 p.m. following the instructions Jarrod posted on Piazza.

2. Some practice with matrix manipulations.

   - (a) Show that the determinant of a square matrix that has an eigendecomposition is the product of the eigenvalues.

   - (b) Show that _∥A∥_ 2 is the largest of the absolute values of the eigenvalues of _A_ for symmetric _A_ . To do so, find the following quantity,


If you’re not familiar with the notion of the supremum (the ’sup’ here), just think of it as the maximum.

Hints: when you get to having the quantity Γ<sup>_⊤_</sup> _z_ for orthogonal Γ, set _y_ = Γ<sup>_⊤_</sup> _z_ and show that if _∥z∥_ 2 = 1 then _∥y∥_ 2 = 1. Finally, if you have the quantity _y_<sup>_⊤_</sup> _Dy_ for diagonal matrix _D_ , express this as a sum and think intuitively about how to maximize it if _∥y∥_ 2 = 1.

3. Suppose you have a dense matrix _X_ and a diagonal matrix _D_ . How would you compute the following in R in the most efficient way?

(a) _DX_

1

### (b) _XD_

4. This problem has you work out the number of calculations involved in the LU decomposition. For any terms involving _n_<sup>3</sup> or _n_<sup>2</sup> , please find the exact number of calculations, e.g., 5 _n_<sup>3</sup> _/_ 2 + 75 _n_<sup>2</sup> , NOT the order of the calculation (i.e., not _O_ ( _n_<sup>3</sup> )). You can ignore pivoting for the purpose of this problem. Remember not to count any steps that involve multiplying by 0 or 1. If you don’t do the extra credit (part d), you can just use the result given in in 4d in the later subparts of the problem.

   - (a) For an _n × n_ invertible matrix, find the number of flops involved in the forward reduction step of the LU decomposition, which finds _L_ and _U_ (don’t include the calculations that change _b_ to _b_<sup>_∗_</sup> ). [Remember from our derivation in class that _L_ = ( _Ln−_ 1 _· · · L_ 1)<sup>_−_1</sup> can be formed directly from quantities computed in finding _U_ , so all you’re doing here is counting the number of flops in Gaussian elimination.] How does this compare to the number of calculations involved in the Cholesky decomposition based on the count we did in class? Now also consider the additional computation involved in finding _b_<sup>_∗_</sup> , but don’t count (i.e., double-count) any calculations that you’ve already counted.

   - (b) How many additional flops are involved in the backward elimination step that finds _x_ based on _Ux_ = _b_<sup>_∗_</sup> ? (You do not need to re-derive this - we did it in class.)

   - (c) How many flops are involved in (a) and (b) if _b_ is actually a matrix (let’s call it _B_ ) with _p_ columns?

   - (d) (Extra credit) We could use _solve_ () in R (i.e., the _dgesv_ function in LAPACK) to explicitly find the inverse, _A_<sup>_−_1</sup> and then multiply _A_<sup>_−_1</sup> by the matrix _B_ . This seems like it might be appealing - if _p_ is large, maybe it’s more efficient to find the inverse and then just use matrix multiplication to find the result all at once rather than doing a bunch of backward eliminations, one per column of _B_ . Count the number of steps involved in using the LU to find _V_ = _A_<sup>_−_1</sup> such that _LUV_ = _I_ . You should find that finding the inverse takes _n_<sup>3</sup> + _O_ ( _n_<sup>2</sup> ) flops, including the flops needed to do the initial LU decomposition. For this part you do NOT need to find the constant in front of the _n_<sup>2</sup> term.

      - Hints: _A_<sup>_−_1</sup> = _U_<sup>_−_1</sup> _L_<sup>_−_1</sup> and _L_<sup>_−_1</sup> = _Ln−_ 1 _· · · L_ 2 _L_ 1 and the terms in the _Lj_ matrices are known from doing the initial LU decomposition.

   - (e) Now suppose we have _A_<sup>_−_1</sup> = _V_ from part (d). Count the flops involved in calculating _V B_ .

   - (f) Finally compare the total flops involved in finding _A_<sup>_−_1</sup> _B_ based on (c) and based on (d-e). Does the comparison of which is better depend on how big _p_ is?

   - (g) Empirically test your results in R for calculating _A_<sup>_−_1</sup> _B_ using an arbitrary matrix _A_ = _Z_<sup>_⊤_</sup> _Z_ with _n ∈{_ 100 _,_ 3000 _}_ and _p ∈{_ 1 _,_ 100 _,_ 3000 _}_ . Compare the use of (1) the LU via _solve()_ without explicitly finding the inverse, (2) _solve()_ to explicitly find the inverse followed by matrix multiplication, and (3) using the Cholesky decomposition. Use only one thread in your timing.

   - (h) Now suppose you are going to have to do a calculation with lots of new matrices, _Bj, j_ = 1 _,_ 2 _, . . ._ in the future. Is there any advantage to precomputing _A_<sup>_−_1</sup> and just doing the matrix multiplication, _A_<sup>_−_1</sup> _Bj_ for many _Bj_ as opposed to having _L_ and _U_ in hand and computing ( _LU_ )<sup>_−_1</sup> _Bj_ ?

5. The following calculation arises in solving a least squares regression problem where the coefficients are subject to an equality constraint, in particular, we want to minimize ( _Y − Xβ_ )<sup>_⊤_</sup> ( _Y − Xβ_ ) subject to the _m_ constraints _Aβ_ = _b_ for an _m_ by _p_ matrix _A_ . Solving this problem is a form of optimization

2

called quadratic programming. Some derivation using the Lagrange multiplier approach gives the following solution:


where _C_ = _X_<sup>_⊤_</sup> _X_ and _d_ = _X_<sup>_⊤_</sup> _Y_ . Write an R function to efficiently compute _β_<sup>ˆ</sup> , taking account of the principles discussed in class in terms of matrix inverses and factorizations. Note: you can use any of R’s matrix manipulation functions that you want - I’m not expecting you to code up any algorithms from scratch. In reality an efficient solution is only important when the number of regression coefficients, _p_ , is large.

6. (Extra credit) For this problem, your task is to empirically explore the condition number of the eigendecomposition. First create a set of eigenvectors. An easy way to do this is to find the eigenvectors of _A_ = _Z_<sup>_⊤_</sup> _Z_ for arbitrary _Z_ , throwing away the eigenvalues. Now explore creating positive eigenvalues of different magnitudes and creating ΓΛΓ<sup>_⊤_</sup> from the Γ you got for _A_ and your chosen eigenvalues. Use _eigen()_ and see how close the computed eigenvalues are to the actual eigenvalues. I would use _n_ = 100 and let the eigenvalues vary between all being equal and having a range of values from very large to very small. At what condition number do you empirically see that your matrix is not numerically positive definite? How does the error in the estimated eigenvalues relative to the known true values vary with the condition number and the magnitude of the eigenvalues?

3

---

[Up: contents](../index.md)
