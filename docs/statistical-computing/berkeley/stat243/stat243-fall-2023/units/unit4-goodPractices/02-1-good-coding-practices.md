---
title: 1. Good coding practices
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit4-goodPractices.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit4-goodPractices.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Good coding practices

**Source:** [`units/unit4-goodPractices.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit4-goodPractices.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

Some of these tips apply more to software development and some more to
analyses done for specific projects; hopefully it will be clear in most
cases.

## Editors

Use an editor that supports the language you are using (e.g., *Atom*, *Emacs*/*Aquamacs*, *Sublime*, *vim*, *VSCode*, *TextMate*, *WinEdt*, or the built-in editor in *RStudio* [you can use Python from within RStudio]). Some advantages of this can include:

  1. helpful color coding of different types of syntax,
  2. automatic indentation and spacing,
  3. parenthesis matching,
  4. line numbering (good for finding bugs), and
  5. code can often be run (or compiled) and debugged from within the editor.

See the problem set submission how-to document for more information about editors that interact nicely with Quarto documents.

## Coding syntax

The PEP 8 style guide is your go-to reference for Python style.
I've highlighted some details here as well as included some general
suggestions of my own.

- Header information: put metainfo on the code into the first few
    lines of the file as comments. Include who, when, what, how the code
    fits within a larger program (if appropriate), possibly the versions
    of Python and key packages that you used.
- Write docstrings for public modules, classes, functions, and methods.
    For non-public items, a comment after the `def` line is sufficient
    to describe the purpose of the item.
- Indentation: Python is strict about indentation of course, which
    helps to enforce clear indentation more than in other languages.
    This helps you and others to read and understand the code and can
    help in detecting errors in your code because it can expose lack of
    symmetry.
    - use 4 spaces per indentation level (avoid tabs if possible).
- Whitespace: use it in a variety of places. Some places where it is good to have it
    are
    - around operators (assignment and arithmetic);
    - between function arguments;
    - between list/tuple elements; and
    - between matrix/array indices.
- Use blank lines to separate blocks of code with comments to say what
    the block does.
- Use whitespaces or parentheses for clarity even if not needed for order of
    operations. For example, `a/y*x` will work but is not easy to read
    and you can easily induce a bug if you forget the order of ops. Instead,
    use `a/y * x`.
- Avoid code lines longer than 79 characters and comment/docstring lines
    longer than 72 characters.
- Comments: add lots of comments (but don't belabor the
    obvious, such as `x = x + 1  # increment x`).
    - Remember that in a few months, you may not follow your own
    code any better than a stranger.
    - Some key things to document: (1)
      summarizing a block of code, (2) explaining a very complicated piece
      of code - recall our complicated regular expressions, and (3) explaining
      arbitrary constant values.
    - Comments should generally be complete sentences.
- You can use parentheses to group operations such that they can be split up into lines
  and easily commented, e.g.,
  ```python
  #| eval: false
  newdf = (
          pd.read_csv('file.csv')
          .rename(columns = {'STATE': 'us_state'})  # adjust column names
          .dropna()                                 # remove some rows
          )
  ```
- For software development, break code into separate files
    (2000-3000 lines per file) with meaningful file names and related
    functions grouped within a file.
- Being consistent about the naming style for objects and functions is hard, but try to be consistent. PEP8 suggests:
    - Class names should be UpperCamelCase.
    - Function, method, and variable names should be snake_case, e.g., `number_of_its` or `n_its`.
    - Non-public methods and variables should have a leading underscore.
- Try to have the names be informative without being overly long.
- Don't overwrite names of objects/functions that already exist in Python. E.g., don't use `len`. That said, the namespace system helps with the unavoidable cases where there are name conflicts.
- Use active names for functions (e.g., `calc_loglik`, `calc_log_lik`
    rather than `loglik` or `loglik_calc`). The idea is that a function
    in a programming language is like a verb in regular language (a
    function *does* something), so use a verb to name it.
- Learn from others' code

This semester, someone will be reading your code - the GSI and and me when we
look at your assignments. So to help us in understanding your code and
develop good habits, put these ideas into practice in your assignments.

While not Python examples, the files [goodCode.R](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/goodCode.R) and [badCode.R](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/badCode.R) in the `units` directory of the
class repository provide examples of code written such that it does and
does not conform to the general ideas listed above (leaving aside the different syntax of Python and R).


## Coding style

This is particularly focused on software development, but some of the
ideas are useful for data analysis as well.

- Break down tasks into core units
- Write reusable code for core functionality and keep a single copy of
    the code (using version control or at least with a reasonable backup strategy) so you
    only need to make changes to a piece of code in one place
- Smaller functions are easier to debug, easier to understand, and can
    be combined in a modular fashion (like the UNIX utilities)
- Write functions that take data as an argument and not lines of code
    that operate on specific data objects. Why? Functions allow us to
    reuse blocks of code easily for later use and for recreating an
    analysis (reproducible research). It's more transparent than
    sourcing a file of code because the inputs and outputs are specified
    formally, so you don't have to read through the code to figure out
    what it does.
- Functions should:
    - be modular (having a single task);
    - have meaningful name; and
    - have a doc string describing their purpose, inputs and outputs.
- Write tests for each function (i.e., unit tests)
- Don't hard code numbers - use variables (e.g., number of iterations,
    parameter values in simulations), even if you don't expect to change
    the value, as this makes the code more readable. For example, the speed of light is a constant in a scientific sense, but best to make it a variable in code: `speed_of_light = 3e8`
- Use lists or tuples to keep disparate parts of related data together
- Practice defensive programming (see also the discussion below on assertions)
    - check function inputs and warn users if the code will do something they might not expect or makes particular choices;
    - check inputs to *if*:
        - Note that in Python, an expression used as the condition of an `if` will be equivalent to `True` unless it is one of `False`, `0`, `None`, or an empty list/tuple/string.
    - provide reasonable default arguments;
    - document the range of valid inputs;
    - check that the output produced is valid; and
    - stop execution based on checks and give an informative error message.
- Try to avoid system-dependent code that only runs on a specific
    version of an OS or specific OS
- Learn from others' code
- Consider rewriting your code once you know all the settings and
    conditions; often analyses and projects meander as we do our work
    and the initial plan for the code no longer makes sense and the code
    is no longer designed specifically for the job being done.

## Assertions, exceptions and testing

Assertions, exceptions and testing are critically important for writing robust
code that is less likely to contain bugs.

### Exceptions

You've probably already seen exceptions in action whenever you've done something
in Python that causes an error to occur and an error message to be printed.
Syntax errors are different from exceptions in that exceptions occur
when the syntax is correct but the execution of the code results in some sort of error.

Exceptions can be a valuable tool for making your code handle different modes of failure (missing file, URL unreachable, permission denied, invalid inputs, etc.). You use them when you are writing code that is supposed to perform a task (e.g., a function that does something with an input file) to indicate that the task failed and the reason for that failure (e.g., the file was not there in the first place). In such case, you want your code to raise an exception and make the error message informative as possible, typically by handling the exception thrown by another function you call and augmenting the message. Another possibility is that your code detects a situation where you need to throw an exception (e.g., an invalid input to a function).

The other side of the coin happens when you want to write a piece of code that handles failure in a specific way, instead of simply giving up. For example, if you are writing a script that reads and downloads hundreds of URLs, you don't want your program to stop when any of them fails to respond (or do you?). You might want to continue with the rest of the URLs, and write out the failed URLs in a secondary output file.

#### Using `try-except` to continue execution

If you want some code to continue running even when it encounters an error, you can use `try-except`.
This would often be done in code where you were running some workflow rather than in functions
that you write for general purpose use (e.g., code in a package you are writing).

Suppose we have a loop and we want to run all the iterations even if the code for some iterations fail.
We can embed the code that might fail in a `try` block and then in the `except` block, run code
that will handle the situation when the error occurs.

```python
#| eval: false
for i in range(n):
    try:
        <some code that might fail>
        result[i] = <actual result>
    except:
        <what to do if the code fails>
        result[i] = None
```

#### Strategies for invoking and handling errors

Here we'll address situations that might arise when you are developing code for general
purpose use (e.g., writing functions in a package) and need that code
to invoke an error under certain circumstances or deal gracefully with an error occurring
in some code that you are calling.

A basic situation is when you want to detect a situation where you need to
invoke an error (i.e., throw an exception).

With `raise` you can invoke an exception. Suppose we need an input to be a positive number.
We'll use Python's built-in `ValueError`, one of the various [exception types
that Python provides](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) and that you could use. You can also create your own exceptions by subclassing one of Python's existing exception classes. (We haven't yet discussed classes and object-oriented programming, so don't worry if you're not sure about what that means.)

```python
#| error: true
def myfun(val):
    if val <= 0:
        raise ValueError("`val` should be positive")

myfun(-3)
```

Next let's consider cases where your function runs some code that might return an
error.

We'd often want to catch the error using `try-except`. In some cases we
would want to notify the user and then continue (perhaps falling back to a
different way to do things or returning `None`
from our function) while in others we might want to provide a more informative
error message than if we had just let the error occur, but still have the
exception be raised.

First let's see the case of continuing execution.


```python
#| error: true
import os

def myfun(filename):
    try:
        with open(filename, "r") as file:
            text = file.read()
    except Exception as err:
        print(f"{err}\nCheck that the file `{filename}` can be found "\
              f"in the current path: `{os.getcwd()}`.")
        return None

    return(text.lower())


myfun('missing_file.txt')
```

Finally let's see how we can intercept an error but then "re-raise" the error rather than
continuing execution.

```python
#| error: true
import requests

def myfun(url):
    try:
        requests.get(url)
    except Exception as err:
        print(f"There was a problem accessing {url}. "\
              f"Perhaps it doesn't exist or the URL has a typo?")
        raise

myfun("http://missingurl.com")
```


### Assertions

Assertions are a quick way to raise a specific type of Exception (AssertionError). Assertions are useful for performing quick checks in your code that the state of the program is as you expect. They're primarily intended for use during the development
process to provide "sanity checks" that specific conditions are true, and there are ways to disable them when you are running your code for production purposes (to improve performance). A common use is for verifying preconditions and postconditions (especially preconditions). One would generally only expect such conditions not to be true if there is a bug in the code. Here's an example of
using the `assert` statement in Python, with a clear assertion message
telling the developer what the problem is.

```python
#| eval: false
number = -42
assert number > 0, f"number greater than 0 expected, got: {number}"
## Produces this error:
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## AssertionError: number greater than 0 expected, got: -42

```

Various operators/functions are commonly used in assertions, including

```python
#| eval: false
assert x in y
assert x not in y
assert x is y
assert x is not y
assert isinstance(x, <some_type>)
assert all(x)
assert any(x)
```

### Testing

Testing is informally what you do after you write some code and want to check that it actually works. But when you are developing important code (e.g. functions that are going to be used by others) you typically want to encode your tests in code. There are many reasons to do that, including making sure that if someone else changes your code later on without fully understanding what it was supposed to do, the test suite should immediately indicate that.

Some people even advocate for writing a preliminary test suite before writing the code itself(!) as it can be a good way to organize work and track progress, as well as act as a secondary form of documentation for clarity.  This can include
tests that your code provides correct and useful errors when something
goes wrong (so that means that a test might be to see if problematic
input correctly produces an error). *Unit tests* are intended to test
the behavior of small pieces (units) of code, generally individual
functions. Unit tests naturally work well with the ideas above of
writing small, modular functions. I recommend the `pytest` package,
which is designed to make it easier to write sets of good tests.

In lab, we'll go over assertions, exceptions, and testing in
detail.

## Version control

- Use it! Even for projects that only you are working on. It's the closest thing you'll get to having a time machine!
- Use an issues tracker (e.g., the GitHub issues tracker is quite
    nice), or at least a simple to-do file, noting changes you'd like to
    make in the future.
- In addition to good commit messages, it's a good idea to keep good
    running notes documenting your projects.

We've already seen Git some and will see it in a lot more detail later
in the semester, so I don't have more to say here.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2. Debugging and recommendations for avoiding bugs →](03-2-debugging-and-recommendations-for-avoiding-bugs.md)
