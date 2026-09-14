---
title: 3 Computational issues
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit10-linalg.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Computational issues

**Source:** [`units/unit10-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit10-linalg.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Storing matrices**

We’ve discussed column-major and row-major storage of matrices. First, retrieval of matrix elements from memory is quickest when multiple elements are contiguous in memory. So in a column-major language (e.g., R, Fortran), it is best to work with values in a common column (or entire columns) while in a row-major language (e.g., Python, C) for values in a common row.

In some cases, one can save space (and potentially speed) by overwriting the output from a matrix calculation into the space occupied by an input. This occurs in some clever implementations of matrix factorizations.

### **3.2 Algorithms**

Good algorithms can change the efficiency of an algorithm by one or more orders of magnitude, and many of the improvements in computational speed over recent decades have been in algorithms rather than in computer speed.

Most matrix algebra calculations can be done in multiple ways. For example, we could compute _b_ = _Ax_ in either of the following ways, denoted here in pseudocode.

1. Stack the inner products of the rows of _A_ with _x_ .


11


2. Take the linear combination (based on _x_ ) of the columns of _A_


In this case the two approaches involve the same number of operations but the first might be better for row-major matrices (so might be how we would implement in C) and the second for columnmajor (so might be how we would implement in Fortran). **Challenge** : check whether the second approach is faster in R. (Write the code just doing the outer loop and doing the inner loop using vectorized calculation.)

**General computational issues** The same caveats we discussed in terms of computer arithmetic hold naturally for linear algebra, since this involves arithmetic with many elements. Good implementations of algorithms are aware of the danger of catastrophic cancellation and of the possibility of dividing by zero or by values that are near zero.

### **3.3 Ill-conditioned problems**

**Basics** A problem is ill-conditioned if small changes to values in the computation result in large changes in the result. This is quantified by something called the _condition number_ of a calculation. For different operations there are different condition numbers.

Ill-conditionedness arises most often in terms of matrix inversion, so the standard condition number is the “condition number with respect to inversion”, which when using the _L_ 2 norm is the

12

ratio of the absolute values of the largest to smallest eigenvalue. Here’s an example:


The solution of _Ax_ = _b_ for _b_ = (32 _,_ 23 _,_ 33 _,_ 31) is _x_ = (1 _,_ 1 _,_ 1 _,_ 1), while the solution for _b_ + _δb_ = (32 _._ 1 _,_ 22 _._ 9 _,_ 33 _._ 1 _,_ 30 _._ 9) is _x_ + _δx_ = (9 _._ 2 _, −_ 12 _._ 6 _,_ 4 _._ 5 _, −_ 1 _._ 1), where _δ_ is notation for a perturbation to the vector or matrix.

norm2 <- **function** (x) **sqrt** ( **sum** (x^2))

A <- **matrix** ( **c** (10,7,8,7,7,5,6,5,8,6,10,9,7,5,9,10),4) b <- **c** (32, 23, 33, 31) x <- **solve** (A, b)

bPerturbed <- **c** (32.1, 22.9, 33.1, 30.9) xPerturbed <- **solve** (A, bPerturbed)

What’s going on? Some manipulations with inequalities involving the induced matrix norm (for any chosen vector norm, but we might as well just think about the Euclidean norm) (see Gentle-CS Sec. 5.1) give


where we define the condition number w.r.t. inversion as cond( _A_ ) _≡∥A∥∥A_<sup>_−_1</sup> _∥_ . We’ll generally work with the _L_ 2 norm, and for a nonsingular square matrix the result is that the condition number is the ratio of the absolute values of the largest and smallest magnitude eigenvalues. This makes sense since _∥A∥_ 2 is the absolute value of the largest magnitude eigenvalue of _A_ and _∥A_<sup>_−_1</sup> _∥_ 2 that of the inverse of the absolute value of the smallest magnitude eigenvalue of _A_ .

We see in the code above that the large disparity in eigenvalues of _A_ leads to an effect predictable from our inequality above, with the condition number helping us find an upper bound.

e <- **eigen** (A) **norm2** (x - xPerturbed) _## delta x_ ## [1] 16.39695

**norm2** (b - bPerturbed) _## delta b_

13

---

[← Unit 10 — linalg Part 05 —](05-unit-10-linalg-part-05.md) · [Up: contents](index.md) · [Unit 10 — linalg Part 07 — →](07-unit-10-linalg-part-07.md)
