---
title: '5. Programming paradigms: object-oriented and functional programming'
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit5-programming.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Programming paradigms: object-oriented and functional programming

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

Object-oriented and functional programming are two important approaches to programming.

Functional programming (FP) focuses on writing functions that take inputs and produce outputs. Ideally those functions don't change the state (i.e., the values) of any variables and can be treated as black boxes. Functions can be treated like other variables, such as passing functions as arguments to another function (as one does with `map` in Python).

Object-oriented programming (OOP) revolves around objects that belong to classes. The class of an object defines the fields (the data objects) holding information and  methods that can be applied to those fields. When one calls a method, it may modify the value of the fields. A statistical analogy is that an object of a class is like the realization (the object) of a random variable (the class).

One can think of functional programming as being focused on actions (or *verbs* to make an analogy with human language). One carries out a computation as a sequence of function calls. One can think of OOP as being focused on the objects (or *nouns*). One carries out a computation as a sequence of operations with the objects, using the class methods.

Many languages are multi-paradigm, containing aspects of both approaches and allowing programmers to use either approach. Both R and Python are like this, though one would generally consider R to be more functional and Python to be more object-oriented.

Let's illustrate the ideas with some numpy and list functionality.

```python
import numpy as np
x = np.array([1.2, 3.5, 4.2, 9.7])
x.shape     # field (or attribute) of the numpy array class
x.sum()     # method of the class
np.sum(x)   # equivalent numpy function
len(x)      # built-in function

---

[← myArray[2.73] # What do you think is going to happen?](07-myarray-2-73-what-do-you-think-is-going-to-happen.md) · [Up: contents](index.md) · [functional approach: apply functions sequentially →](09-functional-approach-apply-functions-sequentially.md)
