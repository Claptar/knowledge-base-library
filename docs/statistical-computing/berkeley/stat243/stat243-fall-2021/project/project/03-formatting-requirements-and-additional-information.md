---
title: Formatting requirements and additional information
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/project.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/project/project.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formatting requirements and additional information

**Source:** [`project/project.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/project.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Your solution to the problem should have two parts:

   - (a) An R package named _GA_ , including the .tar.gz file created by R CMD build GA. I should be able to install your package by simply running R CMD INSTALL GA_version.tar.gz or install_github(paste0(username, ’/GA’)) where _username_ contains the GitHub user name of the group member in whose GitHub account the project resides. A good starting place for information about R packages is Hadley Wickham’s book: https://r-pkgs.had.co.nz/. You can use _usethis::create_package_ to create the initial set of directories for the package. The package should include:

      - i. A primary function called _select_ that carries out the variable selection, located in a file _select.R_ in the _R_ directory of the package, and including appropriate code comments.

      - ii. Other supporting code in additional files in the _R_ directory of the package, including appropriate code comments

      - iii. Formal tests, located in the package. You can set this up with _usethis::use_testthat_ ; however, I don’t care about the exact structure of the tests folder in your R package, so long as I can run testthat::test_package(’GA’) or some standard invocation that you give me and have it run all your tests. Please check that you can run the tests successfully when you install your package outside of the context in which you are doing your development (e.g., on the SCF).

      - iv. Help information for the main function, in the form of standard R documentation in a file called _select.Rd_ in the _man_ directory. You can either write _select.Rd_ by hand or you can have it generated based on using the _roxygen2_ package (see https://adv-r.had.co.nz/Documentingfunctions.html for an example), with the documentation included in the R code files. You do not need help pages for your auxiliary functions.

   - (b) A PDF document describing your solution, prepared in R Markdown or L<sup>A</sup> TEX+knitr. The description does not need to be more than 2-4 pages, but should describe the approach you took in terms of functions/modularity/object-oriented programming, the testing that you carried out, and the results of applying the implementation to the example(s). It must include a paragraph describing the specific contributions of each team member and which person/people were responsible for each component of the work. **Please submit a paper copy of the document to me - either directly to me, under my door, or in my mailbox. On your paper solution, please indicate the GitHub user name of the group member in whose Github repository the final version of the project resides.**

2

2. You should start the process by mapping out the modular components you need to write and how they will fit together, as well as what the primary function will do. After one person writes a component, another person on the team should test it and, with the original coder, improve it. You could also consider using pair programming for some of your development.

3. You should use Git and GitHub to manage your collaboration, with branching as needed and regular commits. Please have the project be a repository named (exactly) _GA_ within the github.com account of one of the project members. Please make the repository private and share it with me (user ’paciorek’ on GitHub.com).

3

---

[← Problem](02-problem.md) · [Up: contents](index.md)
