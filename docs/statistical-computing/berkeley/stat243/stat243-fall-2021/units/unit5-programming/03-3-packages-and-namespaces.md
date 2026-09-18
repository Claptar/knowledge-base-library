---
title: 3 Packages and namespaces
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Packages and namespaces

One of the killer apps of R is the extensive collection of add-on packages on CRAN (www.cran.r-project.org) that provide much of R's functionality. To make use of a package it needs to be installed on your system (using `install.packages()` once only) and loaded into R (using `library()` every time you start R).

Some packages are *installed* by default with R and of these, some are *loaded* by default, while others require a call to `library()`. For packages I use a lot, I install them once and then load them automatically every time I start R using my `~/.Rprofile` file.

If you want to sound like an R expert, make sure to call them *packages* and not *libraries*. A *library* is the location in the directory structure where the packages are installed/stored.

**Loading packages** You can use `library()` to either (1) make a package available (loading it), (2) get an overview of the package, or (3) (if called without arguments) to see all the installed packages.

```r
library(dplyr)
##
## Attaching package: ’dplyr’
## The following objects are masked from ’package:stats’:
##
##     filter, lag
## The following objects are masked from ’package:base’:
##
##     intersect, setdiff, setequal, union
library(help = dplyr)
## library() # I don't want to run this on my SCF machine
## because so many are installed
```

If you run `library()`, you'll notice that some of the packages are in a system directory and some are in your home directory. Packages often depend on other packages. In general, if one package depends on another, R will load the dependency, but if the dependency is installed locally (see below), R may not find it automatically and you may have to use `library()` to load the dependency first. `.libPaths()` shows where R looks for packages on your system and `searchpaths()` shows where individual packages are loaded from. Looking the help info for `.libPaths()` gives some information about how R decides what locations to look in for packages.

```r
.libPaths()
## [1] "/accounts/gen/vis/paciorek/R/x86_64-pc-linux-gnu-library/4.1"
## [2] "/system/linux/lib/R-20.04/4.1/x86_64/site-library"
## [3] "/usr/lib/R/site-library"
## [4] "/usr/lib/R/library"

searchpaths()
## [1] ".GlobalEnv"
## [2] "/system/linux/lib/R-20.04/4.1/x86_64/site-library/dplyr"
## [3] "/system/linux/lib/R-20.04/4.1/x86_64/site-library/pryr"
## [4] "/system/linux/lib/R-20.04/4.1/x86_64/site-library/knitr"
## [5] "/usr/lib/R/library/stats"
## [6] "/usr/lib/R/library/graphics"
## [7] "/usr/lib/R/library/grDevices"
## [8] "/usr/lib/R/library/utils"
## [9] "/usr/lib/R/library/datasets"
## [10] "/system/linux/lib/R-20.04/4.1/x86_64/site-library/SCF"
## [11] "/usr/lib/R/library/methods"
## [12] "Autoloads"
## [13] "/usr/lib/R/library/base"
```

**Installing packages** If a package is on CRAN but not on your system, you can install it easily (usually). You don't need root permission on a machine to install a package (though sometimes you run into hassles if you are installing it just as a user, so if you have administrative privileges it may help to use them). Of course in RStudio, you can install via the GUI. If you are installing by specifying the `lib` argument, you'd generally want to use whatever user-owned directory (i.e., library) is specified by the output of `.libPaths()`. If none of them are user-owned, you may need to add a library via `.libPaths()` (e.g., by putting something like `.libPaths('~/Rlibs')` in your `.Rprofile`).

```r
install.packages('dplyr', lib = '~/Rlibs') # ~/Rlibs needs to exist!
```

Note that R will generally install the package in a reasonable place if you omit the `lib` argument. You can also download the zipped source file from CRAN and install from the file; see the help page for `install.packages()`. This is called "installing from source". On Windows and Mac, you'll need to do something like this:

```r
install.packages('dplyr_VERSION.tar.gz', repos = NULL, type = 'source')
```

If you've downloaded the binary package (files ending in `.tgz` for Mac and `.zip` for Windows) and want to install the package directly from the file, use the syntax above but omit the `type='source'` argument.

The difference between the source package and the binary package is that the source package has the raw R (and C and Fortran, in some cases) code as text files while the binary package has all the code in a binary/non-text format, including any C and Fortran code having been compiled. To install a source package with C or Fortran code in it, you'll need to have developer/command-line tools (e.g., XCode on Mac or Rtools.exe on Windows) installed on your system so that you have a compiler.

**Package namespaces** The objects in a package (primarily functions, but also data) are in their own workspaces, and are accessible after you load the package using `library()`, but are not directly visible when you use `ls()`. In other words, each package has its own *namespace*. Namespaces help achieve modularity and avoid having zillions of objects all reside in your workspace. We'll talk more about this when we talk about scope and environments. If we want to see the objects in a package's namespace, we can do the following:

```r
search()
##  [1] ".GlobalEnv"        "package:dplyr"
##  [3] "package:pryr"      "package:knitr"
##  [5] "package:stats"     "package:graphics"
##  [7] "package:grDevices" "package:utils"
##  [9] "package:datasets"  "package:SCF"
## [11] "package:methods"   "Autoloads"
## [13] "package:base"

## ls(pos = 5) # for the stats package
ls(pos = 5)[1:5] # just show the first few
## [1] "acf"        "acf2AR"     "add.scope"  "add1"
## [5] "addmargins"

ls("package:stats")[1:5] # equivalent
## [1] "acf"        "acf2AR"     "add.scope"  "add1"
## [5] "addmargins"
```

---

[← 2 Text manipulation, string processing and regular expressions (regex)](02-2-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [4 Types, classes, and object-oriented programming →](04-4-types-classes-and-object-oriented-programming.md)
