---
title: or to install within your home directory if you do not have admin control of
  the computer
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/07/python.md
source_file: sources/berkeley-stat243/stat243-fall-2019/section/07/python.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# or to install within your home directory if you do not have admin control of the computer

**Source:** [`section/07/python.md`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/07/python.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

pip install --user numpy

```

For additional help with installation, please see the [IPython installation page](http://ipython.org/install.html).


Resources
---------------

Useful written references and tutorials:

-   <https://docs.python.org/3/index.html>
-   <https://docs.python.org/3/library/index.html>
-   <https://scipy-lectures.github.io/>

Some introductory video lectures:

-   <https://www.youtube.com/watch?v=a_Z_6brm9ZQ>

While working through this tutorial, you should type the example code
snippets at an interactive Python terminal. I recommend using either the
IPython shell or a Jupyter IPython notebook. To start an IPython shell, type
the following at a bash prompt:

``` {.sourceCode .bash}
ipython
```

To start an Jupyter IPython notebook, type this:

``` {.sourceCode .bash}
jupyter notebook
```

A notebook should open in your browser.

Alternatively you can access Jupyter notebooks through a service called [Jupyterhub on the SCF](https://jupyter.stat.berkeley.edu).

Side note: to have all output (not just the last result) printed in the Jupyter notebook, you can run this in a cell in your notebook.

```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```


Python 2 vs. 3
--------------------------

Python 3 is the current version of Python. For many years the old version (Python 2) has co-existed with Python 3 and Python 2 has been used by many people despite the existence of Python 3. Python 2 is now being phased out.

Introduction
===============

Formatting Python code
-------------------------

Unlike most languages, in Python indentation determines code blocks, including functions, loops, and if-else statements.

The standard is one tab or 4 spaces, but you can use other spacing if it's consistent within a block of code.


``` {.sourceCode .python}
a = 3
 a = 3  # this will cause an IndentationError, at least in Python itself, if not IPython
```

Note that because indentation determines the beginning and end of code blocks, the following two pieces of code do different things.

``` {.sourceCode .python}
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

The importance of indentation can cause problems when cutting and pasting code into a Python session.

Objects
-------

Everything is an object in Python. Roughly, this means that it can be
tagged with a variable (i.e., given a name) and passed as an argument to a function. Often it
means that everything has *attributes* and *methods*.

Certain objects in Python are mutable (e.g., lists, dictionaries), while
other objects are immutable (e.g., tuples, strings, sets). Mutable means one can change parts of the object.

Many objects can be composite (e.g., a list of dictionaries or a dictionary of lists,
tuples, and strings).

Here's a list in Python. It's similar to a list in R in that it can store heterogeneous information, but the syntax is a bit different.

Also note that indexing in Python starts at 0 not at 1.

``` {.sourceCode .python}
myList = [1, 2, 'foo']
myList[0]
myList[1]
myList[1] = 2.5
myList
```

Here's a tuple in Python. What's different compared to the list?


``` {.sourceCode .python}
myTuple = (1, 2, 'foo')
myTuple[1] = 2.5
myTuple
```

Variables
---------

As in R and other interpreted languages, variables are not their values in Python (think "I am not my name, I am
the person named XXX"). You can think of variables as tags on objects.
In particular, variables can point to (be bound to) an object of one type and then
reassigned to an object of another type without error.

``` {.sourceCode .python}
a = 'foobar'
a
a * 4
len(a)

a = 3
a
a*4
len(a)
```

Modules, files, packages, import
--------------------------------

While you will often explore things from an interactive Python prompt,
you will save your code in files for reuse as well as to document what
you’ve done. You can use Python code saved in a plain text file from a
Python prompt or other files by importing it. Typically, this is done at
the top of a file (if you are working at a prompt, you just need to
import it before you want to use the functionality).

Note that the use of `mytest.` is similar to our discussion of package
namespaces in R.

``` {.sourceCode .bash}
cat mytest.py  # special IPython functionality to call the operating system
```

``` {.sourceCode .python}
del(a); del(hello)   # delete any existing objects

import mytest          # make available objects/functions in mytest.py

mytest.hello()         # access using object-oriented style syntax
mytest.a

hello()
a
```

We can import everything in the test.py file if we want. Why
might this not be a great idea?

``` {.sourceCode .python}
from mytest import *

hello()
a
```


As in R, you can also load in additional supporting packages for extra functionality.
In contrast to R, a lot of basic functionality is provided in supporting packages
that need to be loaded before you can use it.

Here are some examples of importing Python packages and using functionality from them:

``` {.sourceCode .python}
from math import cos
cos(0)
sin(0)    # why doesn't this work?
import math
math.cos(0)
math.sin(0)
import numpy as np
numpy.arctan(1)
np.arctan(1)
import scipy as sp
import matplotlib.pyplot as plt
```

Note as seen above for numpy and scipy, it's common to import a package but give it a
shortened name, 'np' and 'sp' in this case.

The different packages have different namespaces, which helps to avoid problems with
different packages using the same names for different functions.


Documentation and getting help
-------------------------------

We can get help like this.

``` {.sourceCode .python}
In [1]: import numpy as np

In [2]: np.ndim?
Type:        function
String form: <function ndim at 0x7fcabd864938>
File:        /usr/lib64/python2.7/site-packages/numpy/core/fromnumeric.py
Definition:  np.ndim(a)
Docstring:
Return the number of dimensions of an array.

Parameters
----------
a : array_like
    Input array.  If it is not already an ndarray, a conversion is
    attempted.

Returns
-------
number_of_dimensions : int
    The number of dimensions in `a`.  Scalars are zero-dimensional.

See Also
--------
ndarray.ndim : equivalent method
shape : dimensions of array
ndarray.shape : dimensions of array

Examples
--------
>>> np.ndim([[1,2,3],[4,5,6]])
2
>>> np.ndim(np.array([[1,2,3],[4,5,6]]))
2
>>> np.ndim(1)
0
```

Docstrings are an important part of Python. A docstring is a character string that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object. All modules (e.g., test.py is a module) should normally have docstrings, and all functions and classes exported by a module should also have docstrings.


Decoding error messages
--------------------------

Run the following code and try to tease out where the error is. The tricky part is that the error occurs within a function where the function comes from a module (separate code file).

``` {.sourceCode .python}
import days

days.print_friday_message()
```

The list of function calls that led to the error is called a *traceback*.  (Recall that in R you can get similar output using `traceback()` after an error or setting `options(error = recover)` before an error.)

Data Structures
===============

Python has a number of basic data structure types that are widely used. There are both similarities and differences from basic data structures in R.

-   <https://docs.python.org/3/library/stdtypes.html>
-   <https://docs.python.org/3/tutorial/datastructures.html>
-   <https://docs.python.org/3/reference/datamodel.html>

Numbers
-------

Python has integers, floats, and complex numbers with the usual
operations.

``` {.sourceCode .python}
2*3
2/3

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [be careful - if you try 2/3 in Python 2, you'll get different behavior. →](03-be-careful---if-you-try-2-3-in-python-2-you-ll-get-different.md)
