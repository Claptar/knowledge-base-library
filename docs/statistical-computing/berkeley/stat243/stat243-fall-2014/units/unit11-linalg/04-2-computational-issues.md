---
title: 2 Computational issues
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit11-linalg.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Computational issues

**Source:** [`units/unit11-linalg.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit11-linalg.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Storing matrices**

We’ve discussed column-major and row-major storage of matrices. First, retrieval of matrix elements from memory is quickest when multiple elements are contiguous in memory. So in a column-major language (e.g., R, Fortran), it is best to work with values in a common column (or entire columns) while in a row-major language (e.g., C) for values in a common row.

In some cases, one can save space (and potentially speed) by overwriting the output from a matrix calculation into the space occupied by an input. This occurs in some clever implementations of matrix factorizations.

### **2.2 Algorithms**

Good algorithms can change the efficiency of an algorithm by one or more orders of magnitude, and many of the improvements in computational speed over recent decades have been in algorithms rather than in computer speed.

Most matrix algebra calculations can be done in multiple ways. For example, we could compute _b_ = _Ax_ in either of the following ways, denoted here in pseudocode.

1. Stack the inner products of the rows of _A_ with _x_ .


2. Take the linear combination (based on _x_ ) of the columns of _A_


10

}

}

In this case the two approaches involve the same number of operations but the first might be better for row-major matrices (so might be how we would implement in C) and the second for columnmajor (so might be how we would implement in Fortran). **Challenge** : check whether the second approach is faster in R. (Write the code just doing the outer loop and doing the inner loop using vectorized calculation.)

**General computational issues** The same caveats we discussed in terms of computer arithmetic hold naturally for linear algebra, since this involves arithmetic with many elements. Good implementations of algorithms are aware of the danger of catastrophic cancellation and of the possibility of dividing by zero or by values that are near zero.

### **2.3 Ill-conditioned problems**

**Basics** A problem is ill-conditioned if small changes to values in the computation result in large changes in the result. This is quantified by something called the _condition number_ of a calculation. For different operations there are different condition numbers.

Ill-conditionedness arises most often in terms of matrix inversion, so the standard condition number is the “condition number with respect to inversion”, which when using the _L_ 2 norm is the ratio of the absolute values of the largest to smallest eigenvalue. Here’s an example:


The solution of _Ax_ = _b_ for _b_ = (32 _,_ 23 _,_ 33 _,_ 31) is _x_ = (1 _,_ 1 _,_ 1 _,_ 1), while the solution for _b_ + _δb_ = (32 _._ 1 _,_ 22 _._ 9 _,_ 33 _._ 1 _,_ 30 _._ 9) is _x_ + _δx_ = (9 _._ 2 _, −_ 12 _._ 6 _,_ 4 _._ 5 _, −_ 1 _._ 1), where _δ_ is notation for a perturbation to the vector or matrix. What’s going on?

norm2 <- **function** (x) **sqrt** ( **sum** (x^2)) A <- **matrix** ( **c** (10,7,8,7,7,5,6,5,8,6,10,9,7,5,9,10),4) e <- **eigen** (A) b <- **c** (32, 23, 33, 31) bPerturb <- **c** (32.1, 22.9, 33.1, 30.9)

11

x <- **solve** (A, b) xPerturb <- **solve** (A, bPerturb) **norm2** (x - xPerturb) ## [1] 16.39695 **norm2** (b - bPerturb) ## [1] 0.2 **norm2** (x - xPerturb)/ **norm2** (x) ## [1] 8.198475 (e$val[1]/e$val[4])* **norm2** (b - bPerturb)/ **norm2** (b) ## [1] 9.942834

Some manipulations with inequalities involving the induced matrix norm (for any chosen vector norm, but we might as well just think about the Euclidean norm) (see Gentle-CS Sec. 5.1) give


where we define the condition number w.r.t. inversion as cond( _A_ ) _≡∥A∥∥A_<sup>_−_1</sup> _∥_ . We’ll generally work with the _L_ 2 norm, and for a nonsingular square matrix the result is that the condition number is the ratio of the absolute values of the largest and smallest magnitude eigenvalues. This makes sense since _∥A∥_ 2 is the absolute value of the largest magnitude eigenvalue of _A_ and _∥A_<sup>_−_1</sup> _∥_ 2 that of the inverse of the absolute value of the smallest magnitude eigenvalue of _A_ . We see in the code above that the large disparity in eigenvalues of _A_ leads to an effect predictable from our inequality above, with the condition number helping us find an upper bound.

The main use of these ideas for our purposes is in thinking about the numerical accuracy of a linear system solution (Gentle-NLA Sec 3.4). On a computer we have the system


where the ’perturbation’ is from the inaccuracy of computer numbers. Our exploration of computer numbers tells us that


12

where _p_ = 16 for standard double precision floating points. Following Gentle, one gets the approximation


so if cond( _A_ ) _≈_ 10<sup>_t_</sup> , we have accuracy of order 10<sup>_t−p_</sup> instead of 10<sup>_−p_</sup> . (Gentle cautions that this holds only if 10<sup>_t−p_</sup> _≪_ 1). So we can think of the condition number as giving us the number of digits of accuracy lost during a computation relative to the precision of numbers on the computer. E.g., a condition number of 10<sup>8</sup> means we lose 8 digits of accuracy relative to our original 16 on standard systems. One issue is that estimating the condition number is itself subject to numerical error and requires computation of _A_<sup>_−_1</sup> (albeit not in the case of _L_ 2 norm with square, nonsingular _A_ ) but see Golub and van Loan (1996; p. 76-78) for an algorithm.

**Improving conditioning** Ill-conditioned problems in statistics often arise from collinearity of regressors. Often the best solution is not a numerical one, but re-thinking the modeling approach, as this generally indicates statistical issues beyond just the numerical difficulties.

A general comment on improving conditioning is that we want to avoid large differences in the magnitudes of numbers involved in a calculation. In some contexts such as regression, we can center and scale the columns to avoid such differences - this will improve the condition of the problem. E.g., in simple quadratic regression with _x_ = _{_ 1990 _, . . . ,_ 2010 _}_ (e.g., regressing on calendar years), we see that centering and scaling the matrix columns makes a huge difference on the condition number

x1 <- 1990:2010 x2 <- x1 - 2000 _# centered_ x3 <- x2/10 _# centered and scaled_ X1 <- **cbind** ( **rep** (1, 21), x1, x1^2) X2 <- **cbind** ( **rep** (1, 21), x2, x2^2) X3 <- **cbind** ( **rep** (1, 21), x3, x3^2) e1 <- **eigen** ( **crossprod** (X1)) e1$values ## [1] 3.360186e+14 7.699100e+02 -3.833498e-08 e2 <- **eigen** ( **crossprod** (X2)) e2$values ## [1] 50677.704275 770.000000 9.295725

13

e3 <- **eigen** ( **crossprod** (X3)) e3$values


The basic story is that simple strategies often solve the problem, and that you should be cognizant of the absolute and relative magnitudes involved in your calculations.

One rule of thumb is to try to work with numbers whose magnitude is around 1. We can often scale the values in our problem in order to do this. I.e., change the units of your variables. Instead of personal income in dollars, use personal income in thousands or hundreds of thousands of dollars.

---

[← Unit 11 — linalg Part 03 —](03-unit-11-linalg-part-03.md) · [Up: contents](index.md) · [3 Matrix factorizations (decompositions) and solving systems of linear equations →](05-3-matrix-factorizations-decompositions-and-solving-systems-o.md)
