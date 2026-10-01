---
title: "28. R Practice: Structures, Functions, I/O"
course: "Berkeley Stat 243"
chapter: 28
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 28. R Practice: Structures, Functions, I/O

## What this covers

This chapter works through a self-contained practice worksheet from the STAT 243 discussion sections: building
and subsetting basic R data structures, writing vectorized code instead of loops, using the `apply` family of
functions, writing small functions with defensive input-checking, and reading and saving data files. It assumes
the reader already knows the material from the course's R bootcamp — vectors, indexing, control flow — since the
worksheet itself points there for anything not covered below.

## Vectors, factors, and data frames

R's basic containers are vectors (numeric, character, or logical), factors, and data frames. A vector is built
from a fixed-length sequence of values of one type; `seq` and `rep` are the two general tools for generating one
without typing out every element, and comparison operators applied to a vector return a logical vector of the
same length, one entry per element. A factor is a vector of category labels together with the fixed list of
levels those labels are allowed to take; `factor()` converts a character vector into one.

A data frame is a list of column vectors of equal length, given column names, and displayed as a table; unlike a
matrix, its columns need not all be the same type. Building one from several vectors already computed
separately — rather than typing the data in — is the natural way to construct it once each column is a vector of
the right length. A data frame's row labels are a distinct piece of metadata from any of its columns: a vector
can be used as `row.names` instead of as a column, which changes what `df[i, ]` returns and whether the values are reachable as a column at all.

## Subsetting

The subsetting operations for a matrix or data frame are indexing by position, by name, and by a logical vector
of the same length as the dimension being indexed — the last of these is what lets you keep only the rows
satisfying a condition without writing a loop over rows. A matrix converted from a data frame keeps only the
values, dropping the column names and the possibility of mixed column types that a data frame allows.

## Vectorized calculation, `outer`, and the `apply` family

R's arithmetic and elementary functions (`exp`, `sqrt`, `cos`, and so on) are vectorized: applied to a vector,
they return a vector of the function applied elementwise, so an expression like $e^{2x}x^{\sqrt{x}}$ evaluates at
an entire grid of $x$ values in one call, with no explicit loop. `row(x)` and `col(x)` return matrices, the same
shape as `x`, holding the row index and the column index of each entry; the difference `row(x) - col(x)` is
therefore the distance of each entry from the diagonal, which is what a banded or distance-from-diagonal pattern
in a matrix is built from. `outer(a, b, FUN)` builds a matrix whose $(i,j)$ entry is `FUN(a[i], b[j])`, and is
the direct way to build a matrix from an addition (or other two-argument) table over two index vectors, including
one that wraps around using the remainder after division.

`apply(X, margin, FUN)` applies `FUN` to each row (`margin = 1`) or column (`margin = 2`) of a matrix and
collects the results; because it always calls `FUN` once per row or column, a purpose-built summary such as
`rowSums` is faster on a large matrix even though the two compute the same numbers. `sapply` and `lapply` do the
analogous thing over the elements of a list: `lapply` always returns a list, one element per input element,
while `sapply` tries to simplify that list into a vector or matrix when the results are all the same length and
type, and falls back to a list when they are not — which is why the two can return objects of different classes
applied to the same object, depending on what is inside it.

## Writing functions

`stopifnot(condition)` stops the function with an error if `condition` is not `TRUE`, and is the standard way to
check that an argument satisfies a type or shape assumption before the rest of the function body relies on it.
A function argument can be given a default value in its definition (`na.rm = FALSE`), so that a caller only needs
to supply it to change the default behaviour, such as removing `NA`s before a computation.

`sample()` draws a random sample, and, used with `replace = TRUE`, is the standard way to simulate coin flips or
any other draw with replacement. `set.seed()` fixes the state of R's random number generator, so that a call to
`sample` (or any other random-number function) after it is reproducible; calling it once before a sequence of
random draws you want to be able to reproduce is the usual pattern, whereas calling it inside a function that is
meant to be called many times — as in generating many independent simulation replicates — would reset the
generator to the same state on every call and make every replicate identical. `replicate(n, expr)` evaluates
`expr` `n` times and collects the results, which is the tool for running a stochastic function many times to
build up a distribution of its output, such as a histogram of simulated outcomes.

A function can branch on the value of a character argument (its `operation`) using conditional logic, with a
final branch that issues a `warning` when the argument does not match any of the expected cases. Finally,
`cumsum(x)` is R's built-in cumulative sum; writing the same computation explicitly with a `for` loop that keeps
a running total is a way to check, by comparison with the built-in, that the loop's logic is right — the general
technique for reimplementing a vectorized built-in in order to understand what it does.

## Loading and saving data

Reading a file into R takes its path, not its name alone: the exercises deliberately keep the data file where it
is and require either a full path or a path relative to the current location, rather than copying the file
alongside the script or changing the working directory to match it. Stata `.dta` files, CSV files, and
whitespace-delimited text files each need their own reading function; once loaded, `class`, `str`, `length`,
`dim`, and `sapply` (applied over the columns) are the standard tools for finding out what kind of object came
back and what is in it.

Saving part or all of the current workspace to an `.RData` file with `save`, and reading it back with `load` in a
fresh R session, is how objects are carried between sessions without recomputing them; `ls()` lists what is
currently in the workspace, which is how you check that a fresh session starts empty and that `load` puts back
what `save` wrote out.

## Exercises

*(From the STAT 243 "R Practice" worksheet; assumes R bootcamp modules 1-4 and 6.)*

### Creating vectors and a data frame

1. Create the following vectors:
   a. $1, 2, 3, \dots, 49, 50$
   b. a logical vector that is `TRUE` exactly when the corresponding element of (a) is even
   c. $50, 49, \dots, 3, 2, 1$
   d. $1, 2, 3, \dots, 49, 50, 49, \dots, 3, 2, 1$
   e. $-10, -9, -8, \dots, 8, 9, 10$
   f. $3, 6, 9, \dots, 45, 48$
   g. `"3", "6", "9", ..., "45", "48"` (build it from the vector in (f))
   h. `"a", "a", "a", "a", "b", "b", "b", "c", "c", "d"` (using `rep`)
   i. the character vector from (h), turned into a factor
   j. 200 numbers between $-1$ and $1$ inclusive (using `seq`)

2. Build a data frame `df1`:
   a. a vector $1, 2, \dots, 50$ called `x`
   b. `y`, the cosine of `x`
   c. `z`, the tangent of `y`
   d. `w`, the elementwise product of `y` and `z`
   e. a logical vector `f` that is `TRUE` exactly when `x` is between 10 and 29 inclusive
   f. a data frame `df1` with columns `x, y, z, w, f` in that order
   g. how would you change the column names of `df1` to uppercase?
   h. what would you have done differently to use `x` as row names instead of as a column — and would you still have needed to construct `x` first?

### Subsetting data structures

1. a. a matrix `m1` of only the numeric columns of `df1`
   b. a matrix `m2` of only the rows of `df1` where `f` is `TRUE`
   c. a data frame `df2` of only the rows where `z` is non-negative, with all columns except `z`
   d. a data frame `df3` that is `df1` without its 3rd and 17th rows
   e. a data frame `df4` of only the even-numbered rows of `df1`

### Vectorized calculations

1. A vector of values $e^{2x}x^{\sqrt{x}}$ for $x = 1, 1.1, 1.2, \dots, 2.9, 3.0$.

2. a. a $5\times5$ matrix of zeros called `x`
   b. inspect what `row(x)` and `col(x)` return
   c. using `row(x)` and `col(x)`, build
   $$\begin{pmatrix}
   0 & 1 & 0 & 0 & 0 \\
   1 & 0 & 1 & 0 & 0 \\
   0 & 1 & 0 & 1 & 0 \\
   0 & 0 & 1 & 0 & 1 \\
   0 & 0 & 0 & 1 & 0
   \end{pmatrix}$$
   d. using `row(x)` and `col(x)`, build
   $$\begin{pmatrix}
   0 & 1 & 2 & 3 & 4 \\
   1 & 0 & 1 & 2 & 3 \\
   2 & 1 & 0 & 1 & 2 \\
   3 & 2 & 1 & 0 & 1 \\
   4 & 3 & 2 & 1 & 0
   \end{pmatrix}$$

3. Using `outer` (look at its `FUN` argument):
   a. $$\begin{pmatrix}
   0 & 1 & 2 & 3 & 4 \\
   1 & 2 & 3 & 4 & 5 \\
   2 & 3 & 4 & 5 & 6 \\
   3 & 4 & 5 & 6 & 7 \\
   4 & 5 & 6 & 7 & 8
   \end{pmatrix}$$
   b. modify (a) to get
   $$\begin{pmatrix}
   0 & 1 & 2 & 3 & 4 \\
   1 & 2 & 3 & 4 & 0 \\
   2 & 3 & 4 & 0 & 1 \\
   3 & 4 & 0 & 1 & 2 \\
   4 & 0 & 1 & 2 & 3
   \end{pmatrix}$$

### `apply`, `sapply`, `lapply`

1. Normalize rows and columns:
   a. a $5\times6$ matrix `m1` of numbers drawn uniformly from $(1, 100)$
   b. a matrix `m2`, using `apply` with a small function you write, that normalizes the rows of `m1` to sum to 1; check the dimensions of `m2` against `m1` — are they the same, and why?
   c. verify with `apply` that the rows of `m2` sum to 1, then verify again with `rowSums` — why prefer `rowSums` to `apply` here?
   d. repeat (b)-(c), normalizing the columns instead

2. A linear model:
   a. a vector `x` of $1, 1.1, 1.2, \dots, 9.9, 10.0$
   b. a vector `y` equal to twice `x` plus standard Gaussian noise
   c. a scatterplot of `y` against `x`
   d. an `lm` object `my_lm` regressing `y` on `x`
   e. the classes of the elements of `my_lm`, using `lapply`
   f. the classes of the elements of `my_lm`, using `sapply`
   g. do the two differ? Why, or why not — and when in general would they?

### Functions

1. A function returning the sum of absolute deviations from the median of a numeric vector `x`:
   a. check that `x` is numeric (using `stopifnot`)
   b. add an `na.rm` argument, defaulting to `FALSE`, that removes `NA`s from the computation when `TRUE`

2. Simulating a coin toss:
   a. sample, with replacement, a vector `x` of 100 0s and 1s, then do it again and call it `y` — would it make sense to call `set.seed` before doing this, and why?
   b. write `sumHeads(n)` returning the number of heads (coded as 1) in `n` simulated flips — would it make sense to call `set.seed` inside the body of this function, and why or why not?
   c. build a vector `sums_vec` of 10,000 calls to `sumHeads(200)` (using `replicate`)
   d. plot a histogram of `sums_vec`

3. A function of two numeric vectors `x`, `y`, and an argument `operation` defaulting to `"add"`:
   a. if `operation` is `"add"`, return `x + y`
   b. if `"subtract"`, return `x - y`
   c. if `"multiply"`, return `x * y`
   d. if `"divide"`, return `x / y`
   e. otherwise, issue a warning that the operation is unknown

4. A function returning the cumulative sum of a vector `x`, implemented with a `for` loop — check the result against R's built-in `cumsum`.

### Loading and saving data

1. Load the earnings data (e.g. `sections/01/data/heights.dta`, from the course's Github repository) without copying it locally or changing the working directory; call the result `earnings`.
   a. what does `class(earnings)` return?
   b. what does `str(earnings)` return?
   c. what does `length(earnings)` return?
   d. what does `dim(earnings)` return?
   e. use `sapply` to find the class of each column of `earnings`
   f. use `sapply` to run `summary` on just the height-related columns

2. Load a CSV file (e.g. `sections/01/data/cpds.csv`) and a whitespace-delimited text file (e.g. `sections/01/data/stateIncome.txt`).

3. Saving R objects:
   a. use `ls()` to see what is in your workspace
   b. save some of those objects to an `.RData` file in the directory above your current one
   c. open a fresh R session
   d. confirm the new session's workspace is empty
   e. load the `.RData` file you saved
   f. use `ls()`, `class()`, `str()`, `names()`, and anything else useful, to examine what was loaded

## Sources

- `01-creating-datastructures.md` (STAT 243 "R Practice" worksheet, sections "Creating datastructures" through
  "Using apply, sapply, and lapply"), converted from `sections/RPractice/R-practice.pdf` in the
  berkeley-stat243/stat243-fall-2021 repository.
- `02-functions.md` (same worksheet, "Functions" section).
- `03-loading-and-saving-data.md` (same worksheet, "Loading (and saving) data" section).
- The worksheet itself refers to, but does not supply, "modules 1-4 and 6 of the R bootcamp" and the data files
  `sections/01/data/heights.dta`, `cpds.csv`, and `stateIncome.txt` from the course's 2020 Github repository;
  none of these are among the material given here.
- All three converted files note that the source PDF had no extractable text layer and was reconstructed by a
  model, so the exact original wording (and the matrices transcribed above) are marked unverified against the PDF.

---

[← 27. Python Fundamentals for R Users](27-python-fundamentals-for-r-users.md) · [Contents](index.md) · [29. Installing R & RStudio →](29-installing-r-rstudio.md)
