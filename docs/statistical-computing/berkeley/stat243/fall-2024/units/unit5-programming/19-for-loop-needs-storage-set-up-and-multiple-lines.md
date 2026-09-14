---
title: 'for loop: needs storage set up and multiple lines'
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# for loop: needs storage set up and multiple lines

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

results <- []
for _,subset in subsets:   # iterate over the key-value pairs (the subsets)
  results.append(analysis_function(subset))
```

Map operations are also at the heart of the famous *MapReduce* framework, used in Hadoop and Spark for big data processing.

## Function evaluation, frames, and the call stack

### Overview

When we run code, we end up calling functions inside of other function calls.
This leads to a nested series of function calls. The series of calls is the *call stack*.
The stack operates like a stack of cafeteria trays - when a
function is called, it is added to the stack (pushed) and when it
finishes, it is removed (popped).

Understanding the series of calls is important when reading error messages and debugging.
In Python, when an error occurs, the call stack is shown, which has the advantage of
giving the complete history of what led to the error and the disadvantage of producing
often very verbose output that can be hard to understand. (In contrast, in R, only the function in which
the error occurs is shown, but you can see the full call stack by invoking `traceback()`.)

What happens when an Python function is evaluated?

  - The user-provided function arguments are evaluated in the calling scope and the results are
matched to the argument names in the function definition.
  - A new frame containing a new namespace is created to store information related to the function call and placed on the stack. Assignment to the argument names is done in the namespace, including any default arguments.
  - The function is evaluated in the (new) local scope. Any look-up of variables not found in the
local scope (using the namespace that was created) is done using the lexical scoping rules to look in the series of enclosing scopes (if any exist), then in the global/module scope, and then in the built-ins scope.
  - When the function finishes, the return value is passed back to the calling scope and the frame is
taken off the stack. The namespace is removed, unless the namespace is the enclosing scope for an existing namespace.

I'm not expecting you to fully understand that previous paragraph and
all the terms in it yet. We'll see all the details as we proceed through this Unit.

### Frames and the call stack

Python keeps track of the call stack. Each function call is associated with
a frame that has a *namespace* that contains the local variables for that function call.

There are a bunch of functions that let us query what frames are on the
stack and access objects in particular frames of interest. This gives us
the ability to work with objects in the frame from which a function was
called.

We can use functions from the `traceback` package to query the call stack.

```python
#| eval: false
import traceback

def function_a():
    function_b()  # line 2 within function, line 4 overall

def function_b():
    # some comment
    # another comment
    function_c()  # line 4 within function, line 9 overall

def function_c():
    traceback.print_stack() # line 2 within, line 12 overall
    # raise RuntimeError("A fake error")

function_a()    # line 1 relative to the call, line 15 overall
```

If we run that in Python (not via rendering the qmd file directly, because the line numbering shown is strange when things go through the quarto rendering process), we see this:

```
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in function_a
  File "<stdin>", line 4, in function_b
  File "<stdin>", line 2, in function_c
```

If we run the code by putting it in a module, say `file.py` and running `python file.py`, we see this, with the line numbering relative to the overall file, but showing the same stack of function calls:

```
  File "file.py", line 15, in <module>
    function_a()    # line 1 relative to the call, line 15 overall
  File "file.py", line 4, in function_a
    function_b()  # line 2 within function, line 4 overall
  File "file.py", line 9, in function_b
    function_c()  # line 4 within function, line 9 overall
  File "file.py", line 12, in function_c
    traceback.print_stack() # line 2 within, line 12 overall
```

If we comment out the `print_stack()` call and uncomment the error, we see the same traceback information. That's exactly what is happening when you get a long series of information when Python stops with an error.


## Function inputs and outputs

### Arguments

You can see the arguments (and any default values) for a function using the help system.

Let's create an example function:

```python
def add(x, y, z=1, absol=False):
    if absol:
        return abs(x+y+z)
    else:
        return x+y+z
```

When defining a function, arguments without defaults must come first.

When using a function, there are some rules that must be followed.

First, users must provide values for arguments without defaults.

```python
add(3, 5)
add(3, 5, 7)

add(3, 5, absol=True, z=-5)

add(z=-5, x=3, y=5)

try:
    add(3)
except Exception as error:
    print(error)
```

Second, arguments can be specified by position (based on the order of the inputs)
or by name (keyword), using `name=value`. The user needs to provide
positional arguments first.

```python
#| eval: false
add(z=-5, 3, 5)  ## Can't trap `SyntaxError` with `try`

---

[← map using pandas.apply: one line, easy to understand](18-map-using-pandas-apply-one-line-easy-to-understand.md) · [Up: contents](index.md) · [SyntaxError: positional argument follows keyword argument →](20-syntaxerror-positional-argument-follows-keyword-argument.md)
