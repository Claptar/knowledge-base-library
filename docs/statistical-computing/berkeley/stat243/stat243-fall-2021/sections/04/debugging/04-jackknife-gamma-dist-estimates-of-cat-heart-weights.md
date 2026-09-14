---
title: jackknife gamma dist. estimates of cat heart weights
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/04/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/04/debugging.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# jackknife gamma dist. estimates of cat heart weights

**Source:** [`sections/04/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/04/debugging.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

gamma_jackknife(MASS::cats$Hwt)
```
Notice that there is an error returned by the function, but it is unclear what is producing the error.  We can start by calling `traceback()` to see what may have gone wrong.

![](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2021/c918dcc56a197cc539e270f1f7d076010b175c52/sections/04/figures/traceback.png){width=95%}

`traceback()` shows us the set of calls leading up to the error.  We see that the error is produced at 5, and thus came from the call at 4 `FUN(newX[, i], ...)` which occured after calling `calc_var()` function and attempting to excecute the `apply` statement.

An alternative to `traceback()` is `recover()`.  If we have set `options(error = recover)` and call
`gamma_jackknife(MASS::cats$Hwt)` again we will see the call stack (in reverse order of `traceback`), but now we have the option to select a number in the stack that we would like to enter.  I selected 2 and entered the `calc_var` function.  Typing `ls()` showed me that the only object in the function environment is `estimates`, which is a matrix.  However, I see the `is.atomic(x)` error when I try to compute the variance of a column. When we look at the column, we can now see that we output a list, instead of a vector and we know exactly where the error is occuring.  To exit we type `Q` and hit enter.

![](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2021/c918dcc56a197cc539e270f1f7d076010b175c52/sections/04/figures/recover.png){width=95%}

Now let's say we want to browse in the `gamma_jackknife()` function to figure out why we are passing a list to `calc_var` we can utlize the `debug()` function, which will allow us to step through `gamma_jackknife` one line at a time.  We first call `debug(gamma_jackknife)` and then when we attempt to run `gamma_jackknife(MASS::cats$Hwt)`, because an error is produce, we will enter the browser mode.

![](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2021/c918dcc56a197cc539e270f1f7d076010b175c52/sections/04/figures/jackknife.png){width=95%}

We can use the graphical interface in R Studio or the command line, with the command `n` to step through lines of the code and see what it outputs.  Here we see that `gamma_est` is returning a list and that is likely the source of our issues.

For more details on these functions, as well as how to use `trace` to temporarialy add edits see the SCF tutorial and the screencast.  Also, as I stated above if there is enough interest I can do a live demo at the beginning of section.

---

[← R's debugging tools](03-r-s-debugging-tools.md) · [Up: contents](index.md) · [Common errors →](05-common-errors.md)
