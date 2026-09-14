---
title: Unit 04 — programming Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 04 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Use Ctrl-C to interrupt execution. This will generally back out gracefully, returning you to a state as if the command had not been started. Note that if R is exceeding memory availability, there can be a long delay. This can be frustrating, particularly since a primary reason you would want to interrupt is when R runs out of memory.

- The R mailing list archives are very helpful for getting help - always search the archive before posting a question. More info on where to find R help in Unit 5 on debugging.

   - _sessionInfo()_ gives information on the current R session - it’s a good idea to include this information (and information on the operating system such as from _Sys.info()_ ) when you ask for help on a mailing list

4

**sessionInfo** () ## R version 3.2.1 (2015-06-18) ## Platform: x86_64-pc-linux-gnu (64-bit) ## Running under: Ubuntu 14.04.2 LTS ## ## locale: ## [1] LC_CTYPE=en_US.UTF-8 ## [2] LC_NUMERIC=C ## [3] LC_TIME=en_US.UTF-8 ## [4] LC_COLLATE=en_US.UTF-8 ## [5] LC_MONETARY=en_US.UTF-8 ## [6] LC_MESSAGES=en_US.UTF-8 ## [7] LC_PAPER=en_US.UTF-8 ## [8] LC_NAME=C ## [9] LC_ADDRESS=C ## [10] LC_TELEPHONE=C ## [11] LC_MEASUREMENT=en_US.UTF-8 ## [12] LC_IDENTIFICATION=C ## ## attached base packages: ## [1] stats graphics grDevices utils datasets ## [6] base ## ## other attached packages: ## [1] pryr_0.1.2 knitr_1.10.5 SCF_3.2.0 ## ## loaded via a namespace (and not attached): ## [1] magrittr_1.5 formatR_1.2 tools_3.2.1 ## [4] Rcpp_0.11.6 codetools_0.2-11 stringi_0.4-1 ## [7] highr_0.5 methods_3.2.1 stringr_1.0.0 ## [10] evaluate_0.7

- Any code that you wanted executed automatically when starting R can be placed in _~/.Rprofile_ (or in individual _.Rprofile_ files in specific directories). This could include loading packages (see below), sourcing files that contain user-defined functions that you commonly use

5

(you can also put the function code itself in _.Rprofile_ ), assigning variables, and specifying options via _options()_ .

- You can have an R script act as a shell script (like running a bash shell script) as follows.

   1. Write your R code in a text file, say _exampleRscript.R_ .

   2. As the first line of the file, include #!/usr/bin/Rscript (like #!/bin/bash in a bash shell file, as seen in Unit 2).

   3. Make the R code file executable with _chmod_ : chmod ugo+x exampleRscript.R.

   4. Run the script from the command line: ./exampleRscript.R

If you want to pass arguments into your script, you can do so as long as you set up the R code to interpret the incoming arguments:

args <- **commandArgs** (TRUE) _# now args is a character vector containing the arguments.# Suppose the # and the second as a character string and the third as a boolean:_ numericArg <- **as.numeric** (args[1]) charArg <- args[2] logicalArg <- **as.logical** (args[3] **cat** ("First arg is: ", numericArg, "; second is: ", charArg, "; third is: ", logicalArg, ".\n")

./exampleRscript.R 53 blah T ./exampleRscript.R blah 22.5 t ## First arg is, 53 ; second is: blah ; third is: TRUE . ## Warning message: ## NAs introduced by coercion ## First arg is, NA ; second is: 22.5 ; third is: NA .

---

[← Unit 04 — programming Part 03 —](03-unit-04-programming-part-03.md) · [Up: contents](index.md) · [2 Packages and namespaces →](05-2-packages-and-namespaces.md)
