---
title: Unit 05 — programming Part 10 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 10 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Installing packages** If a package is on CRAN but not on your system, you can install it easily (usually). You don’t need root permission on a machine to install a package (though sometimes you run into hassles if you are installing it just as a user, so if you have administrative privileges it may help to use them). Of course in RStudio, you can install via the GUI. If you are installing by specifying the _lib_ argument, you’d generally want to use whatever user-owned directory (i.e., library) is specified by the output of _.libPaths()_ . If none of them are user-owned, you may need to add a library via .libPaths() (e.g., by putting something like .libPaths(’~/Rlibs’) in your _.Rprofile_ ).

**<mark>install.packages</mark>** <mark>('dplyr', lib = '~/Rlibs')</mark> _<mark># ~/Rlibs needs to exis</mark> t!_

Note that R will generally install the package in a reasonable place if you omit the _lib_ argument. You can also download the zipped source file from CRAN and install from the file; see the help page for _install.packages()_ . This is called “installing from source”. On Windows and Mac, you’ll need to do something like this:

**<mark>install.packages</mark>** <mark>('dplyr_VERSION.tar.gz', repos =</mark> **<mark>NULL</mark>** <mark>, type = 'sou</mark> rce')

If you’ve downloaded the binary package (files ending in .tgz for Mac and .zip for Windows) and want to install the package directly from the file, use the syntax above but omit the type=’source’ argument.

The difference between the source package and the binary package is that the source package has the raw R (and C and Fortran, in some cases) code as text files while the binary package has all the code in a binary/non-text format, including any C and Fortran code having been compiled. To install a source package with C or Fortran code in it, you’ll need to have developer/command-line tools (e.g., _XCode_ on Mac or _Rtools.exe_ on Windows) installed on your system so that you have a compiler.

12

**Package namespaces** The objects in a package (primarily functions, but also data) are in their own workspaces, and are accessible after you load the package using _library()_ , but are not directly visible when you use _ls()_ . In other words, each package has its own _namespace_ . Namespaces help achieve modularity and avoid having zillions of objects all reside in your workspace. We’ll talk more about this when we talk about scope and environments. If we want to see the objects in a package’s namespace, we can do the following:

**search** ()

---

[← Unit 05 — programming Part 09 —](09-unit-05-programming-part-09.md) · [Up: contents](index.md) · [Unit 05 — programming Part 11 — →](11-unit-05-programming-part-11.md)
