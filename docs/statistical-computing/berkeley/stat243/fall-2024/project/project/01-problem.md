---
title: Problem
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/project.qmd
source_file: sources/berkeley-stat243/fall-2024/project/project.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`project/project.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/project/project.qmd) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Problem

The project will be done in groups of three, with students assigned randomly.

The project, when split amongst the group
members, is not intended to be a huge undertaking. The goals of the
project are to give you experience in working collaboratively and
developing a well-designed, well-tested piece of software.

The project will be graded as a letter grade and will count for about as
much as two problem sets in your final grade.

Please use standard citation practices to cite any papers/code/online resources/chatbots whose ideas you make use of. Please do not consult with any people (in particular class members) who are not in your group. You are of course welcome to ask Chris or João questions.

Your task is to implement an adaptive-rejection sampler, described in
the Unit 9 notes (Section 5) and with details in Section 2.2 of Gilks
et al. (1992) - the PDF is in the `project` directory of the class Git repository. The result
should be an Python package that I can **easily** install and use.

My grading will be largely based on the following items.

1.  Your solution should allow the user to provide reasonable inputs,
    including the number of values to sample, and should check the
    inputs for validity. The primary input
    should be a Python function that calculates the (possibly unnormalized)
    density of the distribution of interest in a vectorized fashion (e.g., the pdf functions in scipy).
    Your code should include numerical checks that
    catch cases of non-log-concave densities as the calculations
    proceed. (I.e., you do not need to come up with an overall test of
    the input density, but you should be able to do some checks that
    will catch cases where the upper and lower bounds are not actually
    bounding the density.)

2.  Formal testing is required with a set of tests where samples are
    compared to the true distribution.  Given the
    overall output is stochastic, how to do this will require some thought. Note that an important
    part of the grade will depend on how your code performs on tests
    that I have prepared, so think broadly about the various kinds
    of densities a user might provide. You should also
    have unit tests for non-trivial individual functions that carry out the
    individual computations that make up the algorithm.

3.  Your solution should involve modular code, with functions or OOP
    methods that implement discrete tasks. You should have an overall
    design and style that is consistent across the components, in terms
    of functions vs. OOP methods, naming of functions/objects, etc.

4.  In terms of efficiency, the algorithm is inherently sequential.
    However, you should try to vectorize as much as possible and consider
    approaches that allow you to generate multiple points at once.

5.  Your solution should include clear, complete documentation, discussed further in the next section.

6. You should start by using numerical differentiation to estimate the gradients you need. But for an "A" solution, I'd like to see the capability to use automatic differentiation (AD) via JAX or PyTorch.  Often we'd use JAX/PyTorch on a GPU, but here we'll just use them for their AD capabilities. There is no benefit here from using the GPU as we can't set up this problem to do a large number of identical calculations at once.

7. Your code can use any scipy/numpy/jax/pytorch calls you want as building blocks, but otherwise should not use or mimic any external code that implements adaptive rejection sampling.

---

[Up: contents](index.md) · [Formatting requirements and additional information →](02-formatting-requirements-and-additional-information.md)
