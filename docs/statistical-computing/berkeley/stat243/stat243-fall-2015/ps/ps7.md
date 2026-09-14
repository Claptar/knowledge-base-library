---
title: 'Stat243: Problem Set 7, Due Monday Nov. 16'
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps7.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/ps/ps7.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: Problem Set 7, Due Monday Nov. 16

**Source:** [`ps/ps7.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/ps/ps7.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

November 2, 2015

Comments:

- This covers Units 9 and 10.

- It’s due at the start of class on Nov. 16.

- As usual, your solution should mix textual description of your solution, code, and example output. Feel free to write out answers to the mathematical problems by hand if you like. If you do so, please staple them into any PDF pages in the correct order to avoid having Harold have to hunt around for what problem solution is where.

- Please note my comments in the syllabus about when to ask for help and about working together.

- Please give the names of any other students that you worked with on the problem set.

## **Questions**

1. **(Due Monday Nov. 9)** Per the Piazza announcement, please follow the instructions in _section_questions_nov9.pdf_ in the sections directory of the class repository. Write your responses in a file called _ps7_question1.txt_ , put it in the top-level directory of your Git repository, and push to Github as you do for your problem set solutions. Also include your responses in your submission of PS7.

2. Details of the Cholesky decomposition.

   - (a) Work out the operation count (multiplies and divides) for the Cholesky decomposition, including the constant _c_ , not just the order, for terms involving _n_<sup>3</sup> or _n_<sup>2</sup> (e.g., 5 _n_<sup>3</sup> _/_ 2 + 75 _n_<sup>2</sup> , not _O_ ( _n_<sup>3</sup> )). You can ignore the square root and any additions/subtractions. You can ignore pivoting for the purpose of this problem. Remember not to count any steps that involve multiplying by 0 or 1. Compare your result to that given in the notes.

   - (b) Suppose I’ve written out the Cholesky calculation based on for loops. If I wanted to save storage space, can I store the Cholesky upper triangular matrix, _U_ , in the storage space that is used for the original matrix as I go along, assuming I’m willing to lose the original matrix, or do I overwrite anything I need later in the calculation of the Cholesky?

   - (c) Now, using a test matrix _X_ , compute the Cholesky (using R’s _chol()_ function) and monitor memory use based on top or based on _mem_used()_ or _gc()_ in R. Does memory use match that from your answer in part (b)? If not, how much more or less memory is used than you might expect? For a variety of values of _n_ (make sure you have matrices with _n_ in the thousands), find the maximum memory use and the processing time and plot these as a function of _n_ . Empirically how do memory use and processing time scale with _n_ ? [Note: make sure the only objects of

1

any substantial size in your workspace are _X_ and the resulting Cholesky matrix so that you only consider memory use from this operation.] For this problem make sure your calculations use only a single thread/core.

Note: You can compute a positive definite test matrix either using the correlation function examples for stochastic (Gaussian) processes we’ve seen in class, or consider the implications of problem 5a.

3. Compare the speed of _b_ = _X_<sup>_−_1</sup> _y_ using: (a) solve(X) followed by ’ _%*%_ ’; (b) solve(X,y); and (c) Cholesky decomposition followed by solving triangular systems. Do this for a matrix of size 5000 _×_ 5000 using a single thread.

   - (a) How do the timing and relative ordering amongst methods compare to the order of computations we discussed in class and the notes? (I don’t think I mentioned it anywhere, but the full inversion can be found to take _n_<sup>3</sup> calculations.)

   - (b) Are the results for _b_ the same numerically for the different methods (up to machine precision)? Comment on how many decimal places in _b_ agree, and relate this to the condition number of the calculation.

4. Suppose I need to compute the generalized least squares estimator, _β_<sup>ˆ</sup> = ( _X_<sup>_⊤_</sup> Σ<sup>_−_1</sup> _X_ )<sup>_−_1</sup> _X_<sup>_⊤_</sup> Σ<sup>_−_1</sup> _Y_ , for _X n × p_ , Σ _n × n_ and assume that _n > p_ . Assume _n_ could be of order several thousand and _p_ of order in the hundreds. First write out in pseudo-code how you would do this in an efficient way - i.e., the particular linear algebra steps and the order of operations. Then write efficient R code in the form of a function, _gls()_ , to do this - you can rely on the various high-level functions for matrix decompositions and solving systems of equations, but you should not use any code that already exists for doing generalized least squares.

5. Some practice with matrix manipulations.

   - (a) Consider a rectangular matrix, _X_ , with dimensions _n×p_ and _n > p_ . Show that the right singular vectors of _X_ are the eigenvectors of the matrix _X_<sup>_⊤_</sup> _X_ and that the eigenvalues of _X_<sup>_⊤_</sup> _X_ are the squares of the singular values of _X_ . Also show that _X_<sup>_⊤_</sup> _X_ is positive semi-definite (which is good because _X_<sup>_⊤_</sup> _X_ is essentially an empirical covariance matrix, up to scaling and shifting). (Sidenote: as I mentioned in class, since the condition number of X is the ratio of the largest and smallest magnitude singular values, this shows why the condition number for using the Cholesky for regression is the square of the condition number for using the QR.)

   - (b) Consider an _n × n_ positive semi-definite matrix _X_ and assume you have already computed the eigendecomposition of _X_ . How can you compute the eigenvalues of _Z_ = _X_ + _cI_ in _O_ ( _n_ ) arithmetic calculations (including any additions or multiplications), where _c_ is a scalar and _I_ is the identity matrix.

2

---

[Up: contents](../index.md)
