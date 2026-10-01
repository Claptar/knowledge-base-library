---
title: "25. Comparing R and Python Semantics"
course: "Berkeley Stat 243"
chapter: 25
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 25. Comparing R and Python Semantics

## What this covers

This session is a lab, not a lecture: a list of questions to be settled by writing and running
small pieces of Python code, in groups, and comparing the result against how R behaves on the same
question. It assumes the reader already knows R's answers for each topic on the list — copying and
mutation, lazy evaluation, lexical scoping, growing a vector, vectorized versus looped arithmetic,
and how R resolves a name against a loaded package — because every question here is exactly one of
those, asked again with Python substituted for R. Nothing below settles the questions: that is the
point of the exercise, and this chapter keeps that shape rather than supplying answers the source
does not contain.

## What the questions are asking

The ten main questions and four additional ones cluster around a handful of recurring ideas from
language semantics. Naming them here is only to make the questions parseable, not to answer any of
them for Python.

**Copying, aliasing, and mutation** (questions 1, 2, 5, 9). A function is *pass-by-value* if the
callee receives an independent copy of an argument, so that changing it inside the function has no
effect on the caller's copy; it is *pass-by-reference* if the callee receives a handle to the same
underlying object, so a mutation is visible back in the caller. The same distinction applies to
copying a container directly: two names are *aliases* of one another if changing the object through
one name is visible through the other, and copying is *independent* if it is not. Growing a
container by appending to it can be cheap — if the container is extended in place — or expensive, if
each append requires allocating a new, larger backing store and copying every existing element into
it; question 5 is asking which of these Python does. Question 9 is the same distinction stated
directly: does modifying an element, or calling a method, change the object without producing a new
one at all.

**Evaluation and name resolution** (questions 4, 6, 10, 11). *Lazy evaluation* means an argument
expression is not evaluated until the point inside the function where its value is first needed,
rather than eagerly, at the moment the function is called; R implements this with objects called
promises, which is why question 4 asks specifically about promises. *Lexical scoping* means that a
free variable inside a function is looked up in the environment where the function was *defined*,
not the environment from which it happens to be *called*. A *closure* is a function that keeps
access to variables from its enclosing scope even after that scope has otherwise finished running,
so each instance of the closure can carry its own captured data — question 11 is asking whether
Python supports building one. Question 10 is about namespace resolution: when a name is defined
both in an imported module and in the caller's own top-level code, which definition a bare use of
that name resolves to, and in what order the possible namespaces are searched.

**Representation and precision** (questions 3, 7). A missing value can be represented as a genuine
hole in a container or as a sentinel value stored like any other element; question 3 asks which of
these Python lists and numpy arrays do. Numeric types can be fixed-width, with a hard ceiling past
which arithmetic overflows or wraps, or arbitrary-precision, growing to fit whatever value is
computed; question 7 asks where Python's integers and floats fall.

**Performance** (questions 8, 12). Vectorized code expresses an operation as a single call over an
entire array at once; the alternative is an explicit loop over the array's elements one at a time.
Question 8 asks how the two compare in numpy, and by extension in R. Question 12 is asking whether
dictionary lookup time is roughly independent of the dictionary's size — the signature of a hash
table — or grows with size, the signature of a linear scan.

**Tooling and object systems** (questions 13, 14). These ask for a direct comparison of Python's
debugger against R's, and of Python's class system against R's R6 system, using the object-oriented
programming material from lab 6 as the reference point for the Python side.

## Exercises

Work in groups of three (four if necessary). Everyone can take a different question, or the group
can move through them together — either way, budget about fifty minutes and expect not to finish
everything.

### Main questions

1. Do Python functions behave like pass-by-value or pass-by-reference — that is, if you pass in an
   object and modify it inside the function, does that affect the value of the object in the
   environment from which the function was called? Check this for a scalar, a list, and a numpy
   array.
2. If you copy a list, a dictionary, or a numpy array in Python, are the values copied, or does the
   new object just use the same underlying memory as the original?
3. How are missing values handled in Python lists? What about in numpy arrays?
4. Do Python functions use promises, or lazy evaluation more generally?
5. Assess whether it is inefficient to grow a list in Python, the way it is in R. Consider whether a
   copy is made when the object grows.
6. How does variable scoping work in Python — does it use lexical scoping, looking for a variable in
   the environment where the function was defined?
7. Are the maximum and minimum sizes of integers and real-valued numbers the same as they are in R?
8. Compare the relative efficiency of for-loops versus vectorized calculations on numpy arrays, and
   see how that comparison lines up with the equivalent operation in R.
9. Can lists and numpy arrays be modified in place, without copying the object?
10. Does Python allow you to have functions and variables in the global environment with the same
    names as functions or variables in a package or a module — for example, a file `test.py` in your
    working directory that you import with `import test`? Try it with `math.cos` and a function you
    write yourself called `cos`. How does this compare to how R finds objects?

### Additional questions

11. Can you create a closure with embedded data, the way we did in R?
12. Can you tell whether the speed of looking up a value in a dictionary varies with the size of the
    dictionary? (This would tell you whether something like hashing is going on, or whether the
    lookup has to scan through every element.)
13. Compare the Python debugger to R's debugger.
14. If you create classes and objects using Python's object-oriented system, what are the
    similarities and differences relative to R's R6 system? There is a short section on
    object-oriented programming in Python in the lab 6 materials.

## Sources

Both files are converted, licence CC0-1.0, from the same source Rmd:
`sections/09/py_vs_R.Rmd` in `berkeley-stat243/stat243-fall-2021`.

- Session framing and instructions: `01-py-vs-r-part-01.md`.
- The full question list, main and additional: `02-questions.md`.

The lecture referred to but did not supply an example script, `syntax.py`, and to "the lab 6
materials" for a section on Python object-oriented programming (question 14) — neither is among the
inputs for this chapter. No slide deck or transcript was supplied for this session; it is a lab
handout only, with no exposition or worked answers in the source.

---

[← 24. Problem Set 8](24-problem-set-8.md) · [Contents](index.md) · [26. Python for R Users →](26-python-for-r-users.md)
