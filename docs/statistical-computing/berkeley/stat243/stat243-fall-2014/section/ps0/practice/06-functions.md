---
title: Functions
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/ps0/practice.tex
source_file: sources/berkeley-stat243/stat243-fall-2014/section/ps0/practice.tex
licence: unresolved
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Functions

**Source:** [`section/ps0/practice.tex`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/section/ps0/practice.tex) · **Licence:** unresolved · Converted 2026-09-14 from `.tex` (high)

1.  Write a function which returns the sum of the absolute deviations from the median of an input vector x. Add the following:

    1.  Make sure the input vector x is numeric (hint: use R’s ? function to find out how to use `stopifnot`)

    2.  An additional argument `na.rm` which is a logical. If it is `TRUE`, the function removes all the NAs from the computation of the return value. Give it a default value of `FALSE`.

2.  Simulate a coin toss

    1.  Use the `sample` function to sample with replacement a vector of 0s and 1s with 100 elements. Call this `x`. Do it again and call it `y`. Would it make sense to call `set.seed` before calling `sample`? Why?

    2.  Write a function `sum_heads` that takes as input the number of desired coin flips and returns the number of heads (assume heads are coded by 1). Would it make sense to call `set.seed` in the body of your function? Why?

    3.  Create a new vector `sums` by calling `sum_heads(200)` 10,000 times. (Hint: use `replicate`)

    4.  Plot a histogram of `sums`

3.  Write a function that takes two numeric vectors `x` and `y` as well as a variable `operation` with a default value of `"add"`.

    1.  If `operation` is `"add"`, return `x+y`

    2.  If `operation` is `"subtract"`, return `x-y`

    3.  If `operation` is `"multiply"`, return `x*y`

    4.  If `operation` is `"divide"`, return `x/y`

    5.  If `operation` isn’t one of the above, return a warning that `operation` is unknown.

4.  Write a function that takes a vector `x` and returns a vector containing the cumulative sum vector. Note that R provides a builtin function `cumsum` that you can use to verify that your function works. You should implement this function using a `for` loop to make sure you understand how it works.

---

[← Using apply, sapply, and lapply](05-using-apply-sapply-and-lapply.md) · [Up: contents](index.md) · [Loading (and saving) data →](07-loading-and-saving-data.md)
