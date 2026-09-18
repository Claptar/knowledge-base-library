---
title: 1 Good coding practices
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit4-goodPractices.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit4-goodPractices.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit4-goodPractices.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit4-goodPractices.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Good coding practices

August 30, 2021

Sources:
• Chambers
• Hadley Wickham's advanced R notes on debugging.
• Roger Peng's notes on debugging in R
• Murrell, Introduction to Data Technologies, Ch. 2
• Journal of Statistical Software vol. 42: 19 Ways of Looking at Statistical Software
• Wilson et at., Best practices for scientific computing, ArXiv:1210:0530
• Gentzkow and Shapiro tutorial for social scientists
• https://github.com/berkeley-stat243/stat243-fall-2014/blob/master/section/millman-perez.pdf
• Chapter 11 of Transparent and Reproducible Social Science Research

This unit covers good coding/software development practices, debugging (and practices for avoiding bugs), and doing reproducible research. As in later units of the course, the material is generally not specific to R, but some details and the examples are in R.

Some of these tips apply more to software development and some more to analyses done for specific projects; hopefully it will be clear in most cases.

### 1.1 Editors

Use an editor that supports the language you are using (e.g., *Sublime*, *Atom*, *Emacs/Aquamacs*, *vim*, *VSCode*, *TextMate*, *WinEdt*, *Tinn-R*, or the built-in editors in *RStudio*). Some advantages of this can include: (1) helpful color coding of different types of syntax and of strings, (2) automatic indentation and spacing, (3) code can often be run or compiled from within the editor, (4) parenthesis matching, (5) line numbering (good for finding bugs).

### 1.2 Coding syntax

The files *goodCode.R* and *badCode.R* in the *units* directory of the class repository provide examples of code written such that it does and does not conform to the suggestions listed in this section. Here are some style guides:

• Adler has style tips.
• Hadley Wickham's style guide.
• A empirical style guide based on the code of R Core and key package developers.
• Google's R style guide.
• This R journal article summarizes the state of naming styles on CRAN.

And here's a summary of my own thoughts:

• Header information: put metainfo on the code into the first few lines of the file as comments. Include who, when, what, how the code fits within a larger program (if appropriate), possibly the versions of R and key packages that you wrote this for

• Indentation: do this systematically (your editor can help here). This helps you and others to read and understand the code and can help in detecting errors in your code because it can expose lack of symmetry.

• Whitespace: use a lot of it. Some places where it is good to have it are (1) around operators (assignment and arithmetic), (2) between function arguments and list elements, (3) between matrix/array indices, in particular for missing indices.

• Use blank lines to separate blocks of code and comments to say what the block does

• Split long lines at meaningful places.

• Use parentheses for clarity even if not needed for order of operations. For example, `a/y*x` will work but is not easy to read and you can easily induce a bug if you forget the order of ops.

• Documentation - add lots of comments (but don't belabor the obvious). Remember that in a few months, you may not follow your own code any better than a stranger. Some key things to document: (1) summarizing a block of code, (2) explaining a very complicated piece of code - recall our complicated regular expressions, (3) explaining arbitrary constant values.

• For software development, break code into separate files (<2000-3000 lines per file) with meaningful file names and related functions grouped within a file.

• Choose a consistent naming style for objects and functions: e.g. *nIts* vs. *n.its* vs *numberOfIts* vs. *n_its*

  – This R journal article summarizes the state of naming styles on CRAN.

  – Adler and Google's R style guide recommend naming objects with lowercase words, separated by periods, while naming functions by capitalizing the name of each word that is joined together, with no periods.

  – On the other hand, programmers who use other languages dislike R code with periods in it except in the context of object-oriented programming (OOP). E.g., *summary.lm* is clear in that the period distinguishes the method from the class. Naming a method something like *special.summary.lm* or an object *my.summary* then confuses things. Personally, I suggest avoiding periods except for OOP.

• Try to have the names be informative without being overly long.

• Don't overwrite names of objects/functions that already exist in R. E.g., don't use 'lm'.
```R
> exists('lm')
```

• Use active names for functions (e.g., *calcLogLik*, *calc_logLik* rather than *logLik* or *logLikCalc*). The idea is that a function in a programming language is like a verb in regular language (a function does something), so use a verb in naming it.

• Learn from others' code

This semester, someone will be reading your code - Omid and me when we look at your assignments. So to help us in understanding your code and develop good habits, put these ideas into practice in your assignments.

### 1.3 Coding style

This is particularly focused on software development, but some of the ideas are useful for data analysis as well.

• Break down tasks into core units

• Write reusable code for core functionality and keep a single copy of the code (w/ backups of course or ideally version control) so you only need to make changes to a piece of code in one place

• Smaller functions are easier to debug, easier to understand, and can be combined in a modular fashion (like the UNIX utilities)

• Write functions that take data as an argument and not lines of code that operate on specific data objects. Why? Functions allow us to reuse blocks of code easily for later use and for recreating an analysis (reproducible research). It's more transparent than sourcing a file of code because the inputs and outputs are specified formally, so you don't have to read through the code to figure out what it does.

• Functions should:
  – be modular (having a single task);
  – have meaningful name; and
  – have a comment describing their purpose, inputs and outputs (see the help file for an R function for how this is done in that context).

• Write tests for each function (i.e., unit tests)

• Object orientation is a nice way to go

• Don't hard code numbers - use variables (e.g., number of iterations, parameter values in simulations), even if you don't expect to change the value, as this makes the code more readable:
```R
> speedOfLight <- 3e8
```

• Use R lists to keep disparate parts of related data together

• Practice defensive programming (see also the discussion below on assertions)
  – check function inputs and warn users if the code will do something they might not expect or makes particular choices;
  – check inputs to *if* and the ranges in *for* loops:
    * use `seq_len()` and `seq_along()` instead of `1:n` in setting up for loops
    * use `if(isTRUE(condition))` in if statements in case condition is NA (which would otherwise cause an error)
  – provide reasonable default arguments;
  – document the range of valid inputs;
  – check that the output produced is valid; and
  – stop execution based on checks and give an informative error message.

• Try to avoid system-dependent code that only runs on a specific version of an OS or specific OS

• Learn from others' code

• Consider rewriting your code once you know all the settings and conditions; often analyses and projects meander as we do our work and the initial plan for the code no longer makes sense and the code is no longer designed specifically for the job being done.

### 1.4 Assertions and testing

Both tests and assertions are critically important for writing robust code that is less likely to contain bugs.

Assertions are checks in your code that the state of the program is as you expect, including arguments provided by users. In addition to simple use of `stopifnot()` and using `if()` combined with `stop()` and `warning()`, the *assertthat* and *assertr* packages provide useful tools. The *checkmate* package specifically helps in checking arguments.

Tests evaluate whether your code operates correctly. This can include tests that your code provides correct and useful errors when something goes wrong (so that means that a test might be to see if problematic input correctly produces an error). Unit tests are intended to test the behavior of small pieces (units) of code, generally individual functions. Unit tests naturally work well with the ideas above of writing small, modular functions. *testthat* and other packages are designed to make it easier to write sets of good tests.

In Section 2 on September 11, we'll go over assertions and testing in detail.

### 1.5 Version control

• Use it! Even for projects that only you are working on.

• Use an issues tracker (e.g., the Github issues tracker is quite nice), or at least a simple to-do file, noting changes you'd like to make in the future.

• In addition to good commit messages, it's a good idea to keep good notes documenting your projects.

We've already seen Git some and will see it in a lot more detail later in the semester, so not too much more to say here.

## 2 Debugging and recommendations for avoiding bugs

The *R debugging tutorial* has information on
• basic debugging strategies,
• using R's interactive debugging tools,
• common causes of bugs,
• tips and tools for avoiding bugs and catching errors, and
• information on how to get help online.

In a lab in coming weeks, we'll go over debuggin in detail, so you don't need to look through the *R debugging tutorial* at this time.

## 3 Tips for running analyses

Save your output at intermediate steps (including the random seed state) so you can restart if an error occurs or a computer fails. Using `save()` and `save.image()` to write to *.Rda* (*.RData*) files work well for this.

Run your code on a small subset of the problem before setting off a job that runs for hours or days. Make sure that the code works on the small subset and saves what you need properly at the end.

---

[Up: contents](index.md) · [4 Reproducible research →](02-4-reproducible-research.md)
