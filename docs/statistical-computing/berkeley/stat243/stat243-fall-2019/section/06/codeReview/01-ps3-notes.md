---
title: PS3 Notes
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/06/codeReview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/06/codeReview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# PS3 Notes

**Source:** [`section/06/codeReview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/06/codeReview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

1. Problem Statements
You **have to** answer the questions on the homework. Do whatever you'd like beyond
that, be as creative as you wish, but **you must answer the questions that were asked**.

2. Include Code
Most people include it as they go along, that's fine.
If you find that messy, put an appendix at the end with all of the function definitions.
This applies to code for plots as well.

3. Bonus/Extra Credit
This is something additional, above and beyond the basic homework.
Repeating the analysis already performed, but with different parameters, is not
novel.

4. Plots and Comments
Plots need to have a title, axis labels, and a key if there are several types of data.
Code and comment lines should be ~80 characters in length.
e.g.
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
    colChoice <- c("black","magenta")
    cols <- sample(x = colChoice, size = n, replace = T, prob = c(1,2))

    # could use a key to set them
    # colChoice <- c("black","magenta")
    # key <- (y > 5)
    # cols <- character(length = n)
    # cols[key] <- colChoice[1]
    # cols[!key] <- colChoice[2]

    # parameters
    par(las = 1, font.lab = 2, font.axis = 2, font.main = 2, cex.main = 2, cex.lab = 1.4, cex.axis = 1, lwd = 2)
    # par(las = 1, font.lab = 2, font.axis = 2, font.main = 2,
    #     cex.main = 2, cex.lab = 1.4, cex.axis = 1, lwd = 2)

    # plot
    plot(x = x, y = y, type = "b",
         xlim = c(0,n), ylim = c(0,13),
         main = "Short but Informative Title",
         xlab = "Label Related to Data",
         ylab = "Label Related to Data",
         lwd = 2, pch = 19, cex = 1.75,
         panel.first = grid(),
         col = cols)
    #box(lwd = 3)

    # add legend
    legend("topright", legend = c("Black Group","Pink Group"),
           title = "Group Designation", col = colChoice,
           pch = 15, pt.cex = 2, bg = "white")
    ```
\newpage

    ```r
    ####################
    ## Bad plotting
    ####################
    # same stuff, bad lines
    black <- which(cols == "black")
    pink <- which(cols == "magenta")

    # settings
    par(las = 1, font.lab = 2, font.axis = 2, font.main = 2,
        cex.main = 2, cex.lab = 1.4, cex.axis = 1, lwd = 2)

    # plot
    plot(x = x[black], y = y[black], type = "l",
         xlim = c(0,n), ylim = c(0,13),
         main = "[blank]",
         xlab = "year",
         ylab = "count",
         lwd = 2,
         panel.first = grid(),
         col = "black")

    # plot second line
    lines(x = x[pink], y = y[pink], type = "l", lwd = 2, col = "magenta")
    ```
\newpage

5. Object Initialization, Atomic Access, and Growth
There are many ways to initialize objects in R, but there are more and less
correct methods to do it.
    ```r
    ####################
    ## Object Initialization
    ####################
    n = 10000

    # integers
    x1 <- rep(as.integer(NA), n)
    x2 <- rep(1L, n)
    x3 <- c(1:n)
    x3.5 <- 1:n
    x4 <- vector(mode = "integer", length = n)
    x5 <- integer(length = n)

    # double
    x6 <- double(length = n)
    x6.5 <- numeric(length = n)

    # logical
    x7 <- logical(length = n)

    # lists
    #  There is not a good way to do this, sorry
    x9 <- vector(mode = "list", length = n)

    # benchmark for fun
    microbenchmark::microbenchmark("repNA" = rep(as.integer(NA), n),
                                   "rep" = rep(0L, n),
                                   "repInt" = rep.int(x = 0L,times = n),
                                   "int()" = integer(length = n),
                                   "vec()" = vector(mode = "integer", length = n),
                                   times = 1000)
    ```

    ```r
    ####################
    ## Object replacement/access
    ####################
    # run this in TERMINAL!!!
    x1 <- integer(length = n)
    .Internal(inspect(x1))
    x1 <- vapply(X = 1:n, FUN = as.integer, FUN.VALUE = integer(length = 1))
    .Internal(inspect(x1)) # this will be different!!
    x1[1:n] <- vapply(X = 1:n, FUN = as.integer, FUN.VALUE = integer(length = 1))
    .Internal(inspect(x1)) # this will be the same
    ```
\newpage

    ```r
    ####################
    ## Growing Objects
    ####################
    # Initialize
    myList <- list()
    myVec <- numeric(length = 1)

    # check length
    cat("Length of list is:", length(myList),
        "\nLength of vector is:", length(myVec))

    # loop
    for(i in 1:n){
      myList[[i]] <- "HAHAHA, I'm growing!"
      myVec[i] <- as.integer(i)
      # effectively the same as append() or c(old, new)
    }

    # check length
    cat("Length of list is:", length(myList),
        "\nLength of vector is:", length(myVec))
    ```

6. Vectorizing
"Vectorizing" in R implies using functions that operate in parallel over certain objects.
R is vectorized in many operations (addition, subtraction, multiplication, division).
Many functions have built-in vectorization as well, make sure to check the function
documentation.
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

[Up: contents](index.md) · [PS3 Code Review →](02-ps3-code-review.md)
