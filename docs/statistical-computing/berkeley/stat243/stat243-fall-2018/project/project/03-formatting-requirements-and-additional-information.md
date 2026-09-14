---
title: Formatting requirements and additional information
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/project/project.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/project/project.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formatting requirements and additional information

**Source:** [`project/project.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/project/project.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Your solution to the problem should have two parts:

1. A PDF document describing your solution, prepared in L<sup>A</sup> TEX or R Markdown. The description does not need to be more than a few pages, but should describe the approach you took in terms of functions/modularity/object-oriented programming, and the testing that you carried out. It must include a paragraph describing the specific contributions of each team member and which person/people were responsible for each component of the work. **Please submit a paper copy of the document to me - either directly to me, under my door, or in my mailbox. On your paper solution, please indicate the Github user name of the group member in whose Github account the final version of the project resides.**

2. An R package named _ars_ , including the .tar.gz file created by R CMD build ars, committed to the relevant Github repository. The package should include:

   - (a) A primary function called _ars_ that carries out the simulation, located in a file _ars.R_ in the _R_ directory of the package,

   - (b) Formal tests you applied to your overall function, located in the _tests_ directory of the package. I will run the testing using library(testthat); test_package(’ars’) (please check that you can run that successfully before submitting).

   - (c) Auxiliary functions used by the primary function and testing function,

   - (d) Help information for the main function, in a file _ars.Rd_ in the _man_ directory.

**I should be able to install the package using** devtools::install_github(’student_name/ars’).

For a given subtask of the problem, if you find good code available, you may use it as a modular component of your code provided it does not constitute too large a part of your solution and provided you test the code. Consult me with questions on this matter.

2

You should use Git and Github to manage your collaboration. Please have the project be a repository within the Github account of one of the project members.

You should start the process by mapping out the modular components you need to write and how they will fit together, as well as what the primary function will do. After one person writes a component, another person on the team should test it and, with the original coder, improve it.

A good starting place for information about R packages is Hadley Wickham’s book: http://r-pkgs.had.co.nz/.

3

---

[← Problem](02-problem.md) · [Up: contents](index.md)
