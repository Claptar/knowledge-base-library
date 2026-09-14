---
title: 2. Debugging and recommendations for avoiding bugs
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit4-goodPractices.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit4-goodPractices.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Debugging and recommendations for avoiding bugs

**Source:** [`units/unit4-goodPractices.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit4-goodPractices.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Python's `pdb` package provides a standard debugger, with the ipython `ipdb` being a useful wrapper around `pdb`. JupyterLab also has a debugger. Perhaps the most commonly-used graphical debugger is provided via [VS Code](https://code.visualstudio.com/docs/python/debugging), which I encourage you to check out, particularly if you already use VS Code.


## Basic debugging strategies

Here we'll discuss some basic strategies for finding and fixing bugs. Other useful locations for tips on debugging include:

  - [Efficient Debugging by Goldspink](https://www.codementor.io/mattgoldspink/how-to-debug-code-efficiently-and-effectively-du107u9jh)
  - [Debugging for Beginners by Brody](https://blog.hartleybrody.com/debugging-code-beginner/)

Read and think about the error message (the *traceback*), starting from the bottom of the traceback. Sometimes it's inscrutable, but often it just needs a bit of deciphering. Looking up a given error message by simply doing a web search with the exact message in double quotes can be a good strategy, or you could look specifically on Stack Overflow.

Below we'll see how one can view the stack trace. Usually when an error occurs, it occurs in a function call that is nested in a series of function calls. This series of calls is the *call stack* and the *traceback* or *stack trace* shows that series of calls that led to the error. To debug, you'll often need to focus on the function being executed at the time the error occurred (which will be at the top of the call stack but the bottom of the traceback) and the arguments passed into that function. However, if the error occurs in a function you didn't write, the problem will often be with the arguments that your code provided at the last point in the call stack at which code that you wrote was run. Check the arguments that your code passed into that first function that is not a function of yours.

When running code that produces multiple errors, fix errors from the top down - fix the first error that is reported, because later errors are often caused by the initial error. It's common to have a string of many errors, which looks daunting, caused by a single initial error.

Is the bug reproducible - does it always happen in the same way at at the same point? It can help to restart Python and see if the bug persists - this can sometimes help in figuring out if there is a scoping issue and we are using a global variable that we did not mean to.

If you can't figure out where the error occurs based on the error messages, a basic strategy is to build up code in pieces (or tear it back in pieces to a simpler version). This allows you to isolate where the error is occurring. You might use a binary search strategy. Figure out which half of the code the error occurs in. Then split the 'bad' half in half and figure out which half the error occurs in. Repeat until you've isolated the problem.

If you've written your code modularly with lots of functions, you can test individual functions. Often the error will be in what gets passed into and out of each function.

At the beginning of time (the 1970s?), the standard debugging strategy was to insert print statements in one's code to see the value of a variable and thereby decipher what could be going wrong. We have better tools nowadays. But sometimes we still need to fall back to inserting print statements.

Python is a scripting language, so you can usually run your code line by line to figure out what is happening. This can be a decent approach, particularly for simple code. However, when you are trying to find errors that occur within a series of many nested function calls or when the errors involve variable scoping (how Python looks for variables that are not local to a function), or in other complicated situations, using formal debugging tools can be much more effective.  Finally, if the error occurs inside of functions provided by Python, rather than ones you write, it can be hard to run the code in those functions line by line.

## Using pdb

We can activate the debugger in various ways:

  - by inserting `breakpoint()` (or equivalently `import pdb; pdb.set_trace()`) inside a function or module at a location of interest (and then running the function or module)
  - by using `pdb.pm()` after an error (i.e., an *exception*) has occurred to invoke the browser at the point the error occurred
    - alternatively in IPython/Jupyter Notebook, run `%debug` (an IPython 'magic' command) and then run the code that results in the error
  - by running a function under debugger control with `pdb.run()`
  - by starting python with `python -m pdb file.py` and adding breakpoints

If you're using IPython or a Jupyter Notebook, `ipdb` is a wrapper for `pdb` that has all the same commands, but provides some nice features for interactivity (such as tab completion and syntax highlighting).

### Using `breakpoint`

Let's define a function that will run a stratified analysis, in this case fitting a regression to each of the strata (groups/clusters) in some data.
Our function is in `run_with_break.py`, and it contains `breakpoint` at the point where we want to invoke the debugger.

Now I can call the function and will be put into debugging mode just before the next line is called:

```python
#| eval: false
import run_with_break as run
run.fit(run.data, run.n_cats)
```

When I run this, I see this:

```
>>> run.fit(data, n_cats)
> /accounts/vis/paciorek/teaching/243/fall-2024/units/run_with_break.py(10)fit()
-> sub = data[data['cats'] == i]
(Pdb)
```

This indicates I am debugging at line 10 of `run_with_break.py`, which is the line that creates `sub`, but
I haven't yet created `sub`.

I can type `n` to run that line and go to the next one:

```
(Pdb) n
> /accounts/vis/paciorek/teaching/243/fall-2024/units/run_with_break.py(11)fit()
-> model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
```

at which point the debugger is about to execute line 11, which fits the regression.

I can type `c` to continue until the next breakpoint:

```
(Pdb) c
> /accounts/vis/paciorek/teaching/243/fall-2024/units/run_with_break.py(10)fit()
-> sub = data[data['cats'] == i]
```

Now if I print `i`, I see that it has incremented to `1`.

```
(Pdb) p i
1
```

We could keep hitting `n` or `c` until hitting the stratum where an error occurs, but that would be tedious.

Let's hit `q` to quit out of the debugger.

```
(Pdb) q
>>>
```

Note that all of these commands have graphical-based equivalents in VS Code.

Next let's see how we can enter debugging mode only at point an error occurs.

### Post-mortem debugging

We'll use a version of the module without the `breakpoint()` command.

```python
#| eval: false
import pdb
import run_no_break as run

run.fit(run.data, run.n_cats)
pdb.pm()
```

That puts us into debugging mode at the point the error occurred:

```
> /usr/local/linux/miniforge-3.12/lib/python3.12/site-packages/numpy/core/fromnumeric.py(86)_wrapreduction()
-> return ufunc.reduce(obj, axis, dtype, out, **passkwargs)
(Pdb)
```

which turns out to be in some internal Python function that calls a `reduce` function, which is where
the error occurs (presumably the debugger doesn't enter this function because it calls compiled code):

```
(Pdb) l
 81  	            if dtype is not None:
 82  	                return reduction(axis=axis, dtype=dtype, out=out, **passkwargs)
 83  	            else:
 84  	                return reduction(axis=axis, out=out, **passkwargs)
 85
 86  ->	    return ufunc.reduce(obj, axis, dtype, out, **passkwargs)
 87
 88
 89  	def _take_dispatcher(a, indices, axis=None, out=None, mode=None):
 90  	    return (a, out)
 91
```

We can enter `u` multiple times (it's only shown once below) to go up in the stack of function calls until we recognize code that we wrote:

```
(Pdb) u
> /accounts/vis/paciorek/teaching/243/fall-2024/units/run_no_break.py(10)fit()
-> model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
```

Now let's use `p` to print variable values to understand the problem:

```
(Pdb)  p i
29
(Pdb) p sub
Empty DataFrame
Columns: [y, x, cats]
Index: []
```

Ah, so in the 29th stratum there are no data!


### pdb commands

Here's a list of useful pdb commands (some of which we saw above) that you can use once you've entered debugging mode.

  - `h` or `help`: shows all the commands
  - `l` or `list`: show the code around where the debugger is currently operating
  - `c` or `continue`: continue running the code until the next breakpoint
  - `p` or `print`: print a variable or the result of evaluating an expression
  - `n` or `next`: run the current line and go to the next line in the current function
  - `s` or `step`: jump (step) into the function called in the current line (if it's a Python function)
  - `r` or `run`: exit out of the current function (e.g., if you accidentally stepped into a function) (but note this stops at breakpoints)
  - `unt` or `until`: run until the next line (or `unt <number>` to run until reaching line number <number>); this is useful for letting a loop run until completion
  - `b` or `break`: set a breakpoint
  - `tbreak`: one-time breakpoint
  - `where`: shows call stack
  - `u` (or `up`) and `d` (or `down`): move up and down the call stack
  - `q` quit out of the debugger
  - `<return>`: runs the previous pdb command again

### Invoking pdb on a function or block of code

We can use `pdb.run()` to run a function under the debugger. We need to make sure to use `s` as the first pdb command
in order to actually step into the function. From there, we can debug as normal as if we had set a breakpoint at the start
of the function.


```python
#| eval: false
import run_with_break as run
import pdb
pdb.run("run.fit(run.data, run.n_cats)")
(Pdb) s
```

### Invoking pdb on a module

We can also invoke pdb when we start Python, executing a file (module). Here we've added `fit(data, n_cats)`
at the end of `run_no_break2.py` so that we can have that run under the debugger.

```bash
#| eval: false
python -m pdb run_no_break2.py
```

```
> /accounts/vis/paciorek/teaching/243/fall-2024/units/run_no_break2.py(1)<module>()
-> import numpy as np
(Pdb)
```

Let's set a breakpoint at the same place we did with `breakpoint()` but using a line number (this avoids having to actually modify our code):

```
(Pdb) b 9
Breakpoint 1 at /accounts/vis/paciorek/teaching/243/fall-2024/units/run_no_break.py:9
```

```python
#| eval: false
(Pdb) c
> /accounts/vis/paciorek/teaching/243/fall-2024/units/run_no_break2.py(9)fit()
-> model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
```

So we've broken at the same point where we manually added `breakpoint()` in `run_with_break.py`.

Or we could have set a breakpoint at the start of the function:

```
(Pdb) disable 1
Disabled breakpoint 1 at /accounts/vis/paciorek/teaching/243/fall-2024/units/run_no_break2.py:9
(Pdb) b fit
Breakpoint 1 at /accounts/vis/paciorek/teaching/243/fall-2024/units/run_no_break.py:6
```

## Some common causes of bugs

Some of these are Python-specific, while others are common to a variety of languages.

 - Parenthesis mis-matches
 - `==` vs. `=`
 - Comparing real numbers exactly using `==` is dangerous because numbers on a computer are only represented to limited numerical precision. For example,
   ```python
   1/3 == 4*(4/12-3/12)
   ```
   We'll discuss in detail in Unit 8.
 - You expect a single value but execution of the code gives an array
 - Silent type conversion when you don't want it, or lack of coercion where you're expecting it
 - Using the wrong function or variable name
 - Giving unnamed arguments to a function in the wrong order
 - Forgetting to define a variable in the environment of a function and having Python, via lexical scoping, get that variable as a global variable from one of the enclosing scope. At best the types are not compatible and you get an error; at worst, you use a garbage value and the bug is hard to trace. In some cases your code may work fine when you develop the code (if the variable exists in the enclosing environment), but then may not work when you restart Python if the variable no longer exists or is different.
 - Python (usually helpfully) drops matrix and array dimensions that are extraneous. This can sometimes confuse later code that expects an object of a certain dimension. More on this below.

## Tips for avoiding bugs and catching errors

### Practice defensive programming

When writing functions, and software more generally, you'll want to warn the user or stop execution when there is an error and exit gracefully, giving the user some idea of what happened. Here are some things to consider:

 - check function inputs and warn users if the code will do something they might not expect or makes particular choices;
 - check inputs to `if` and the ranges in `for` loops;
 - provide reasonable default arguments;
 - document the range of valid inputs;
 - check that the output produced is valid; and
 - stop execution based on assertions, `try` or `raise` with an informative error message.


Here's an example of building a robust square root function:


```python
import warnings

def mysqrt(x):
    if isinstance(x, str):
        raise TypeError(f"What is the square root of '{x}'?")
    if isinstance(x, (float, int)):
        if x < 0:
            warnings.warn("Input value is negative.", UserWarning)
            return float('nan')   # Avoid complex number result.
        else:
            return x**0.5
    else:
        raise ValueError(f"Cannot take the square root of {x}")


mysqrt(3.1)
mysqrt(-3)
```

```python
#| eval: false
mysqrt('hat')
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in mysqrt
TypeError: What is the square root of 'hat'?
```

### Catch run-time errors with  `try/except` statements

Also, sometimes a function you call will fail, but you want to continue execution. For example, consider the stratified analysis show previously in which you take subsets of your data based on some categorical variable and fit a statistical model for each value of the categorical variable. If some of the subsets have no or very few observations, the statistical model fitting might fail. To do this, you might be using a for loop or `apply`. You want your code to continue and fit the model for the rest of the cases even if one (or more) of the cases cannot be fit.  You can wrap the function call that may fail within the `try` statement and then your code won't stop, even when an error occurs. Here's a toy example.

```python
import numpy as np
import pandas as pd
import random
import statsmodels.api

np.random.seed(2)
n_cats = 30
n = 80
y = np.random.normal(size=n)
x = np.random.normal(size=n)
cats = [np.random.randint(0, n_cats-1) for _ in range(n)]
data = pd.DataFrame({'y': y, 'x': x, 'cats': cats})

params = np.full((n_cats, 2), np.nan)
for i in range(n_cats):
    sub = data[data['cats'] == i]
    try:
        model = statsmodels.api.OLS(sub['y'], statsmodels.api.add_constant(sub['x']))
        fit = model.fit()
        params[i, :] = fit.params.values
    except Exception as error:
        print(f"Regression cannot be fit for stratum {i}.")

print(params)
```

The stratum with id 7 had no observations, so that call to do the regression failed, but the loop continued because we 'caught' the error with `try`. In this example, we could have checked the sample size for the subset before doing the regression, but in other contexts, we may not have an easy way to check in advance whether the function call will fail.

### Maintain dimensionality

Python (usually helpfully) drops array dimensions that are extraneous. This can sometimes confuse later code that expects an object of a certain dimension. Here's a work-around:

```python
import numpy as np
mat = np.array([[1, 2], [3, 4]])
np.sum(mat, axis=0)         # This sums columns, as desired

row_subset = 1
mat2 = mat[row_subset, :]
np.sum(mat2, axis=0)        # This sums the elements, not the columns.

if len(mat2.shape) != 2:    # Fix dimensionality.
    mat2 = mat2.reshape(1, -1)


np.sum(mat2, axis=0)
```

In this simple case it's obvious that a dimension will be dropped, but in more complicated settings, this can easily occur for some inputs without the coder realizing that it may happen. Not dropping dimensions is much easier than putting checks in to see if dimensions have been dropped and having the code behave differently depending on the dimensionality.

### Find and avoid global variables

In general, using global variables (variables that are not created or passed into a function) results in code that is not robust. Results will change if you or a user modifies that global variable, usually without realizing/remembering that a function depends on it.

One ad hoc strategy is to remove objects you don't need from Python's global scope, to avoid accidentally using values from an old object via Python's scoping rules.
You can also run your function in a fresh session to see if it's unable to find variables.


```python
del x   # Mimic having a fresh sesson (knowing in this case `x` is global).

def f(z):
    y = 3
    print(x + y + z)

try:
    f(2)
except Exception as error:
    print(error)

```

### Miscellaneous tips

 - Use core Python functionality and algorithms already coded. Figure out if a functionality already exists in (or can be adapted from) an Python package (or potentially in a C/Fortran library/package): code that is part of standard mathematical/numerical packages will probably be more efficient and bug-free than anything you would write.
 - Code in a modular fashion, making good use of functions, so that you don't need to debug the same code multiple times. Smaller functions are easier to debug, easier to understand, and can be combined in a modular fashion (like the UNIX utilities).
 - Write code for clarity and accuracy first; then worry about efficiency. Write an initial version of the code in the simplest way, without trying to be efficient (e.g., you might use for loops even if you're coding in Python); then make a second version that employs efficiency tricks and check that both produce the same output.
 - Plan out your code in advance, including all special cases/possibilities.
 - Write tests for your code early in the process.
 - Build up code in pieces, testing along the way. Make big changes in small steps, sequentially checking to see if the code has broken on test case(s).
 - Be careful that the conditions of `if` statements and `while` loops and the sequences of `for` loops are robust.
 - Don't hard code numbers - use variables (e.g., number of iterations, parameter values in simulations), even if you don't expect to change the value, as this makes the code more readable and reduces bugs when you use the same number multiple times; e.g. `speed_of_light = 3e8` or `n_its = 1000`.


In a future Lab, we'll go over debugging in detail.

### Code review

It's a good idea to have others review your code, ideally during the development process.

[This article](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012375) provides guidance on good practices for code review.

---

[← This test will fail.](03-this-test-will-fail.md) · [Up: contents](index.md) · [3. Tips for running analyses →](05-3-tips-for-running-analyses.md)
