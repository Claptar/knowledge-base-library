---
title: note the overestimation of standard error 119 > 3
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/04/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# note the overestimation of standard error 119 > 3

**Source:** [`labs/04/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/04/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

logitBoot(my_data$y, my_data$x)
```

When calling `logitBoot(my_data$y, my_data$x)`, which is supposed to give the
same standard error of around 3, we return a value of over 100.

## Debugging steps

The goal here is to figure out what is going wrong and, if time, fix the issue.
Below are a list of steps you can take reach this goal. Note, that the functions
are in the `logitBoot.R` script, so it will easiest to open that file and work
from there.

  - Load `data.csv` and look at the data to see what we are working with. There
    should be a column of `y` values (which are 0 or 1) and a column of `x`
    values (which are continuous).
    - The goal of logistic regression is to model which class `y` (0 or 1) an
      observation falls in based on `x`.
  - Load the functions in the `logitBoot.R` script
    - If you're using RStudio, be sure to set the working directory to the
    `labs/04/` directory. You can do this Using Session > Set Working Directory > To Source File Location
    from the top menu. Then you can use the **Source** button at the top of the RStudio source file editor
    to source in the whole file at one time.
    - Try to run the `logitBoot(my_data$y, my_data$x)`. Notice the overestimate
      and the warning. We want to figure out what is going wrong.
  - Use **one** of the methods we discussed about to debug `logitBoot`:
    - add breakpoints
    - use `debug()`/`debugonce()`
    - manually add a call to `browser()`
    - use `trace()` to temporarily add a call to `browser()`
  - Now rerun `logitBoot(my_data$y, my_data$x)`.
    - Run through each line until you compute the vector `boot_coefs`. Use the
      `range()`, `quantile()`, `mean()`, `median()`, etc. functions to examine
      statistics from `boot_coefs` and try to find any strange values.
    - Find the index of sample that is causing the issue.
  - Now that we have identified where the issue is occuring we still need to
    figure out why that particular permutation is problematic.
    - Edit the function to return a list of coefficient, `y_boot`, and `x_boot`.
    - Change `sapply` to `lapply`.
  - Rerun `logitBoot(my_data$y, my_data$x)`, which will start debugging where
    you set the debug point. Step through the code lines and look at
    `boot_coefs[[i]]` where `i` is the index found in step 5.
    - Look at the values of `x_boot` that correspond to `y_boot = 1`. Also,
      `sort` the `x_boot` output. Can you tell what is going wrong?
  - Now that we know what is causing the warning we can remove the changes that
    you made, so that `logitBoot()` outputs a vector again, instead of a list.
    Alternatively, for extra practice with nested list structures, you can
    modify `logitBoot()` further to work with the new `boot_coefs` data
    structure.

After identifying the issue, we could edit the `myGLM()` function to not compute
the model when that particular issue arises. Or we could instead employ a more
holistic approach with `tryCatch()`. With this we can handle unforseen issues that
may arise. (This is what is implemented in the `logitBoot_solution.R` script,
which I will push after section.) Note, with the fixed code we now seem to
underestimating the standard error. I am not sure why that is happening...
because as far as I can tell the code is working correctly.

---

[← estimate standard error with our bootstrap function](10-estimate-standard-error-with-our-bootstrap-function.md) · [Up: contents](index.md)
