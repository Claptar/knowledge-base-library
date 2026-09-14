---
title: General notes about homeworks
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/05/CodeReview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/05/CodeReview.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# General notes about homeworks

**Source:** [`sections/05/CodeReview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/05/CodeReview.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Below are a couple notes about to keep in mind when doing your problem sets.

1. Problem Statements
You **have to** answer the questions on the homework. Do whatever you'd like beyond
that, be as creative as you wish, but **you must answer the questions that were asked**. This includes all parts of a written response question. If you do not answer these, you are throwing away points.

2. Include Code
Most people include it as they go along, that's fine.  If you find that messy, put an appendix at the end with all of the function definitions.  This applies to code for plots as well.

3. A Couple of Useful Tools in RStudio
You can autoindent your code in RStudio using Command or Ctrl + I.  You can also autoformat your code with Shift + Command or Ctrl + A.  There are some other useful shortcuts in the Code menu.

4. Bonus/Extra Credit
This is something additional, above and beyond the basic homework.  Repeating the analysis already performed, but with different parameters, is not novel.

5. Please use `suppressPackageStartupMessages()` or set `warning = FALSE` and `message = FALSE` in a code chunk that **only** loads the packages.  Please don't use these chunk options on other chunks.  If something is going wrong you need to fix it, as opposed to not printing the warning.

6. Code Testing
You should have already tested all aspects of your R code before you submit it. Your code should run properly if you restart  RStudio  and Knit your .Rmd. I have seen several assignments where students renamed a variable at the last second which causes their code to break, are referencing a global variable that doesn't exist in the .Rmd, etc. which tells me they did not fully test that their code works before submitting. When reasonable,  functions you create should have a set of small but thoughtful examples showing that the code works as expected.

7. Simplicity is the Ultimate Sophistication
You should always be thinking of ways to make your code as simple as possible (while maintaining correctness, numerical precision, speed, etc.). For example, the following three chunks of code all do the same thing:
```r
total = 0
for (i in 1:length(x)) {
  total = total + x[i]
}
total/length(x)
```

```r
sum(x)/length(x)
```

```r
mean(x)
```
but the third option is preferable. Simple code helps with debugging (as there are fewer lines of code to check), improves readability (both for yourself and others), and can often (though not always) result in faster code.


8. Plots and Comments
Plots need to have a title, axis labels, and a key if there are several types of data.  Code and comment lines should be ~80 characters in length.  e.g.
    ```r
    ####################
    ## Make Comment point
    ####################
    # This is a bad comment
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    # This is a good comment
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
    # incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
    # nostrud exercitation ullamco laboris nisi ut aliquip ...etc

    ####################
    ## Good plotting
    ####################
    # setup things
    n <- 50
    x <- 1:n
    y <- runif(n = n, min = 0, max = 10)
    col_factor <- sample(x = c(1, 2), size = n, replace = T, prob = c(1, 2))
    df <- data.frame(x, y, color = as.factor(col_factor))

    # make the plot
    ggplot(df, aes(x = x, y = y)) +
      geom_point(aes(color = color), size = 3) +
      geom_line() +
      theme_bw() +
      labs(x = "Label related to data", y = "Label related to data") +
      ggtitle("Short but informative title") +
      scale_color_discrete(name = "Group designation") +
      theme(legend.position = c(1, 1),
            legend.justification = c(1, 1),
            legend.background = element_blank(),
            legend.box.background = element_rect(colour = "black")) +
      ylim(0, 13)
    ```
\newpage

9. Vectorizing
"Vectorizing" in R implies using functions that operate in parallel over certain objects. R is vectorized in many operations (addition, subtraction, multiplication, division). Many functions have built-in vectorization as well, make sure to check the function documentation.
    ```r
    ####################
    ## vectorized division
    ####################
    x <- 1:100
    y <- 100:1

    mHold <- mapply(FUN = "/", x, y)
    dHold <- x/y

    all.equal(mHold, dHold)
    identical(mHold, dHold)

    ####################
    ## vectorized multinomial
    ####################
    myprobs <- matrix(data = c(0.1,0.1,0.8, 1/3,1/3,1/3), nrow = 2, byrow = T)

    set.seed(0)
    apHold <- t(apply(X = myprobs, MARGIN = 1, FUN = rmultinom, n = 1, size = 100))

    set.seed(0)
    edHold <- extraDistr::rmnom(n = 2, size = 100, prob = myprobs)

    all.equal(apHold, edHold)
    identical(apHold, edHold) # why false?

    # short benchmark
    microbenchmark::microbenchmark("apply" = apply(X = myprobs, MARGIN = 1,
                                                   FUN = rmultinom, n = 1, size = 100),
                                   "vector" = extraDistr::rmnom(n = 2, size = 100,
                                                                prob = myprobs),
                                   times = 100)
    ```
\newpage

---

[← Code review instructions](01-code-review-instructions.md) · [Up: contents](index.md)
