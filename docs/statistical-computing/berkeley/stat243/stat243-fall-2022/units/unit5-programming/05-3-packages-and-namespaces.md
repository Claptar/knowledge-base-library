---
title: 3. Packages and namespaces
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Packages and namespaces

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Scripting languages that become popular generally have an extensive collection
of add-on packages available online (the causal relationship of the popularity and
the extensive add-on packages goes in both directions). Packages need to
be *installed* (once) on your computer and *loaded* (every time you start a new session).

A big part of R's popularity is indeed the extensive collection of add-on
packages on [CRAN](https://cran.r-project.org) (and GitHub and elsewhere) that provide
much of R's functionality. To make use of a package it needs to be
installed on your system (using *install.packages* once only) and
loaded into R (using *library* every time you start R).

Some packages are *installed* by default with R and of these, some are
*loaded* by default, while others require a call to *library*.

If you want to sound like an R expert, make sure to call them *packages*
and not *libraries*. A *library* is the location in the directory
structure where the packages are installed/stored.


## Loading packages

You can use *library* to either (1) make a package available (loading
it), (2) get an overview of the package, or (3) (if called without
arguments) to see all the installed packages.

```r
library(dplyr)              # load the package
library(help = dplyr)       # get some help info about the package
```

Packages in R (and in Python, Julia, etc.) may be installed in various places
on the filesystem, and it sometimes it is helpful (e.g., if you end up with multiple
versions of a package installed on your system) to be able to figure out
where on the filesystem the package is being loaded from.
If you run `library()`, you'll notice that some of the packages are in a
system directory and some are in your home directory.

`.libPaths()` shows where R
looks for packages on your system and `searchpaths()` shows where
individual packages currently loaded in your session have been loaded from. The help information
for *.libPaths* gives some information about how R decides what locations
to look in for packages (and how you can modify that).

```r
.libPaths()
searchpaths()
```

## Installing packages

If a package is on CRAN but not on your system, you can install it
easily (usually). You don't need root permission on a machine to install
a package (though sometimes you run into hassles if you are installing
it just as a user, so if you have administrative privileges it may help
to use them). Of course in RStudio, you can install via the GUI.

Packages often depend on other packages. In general, if one package depends on another,
R will install the dependency automatically, but sometimes you'll need to
install a dependency yourself.  In general, package dependencies
are handled very cleanly in R without you having having to worry much about it;
this is less the case in Python.


Note that R will generally install the package in a reasonable place by default
but you can control where it is installed using the *lib* argument.

```r
install.packages('dplyr', lib = '~/Rlibs') # ~/Rlibs needs to exist!
```

You can also download the zipped source file from CRAN and install from
the file; see the help page for *install.packages*. This is called
"installing from source". On Windows and Mac, you'll need to do
something like this:

```r
install.packages('dplyr_VERSION.tar.gz', repos = NULL, type = 'source')
```

This can be handy if you need to install [an older version of a package](https://cran.r-project.org/src/contrib/Archive)
for reproducibility or because of some dependency incompatibility.

If you've downloaded the binary package (files ending in .tgz for Mac
and .zip for Windows) and want to install the package directly from the
file, use the syntax above but omit the `type= 'source'` argument.

### Source vs. binary packages

The difference between a *source* package and a *binary* package is that
the source package has the raw R (and C and Fortran, in some cases) code
as text files while the binary package has all the code in a
binary/non-text format, including that any C and Fortran code will have already been
compiled. To install a source package with C or Fortran code in it,
you'll need to have developer/command-line tools (e.g., *XCode* on Mac
or *Rtools.exe* on Windows) installed on your system so that you have a
compiler.

## Managing packages using package managers

For reproducibility, it's important to know the versions of the packages you use (and the version of R).
Package managers make it easy to do this. Some useful packages that do package management in R are *checkpoint*, *renv*, and *packrat*. The basic commonality is that they try to make it easy to 'freeze' the versions of hte packages you are using, record that information, and restore the versions (potentially on some other machine and by some user other than yourself). The package manager may tell you where the packages are installed, but you can always verify things with `.libPaths()`.

In Python, you can set up and manage isolated environments in which you can control the package versions using virtualenvs or Conda environments.


## Package namespaces

The objects in a package (primarily functions, but also data) are in
their own workspaces, and are accessible after you load the package
using `library()`, but are not directly visible when you use `ls()`. In
other words, each package has its own *namespace*. Namespaces help
achieve modularity and avoid having zillions of objects all reside in
your workspace.  If we want to see the objects in a package's namespace, we
can do the following:

```r
search()
## ls(pos = 4) # for the stats package
ls(pos = 4)[1:5] # just show the first few
ls("package:stats")[1:5] # equivalent
ls("package:stats", pattern = "^lm")
```

### Why have namespaces?

We'll talk more about namespaces when we talk about variable scope and
environments. But as some motivation for why this is useful, consider the following.

The *lm* function calls the *lm.fit* function to calculate the least squares solution in regression.

Suppose we write our own *lm.fit* function that does something else:

```r
lm.fit <- function(x)
    print('hi')

x <- 7
lm.fit(x)
```

One might expect that if one now uses `lm()` to fit a regression, that it wouldn't work correctly because we have an *lm.fit* function in our workspace that doesn't calculate the least squares solution. But it works just fine (see below), because *lm* and *lm.fit* are in the *stats* package namespace (see above) and R's scoping rules (more later) ensure that the *lm.fit* that is found when I run *lm* is the *lm.fit* needed to run the regression and not my silly *lm.fit* function in current workspace.

```r
n <- 10
x <- runif(n)
y <- runif(n)
mod <- lm(y ~ x)
mod
```

### Namespace resolution

Standard practice in R has generally been to load a package and then use any of the items in the package namespace directly, e.g.,

```r
library(stringr)
str_detect("hello there", "hello")
```

However, particularly if you're using the package in only a limited way, it can be a nice idea to not load the entire package and instead use the namespace resolution operator in a style that might remind you of Python and some other languages:

```r
stringr::str_detect("hello there", "hello")
```

```python
import numpy as np
x = np.ndarray([0,3,5])
```

Of course in Python you could also load the entire package (i.e., import the entire namespace), though it's not standard practice:

```python
from numpy import *
## OR: from numpy import ndarray
x = ndarray([0,3,5])
```

Loading entire packages often causes 'name collisions' where there are multiple functions (or variables, more genreally) that have the same name. This can be confusing. We'll see how R determines what function to use later in the Unit.

---

[← 2. Interacting with the operating system and external code and configuring R](04-2-interacting-with-the-operating-system-and-external-code-an.md) · [Up: contents](index.md) · [4. Types and data structures →](06-4-types-and-data-structures.md)
