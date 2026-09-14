---
title: 3. Computational issues
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Computational issues

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

1.  Collect the inner products of the rows of $A$ with $x$.\

```
        # initialize b[1:n]=0
        for(i=1:n) {
            for(j=1:m){
                b_i = b_i + a_{ij} x_j
            }
        }
```

2.  Take the linear combination (based on $x$) of the columns of $A$\

```
        # initialize b[1:n]=0
        for(j=1:m){
            for(i = 1:n){
                b_i = b_i + a_{ij} x_j
            }
        }
```

In this case the two approaches involve the same number of operations.
But the first accesses $A$ by row, so it might be better for row-major matrices (so might be how we
would implement in C). The second accesses $A$ by column, so it might be better for column-major matrices (so might be how
we would implement in Fortran).

!!! tip "Tip"
Check whether the first
approach is faster in Python with numpy's default row-major ordering.
(Write the code just doing the outer loop as a for loop and
doing the inner loop using vectorized calculation.) Your answer will
probably depend on how big the matrices are.
:::

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

```python
def norm2(x):
    return(np.sum(x**2) ** 0.5)

A = np.array([[10,7,8,7],[7,5,6,5],[8,6,10,9],[7,5,9,10]])
b = np.array([32,23,33,31])
x = np.linalg.solve(A, b)

bPerturbed = np.array([32.1, 22.9, 33.1, 30.9])
xPerturbed = np.linalg.solve(A, bPerturbed)

delta_b = bPerturbed - b
delta_x = xPerturbed - x
```


What's going on? Some manipulations with inequalities involving the
induced matrix norm (for any chosen vector norm, but we might as well
just think about the Euclidean norm) (see Gentle-CS Sec. 5.1 or the derivation in class) give
$$\frac{\|\delta x\|}{\|x\|}\leq\|A\|\|A^{-1}\|\frac{\|\delta b\|}{\|b\|}$$
where we define the condition number w.r.t. inversion as
$\mbox{cond}(A)\equiv\|A\|\|A^{-1}\|$. We'll generally work with the
$L_{2}$ norm, and for a nonsingular square matrix the result is that the
condition number is the ratio of the absolute values of the largest and
smallest magnitude eigenvalues. This makes sense since $\|A\|_{2}$ is
the absolute value of the largest magnitude eigenvalue of $A$ and
$\|A^{-1}\|_{2}$ is the absolute value of the largest magnitude eigenvalue of $A^{-1}$.
But since the eigenvalues of the inverse are the inverses of the eigenvalues of $A$,
the latter is the inverse of the absolute value of the smallest magnitude eigenvalue of $A$.

We see in the code below that the large disparity in eigenvalues of $A$
leads to an effect predictable from our inequality above, with the
condition number helping us find an upper bound.

```python
e = np.linalg.eig(A)
evals = e[0]
print(evals)

## relative perturbation in x much bigger than in b
norm2(delta_x) / norm2(x)
norm2(delta_b) / norm2(b)

## ratio of relative perturbations
(norm2(delta_x) / norm2(x)) / (norm2(delta_b) / norm2(b))

## ratio of largest and smallest magnitude eigenvalues
## confusingly evals[2] is the smallest, not evals[3]
(evals[0]/evals[2])
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

```python
import statsmodels.api as sm
rng = np.random.default_rng(seed=1)

t1 = np.arange(1990, 2011)  # naive covariate
n = len(t1)
X1 = np.column_stack((np.ones(n), t1, t1 ** 2))

beta = np.array([5, 0.1, 0.0001])
y = X1 @ beta + rng.normal(size = n)

e1 = np.linalg.eig(X1.T @ X1)
np.sort(e1[0])[::-1]
np.linalg.cond(X1.T @ X1)  # built-in!
sm.OLS(y, X1).fit().params
```

The fitted values are quite different than the true beta values of (5, 0.1, 0.0001), particularly the intercept and linear terms. This is primarily because of the ill-conditioning, rather than that the OLS estimate
is different than the true values because we are estimating beta.

Now we'll do a simple transformation, subtracting off the mean of the covariate,
so that the covariate values (in particular the quadratic values) don't have such large magnitudes.

```python
t2 = t1 - 2000              # centered
X2 = np.column_stack((np.ones(n), t2, t2 ** 2))
e2 = np.linalg.eig(X2.T @ X2)
with np.printoptions(suppress=True):
    print(np.sort(e2[0])[::-1])
sm.OLS(y, X2).fit().params
```

We can work out that the effect of centering is that the true beta values
after centering are (605, 0.5, 0.0001). (Consider $\beta_0 + \beta_1(t-c+c) + \beta_2(t-c+c)^2$ for $c=2000$.) So for the intercept and linear term, the OLS estimates are now pretty similar to the true values.

Interestingly, the estimate for the quadratic terms has not changed at all. This is quite surprising. There must be something subtle going on that causes that not to be affected by the bad conditioning, but I'm not sure what is happening there.

We could go even further to improve the conditioning.

```python
t3 = t2/10                  # centered and scaled
X3 = np.column_stack((np.ones(n), t3, t3 ** 2))
e3 = np.linalg.eig(X3.T @ X3)
with np.printoptions(suppress=True):
    print(np.sort(e3[0])[::-1])
```

I haven't shown the OLS results for the third version,
but with a bit of arithmetic to be done,
but you should be able to verify that the third
approach also gives reasonable answers.


The basic story is that simple strategies often solve the problem, and
that you should be aware of the absolute and relative magnitudes
involved in your calculations.

One rule of thumb is to try to work with numbers whose magnitude is
around 1. We can often scale the values in our problem in order to do
this. I.e., change the units of your variables. Instead of personal
income in dollars, use personal income in thousands or hundreds of
thousands of dollars.

---

[← Generate a realization.](05-generate-a-realization.md) · [Up: contents](index.md) · [4. Matrix factorizations (decompositions) and solving systems of linear equations →](07-4-matrix-factorizations-decompositions-and-solving-systems-o.md)
