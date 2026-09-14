---
title: Questions
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/09/py_vs_R.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/09/py_vs_R.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Questions

**Source:** [`sections/09/py_vs_R.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/09/py_vs_R.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

### Main Questions

(Ideally, you will make it through all of these, although there if you run out
of time that is okay.)

1) Do Python functions behave like pass-by-value or pass-by-reference
i.e., if you pass in an object and modify it, does that affect the value of the
object in the environment from which the function was called?
Check this for a scalar, a list, and a numpy array.

2) If you copy a list, dictionary, or numpy array in Python, are the values copied
or does the new object just use the same memory as the original object?

3) How are `NA`s handled in Python lists? What about in numpy arrays?

4) Do Python functions use promises/lazy evaluation?

5) Assess whether it is inefficient to grow a list in Python, as it is in R. Consider
whether a copy is made when the object grows.

6) How does variable scoping work in Python - does it use lexical scoping and
look for variables in the environment where a function was defined?

7) Are the maximum and minimum sizes of integers and real-valued numbers the same
as they are in R?

8) Consider the relative efficiency of for loops versus vectorized calculations
for numpy arrays and see how it compares to the equivalent operation in R.

9) Can lists and numpy arrays be modified in place, without copying the object?

10) Consider whether Python allows you to have functions and variables in the
global environment that have the same names as functions/variables in packages or
in modules (e.g., a file test.py in your working directory that you can import
using 'import test'). E.g. consider math.cos and create your own 'cos' function.
How does this compare to how R finds objects?


### Additional Questions

(Work on these if you finish quickly/are curious)

11) Can you create a closure with embedded data, like we did in R?

12) Can you determine if the speed of looking up values in a dictionary varies
with the size of the dictionary (this will indicate if something like hashing is
going on or if the look up has to scan through all the elements).

13) Compare the Python debugger to R's debugger.

14) If you create classes and objects in Python's object-oriented system, what are
the similarities and differences relative to R's R6 system? There is a brief section
on object-oriented programming in Python in the lab 6 materials.

---

[← Py vs R Part 01 —](01-py-vs-r-part-01.md) · [Up: contents](index.md)
