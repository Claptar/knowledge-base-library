---
title: 6. Types and data structures
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Types and data structures

**Source:** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

As we're reading data into Python or other languages, it's important to think about the data structures we'll use to store the information. The data structure we choose can affect:

- the amount of memory we need,
- how quickly we can access the information in the data structure,
- how much copying needs to be done to add information to or remove information from the data structure,
- how efficiently we can use the data in subsequent computations.

This means that what you plan to do with the data should guide what kind of structure you store the data in.

## Standard data structures in Python and R

- In Python and R, one often ends up working with dataframes, lists, and arrays/vectors/matrices/tensors.
- In Python we commonly work with data structures that are part of additional packages, in particular numpy arrays and pandas dataframes.
- Dictionaries in Python allow for easy use of key-value pairs where one can access values based on their key/label. In R one can do something similar with named vectors or named lists or (more efficiently) by using environments.
- In R, if we are not working with rectangular datasets or standard numerical objects, we often end up using lists or enhanced versions of lists, sometimes with deeply nested structures.

In Unit 5, we'll talk about *distributed* data structures that allow one to easily work with data distributed across multiple computers.

## (BACKGROUND) Other kinds of data structures

You may have heard of various other kinds of data structures, such as linked lists, trees, graphs, queues, and stacks. One of the key aspects that differentiate such data structures is how one navigates through the elements.

*Sets* are collections of elements that don't have any duplicates (like a mathematical set).

With a *linked list*, with each element (or node) has a value and a pointer (reference) to the location of the next element. (With a doubly-linked list, there is also a pointer back to the previous element.) One big advantage of this is that one can insert an element by simply modifying the pointers involved at the site of the insertion, without copying any of the other elements in the list. A big disadvantage is that to get to an element you have to navigate through the list.

![Linked list (courtesy of computersciencewiki.org)](https://raw.githubusercontent.com/berkeley-stat243/fall-2026/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/linked-list.png){fig-alt="Drawing of linked list"}


Both *trees* and *graphs* are collections of nodes (vertices) and links (edges). A tree involves a set of nodes and links to child nodes (also possibly containing information linking the child nodes to their parent nodes). With a graph, the links might not be directional, and there can be cycles.

![Tree (courtesy of computersciencewiki.org)](https://raw.githubusercontent.com/berkeley-stat243/fall-2026/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/tree.png){fig-alt="Drawing of tree"}


![Graph (courtesy of computersciencewiki.org)](https://raw.githubusercontent.com/berkeley-stat243/fall-2026/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/graph.png){fig-alt="Drawing of graph"}


A *stack* is a collection of elements that behave like a stack of lunch trays. You can only access the top element directly("last in, first out"), so the operations are that you can push a new element onto the stack or pop the top element off the stack. In fact, nested function calls behave as stacks, and the memory used in the process of evaluating the function calls is called the 'stack'.

A *queue* is like the line at a grocery store, behaving as "first in, first out".

One can use such data structures either directly or via add-on packages in Python and R, though I don't think they're all that commonly used in R. This is probably because statistical/data science/machine learning workflows often involve either 'rectangular' data (i.e., dataframe-style data) and/or mathematical computations with arrays. That said, trees and graphs are widely used.

Some related concepts that we'll discuss further in Unit 4 include:

 - types: this refers to how a given piece of information is stored and what operations can be done with the information.
 - pointers: references to other locations (addresses) in memory. One often uses pointers to avoid unnecessary copying of data.
 - hashes: hashing involves fast lookup of the value associated with a key (a label), using a hash function, which allows one to convert the key to an address. This avoids having to find the value associated with a specific key by looking through all the keys until the key of interest is found (an O(n) operation).

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

```
double y;
double x = 3.1;
y = x * 7.1;

double myfun(int x) {return (double) x;}
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

[← 5. Modules and packages](08-5-modules-and-packages.md) · [Up: contents](index.md) · [myList[2.0] # What do you think is going to happen? →](10-mylist-2-0-what-do-you-think-is-going-to-happen.md)
