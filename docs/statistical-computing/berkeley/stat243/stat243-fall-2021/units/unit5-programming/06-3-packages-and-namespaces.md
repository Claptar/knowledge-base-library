---
title: 3 Packages and namespaces
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Packages and namespaces

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One of the killer apps of R is the extensive collection of add-on packages on CRAN (www.cran.rproject.org) that provide much of R’s functionality. To make use of a package it needs to be installed on your system (using _install.packages()_ once only) and loaded into R (using _library()_ every time you start R).

Some packages are _installed_ by default with R and of these, some are _loaded_ by default, while others require a call to _library()_ . For packages I use a lot, I install them once and then load them automatically every time I start R using my _~/.Rprofile_ file.

If you want to sound like an R expert, make sure to call them _packages_ and not _libraries_ . A _library_ is the location in the directory structure where the packages are installed/stored.

**Loading packages** You can use _library()_ to either (1) make a package available (loading it), (2) get an overview of the package, or (3) (if called without arguments) to see all the installed packages.

10

**library** (dplyr) _## ## Attaching package: ’dplyr’ ## The following objects are masked from ’package:stats’: ## ## filter, lag ## The following objects are masked from ’package:base’: ## ## intersect, setdiff, setequal, union_ **library** (help = dplyr) _## library() # I don't want to run this on my SCF machine ## because so many are installed_

If you run library(), you’ll notice that some of the packages are in a system directory and some are in your home directory. Packages often depend on other packages. In general, if one package depends on another, R will load the dependency, but if the dependency is installed locally (see below), R may not find it automatically and you may have to use _library()_ to load the dependency first. _.libPaths()_ shows where R looks for packages on your system and _searchpaths()_ shows where individual packages are loaded from. Looking the help info for _.libPaths()_ gives some information about how R decides what locations to look in for packages.

**.libPaths** ()

---

[← 2 Text manipulation, string processing and regular expressions (regex)](05-2-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [Unit 05 — programming Part 07 — →](07-unit-05-programming-part-07.md)
