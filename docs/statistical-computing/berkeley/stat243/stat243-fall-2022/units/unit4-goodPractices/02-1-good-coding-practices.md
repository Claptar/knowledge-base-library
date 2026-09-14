---
title: 1. Good coding practices
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit4-goodPractices.md
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit4-goodPractices.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Good coding practices

**Source:** [`units/unit4-goodPractices.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit4-goodPractices.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

Some of these tips apply more to software development and some more to
analyses done for specific projects; hopefully it will be clear in most
cases.

## Editors

Use an editor that supports the language you are using (e.g., *Atom*, *Emacs*/*Aquamacs*, *Sublime*, *vim*, *VSCode*, *TextMate*, *WinEdt*, or
the built-in editor in *RStudio*). Some advantages of this can include:
(1) helpful color coding of different types of syntax and of strings,
(2) automatic indentation and spacing, (3) code can often be run or
compiled from within the editor, (4) parenthesis matching, (5) line
numbering (good for finding bugs).

## Coding syntax

The files [goodCode.R](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/goodCode.R) and [badCode.R](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/badCode.R) in the *units* directory of the
class repository provide examples of code written such that it does and
does not conform to the suggestions listed in this section.

Here are some R-related style guides:

- Adler has style tips.
- The [tidyverse style guide](https://style.tidyverse.org/) or its offshoot [Google R style](https://google.github.io/styleguide/Rguide.html).
- A [empirical style guide](http://cran.r-project.org/web/packages/rockchalk/vignettes/Rstyle.pdf) based on the code of R Core and key package developers.
- This [R journal article](http://journal.r-project.org/archive/2012-2/RJournal_2012-2_Baaaath.pdf) summarizes the state of naming styles on CRAN.

And here's a summary of my own thoughts:

- Header information: put metainfo on the code into the first few
    lines of the file as comments. Include who, when, what, how the code
    fits within a larger program (if appropriate), possibly the versions
    of R and key packages that you used.
- Indentation: do this systematically (your editor can help here).
    This helps you and others to read and understand the code and can
    help in detecting errors in your code because it can expose lack of
    symmetry.
- Whitespace: use a lot of it. Some places where it is good to have it
    are
    - around operators (assignment and arithmetic);
    - between function arguments;
    - between list elements; and
    - between matrix/array indices, in particular for missing indices.
- Use blank lines to separate blocks of code and comments to say what
    the block does
- Split long lines at meaningful places.
- Use parentheses for clarity even if not needed for order of
    operations. For example, `a/y*x` will work but is not easy to read
    and you can easily induce a bug if you forget the order of ops.
- Documentation - add lots of comments (but don't belabor the
    obvious). Remember that in a few months, you may not follow your own
    code any better than a stranger. Some key things to document: (1)
    summarizing a block of code, (2) explaining a very complicated piece
    of code - recall our complicated regular expressions, (3) explaining
    arbitrary constant values.
- For software development, break code into separate files
    (2000-3000 lines per file) with meaningful file names and related
    functions grouped within a file.
-  Choose a consistent naming style for objects and functions: e.g.
    *nIts* vs. *n.its* vs *numberOfIts* vs. *n_its*
    - This [R journal article](http://journal.r-project.org/archive/2012-2/RJournal_2012-2_Baaaath.pdf) summarizes the state of naming styles on CRAN.
    - In object-oriented languages such as  Python and Java, periods are used in the context of object-oriented programming, so I recommend not using periods in the names of your objects.
- Try to have the names be informative without being overly long.
- Don't overwrite names of objects/functions that already exist in R. E.g., don't use 'lm'. That said, the namespace system helps with the unavoidable cases where there are name conflicts.
- Use active names for functions (e.g., *calcLogLik*, *calc_logLik*
    rather than *logLik* or *logLikCalc*). The idea is that a function
    in a programming language is like a verb in regular language (a
    function *does* something), so use a verb in naming it.
- Learn from others' code

This semester, someone will be reading your code - the GSI and and me when we
look at your assignments. So to help us in understanding your code and
develop good habits, put these ideas into practice in your assignments.

## Coding style

This is particularly focused on software development, but some of the
ideas are useful for data analysis as well.

- Break down tasks into core units
- Write reusable code for core functionality and keep a single copy of
    the code (w/ backups of course or ideally version control) so you
    only need to make changes to a piece of code in one place
- Smaller functions are easier to debug, easier to understand, and can
    be combined in a modular fashion (like the UNIX utilities)
- Write functions that take data as an argument and not lines of code
    that operate on specific data objects. Why? Functions allow us to
    reuse blocks of code easily for later use and for recreating an
    analysis (reproducible research). It's more transparent than
    sourcing a file of code because the inputs and outputs are specified
    formally, so you don't have to read through the code to figure out
    what it does.
- Functions should:
    - be modular (having a single task);
    - have meaningful name; and
    - have a comment describing their purpose, inputs and outputs (see the help file for an R function of your choice for how this is done in that context).
- Write tests for each function (i.e., unit tests)
- Don't hard code numbers - use variables (e.g., number of iterations,
    parameter values in simulations), even if you don't expect to change
    the value, as this makes the code more readable. For example, the speed of light is a constant in a scientific sense, but best to make it a variable in code: `speedOfLight <- 3e8`
- Use R lists to keep disparate parts of related data together
- Practice defensive programming (see also the discussion below on assertions)
    - check function inputs and warn users if the code will do something they might not expect or makes particular choices;
    - check inputs to *if* and the ranges in *for* loops:
        - use `seq_len()` and `seq_along()` instead of `1:n` in setting up for loops
        - use `if(isTRUE(condition))` in if statements in case the condition is NA (which would otherwise cause an error)
    - provide reasonable default arguments;
    - document the range of valid inputs;
    - check that the output produced is valid; and
    - stop execution based on checks and give an informative error message.
- Try to avoid system-dependent code that only runs on a specific
    version of an OS or specific OS
- Learn from others' code
- Consider rewriting your code once you know all the settings and
    conditions; often analyses and projects meander as we do our work
    and the initial plan for the code no longer makes sense and the code
    is no longer designed specifically for the job being done.

## Assertions and testing

Both tests and assertions are critically important for writing robust
code that is less likely to contain bugs.

Assertions are checks in your code that the state of the program is as
you expect, including arguments provided by users. In addition to simple
use of *stopifnot()* and using *if()* combined with *stop()* and
*warning()*, the *assertthat* and *assertr* packages provide useful
tools. The *checkmate* package specifically helps in checking arguments.

Tests evaluate whether your code operates correctly. This can include
tests that your code provides correct and useful errors when something
goes wrong (so that means that a test might be to see if problematic
input correctly produces an error). *Unit tests* are intended to test
the behavior of small pieces (units) of code, generally individual
functions. Unit tests naturally work well with the ideas above of
writing small, modular functions. *testthat* and other packages are
designed to make it easier to write sets of good tests.

In Lab 2, we'll go over assertions and testing in
detail.

## Version control

- Use it! Even for projects that only you are working on.
- Use an issues tracker (e.g., the GitHub issues tracker is quite
    nice), or at least a simple to-do file, noting changes you'd like to
    make in the future.
- In addition to good commit messages, it's a good idea to keep good
    running notes documenting your projects.

We've already seen Git some and will see it in a lot more detail later
in the semester, so I don't have more to say here.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Debugging and recommendations for avoiding bugs →](03-2-debugging-and-recommendations-for-avoiding-bugs.md)
