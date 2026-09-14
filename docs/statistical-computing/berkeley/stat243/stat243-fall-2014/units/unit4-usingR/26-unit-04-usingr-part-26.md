---
title: Unit 04 — usingR Part 26 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 26 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This can get confusing, but can be very powerful. Basically, I’m calculating the min for each element of the second dimension in the second-to-last example and for each pair of elements in the first and third dimensions in the final example. Caution: if the result of each subcalculation is a vector, these will be _cbind()_ ’ed together (recall column-major order), so if you used _apply()_ on the row margin, you’ll need to transpose the result.

**Why use apply(), lapply(), etc.?** The various _apply()_ functions (apply, lapply, sapply, tapply, etc.) may be faster than a loop (when a substantial part of the work lies in the overhead of the looping), but if the dominant part of the calculation lies in the time required by the function on each of the elements, then the main reason for using an _apply()_ variant is code clarity. Here’s an example where _apply()_ is not faster than a loop.

29

n <- 5e+05 nr <- 10000 nCalcs <- n/nr mat <- **matrix** ( **rnorm** (n), nrow = nr) times <- 1:nr **system.time** (out1 <- **apply** (mat, 2, **function** (vec) { mod = **lm** (vec ~ times) **return** (mod$coef[2]) })) ## user system elapsed ## 0.844 0.000 0.847 **system.time** ({ out2 = **rep** (NA, nCalcs) **for** (i **in** 1:nCalcs) { out2[i] = **lm** (mat[, i] ~ times)$coef[2] } }) ## user system elapsed ## 0.604 0.000 0.607

### **4.3 Long and wide formats**

Finally, we may want to convert between so-called ’long’ and ’wide’ formats, which are motivated by working with longitudinal data (multiple observations per subject). The wide format has repeated measurements for a subject in separate columns, while the long format has repeated measurements in separate rows, with a column for differentiating the repeated measurements. _stack()_ converts from wide to long while _unstack()_ does the reverse. _reshape()_ is similar but more flexible and it can go in either direction. The wide format is useful for doing separate analyses by group, while the long format is useful for doing a single analysis that makes use of the groups, such as ANOVA or mixed models. Let’s use the precipitation data as an example.

**load** ("../data/prec.RData") prec <- prec[1:1000, ] _# just to make the example code run faster_ precVars <- 5: **ncol** (prec)

30

precStacked <- **stack** (prec, select = precVars) out <- **unstack** (precStacked) _# to use reshape, we need a unique id for each row since # reshape considers each row in the wide format as a # subject_ prec <- **cbind** (unique = 1: **nrow** (prec), prec) precVars <- precVars + 1 precLong <- **reshape** (prec, varying = **names** (prec)[precVars], idvar = "unique", direction = "long", sep = "") precLong <- precLong[! **is.na** (precLong$prec), ] precWide <- **reshape** (precLong, v.names = "prec", idvar = "unique", direction = "wide", sep = "")

Check out _melt()_ and _cast()_ in the _reshape2_ package for easier argument formats than _reshape()_ .

### **4.4 Linear algebra**

We’ll focus on matrices here. A few helpful functions are _nrow()_ and _ncol()_ , which tell the dimensions of the matrix. The _row()_ and _col()_ functions will return matrices of the same size as the original, but filled with the row or column number of each element. So to get the upper triangle of a matrix, _X_ , we can do:

X <- **matrix** ( **rnorm** (9), 3) X ## [,1] [,2] [,3] ## [1,] -1.525 -0.514 -0.225 ## [2,] 1.600 -0.953 1.804 ## [3,] -0.685 -0.338 0.354 X[ **col** (X) >= **row** (X)] ## [1] -1.525 -0.514 -0.953 -0.225 1.804 0.354

See also the _upper.tri()_ and _lower.tri()_ functions, as well as the _diag()_ function. _diag()_ is quite handy - you can extract the diagonals, assign into the diagonals, or create a diagonal matrix:

31

**diag** (X) ## [1] -1.525 -0.953 0.354 **diag** (X) <- 1 X ## [,1] [,2] [,3] ## [1,] 1.000 -0.514 -0.225 ## [2,] 1.600 1.000 1.804 ## [3,] -0.685 -0.338 1.000 d <- **diag** ( **c** ( **rep** (1, 2), **rep** (2, 2))) d ## [,1] [,2] [,3] [,4] ## [1,] 1 0 0 0 ## [2,] 0 1 0 0 ## [3,] 0 0 2 0 ## [4,] 0 0 0 2

To transpose a matrix, use _t()_ , e.g., t(X).

**Basic operations** The basic matrix-vector operations are:

X %*% Y _# matrix multiplication_ X * Y _# direct product_ x %o% y _# outer product of vectors x, y: x times t(y)_ **outer** (x, y) _# same thing # evaluation of f(x,y) for all pairs of x,y values:_ **outer** (x, y, **function** (x, y) **cos** (y)/(1 + x^2)) **crossprod** (X, Y) _# same as but faster than t(X) %*% Y!_

For inverses ( _X_<sup>_−_1</sup> ) and solutions of systems of linear equations ( _X_<sup>_−_1</sup> _y_ ):

**solve** (X) _# inverse of X_ **solve** (X, y) _# (inverse of X) %*% y_

32

Note that if all you need to do is solve the linear system, you should never explicitly find the inverse, UNLESS you need the actual matrix, e.g., to get a covariance matrix of parameters.

Otherwise, to find many solutions, all with the same matrix, _X_ , you can use _solve()_ with the second argument being a matrix with each column a different ’y’ vector for which you want the solution.

_solve()_ is an example of using a matrix decomposition to solve a system of equations (in particular the LU decomposition). We’ll defer matrix decompositions (LU, Cholesky, eigendecomposition, SVD, QR) until the numerical linear algebra unit.

---

[← Unit 04 — usingR Part 25 —](25-unit-04-usingr-part-25.md) · [Up: contents](index.md) · [5 Flow control and logical operations →](27-5-flow-control-and-logical-operations.md)
