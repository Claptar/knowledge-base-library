---
title: '[7] highr0.8 stringr1.4.0 xfun0.8 ## [10] evaluate0.14'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [7] highr0.8 stringr1.4.0 xfun0.8 ## [10] evaluate0.14

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Any code that you wanted executed automatically when starting R can be placed in _~/.Rprofile_ (or in individual _.Rprofile_ files in specific directories). This could include loading packages (see below), sourcing files that contain user-defined functions that you commonly use (you can also put the function code itself in _.Rprofile_ ), assigning variables, and specifying options via _options()_ .

- You can have an R script act as a shell script (like running a bash shell script) as follows. This will probably on work on Linux and Mac.

   1. Write your R code in a text file, say _exampleRscript.R_ .

   2. As the first line of the file, include #!/usr/bin/Rscript (like #!/bin/bash in a bash shell file, as seen in Unit 2) or (for more portability across machines, include #!/usr/bin/env Rscript.

   3. Make the R code file executable with _chmod_ : chmod ugo+x exampleRscript.R.

   4. Run the script from the command line: ./exampleRscript.R

If you want to pass arguments into your script, you can do so as long as you set up the R code to interpret the incoming arguments:

args <- **commandArgs** (TRUE) _## Now args is a character vector containing the arguments. ## Suppose the first argument should be interpreted as a number # and the second as a character string and the third as a boolean:_ numericArg <- **as.numeric** (args[1]) charArg <- args[2] logicalArg <- **as.logical** (args[3] **cat** ("First arg is: ", numericArg, "; second is: ", charArg, "; third is: ", logicalArg, ".\n")

./exampleRscript.R 53 blah T ./exampleRscript.R blah 22.5 t

---

[← Unit 05 — programming Part 03 —](03-unit-05-programming-part-03.md) · [Up: contents](index.md) · [Error in running command bash →](05-error-in-running-command-bash.md)
