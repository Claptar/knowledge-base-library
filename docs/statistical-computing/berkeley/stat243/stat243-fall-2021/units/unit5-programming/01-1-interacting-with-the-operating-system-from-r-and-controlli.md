---
title: 1 Interacting with the operating system from R and controlling R's behavior
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Interacting with the operating system from R and controlling R's behavior

October 2, 2021

This unit covers a variety of programming concepts, illustrated in the context of R. So it also serves as a way to teach advanced features of R. In general the concepts are relevant in other languages, though other languages may implement things differently. One of my goals here for us to think about why things are the way they are in R. I.e., what principles were used in creating the language and what choices were made? While other languages use different principles and made difference choices, understanding what R does in detail will be helpful when you are learning another language.

References:

* Books on R listed on the syllabus: Adler, Chambers, Wickham
* R intro manual and R language manual (R-lang), both on CRAN.
* Venables and Ripley, Modern Applied Statistics with S
* Murrell, Introduction to Data Technologies

I'm going to try to refer to R syntax as *statements*, where a statement is any code that is a valid, complete R expression. I'll try not to use the term *expression*, as this actually means a specific type of object within the R language, as seen in Section 9.

I'll assume everyone knows about the following functions/functionality in R:
`getwd()`, `setwd()`, `source()`, `pdf()`, `save()`, `save.image()`, `load()`

* To run UNIX commands from within R, use `system()`, as follows, noting that we can save the result of a system call to an R object:

```r
system("ls -al")
## knitr/Sweave doesn't seem to show the output of system()
files <- system("ls", intern = TRUE)
files[1:5]
## [1] "cache"              "exampleRscript.R"
## [3] "exampleRscript.R~" "figures"
## [5] "subset_unit5.sh"
```

* There are also a bunch of functions that will do specific queries of the filesystem, including

```r
file.exists("unit2-bash.sh")
## [1] FALSE

list.files("../data")
## [1] "coop.txt.gz"    "cpds.csv"       "hivSequ.csv"
## [4] "IPs.RData"      "precip.txt"     "RTADataSub.csv"
```

* There are some tools for dealing with differences between operating systems. Here's an example:

```r
list.files(file.path("..", "data"))
## [1] "coop.txt.gz"    "cpds.csv"       "hivSequ.csv"
## [4] "IPs.RData"      "precip.txt"     "RTADataSub.csv"
```

* To get some info on the system you're running on:

```r
Sys.info()
##                               sysname
##                               "Linux"
##                               release
##                   "5.4.0-74-generic"
##                               version
## "#83-Ubuntu SMP Sat May 8 02:35:39 UTC 2021"
##                              nodename
##                             "smeagol"
##                               machine
##                              "x86_64"
##                                 login
##                            "paciorek"
##                                  user
##                            "paciorek"
##                        effective_user
##                            "paciorek"
```

* To see some of the options that control how R behaves, try the `options()` function. The *width* option changes the number of characters of width printed to the screen, while the *max.print* option prevents too much of a large object from being printed to the screen. The *digits* option changes the number of digits of numbers printed to the screen (but be careful as this can be deceptive if you then try to compare two numbers based on what you see on the screen).

```r
## options() # this would print out a long list of options
options()[1:5]
## $add.smooth
## [1] TRUE
##
## $bitmapType
## [1] "cairo"
##
## $browser
## [1] "xdg-open"
##
## $browserNLdisabled
## [1] FALSE
##
## $CBoundsCheck
## [1] FALSE

options()[c('width', 'digits')]
## $width
## [1] 55
##
## $digits
## [1] 7

## options(width = 120)
## often nice to have more characters on screen
options(width = 55) # for purpose of making pdf of this document
options(max.print = 5000)
options(digits = 3)
a <- 0.123456; b <- 0.1234561
a; b; a == b
## [1] 0.123
## [1] 0.123
## [1] FALSE
```

* Use `Ctrl-C` to interrupt execution. This will generally back out gracefully, returning you to a state as if the command had not been started. Note that if R is exceeding memory availability, there can be a long delay. This can be frustrating, particularly since a primary reason you would want to interrupt is when R runs out of memory.

* The R mailing list archives are very helpful for getting help - always search the archive before posting a question. More info on where to find R help in Unit 5 on debugging.

  - `sessionInfo()` gives information on the current R session - it's a good idea to include this information (and information on the operating system such as from `Sys.info()`) when you ask for help on a mailing list

```r
sessionInfo()
## R version 4.1.0 (2021-05-18)
## Platform: x86_64-pc-linux-gnu (64-bit)
## Running under: Ubuntu 20.04.2 LTS
##
## Matrix products: default
## BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3
## LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/liblapack.so.3
##
## locale:
##  [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C
##  [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8
##  [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8
##  [7] LC_PAPER=en_US.UTF-8       LC_NAME=C
##  [9] LC_ADDRESS=C               LC_TELEPHONE=C
## [11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C
##
## attached base packages:
## [1] stats     graphics  grDevices utils     datasets
## [6] methods   base
##
## other attached packages:
## [1] pryr_0.1.4  knitr_1.33  SCF_4.1.0
##
## loaded via a namespace (and not attached):
##  [1] compiler_4.1.0   magrittr_2.0.1   tools_4.1.0
##  [4] Rcpp_1.0.7       codetools_0.2-18  stringi_1.7.3
##  [7] highr_0.9        stringr_1.4.0    xfun_0.25
## [10] evaluate_0.14
```

* Any code that you wanted executed automatically when starting R can be placed in `~/.Rprofile` (or in individual `.Rprofile` files in specific directories). This could include loading packages (see below), sourcing files that contain user-defined functions that you commonly use (you can also put the function code itself in `.Rprofile`), assigning variables, and specifying options via `options()`.

* You can have an R script act as a shell script (like running a bash shell script) as follows. This will probably on work on Linux and Mac.

  1. Write your R code in a text file, say `exampleRscript.R`.
  2. As the first line of the file, include `#!/usr/bin/Rscript` (like `#!/bin/bash` in a bash shell file, as seen in Unit 2) or (for more portability across machines, include `#!/usr/bin/env Rscript`.
  3. Make the R code file executable with chmod: `chmod ugo+x exampleRscript.R`.
  4. Run the script from the command line: `./exampleRscript.R`

  If you want to pass arguments into your script, you can do so as long as you set up the R code to interpret the incoming arguments:

```r
args <- commandArgs(TRUE)
## Now args is a character vector containing the arguments.
## Suppose the first argument should be interpreted as a number
# and the second as a character string and the third as a boolean:
numericArg <- as.numeric(args[1])
charArg <- args[2]
logicalArg <- as.logical(args[3])
cat("First arg is: ", numericArg, "; second is: ",
    charArg, "; third is: ", logicalArg, ".\n")
```

```text
./exampleRscript.R 53 blah T
./exampleRscript.R blah 22.5 t
## First arg is:  53 ; second is:  blah ; third is:  TRUE .
## Warning message:
## NAs introduced by coercion
## First arg is:  NA ; second is:  22.5 ; third is:  NA .
```

---

[Up: contents](index.md) · [2 Text manipulation, string processing and regular expressions (regex) →](02-2-text-manipulation-string-processing-and-regular-expression.md)
