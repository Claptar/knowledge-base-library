---
title: 9. Efficiency
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit5-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 9. Efficiency

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit5-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Interpreters and compilation

### Why are interpreted languages slow?

Compiled code runs quickly because the original code has been translated into instructions (machine language) that the processor can understand (i.e., zeros and ones). In the process of doing so, various checking and lookup steps are done once and don't need to be redone when running the compiled code.

In contrast, when one runs code in an interpreted language such as Python or R, the interpreter needs to do all the checking and lookup each time the code is run. This is required because the types and locations in memory of the variables could have changed.

We'll focus on Python in the following discussion, but most of the concepts apply to other interpreted languages.

For example, consider this code:

```python
#| eval: false
x = 3
abs(x)
x*7

x = 'hi'
abs(x)
x*3

```

Because of dynamic typing, when the interpreter sees `abs(x)` it needs to check if `x` is something to which the absolute value function can be applied, including dealing with the fact that `x` could be a list or array with many numbers in it. In addition it needs to (using scoping rules) look up the value of `x`. (Consider that `x` might not even exist at the point that `abs(x)` is called.) Only then can the absolute value calculation happen. For the multiplication, Python needs to lookup the version of `*` that can be used, depending on the type of `x`.

Let's consider writing a loop with some ridiculous code:

```python
#| eval: false
x = np.random.normal(10)
for i in range(10):
    if np.random.normal(size = 1) > 0:
        x = 'hi'
    if np.random.normal(size = 1) > 0.5:
        del x
    x[i]= np.exp(x[i])
```

There is no way around the fact that because of how dynamic this is, the interpreter needs to check if `x` exists, if it is an array of sufficient length, if it contains numeric values, and it needs to go retrieve the required value, EVERY TIME the `np.exp()` is executed. Now the code above is unusual, and in most cases, we wouldn't have the `if` statements that modify `x`. So you could imagine a process by which the checking were done on the first iteration and then not needed after that -- that gets into the idea of just-in-time compilation, discussed later.

The standard Python interpreter (CPython) is a C function so in some sense everything that happens is running as compiled code, but there are lots more things being done to accomplish a given task using interpreted code than if the task had been written directly in code that is compiled. By analogy, consider talking directly to a person in a language you both know compared to talking to a person via an interpreter who has to translate between two languages. Ultimately, the same information gets communicated (hopefully!) but the number of words spoken and time involved is much greater.

When running more complicated functions, there is often a lot of checking that is part of the function itself. For example scipy's `solve_triangular` function ultimately calls out to the `trtrs` Lapack function, but before doing so, there is a lot of checking that can take time. To that point, the documentation suggests you might set `check_finite=False` to improve performance at the expense of potential problems if the input matrices contain troublesome elements.

We can flip the question on its head and ask what operations in an interpreted language will execute quickly. In Python, these include:

- operations that call out to compiled C code,
- linear algebra operations (these call out to compiled C or Fortran code provided by the BLAS and LAPACK software packages), and
- vectorized calls rather than loops:
   - vectorized calls generally run loops in compiled C code rather than having the loop run in Python, and
   - that means that the interpreter doesn't have to do all the checking discussed above for every iteration of the loop.


### Compilation

#### Overview

Compilation is the process of turning code in a given language (such a C++) into machine code. Machine code is the code that the processor actually executes. The machine code is stored in the executable file, which is a binary file. The history of programming has seen ever great levels of abstraction, so that humans can write code using syntax that is easier for us to understand, re-use, and develop building blocks that can be put together to do complicated tasks. For example assembly language is a step above machine code. Languages like C and Fortran provide additional abstraction beyond that. The Statistics 750 class at CMU has a [nice overview](https://36-750.github.io/tools/computer-architecture/#how-programs--aka-apps--run) if you want to see more details.

Note that interpreters such as Python are themselves programs -- the standard Python interpreter (CPython) is a C program that has been compiled. It happens to be a program that processes Python code. The interpreter doesn't turn Python code into machine code, but the interpreter itself is machine code.

#### Just-in-time (JIT) compilation

Standard compilation (ahead-of-time or AOT compilation) happens before any code is executed and can involve a lot of optimization to produce the most efficient machine code possible.

In contrast, just-in-time (JIT) compilation happens at the time that the code is executing. JIT compilation is heavily used in Julia, which is very fast (in some cases as fast as C). JIT compilation involves translating to machine code as the code is running. One nice aspect is that the results are cached so that if code is rerun, the compilation process doesn't have to be redone. So if you use a language like Julia, you'll see that the speed can vary drastically between the first time and later times you run a given function during a given session.

One thing that needs to be dealt with is type checking. As discussed above, part of why an interpreter is slow is because the type of the variable(s) involved in execution of a piece of code is not known in advance, so the interpreter needs to check the type. In JIT systems, there are often type inference systems that determine variable types.

JIT compilation can involve translation from the original code to machine code or translation of bytecode (see next section) to machine code.

At the end of this unit, we'll see the use of JIT compilation with the JAX package in Python.

`numba` is a standard JIT compiler for Python and numpy that uses the LLVM compiler library. To use it one applies the `numba.njit` decorator to a Python function.


#### Byte compiling (optional)

Functions in Python and Python packages may byte compiled. What does that mean?
Byte-compiled code is a special representation that can be
executed more efficiently because it is in the form of compact codes
that encode the results of parsing and semantic analysis of scoping and
other complexities of the Python source code. This byte code can be executed
faster than the original Python code because it skips the stage of having to
be interpreted by the Python interpreter.

If you look at the file names in the directory of an installed Python
package you may see files with the `.pyc` extension.
These files have been byte-compiled.

We can byte compile our own functions using either the `py_compile` or `compileall`
modules. Here's an
example (silly since as experienced Python programmers, we would use
vectorized calculation here rather than this unvectorized code.)

```python
#| include: false
## This is not working with knitr engine:
## `reticulate` has problem with `vec.pyc`.

```python
#| eval: false
import time

def f(vals):
    x = np.zeros(len(vals))
    for i in range(len(vals)):
        x[i] = np.exp(vals[i])
    return x

x = np.random.normal(size = 10**6)
t0 = time.time()
out = f(x)
time.time() - t0
```
```
0.7561802864074707
```

```python
#| eval: false
t0 = time.time()
out = np.exp(x)
time.time() - t0
```
```
0.013027191162109375
```

```bash
#| include: false
cp vec_orig.py vec.py
```

```python
#| eval: false
import py_compile
py_compile.compile('vec.py')
```

```
'__pycache__/vec.cpython-312.pyc'
```

```bash
#| eval: false
cp __pycache__/vec.cpython-312.pyc vec.pyc
rm vec.py    # Make sure non-compiled module not loaded.
```

```python
#| eval: false
import vec
vec.__file__
```
```
'/accounts/vis/paciorek/teaching/243fall24/fall-2024/units/vec.pyc'
```

```python
#| eval: false
t0 = time.time()
out = vec.f(x)
time.time() - t0
```
```
0.7301280498504639
```

Unfortunately, as seen above byte compiling may not speed things up much. I'm not sure why.


## Benchmarking and profiling

Recall that it's a waste of time to optimize code before you determine  (1) that the code is too slow for how it will be used and (2) which are the slow steps on which to focus your attempts to speed the code up. A 100x speedup in a step that takes 1% of the time will speed up the overall code by essentially nothing.

### Timing your code

There are a few ways to time code:

```python
import time
x = np.random.normal(size = 10**7)
t0 = time.time()
y = np.exp(x)
t1 = time.time()

print(f"Execution time: {t1-t0} seconds.")
```

In general, it's a good idea to repeat (replicate) your timing, as there is some stochasticity in how fast your computer will run a piece of code at any given moment.

```python
import time
t0 = time.time()
y = np.exp(3.)
t1 = time.time()

print(f"Execution time: {t1-t0} seconds.")
```

Using `time` is fine for code that takes a little while to run, but for code that is really fast (such as the code above), it may not be very accurate. Measuring fast bits of code is tricky to do well. This next approach is better for benchmarking code (particularly faster bits of code).

```python
import timeit

timeit.timeit('x = np.exp(3.)', setup = 'import numpy as np', number = 100)

code = '''
x = np.exp(3.)
'''

timeit.timeit(code, setup = 'import numpy as np', number = 100)
```

That reports the **total** time for the 100 replications.

We can run it from the command line.

```bash
python -m timeit -s 'import numpy' -n 1000 'x = numpy.exp(3.)'
```

`timeit` ran the code 1000 times for 5 different repetitions, giving the **average** time for the 1000 samples for the best of the 5 repetitions.


### Profiling

The `Cprofile` module will show you how much time is spent in
different functions, which can help you pinpoint bottlenecks in your
code.

I haven't run this code when producing this document as the output of
the profiling can be lengthy.


```python
#| eval: false

def lr_slow(y, x):
    xtx = x.T @ x
    xty = x.T @ y
    inv = np.linalg.inv(xtx)
    return inv @ xty

## generate random observations and random matrix of predictors
n = 7000
y = np.random.normal(size = 7000)
x = np.random.normal(size = (7000,1000))

t0 = time.time()
regr = lr_slow(y, x)
t1 = time.time()
print(f"Execution time: {t1-t0} seconds.")

import cProfile
cProfile.run('lr_slow(y,x)')
```


The `cumtime` column includes the time spent in nested calls to functions while the `tottime` column excludes it.

As we'll discuss in detail in Unit 10, we almost never want to explicitly invert
a matrix. Instead we factorize the matrix and use the factorized result to do the
computation of interest. In this case using the Cholesky decomposition is a standard
approach, followed by solving triangular systems of equations.

```python
#| eval: false

import scipy as sp

def lr_fast(y, x):
    xtx = x.T @ x
    xty = x.T @ y
    L = sp.linalg.cholesky(xtx)
    out = sp.linalg.solve_triangular(L.T,
          sp.linalg.solve_triangular(L, xty, lower=True),
          lower=False)
    return out

t0 = time.time()
regr = lr_fast(y, x)
t1 = time.time()
print(f"Execution time: {t1-t0} seconds.")

cProfile.run('lr_fast(y,x)')
```

In principle, the Cholesky now dominates the computational time (but is much faster than `inv`),
so there's not much more we can do in this case. That said, it's not obvious from the profiling
that the fact that most of the time is in the Cholesky is the case. Interpreting the output of a
profiler can be hard. In this case to investigate further I would probably time individual steps
with `timeit`.

You might wonder if it's better to use `x.T` or `np.transpose(x)`. Try using `timeit` to decide.

The Python profilers (`cProfile` and `profile` (not shown)) use [deterministic profiling](https://docs.python.org/3/library/profile.html#what-is-deterministic-profiling) -- calculating the interval between events (i.e., function calls and returns). However, there is some limit to accuracy -- the underlying 'clock' measures in units of about 0.001 seconds.

(In contrast, R's profiler works by sampling (statistical profiling) - every little while during a calculation it finds out what function R is in and saves that information to a file. So if you try to profile code that finishes really quickly, there's not enough opportunity for the sampling to represent the calculation accurately and you may get spurious results.)


## Writing efficient (Python) code

We'll discuss a variety of these strategies, including:

- Pre-allocating memory rather than growing objects iteratively
- Vectorization and use of fast matrix algebra
- Consideration of loops vs. map operations
- Speed of lookup operations, including hashing

While illustrated in Python, many of the underlying ideas pertain in other contexts.

### Pre-allocating memory

Let's consider whether we should pre-allocate space for the output of an operation or if it's ok to keep extending the length of an array or list.

```python
n = 100000
z = np.random.normal(size = n)

## Pre-allocation

def fun_prealloc(vals):
   n = len(vals)
   x = [0] * n
   for i in range(n):
       x[i] = np.exp(vals[i])
   return x

## Appending to a list

def fun_append(vals):
   x = []
   for i in range(n):
       x.append(np.exp(vals[i]))
   return x

## Appending to a numpy array

def fun_append_np(vals):
   x = np.array([])
   for i in range(n):
       x = np.append(x, np.exp(vals[i]))
   return x


t0 = time.time()
out1 = fun_prealloc(z)
time.time() - t0

t0 = time.time()
out2 = fun_append(z)
time.time() - t0

t0 = time.time()
out3 = fun_append_np(z)
time.time() - t0
```

So what's going on? First let's consider what is happening with the use of `np.append`.
Note that it is a function, rather than a method, and we need to reassign to `x`.
What must be happening in terms of memory use and copying when we append an element?

```python
x = np.random.normal(size = 5)
id(x)
id(np.append(x, 3.34))
```

We can avoid that large cost of copying and memory allocation by pre-allocating space for the entire output array. (This is equivalent to variable initialization in compiled languages.)

Ok, but how is it that we can append to the **list** at apparently no cost?

It's not magic, just that Python is clever. Let's get an idea of what is going on:

```python
def fun_append2(vals):
   n = len(vals)
   x = []
   print(f"Initial id: {id(x)}")
   sz = sys.getsizeof(x)
   print(f"iteration 0: size {sz}")
   for i in range(n):
       x.append(np.exp(vals[i]))
       if sys.getsizeof(x) != sz:
           sz = sys.getsizeof(x)
           print(f"iteration {i}: size {sz}")
   print(f"Final id: {id(x)}")
   return x

z = np.random.normal(size = 1000)
out = fun_append2(z)
```

Surprisingly, the id of `x` doesn't seem to change, even though we are allocating new memory at many of the iterations. What is happening is that `x` is a wrapper object that contains within it a reference to an array of references (pointers) to the list elements. The location of the wrapper object doesn't change, but the underlying array of references/pointers is being reallocated.

Side note: I don't know of any way to find out the location of the underlying array of pointers. I believe that under the hood, Python uses the `realloc` system call to request memory from the operating system when it needs to use additional pointers, and that the operating system can then try to allocate the additional memory at the same location (i.e., extending the block of memory).

Note that as we discussed in the previous section on memory use, our assessment of size above does not include the actual size of the list elements, as illustrated by having one element of the list be a big object:

```python
print(sys.getsizeof(out))
out[2] = np.random.normal(size = 100000)
print(sys.getsizeof(out))
```

!!! tip "Tip"
One upshot of how Python efficiently grows lists is that if you need to grow an object, use a Python list. Then once it is complete, you can always convert it to another type, such as a numpy array.
:::

### Vectorization and use of fast matrix algebra

One key way to write efficient Python code is to take advantage of numpy's
vectorized operations.

```python
n = 10**6
z = np.random.normal(size = n)
t0 = time.time()
x = np.exp(z)
print(time.time() - t0)


x = np.zeros(n)  # Leave out pre-allocation timing to focus on computation.
t0 = time.time()
for i in range(n):
    x[i] = np.exp(z[i])


print(time.time() - t0)
```

So what is different in how Python handles the calculations above that
explains the huge disparity in efficiency? The vectorized calculation is being done natively
in C in a for loop. The explicit Python for loop involves executing the for
loop in Python with repeated calls to C code at each iteration. This involves a lot
of overhead because of the repeated processing of the Python code inside the loop. For example,
in each iteration of the loop, Python is checking the types of the variables because it's possible
that the types might change, as discussed earlier.

You can usually get a sense for how quickly a Python call will pass things along
to C or Fortran by looking at the body of the relevant function(s) being called.

Unfortunately seeing the source code in Python often involves going and finding it in a file on disk,
whereas in R, printing a function will show its source code. However you can use `??` in IPython
to get the code for non-builtin functions. Consider `numpy.linspace??`.

Here I found the source code for the scipy `triangular_solve` function, which calls out to a Fortran function `trtrs`, found in the LAPACK library.

```bash
#| eval: false
## On an SCF machine:
/usr/local/linux/miniforge-3.12/lib/python3.12/site-packages/scipy/linalg/_basic.py
```

With a bit more digging around we could verify that `trtrs` is a LAPACK funcion by doing some grepping:

```
./linalg/_basic.py:    trtrs, = get_lapack_funcs(('trtrs',), (a1, b1))
```

Many numpy and scipy functions  allow you to pass in arrays, and operate on those
arrays in vectorized fashion. So before writing a for loop, look
at the help information on the relevant function(s) to see if they
operate in a vectorized fashion. Functions might take arrays for one or more of their arguments.

Outside of the numerical packages, we often have to manually do the looping:

```python
x = [3.5, 2.7, 4.6]
try:
    math.cos(x)
except Exception as error:
    print(error)

[math.cos(val) for val in x]
list(map(math.cos, x))
```

!!! tip "Tip"
Consider the chi-squared statistic involved in
a test of independence in a contingency table:

$$
\chi^{2}=\sum_{i}\sum_{j}\frac{(y_{ij}-e_{ij})^{2}}{e_{ij}},\,\,\,\, e_{ij}=\frac{y_{i\cdot}y_{\cdot j}}{y_{\cdot\cdot}}
$$

where $y_{i\cdot}=\sum_{j}y_{ij}$ and $y_{\cdot j} = \sum_{i} y_{ij}$ and $y_{\cdot\cdot} = \sum_{i} \sum_{j} y_{ij}$. Write this in a vectorized way
without any loops.  Note that 'vectorized' calculations also work
with matrices and arrays.
:::

Sometimes we can exploit vectorized mathematical operations in
surprising ways, though sometimes the
code is uglier.

```python
#| cache: true
x = np.random.normal(size = n)

## List comprehension
timeit.timeit('truncx = [max(0,val) for val in x]', number = 10, globals = {'x':x})
```

```python
#| cache: true
## Vectorized slice replacement
timeit.timeit('truncx = x.copy(); truncx[x < 0] = 0', number = 10, globals = {'x':x})
```

```python
#| cache: true
## Vectorized math trick
timeit.timeit('truncx = x * x>0', number = 10, globals = {'x':x})
```

We'll discuss what has to happen (in terms of calculations, memory allocation, and copying) in the two vectorized approaches to try to understand which is more efficient.

!!! tip "Tip"
 - If you do need to loop over dimensions of a matrix or array, if possible
loop over the smallest dimension and use the vectorized calculation
on the larger dimension(s). For example if you have a 10000 by 10 matrix, try to set
up your problem so you can loop over the 10 columns rather than the 10000 rows.
 - In general, in Python looping over rows is likely to be faster than looping over columns
because of numpy's row-major ordering (by default, matrices are stored in memory as a long array in which values in a row are adjacent to each other). However how numpy handles this is [more complicated](https://numpy.org/doc/stable/dev/internals.html#multidimensional-array-indexing-order-issues) (see more in the [Section on cache-aware programming](26-the-following-lines-are-very-inefficient.md#cache-aware-programming)), such that it may not matter for numpy calculations.
 - You can use direct arithmetic operations to add/subtract/multiply/divide
a 1-d array by each column of a matrix, e.g. `A*b` does element-wise multiplication of
each row of *A* by a 1-d array *b*. If you need to operate
by column, you can do it by transposing the matrix.
:::

Caution: relying on Python's broadcasting rule in the context of vectorized
operations, such as is done when direct-multiplying a matrix by a
1-d array to scale the columns relative to each other, can be dangerous as the code may not be easy for someone to read
and poses greater dangers of bugs. In some cases you may want to
first write the code more directly and
then compare the more efficient code to make sure the results are the same. It's also a good idea to  comment your code in such cases.

### Vectorization, mapping, and loops

Next let's consider when loops and mapping would be particularly slow and how mapping and loops might compare to each other.

First, the potential for inefficiency of looping and map operations in interpreted languages will depend in part on whether a substantial part of the work is in the overhead involved in the looping or in the time required by the function evaluation on each of the elements.

Here's an example, where the core computation is very fast, so we might expect the overhead of looping (in its various forms seen here) to be important.

```python
import time
n = 10**6
x = np.random.normal(size = n)

t0 = time.time()
out = np.exp(x)
time.time() - t0

t0 = time.time()
vals = np.zeros(n)
for i in range(n):
    vals[i] = np.exp(x[i])


time.time() - t0

t0 = time.time()
vals = [np.exp(v) for v in x]
time.time() - t0

t0 = time.time()
vals = list(map(np.exp, x))
time.time() - t0
```

Regardless of how we do the looping (an explicit loop, list comprehension, or `map`), it looks like we can't avoid the overhead unless we use the vectorized call,
which is of course the recommended approach in this case, both for speed and readability (and conciseness).

Second, is it faster to use `map` than to use a loop? In the example above it is somewhat (but not substantially) faster to use `map` (and still much slower than vectorization). In the loop case, the interpreter needs to do the checking we discussed earlier in this section at each iteration of the loop. What about in the `map` case? For mapping over a numpy array, perhaps not, but what if mapping over a list? Without digging into how `map` works, it's hard to say, but it does seem that based on this example, `map` is not doing anything special that saves much time when mapping over the elements of a numpy array.

Here's an example where the bulk of time is in the actual computation and not in the looping itself. We'll run a bunch of regressions on a matrix `X` (i.e., each column of `X` is a predictor) using each column of the matrix `mat` to do a separate regression.

```python
import time
import statsmodels.api as sm

n = 500000;
nr = 10000
nCalcs = int(n/nr)

mat = np.random.normal(size = (nr, nCalcs))

X = list(range(nr))
X = sm.add_constant(X)

def regrFun(i):
    model = sm.OLS(mat[:,i], X)
    return model.fit().params[1]

t0 = time.time()
out1 = list(map(regrFun, range(nCalcs)))
time.time() - t0

t0 = time.time()
out2 = np.zeros(nCalcs)
for i in range(nCalcs):
    out2[i] = regrFun(i)


time.time() - t0
```

Here they're about the same time (depending on when I render the document, I am getting some stochasticity in the timing). This is not too surprising -- the overhead of the iteration should be small relative to the fundamental cost of the model fitting, and we wouldn't be concerned with the overhead of using a loop.

### Matrix algebra efficiency

Often calculations that are not explicitly linear algebra calculations
can be done as matrix algebra. If our Python installation has a fast (and possibly parallelized) BLAS, this allows our calculation to take advantage of it.

For example, we can sum the rows of a matrix by multiplying by a 1-d array of ones.

```python
mat = np.random.normal(size=(500,500))

timeit.timeit('mat.dot(np.ones(500))', setup = 'import numpy as np',
              number = 1000, globals = {'mat': mat})

timeit.timeit('np.sum(mat, axis = 1)', setup = 'import numpy as np',
              number = 1000, globals = {'mat': mat})
```

Given the extra computation involved in actually multiplying each number by one, it's surprising that this is faster than numpy sum function. One thing we'd want to know is whether the BLAS matrix multiplication call is being done in parallel.

On the other hand, big matrix operations can be slow.

!!! tip "Tip"
Suppose you
want a new matrix that computes the differences between successive
columns of a matrix of arbitrary size. How would you do this as matrix
algebra operations? It's possible to write it as multiplying the matrix
by another matrix that contains 0s, 1s, and -1s in appropriate places.
 Here it turns out that the
*for* loop is much faster than matrix multiplication. However,
there is a way to do it faster as matrix direct subtraction.
:::

### Order of operations and efficiency

When doing matrix algebra, the order in which you do operations can
be critical for efficiency. How should I order the following calculation?

```python
n = 5000
A = np.random.normal(size=(n, n))
B = np.random.normal(size=(n, n))
x = np.random.normal(size=n)

t0 = time.time()
res1 = (A @ B) @ x
print(time.time() - t0)

t0 = time.time()
res1 = A @ (B @ x)
print(time.time() - t0)

```

!!! tip "Tip"
Why is the second order much faster?

Count the number of multiplications involved in each of the two approaches.
:::

### Avoiding unnecessary operations

We can use the matrix direct product (i.e., `A*B`) to do
some manipulations much more quickly than using matrix multiplication.

!!! tip "Tip"
How can I use the direct product to find the trace
of a matrix, $XY$?
:::

When working with diagonal matrices, you can generally get much faster results by being smart. The following operations: $X+D$, $DX$, $XD$
are mathematically the sum of two matrices and products of two matrices.
But we can do the computation without using two full matrices.


```python
n = 1000
X = np.random.normal(size=(n, n))
diagvals = np.random.normal(size=n)
D = np.diag(diagvals)

---

[← Let's turn that into a function for later use](24-let-s-turn-that-into-a-function-for-later-use.md) · [Up: contents](index.md) · [The following lines are very inefficient →](26-the-following-lines-are-very-inefficient.md)
