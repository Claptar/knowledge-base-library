---
title: Unit 04 — usingR Part 23 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 23 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In some cases you may actually need an object containing the subsets of the data, for which you can use _split()_ :

**<mark>split</mark>** <mark>(mtcars, mtcars$cyl)</mark>

To stratify based on a continuous variable, you can create a factor with the _cut()_ function. By default the levels are not formally ordered, but we can manipulate them with _relevel()_ , or make sure they’re ordered by using the _ordered_result_ argument to _cut()_ .

x <- **rnorm** (100) f <- **cut** (x, breaks = **c** (-Inf, -1, 1, Inf), labels = **c** ("low", "medium", "high")) **levels** (f) _# note that f is not explicitly ordered_ ## [1] "low" "medium" "high" f <- **relevel** (f, "high") _# puts high as first level_ f <- **cut** (x, breaks = **c** (-Inf, -1, 1, Inf), labels = **c** ("low", "medium", "high"), ordered_result = TRUE)

The _do.call()_ function will apply a function to the elements of a list. For example, we can _rbind()_ together (if compatible) the elements of a list of vectors instead of having to loop over the elements or manually type them in:

23

myList <- **list** (a = 1:3, b = 11:13, c = 21:23) **args** (rbind) ## function (..., deparse.level = 1) ## NULL **rbind** (myList$a, myList$b, myList$c) ## [,1] [,2] [,3] ## [1,] 1 2 3 ## [2,] 11 12 13 ## [3,] 21 22 23 **rbind** (myList) ## a b c ## myList Integer,3 Integer,3 Integer,3 **do.call** (rbind, myList) ## [,1] [,2] [,3] ## a 1 2 3 ## b 11 12 13 ## c 21 22 23

Why couldn’t we just use _rbind()_ directly? Basically we’re using _do.call()_ to use functions that take “...” as input (i.e., functions accepting an arbitrary number of arguments) and to use the list as the input instead (i.e., to use the list elements).

### **4.2 Vectors and matrices**

**Column-major vs. row-major matrix storage** Matrices in R are column-major ordered, which means they are stored by column as a vector of concatenated columns.

mat <- **matrix** ( **rnorm** (500), nr = 50) **identical** (mat[1:50], mat[, 1]) ## [1] TRUE **identical** (mat[1:10], mat[1, ])

24

---

[← 3 4 5 ## 4 21.5 26.9 28.2 ## 6 19.8 19.8 19.7 ## 8 15.1 NA 15.4](22-3-4-5-4-21-5-26-9-28-2-6-19-8-19-8-19-7-8-15-1-na-15-4.md) · [Up: contents](index.md) · [[1] FALSE vec <- c (mat) mat2 <- matrix (vec, nr = 50) identical (mat, mat2) ## [1] TRUE →](24-1-false-vec---c-mat-mat2---matrix-vec-nr-50-identical-mat-ma.md)
