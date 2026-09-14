---
title: Unit 05 — programming Part 03 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 03 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Use Ctrl-C to interrupt execution. This will generally back out gracefully, returning you to a state as if the command had not been started. Note that if R is exceeding memory availability, there can be a long delay. This can be frustrating, particularly since a primary reason you would want to interrupt is when R runs out of memory.

- The R mailing list archives are very helpful for getting help - always search the archive before posting a question. More info on where to find R help in Unit 5 on debugging.

   - _sessionInfo()_ gives information on the current R session - it’s a good idea to include

4

this information (and information on the operating system such as from _Sys.info()_ ) when you ask for help on a mailing list

**sessionInfo** ()

- ## R version 3.6.1 (2019-07-05) ## Platform: x86_64-pc-linux-gnu (64-bit) ## Running under: Ubuntu 18.04.3 LTS ## ## Matrix products: default ## BLAS: /usr/lib/x86_64-linux-gnu/openblas/libblas.so.3 ## LAPACK: /usr/lib/x86_64-linux-gnu/libopenblasp-r0.2.20.so ## ## locale: ## [1] LC_CTYPE=en_US.UTF-8 ## [2] LC_NUMERIC=C ## [3] LC_TIME=en_US.UTF-8 ## [4] LC_COLLATE=en_US.UTF-8 ## [5] LC_MONETARY=en_US.UTF-8 ## [6] LC_MESSAGES=en_US.UTF-8 ## [7] LC_PAPER=en_US.UTF-8 ## [8] LC_NAME=C ## [9] LC_ADDRESS=C ## [10] LC_TELEPHONE=C ## [11] LC_MEASUREMENT=en_US.UTF-8 ## [12] LC_IDENTIFICATION=C ## ## attached base packages: ## [1] stats graphics grDevices utils datasets ## [6] methods base ## ## other attached packages: ## [1] pryr_0.1.4 knitr_1.24 SCF_3.6.1 ## ## loaded via a namespace (and not attached): ## [1] compiler_3.6.1 magrittr_1.5 tools_3.6.1 ## [4] Rcpp_1.0.5 codetools_0.2-16 stringi_1.4.3

5

---

[← 1 Interacting with the operating system from R and controlling R’s behavior](02-1-interacting-with-the-operating-system-from-r-and-controlli.md) · [Up: contents](index.md) · [[7] highr0.8 stringr1.4.0 xfun0.8 ## [10] evaluate0.14 →](04-7-highr0-8-stringr1-4-0-xfun0-8-10-evaluate0-14.md)
