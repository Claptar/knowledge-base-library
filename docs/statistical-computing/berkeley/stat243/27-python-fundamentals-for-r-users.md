---
title: "27. Python Fundamentals for R Users"
course: "Berkeley Stat 243 Fall 2024"
chapter: 27
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 27. Python Fundamentals for R Users

## What this covers

This chapter is a working introduction to Python, written for students who already think in R. It
walks through Python's core object types (lists, tuples, dictionaries), control flow, functions,
the NumPy/SciPy stack for numerical work, pandas data frames, and enough of Python's class syntax
to read a small object-oriented example. Nothing here assumes prior Python; what it does assume is
R, since almost every idea below is introduced by contrast with how R does the same thing. It
comes from a lab section built as a companion notebook to a longer written introduction, and is
meant to be run interactively, one cell at a time.

## Objects, mutability, and dynamic typing

A Python list is written with square brackets and can mix types freely:

```python
myList = [1, 2, 'foo']
print("original list:", myList)
```

Indexing starts at 0, unlike R's 1-based indexing:

```python
print("First item:", myList[0])
print("Second item:", myList[1])
```

Lists are mutable — you can reassign an element in place:

```python
myList[1] = 2.5
```

A tuple looks like a list but with parentheses, and it is **immutable**: the same kind of
assignment that just worked on the list raises an error on a tuple, and the tuple is left
unchanged.

```python
myTuple = (1, 2, 'foo')
myTuple[1] = 2.5   # raises an error
```

Python variables are dynamically typed: a name is just a label that can be rebound to a value of
any type, and the type travels with the value, not the name.

```python
a = 'foobar'
print(a * 4)      # string repetition — no direct R equivalent
print(len(a))     # length of the string

a = 3
print(a * 4)      # now ordinary multiplication
print(len(a))     # error: an int has no length
```

The `a * 4` line means something different depending on what `a` currently is — string repetition
versus numeric multiplication — because Python resolves `*` by asking the object what it means,
not by looking at a declared type.

## Modules, packages, and imports

`del(a)` removes a name from the current namespace. Importing a module makes its contents available
only through the module's name — a custom script `mytest.py`, once imported with `import mytest`,
exposes `mytest.hello()` and `mytest.a`, but calling `hello()` or referring to `a` directly still
fails, because those names were never added to the current namespace. `from mytest import *`
fixes that by importing everything into the current namespace directly, so `hello()` and `a` work
unqualified afterward.

The same distinction applies to standard packages, and it is the point where Python most departs
from R's habit of loading an entire library at once:

```python
from math import cos
print(cos(0))     # works
print(sin(0))     # fails — sin was never imported

import math
print(math.cos(0), math.sin(0))   # both available, qualified by the module name
```

Importing under an alias is common and changes what name you must use to reach the package:

```python
import numpy as np
numpy.arctan(1)   # fails — the name numpy was never bound
np.arctan(1)      # works
```

Appending `?` after an object in Jupyter (e.g. `np.ndim?`) pulls up its documentation, the rough
analogue of `?` or `help()` in R. Errors surface as Python tracebacks — importing a second script,
`days.py`, and calling one of its functions is used in the lab purely to show what that traceback
looks like and how to read it.

## Numbers, tuples, and lists in more detail

Numeric literals carry their own type: `type(1)`, `type(1.1)`, and `type(1 + 2j)` give `int`,
`float`, and `complex` respectively, and functions from `math` (already imported above) work on any
of them, e.g. `math.cos(0)`, `math.cos(math.pi)`. Typing a partial name followed by tab in Jupyter
(e.g. `x.` or `math.`) lists the methods and functions available — a way of discovering the API
interactively rather than from a manual.

A tuple can also be written without parentheses, since it is the comma that creates the tuple:

```python
x = 1; y = 'foo'
xy = (x, y)
xy = x, y          # equivalent
print(xy[1])       # indexing works, like a list
```

Unpacking assigns the elements of a tuple to several names in one line:

```python
a, b = x, y
```

Lists support the same slicing syntax as tuples and strings, `start:stop:step`, and support it more
flexibly since they are mutable:

```python
dice = [1, 2, 3, 4, 5, 6]
dice.extend([7, 8])          # append several elements
dice.insert(3, 100)          # insert one element at a position

dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice[0::3]     # every third element starting from index 0
dice[1:4:2]    # index 1 up to (not including) 4, step 2
```

Indexing past the end of a list (`dice[6]` on a 6-element list) raises an error rather than
returning a missing value — there is no implicit padding. A slice can also appear on the left of an
assignment, replacing a whole run of elements at once:

```python
dice[1::2] = dice[::2]
```

## Dictionaries

A dictionary maps keys to values and is written with braces:

```python
students = {"Jarrod Millman": ['A', 'B+', 'A-'],
            "Thomas Kluyver": ['A-', 'A-'],
            "Stefan van der Wait": 'and now for something completely different.'}

students.keys()
students.values()
students["Jarrod Millman"]
students["Jarrod Millman"][1]     # value can itself be indexed further
```

As with other objects, typing `students.` followed by tab in Jupyter shows the methods a dictionary
supports.

## Control flow

Python has no braces; a block is whatever is indented one level further than the line that opens
it (`if`, `else`, `for`, `def`, ...). That makes indentation semantically meaningful, and it is easy
to attach an `else` to the wrong `if` by getting the indentation wrong:

```python
if x >= 4:
    print("a is big")
    if a == 4:
        print("a is small")
else:
    print("a is small")
```

Here the `else` lines up with the *outer* `if`, so it only ever fires when `x < 4`; the inner `if`
has no `else` at all. Indent the `else` one level further and it belongs to the inner `if` instead:

```python
if x >= 4:
    print("a is big")
    if a == 4:
        print("a is small")
    else:
        print("a is small")
```

Same text, different meaning — the lesson is to read indentation as structure, not as decoration.

`for` loops iterate directly over a sequence, with no explicit index variable needed:

```python
for x in [1, 2, 3, 4]:
    print(x)

for x in [1, 2, 3, 4]:
    y = x * 2
    print(y, end=" ")   # end=" " suppresses the newline pandas/print adds by default
```

A subtlety worth noting: the loop variable is not scoped to the loop. After

```python
for x in range(30):
    print(x)
    y = x
```

`y` (and `x`) still exist afterward, holding the value from the final iteration.

### List comprehensions

A list comprehension builds a list from a loop in one expression:

```python
y = [x for x in range(4)]
```

and can filter as it goes:

```python
vals = [-4, 3, -1, 2.5, 7]
[x for x in vals if x > 0]
```

## Functions

Functions are defined with `def`, and parameters can have default values:

```python
def add(x, y=1, absol=False):
    if absol:
        return abs(x + y)
    else:
        return x + y
```

Arguments can be supplied positionally or by keyword, and keyword arguments can be given out of
order:

```python
add(3)                    # y and absol take their defaults
add(3, 5)                 # positional
add(3, absol=True, y=5)   # mixed
add(y=-5, x=3)            # both by keyword, any order
```

But once you use a keyword argument, every argument after it must also be given by keyword —
`add(y=-5, 3)` is a syntax error, because Python cannot tell whether the trailing `3` should fill
`x` or some later parameter.

## NumPy and SciPy

A plain Python list is not a numerical array — `numpy.array` converts one into something that
supports elementwise arithmetic and carries a fixed dtype:

```python
import numpy as np
z = [0, 1, 2]
y = np.array(z)
y.dtype
```

A two-dimensional array is built from nested lists, with the element type fixed explicitly if
needed:

```python
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
x * x        # elementwise multiplication
x.dot(x)     # matrix multiplication — a different operation from *
x.T          # transpose
```

Linear algebra lives in `np.linalg`:

```python
np.linalg.svd(x)          # singular value decomposition
e = np.linalg.eig(x)      # eigen decomposition
e[0]                       # eigenvalues
e[1][:, 0]                 # first eigenvector (a column of the returned matrix)
```

`np.linspace(0, 1, 5)` builds an evenly spaced sequence. Random sampling uses `np.random`, and
setting a seed makes it reproducible:

```python
np.random.seed(0)
x = np.random.normal(size=10)
```

Boolean arrays are used to filter and to assign selectively:

```python
pos = x > 0        # a boolean array, same shape as x
y = x[pos]          # only the positive entries
x[pos] = 0           # zero out just those entries, in place
x[[1, 3, 4]]         # "fancy" indexing — select by a list of positions
```

Elementwise functions such as `np.cos(x)` apply to a whole array at once. `scipy.stats` supplies
distributions, and a distribution's parameters can be passed either at each call or once, by
constructing a frozen distribution object:

```python
import scipy.stats as st
st.norm.cdf(1.96, 0, 1)
st.norm.cdf(1.96, 0.5, 2)
st.norm(0.5, 2).cdf(1.96)     # equivalent to the line above
```

## Pandas

`pandas` provides a data-frame type built on top of NumPy. Reading a CSV and inspecting it:

```python
import pandas as pd
dat = pd.read_csv('gapminder.csv')
dat.head()
dat.columns
```

A column can be pulled out by bracket or, if its name is a valid identifier, by attribute:

```python
dat['year']
dat.year
```

Row slicing and sorting work as expected:

```python
dat[0:5]
dat.sort_values(['year', 'country'])
```

`.loc` indexes by label, and can select rows and columns together:

```python
dat.loc[0:5, ['year', 'country']]
```

Boolean filtering follows the same pattern as NumPy:

```python
dat[dat.year == 1952]
```

`.apply` runs a function over each column (or row) of a data frame:

```python
ndat = dat[['pop', 'lifeExp', 'gdpPercap']]
ndat.apply(lambda col: col.max() - col.min())
```

Filtering rows and then modifying the result should go through `.copy()` — otherwise the filtered
object is only a view onto the original, and assigning a new column to it can behave unexpectedly:

```python
dat2007 = dat[dat.year == 2007].copy()
dat2007.groupby('continent', as_index=False).mean()
```

`groupby(...).transform(...)` applies a function within each group and returns a result aligned
back to the original row order — useful for adding a per-group standardized column:

```python
def stdize(vals):
    return (vals - vals.mean()) / vals.std()

dat2007['lifeExpZ'] = dat2007.groupby('continent')['lifeExp'].transform(stdize)
```

## Classes

A class bundles data and behaviour together. `__init__` runs when an instance is created,
`__repr__` controls how an instance prints, and ordinary methods take `self` as their first
parameter:

```python
class Rectangle(object):
    dim = 2      # class variable — shared by every instance, unless overridden
    counter = 0
    def __init__(self, height, width):
        self.height = height   # instance variable
        self.width = width
        self.set_diagonal()
        Rectangle.counter += 1
    def __repr__(self):
        return "{0} by {1} rectangle".format(self.height, self.width)
    def area(self, verbose=False):
        if verbose:
            print('Computing the area... ')
        return self.height * self.width
    def set_diagonal(self):
        self.diagonal = pow(self.height**2 + self.width**2, 0.5)

x = Rectangle(10, 5)
```

`dim` is a class variable: every `Rectangle` shares it until an instance is given its own. Assigning
`x.dim = 'foo'` does not change `Rectangle.dim` for other instances — it creates an instance
attribute on `x` that shadows the class attribute for `x` alone. `counter`, by contrast, is
incremented through `Rectangle.counter` inside `__init__`, so every instance created shares and
updates the same class-level count: after creating two rectangles, both `x.counter` and `y.counter`
report the same total. Calling `x.area()` and `Rectangle.area(x)` do the same thing — the first is
shorthand for the second, with `x` supplied automatically as `self`.

## Strings

The `string` module holds some useful constants, such as `string.digits`, and strings support the
same indexing and slicing as lists and tuples, including negative indices counted from the end and
a negative step for reversal:

```python
import string
string.digits[1]        # single character
string.digits[-1]       # last character
string.digits[1:5]      # slice
string.digits[1:5:2]    # slice with step
string.digits[:5:-1]    # from the end, stepping backward
```

Strings have their own methods (`.upper()`, and many more discoverable by tab-completion),
support `+` for concatenation and `*` for repetition, and are compared lexicographically with the
ordinary comparison operators:

```python
string1 = "my string"
string1.upper()
string1 + "is your string"
"*" * 10
print(string1 > "ab")
print(string1 > "zz")
```

Like tuples, strings are immutable: you cannot assign into a slice of a string
(`string1[3:5] = 'ts'` fails). To change part of a string you build a new one by slicing and
concatenating around the part you want to replace:

```python
string1[:3] + 'ts' + string1[5:]
```

## Exercises

**Numbers**

- Compute $\left(\left\lceil \frac{3}{4} \times 4 \right\rceil\right)^3$.
- Compute $\sqrt{-1}$.

**Tuples**

- Store `x = 5` and `y = 6`. Swap their values in a single line of code. How would you do this in R?
- What happens when you multiply a tuple by a number? How is this different from the similar syntax
  in R?
- What's nice about using immutable objects?

**Lists**

- What do you get if you multiply a list of numbers by a number?
- What does the following tell you about copying and memory use in Python?

  ```python
  a = [1, 3, 5]
  b = a
  print(id(a))
  print(id(b))
  a[1] = 5
  print(id(a))
  ```

**Control flow**

- See what `[1, 2, 3] + 3` returns. Explain what happened and why.
- Use a list comprehension to add a scalar to every element of a list of scalars.

**Functions**

- Define a function that takes the square root of a number and, if requested by the user, sets the
  square root of a negative number to $0$ instead of raising an error.

**NumPy**

- See what happens if you try to create a NumPy array from a mix of numbers and character strings.
- Try to add a vector to a matrix. How does the result compare to the same operation in R?

**Pandas**

- Use `pd.merge()` to merge the continent-level mean life expectancy for 2007 back into the
  original `dat2007` data frame.

**Strings**

Using `x = 'The ant wants what all ants want.'`, and without changing `x` itself:

- Convert the string to all lower-case letters.
- Count the number of occurrences of the substring `ant`.
- Build a list of the words occurring in `x`, with punctuation removed and every word lower-cased.
- Using only string methods on `x`, produce `The chicken wants what all chickens want.`
- Using indexing and the `+` operator, produce `The tna wants what all ants want.`
- Produce the same string again, this time using a string method instead of indexing and `+`.
- What can you do with the `in` and `not in` operators? What R operator is this most like, and how
  does it differ?
- Work out how to check whether Python is explicitly counting characters when it evaluates
  `len(x)`.
- Compare the time it takes to compute the length of a long string in Python versus in R. What does
  that suggest about what each language is doing behind the scenes?

## Sources

Both notes files come from the same source notebook, `sections/06/python_intro.ipynb`, in the
`berkeley-stat243/stat243-fall-2021` repository (licensed CC0-1.0), split at the point where the
notebook moves from general objects/data structures to strings specifically:

- Objects, variables, imports, numbers, tuples, lists, dictionaries, control flow, functions,
  NumPy/SciPy, pandas, and classes: `sections/06/python_intro/01-introduction.md`.
- String indexing, slicing, and the string exercises: `sections/06/python_intro/02-strings.md`.

No slide deck or lecture transcript was supplied for this chapter; it is built entirely from the
lab notebook's code cells and inline commentary.

The notebook itself refers to material it does not contain: an accompanying HTML file with "more
details" that the notebook was written to illustrate and practice, and three data/script files used
by its exercises — `mytest.py` and `days.py` (custom scripts used in the imports section) and
`gapminder.csv` (the dataset used throughout the pandas section) — none of which were supplied
alongside the notebook.

---

[← 26. Python for R Users](26-python-for-r-users.md) · [Contents](index.md) · [28. R Practice: Structures, Functions, I/O →](28-r-practice-structures-functions-i-o.md)
