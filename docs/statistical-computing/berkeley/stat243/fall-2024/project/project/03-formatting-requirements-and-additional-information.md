---
title: Formatting requirements and additional information
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/project.qmd
source_file: sources/berkeley-stat243/fall-2024/project/project.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Formatting requirements and additional information

**Source:** [`project/project.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/project.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

1. Your solution to the problem should have two parts:

   a. A Python package named `ars`, which can be as simple as a directory named `ars` with .py modules and an `__init__.py`. (If you'd like to get experience with creating a package that could be installed via `pip` or `conda install` you're welcome to explore that but it's not required.) The package should be made available to me via a private repository named `ars-dev` within the Berkeley GitHub account or github.com account of one of the project members. **Make sure to share the repository with me** (my username is `paciorek` in either `github.berkeley.edu` or `github.com`.)

       The package should include:

       i. A primary function called `ars` that carries out the sampling, including appropriate code comments.

       ii. Other supporting code in the same or additional files (please think about clear organization), including appropriate code comments.

       iii. Formal tests set up using `pytest` and included in the package. I should be able to easily run these tests.

       iv. Help information for the main function, in the form of a standard Python docstring for `ars`. As part of this, you should have working examples in the example section of the docstring. You do not need extensive docstrings for your auxiliary functions but there should be a brief docstring just stating what each function does.

   b. A PDF document describing your solution, provided as a Quarto document (you're welcome to develop this using a Jupyter notebook and then convert to qmd). The description does not need to be more than 2-4 pages, but it should summarize the approach you took in terms of functions/modularity/object-oriented programming, the testing that you carried out, and the results of applying the implementation to various examples. It must include a paragraph describing the specific contributions of each team member and which person/people were responsible for each component of the work. Please submit a paper copy of the document to me - either directly to me, under my door, or in my mailbox. **On your paper solution, please indicate the URL of the GitHub repository for the project.**

2. You should start the process by mapping out the modular components you need to write and how they will fit together, as well as what the primary function will do. After one person writes a component, another person on the team should test it and, with the original coder, improve it. You could also consider using pair programming for some of your development.

3. You should use Git and GitHub to manage your collaboration.

---

[← Problem](02-problem.md) · [Up: contents](index.md)
