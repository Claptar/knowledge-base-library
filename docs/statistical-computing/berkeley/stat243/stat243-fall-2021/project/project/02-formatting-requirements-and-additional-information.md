---
title: Formatting requirements and additional information
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/project.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/project/project.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`project/project.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/project.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Formatting requirements and additional information

1. Your solution to the problem should have two parts:
   (a) An R package named *GA*, including the .tar.gz file created by `R CMD build GA`. I should be able to install your package by simply running `R CMD INSTALL GA_version.tar.gz` or `install_github(paste0(username, '/GA'))` where *username* contains the GitHub user name of the group member in whose GitHub account the project resides. A good starting place for information about R packages is Hadley Wickham's book: https://r-pkgs.had.co.nz/. You can use `usethis::create_package` to create the initial set of directories for the package. The package should include:
       i. A primary function called *select* that carries out the variable selection, located in a file *select.R* in the *R* directory of the package, and including appropriate code comments.
       ii. Other supporting code in additional files in the *R* directory of the package, including appropriate code comments
       iii. Formal tests, located in the package. You can set this up with *usethis::use_testthat*; however, I don't care about the exact structure of the tests folder in your R package, so long as I can run `testthat::test_package('GA')` or some standard invocation that you give me and have it run all your tests. Please check that you can run the tests successfully when you install your package outside of the context in which you are doing your development (e.g., on the SCF).
       iv. Help information for the main function, in the form of standard R documentation in a file called *select.Rd* in the *man* directory. You can either write *select.Rd* by hand or you can have it generated based on using the *roxygen2* package (see https://adv-r.had.co.nz/Documenting-functions.html for an example), with the documentation included in the R code files. You do not need help pages for your auxiliary functions.
   (b) A PDF document describing your solution, prepared in R Markdown or LaTeX

---

[← Problem](01-problem.md) · [Up: contents](index.md)
