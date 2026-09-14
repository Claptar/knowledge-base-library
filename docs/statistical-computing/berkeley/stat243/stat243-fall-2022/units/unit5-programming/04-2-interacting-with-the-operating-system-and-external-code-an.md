---
title: 2. Interacting with the operating system and external code and configuring
  R
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Interacting with the operating system and external code and configuring R

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Interacting with the operating system

Scripting languages allow one to interact with the operating system in various ways.
Most allow you to call out to the shell to run arbitrary shell code and save results within your session.

I'll assume everyone knows about the following functions/functionality for interacting with the filesystem and file
in R: *getwd*, *setwd*, *source*, *pdf*, *save*, *save.image*, *load*.

-   To run UNIX commands from within R, use `system()`, as follows,
    noting that we can save the result of a system call to an R object:

    ```r
    system("ls -al")   ## results apparently not shown when compiled...
    files <- system("ls", intern = TRUE)
    files[1:5]
    ```

-   There are also a bunch of functions that will do specific queries of
    the filesystem, including

    ```r
    file.exists("unit2-dataTech.Rmd")
    list.files("../data")
    ```

-   There are some tools for dealing with differences between operating
    systems. *file.path* is a nice example:

    ```r
    list.files(file.path("..", "data"))
    ```

    It's best if you can to write your code in a way that is *agnostic* to the underlying operating system.

-   To get some info on the system you're running on:

    ```r
    Sys.info()
    ```

## Controlling the behavior of R

Scripting languages generally allow you to control/customize their behavior
in various ways by setting options.

-   To see some of the options that control how R behaves, try the
    *options* function. The *width* option changes the number of
    characters of width printed to the screen, while *max.print*
    revents too much of a large object from being printed to the
    screen.

    ```r
    ## options()  # this would print out a long list of options
    options()[1:4]
    options()[c('width', 'digits')]

    ## Often it's nice to have more characters in each line on the screen,
    ## but that would cause overly lines in the compiled file.
    ## options(width = 120)

    options(max.print = 5000)
    ```

    The *digits* option changes the number of digits of numbers
    printed to the screen (but be careful as this can be deceptive if
    you then try to compare two numbers based on what you see on the
    screen).
    ```r
    options(digits = 3)
    a <- 0.123456; b <- 0.1234561
    a; b; a == b
    ```

    More on how to (and how not to) compare real-valued numbers on a computer in Unit 8.

-   Use `Ctrl-C` to interrupt execution. This will generally back out
    gracefully, returning you to a state as if the command had not been
    started. Note that if R is exceeding the amount of memory available, there can
    be a long delay. This can be frustrating, particularly since a
    primary reason you would want to interrupt is when R runs out of
    memory.

-   *sessionInfo* gives information on the current R session and can
    be very helpful for recording the state of your session (including package versions) to allow for reproducibility.

    ```r
    sessionInfo()
    ```

-   Any code that you wanted executed automatically when starting R can
    be placed in `~/.Rprofile` (or in individual, project-specific `.Rprofile` files in
    specific directories). This could include loading packages (see
    below), sourcing files that contain user-defined functions that you
    commonly use (you can also put the function code itself in
    `.Rprofile`), assigning variables, and specifying options via
    `options()`.

-   You can have an R script act as a shell script (like running a bash
    shell script) as follows. This will probably on work on Linux and
    Mac.

    1.  Write your R code in a text file, say `exampleRscript.R`.
    2.  As the first line of the file, include `#!/usr/bin/Rscript`
        (like `#!/bin/bash` in a bash shell file, as seen in Unit 2) or
        for more portability across machines, include
        `#!/usr/bin/env Rscript`.
    3.  Make the R code file executable with *chmod*:
        `chmod ugo+x exampleRscript.R`.
    4.  Run the script from the command line: `./exampleRscript.R`

    If you want to pass arguments into your script, you can do so as
    long as you set up the R code to interpret the incoming arguments:

    ```r
    args <- commandArgs(TRUE)

    ## Now args is a character vector containing the arguments.
    ## Suppose the first argument should be interpreted as a number
    ## and the second as a character string and the third as a boolean:

    numericArg <- as.numeric(args[1])
    charArg <- args[2]
    logicalArg <- as.logical(args[3])

    cat("First arg is: ", numericArg, "; second is: ", charArg,
        "; third is: ", logicalArg, ".\n")
    ```

    Now we can run it as follows in the shell:

    ```bash
    ./exampleRscript.R 53 blah T
    ./exampleRscript.R blah 22.5 t
    ```

## Interacting with external code

Scripting languages such as R, Python, and Julia allow you to call out to "external code",
which often means C or C++ (but also Fortran, Java and other languages).

In fact, the predecessor language to R,
which was called 'S' was developed specifically (at AT&T's Bell Labs in the 1970s and 1980s) as an interactive
wrapper around Fortran, the numerical programming language most commonly used at the time (and still widely relied on today in various legacy codes).

Calling out to external code is particularly important in languages like R and Python that are often much slower
than compiled code and less important in a fast language like Julia (which uses Just-In-Time compilation -- more on that later).

In R, one can call directly out to C or C++ code using *.Call* or one can use the [Rcpp package](https://adv-r.hadley.nz/rcpp.html). *Rcpp* is specifically designed to be able to write C++ code that feels somewhat like writing R code and where it is very easy to pass data between R and C++.

In Python, one can [directly call out to C or C++ code](https://docs.python.org/3/extending/extending.html) or one can use *Cython* to interact with C. With Cython, one can:
  - Have Cython automatically translate Python code to C, if you provide type definitions for your variables.
  - Define C functions that can be called from your Python code.

---

[← 1. Text manipulation, string processing and regular expressions (regex)](03-1-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [3. Packages and namespaces →](05-3-packages-and-namespaces.md)
