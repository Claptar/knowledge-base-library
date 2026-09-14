---
title: 'Group problem for section: logitBoot()'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/05/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/05/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Group problem for section: logitBoot()

**Source:** [`sections/05/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/05/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

For the group work this week we will step through debugging the `logitBoot` function.  This is a function that computes a bootstrapped estimate of the standard error of the coefficient on a logistic regression model.  From R's implementation of logistic regression, stored in the `mod` variable, we can see that the estimated standard error is around 3.  However, by calling `logitBoot(my_data$y, my_data$x)`, which is supposed to get this same standard error, we return a value of over 100.

The goal here is to figure out what is going wrong and, if time, fix the issue.  Below are a list of steps you can take reach this goal.  Note, that the functions are in the `logitBoot.R` script, so it will easiest to open that file and work from there.

  - Load `data.csv` and look at the data to see what we are working with.   There should be a column of `y` values (which are 0 or 1) and a column of `x` values (which are continuous).
    - The goal of logistic regression is to model which class `y` (0 or 1) an observation falls in based on `x`.
  - Load the functions in the `logitBoot.R` script.
  - Fit the logistic regression model in R using the `glm` function (code provided) and look at the `summary(mod)`
    - Notice the estimated standard error on the coefficient for `x` is around 3.
  - Try to run the `logitBoot(my_data$y, my_data$x)`.  Notice the overestimate and the warning.  We want to figure out what is going wrong.
  - Call `debug(logitBoot)` and rerun `logitBoot(my_data$y, my_data$x)`.  This will take you into the browser window for `logitBoot`
    - Run through each line until you compute the vector `boot_coefs`.  Use the `range` and `quantile` functions to examine `boot_coefs` and see what could be going wrong.
    - Find the index of sample that is causing the issue.
  - Now that we have identified where the issue is occuring we still need to figure out why that paricular permutation is problematic.  For that we will use `trace` to temporarily edit our functions.
    - Call `trace(myGLM, edit = TRUE)` and edit the function to return a list of coeficient, `y_boot`, and `x_boot`.
    - Call `trace(logitBoot, edit = TRUE)` and change `sapply` to `lapply`
  - Rerun `logitBoot(my_data$y, my_data$x)`, which will again open the browser window. Step through the code lines and look at `boot_coefs[[i]]` where `i` is the index found in step 5.
    - Look at the values of `x_boot` that correspond to `y_boot = 1`.  Also, `sort` the `x_boot` output.  Can you tell what is going wrong?
  - Now that we know what is causing the warning we can call `untrace(logitBoot)` and `untrace(myGLM)` to remove the temporary edits.

After identifing the issue and we could edit the `myGLM` function to not compute the model when that particular issue arises.  Alternatively, we could employ a more holistic approach with `tryCatch`.  With this we can handle unforseen issues that may arise.  This is what is implemented in the `potential_solution.R` script.  Note, with the fixed code we now seem to underestimating the standard error.  I am not sure why that is happening... because as far as I can tell the code is working correctly.

```r
my_data <- read.csv('./data.csv')

logitBoot <- function(y, x, n_boot = 2000) {
  set.seed(5)

  # do n_boot random permutations of x and y and return coefficient on x with
  # the myGLM function
  boot_coefs <- sapply(seq_len(n_boot), myGLM, y, x)

  # compute standard deviation of those estimates and return
  boot_se <- sd(boot_coefs)
  return(boot_se)
}

myGLM <- function(i, y, x) {
  n <- length(y)

  # randomly sample with replacement from the observations in the data
  boot_sample <- sample(seq_len(n), n, replace = TRUE)

  # create vectors of the bootstrapped samples
  x_boot <- x[boot_sample]
  y_boot <- y[boot_sample]

  # fit logistic regression on permutated data
  mod_boot <- glm(y_boot ~ x_boot, family = 'binomial')

  # return the estimated coefficient
  return(mod_boot$coef[2])
}

---

[← Getting help online](06-getting-help-online.md) · [Up: contents](index.md) · [fit model in R →](08-fit-model-in-r.md)
