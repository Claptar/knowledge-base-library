---
title: 1. Good coding practices
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit3-goodPractices.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit3-goodPractices.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit3-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit3-goodPractices.qmd) — berkeley-stat243 · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1. Good coding practices

Some of these tips apply more to software development and some more to
analyses done for specific projects; hopefully it will be clear in most
cases what the relevant context(s) is/are.

## Editors

Use an editor (or integrated development environment) that supports the language you are using (e.g., *VS Code*, *Emacs*/*Aquamacs*, *Sublime*, *vim*, *TextMate*, *WinEdt*, or the built-in editor in *RStudio* [you can use Python from within RStudio]). Some advantages of this can include:

  1. helpful color coding of different types of syntax,
  2. automatic indentation and spacing,
  3. parenthesis matching,
  4. line numbering (good for finding bugs),
  5. code can often be run (or compiled) and debugged from within the editor, and
  6. integrated AI coding assistants for some IDEs (in particular in VS Code).

See the [problem set submission how-to](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/howtos/submitPS.html) for more information about editors that interact nicely with Quarto documents.

## Code syntax and style

### Coding syntax tips

The [PEP 8 style guide](https://peps.python.org/pep-0008) is your go-to reference for Python style.
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
- Comments: add helpful comments (but don't belabor the
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

You should put these ideas into practice in your assignments.

### Coding style suggestions

This is particularly focused on software development, but some of the
ideas are useful for data analysis as well.

- Break down tasks into core units.
- Write reusable code for core functionality and keep a single copy of
    the code (using version control) so you
    only need to make changes to a piece of code in one place.
- Smaller functions are easier to debug, easier to understand, and can
    be combined in a modular fashion (like the UNIX utilities).
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
- Write tests for each function (i.e., unit tests).
- Don't hard code numbers - use variables (e.g., number of iterations,
    parameter values in simulations), even if you don't expect to change
    the value, as this makes the code more readable. For example, the speed of light is a constant in a scientific sense, but best to make it a variable in code: `speed_of_light = 3e8`.
- Use lists or tuples to keep disparate parts of related data together.
- Practice defensive programming (see also the discussion below on raising exceptions and assertions):
    - check function inputs and warn users if the code will do something they might not expect or makes particular choices;
    - check inputs to *if*:
        - Note that in Python, an expression used as the condition of an `if` will be equivalent to `True` unless it is one of `False`, `0`, `None`, or an empty list/tuple/string.
    - provide reasonable default arguments;
    - document the range of valid inputs;
    - check that the output produced is valid; and
    - stop execution based on checks and give an informative error message.
- Try to avoid system-dependent code that only runs on a specific
    version of an OS or specific OS.
- Learn from others' code.
- Ask others to review your code and help by reviewing other people's code.
- Consider rewriting your code once you know all the settings and
    conditions; often analyses and projects meander as we do our work
    and the initial plan for the code no longer makes sense and the code
    is no longer designed specifically for the job being done.

### Linting

Linting is the process of applying a tool to your code to enforce style.

Here we'll see how to use `ruff`. You might also consider `black`.

We’ll practice with ruff with a small module we’ll use next also for debugging.

!!! tip "Tip"
You can install `ruff` via pip (`pip install ruff`), either inside a Conda environment or outside (in which case it will likely be installed at `~/.local/bin/ruff`).
:::

First, we check for and fix syntax errors.

```bash
#| output: false
#| echo: false
cp test-unlinted.py test.py
rm -f test-save.py
```

```bash
ruff check test.py
```

Then we ask ruff to reformat to conform to standard style.

```bash
cp test.py test-save.py   # Not required, just so we can see what `ruff` did.
ruff format test.py
```

Let’s see what changed:

```bash
#| error: true
diff test-save.py test.py
```

```bash
#| output: false
#| echo: false
cp test-unlinted.py test.py
```

So we see that `ruff` fixed spacing and properly indented the comment line.

## Assertions, exceptions and testing

Assertions, exceptions and testing are critically important for writing robust
code that is less likely to contain bugs.

This has always been the case. It continues to be the case with increasing reliance on AI coding agents, which can and do make mistakes.

### Exceptions

You've probably already seen exceptions in action whenever you've done something
in Python that causes an error to occur and an error message to be printed.
Syntax errors are different from exceptions in that exceptions occur
when the syntax is correct, but the execution of the code results in some sort of error (i.e., a *run-time error*).

Exceptions can be a valuable tool for making your code handle different modes of failure (missing file, URL unreachable, permission denied, invalid inputs, etc.). You use them when you are writing code that is supposed to perform a task (e.g., a function that does something with an input file) to indicate that the task failed and the reason for that failure (e.g., the file was not there in the first place). In such a case, you want your code to raise an exception and make the error message informative as possible, typically by handling the exception thrown by another function you call and augmenting the message. Another possibility is that your code detects a situation where you need to throw an exception (e.g., an invalid input to a function).

The other side of the coin happens when you want to write a piece of code that handles failure in a specific way, instead of simply giving up. For example, if you are writing a script that reads and downloads hundreds of URLs, you don't want your program to stop when any of them fails to respond (or do you?). You might want to continue with the rest of the URLs, and write out the failed URLs in a secondary output file.

#### Strategies for invoking and handling errors

Here we'll address situations that might arise when you are developing code for general
purpose use (e.g., writing functions in a package) and need that code
to invoke an error under certain circumstances or deal gracefully with an error occurring
in some code that you are calling.

A basic situation is when you want to detect a situation where you need to
invoke an error (i.e., "throw an exception").

With `raise` you can invoke an exception. Suppose we need an input to be a positive number.
We'll use Python's built-in `ValueError`, one of the various [exception types
that Python provides](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) and that you could use. You can also create your own exceptions by subclassing one of Python's existing exception classes. (We haven't yet discussed classes and object-oriented programming, so don't worry if you're not sure about what that means.)

```python
#| echo: false
#| eval: false
#| error: true
## This is causing a rendering error: "Text line contains an invalid character"
def myfun(val):
    if val <= 0:
        raise ValueError("`val` should be positive")

myfun(-3)
```

```python
#| error: true
def myfun(val):
    if val <= 0:
        raise ValueError("`val` should be positive")

myfun(-3)
```

Next let's consider cases where your function runs some code that might result in an
error (or might not).

We'd often want to catch the error using `try-except`. In some cases we
would want to notify the user and then continue (perhaps falling back to a
different way to do things or returning `None`
from our function) while in others we might want to provide a more informative
error message than if we had just let the error occur, but still have the
exception be raised.

We can embed the code that might fail in a `try` block and then in the `except` block, run code that will handle the situation when the error occurs.

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
continuing execution. This isn't printing out nicely in the rendered document if I actually
run this code during rendering, so I'll just insert some of the output that should be produced.

```python
#| error: true
#| eval: false
import requests

def myfun(url):
    try:
        requests.get(url)
    except Exception as err:
        print(f"There was a problem accessing {url}. "\
              f"Perhaps it doesn't exist or the URL has a typo?")
        raise

myfun("http://missingurl_forsure.com")
```

```
There was a problem accessing http://missingurl_forsure.com. Perhaps it doesn't exist or the URL has a typo?
Traceback (most recent call last):
  File "/usr/local/linux/miniforge-3.13/lib/python3.13/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
        (self._dns_host, self.port),
    ...<2 lines>...
        socket_options=self.socket_options,
    )

<snip>

  File "/usr/local/linux/miniforge-3.13/lib/python3.13/site-packages/requests/adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='missingurl_forsure.com', port=80): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPConnection object at 0x7ca7d8e13e00>: Failed to resolve 'missingurl_forsure.com' ([Errno -2] Name or service not known)"))
```

### Assertions

Assertions are a quick way to raise a specific type of Exception: an `AssertionError`. Assertions are useful for performing quick checks in your code that the state of the program is as you expect. They're primarily intended for use during the development
process to provide "sanity checks" that specific conditions are true, and there are ways to disable them when you are running your code for production purposes (to improve performance). A common use is for verifying preconditions and postconditions (especially preconditions). One would generally only expect such conditions not to be true if there is a bug in the code. Here's an example of
using the `assert` statement in Python, with a clear assertion message
telling the developer what the problem is.

```python
#| error: true
number = -42
assert number > 0, f"number greater than 0 expected, got: {number}"
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

Assertions can also be quite useful in the context of data analysis pipelines for checking that the state of the analysis is as expected. E.g., at various points, you might check that the dimension of your data is as expected, check for missing or extreme/unexpected values, etc.

Next we'll see that assertions are a core part of setting up tests.

### Testing

When we set up formal testing for code, the testing itself is written in code so that it can be run repeatedly. Setting up formal tests increases our faith in the correctness of the code. And by having the testing be reproducible, it helps to make sure that  if anyone changes the code later on and breaks something, the test suite should immediately indicate that.

Some people even advocate for writing a preliminary test suite before writing the code itself(!) as it can be a good way to organize work and track progress, as well as act as a secondary form of documentation for clarity.  This can include
tests that your code provides correct and useful errors when something
goes wrong (so that means that a test might be to see if problematic
input correctly produces an error). *Unit tests* are intended to test
the behavior of small pieces (units) of code, generally individual
functions. Unit tests naturally work well with the ideas above of
writing small, modular functions. I recommend the `pytest` package,
which is designed to make it easier to write sets of good tests.

Here is an example of the contents of a test file, called `test_dummy.py`.

```python
#| eval: false
import pytest
import numpy as np

import dummy

def test_numeric():
    assert dummy.add_one(3) == 4

# This test will fail.
def test_numpy_array():
    assert np.all(np.equal(dummy.add_one(np.array([3,4])), np.array([4,5])))

def test_bad_input():
    with pytest.raises(TypeError):
        dummy.add_one('hello')

def test_warning():
    with pytest.warns(UserWarning, match='complex'):
        dummy.add_one(1+3j)
```

We can then run the tests via `pytest` like this:

```bash
#| error: true
pytest test_dummy.py
```

You can run `pytest` on individual files or on directories or simply in the current working directory. In the latter cases, it will look for test files (those with the letters "test" in the file name) in the directory and all subdirectories.

In lab, we'll go over assertions, exceptions, and testing in
detail.

### Automated testing

*Continuous integration* (CI) is the term for carrying out actions automatically as your code changes. The most common kind of CI is automated testing - running your tests on your code when you make changes to the code. This enforces the discipline of running tests regularly and avoids the common problem that testing passes locally on your own machine, but fails for various reasons when done elsewhere.

A standard way to do this is via GitHub Actions (GHA).

To set up a GitHub Actions workflow, one

- specifies when the workflow will run (e.g., when a push or pull request is made, or only manually)
- provides instructions for how to set up the environment for the workflow
- provides the operations that the workflow should run.

The workflow is specified using a YAML file placed in the `.github/workflows` directory of the repository.

With GHA, you specify the operating system and then the steps to run in the YAML file. Some steps will  customize the environment as the initial steps and then additional step(s) will run shell or other code to run your workflow. You use pre-specified operations (called *actions*) to do common things (such as checking out a GitHub repository and installing commonly used software).

When triggered, GitHub will run the steps in a virtual machine, which is called the *runner*.

Here's an example YAML file for testing [an example package called `mytoy`](https://github.com/fperez/mytoy):

```
on:
  push:
    branches:
    - main

jobs:
  CI:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v7

    # Install package and dependencies
    - name: Set up Python
      uses: actions/setup-python@v7
      with:
        python-version: 3.14

    - name: Install mytoy and pytest
      run: |
        pip install pytest
        pip install --user .

    - name: Run tests
      run: |
        cd mytoy
        pytest
```

Unfortunately, GitHub Actions is not available via `github.berkeley.edu` so we
can't use it with your class repositories for your problem set work.

## Version control

- Use it! Even for projects that only you are working on. It's the closest thing you'll get to having a time machine!
- Use an issues tracker (e.g., the GitHub issues tracker is quite
    nice), or at least a simple to-do file, noting changes you'd like to
    make in the future.

We'll be discussing Git a lot separately.

## AI-assisted coding tools

There is now a large variety of AI-assisted coding tools that are available within integrated development environments (IDEs) and allow you to easily work with AI while you are coding. This makes for an easier workflow than copy-pasting from a ChatBot.

!!! warning "Warning"
The arena of AI-assisted coding tools is evolving very quickly.
:::

Some common features of many tools include:

- AI-assisted code completion (extended tab completion)
- AI-assisted code suggestions (accept/reject, similar to grammar suggestions in text editing)
- Built-in Chat window providing interaction with an agent that can write and edit code.
- Ability to give files/directories as context.

Many of the tools are available through VS Code (as extensions, such as GitHub Copilot and Gemini Code Assist) or built on top of VS Code (e.g., Cursor). Other tools provide command line interfaces (e.g., Claude Code, Codex and Antigravity)

Beware of generating chunks of code (particularly large chunks) that you don't understand, particularly as you are learning. Think of the tools as helping you brainstorm.

A potential hierarchy of uses:

 - For straightforward syntax where checking the outcome is sufficient (e.g., code for formatting plots).
 - For (possibly complicated) small pieces of code where extensive testing may be sufficient (e.g., regular expressions).
 - For more extensive analysis or algorithm code, where you should check and understand the code fully.

---

[← Overview](01-overview.md) · [Up: contents](index.md) · [2. Debugging and recommendations for avoiding bugs →](03-2-debugging-and-recommendations-for-avoiding-bugs.md)
