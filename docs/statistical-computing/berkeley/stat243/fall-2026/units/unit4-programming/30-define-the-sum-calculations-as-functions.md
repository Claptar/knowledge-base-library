---
title: Define the sum calculations as functions
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit4-programming.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Define the sum calculations as functions

**Source:** [`units/unit4-programming.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit4-programming.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

def sum_by_row():
    return np.sum(tA, axis=1)

def sum_by_column():
    return np.sum(A, axis=0)

timeit.timeit(sum_by_row, number=10)
timeit.timeit(sum_by_column, number=10)  # potentially slow
```

Suppose we instead do the looping manually.

```python
timeit.timeit('[np.sum(A[:,col]) for col in range(A.shape[1])]',
    setup = 'import numpy as np', number=10, globals = {'A': A})
timeit.timeit('[np.sum(tA[row,:]) for row in range(tA.shape[0])]',
    setup = 'import numpy as np', number=10, globals = {'tA': tA})
```

Indeed, the row-wise calculations are much faster when done manually. However, when done with the `axis` argument in `np.sum` there is little difference. So that suggests numpy might be doing something clever in its implementation of `sum` with the `axis` argument.

!!! tip "Tip"
Suppose you were writing code for this kind of use case. How could you set up your calculations to do either row-wise or column-wise operations in a way that processes each number sequentially based on the order in which the numbers are stored? For example suppose the values are stored row-major but you want the column sums.
:::

When we define a numpy array, we can choose to use column-major order (i.e., "Fortran" order) with the `order` argument.

### Loop fusion

Let's consider this (vectorized) code:

```python
#| eval: false
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

Combining loops is called 'fusing' and is an [important optimization that Julia can do](https://docs.julialang.org/en/v1/manual/performance-tips/#More-dots:-Fuse-vectorized-operations), as shown in [this demo](https://computing.stat.berkeley.edu/tutorial-parallelization/parallel-julia#4-loops-and-fused-operations). It’s also a [key optimization done by XLA](https://www.tensorflow.org/xla), a compiler used with JAX and Tensorflow, so one approach to getting loop fusion in Python is to use JAX (or Tensorflow) for such calculations within Python rather than simply using numpy.

### JIT compilation (with JAX)

You can think of JAX as a version of numpy enabled to use the GPU (or automatically parallelize on CPU threads) and provide automatic differentiation. For its core operations, JAX defines versions of the operations (as compiled code) for the CPU and for the GPU.

We can also JIT compile JAX code. Behind the scenes, the instructions are compiled to machine code for different backends (e.g., CPU and GPU) using the XLA compiler.

Let's first consider running a vectorized calculation using JAX on the CPU, which will use multiple threads (discussed in Unit 6), each thread running on a separate CPU core on our computer. For now all we need to know is that the calculation will run in parallel, so we expect it to be faster than when using numpy, which won't run the calculation in parallel.

!!! warning "Warning"
This demo uses 4 GB of memory just in the process of creating `x`. Run on your own machine with caution.
:::

```python
#| eval: false
import time
import numpy as np
import jax.numpy as jnp

def myfun_np(x):
    y = np.exp(x) + 3 * np.sin(x)
    return y

def myfun_jnp(x):
    y = jnp.exp(x) + 3 * jnp.sin(x)
    return y

n = 500000000

x = np.random.normal(size = n).astype(np.float32)  # 32-bit for consistency with JAX default
x_jax = jnp.array(x)  # 32-bit by default
print(x_jax.platform())
```

```
cpu
```

```python
#| eval: false
t0 = time.time()
z = myfun_np(x)
t1 = time.time() - t0

t0 = time.time()
z_jax = myfun_jnp(x_jax).block_until_ready()
t2 = time.time() - t0

print(f"numpy time: {round(t1,3)}\njax time: {round(t2,3)}")
```

Running on the SCF gandalf machine (not shown above), we get these times.

```
numpy time: 17.181
jax time: 5.722
```

There's a nice speedup compared to numpy.

Since JAX will often execute computations asynchronously (in particular when using the GPU), the `block_until_ready` invocation ensures that the computation finishes before we stop timing.

By default the JAX floating point type is 32-bit so we forced the use of 32-bit numbers for numpy
for comparability. One could have JAX use 64-bit numbers like this:

```python
#| eval: false
import jax
jax.config.update("jax_enable_x64", True)
```

Next let's consider JIT compiling it, which should fuse the vectorized operations and avoid temporary objects. The JAX docs have a [nice discussion](https://jax.readthedocs.io/en/latest/notebooks/thinking_in_jax.html#to-jit-or-not-to-jit) of when JIT compilation will be beneficial.

```python
#| eval: false
import jax
myfun_jnp_jit = jax.jit(myfun_jnp)

t0 = time.time()
z_jax_jit = myfun_jnp_jit(x_jax).block_until_ready()
t3 = time.time() - t0
print(f"jitted jax time: {round(t3,3)}")
```

```
jitted jax time: 3.218
```

So that gives a nice two-fold additional speedup.

We could also have used the `jax.jit` decorator rather than directly calling `jax.jit`:

```python
#| eval: false
@jax.jit
def myfun_jnp(x):
    y = jnp.exp(x) + 3 * jnp.sin(x)
    return y
```

### Lazy evaluation

What's strange about this R code?

```r
f <- function(x) print("hi")
system.time(mean(rnorm(1000000)))
system.time(f(3))
system.time(f(mean(rnorm(1000000))))
```

It seems like the `rnorm(1000000)` is not actually executed when being passed to `f`. That is "lazy evaluation" in action - the code that is passed in as an argument is only evaluated when it is needed (and in this case it's not needed for the function to run).

Lazy evaluation is not just an R thing. It also occurs in Tensorflow (particularly version 1),
the Python Dask package, and in Spark. The basic idea is to delay executation until
it's really needed, with the goal that if one does so, the system may be
able to better optimize a series of multiple steps as a joint operation
relative to executing them one by one.

However, Python itself does not have lazy evaluation.

---

[← The following lines are very inefficient](29-the-following-lines-are-very-inefficient.md) · [Up: contents](index.md)
