---
title: First host is the scheduler.
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# First host is the scheduler.

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

Here when we use the `processes` scheduler, we make copies. Whether there is a copy per task or a copy per process seems to depend on exactly what the parallelized code is doing, and I don't have additional information about this. In this case we see one copy per task, the worst case situation.

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
Object id: 128054524603408, process id: 257843
Object id: 126667880147984, process id: 257847
Object id: 123521035054096, process id: 257849
Object id: 125675309853712, process id: 257848
Object id: 128054526286832, process id: 257843
Object id: 126667881831408, process id: 257847
Object id: 123521036737520, process id: 257849
Object id: 125675311537136, process id: 257848
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

[← We'd need to sort the results appropriately to align them with the observations.](08-we-d-need-to-sort-the-results-appropriately-to-align-them-wi.md) · [Up: contents](index.md) · [6. Additional details and topics (optional) →](10-6-additional-details-and-topics-optional.md)
