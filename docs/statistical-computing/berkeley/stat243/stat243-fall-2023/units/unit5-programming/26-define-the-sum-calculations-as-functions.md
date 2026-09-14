---
title: Define the sum calculations as functions
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit5-programming.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Define the sum calculations as functions

**Source:** [`units/unit5-programming.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit5-programming.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

def sum_by_column():
    return np.sum(A, axis=0)

def sum_by_row():
    return np.sum(tA, axis=1)

timeit.timeit(sum_by_column, number=10)  # potentially slow
timeit.timeit(sum_by_row, number=10)
```

Suppose we instead do the looping manually.

```python
timeit.timeit('[np.sum(A[:,col]) for col in range(A.shape[1])]',
    setup = 'import numpy as np', number=10, globals = {'A': A})
timeit.timeit('[np.sum(tA[row,:]) for row in range(tA.shape[0])]',
    setup = 'import numpy as np', number=10, globals = {'tA': tA})
```

Indeed, the row-wise calculations are much faster when done manually. However, when done with the `axis` argument in `np.sum` there is little difference. So that suggests numpy might be doing something clever in its implementation of `sum` with the `axis` argument.

> **Challenge**: suppose you were writing code for this kind of use case. How could you set up your calculations to do either row-wise or column-wise operations in a way that processes each number sequentially based on the order in which the numbers are stored. For example suppose the values are stored row-major but you want the column sums.

When we define a numpy array, we can choose to use column-major order (i.e., "Fortran" order) with the `order` argument.

### Loop fusion

Let's consider this (vectorized) code:

```python
x = np.exp(x) + 3*np.sin(x)
```

This code has some downsides.

  - Think about whether any additional memory has to be allocated.
  - Think about how many for loops will have to get executed.

Contrast that to running directly as a for loop (e.g., here in Julia or in C/C++):

```julia
#| eval: false
for i in 1:length(x)
    x[i] = exp(x[i]) + 3*sin(x[i])
end
```

How does that affect the downsides mentioned above?

Combining loops is called 'fusing' and is an [important optimization that Julia can do](https://docs.julialang.org/en/v1/manual/performance-tips/#More-dots:-Fuse-vectorized-operations), as shown in [this demo](https://berkeley-scf.github.io/tutorial-parallelization/parallel-julia#4-loops-and-fused-operations). It’s also a [key optimization done by XLA](https://www.tensorflow.org/xla), a compiler used with Tensorflow, so one approach to getting loop fusion in Python is to use Tensorflow for such calculations within Python rather than simply using numpy.


### Lazy evaluation

What's strange about this R code?

```r
f <- function(x) print("hi")
system.time(mean(rnorm(1000000)))
system.time(f(3))
system.time(f(mean(rnorm(1000000))))
```

Lazy evaluation is not just an R thing. It also occurs in Tensorflow (particularly version 1),
the Python Dask package, and in Spark. The basic idea is to delay executation until
it's really needed, with the goal that if one does so, the system may be
able to better optimize a series of multiple steps as a joint operation
relative to executing them one by one.

However, Python itself does not have lazy evaluation.

---

[← The following lines are very inefficient](25-the-following-lines-are-very-inefficient.md) · [Up: contents](index.md)
