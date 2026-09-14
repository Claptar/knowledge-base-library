---
title: Problem
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/project/project.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/project/project.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem

**Source:** [`project/project.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/project/project.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Your task is to implement an genetic algorithm for variable selection in regression problems, including both linear regression and GLMs. Some details are available in Section 3.4 of the Givens and Hoeting book on Computational Statistics - see the electronic book available on Oskicat, or the PDF of Chapter 3 in the class Github repo. You should also be able to find plenty of other information about genetic algorithms online.

1. Your solution should allow the user to provide reasonable inputs, in terms of specifying a dataset and regression model formula, as well as the type of regression. Much of this is information you should just be able to pass along to _lm()_ or _glm()_ . By default you should just use AIC as your objective criterion/fitness function, but allow users to provide their own fitness function. Similarly you can use the genetic operators described in Givens and Hoeting for variable selection, but ideally your code should be general enough that a user could provide additional operators.

2. Formal testing is required, with a set of tests where results are compared to some known truth. You should have tests for the overall function, and for any modules that do anything complicated. For testing the overall function, since the algorithm is stochastic, you’ll need to think carefully about how to set this up. The output of your testing function should be clear and interpretable. I.e., when I run your test function, it should print informative messages of what it is doing and whether the test was passed or failed.

3. Your solution should involve modular code, with functions or OOP methods that implement discrete tasks. You should have an overall design and style that is consistent across the components, in terms of functions vs. OOP methods, naming of objects, etc.

4. In terms of efficiency, the generations are inherently sequential. However, you should try to vectorize as much as possible and allow for shared memory parallel processing when working with the population in a given generation, in particular the evaluation of the fitness function.

5. Show the results of using your implementation on one or more real examples. One possibility is to use it on a subset of the airline data from PS6. For example, you could model delay/non-delay based on predictors such as origin airport, destination airport, month-year combinations, origin-destination pairs, etc. But you don’t have to use this dataset.

6. Your solution should include help/manual information as follows: (a) basic doc strings for any function you create (i.e., include comments at the beginning of the function), as well as commenting of code as appropriate. (b) An overall help page for the primary function. This could be in the form of comments in the R code in the form used in the _roxygen2_ package (see http://adv-r.had.co.nz/Documentingfunctions.html for an example) or simply a PDF (e.g., see the help info on, say, p. 29 of http://www.cran.rproject.org/web/packages/spam/spam.pdf for help on the _chol()_ function in the _spam_ package). I’d prefer the first (and that is likely to be easier), but the latter is fine too.

2

---

[← Formatting requirements](02-formatting-requirements.md) · [Up: contents](index.md)
