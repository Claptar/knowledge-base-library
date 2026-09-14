---
title: Substantive and formatting requirements
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/project/project.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/project/project.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Substantive and formatting requirements

**Source:** [`project/project.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/project/project.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Your solution should allow the user to provide reasonable inputs, in terms of specifying a dataset and regression model formula, as well as the type of regression. Much of this is information you should just be able to pass along to _lm()_ or _glm()_ . By default you should just use AIC as your objective criterion/fitness function, but allow users to provide their own fitness function. Similarly you can use the genetic operators described in Givens and Hoeting for variable selection, but ideally your code should be general enough that a user could provide additional operators.

2. Your solution should involve modular code, with functions or OOP methods that implement discrete tasks. You should have an overall design and style that is consistent across the components, in terms of functions vs. OOP methods, naming of objects, etc.

3. In terms of efficiency, the generations are inherently sequential. However, you should try to vectorize as much as possible. If you like, you can allow for shared memory parallel processing when working with the population in a given generation, in particular the evaluation of the fitness function, but it is not required.

4. Show the results of using your implementation on one or more real examples. Have the use of the package on the example(s) be coded in the example section of the R help for one or more of your functions.

1

5. Formal testing is required, with a set of tests where results are compared to some known truth. You should have tests for the overall function and any modules that do anything complicated. For testing the overall function, since the algorithm is stochastic, you’ll need to think carefully about how to set this up. The output of your testing should be clear and interpretable. I.e., when I run your tests I should see informative messages of what is being done and whether a given test was passed or failed. You should also have unit tests for individual functions that carry out the individual computations that make up the algorithm. Please use the _testthat_ package, for which there is information here: http://r-pkgs.had.co.nz/tests.html.

6. Your solution should include help/manual information as follows:

   - (a) Basic doc strings for any function you create (i.e., include comments at the beginning of the function), as well as commenting of code as appropriate.

   - (b) An overall help page for the primary function. This help page should be directly in the form of standard R documentation in a file called _select.Rd_ . You can either write _select.Rd_ by hand or you can have it generated based on using the _roxygen2_ package (see http://adv-r.had.co.nz/Documentingfunctions.html for an example), with the documentation included in the R code files. You do not need help pages for your auxiliary functions.

7. Your solution to the problem should have two parts:

   - (a) An R package named _GA_ , including the .tar.gz file created by R CMD build GA. I should be able to install your package by simply running install_github(paste0(username, ’/GA’)) where _username_ contains the Github user name of the group member in whose Github account the project resides. A good starting place for information about R packages is Hadley Wickham’s book: http://r-pkgs.had.co.nz/. You can use _devtools::create_ to create the initial set of directories for the package.

The package should include:

      - i. A primary function called _select_ that carries out the variable selection, located in a file _select.R_ in the _R_ directory of the package.

      - ii. Other supporting code in additional files in the _R_ directory of the package.

      - iii. Formal tests, located in the _tests_ directory of the package. I don’t care about the exact structure of the tests folder in your R package, so long as I can run test_package(’GA’) and have it run all your tests.

      - iv. Help information for the main function, in a file _select.Rd_ in the _man_ directory.

   - (b) A PDF document describing your solution, prepared in L<sup>A</sup> TEX or R Markdown. The description does not need to be more than a couple pages, but should describe the approach you took in terms of functions/modularity/object-oriented programming, the testing that you carried out, and the results of applying the implementation to the example(s). It must include a paragraph describing the specific contributions of each team member and which person/people were responsible for each component of the work. Please submit a paper copy of the document to me - either directly to me, under my door, or in my mailbox. On your paper solution, please indicate the Github user name of the group member in whose Github repository the final version of the project resides.

8. You should be writing your own code for essentially everything except the model fitting and other standard functionality available in base R and the R packages such as _stats_ that are provided with the standard R installation. If you’d like to use any other code or packages, please consult with me first.

2

9. You should use Git and Github to manage your collaboration. Please have the project be a repository named (exactly) _GA_ within the Github account of one of the project members.

10. You should start the process by mapping out the modular components you need to write and how they will fit together, as well as what the primary function will do. After one person writes a component, another person on the team should test it and, with the original coder, improve it.

3

---

[← Problem](02-problem.md) · [Up: contents](index.md)
