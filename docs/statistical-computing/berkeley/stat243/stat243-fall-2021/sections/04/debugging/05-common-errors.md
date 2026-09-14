---
title: Common errors
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/04/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/04/debugging.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Common errors

**Source:** [`sections/04/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/04/debugging.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Parenthesis mis-matches
- `[[...]]` vs. `[...]`
    ```r
    # example list
    myList <- list("A"=1:10,
                   "B"=11:20)

    # one set
    cat("Type: ", typeof(myList[1]), "\nLength: ", length(myList[1]), sep = "")

    # two sets
    cat("Type: ", typeof(myList[[1]]), "\nLength: ", length(myList[[1]]), sep = "")
    ```
- `==` vs. `=`
- Comparing real numbers exactly using `==` is dangerous because numbers on a
computer are only represented to limited numerical precision.
    ```r
    # exact comparison
    1/3 == 4*(4/12 - 3/12)

    # approximate comparison
    #  default tolerance is sqrt(.Machine$double.eps)
    all.equal(target = 1/3 ,current = 4*(4/12 - 3/12))
    ```
- You expect a single value but execution of the code gives a vector
- You want to compare an entire vector but your code just compares the first value
(e.g., in an if statement)
    - consider using `identical()` or `all.equal()`
    ```r
    x <- 1:10
    y <- 1:5
    if (x == y) {
      print("Equal")
    }else {
      print("Not equal")
    }

    if (identical(x, y)) {
      print("Equal")
    }else {
      print("Not equal")
    }
    ```
- Silent type conversion when you don't want it, or lack of coercion where you're expecting it
    - eg., `read.csv()` and the `stringsAsFactors` argument
- Using the wrong function or variable name
- Giving unnamed arguments to a function in the wrong order
- In an if-else statement, the `else` cannot be on its own line (unless all the code is enclosed in `{}`)
because R will see the `if` part of the statement, which is a valid R statement,
will execute that, and then will encounter the `else` and return an error.
- Forgetting to define a variable in the environment of a function and having R,
via lexical scoping, get that variable as a global variable from one of the enclosing
environments. At best the types are not compatible and you get an error; at worst,
you use a garbage value and the bug is hard to trace. In some cases your code may
work fine when you develop the code (if the variable exists in the enclosing environment),
but then may not work when you restart R if the variable no longer exists or is different.
    - Clear your environment before testing (`rm(list=ls());gc()`)
    - Restart `R` session and test
- R (usually helpfully) drops matrix and array dimensions that are extraneous.
This can sometimes confuse later code that expects an object of a certain dimension.
    ```r
    # 3x3 matrix
    myMat <- matrix(data = 1:9, nrow = 3, ncol = 3)

    # lost dimensions
    dim(myMat[1, ])

    # keep dimensions
    dim(myMat[1, , drop = FALSE])
    ```

---

[← jackknife gamma dist. estimates of cat heart weights](04-jackknife-gamma-dist-estimates-of-cat-heart-weights.md) · [Up: contents](index.md) · [Getting help online →](06-getting-help-online.md)
