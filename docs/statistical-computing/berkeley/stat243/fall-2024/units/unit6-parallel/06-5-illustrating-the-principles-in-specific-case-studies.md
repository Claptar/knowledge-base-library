---
title: 5. Illustrating the principles in specific case studies
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit6-parallel.qmd) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 5. Illustrating the principles in specific case studies

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

# Generate data
n = 1000
p = 50
X = pd.DataFrame(np.random.normal(size = (n, p)),\
                 columns=[f"X{i}" for i in range(1, p + 1)])
Y = X['X1'] + np.sqrt(np.abs(X['X2'] * X['X3'])) +\
    X['X2'] - X['X3'] + np.random.normal(size = n)

n_folds = 10
seq = np.arange(n_folds)
folds = np.random.permutation(np.repeat(seq, 100))
```

To do a parallel map, we need to use the distributed scheduler, but it's
fine to do that with multiple cores on a single machine (such as a
laptop).

```python
n_cores = 2
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = n_cores)
c = Client(cluster)

tasks = c.map(cv_fit, range(n_folds))
results = c.gather(tasks)
# We'd need to sort the results appropriately to align them with the observations.
```

Now suppose you have 4 cores (and therefore won't have an equal number
of tasks per core with the 10 tasks). The approach in the next scenario should work
better.

## Scenario 4: parallelizing over prediction methods

**Scenario**: parallelizing over prediction methods or other cases where
execution time varies.

If you need to parallelize over prediction methods or in other contexts
in which the computation time for the different tasks varies widely, you
want to avoid having the parallelization group the tasks into batches in
advance, because some cores may finish a lot more quickly than others.
Starting the tasks one by one (not in batches) is called *dynamic allocation*.

In contrast, if the computation time is about the same for the different tasks
and you have a large number of tasks (in which case the effect of averaging may also help with load-balancing)
then you want to group the tasks into batches.  This is called *static allocation* or *prescheduling*.
This avoids the extra overhead (~1 millisecond per task) of scheduling many tasks.

### Dynamic allocation

With Dask's `distributed` scheduler, Dask starts up each delayed evaluation separately (i.e., dynamic allocation).

We’ll set up an artificial example with four slow tasks and 12 fast tasks and see the speed of running with the default of dynamic allocation under Dask's distributed scheduler. Then in the next section, we’ll compare to the worst-case scenario with all four slow tasks in a single batch.

```python
import scipy.special

n_cores = 4
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = n_cores)
c = Client(cluster)

## 4 slow tasks and 12 fast ones.
n = np.repeat([10**7, 10**5, 10**5, 10**5], 4)

def fun(i):
    print(f"Working on {i}.")
    return np.mean(scipy.special.gammaln(np.exp(np.random.normal(size = n[i]))))


t0 = time.time()
out = fun(1)
print(time.time() - t0)

t0 = time.time()
out = fun(5)
print(time.time() - t0)

t0 = time.time()
tasks = c.map(fun, range(len(n)))
results = c.gather(tasks)
print(time.time() - t0)  # 0.8 sec.

cluster.close()
```

Note that with relatively few tasks per core here, we could have gotten unlucky
if the tasks were in a random order and multiple slow tasks happen to be done
by a single worker.

### Static allocation

Next, note that by default the ‘processes’ scheduler sets up tasks in batches, with a default chunksize of 6. In this case that means that the first 4 (slow) tasks are all allocated to a single worker.

```python
dask.config.set(scheduler='processes', num_workers = 4)

tasks = []
p = len(n)
for i in range(p):
    tasks.append(dask.delayed(fun)(i))  # add lazy task

t0 = time.time()
results = dask.compute(tasks)  # compute all in parallel
print(time.time() - t0)   # 2.6 sec.
```

To force dynamic allocation, we can set `chunksize = 1` (as was shown in our original example of using the `processes` scheduler).

```python
#| eval: false
dask.config.set(scheduler='processes', num_workers = 4, chunksize = 1)

tasks = []
p = len(n)
for i in range(p):
    tasks.append(dask.delayed(fun)(i))  # add lazy task

t0 = time.time()
results = dask.compute(tasks)  # compute all in parallel
print(time.time() - t0)   # 2.6 sec.
```

We haven't illustrated it here, but if each task is quick and we have a lot of tasks, we likely want static allocation to avoid the extra overhead of starting each task individually.

### Choosing static vs. dynamic allocation in Dask

With the `distributed` scheduler, Dask starts up each delayed evaluation separately (i.e., dynamic allocation).
And even with a distributed `map()` it doesn’t appear possible to ask that the tasks be broken up into batches.
Therefore if you want static allocation, you could use the `processes` scheduler if using a single machine, or
if you need to use the `distributed` schduler you could break up the tasks into batches manually.

With the `processes` scheduler, static allocation is the default, with a default chunksize of 6 tasks per batch.
You can force dynamic allocation by setting `chunksize = 1`.

(Note that in R, static allocation is the default when using the `future` package.)

## Scenario 5: 10-fold CV across multiple methods with many more than 10 cores

**Specific scenario**: You are running an ensemble prediction method such as
SuperLearner or Bayesian model averaging on 10 cross-validation folds,
with many statistical/machine learning methods.

**General scenario**: parallelizing nested tasks or a large number of tasks,
ideally across multiple machines.

Here you want to take advantage of all the cores you have available, so
you can't just parallelize over folds.

First we'll discuss how to deal with the nestedness of the problem and
then we'll talk about how to make use of many cores across multiple
nodes to parallelize over a large number of tasks.

### Scenario 5A: nested parallelization

One can always flatten the looping, either in a for loop or in similar
ways when using apply-style statements.

```python
#| eval: false

## original code: multiple loops
for fold in range(n):
  for method in range(M):
     ### code here

## revised code: flatten the loops
for idx in range(n*M):
    fold = idx // M
    method = idx % M
    print(idx, fold, method)### code here
```

Rather than flattening the loops at the loop level (which you'd need to do to use `map`), one could just
generate a list of delayed tasks within the nested loops.

```python
#| eval: false
for fold in range(n):
  for method in range(M):
     tasks.append(dask.delayed(myfun)(fold,method))
```

The future package in R has some nice functionality for easily parallelizing with nested loops.

### Scenario 5B: Parallelizing across multiple nodes

If you have access to multiple machines networked together, including a
Linux cluster, you can use Dask to start workers across
multiple nodes (either in a nested parallelization situation with many
total tasks or just when you have lots of unnested tasks to parallelize
over). Here we'll just illustrate how to use multiple nodes, but if you
had a nested parallelization case you can combine the ideas just above
with the use of multiple nodes.

Simply start Python as you usually would. Then the following code
will parallelize on workers across the machines specified.

```python
#| eval: false
from dask.distributed import Client, SSHCluster
# First host is the scheduler.
cluster = SSHCluster(
    ["gandalf.berkeley.edu", "radagast.berkeley.edu", "radagast.berkeley.edu",
    "arwen.berkeley.edu", "arwen.berkeley.edu"]
)
c = Client(cluster)

## On the SCF, Savio and other clusters using the SLURM scheduler,
## you can figure out the machine names like this, repeating the name of the
## first machine to account for the main/scheduler/controller process:
##
## machines = subprocess.check_output("srun hostname", shell = True,
##            universal_newlines = True).strip().split('\n')
## machines = [machines[0]] + machines

def fun(i, n=10**6):
    return np.mean(np.random.normal(size = n))

n_tasks = 120

tasks = c.map(fun, range(n_tasks))
results = c.gather(tasks)

## And just to check we are actually using the various machines:
import subprocess

c.gather(c.map(lambda x: subprocess.check_output("hostname", shell = True), \
               range(4)))

cluster.close()
```

## Scenario 6: Stratified analysis on a very large dataset

**Specific scenario**: You are doing stratified analysis on a very large dataset
and want to avoid unnecessary copies.

**General scenario**: Avoiding copies when working with large data in parallel.

In many parallelization tools, if you try to parallelize this case on a single node, you end up making copies of the original dataset, which both takes up time and eats up memory. That is because the separate processes do not have access to objects used in the main (or other) processes, even though they are sharing the same physical memory. So the data needs to be sent to each process (or task) individually and then stored as distinct objects in memory.

Here when we use the `processes` scheduler, we make copies. Whether there is a copy per task or a copy per process seems to depend on exactly what the parallelized code is doing (perhaps based on whether there is random number generation in the code).

```python
import os

def do_analysis(i,x):
    '''
    A fake "analysis", identical for each task.
    '''
    # Check number of processes and copies.
    print(f"Object id: {id(x)}, process id: {os.getpid()}")
    return np.mean(x)

n_cores = 4

x = np.random.normal(size = 5*10**7)   # our big "dataset"

dask.config.set(scheduler='processes', num_workers = n_cores, chunksize = 1)

tasks = []
p = 8
for i in range(p):
    tasks.append(dask.delayed(do_analysis)(i,x))

t0 = time.time()
results = dask.compute(tasks)
t_elapsed = time.time() - t0
```

```
Object id: 140528840440112, process id: 1148556
Object id: 140619687115056, process id: 1148559
Object id: 140509694916912, process id: 1148561
Object id: 140539164195120, process id: 1148560
Object id: 140528840440112, process id: 1148556
Object id: 140619687115056, process id: 1148559
Object id: 140509694916912, process id: 1148561
Object id: 140539164195120, process id: 1148560
```

```python
print(t_elapsed)
```

A much better approach here would be to use the `threads` scheduler, in which case all workers can access the same data objects with no copying (but of course we cannot modify the data in that case without potentially causing problems for the other tasks). Without the copying, this is really fast.

```python
dask.config.set(scheduler='threads', num_workers = n_cores)

tasks = []
p = 8
for i in range(p):
    tasks.append(dask.delayed(do_analysis)(i,x))

t0 = time.time()
results = dask.compute(tasks)
print(time.time() - t0)
```

We can also consider using the the `distributed` scheduler (which is fine to use on a single machine or multiple machines). In order to have one copy per worker instead of one copy per task, we can apply `delayed()` to the global data object.

However, with the Dask distributed scheduler, it is complicated to assess what is going on, because the scheduler seems to try to optimize assignment of tasks to workers in a way that may cause an imbalance in the number of tasks assigned to each worker. In this example, all the tasks are assigned to a single worker.

(If instead the `do_analysis` function ran this: `np.mean(x + np.random.normal(size=5*10**7))`, we'd see the tasks be done on more than one worker.)

```python
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = n_cores)
c = Client(cluster)

x = dask.delayed(x)  # To have one copy per worker.

tasks = []
p = 8
for i in range(p):
    tasks.append(dask.delayed(do_analysis)(i,x))

t0 = time.time()
results = dask.compute(tasks)
print(time.time() - t0)

cluster.close()
```

Also, Dask gives a warning about sending the data to the workers in advance. I’m not sure of the distinction between what it is recommending and use of `dask.delayed(x)`. When I tried to use `scatter()` in various ways, I wasn't able to silence the warning.

## Scenario 7: Simulation study with n=1000 replicates: parallel random number generation

We’ll probably skip this for now and come back to it when we discuss random number generation in the Simulation Unit.

The key thing when thinking about random numbers in a parallel context
is that you want to avoid having the same 'random' numbers occur on
multiple processes. On a computer, random numbers are not actually
random but are generated as a sequence of pseudo-random numbers designed
to mimic true random numbers. The sequence is finite (but very long) and
eventually repeats itself. When one sets a seed, one is choosing a
position in that sequence to start from. Subsequent random numbers are
based on that subsequence. All random numbers can be generated from one
or more random uniform numbers, so we can just think about a sequence of
values between 0 and 1.

**Specific scenario**: You are running a simulation study with n=1000 replicates.

**General scenario**: Safely handling random number generation in parallel.

Each replicate involves fitting two statistical/machine learning
methods.

Here, unless you really have access to multiple hundreds of cores, you
might as well just parallelize across replicates.

However, you need to think about random number generation. One option is to set the random number seed to different values for each replicate. One danger in setting the seed like that is that the random numbers in the different replicate could overlap somewhat. This is probably somewhat unlikely if you are not generating a huge number of random numbers, but it’s unclear how safe it is.

We can use functionality with numpy's PCG64 or MT19937 generators to be completely safe in our parallel random number generation. Each provide a `jumped()` function that moves the RNG ahead as if one had generated a very large number of random variables ($2^{128}$) for the Mersenne Twister and nearly that for the PCG64).

Here’s how we can set up the use of the PCG64 generator:

```python
bitGen = np.random.PCG64(1)
rng = np.random.Generator(bitGen)
rng.random(size = 3)
```

Now let’s see how to jump forward. And then verify that jumping forward two increments is the same as making two separate jumps.

```python
bitGen = np.random.PCG64(1)
bitGen = bitGen.jumped(1)
rng = np.random.Generator(bitGen)
rng.normal(size = 3)

bitGen = np.random.PCG64(1)
bitGen = bitGen.jumped(2)
rng = np.random.Generator(bitGen)
rng.normal(size = 3)

bitGen = np.random.PCG64(1)
bitGen = bitGen.jumped(1)
bitGen = bitGen.jumped(1)
rng = np.random.Generator(bitGen)
rng.normal(size = 3)
```

We can also use `jumped()` with the Mersenne Twister.

```python
bitGen = np.random.MT19937(1)
bitGen = bitGen.jumped(1)
rng = np.random.Generator(bitGen)
rng.normal(size = 3)
```

So the strategy to parallelize across tasks (or potentially workers if random number generation is done sequentially for tasks done by a single worker) is to give each task the same seed and use `jumped(i)` where `i` indexes the tasks (or workers).

```python
#| eval: false
def myrandomfun(i):
    bitGen = np.random.PCG(1)
    bitGen = bitGen.jumped(i)
    # insert code with random number generation
```

One caution is that it appears that the period for PCG64 is $2^{128}$ and that `jumped(1)` jumps forward by nearly that many random numbers. That seems quite strange, and I don’t understand it.

Alternatively as [recommended in the docs](https://numpy.org/doc/stable/reference/random/bit_generators/pcg64.html):

```python
#| eval: false
n_tasks = 10
sg = np.random.SeedSequence(1)
rngs = [Generator(PCG64(s)) for s in sg.spawn(n_tasks)]
## Now pass elements of rng into your function that is being computed in parallel

def myrandomfun(rng):
    # insert code with random number generation, such as:
    z = rng.normal(size = 5)
```

In R, the `rlecuyer` package deals with this. The L’Ecuyer algorithm has a period of $2^{191}$, which it divides into subsequences of length $2^{127}$.

---

[← 4. Introduction to Dask](05-4-introduction-to-dask.md) · [Up: contents](index.md) · [6. Additional details and topics (optional) →](07-6-additional-details-and-topics-optional.md)
