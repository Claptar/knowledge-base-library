---
title: 4. Types and data structures
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 4. Types and data structures

## Data structures

Please see the [data structures section of Unit 2](../unit2-dataTech/index.md) for some general discussion of data structures.

We'll also see more complicated data structures when we consider objects in the section on object-oriented programming.

## Types and classes

### Overview and static vs. dynamic typing

The term 'type' refers to how a given piece of information is stored and what operations can be done with the information.

'Primitive' types are the most basic types that often relate directly to how data are stored in memory or on disk (e.g., boolean, integer, numeric (real-valued, aka *double* or *floating point*), character, pointer (aka *address*, *reference*).

In compiled languages like C and C++, one has to define the type of each variable. Such languages are *statically* typed.
Interpreted (or scripting) languages such as Python and R have *dynamic* types. One can associate different types of information with a given variable name at different times and without declaring the type of the variable:

```python
x = 'hello'
print(x)
x = 7
x*3
```

In contrast in a language like C, one has to declare a variable based on its type before using it:

```c
#| eval: false
double y;
double x = 3.1;
y = x * 7.1;
```

Dynamic typing can be quite helpful from the perspective of quick implementation and avoiding tedious type definitions and problems from minor inconsistencies between types (e.g., multiplying an integer by a real-valued number).
But static typing has some critical advantages from the perspective of software development, including:

  - protecting against errors from mismatched values and unexpected user inputs, and
  - generally much faster execution because the type of a variable does not need to be checked when the code is run.

More complex types in Python (and in R) often use references (*pointers*, aka *addresses*) to the actual locations of the data. We'll see this in detail when we discuss Memory.

### Types in Python

You should be familiar with the important built-in data types in Python,
most importantly lists, tuples, and dictionaries, as well
as basic scalar types such as integers, floats, and strings.

Let's look at the type of various built-in data structures in Python and in numpy, which provides important types for numerical computing.

```python
x = 3
type(x)
x = 3.0
type(x)
x = 'abc'
type(x)
x = False
type(x)

x = [3, 3.0, 'abc']
type(x)

import numpy as np

x = np.array([3, 5, 7])  ## array of integers
type(x)
type(x[0])

x = np.random.normal(size = 3) # array of floats (aka 'doubles')
type(x[0])

x = np.random.normal(size = (3,4)) # multi-dimensional array
type(x)
```

Sometimes numpy may modify a type to make things easier for you, which often works well, but you may want to control it yourself to be sure:

```python
x = np.array([3, 5, 7.3])
x
type(x[0])

x = np.array([3.0, 5.0, 7.0]) # Force use of floats (either `3.0` or `3.`).
type(x[0])

x = np.array([3, 5, 7], dtype = 'float64')
type(x[0])
```

This can come up when working on a GPU, where the default is usually 32-bit (4-byte) numbers instead of 64-bit (8-byte) numbers.

### Composite objects

Many objects
can be *composite* (e.g., a list of dictionaries or a dictionary of lists,
tuples, and strings).

```python
mydict = {'a': 3, 'b': 7}
mylist = [3, 5, 7]

mylist[1] = mydict
mylist
mydict['a'] = mylist
```

### Mutable objects

Most objects in Python can be modified *in place* (i.e., modifying only some of the object), but tuples, strings, and sets are *immutable*:

```python
x = (3,5,7)
try:
    x[1] = 4
except Exception as error:
    print(error)

s = 'abc'
s[1]
try:
    s[1] = 'y'
except Exception as error:
    print(error)
```

### Converting between types

This also goes by the term *coercion* and *casting*.
Casting often needs to be done explicitly in compiled languages and somewhat less so in interpreted languages like Python.

We can *cast* (coerce) between different basic types:

```python
y = str(x[0])
y
y = int(x[0])
type(y)
```

Some common conversions are converting numbers that are being
interpreted as strings into actual numbers and converting between booleans and numeric values.

In some cases Python will automatically do
conversions behind the scenes in a smart way (or occasionally not so
smart way). Consider these attempts/examples of implicit coercion:

```python
x = np.array([False, True, True])
x.sum()         # What do you think is going to happen?

x = np.random.normal(size = 5)
try:
    x[3] = 'hat'    # What do you think is going to happen?
except Exception as error:
    print(error)

myList = [1, 3, 5, 9, 4, 7]
# myList[2.0]    # What do you think is going to happen?
# myList[2.73]   # What do you think is going to happen?
```

R is less strict and will do conversions in some cases that Python won't:

```r
x <- rnorm(5)
x[2.0]
x[2.73]
```

Question: What are the advantages and disadvantages of the different behaviors of Python and R?

### Dataframes

Hopefully you're also familiar with the Pandas dataframe type.

Pandas picked up the idea of dataframes from R and functionality is similar in many ways to
what you can do with R's `dplyr` package.

`dplyr` and `pandas` provide a lot of functionality for the "split-apply-combine"
framework of working with "rectangular" data. Unfortunately, using Pandas can be a bit hard to learn/remember. I suggest looking into learning [`polars`](../unit2-dataTech/index.md) as an alternative.

Often analyses are done in a stratified fashion - the same operation or
analysis is done on subsets of the data set. The subsets might be
different time points, different locations, different hospitals,
different people, etc.

The split-apply-combine framework is intended to operate in this kind of
context:
  - first one splits the dataset by one or more variables,
  - then one does something to each subset, and
  - then one combines the results.

split-apply-combine is also closely related to the famous Map-Reduce framework
underlying big data tools such as Hadoop and Spark.

It's also very similar to standard SQL queries involving filtering, grouping, and
aggregation.

### Python object protocols

There are a number of broad categories of kinds of objects: `mapping`, `number`, `sequence`, `iterator`. These are called object protocols.

All objects that fall in a given category share key characteristics. For example `sequence` objects have a notion of "next", while
`iterator` objects have a notion of "stopping".

If you implement your own class that falls into one of these categories, it should follow the relevant protocol
by providing the required methods. For example a container class that supports iteration should provide the `__iter__` and `__next__` methods.

Here we see that `tuple`s are iterable containers:

```python
mytuple = ("apple", "banana", "cherry")

for item in mytuple:
    print(item)

## We can manually create the iterator and iterate through it.
myit = iter(mytuple)
## myit = mytuple.__iter__()  ## This is equivalent to using `iter(mytuple)`.

print(next(myit))
print(next(myit))
myit.__next__()   ## This is equivalent to using `next(myit)`.
```

We've actually gotten ahead of ourselves -- how is it that `iter` seems to do the same thing as `mytuple.__iter__()`
and `next` seems to do the same thing as `myit.__next__()`? We'll discuss that in the next section when we discuss the [Python object model](07-6-object-oriented-programming-oop.md#the-python-object-model-and-dunder-methods).

```python
x = zip(['clinton', 'bush', 'obama', 'trump'], ['Dem', 'Rep', 'Dem', 'Rep'])
next(x)
next(x)
```

We can also go from an iterable object to a standard list:

```python
r = range(5)
r
list(r)
```

---

[← 3. Modules and packages](04-3-modules-and-packages.md) · [Up: contents](index.md) · [5. Programming paradigms: object-oriented and functional programming →](06-5-programming-paradigms-object-oriented-and-functional-progr.md)
