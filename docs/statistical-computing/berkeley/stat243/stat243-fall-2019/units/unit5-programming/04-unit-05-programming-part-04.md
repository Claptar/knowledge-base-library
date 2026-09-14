---
title: Unit 05 — programming Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 04 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Use Ctrl-C to interrupt execution. This will generally back out gracefully, returning you to a state as if the command had not been started. Note that if R is exceeding memory availability, there can be a long delay. This can be frustrating, particularly since a primary reason you would want to interrupt is when R runs out of memory.

- The R mailing list archives are very helpful for getting help - always search the archive before posting a question. More info on where to find R help in Unit 5 on debugging.

   - _sessionInfo()_ gives information on the current R session - it’s a good idea to include this information (and information on the operating system such as from _Sys.info()_ ) when you ask for help on a mailing list

4

#### **sessionInfo** ()

- ## R version 3.6.1 (2019-07-05) ## Platform: x86_64-pc-linux-gnu (64-bit) ## Running under: Ubuntu 18.04.2 LTS ## ## Matrix products: default ## BLAS: /usr/lib/x86_64-linux-gnu/openblas/libblas.so.3 ## LAPACK: /usr/lib/x86_64-linux-gnu/libopenblasp-r0.2.20.so ## ## locale: ## [1] LC_CTYPE=en_US.UTF-8 ## [2] LC_NUMERIC=C ## [3] LC_TIME=en_US.UTF-8 ## [4] LC_COLLATE=en_US.UTF-8 ## [5] LC_MONETARY=en_US.UTF-8 ## [6] LC_MESSAGES=en_US.UTF-8 ## [7] LC_PAPER=en_US.UTF-8 ## [8] LC_NAME=C ## [9] LC_ADDRESS=C ## [10] LC_TELEPHONE=C ## [11] LC_MEASUREMENT=en_US.UTF-8 ## [12] LC_IDENTIFICATION=C ## ## attached base packages: ## [1] stats graphics grDevices utils datasets ## [6] methods base ## ## other attached packages: ## [1] pryr_0.1.4 knitr_1.24 ## [3] RhpcBLASctl_0.18-205 SCF_3.6.1 ## ## loaded via a namespace (and not attached): ## [1] compiler_3.6.1 magrittr_1.5 tools_3.6.1 ## [4] Rcpp_1.0.2 codetools_0.2-15 stringi_1.4.3 ## [7] highr_0.8 stringr_1.4.0 xfun_0.8

5

<mark>## [10] evaluate_0.14</mark>

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
