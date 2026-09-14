---
title: We'd need to sort the results appropriately to align them with the observations.
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit6-parallel.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit6-parallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# We'd need to sort the results appropriately to align them with the observations.

**Source:** [`units/unit6-parallel.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit6-parallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

We’ll set up an artificial example with four slow tasks and 12 fast tasks and see the speed of running with the default of dynamic allocation under Dask's distributed scheduler. Then in the next section, we’ll compare to a situation in which more than one slow task may end up in a single batch/chunk.

```python
import scipy.special

n_cores = 4
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(n_workers = n_cores)
c = Client(cluster)

## 4 slow tasks and 12 fast ones.
n = np.repeat([5*10**7, 10**6, 10**6, 10**6], 4)
print(n)

def fun(i):
    print(f"Working on {i}.")
    out = np.mean(scipy.special.gammaln(np.exp(np.random.normal(size = n[i]))))
    print(f"Finishing {i}.")
    return out


t0 = time.time()
out = fun(1)
print(time.time() - t0)

t0 = time.time()
out = fun(5)
print(time.time() - t0)

t0 = time.time()
tasks = c.map(fun, range(len(n)))
results = c.gather(tasks)
print(time.time() - t0)

cluster.close()
```

For some reason the logging messages show up in the Quarto rendering output and not here in the document.

Note that (even with dynamic allocation) with relatively few tasks per core here, we could have gotten unlucky
if the tasks were in a random order and multiple slow tasks happen to be done by a single worker.

### Static allocation

Next, note that by default the ‘processes’ scheduler sets up tasks in batches, with a default chunksize of 6. However, it's difficult to understand out how Dask chooses to assign tasks to chunks (based on running this repeatedly there seems to be some randomness).


```python
dask.config.set(scheduler='processes', num_workers = 4)

tasks = []
p = len(n)
for i in range(p):
    tasks.append(dask.delayed(fun)(i))  # add lazy task

t0 = time.time()
results = dask.compute(tasks)  # compute all in parallel
print(time.time() - t0)
```

To force dynamic allocation, we can set `chunksize = 1` (as was shown in our original example of using the `processes` scheduler).

```python
#| eval: true
dask.config.set(scheduler='processes', num_workers = 4, chunksize = 1)

tasks = []
p = len(n)
for i in range(p):
    tasks.append(dask.delayed(fun)(i))  # add lazy task

t0 = time.time()
results = dask.compute(tasks)  # compute all in parallel
print(time.time() - t0)
```

In some cases when this has run, the times above are pretty similar.

In principle, with variability in execution time for the tasks, dynamic allocation should be faster than with static allocation, unless the static assignment of tasks to chunks is carefully done to achieve good load-balancing (or the assignment just happens to work out that way). It's also complicated by the fact that with dynamic allocation, one is essentially relying on the dynamics of the allocation resulting in achieving good load-balancing, which may not always happen.

We haven't illustrated it here, but if each task is quick and we have a lot of tasks, we likely want static allocation to avoid the extra overhead of starting each task individually. In fact, that is a main  motivation for static allocation.

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
