---
title: 1 Good coding practices
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit4-goodPractices.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit4-goodPractices.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Good coding practices

**Source:** [`units/unit4-goodPractices.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit4-goodPractices.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some of these tips apply more to software development and some more to analyses done for specific projects; hopefully it will be clear in most cases.

1

### **1.1 Editors**

Use an editor that supports the language you are using (e.g., _Sublime, Atom, Emacs_ / _Aquamacs_ , _vim, TextMate, WinEdt_ , _Tinn-R_ , or the built-in editors in _RStudio_ ). Some advantages of this can include: (1) helpful color coding of different types of syntax and of strings, (2) automatic indentation and spacing, (3) code can often be run or compiled from within the editor, (4) parenthesis matching, (5) line numbering (good for finding bugs).

### **1.2 Coding syntax**

The files _goodCode.R_ and _badCode.R_ in the _units_ directory of the class repository provide examples of code written such that it does and does not conform to the suggestions listed in this section. Here are some style guides:

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

- Split long lines at meaningful places.

2

- Use parentheses for clarity even if not needed for order of operations. For example, a/y*x will work but is not easy to read and you can easily induce a bug if you forget the order of ops.

- Documentation - add lots of comments (but don’t belabor the obvious). Remember that in a few months, you may not follow your own code any better than a stranger. Some key things to document: (1) summarizing a block of code, (2) explaining a very complicated piece of code - recall our complicated regular expressions, (3) explaining arbitrary constant values.

- For software development, break code into separate files (<2000-3000 lines per file) with meaningful file names and related functions grouped within a file.

- Choose a consistent naming style for objects and functions: e.g. _nIts_ vs. _n.its_ vs _numberOfIts_ vs. _n_its_

   - This R journal article summarizes the state of naming styles on CRAN.

   - Adler and Google’s R style guide recommend naming objects with lowercase words, separated by periods, while naming functions by capitalizing the name of each word that is joined together, with no periods.

   - On the other hand, programmers who use other languages dislike R code with periods in it except in the context of object-oriented programming (OOP). E.g., _summary.lm_ is clear in that the period distinguishes the method from the class. Naming a method something like _special.summary.lm_ or an object _my.summary_ then confuses things. Personally, I suggest avoiding periods except for OOP.

- Try to have the names be informative without being overly long.

- Don’t overwrite names of objects/functions that already exist in R. E.g., don’t use ’lm’. > exists(’lm’)

- Use active names for functions (e.g., _calcLogLik_ , _calc_logLik_ rather than _logLik_ or _logLikCalc_ )

- Learn from others’ code

This semester, someone will be reading your code - Omid and me when we look at your assignments. So to help us in understanding your code and develop good habits, put these ideas into practice in your assignments.

3

### **1.3 Coding style**

This is particularly focused on software development, but some of the ideas are useful for data analysis as well.

- Break down tasks into core units

- Write reusable code for core functionality and keep a single copy of the code (w/ backups of course or ideally version control) so you only need to make changes to a piece of code in one place

- Smaller functions are easier to debug, easier to understand, and can be combined in a modular fashion (like the UNIX utilities)

- Write functions that take data as an argument and not lines of code that operate on specific data objects. Why? Functions allow us to reuse blocks of code easily for later use and for recreating an analysis (reproducible research). It’s more transparent than sourcing a file of code because the inputs and outputs are specified formally, so you don’t have to read through the code to figure out what it does.

- Functions should:

   - be modular (having a single task);

   - have meaningful name; and

   - have a comment describing their purpose, inputs and outputs (see the help file for an R function for how this is done in that context).

- Write tests for each function (i.e., unit tests)

- Object orientation is a nice way to go

- Don’t hard code numbers - use variables (e.g., number of iterations, parameter values in simulations), even if you don’t expect to change the value, as this makes the code more readable:

> speedOfLight <- 3e8

- Use R lists to keep disparate parts of related data together

- Practice defensive programming (see also the discussion below on assertions)

   - check function inputs and warn users if the code will do something they might not expect or makes particular choices;

4

   - check inputs to _if_ and the ranges in _for_ loops:

      - <sup>use</sup><sup>_seq_len()_and</sup><sup>_seq_along()_instead of 1:n in setting up for loops</sup>

      - <sup>use if(isTRUE(condition)) in if statements in case condition is NA (which</sup> would otherwise cause an error)

   - provide reasonable default arguments;

   - document the range of valid inputs;

   - check that the output produced is valid; and

   - stop execution based on checks and give an informative error message.

- Try to avoid system-dependent code that only runs on a specific version of an OS or specific OS

- Learn from others’ code

- Consider rewriting your code once you know all the settings and conditions; often analyses and projects meander as we do our work and the initial plan for the code no longer makes sense and the code is no longer designed specifically for the job being done.

### **1.4 Assertions and testing**

Both tests and assertions are critically important for writing robust code that is less likely to contain bugs.

Assertions are checks in your code that the state of the program is as you expect, including arguments provided by users. In addition to simple use of _stopifnot()_ and using _if()_ combined with _stop()_ and _warning()_ , the _assertthat_ and _assertr_ packages provide useful tools. The _checkmate_ package specifically helps in checking arguments.

Tests evaluate whether your code operates correctly. This can include tests that your code provides correct and useful errors when something goes wrong (so that means that a test might be to see if problematic input correctly produces an error). _Unit tests_ are intended to test the behavior of small pieces (units) of code, generally individual functions. Unit tests naturally work well with the ideas above of writing small, modular functions. _testthat_ and other packages are designed to make it easier to write sets of good tests.

In Section 2 on September 11, we’ll go over assertions and testing in detail.

### **1.5 Version control**

- Use it! Even for projects that only you are working on.

5

- Use an issues tracker (e.g., the Github issues tracker is quite nice), or at least a simple to-do file, noting changes you’d like to make in the future.

- In addition to good commit messages, it’s a good idea to keep good notes documenting your projects.

We’ve already seen Git some and will see it in a lot more detail later in the semester, so not too much more to say here.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Debugging and recommendations for avoiding bugs →](03-2-debugging-and-recommendations-for-avoiding-bugs.md)
