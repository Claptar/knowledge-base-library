---
title: '[15] "/usr/lib/R/library/base"'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [15] "/usr/lib/R/library/base"

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Installing packages** If a package is on CRAN but not on your system, you can install it easily (usually). You don’t need root permission on a machine to install a package (though sometimes you run into hassles if you are installing it just as a user, so if you have administrative privileges it may help to use them). Of course in RStudio, you can install via the GUI.

8

**<mark>install.packages</mark>** <mark>("fields", lib = "~/Rlibs")</mark> _<mark># ~/Rlibs needs to ex</mark> ist!_

Note that R will generally install the package in a reasonable place if you omit the _lib_ argument. You can also download the zipped source file from CRAN and install from the file; see the help page for _install.packages()_ . On Windows and Mac, you’lll need to do something like this:

**<mark>install.packages</mark>** <mark>("fields.tar.gz", repos =</mark> **<mark>NULL</mark>** <mark>, type = "source")</mark>

If you’ve downloaded the binary package (files ending in .tgz for Mac and .zip for Windows), omit the type=’source’ argument.

The difference between the source package and the binary package is that the source package has the raw R (and C and Fortran, in some cases) code while the binary package has all the code in a binary/non-text format, including any C and Fortran code having been compiled.

**Accessing objects from packages** The objects in a package (primarily functions, but also data) are in their own workspaces, and are accessible after you load the package using _library()_ , but are not directly visible when you use _ls()_ . We’ll talk more about this when we talk about scope and environments. If we want to see the objects in one of the other workspaces, we can do the following:

**search** ()

---

[← [14] "Autoloads"](15-14-autoloads.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 17 — →](17-unit-04-usingr-part-17.md)
