---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/06/python_intro.ipynb
licence: CC0-1.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sections/06/python_intro.ipynb`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/06/python_intro.ipynb) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## Section 7: python practice notebook

In this section we are going through an introduction to python.  The .html file has more details but this notebook will serve as a place to illustrate the code from the html file and do the exercises

Note, to run the code chunks the keyboard shortcut is Shift + Enter.  For a list of useful keyboard shortcuts in jupyter notebook you can go to this [link](https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330)

### Objects
First, we create a list and print it out

```python
myList = [1, 2, 'foo']
print("original list:", myList)
```

Note that the indexing in python starts at 0

```python
print("First item:", myList[0])
print("Second item:", myList[1])
```

You can also update parts of the list

```python
myList[1] = 2.5
myList
```

However, you cannot do that with tuples

```python
myTuple = (1, 2, 'foo')
print("original tuple:", myTuple)

# try to update the tuple
myTuple[1] = 2.5
```

```python
# the tuple remains the same
print("new tuple:", myTuple)
```

### Variables

```python
a = 'foobar'
print("original a:", a)
print("different than R:", a * 4)
print("length of a:", len(a))
```

```python
a = 3
print("original a:", a)
print("what we expect, but different than above:", a * 4)
# produces an error
print("length of a:", len(a))
```

### Modules, files, packages, import

```python
# deleting a
del(a)
```

```python
# mytest.py is a python script in the sections/07 folder
import mytest
```

```python
mytest.hello()
```

```python
mytest.a
```

```python
# this will not work
hello()
```

```python
# or this
a
```

```python
from mytest import *

# now they do
hello()
a
```

Also import Python packages, similar to loading an R library, except you can choose which methods to import.

```python
from math import cos
print("Can compute cos now:", cos(0))
print("Can't compute sin:", sin(0))
```

```python
# import the whole package and we can
import math
print("Can compute cos:", math.cos(0), "and sin:", math.sin(0))
```

```python
# importing numpy as np
import numpy as np

# this will not work because we imported as np
numpy.arctan(1)
```

```python
# this is how to use numpy
np.arctan(1)
```

See documentation

```python
np.ndim?
```

### Decoding error messages
days.py is another python script that is included in the sections/07 folder.  This will show you how error messages look in python.

```python
import days
days.print_friday_message()
```

### Data structures

#### Numbers

```python
print(2 * 3)
print(2 / 3)
```

```python
x = 1.1
type(x)
```

```python
print("multiplication:", x * 2)
print("exponentiation:", x ** 2)
```

```python
(type(1), type(1.1), type(1 + 2j))
```

```python
# trying various functions from math package we imported earlier
(math.cos(0), math.cos(math.pi), math.cos(x))
```

In the empty chunk below try typing math. and then a tab to see all of the functions that come with the math package.

#### Exercises
Compute the follow things in the empty chunks below
- $\left(\lceil \frac{3}{4} \times 4 \rceil\right)^3$

- $\sqrt(-1)$

### Objects

```python
x = 3.0
type(x)
```

Try typing x. followed by a tab to see the methods that are available for this float

#### Tuples

```python
x = 1; y = 'foo'
# define the tuple
xy = (x, y)
type(xy)
```

```python
# another way to do it
xy = x, y
type(xy)
```

```python
print("full tuple:", xy)
print("indexing tuple:", xy[1])
```

```python
# recall tuples are immutable
xy[1] = 3
```

```python
a, b = x, y
print(a)
print(b)
type(a)
```

#### Exercises
- Store x = 5 and y = 6.  Swap their values in a single line of code.  (How would you do this in R?)

```python
x = 5
y = 6
y, x = x, y
print(x, y)
```

- What happens when you multiple a tuple by a number? How is this different than similar syntax in R?

- What's nice about using immutable objects?

### Lists

```python
dice = [1, 2, 3, 4, 5, 6]
print("original list:", dice)

# extend
dice.extend([7, 8])
print("extended list:", dice)

# insert
dice.insert(3, 100)
print("inserted list:", dice)
```

```python
dice.
```

Indexing a list

```python
dice = [1, 2, 3, 4, 5, 6]
print("first entry", dice[0])
print("second entry", dice[1])
```

The 6th index does not exist

```python
dice[6]
```

Using sequencing

```python
dice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dice[0::3]
```

```python
dice[1:4:2]
```

```python
dice[1::2] = dice[::2]
dice
```

#### Exercises
- What do you get if you multiply a list of numbers by a number?

- What does the following tell you about copying and memory use in Python?

```python
a = [1, 3, 5]
b = a
print("address of a:", id(a))
print("address of a:", id(b))

# update a
a[1] = 5
print("address of updated a:", id(a))
```

### Dictionaries

```python
students = {"Jarrod Millman": ['A', 'B+', 'A-'],
            "Thomas Kluyver": ['A-', 'A-'],
            "Stefan van der Wait": 'and now for something completely different.'
           }
students
```

```python
students.keys()
```

```python
students.values()
```

```python
students["Jarrod Millman"]
```

```python
students["Jarrod Millman"][1]
```

Try typing students. followed by a tab to see what methods are available for dictionaries

```python
students.
```

### Control flow

```python
x = 2
if(x >= 4):
    print("a is big")
    if(a == 4):
        print("a is small")
else:
    print("a is small")
```

```python
if(x >= 4):
    print("a is big")
    if(a == 4):
        print("a is small")
    else:
        print("a is small")
```

#### For loops and list comprehension

```python
for x in [1, 2, 3, 4]:
    print(x)
```

```python
for x in [1, 2, 3, 4]:
    y = x * 2
    print(y, end = " ")
```

```python
for x in range(30):
    print(x)
    y = x
```

```python
print(y)
```

```python
y = [x for x in range(4)]
y
```

List comprehension

```python
vals = [-4, 3, -1, 2.5, 7]
[x for x in vals if x > 0]
```

#### Exercises
- See what [1, 2, 3] + 3 returns. Try to explain what happened and why.

- Use list comprehension to perform element-wise addition of a scalar to a list of scalars

### Functions

```python
def add(x, y = 1, absol = False):
    if absol:
        return(abs(x + y))
    else:
        return(x + y)
```

```python
add(3)
```

```python
add(3, 5)
```

```python
add(3, absol = True, y = 5)
```

```python
add(y = -5, x = 3)
```

```python
add(y = -5, 3)
```

#### Excercise
- Define a function that will take the square root of a number of will (if requested by the user) set the square root of a negative number to 0.

### Math and statistics: NumPy and SciPy

```python
z = [0, 1, 2]
```

```python
y = np.array(z)
y
```

```python
y.dtype
```

```python
x = np.array([[1, 2], [3, 4]], dtype = np.float64)
# element-wise multiplication
x * x
```

```python
# matrix multiplication
x.dot(x)
```

```python
# transpose
x.T
```

```python
# SVD
np.linalg.svd(x)
```

```python
e = np.linalg.eig(x)
e[0]
```

```python
e[1][:, 0]
```

Creating a sequence in numpy

```python
np.linspace(0, 1, 5)
```

Randomly sample from normal distribution

```python
np.random.seed(0)
x = np.random.normal(size = 10)
```

```python
pos = x > 0
pos
```

```python
y = x[pos]
y
```

```python
x[[1, 3, 4]]
```

```python
x[pos] = 0
```

```python
np.cos(x)
```

Some scipy routines

```python
import scipy.stats as st
print(st.norm.cdf(1.96, 0, 1))
print(st.norm.cdf(1.96, 0.5, 2))
print(st.norm(0.5, 2).cdf(1.96))
```

#### Excercise
- See what happens if you try to create a numpy array with a mix of numbers and character strings.

- Try to add a vector to a matrix; how does this compare to R?

### Pandas

```python
import pandas as pd
dat = pd.read_csv('gapminder.csv')
dat.head()
```

```python
dat.columns
```

```python
dat['year']
```

```python
dat.year
```

```python
dat[0:5]
```

```python
dat.sort_values(['year', 'country'])
```

```python
dat.loc[0:5, ['year', 'country']]
```

```python
dat[dat.year == 1952]
```

```python
ndat = dat[['pop','lifeExp','gdpPercap']]
ndat.apply(lambda col: col.max() - col.min())
```

```python
dat2007 = dat[dat.year == 2007].copy()
dat2007.groupby('continent', as_index=False).mean()
```

```python
def stdize(vals):
    return((vals - vals.mean()) / vals.std())

dat2007['lifeExpZ'] = dat2007.groupby('continent')['lifeExp'].transform(stdize)
dat2007
```

#### Exercise
- Use *pd.merge()* to merge the continent means for life expectancy for 2007 back into the original dat2007 dataFrame.

### Classes

```python
class Rectangle(object):
    dim = 2  # class variable
    counter = 0
    def __init__(self, height, width):
        self.height = height  # instance variable
        self.width = width    # instance variable
        self.set_diagonal()
        Rectangle.counter += 1
    def __repr__(self):
        return("{0} by {1} rectangle".format(self.height, self.width))
    def area(self, verbose = False):
        if verbose:
            print('Computing the area... ')
        return(self.height*self.width)
    def set_diagonal(self):
        self.diagonal = pow(self.height**2 + self.width**2, 0.5)

x = Rectangle(10, 5)
x
```

```python
print(x.dim)
x.dim = 'foo'
print(x.dim) # hmmm
```

```python
x.area()
```

```python
Rectangle.area(x)
```

```python
y = Rectangle(4, 8)
print(y.counter)
print(x.counter)
```

---

[Up: contents](index.md) · [Strings →](02-strings.md)
