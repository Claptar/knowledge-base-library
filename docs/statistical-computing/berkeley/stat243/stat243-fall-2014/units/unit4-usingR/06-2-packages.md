---
title: 2 Packages
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Packages

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One of the killer apps of R is the extensive collection of add-on packages on CRAN (www.cran.rproject.org) that provide much of R’s functionality. To make use of a package it needs to be installed on your system (using _install.packages()_ once only) and loaded into R (using _library()_ every time you start R).

Some packages are _installed_ by default with R and of these, some are _loaded_ by default, while others require a call to _library()_ . For packages I use a lot, I install them once and then load them automatically every time I start R using my _~/.Rprofile_ file.

**Loading packages** You can use _library()_ to either (1) make a package available (loading it), (2) get an overview of the package, or (3) (if called without arguments) to see all the installed packages.

**library** (fields) _## Loading required package: methods ## Loading required package: spam ## Loading required package: grid ## Spam version 0.41-0 (2014-02-26) is loaded. ## Type ’help( Spam)’ or ’demo( spam)’ for a short introduction ## and overview of this package. ## Help for individual functions is also obtained by adding the ## suffix ’.spam’ to the function name, e.g. ’help( chol.spam)’. ## ## Attaching package: ’spam’ ## ## The following objects are masked from ’package:base’: ## ## backsolve, forwardsolve ## ## Loading required package: maps_ **library** (help = fields) _# library() # I don't want to run this on SCF because so # many are installed_

7

Notice that some of the packages are in a system directory and some are in my home directory. Packages often depend on other packages. In general, if one package depends on another, R will load the dependency, but if the dependency is installed locally (see below), R may not find it automatically and you may have to use _library()_ to load the dependency first. _.libPaths()_ shows where R looks for packages on your system and _searchpaths()_ shows where individual packages are loaded from.

**.libPaths** ()

---

[← Unit 04 — usingR Part 05 —](05-unit-04-usingr-part-05.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 07 — →](07-unit-04-usingr-part-07.md)
