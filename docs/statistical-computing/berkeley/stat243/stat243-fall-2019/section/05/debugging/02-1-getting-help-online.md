---
title: 1) Getting Help Online
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/05/debugging.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1) Getting Help Online

**Source:** [`section/05/debugging.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/debugging.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## 1.1) Mailing Lists and Online Forums

There are several mailing lists that have lots of useful postings.
In general if you have an error, others have already posted about it.

- Simple web searches - *a la Google*
    - You may want to include "in R" or preface your question with "R yada yada yada"
- [Stack overflow](http://stackoverflow.com): R stuff will be tagged with 'R'
    - [http://stackoverflow.com/questions/tagged/r](http://stackoverflow.com/questions/tagged/r)
- R help special interest groups (SIG) such as r-sig-hpc (high performance computing),
r-sig-mac (R on Macs), etc.
    - To search a SIG you might include the name of the SIG in the search string
- [Rseek.org](http://Rseek.org) for web searches restricted to sites that have information on R
- R help: [R mailing lists archive](http://tolstoy.newcastle.edu.au/R)

Note: of course the various mailing lists are also helpful for figuring out how
to do things, not just for fixing bugs. For example, this [blog post](http://www.r-bloggers.com/the-guerilla-guide-to-r/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29) has a guide to R based simply on Stack Overflow posts.

## 1.2) Asking Questions Online

If you've searched the archive and haven't found an answer to your problem, you
can often get help by posting to the R-help mailing list or one of the other
lists mentioned above. A few guidelines (generally relevant when posting to mailing
lists beyond just the R lists):

- Search the archives and look through relevant R books or manuals first.
    - [Advanced R](http://adv-r.had.co.nz/) by Hadley Wickham
- Boil your problem down to the essence of the problem, giving an example,
including the output and error message
    - My first [SO](https://stackoverflow.com/questions/49822833/r-package-call-c-function-within-rcpp) post
        - Notice the not-so-polite comments, see the remark below
    - My second [SO](https://stackoverflow.com/questions/56298503/r-vignette-fails-on-internal-package-function) question
- Say what version of R, what operating system and what operating system version you're using.
    - Provide `sessionInfo()` and `Sys.info()`. These show the current state of your machine
- Read the [R mailing list posting guide](https://www.r-project.org/posting-guide.html).

The R mailing lists are a way to get free advice from the experts, who include
some of the world's most knowledgeable R experts - seriously - members of the R
core development team contribute frequently. The cost is that you should do your
homework and that sometimes the responses you get __may be blunt__, along the lines
of “read the [manual](https://cran.r-project.org/manuals.html)”. Chris considers it a
pretty good tradeoff - where else do you get the foremost experts in a domain actually helping you?


## 2) Common Errors

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


## 3) `R`'s Debugging Tools

### 3.1) Tools

- `browser()`: pauses current execution, provides an interactive interpreter.
You can now step through a function line-by-line to find errors.
- `debug(someFunc)`: sets a `browser()` statement at the first line of `someFunc`
    - `undebug(someFunc)` removes the `debug()` statement. Or close the `R` session
    - `debugonce(someFunc)` lets you debug only once, no need to run `undebug()`
- `options(error = recover)`: invokes a browser whenever an error occurs
- `trace()`: allows you to temporarily modify a function without saving the modifications

### 3.2) Example of Debugging

Code found [here](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/05/jackKnife.R)
```r

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Need MASS for cats data →](03-need-mass-for-cats-data.md)
