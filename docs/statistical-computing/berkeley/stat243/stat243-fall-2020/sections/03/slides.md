---
title: Slides
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/slides.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/03/slides.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Slides

**Source:** [`sections/03/slides.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/03/slides.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Assertions and<br>testing<br><!-- End of picture text -->

**STAT 243 Section 3 Zoe Vernon**

Assertion vs. Testing

# **Assertions**

# **Testing**

- Produce error message inside a function

- Document private properties and assumptions of a class.

- Work on live data

   - Allows testing of infinitely many cases

- Produce error message based on function output

- ● Check externally visible properties.

- Tests only a small number of cases.

Both assertions and testings are a part of good defensive coding practices. They ensure that functions are working as expected.

Assertions

# **Assertions**

Assertions check whether a statement is true and return an error if not.

Three primary types

1. Pre-conditions: input as expected

2. Invariants:  intermediate computation as expected 3. Post-conditions: end values as expected

# **assertthat package**

assertthat is a package that provides functions for producing useful error messages. Three main functions

1. assert_that() signals an error if the argument passed to it is FALSE. 2. see_if() returns logical value with error message as attribute if the argument passed to it is FALSE.

3. validate_that() returns error message as a string if the argument passed to it is FALSE.

# **assertthat package**

It is good practice to add assertions in your functions to ensure they are behaving properly.

You can also add your own error messages using the on_failure() function. There is an example in the tutorial.

# **assertthat package**

Demo

Unit testing

# **Unit testing**

Unit testing describes reproducible tests that provide formal checks of function output.

This replaces the more informal version of testing where the user tests a number of examples in the command line.

There are a number of benefits including fewer bugs and better code structure.

# **testthat package**

R package for adding unit tests to your code.

There are two primary aspects of testings that form a hierarchy:

1. Tests: Check output of function is as expected.  You will likely have multiple tests per function.

2. Expectations: Tests are made up of a number of expectations about the properties of the output

# **testthat package**

Demo

---

[Up: contents](../../index.md)
