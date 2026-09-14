---
title: this should confirm what you might suspect
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md
source_file: sources/berkeley-stat243/stat243-fall-2022/labs/07/python_intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# this should confirm what you might suspect

**Source:** [`labs/07/python_intro.md`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/labs/07/python_intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

a[1] = 5
```

Dictionaries

Dictionaries are mutable, unordered collections of key-value pairs. They're like named lists or named vectors in R.

```python
students = {"Jarrod Millman": ['A', 'B+', 'A-'],
            "Thomas Kluyver": ['A-', 'A-'],
            "Stefan van der Walt": 'and now for something completely different'}
students
students.keys()
students.values()
students["Jarrod Millman"]
students["Jarrod Millman"][1]
students.
```


Control flow

-   <https://docs.python.org/3/tutorial/controlflow.html>

If-then-else

-   <https://docs.python.org/3/tutorial/controlflow.html#if-statements>

This is as expected based on your experience with other languages. As previously noted, the indentation is important.

```python
x = 2

if a>=4:
    print('a is big')
    if(a == 4):
        print('a is 4')
else:
    print('a is small')

if a>=4:
    print('a is big')
    if(a == 4):
        print('a is 4')
    else:
        print('a is not 4')
```

For-loops (and list comprehension)

-   <https://docs.python.org/3/tutorial/controlflow.html#for-statements>
-   <https://docs.python.org/3/whatsnew/2.0.html#list-comprehensions>

Here's basic use of a for loop. Once again indentation is critical, in this case for indicating where the loop ends.

```python
for x in [1,2,3,4]:
    print(x)

for x in [1,2,3,4]:
    y = x*2
    print(y, end=" ")

print("\n")
for x in range(30):
    print(x)
    y = x


print(y, end=" ")
```

Building up a list piece-by-piece is a common task, which can easily be
done in a for-loop. An approach called 'List comprehension' provides a compact syntax to
handle this task.

```python
y = [x for x in range(4)]

vals = [-4, 3, -1, 2.5, 7]
[x for x in vals if x > 0]  # list comprehension

```


**Exercises**

- See what `[1, 2, 3] + 3` returns. Try to explain what happened and why.
- Use list comprehension to perform element-wise addition of a scalar to a list of scalars.


Functions

-   <https://docs.python.org/3/tutorial/controlflow.html#defining-functions>

Here's an example that illustrates both positional arguments (always first) and named arguments.

```python
def add(x, y=1, absol=False):
    if absol:
        return(abs(x+y))
    else:
        return(x+y)

add(3)
add(3, 5)

add(3, absol=True, y=-5)

add(y=-5, x=3)
add(y=-5, 3)
```

**Exercises**

- Define a function that will take the sqrt of a number and will (if requested by the user) set the square root of a negative number to 0.


Math and Statistics

NumPy and SciPy

Standard lists in Python are not amenable to mathematical manipulation unlike standard vectors in R. Instead we generally work with numpy arrays. These arrays can be of various dimensions (i.e., vectors, matrices, multi-dimensional arrays). One important difference between R and numpy objects is that numpy performs operations *in place* - i.e. the object itself is modified and no copies are made.

```python
z = [0, 1, 2]

y = np.array(z)
y*3

y.dtype  # what type of value is stored in the array


x = np.array([[1, 2], [3, 4]], dtype=np.float64)
x*x         # element wise multiplication
x.dot(x)    # matrix multiplication
x.T         # transpose

np.linalg.svd(x)   # do an SVD

e = np.linalg.eig(x)  # find eigenvalues and vectors

e[0]  # first eigenvalue (not the largest in this case...)
e[1][:, 0] # corresponding eigenvector
```

All of the elements of the array must be of the same type.

There are a variety of numpy functions that allow us to do standard mathematical/statistical manipulations.

Here we'll use some of those functions in addition to some syntax for subsetting and vectorized calculations.

```python
np.linspace(0, 1, 5)

np.random.seed(0)
x = np.random.normal(size=10)

pos = x > 0

y = x[pos]

x[[1, 3, 4]]

x[pos] = 0

np.cos(x)
```

scipy has even more numerical routines, including working with distributions and additional linear algebra.

```python
import scipy.stats as st
st.norm.cdf(1.96, 0, 1)
st.norm.cdf(1.96, 0.5, 2)
st.norm(0.5, 2).cdf(1.96)
```

**Exercise**

- See what happens if you try to create a numpy array with a mix of numbers and character strings.
- Try to add a vector to a matrix; how does this compare to R?


Pandas

Pandas provides a Python implementation of R's dataframe capabilities. Let's see some example code.

```python
import pandas as pd
dat = pd.read_csv('gapminder.csv')
dat.head()

dat.columns
dat['year']
dat.year
dat[0:5]

dat.sort_values(['year', 'country'])

dat.loc[0:5, ['year', 'country']]  # R-style indexing

dat[dat.year == 1952]

ndat = dat[['pop','lifeExp','gdpPercap']]
ndat.apply(lambda col: col.max() - col.min())
```

Now let's see the sort of split-apply-combine functionality that is popular in dplyr and related R packages.

```python
dat2007 = dat[dat.year == 2007].copy()

dat2007.groupby('continent', as_index=False).mean()

def stdize(vals):
    return((vals - vals.mean()) / vals.std())

dat2007['lifeExpZ'] = dat2007.groupby('continent')['lifeExp'].transform(stdize)
```

**Exercise**

- Use *pd.merge()* to merge the continent means for life expectancy for 2007 back into the original *dat2007* dataFrame.


Additional topics

Style

Adopting standard coding conventions is good practice.

-   <https://www.python.org/dev/peps/pep-0008/>
-   <https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style>
-   <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>
-   <http://matplotlib.org/devel/coding_guide.html>

The first link above is the official "Style Guide for Python Code",
usually referred to as PEP8 (PEP is an acronym for Python Enhancement
Proposal). There are a couple of potentially helpful tools for helping
you conform to the standard. The
[pep8](https://pypi.python.org/pypi/pep8) package that provides a
commandline tool to check your code against some of the PEP8 standard
conventions. Similarly,
[autopep8](https://pypi.python.org/pypi/autopep8) provides a tool to
automatically format your code so that it conforms to the PEP8
standards. I have used both a little and they seem to work fairly well.

Classes

-   <https://docs.python.org/3/tutorial/classes.html>

We've already seen a bunch of object-oriented behavior. Here we'll see how to make our own classes and objects that are instances (realizations) of a class.

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

x.dim
x.dim = 'foo'
x.dim # hmmm

x.area()
Rectangle.area(x)

y = Rectangle(4, 8)
y.counter
x.counter
```

Strings

Strings are immutable sequences of (zero or more) characters.

**Sequences**

Unlike numbers, Python strings are container objects. Specifically, it
is a sequence. Python has several sequence types including strings,
tuples, and lists. Sequence types share some common functionality, which
we can demonstrate with strings.

**Indexing**

To see how indexing works in Python let’s use the
string containing the digits 0 through 9.

```python
import string
string.digits
string.digits[1]
string.digits[-1]
```

Note that indexing starts at 0 (unlike R and Fortran, but like C).
Also negative integers index starting from the end of the sequence.
You can find the length of a sequence using the *len* function.

**Slicing**

Slicing allows you to select a subset of a string (or
any sequence) by specifying start and stop indices as well as a
step, which you specify using the `start:stop:step` notation inside
of square braces.

```python
string.digits[1:5]
string.digits[1:5:2]
string.digits[1::2]
string.digits[:5:-1]
string.digits[1:5:-1]
string.digits[-3:-7:-1]
```

**Subsequence testing**

```python
'23' in string.digits
'25' not in string.digits
```

**String methods**

```python
string1 = "my string"
string1.
```

```
string1.capitalize  string1.islower     string1.rpartition
string1.center      string1.isspace     string1.rsplit
string1.count       string1.istitle     string1.rstrip
string1.decode      string1.isupper     string1.split
string1.encode      string1.join        string1.splitlines
string1.endswith    string1.ljust       string1.startswith
string1.expandtabs  string1.lower       string1.strip
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
"*"*10

string1[3:]
string1[3:4]
string1[4::2]

string1[3:5] = 'ts'
```

```python
string1 > "ab"
string1 > "zz"
string1.__
```

```
string1.__add__           string1.__len__
string1.__class__         string1.__lt__
string1.__contains__      string1.__mod__
string1.__delattr__       string1.__mul__
string1.__doc__           string1.__ne__
string1.__eq__            string1.__new__
string1.__format__        string1.__reduce__
string1.__ge__            string1.__reduce_ex__
string1.__getattribute__  string1.__repr__
string1.__getitem__       string1.__rmod__
string1.__getnewargs__    string1.__rmul__
string1.__getslice__      string1.__setattr__
string1.__gt__            string1.__sizeof__
string1.__hash__          string1.__str__
string1.__init__          string1.__subclasshook__
```

**Exercises**

- Using this string: `x = 'The ant wants what all ants want.'`, solve the following string manipulation problems using string indexing, slicing, methods, and subsequence testing:
    1.  Convert the string to all lower case letters (don’t change x).
    2.  Count the number of occurrences of the substring `ant`.
    3.  Create a list of the words occurring in `x`. Make sure to remove
    punctuation and convert all words to lowercase.
    4.  Using only string methods on `x`, create the following string:
    `The chicken wants what all chickens want.`
    5.  Using indexing and the `+` operator, create the following string:
    `The tna wants what all ants want.`
    6.  Do the same thing except using a string method instead.
- What can you do with the *in* and *not in* operators?  What R operator is this like and how is it different?
- Figure out what code you could run to figure out if Python is explicitly counting the number of characters when it does `len(x)`?
- Compare the time for computing the length of a (long) string in Python and R. What can you infer about what is happening behind the scenes?


A Note on the Contents

This content was adapted by Chris Paciorek from [material prepared by K. Jarrod
Millman](http://www.jarrodmillman.com/capstone/bootcamp/standard.html) and is
licensed under the [CC BY-NC-SA 4.0
license](http://creativecommons.org/licenses/by-nc-sa/4.0/).

---

[← x.fromhex x.isinteger](07-x-fromhex-x-isinteger.md) · [Up: contents](index.md)
