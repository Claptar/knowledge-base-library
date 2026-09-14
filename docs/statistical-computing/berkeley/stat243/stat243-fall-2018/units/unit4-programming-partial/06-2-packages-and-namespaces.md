---
title: 2 Packages and namespaces
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Packages and namespaces

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One of the killer apps of R is the extensive collection of add-on packages on CRAN (www.cran.rproject.org) that provide much of R’s functionality. To make use of a package it needs to be installed on your system (using install.packages() once only) and loaded into R (using library() every time you start R).

Some packages are installed by default with R and of these, some are loaded by default, while others require a call to library(). For packages I use a lot, I install them once and then load them automatically every time I start R using my ~/.Rprofile file.

If you want to sound like an R expert, make sure to call them packages and not libraries. A library is the location in the directory structure where the packages are installed/stored.

Loading packages You can use library() to either (1) make a package available (loading it), (2) get an overview of the package, or (3) (if called without arguments) to see all the installed packages.

**library** (dplyr) ## ## Attaching package: ’dplyr’ ## The following objects are masked from ’package:stats’: ## ## filter, lag ## The following objects are masked from ’package:base’: ## ## intersect, setdiff, setequal, union **library** (help = dplyr) ## library() # I don't want to run this on my SCF machine ## because so many are installed

If you run library(), you’ll notice that some of the packages are in a system directory and some are in your home directory. Packages often depend on other packages. In general, if one package depends on another, R will load the dependency, but if the dependency is installed locally (see below), R may not find it automatically and you may have to use library() to load the dependency first. .libPaths() shows where R looks for packages on your system and searchpaths() shows where individual packages are loaded from. Looking the help info for .libPaths() gives some information about how R decides what locations to look in for packages.

7

**.libPaths** ()

---

[← Unit 04 — programming partial Part 05 —](05-unit-04-programming-partial-part-05.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 07 — →](07-unit-04-programming-partial-part-07.md)
