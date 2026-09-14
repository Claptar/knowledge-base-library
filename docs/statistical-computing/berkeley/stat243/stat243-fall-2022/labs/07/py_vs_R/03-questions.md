---
title: Questions
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/py_vs_R.md
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/07/py_vs_R.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Questions

**Source:** [`labs/07/py_vs_R.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/py_vs_R.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

### Main Questions

!!! tip "Tip"
Ideally, you will make it through all of these, although if you run out of time
that is okay.

:::

1. Do Python functions behave like pass-by-value or pass-by-reference? In other
words, if you pass in an object and modify it, does that affect the value of the
object in the environment from which the function was called? Check this for a
scalar, a list, and a `numpy` array.

1. If you copy a list, dictionary, or `numpy` array in Python, are the values
copied or does the new object just use the same memory as the original object?

1. How are `NA`s handled in Python lists? What about in `numpy` arrays?

1. Do Python functions use promises/lazy evaluation?

1. How does variable scoping work in Python - does it use lexical scoping and
look for variables in the environment where a function was defined?

1. Consider the relative efficiency of `for` loops versus vectorized
calculations for `numpy` arrays and see how it compares to the equivalent
operation in R.

1. Can lists and `numpy` arrays be modified in place, without copying the
   object?

1. Consider whether Python allows you to have functions and variables in the
global environment that have the same names as functions/variables in packages
or in modules (e.g., make a file `test.py` in your working directory that you
can import using `import test`). Consider `math.cos` and create your own `cos`
function. How does this compare to how R finds objects?


### Additional Questions

!!! tip "Tip"
Work on these if you finish quickly/are curious

:::

1. Can you create a closure with embedded data, like we did in R?

1. Can you determine if the speed of looking up values in a dictionary varies
with the size of the dictionary (this will indicate if something like hashing is
going on or if the look up has to scan through all the elements).

1. Compare the Python debugger to R's debugger.

1. If you create classes and objects in Python's object-oriented system, what are
the similarities and differences relative to R's R6 system? There is a brief section
on object-oriented programming in Python in the lab 6 materials.

---

[← Py vs R Part 02 —](02-py-vs-r-part-02.md) · [Up: contents](index.md)
