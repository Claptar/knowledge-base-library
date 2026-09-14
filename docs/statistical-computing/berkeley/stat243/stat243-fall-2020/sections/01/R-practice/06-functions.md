---
title: Functions
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/R-practice.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/01/R-practice.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Functions

**Source:** [`sections/01/R-practice.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/R-practice.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Write a function which returns the sum of the absolute deviations from the median of an input vector x. Add the following:

   - (a) Make sure the input vector x is numeric (hint: use R’s ? function to find out how to use `stopifnot` )

   - (b) An additional argument `na.rm` which is a logical. If it is `TRUE` , the function removes all the NAs from the computation of the return value. Give it a default value of `FALSE` .

2. Simulate a coin toss

   - (a) Use the `sample` function to sample with replacement a vector of 0s and 1s with 100 elements. Call this `x` . Do it again and call it `y` . Would it make sense to call `set.seed` before calling `sample` ? Why?

   - (b) Write a function `sumHeads` that takes as input the number of desired coin flips and returns the number of heads (assume heads are coded by 1). Would it make sense to call `set.seed` in the body of your function? Why?

   - (c) Create a new vector `sums vec` by calling `sumHeads(200)` 10,000 times. (Hint: use `replicate` )

   - (d) Plot a histogram of `sums`

3. Write a function that takes two numeric vectors `x` and `y` as well as a variable `operation` with a default value of `"add"` .

   - (a) If `operation` is `"add"` , return `x+y`

   - (b) If `operation` is `"subtract"` , return `x-y`

   - (c) If `operation` is `"multiply"` , return `x*y`

   - (d) If `operation` is `"divide"` , return `x/y`

   - (e) If `operation` isn’t one of the above, return a warning that `operation` is unknown.

4. Write a function that takes a vector `x` and returns a vector containing the cumulative sum vector. Note that R provides a builtin function `cumsum` that you can use to verify that your function works. You should implement this function using a `for` loop to make sure you understand how it works.

3

---

[← Using apply , sapply , and lapply](05-using-apply-sapply-and-lapply.md) · [Up: contents](index.md) · [Loading (and saving) data →](07-loading-and-saving-data.md)
