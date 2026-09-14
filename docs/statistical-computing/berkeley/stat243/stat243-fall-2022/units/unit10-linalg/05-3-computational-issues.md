---
title: 3. Computational issues
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit10-linalg.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit10-linalg.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Computational issues

**Source:** [`units/unit10-linalg.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit10-linalg.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Storing matrices

We've discussed column-major and row-major storage of matrices. First,
retrieval of matrix elements from memory is quickest when multiple
elements are contiguous in memory. So in a column-major language (e.g.,
R, Fortran), it is best to work with values in a common column (or
entire columns) while in a row-major language (e.g., Python, C) for
values in a common row.

In some cases, one can save space (and potentially speed) by overwriting
the output from a matrix calculation into the space occupied by an
input. This occurs in some clever implementations of matrix
factorizations.

## Algorithms

Good algorithms can change the efficiency of an algorithm by one or more
orders of magnitude, and many of the improvements in computational speed
over recent decades have been in algorithms rather than in computer
speed.

Most matrix algebra calculations can be done in multiple ways. For
example, we could compute $b=Ax$ in either of the following ways,
denoted here in pseudocode.

1.  Stack the inner products of the rows of $A$ with $x$.\

```
        for(i=1:n){
            b_i = 0
            for(j=1:m){
                b_i = b_i + a_{ij} x_j
            }
        }
```

2.  Take the linear combination (based on $x$) of the columns of $A$\

```
        for(i=1:n){
            b_i = 0
        }
        for(j=1:m){
            for(i = 1:n){
                b_i = b_i + a_{ij} x_j
            }
        }
```

In this case the two approaches involve the same number of operations
but the first might be better for row-major matrices (so might be how we
would implement in C) and the second for column-major (so might be how
we would implement in Fortran).

**Challenge**: check whether the second
approach is faster in R. (Write the code just doing the outer loop and
doing the inner loop using vectorized calculation.)

#### General computational issues

The same caveats we discussed in terms of computer arithmetic hold
naturally for linear algebra, since this involves arithmetic with many
elements. Good implementations of algorithms are aware of the danger of
catastrophic cancellation and of the possibility of dividing by zero or
by values that are near zero.

## Ill-conditioned problems

#### Basics

A problem is ill-conditioned if small changes to values in the
computation result in large changes in the result. This is quantified by
something called the *condition number* of a calculation. For different
operations there are different condition numbers.

Ill-conditionedness arises most often in terms of matrix inversion, so
the standard condition number is the "condition number with respect to
inversion", which when using the $L_{2}$ norm is the ratio of the
absolute values of the largest to smallest eigenvalue. Here's an
example: $$A=\left(\begin{array}{cccc}
10 & 7 & 8 & 7\\
7 & 5 & 6 & 5\\
8 & 6 & 10 & 9\\
7 & 5 & 9 & 10
\end{array}\right).$$ The solution of $Ax=b$ for $b=(32,23,33,31)$ is
$x=(1,1,1,1)$, while the solution for $b+\delta b=(32.1,22.9,33.1,30.9)$
is $x+\delta x=(9.2,-12.6,4.5,-1.1)$, where $\delta$ is notation for a
perturbation to the vector or matrix.

```r
norm2 <- function(x) sqrt(sum(x^2))

A <- matrix(c(10,7,8,7,7,5,6,5,8,6,10,9,7,5,9,10),4)
A
b <- c(32, 23, 33, 31)
x <- solve(A, b)

bPerturbed <- c(32.1, 22.9, 33.1, 30.9)
xPerturbed <- solve(A, bPerturbed)
```


What's going on? Some manipulations with inequalities involving the
induced matrix norm (for any chosen vector norm, but we might as well
just think about the Euclidean norm) (see Gentle-CS Sec. 5.1) give
$$\frac{\|\delta x\|}{\|x\|}\leq\|A\|\|A^{-1}\|\frac{\|\delta b\|}{\|b\|}$$
where we define the condition number w.r.t. inversion as
$\mbox{cond}(A)\equiv\|A\|\|A^{-1}\|$. We'll generally work with the
$L_{2}$ norm, and for a nonsingular square matrix the result is that the
condition number is the ratio of the absolute values of the largest and
smallest magnitude eigenvalues. This makes sense since $\|A\|_{2}$ is
the absolute value of the largest magnitude eigenvalue of $A$ and
$\|A^{-1}\|_{2}$ that of the inverse of the absolute value of the
smallest magnitude eigenvalue of $A$.

We see in the code above that the large disparity in eigenvalues of $A$
leads to an effect predictable from our inequality above, with the
condition number helping us find an upper bound.

```r
e <- eigen(A)
norm2(x - xPerturbed)  ## delta x
norm2(b - bPerturbed)  ## delta b
norm2(x - xPerturbed)/norm2(x)
(e$val[1]/e$val[4])*norm2(b - bPerturbed)/norm2(b)
```


The main use of these ideas for our purposes is in thinking about the
numerical accuracy of a linear system solution (Gentle-NLA Sec 3.4). On
a computer we have the system $$(A+\delta A)(x+\delta x)=b+\delta b$$
where the 'perturbation' is from the inaccuracy of computer numbers. Our
exploration of computer numbers tells us that
$$\frac{\|\delta b\|}{\|b\|}\approx10^{-p};\,\,\,\frac{\|\delta A\|}{\|A\|}\approx10^{-p}$$
where $p=16$ for standard double precision floating points. Following
Gentle, one gets the approximation

$$\frac{\|\delta x\|}{\|x\|}\approx\mbox{cond}(A)10^{-p},$$ so if
$\mbox{cond}(A)\approx10^{t}$, we have accuracy of order $10^{t-p}$
instead of $10^{-p}$. (Gentle cautions that this holds only if
$10^{t-p}\ll1$). So we can think of the condition number as giving us
the number of digits of accuracy lost during a computation relative to
the precision of numbers on the computer. E.g., a condition number of
$10^{8}$ means we lose 8 digits of accuracy relative to our original 16
on standard systems. One issue is that estimating the condition number
is itself subject to numerical error and requires computation of
$A^{-1}$ (albeit not in the case of $L_{2}$ norm with square,
nonsingular $A$) but see Golub and van Loan (1996; p. 76-78) for an
algorithm.

#### Improving conditioning

Ill-conditioned problems in statistics often arise from collinearity of
regressors. Often the best solution is not a numerical one, but
re-thinking the modeling approach, as this generally indicates
statistical issues beyond just the numerical difficulties.

A general comment on improving conditioning is that we want to avoid
large differences in the magnitudes of numbers involved in a
calculation. In some contexts such as regression, we can center and
scale the columns to avoid such differences - this will improve the
condition of the problem. E.g., in simple quadratic regression with
$x=\{1990,\ldots,2010\}$ (e.g., regressing on calendar years), we see
that centering and scaling the matrix columns makes a huge difference on
the condition number

```r
t1 <- 1990:2010  # naive covariate
X1 <- cbind(rep(1, 21), t1, t1^2)
e1 <- eigen(crossprod(X1))
e1$values

t2 <- t1 - 2000 # centered
X2 <- cbind(rep(1, 21), t2, t2^2)
e2 <- eigen(crossprod(X2))
e2$values

t3 <- t2/10 # centered and scaled
X3 <- cbind(rep(1, 21), t3, t3^2)
e3 <- eigen(crossprod(X3))
e3$values
```


The basic story is that simple strategies often solve the problem, and
that you should be cognizant of the absolute and relative magnitudes
involved in your calculations.

One rule of thumb is to try to work with numbers whose magnitude is
around 1. We can often scale the values in our problem in order to do
this. I.e., change the units of your variables. Instead of personal
income in dollars, use personal income in thousands or hundreds of
thousands of dollars.

---

[← generate a realization](04-generate-a-realization.md) · [Up: contents](index.md) · [4. Matrix factorizations (decompositions) and solving systems of linear equations →](06-4-matrix-factorizations-decompositions-and-solving-systems-o.md)
