---
title: Problem
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/project.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/project/project.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem

**Source:** [`project/project.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/project/project.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Your task is to make an R package to implement a genetic algorithm for variable selection in regression problems, including both linear regression and GLMs. Some details on genetic algorithms are available in Section 3.4 of the Givens and Hoeting book on Computational Statistics - see the electronic book available through UC Library search, or the PDF of Chapter 3 in the _project_ directory of the class GitHub repo. You should also be able to find plenty of other information about genetic algorithms online.

1. Your solution should allow the user to provide reasonable inputs, in terms of specifying a dataset and the type of regression. Much of this is information you should just be able to pass along to _lm()_ or _glm()_ . By default you should just use AIC as your objective criterion but allow users to provide their own objective function. Similarly you can use the genetic operators described in Givens and Hoeting for variable selection, but ideally your code should be general enough that a user could provide additional operators.

2. Your solution should involve modular code, with functions or OOP methods that implement discrete tasks. You should have an overall design and style that is consistent across the components, in terms of functions vs. OOP methods, naming of objects, etc.

3. In terms of efficiency, the generations are inherently sequential. However, you should try to vectorize as much as possible. If you like, you can allow for parallel processing on a single machine when working with the population in a given generation, in particular the evaluation of the fitness function, but it is not required.

4. Show the results of using your implementation on two or more examples. Have the use of the package on the examples be coded in the example section of the R help for your main function.

1

5. Formal testing is required, with a set of tests where results are compared to some known truth. You should have tests for the overall function and any modules that do anything complicated. For testing the overall function, since the algorithm is stochastic, you’ll need to think carefully about how to set this up. You should also have unit tests for individual functions that carry out the individual computations that make up the algorithm. See more details below on how to set up the tests. There is more information on testing here: https://r-pkgs.had.co.nz/tests.html.

6. You should be writing your own code for essentially everything except the model fitting and other standard functionality available in base R and the R packages such as _stats_ that are provided with the standard R installation. If you’d like to use any other code or packages, please consult with me first.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Formatting requirements and additional information →](03-formatting-requirements-and-additional-information.md)
