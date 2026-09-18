---
title: Creating datastructures
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/RPractice/R-practice.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`sections/RPractice/R-practice.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Creating datastructures

Jarrod Millman, Jared Bennett
Update: Zoe Vernon
Statistics 243
UC Berkeley

Updated August, 27, 2020

This is a set of practices to help build a basic working knowledge of R. For those of you who feel like the extra practice is useful we will work on these problems in groups in the first section of Friday 8/28 and go over solutions. This is not a graded assignment. I will post the solutions to the sections 01 folder on Github early next week. Most of the information you will need is covered in modules 1-4 and 6 of the R bootcamp. If not, it will be noted (you are also expected to be able to pick up new functions when needed).

1. Create the following vectors:
   (a) 1, 2, 3, ..., 49, 50
   (b) a logical vector that is TRUE exactly when the corresponding element of the above vector is even
   (c) 50, 49, ..., 3, 2, 1
   (d) 1, 2, 3, ..., 49, 50, 49, ..., 3, 2, 1
   (e) -10, -9, -8, ..., 8, 9, 10
   (f) 3, 6, 9, ..., 45, 48
   (g) "3", "6", "9", ..., "45", "48" (Hint: use the previous vector)
   (h) "a", "a", "a", "a", "b", "b", "b", "c", "c", "d" (Hint: use rep)
   (i) turn the above character vector into a factor vector
   (j) 200 numbers between -1 and 1 (inclusive) (Hint: use seq)

2. Create a data frame through the following steps:
   (a) Create a vector 1, 2, 3, ..., 49, 50 and call it `x`
   (b) Create a vector by taking the cosine of `x` and call it `y`
   (c) Create a vector by taking the tagent of `y` and call it `z`
   (d) Create a vector by multiplying the elements of `y` and `z` and call it `w`
   (e) Create a logical vector that is TRUE exactly when `x` is between 10 and 29 inclusively and call it `f`
   (f) Create a data frame with column names `x`, `y`, `z`, `w`, `f` in that order with the obvious content and call it `df1`
   (g) How would you change the names of `df1` to uppercase letters?
   (h) What would you have done differently if you wanted to use `x` as the row names instead of making it a column? Would you have needed to use `x`?

## Subsetting datastructures

1. Create the following:
   (a) Create a matrix with only the numeric elements of `df1` and call it `m1`
   (b) Create a new matrix `m2` with only the rows where `df1$f` is TRUE
   (c) Create a new data frame `df2` with only the rows where `z` is non-negative and has all columns but `z`
   (d) Create a new data frame `df3` without the 3rd and 17th rows of `df1`
   (e) Create a new data frame `df4` with only the even rows of `df1`

## Vectorized calculations

1. Create a vector of values $e^{2x} x^{\sqrt{x}}$ for $x = 1, 1.1, 1.2, \dots, 2.9, 3.0$.

2. Create the following:
   (a) A $5 \times 5$ matrix of zeros called `x`
   (b) See what `row(x)` and `col(x)` return
   (c) Using `row(x)` and `col(x)` create the following matrix:
   $$\begin{pmatrix}
   0 & 1 & 0 & 0 & 0 \\
   1 & 0 & 1 & 0 & 0 \\
   0 & 1 & 0 & 1 & 0 \\
   0 & 0 & 1 & 0 & 1 \\
   0 & 0 & 0 & 1 & 0
   \end{pmatrix}$$
   (d) Using `row(x)` and `col(x)` create the following matrix:
   $$\begin{pmatrix}
   0 & 1 & 2 & 3 & 4 \\
   1 & 0 & 1 & 2 & 3 \\
   2 & 1 & 0 & 1 & 2 \\
   3 & 2 & 1 & 0 & 1 \\
   4 & 3 & 2 & 1 & 0
   \end{pmatrix}$$

3. Create the following matrices:
   (a) Using the R `outer` function (hint: look at its `FUN` argument)
   $$\begin{pmatrix}
   0 & 1 & 2 & 3 & 4 \\
   1 & 2 & 3 & 4 & 5 \\
   2 & 3 & 4 & 5 & 6 \\
   3 & 4 & 5 & 6 & 7 \\
   4 & 5 & 6 & 7 & 8
   \end{pmatrix}$$
   (b) Modify what you did above
   $$\begin{pmatrix}
   0 & 1 & 2 & 3 & 4 \\
   1 & 2 & 3 & 4 & 0 \\
   2 & 3 & 4 & 0 & 1 \\
   3 & 4 & 0 & 1 & 2 \\
   4 & 0 & 1 & 2 & 3
   \end{pmatrix}$$

## Using apply, sapply, and lapply

1. Normalize rows and columns
   (a) Create a $5 \times 6$ matrix of numbers uniformly drawn from the interval $(1, 100)$ call it `m1`.
   (b) Create a new matrix `m2` using `apply` to normalize the rows so that they sum to 1. You will need to write a little function to use inside of the `apply` call. Check the dimensions of `m2`. Are they the same as `m1`? Why?
   (c) Use `apply` on `m2` to verify that the rows sum to 1. Now use `rowSums` to do the same thing. Why would you use `rowSums` instead of `apply`.
   (d) Repeat the last two steps but normalize the columns.

2. Linear model
   (a) Create a vector `x` containing 1, 1.1, 1.2, ..., 9.9, 10.0
   (b) Create a vector `y` that is twice `x` but with standard Gaussian noise added
   (c) Create a scatterplot
   (d) Create an `lm` object where `y` depends on `x` called `my_lm`
   (e) Use `lapply` to find the classes of the elements of `my_lm`
   (f) Use `sapply` to find the classes of the elements of `my_lm`
   (g) Do they differ? Why or why not? When would they differ and when would they be the same?

---

[Up: contents](index.md) · [Functions →](02-functions.md)
