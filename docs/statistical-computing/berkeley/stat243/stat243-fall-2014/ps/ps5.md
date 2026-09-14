---
title: 'Stat243: Problem Set 5, Due Wednesday Oct. 22'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps5.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/ps/ps5.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stat243: Problem Set 5, Due Wednesday Oct. 22

**Source:** [`ps/ps5.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/ps/ps5.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

October 15, 2014

Comments:

- This covers Unit 7.

- It’s due at the start of class on 10/22.

- Note that you can mix and match R and Python chunks in your knitr/Rmd documents. Simply use engine=’python’ for the Python ones.

- As usual, simply providing the raw code is not enough; make sure to describe how you approached the problem, the steps you took, and output illustrating what your code produces.

- Please note my comments in the syllabus about when to ask for help and about working together.

- As discussed in the syllabus, please turn in (1) a copy on paper, as this makes it easier for us to handle AND (2) an electronic copy through Git following Jarrod’s instructions.

## **Questions**

1. You’re working with a collaborator on a statistical model. They have the following independent binomial data, _yi ∼_ Binom( _n, pi_ ), for which they are estimating the likelihood as


using _prod()_ and _dbinom()_ in R. They tell you that they are getting zero for the likelihood regardless of the value of _β_ , using the data in the file _ps5prob1.Rda_ (this file provides one possible _β_ value as well as _y_ and _X_ ). Verify this and then explain to them what the problem is and how to do the calculation.

2. Here we’ll consider the effects of adding together numbers of very different sizes. Let’s consider adding the number 1 to 10000 copies of the number 1 _×_ 10<sup>_−_16</sup> . Mathematically the answer is obviously 1 + 1 _×_ 10<sup>_−_12</sup> = 1 _._ 000000000001 by multiplication, but we want to use this as an example of the accuracy of summation with numbers of very different magnitudes, so consider the sum 1 + 1 _×_ 10<sup>_−_16</sup> + _· · ·_ + 1 _×_ 10<sup>_−_16</sup> .

   - (a) How many decimal places of accuracy are the most we can expect of our result (i.e., assuming we don’t carry out the calculations in a dumb way). In other words, if we store 1.000000000001 on a computer, how many decimal places of accuracy do we have? This is not a trick question.

1

- (b) In R, create the vector _x_ = _c_ (1 _,_ 1 _×_ 10<sup>_−_16</sup> _, . . . ,_ 1 _×_ 10<sup>_−_16</sup> ). Does the use of _sum()_ give the right answer up to the accuracy expected from part (a)?

- (c) Do the same as in (b) for Python. For Python the _Decimal()_ function from the decimal package is useful for printing additional digits. Also, this code will help you get started in creating the needed vector:

import numpy as np vec = np.array([1e-16]*(10001))

- (d) Use a _for_ loop to do the summation, (( _x_ 1 + _x_ 2) + _x_ 3) + _..._ . Does this give the right answer? Now use a _for_ loop to do the summation with the 1 as the last value in the vector instead of the first value. Right answer? If either of these don’t give the right answer, how many decimal places of accuracy does the answer have? Do the same in Python.

- (e) What do the results suggest about how R’s _sum()_ function works? Is it simply summing the numbers from left to right?

- (f) Extra credit: Figure out what R’s _sum()_ function is doing, either by finding documentation or by looking at the actual code used.

This should suggest that the _sum()_ function works in a smart way, but that if you calculate the sum manually, you need to be careful in some situations.

2

---

[Up: contents](../index.md)
