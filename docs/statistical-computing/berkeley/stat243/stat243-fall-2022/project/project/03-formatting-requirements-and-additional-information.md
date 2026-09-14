---
title: Formatting requirements and additional information
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/project/project.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/project/project.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Formatting requirements and additional information

**Source:** [`project/project.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/project/project.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Your solution to the problem should have two parts:

1.  A PDF document describing your solution, prepared in R Markdown/quarto/knitr.
    The description does not need to be more than a few pages,
    but should describe the approach you took in terms of
    functions/modularity/object-oriented programming, the testing
    that you carried out, and usage on examples. It must include a paragraph describing the
    specific contributions of each team member and which person/people
    were responsible for each component of the work.

    **Please submit a paper copy of the document to
    me - either directly to me, under my door, or in my mailbox. On your paper solution,
    please indicate  the GitHub repository name clearly at the beginning
    of your writeup so I can easily get your materials.**

2.  An R package named `ars`, including the `.tar.gz` file created by
    `R CMD build ars`, committed to the relevant Git repository (see
    below). The package should include:

    a.  A primary function called `ars` that carries out the simulation,
        located in a file `ars.R` in the `R` directory of the package,

    b.  Formal tests you applied to your overall function. You can set
        this up with `usethis::use_testthat`. I should be able to
        run  `testthat::test_package(’ars’)` or `testthat::test_file('/path/to/test-file.R')`
        and have it run all your tests.
        Please check that you can run the tests if you install your own package as
        a fresh install, and indicate in your writeup how I can run
        your tests. There is more information on testing in
        [Hadley Wickham's book](https://r-pkgs.had.co.nz/tests.html).

    c.  Auxiliary functions used by the primary function and testing
        function,

    d.  Help information for the main function, in a file `ars.Rd` in
        the `man` directory. If you want, you can `ars.Rd` by hand,
        but I recommend having it generated based on using the `roxygen2`
        package (see [here for an example](http://adv-r.had.co.nz/Documenting-functions.html)).
        In the latter case you would have the
        documentation included in `ars.R`.

        A good starting place for information about R packages is [Hadley Wickham's book](http://r-pkgs.had.co.nz/).

For a given subtask of the problem, if you find good code available, you
may use it as a modular component of your code provided it does not
constitute too large a part of your solution and provided you test the
code. Consult me with questions on this matter.

You should use Git and GitHub to manage your collaboration. Please have
the project be a private repository named `ars` within the Berkeley GitHub account or github.com account of one
of the project members. **Make sure to share the repository with me (username `paciorek` in either
`github.berkeley.edu` or `github.com`.)**

You should start the process by mapping out as a group the modular
components you need to write and how they will fit together, as well as
what the primary function will do. After one person writes a component,
another person on the team should test it and, with the original coder,
improve it. Or you might consider using pair programming.

---

[← Problem](02-problem.md) · [Up: contents](index.md)
