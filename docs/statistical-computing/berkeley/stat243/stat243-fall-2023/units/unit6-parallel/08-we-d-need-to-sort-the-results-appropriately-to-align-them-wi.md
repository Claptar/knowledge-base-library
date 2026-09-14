---
title: We'd need to sort the results appropriately to align them with the observations.
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit6-parallel.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# We'd need to sort the results appropriately to align them with the observations.

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit6-parallel.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

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
(or if you have so many tasks that the effect of averaging helps with load-balancing)
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

results = dask.compute(tasks)  # compute all in parallel
```

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

---

[← Generate data](07-generate-data.md) · [Up: contents](index.md) · [First host is the scheduler. →](09-first-host-is-the-scheduler.md)
