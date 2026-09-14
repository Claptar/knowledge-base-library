---
title: 4. Types and data structures
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Types and data structures

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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
#| error: true
x = 'hello'
print(x)
x*3
x = 7
x*3
x = {'mykey': 7}
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
  - generally much faster execution because the type of a variable does not need to be checked (and the location of the value found) when the code is run.

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

---

[← 3. Modules and packages](04-3-modules-and-packages.md) · [Up: contents](index.md) · [myList[2.0] # What do you think is going to happen? →](06-mylist-2-0-what-do-you-think-is-going-to-happen.md)
