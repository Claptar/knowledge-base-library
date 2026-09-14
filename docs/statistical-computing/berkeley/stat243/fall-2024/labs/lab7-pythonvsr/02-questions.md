---
title: Questions
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab7-pythonvsr.qmd
source_file: sources/berkeley-stat243/fall-2024/labs/lab7-pythonvsr.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Questions

**Source:** [`labs/lab7-pythonvsr.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/labs/lab7-pythonvsr.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

### Main Questions

!!! tip "Tip"
Ideally, you will make it through all of these, although if you run out of time
that is okay.

:::

1. Do R functions behave like pass-by-value or pass-by-reference? In other
words, if you pass in an object and modify it, does that affect the value of the
object in the environment from which the function was called? Check this for a
scalar, a list, and an R vector.

2. Can R lists and vectors be modified in place, without copying the
   object?

   For this the function `.Internal(inspect)` will be helpful.
   Here's an example for a list.

```
#| eval: false
x <- list(7, c('abc', 'def'), rnorm(5))
.Internal(inspect(x))

@5652776540f8 19 VECSXP g0c3 [REF(1)] (len=3, tl=0)
@5652776b9740 14 REALSXP g0c1 [REF(3)] (len=1, tl=0) 7
@56527580b0d8 16 STRSXP g0c2 [REF(1)] (len=2, tl=0)
@5652776b97b0 09 CHARSXP g0c1 [REF(4),gp=0x60] [ASCII] [cached] "abc"
@565275b60168 09 CHARSXP g0c1 [MARK,REF(14),gp=0x61] [ASCII] [cached] "def"
@565275a97478 14 REALSXP g0c4 [REF(1)] (len=5, tl=0) -0.38248,-0.100364,-0.485605,1.15111,-0.111647

#`5652776540f8` is the address of the overall list.
#`5652776b9740` of the 1-element vector containing '7'.
#`56527580b0d8` is the address of the character vector.
#`565275a97478` is the address of the vector of random numbers.
```

3. Does R behave similarly to Python in terms of storing strings, as seen in PS4?

4. If you make a copy of an R vector does it use the same memory as the
original vector and does changing an element of the original vector affect the
copy of the vector?

5. How does variable scoping work in R - does it use lexical scoping and
look for variables in the environment where a function was defined?

6. Can you create a closure with embedded data, like we did in Python?


### Additional Questions

!!! tip "Tip"
Work on these if you finish quickly/are curious. Note that quick operations can
be tricky to time meaningfully. The `microbenchmark` function from the R
`microbenchmark` package is useful in such cases.

:::

1. Consider the relative efficiency of `for` loops versus vectorized
calculations vs. `apply` for numeric vectors in R and see how it compares to
the equivalent operations in python.

2. Can you determine if the speed of looking up values in a named vector varies
with the size of the vector (this will indicate if something like hashing is
going on or if the lookup has to scan through all the elements).

---

[← Lab7 pythonvsr Part 01 —](01-lab7-pythonvsr-part-01.md) · [Up: contents](index.md) · [Acknowledgements →](03-acknowledgements.md)
