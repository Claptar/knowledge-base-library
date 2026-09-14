---
title: 5 Good coding practices
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit5-debug.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Good coding practices

**Source:** [`units/unit5-debug.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit5-debug.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some of these tips apply more to software development and some more to analyses done for specific projects; hopefully it will be clear in most cases.

### **5.1 Editors**

Use an editor that supports the language you are using (e.g., _Emacs_ / _Aquamacs_ , _vim, TextMate, WinEdt_ , _Tinn-R_ , or the built-in editors in _RStudio_ or the Mac R GUI). Some advantages of this can include: (1) helpful color coding of different types of syntax and of strings, (2) automatic indentation and spacing, (3) code can often be run or compiled from within the editor, (4) parenthesis matching, (5) line numbering (good for finding bugs).

### **5.2 Coding syntax**

Here are some style guides:

- Adler has style tips.

- Hadley Wickham’s style guide.

- A empirical style guide based on the code of R Core and key package developers.

- Google’s R style guide.

- This R journal article summarizes the state of naming styles on CRAN.

And here’s a summary of my own thoughts:

- Header information: put metainfo on the code into the first few lines of the file as comments. Include who, when, what, how the code fits within a larger program (if appropriate), possibly the versions of R and key packages that you wrote this for

- Indentation: do this systematically (your editor can help here). This helps you and others to read and understand the code and can help in detecting errors in your code because it can expose lack of symmetry.

- Whitespace: use a lot of it. Some places where it is good to have it are (1) around operators (assignment and arithmetic), (2) between function arguments and list elements, (3) between matrix/array indices, in particular for missing indices.

- Use blank lines to separate blocks of code and comments to say what the block does

9

- Split long lines at meaningful places.

- Use parentheses for clarity even if not needed for order of operations. For example, a/y*x will work but is not easy to read and you can easily induce a bug if you forget the order of ops.

- Documentation - add lots of comments (but don’t belabor the obvious). Remember that in a few months, you may not follow your own code any better than a stranger. Some key things to document: (1) summarizing a block of code, (2) explaining a very complicated piece of code - recall our complicated regular expressions, (3) explaining arbitrary constant values.

- For software development, break code into separate files (<2000-3000 lines per file) with meaningful file names and related functions grouped within a file.

- Choose a consistent naming style for objects and functions: e.g. _nIts_ vs. _n.its_ vs _numberOfIts_ vs. _n_its_

   - This R journal article summarizes the state of naming styles on CRAN.

   - Adler and Google’s R style guide recommend naming objects with lowercase words, separated by periods, while naming functions by capitalizing the name of each word that is joined together, with no periods.

   - On the other hand, programmers who use other languages dislike R code with periods in it except in the context of object-oriented programming (OOP). E.g., _summary.lm_ is clear in that the period distinguishes the method from the class. Naming a method something like _special.summary.lm_ or an object _my.summary_ then confuses things. Personally, I suggest avoiding periods except for OOP.

- Try to have the names be informative without being overly long.

- Don’t overwrite names of objects/functions that already exist in R. E.g., don’t use ’lm’. > exists(“lm”)

- Use active names for functions (e.g., _calcLogLik_ , _calc_logLik_ )

- Learn from others’ code

This semester, someone will be reading your code - Jarrod and me when we look at your assignments. So to help us in understanding your code and develop good habits, put these ideas into practice in your assignments.

10

### **5.3 Coding style**

This is particularly focused on software development, but some of the ideas are useful for data analysis as well.

- Break down tasks into core units

- Write reusable code for core functionality and keep a single copy of the code (w/ backups of course) so you only need to change it once

- Smaller functions are easier to debug, easier to understand, and can be combined in a modular fashion (like the UNIX utilities)

- Write functions that take data as an argument and not lines of code that operate on specific data objects. Why? Functions allow us to reuse blocks of code easily for later use and for recreating an analysis (reproducible research). It’s more transparent than sourcing a file of code because the inputs and outputs are specified formally, so you don’t have to read through the code to figure out what it does.

- Functions should:

      - be modular (having a single task);

      - have meaningful name; and

      - have a comment describing their purpose, inputs and outputs (see the help file for an R function for how this is done in that context).

- Object orientation is a nice way to go

- Don’t hard code numbers - use variables (e.g., number of iterations, parameter values in simulations), even if you don’t expect to change the value, as this makes the code more readable:

   - speedOfLight <- 3e8

- Use R lists to keep disparate parts of related data together

- Practice defensive programming

      - check function inputs and warn users if the code will do something they might not expect or makes particular choices;

      - check inputs to _if_ and the ranges in _for_ loops;

11

   - provide reasonable default arguments;

   - document the range of valid inputs;

   - check that the output produced is valid; and

   - stop execution based on checks and give an informative error message.

- Try to avoid system-dependent code that only runs on a specific version of an OS or specific OS

- Learn from others’ code

- Consider rewriting your code once you know all the settings and conditions; often analyses and projects meander as we do our work and the initial plan for the code no longer makes sense and the code is no longer designed specifically for the job being done.

### **5.4 Version control**

- Use it! Even for projects that only you are working on.

- Use an issues tracker, or at least a simple to-do file, noting changes you’d like to make in the future.

- In addition to good commit messages, it’s a good idea to keep good notes documenting your projects.

We’ve already seen Git in a lot of detail, so not too much more to say here.

### **5.5 Dealing with run-time errors**

When writing functions, and software more generally, you’ll want to warn the user or stop execution when there is an error and exit gracefully, giving the user some idea of what happened. The _warning()_ and _stop()_ functions allow you to do this; in general they would be called based on an if statement. To stop code if a condition is not satisfied, you can use _stopifnot()_ , e.g.,

> x <- 3

> stopifnot(is(x, "matrix"))

These approaches allow you to catch errors that can be anticipated.

Here’s an example of building a robust square root function using _stop()_ and _warning()_ . Note you could use stopifnot(is.numeric(x)) in place of one of the checks here.

12

mysqrt <- **function** (x) { **if** ( **is.list** (x)) { **warning** ("x is a list; converting to a vector") x <- **unlist** (x) } **if** (! **is.numeric** (x)) { **stop** ("What is the square root of 'bob'?") } **else** { **if** ( **any** (x < 0)) { **warning** ("mysqrt: found negative values; proceeding anyway") x[x >= 0] <- (x[x >= 0])^(1/2) x[x < 0] <- NaN **return** (x) } **else return** (x^(1/2)) } } **mysqrt** ( **c** (1, 2, 3)) ## [1] 1.000 1.414 1.732 **mysqrt** ( **c** (5, -7)) ## Warning: mysqrt: found negative values; proceeding anyway ## [1] 2.236 NaN **mysqrt** ( **c** ("asdf", "sdf")) **## Error: What is the square root of ’bob’? mysqrt** ( **list** (5, 3, "ab")) ## Warning: x is a list; converting to a vector **## Error: What is the square root of ’bob’?**

You can control what happens when a warning occurs with _options()$warning_ . This can be helpful for debugging - e.g., you can force R to stop if a warning is issued rather than continuing so you can delve into what happened.

Also, sometimes a function you call will fail, but you want to continue execution. For example,

13

suppose you are fitting a bunch of linear models and occasionally the design matrix is singular. You can wrap a function call within the _try()_ function (or _tryCatch()_ ) and then your code won’t stop. You can also evaluate whether a given function call executed properly or not. Here’s an example of fitting a model for extreme values:

**library** (ismev) _## Loading required package: mgcv ## Loading required package: nlme ## This is mgcv 1.8-2. For overview type ’help("mgcv-package")’._ **library** (methods) n <- 100 nDays <- 365 x <- **matrix** ( **rnorm** (nDays * n), nr = nDays) x <- **apply** (x, 2, max) x <- **cbind** ( **rep** (0, 100), x) params <- **matrix** (NA, nr = **ncol** (x), nc = 3) **for** (i **in** 1: **ncol** (x)) { fit <- **try** ( **gev.fit** (x[, i], show = FALSE)) **if** (! **is** (fit, "try-error")) params[i, ] = fit$mle } params ## [,1] [,2] [,3] ## [1,] NA NA NA ## [2,] 2.723 0.315 -0.04806

**Challenge** : figure out how to use _tryCatch()_ to deal with the error above. Note that I haven’t used it and it seemed somewhat inscrutable on quick look.

---

[← 4 Getting help online](08-4-getting-help-online.md) · [Up: contents](index.md) · [6 Tips for running analyses →](10-6-tips-for-running-analyses.md)
