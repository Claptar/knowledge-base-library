---
title: 5. Illustrating the principles in specific case studies
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Illustrating the principles in specific case studies

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Scenario 1: one model fit

**Specific scenario**: You need to fit a single statistical/machine learning
model, such as a random forest or regression model, to your data.

**General scenario**: Parallelizing a single task.

### Scenario 1A:

A given method may have been written to use parallelization and you
simply need to figure out how to invoke the method for it to use
multiple cores.

For example the documentation for the `RandomForestClassifier`
in scikit-learn's `ensemble` module indicates it can use multiple
cores -- note the `n_jobs` argument (not shown here because
the help info is very long).

```python
#| eval: false
import sklearn.ensemble
help(sklearn.ensemble.RandomForestClassifier)
```

!!! tip "Tip"
You'll usually need to look for an argument with one of the words *threads*, *processes*,
*cores*, *cpus*, *jobs*, etc. in the argument name.
:::

### Scenario 1B: Parallelized linear algebra

If a method does linear algebra computations on large matrices/vectors,
Python (and R) can call out to parallelized linear algebra packages (the BLAS and
LAPACK).

The BLAS is the library of basic linear algebra operations (written in
Fortran or C). A fast BLAS can greatly speed up linear algebra in R
relative to the default BLAS that comes with R. Some fast BLAS libraries
are

-   Intel's *MKL*; available for educational use for free
-   *OpenBLAS*; open source and free
-   Apple's Accelerate framework BLAS (*vecLib*) for Macs; provided with your Mac

In addition to being fast when used on a single core, all of these BLAS
libraries are threaded - if your computer has multiple cores and there
are free resources, your linear algebra will use multiple cores,
provided your program is linked against the threaded BLAS installed on
your machine and provided the shell environment variable `OMP_NUM_THREADS` is
not set to one. (Macs make use of `VECLIB_MAXIMUM_THREADS` rather than
`OMP_NUM_THREADS` and if MKL is being used, then one needs `MKL_NUM_THREADS`)

For parallel (threaded) linear algebra in Python, one can use an optimized BLAS with the `numpy` and (therefore)
`scipy` packages, on Linux or using the Mac's *vecLib* BLAS.
Details will depend on how you install Python, numpy, and scipy. More details on figuring out what BLAS is being used and how to install a fast threaded BLAS on your own computer are [here](https://statistics.berkeley.edu/computing/faqs/linear-algebra-and-parallelized-linear-algebra-using-blas).

Dask and some other packages also provide threading, but pure Python code is not threaded.

Here's some code that illustrates the speed of using a threaded BLAS:

```python
#| eval: false
import numpy as np
import time

x = np.random.normal(size = (6000, 6000))

start_time = time.time()
x = np.dot(x.T, x)
U = np.linalg.cholesky(x)
elapsed_time = time.time() - start_time
print("Elapsed Time (8 threads):", elapsed_time)
```

We'd need to restart Python after setting `OMP_NUM_THREADS` to 1 in order
to compare the time when run in parallel vs. on a single core.
That's hard to demonstrate in this generated document, but when I ran it,
it took 6.6 seconds, compared to 3 seconds using 8 cores.

!!! warning "Warning"
Note that for smaller linear algebra problems, we may not see any speed-up
or even that the threaded calculation might be slower because of
overhead in setting up the parallelization and because the parallelized
linear algebra calculation involves more actual operations than when done
serially.
:::

### Scenario 1C: GPUs and linear algebra

Linear algebra with large matrices is often a very good use case for GPUs.
So if you or someone implementing a method can run the linear algebra you
need on a GPU, that can give a big speedup.

Here's an example of using the GPU to multiply large matrices using PyTorch.
We could do this similarly with Tensorflow or JAX. I've just inserted the timing
from running this on an SCF machine with a powerful GPU.

Packages such as PyTorch, Tensorflow, and JAX can run linear algebra calculations
in parallel on either the CPU or GPU (depending on whether a GPU is available on the computer
the code is being run on).

Under the hood, there are different implementations (sometimes called *kernels*) of a given computation
For example, there would be both parallelized CPU and GPU implementations of matrix multiplication.


```python
#| eval: false
import torch

start = torch.cuda.Event(enable_timing=True)
end = torch.cuda.Event(enable_timing=True)

gpu = torch.device("cuda:0")

n = 10000
x = torch.randn(n,n, device = gpu)
y = torch.randn(n,n, device = gpu)

## Time the matrix multiplication on GPU:
start.record()
z = torch.matmul(x, y)
end.record()
torch.cuda.synchronize()
print(start.elapsed_time(end))   # 120 ms.

## Compare to CPU:
cpu = torch.device("cpu")

x = torch.randn(n,n, device = cpu)
y = torch.randn(n,n, device = cpu)

## Time the matrix multiplication on CPU:
start.record()
z = torch.matmul(x, y)
end.record()
torch.cuda.synchronize()
print(start.elapsed_time(end))   # 18 sec.
```

The GPU calculation takes 100-200 milliseconds (ms), while the CPU calculation
took 18 seconds using two CPU cores. That's a speed-up of more than 100x!

For a careful comparison between GPU and CPU, we'd want to consider the effect of
using 4-byte floating point numbers for the GPU calculation.

We'd also want to think about how many CPU cores should be used for the comparison.

### Scenario 1D: Parallelized vectorized calculations

Similarly, packages such as PyTorch, Tensorflow, and JAX can parallelize vectorized calculations
on either the CPU or GPU.

Recall that in Unit 5, we [used JAX to run a vectorized calculation on a very large 1-d array](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/unit5-programming.html#jit-compilation-with-jax).
JAX automatically ran that in parallel across multiple (CPU) cores.

Here we'll see that if we have GPU available, JAX will automatically run the calculation in parallel on the GPU.
I'll do this separately on a machine with a GPU and paste the results in here.

```python
#| eval: false
import time
import jax
import jax.numpy as jnp

def myfun_jnp(x):
    y = jnp.exp(x) + 3 * jnp.sin(x)
    return y

n = 500000000

key = jax.random.key(1)
x_jax = jax.random.normal(key, (n,))  # 32-bit by default
print(x_jax.platform())

t0 = time.time()
z_jax1 = myfun_jnp(x_jax).block_until_ready()
t_gpu = round(time.time() - t0, 3)

cpu_device = jax.devices('cpu')[0]
with jax.default_device(cpu_device):
    key = jax.random.key(1)
    x_jax = jax.random.normal(key, (n,))  # 32-bit by default
    print(x_jax.platform())
    t0 = time.time()
    z_jax2 = myfun_jnp(x_jax).block_until_ready()
    t_cpu = round(time.time() - t0, 3)

print(f"GPU time: {t_gpu}\nCPU time: {t_cpu}")
```

```
GPU time: 0.015
CPU time: 4.709
```

So the GPU is much faster, even though the JAX CPU implementation uses multiple threads (as can be seen with `top`).

Forcing JAX to use the CPU when a GPU is available is a bit of a hassle. When I tried to use `jax.config.update('jax_platform_name', 'cpu')`, it didn't seem to work for some reason.


## Scenario 2: three different prediction methods on your data

**Specific scenario**: You need to fit three different statistical/machine
learning models to your data.

**General scenario**: Parallelizing a small number of tasks.

What are some options?

-   use one core per model
-   if you have rather more than three cores, apply the ideas here
    combined with Scenario 1 above - with access to a cluster and
    parallelized implementations of each model, you might use one node
    per model

Here we'll use the `processes` scheduler.
In principal given this relies on numpy code, we could have also used the `threads` scheduler,
but I'm not seeing effective parallelization when I try that.

```python
import dask
import time
import numpy as np

def gen_and_mean(func, n, par1, par2):
    return np.mean(func(par1, par2, size = n))

dask.config.set(scheduler='processes', num_workers = 3, chunksize = 1)

n = 100000000
t0 = time.time()
tasks = []
tasks.append(dask.delayed(gen_and_mean)(np.random.normal, n, 0, 1))
tasks.append(dask.delayed(gen_and_mean)(np.random.gamma, n, 1, 1))
tasks.append(dask.delayed(gen_and_mean)(np.random.uniform, n, 0, 1))
results = dask.compute(tasks)
print(time.time() - t0)

t0 = time.time()
p = gen_and_mean(np.random.normal, n, 0, 1)
q = gen_and_mean(np.random.gamma, n, 1, 1)
s = gen_and_mean(np.random.uniform, n, 0, 1)
print(time.time() - t0)
```

Question: Why might this not have shown a perfect three-fold speedup?

You could also have used tools like a parallel map here
as well, as we'll discuss in the next scenario.

### Lazy evaluation, synchronicity, and blocking

If we look at the delayed objects, we see that each one is a representation of the computation that needs to be
done and that execution happens lazily. Also note that `dask.compute` executes *synchronously*, which means
the main process waits until the `dask.compute` call is complete before allowing other commands to be run.
This synchronous evaluation is also called
a *blocking* call because execution of the task in the worker processes blocks the main process.
In contrast, if control returns to the user before the worker processes are done, that would be
*asynchronous* evaluation (aka, a *non-blocking* call).

Note: the use of `chunksize = 1` forces Dask to immediately start one task on each worker. Without that argument, by default it groups tasks so as to reduce the overhead of starting each task individually, but when we have few tasks, that prevents effective parallelization. We'll discuss this in much more detail in Scenario 4.

Lazy evaluation is a concept that works well with computational graphs where the start of one piece of a computation can't start until another piece ends. For example, when we use `dask.delayed`, Dask will first [figure out the computational graph](https://docs.dask.org/en/stable/delayed.html) underlying a set of function calls and then execute them in the order needed. This makes use of lazy evaluation.

## Scenario 3: 10-fold CV and 10 or fewer cores

**Specific scenario**: You are running a prediction method on 10 cross-validation
folds.

**General scenario**: Parallelizing tasks via a parallel map.

This illustrates the idea of running some number of tasks using the
cores available on a single machine.

Here I'll illustrate using a parallel map, using this simulated dataset and
basic use of `RandomForestRegressor()`.

First, let's set up our fit function and simulate some data.

In this case our fit function uses global variables. The reason for this is that
we'll use Dask's `map` function, which allows us to pass only a single argument.
We could bundle the input data with the `fold_idx` value and pass as a larger
object, but here we'll stick with the simplicity of global variables.

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold

def cv_fit(fold_idx):
    train_idx = folds != fold_idx
    test_idx = folds == fold_idx
    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]
    Y_train = Y[train_idx]
    model = RandomForestRegressor()
    model.fit(X_train, Y_train)
    predictions = model.predict(X_test)
    return predictions


np.random.seed(1)

---

[← 4. Introduction to Dask](05-4-introduction-to-dask.md) · [Up: contents](index.md) · [Generate data →](07-generate-data.md)
