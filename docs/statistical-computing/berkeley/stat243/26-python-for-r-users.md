---
title: "26. Python for R Users"
course: "Berkeley Stat 243"
chapter: 26
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 26. Python for R Users

## What this covers

This chapter is a working introduction to Python for someone who already thinks in R: it assumes
you can write R functions, loops, and vectorized code, and it uses that fluency as the anchor for
everything new. It covers how Python code is laid out, what an "object" and a "variable" are in
Python's sense, the core built-in data structures (numbers, tuples, lists, dictionaries, strings),
control flow, function definitions, a first look at classes, and the numerical/statistical stack
(NumPy, SciPy, pandas) that plays the role R's base vectors and data frames play. Throughout, the
comparison to R is the point, not an aside: several of the differences (0-based indexing, mutable
vs. immutable objects, in-place array operations) are exactly the places an R user's intuition
misfires.

## Setting up

You need Python and IPython installed, plus a handful of packages used throughout: `re`, `numpy`,
`scipy`, and `pandas`. Packages install via `pip`, or via `conda` if you're using the
Anaconda/Miniconda distribution:

```bash
## using conda
conda list
conda install numpy
conda install ipython

## using pip
pip install numpy
pip install ipython
# or, without admin rights on the machine:
pip install --user numpy
```

Work interactively rather than reading code cold. Either start an IPython shell:

```bash
ipython
```

or a Jupyter notebook:

```bash
jupyter notebook
```

(Berkeley students can also reach Jupyter notebooks through [JupyterHub on the
SCF](https://jupyter.stat.berkeley.edu) without a local install.) By default a Jupyter cell only
prints its last expression's value; to have every expression in a cell print, run once per
notebook:

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

**Python 2 vs. 3.** For years Python 2 and Python 3 coexisted, with a lot of legacy code written
against Python 2 — most visibly, `2/3` means integer division in Python 2 but true division in
Python 3. Python 2 is now being phased out; write and expect Python 3.

## Code layout: indentation is syntax

Unlike most languages, Python uses indentation itself to mark the boundaries of a code block —
function bodies, loop bodies, the branches of an `if`. The convention is one tab or four spaces,
but any indentation is legal as long as it is consistent within a block:

```python
a = 3
 a = 3  # this raises an IndentationError, at least in plain Python
```

Because indentation *is* the block structure, two pieces of code that look almost identical can do
different things:

```python
if a >= 4:
    print('a is big')
    if(a == 4):
        print('a is 4')
else:
    print('a is small')

if a >= 4:
  print('a is big')
  if(a == 4):
        print('a is 4')
  else:
        print('a is not 4')
```

In the first block the `else` pairs with the outer `if`; in the second, changed indentation, it
pairs with the inner one. This is also the practical reason cutting and pasting code into a Python
session can silently break: pasted whitespace can shift a line's indentation level.

## Objects and variables

Everything in Python is an object: it can be bound to a name and passed as a function argument, and
it typically has *attributes* (data attached to it) and *methods* (functions attached to it).

Objects split into **mutable** ones, whose contents can be changed in place — lists, dictionaries —
and **immutable** ones, which cannot — tuples, strings, sets, numbers. Objects can also be
composite: a list of dictionaries, a dictionary of lists, and so on.

As in R, a variable is not the value itself but a name bound to an object ("I am not my name, I am
the person named XXX"). A variable can be rebound to an object of a completely different type
without complaint, and how an operator behaves depends entirely on the object currently bound to
the name — `*` means numeric multiplication for a number and repetition for a string:

```python
a = 'foobar'
a
a * 4
len(a)

a = 3
a
a * 4
len(a)
```

## Modules, imports, and namespaces

Interactive exploration is for figuring things out; code you want to reuse or hand to someone else
goes in a file, and you bring it into a session (or into another file) with `import`. If a file
`mytest.py` defines a function `hello` and a variable `a`, importing it as a module keeps its
contents inside the `mytest` namespace, addressed the same way an R package's namespace is:

```python
del(a); del(hello)     # clear any existing objects with these names

import mytest           # make mytest's contents available under mytest.<name>

mytest.hello()
mytest.a

hello()                 # NameError: hello isn't in scope on its own
a
```

You can pull everything out of a module's namespace with `from mytest import *`, but think about why
that might be a bad idea before doing it routinely:

```python
from mytest import *

hello()
a
```

The risk is the same one namespaces exist to prevent: two imported modules that happen to define a
function or variable with the same name will silently collide, and whichever was imported last
wins.

Packages work the same way, and it's idiomatic to import a commonly used package under a short
alias:

```python
from math import cos
cos(0)
sin(0)      # NameError -- only cos was imported from math, not sin

import math
math.cos(0)
math.sin(0)

import numpy as np
numpy.arctan(1)
np.arctan(1)

import scipy as sp
import matplotlib.pyplot as plt
```

Separate namespaces (`math.`, `np.`) are what let two packages define a function with the same
name without conflict.

**Getting help.** `?` after an object or function prints its docstring — a string that is the first
statement in a module, function, class, or method definition, and becomes its `__doc__` attribute.
Every module and every function or class a module exports should have one:

```text
In [1]: import numpy as np

In [2]: np.ndim?
Type:        function
Definition:  np.ndim(a)
Docstring:
Return the number of dimensions of an array.

Parameters
----------
a : array_like

Returns
-------
number_of_dimensions : int

Examples
--------
>>> np.ndim([[1,2,3],[4,5,6]])
2
>>> np.ndim(1)
0
```

Typing a module or package name followed by `.` and Tab lists what's inside it — a quick way to see
what's available without leaving the documentation:

```python
math.
```
```text
math.acos       math.degrees    math.fsum       math.pi
math.acosh      math.e          math.gamma      math.pow
math.asin       math.erf        math.hypot      math.radians
...
math.cosh       math.frexp      math.modf
```

**Reading errors.** When an error occurs inside a function that itself lives in an imported module,
the *traceback* — the chain of calls that led to the error — is how you find where it actually
happened, not just where it surfaced:

```python
import days

days.print_friday_message()
```

This is the Python analogue of `traceback()` after an error in R, or setting
`options(error = recover)` beforehand.

## Data structures

### Numbers

Python has integers, floats, and complex numbers, with the usual arithmetic. Watch the
integer-vs-float division difference between Python 2 and 3:

```python
2 * 3
2 / 3      # in Python 2 this truncates; in Python 3 it doesn't

x = 1.1
type(x)
x * 2
x ** 2

(type(1), type(1.1), type(1 + 2j))
y = 1 + 2j
```

The `math` module supplies the usual numerical functions:

```python
import math
math.cos(0)
math.cos(math.pi)
```

### Tuples

A tuple is an immutable, ordered sequence of zero or more objects; functions often return them.

```python
x = 1; y = 'foo'

xy = (x, y)
type(xy)
xy = x, y          # the parentheses are optional
type(xy)

xy
xy[1]

xy[1] = 3          # error: tuples are immutable

a, b = x, y        # unpacking
a
b
```

### Lists

A list is a mutable, ordered sequence of zero or more objects — heterogeneous, like an R list, but
with different syntax, and 0-indexed rather than 1-indexed.

```python
myList = [1, 2, 'foo']
myList[0]
myList[1]
myList[1] = 2.5
myList
```

```python
dice = [1, 2, 3, 4, 5, 6]
dice.extend([7, 8])
dice.insert(3, 100)
```

Indexing goes from 0 to length minus 1, and slicing with `start:stop:step` selects a subsequence:

```python
dice = [1, 2, 3, 4, 5, 6]
dice[0]
dice[1]
dice[6]        # IndexError -- out of range

dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice[1::2]
dice[1:4:2]
dice[1::2] = dice[::2]
dice
```

### Dictionaries

A dictionary is a mutable, unordered collection of key-value pairs — the analogue of a named list
or named vector in R:

```python
students = {"Jarrod Millman": ['A', 'B+', 'A-'],
            "Thomas Kluyver": ['A-', 'A-'],
            "Stefan van der Walt": 'and now for something completely different'}
students
students.keys()
students.values()
students["Jarrod Millman"]
students["Jarrod Millman"][1]
```

## Objects, attributes, methods, and classes

Python is object-oriented: every variable is an object, an instance of some class. Objects of a
given class share the same methods and the same attribute ("member data") slots, but each instance
holds its own values in those slots. Even a plain number behaves this way — tab completion on a
value shows its methods and attributes:

```python
x = 3.0
type(x)
x.
# x.as_integer_ratio  x.hex               x.real
# x.conjugate         x.imag
# x.fromhex           x.is_integer
```

An attribute is read as `x.foo`; a method is called as `x.foo()`.

You can define your own classes. `Rectangle` below has class-level state (`dim`, `counter`, shared
across all instances) and instance-level state (`height`, `width`, `diagonal`, particular to one
instance), an initializer `__init__` run when an instance is created, a `__repr__` controlling how
an instance prints, and ordinary methods:

```python
class Rectangle(object):
    dim = 2      # class variable
    counter = 0
    def __init__(self, height, width):
        self.height = height    # instance variable
        self.width = width      # instance variable
        self.set_diagonal()
        Rectangle.counter += 1
    def __repr__(self):
        return("{0} by {1} rectangle".format(self.height, self.width))
    def area(self, verbose=False):
        if verbose:
            print('Computing the area... ')
        return(self.height * self.width)
    def set_diagonal(self):
        self.diagonal = pow(self.height**2 + self.width**2, 0.5)

x = Rectangle(10, 5)

x.dim
x.dim = 'foo'
x.dim          # only this instance's dim changed

x.area()
Rectangle.area(x)      # calling a method as an ordinary function on an instance

y = Rectangle(4, 8)
y.counter
x.counter               # shared across both instances
```

## Control flow

### If / else

Behaves as in other languages, with indentation carrying the block boundaries as described above:

```python
x = 2

if a >= 4:
    print('a is big')
    if(a == 4):
        print('a is 4')
else:
    print('a is small')

if a >= 4:
    print('a is big')
    if(a == 4):
        print('a is 4')
    else:
        print('a is not 4')
```

### For loops and list comprehensions

```python
for x in [1, 2, 3, 4]:
    print(x)

for x in [1, 2, 3, 4]:
    y = x * 2
    print(y, end=" ")

print("\n")
for x in range(30):
    print(x)
    y = x

print(y, end=" ")
```

Building a list up element by element in a loop is common enough that Python has a compact syntax
for it, **list comprehension**:

```python
y = [x for x in range(4)]

vals = [-4, 3, -1, 2.5, 7]
[x for x in vals if x > 0]      # list comprehension with a filter
```

## Functions

Arguments can be positional (always given first, in order) or named (given anywhere, by keyword),
and named arguments can carry defaults:

```python
def add(x, y=1, absol=False):
    if absol:
        return(abs(x + y))
    else:
        return(x + y)

add(3)
add(3, 5)
add(3, absol=True, y=-5)
add(y=-5, x=3)
add(y=-5, 3)      # error: a positional argument can't follow a keyword one
```

## Strings

Strings are immutable sequences of characters, and share the sequence machinery used by tuples and
lists.

**Indexing and slicing.** Indexing starts at 0 (unlike R and Fortran, but like C); negative indices
count from the end. `len` gives the length. Slicing uses `start:stop:step`:

```python
import string
string.digits
string.digits[1]
string.digits[-1]

string.digits[1:5]
string.digits[1:5:2]
string.digits[1::2]
string.digits[:5:-1]
string.digits[1:5:-1]
string.digits[-3:-7:-1]
```

**Subsequence testing:**

```python
'23' in string.digits
'25' not in string.digits
```

**String methods and dunder methods.** Tab completion again shows what's available:

```python
string1 = "my string"
string1.
```
```text
string1.capitalize  string1.islower     string1.rpartition
string1.center      string1.isspace     string1.rsplit
string1.count       string1.istitle     string1.rstrip
string1.encode      string1.join        string1.splitlines
string1.endswith    string1.ljust       string1.startswith
string1.find        string1.lstrip      string1.swapcase
string1.format      string1.partition   string1.title
string1.index       string1.replace     string1.translate
string1.isalnum     string1.rfind       string1.upper
string1.isalpha     string1.rindex      string1.zfill
string1.isdigit     string1.rjust
```

```python
string1.upper()
string1.upper?

string1 + " is your string."
"*" * 10

string1[3:]
string1[3:4]
string1[4::2]

string1[3:5] = 'ts'     # error: strings are immutable
```

Comparison operators and "dunder" (double-underscore) methods implement the operators themselves —
`__add__` backs `+`, `__lt__` backs `<`, and so on:

```python
string1 > "ab"
string1 > "zz"
string1.__
```
```text
string1.__add__           string1.__len__
string1.__class__         string1.__lt__
string1.__contains__      string1.__mod__
string1.__eq__            string1.__new__
string1.__ge__            string1.__reduce__
string1.__getattribute__  string1.__repr__
string1.__getitem__       string1.__rmod__
string1.__gt__            string1.__rmul__
string1.__hash__          string1.__str__
```

## The numerical and statistics stack: NumPy, SciPy, pandas

### NumPy arrays

Plain Python lists aren't set up for mathematical manipulation the way R vectors are. NumPy's array
is the object that plays that role, in one or several dimensions. The important difference from R:
**NumPy operations act in place** — the array itself is modified, not a copy.

```python
z = [0, 1, 2]
y = np.array(z)
y * 3

y.dtype        # the type of value stored in the array -- all elements share one type

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
x * x          # elementwise multiplication
x.dot(x)       # matrix multiplication
x.T            # transpose

np.linalg.svd(x)         # SVD
e = np.linalg.eig(x)     # eigenvalues and eigenvectors
e[0]                      # eigenvalues (not sorted largest-first)
e[1][:, 0]                # the eigenvector matching e[0][0]
```

NumPy provides the standard mathematical/statistical operations, plus indexing that supports
boolean masks and integer lists together:

```python
np.linspace(0, 1, 5)

np.random.seed(0)
x = np.random.normal(size=10)

pos = x > 0          # a boolean mask
y = x[pos]

x[[1, 3, 4]]         # index with a list of positions

x[pos] = 0
np.cos(x)
```

### SciPy

SciPy adds further numerical routines, including probability distributions:

```python
import scipy.stats as st
st.norm.cdf(1.96, 0, 1)
st.norm.cdf(1.96, 0.5, 2)
st.norm(0.5, 2).cdf(1.96)
```

### pandas

pandas provides a Python implementation of R's data frame:

```python
import pandas as pd
dat = pd.read_csv('gapminder.csv')
dat.head()

dat.columns
dat['year']
dat.year
dat[0:5]

dat.sort_values(['year', 'country'])
dat.loc[0:5, ['year', 'country']]     # R-style indexing

dat[dat.year == 1952]

ndat = dat[['pop', 'lifeExp', 'gdpPercap']]
ndat.apply(lambda col: col.max() - col.min())
```

pandas also supports the split-apply-combine pattern familiar from `dplyr` and related R packages:

```python
dat2007 = dat[dat.year == 2007].copy()
dat2007.groupby('continent', as_index=False).mean()

def stdize(vals):
    return((vals - vals.mean()) / vals.std())

dat2007['lifeExpZ'] = dat2007.groupby('continent')['lifeExp'].transform(stdize)
```

## Style

Adopting a standard coding convention is good practice. The official one is **PEP8** ("PEP" =
Python Enhancement Proposal), the "Style Guide for Python Code." Two tools help enforce it: `pep8`,
a command-line checker, and `autopep8`, which reformats code to conform automatically.

## Exercises

**Numbers.** Using the "Built-in Types" section of the official [Python Standard Library
reference](https://docs.python.org/3/library/index.html), figure out how to compute:

1. $(\lceil \frac{3}{4} \rceil \times 4)^3$
2. $\sqrt{-1}$

**Tuples.**

- Set `x = 5` and `y = 6`. Swap their values with a single line of code. (How would you do this in
  R?)
- What happens when you multiply a tuple by a number? How does this differ from the analogous
  syntax in R?
- What's the practical benefit of using immutable objects in your code?

**Lists.**

- What do you get if you multiply a list of numbers by a number? (You'll need NumPy to get
  R-like elementwise behavior.)
- What does the following tell you about copying and memory use in Python?

  ```python
  a = [1, 3, 5]
  b = a
  id(a)
  id(b)
  a[1] = 5
  ```

**For loops and list comprehension.**

- See what `[1, 2, 3] + 3` returns. Explain what happened and why.
- Use list comprehension to add a scalar to every element of a list.

**Functions.**

- Define a function that computes the square root of a number, and that optionally (if the caller
  asks) returns 0 for the square root of a negative number instead of erroring.

**NumPy / SciPy.**

- See what happens when you try to build a NumPy array from a mix of numbers and character
  strings.
- Try adding a vector to a matrix; compare the result to what happens in R.

**pandas.**

- Use `pd.merge()` to merge the per-continent mean life expectancy for 2007 back into the original
  `dat2007` data frame.

**Strings.** Using `x = 'The ant wants what all ants want.'`, and only string indexing, slicing,
methods, and subsequence testing:

1. Convert the string to all lower case (without changing `x`).
2. Count the number of occurrences of the substring `ant`.
3. Build a list of the words in `x`, with punctuation removed and everything lowercased.
4. Using only string methods on `x`, produce `'The chicken wants what all chickens want.'`.
5. Using indexing and the `+` operator, produce `'The tna wants what all ants want.'`.
6. Produce the same string as in (5), but using a string method instead.
7. What can you do with the `in` and `not in` operators? What R operator is this like, and how does
   it differ?
8. Work out whether `len(x)` involves Python explicitly counting characters.
9. Compare the time to compute the length of a long string in Python versus in R. What does that
   tell you about what's happening behind the scenes in each?

## Sources

All of this chapter comes from a single supplied document: the Python tutorial handed out in
section 06 of UC Berkeley Stat 243 (Fall 2021),
`docs/statistical-computing/berkeley/stat243/stat243-fall-2021/sections/06/python.md`, itself
adapted by Chris Paciorek from material prepared by K. Jarrod Millman. No slides, transcript, or
separate problem set were supplied for this chapter; the worked examples and exercises above are
exactly the ones in that document, reorganized and with prose added around them.

Two files the tutorial runs code against are referenced but not included in the supplied material:
a module `mytest.py` (used to demonstrate `import`) and a module `days.py` (used to demonstrate
reading a traceback). The pandas examples likewise depend on a `gapminder.csv` dataset that was not
supplied. The tutorial's own "Resources" section, listing further written references and
introductory video lectures, was left blank in the source document.

---

[← 25. Comparing R and Python Semantics](25-comparing-r-and-python-semantics.md) · [Contents](index.md) · [27. Python Fundamentals for R Users →](27-python-fundamentals-for-r-users.md)
