---
title: 2. MapReduce and Dask
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit7-bigData.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. MapReduce and Dask

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit7-bigData.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Traditionally, high-performance computing (HPC) has concentrated on
techniques and tools for message passing such as MPI and on developing
efficient algorithms to use these techniques. In the last 20 years,
focus has shifted to technologies for processing large datasets that are
distributed across multiple machines but can be manipulated as if they
are one dataset.

Two commonly-used tools for doing this are Spark and Python's Dask
package. We'll cover Dask. Spark was popular for a while, but I'm
not sure how much it is used now.

## Overview

A basic paradigm for working with big datasets is the *MapReduce*
paradigm. The basic idea is to store the data in a distributed fashion
across multiple nodes and try to do the computation in pieces on the
data on each node. Results can also be stored in a distributed fashion.

A key benefit of this is that if you can't fit your dataset on disk on
one machine you can on a cluster of machines. And your processing of the
dataset can happen in parallel. This is the basic idea of *MapReduce*.

The basic steps of *MapReduce* are as follows:

-   read individual data objects (e.g., records/lines from CSVs or
    individual data files)
-   *map*: create key-value pairs using the inputs (more formally, the map
    step takes a key-value pair and returns a new key-value pair)
-   *reduce*: for each key, do an operation on the associated values and
    create a result - i.e., aggregate within the values assigned to each
    key
-   write out the {key,result} pair

A similar paradigm that is implemented in `pandas` and `dplyr` is the
[split-apply-combine strategy](http://www.jstatsoft.org/v40/i01/paper).

A few additional comments. In our map function, we could exclude values
or transform them in some way, including producing multiple records from
a single record. And in our reduce function, we can do more complicated
analysis. So one can actually do fairly sophisticated things within what
may seem like a restrictive paradigm. But we are constrained such that
in the map step, each record needs to be treated independently and in
the reduce step each key needs to be treated independently. This allows
for the parallelization.


!!! warning "Warning"
One important note is that any operations that require moving a lot of
data between the workers can take a long time. (This is sometimes
called a *shuffle*.) This could happen if, for example, you computed the
median value within each of many groups if the data for each group are
spread across the workers. In contrast, if we compute the mean or sum,
one can compute the partial sums on each worker and then just add up the
partial sums.
:::

Note that as discussed in Unit 5 the concepts of *map* and *reduce* are core concepts in
functional programming, and of course Python provides the `map` function.

*Hadoop* is an infrastructure for enabling MapReduce across a network of
machines. The basic idea is to hide the complexity of distributing the
calculations and collecting results. Hadoop includes a file system for
distributed storage (HDFS), where each piece of information is stored
redundantly (on multiple machines). Calculations can then be done in a
parallel fashion, often on data in place on each machine thereby
limiting the amount of communication that has to be done over the
network. Hadoop also monitors completion of tasks and if a node fails,
it will redo the relevant tasks on another node. Hadoop is based on
Java. Given the popularity of Spark, I'm not sure how much usage these
approaches currently see. Setting up a Hadoop cluster can be tricky.
Hopefully if you're in a position to need to use Hadoop, it will be set
up for you and you will be interacting with it as a user/data analyst.

Ok, so what is Spark? You can think of Spark as in-memory Hadoop. Spark
allows one to treat the memory across multiple nodes as a big pool of
memory. Therefore, Spark should be faster than Hadoop when the data
will fit in the collective memory of multiple nodes. In cases where it
does not, Spark will make use of the HDFS (and generally, Spark will be
reading the data initially from HDFS.) While Spark is more user-friendly
than Hadoop, there are also some things that can make it hard to use.
Setting up a Spark cluster also involves a bit of work, Spark can be
hard to configure for optimal performance, and Spark calculations have a
tendency to fail (often involving memory issues) in ways that are hard
for users to debug.

## Using Dask for big data processing

Unit 6 on parallelization gives an overview of using Dask for flexible parallelization
on different kinds of computational resources (in particular,
parallelizing across multiple cores on one machine versus parallelizing
across multiple cores across multiple machines/nodes).

Here we'll see the use of Dask to work with distributed datasets. Dask
can process datasets (potentially very large ones) by parallelizing
operations across subsets of the data using multiple cores on one or
more machines.

Like Spark, Dask automatically reads data from files in parallel and
operates on *chunks* (also called *partitions* or *shards*) of the full
dataset in parallel. There are two big advantages of this:

-   You can do calculations (including reading from disk) in parallel
    because each worker will work on a piece of the data.
-   When the data is split across machines, you can use the memory of
    multiple machines to handle much larger datasets than would be
    possible in memory on one machine. That said, Dask processes the
    data in chunks, so one often doesn't need a lot of memory, even just
    on one machine.

While reading from disk in parallel is a good goal, if all the data are
on one hard drive, there are limitations on the speed of reading the
data from disk because of having multiple processes all trying to access
the disk at once. Supercomputing systems will generally have parallel
file systems that support truly parallel reading (and writing, i.e.,
*parallel I/O*). Hadoop/Spark deal with this by distributing across
multiple disks, generally one disk per machine/node.

Because computations are done in external compiled code (e.g., via
`numpy`) it's effective to use the `threads` scheduler when operating on
one node to avoid having to copy and move the data.

### Dask dataframes (pandas)

Dask dataframes are Pandas-like dataframes where each dataframe is split
into groups of rows, stored as smaller Pandas dataframes.

One can do a lot of the kinds of computations that you would do on a
Pandas dataframe on a Dask dataframe, but many operations are not
possible. See [here](http://docs.dask.org/en/latest/dataframe-api.html).

By default dataframes are handled by the `threads` scheduler.
(Recall we discussed Dask's various schedulers in Unit 6.)

Here's an example of reading from a dataset of flight delays (about 11
GB data). You can get the data
[here](https://www.stat.berkeley.edu/share/paciorek/1987-2008.csvs.tgz).

We'll specify some dtypes as otherwise Pandas complains about the fact
that some columns mix what appear to be ints and floats.

```python
#| eval: false
import dask
dask.config.set(scheduler='threads', num_workers = 4)
import dask.dataframe as ddf
path = '/scratch/users/paciorek/243/AirlineData/csvs/'
air = ddf.read_csv(path + '*.csv.bz2',
      compression = 'bz2',
      encoding = 'latin1', # (unexpected) latin1 value(s) in TailNum field in 2001
      dtype = {'Distance': 'float64', 'CRSElapsedTime': 'float64',
      'TailNum': 'object', 'CancellationCode': 'object', 'DepDelay': 'float64',
      'ActualElapsedTime': 'float64', 'ArrDelay': 'float64', 'ArrTime': 'float64',
       'DepTime': 'float64'})
air
air.npartitions
```

Dask will reads the data in parallel from the various .csv.bz2 files
(unzipping on the fly), but note the caveat in the previous section
about the possibilities for truly parallel I/O.

However, recall that Dask uses delayed (lazy) evaluation. In this case, the reading is delayed until
`compute()` is called. For that matter, the various other calculations
(`max`, `groupby`, `mean`) shown below are only done after `compute()` is called.

```python
#| eval: false
import time

t0 = time.time()
max_delay = air.DepDelay.max().compute()   # This takes a while.
print(time.time() - t0)

t0 = time.time()
mean_delay = air.DepDelay.mean().compute()   # This takes a while.
print(time.time() - t0)

air.DepDelay.median().compute()
```

We'll discuss in class why Dask won't do the median. Consider the discussion about moving data in the earlier section on MapReduce.

Next let's see a full split-apply-combine (aka MapReduce) type of analysis.

```python
#| eval: false
sub = air[(air.UniqueCarrier == 'UA') & (air.Origin == 'SFO')]
byDest = sub.groupby('Dest').DepDelay.mean()
results = byDest.compute()            # This takes a while too.
results
```


You should see this:

```
    Dest
    ACV 26.200000
    BFL 1.000000
    BOI 12.855069
    BOS 9.316795
    CLE 4.000000
    ...
```

Note: calling `compute` twice is a bad idea as Dask will read in the data
twice - more on this in a bit.


!!! warning "Warning"
Think carefully about the size of the result from calling `compute`. The
result will be returned as a standard Python object, not distributed across
multiple workers (and possibly machines), and with the object entirely in memory.
It's easy to accidentally return an entire giant dataset.
:::

### Dask bags

Bags are like lists but there is no particular ordering, so it doesn't
make sense to ask for the i'th element.

You can think of operations on Dask bags as being like parallel map
operations on lists in Python or R.

By default bags are handled via the `processes` scheduler.

Let's see some basic operations on a large dataset of Wikipedia log
files. You can get a subset of the Wikipedia data
[here](https://www.stat.berkeley.edu/share/paciorek/wikistats_example.tar.gz).

Here we again read the data in (which Dask will do in parallel):

```python
#| eval: false
import dask.multiprocessing
dask.config.set(scheduler='processes', num_workers = 4)
import dask.bag as db
## This is the full data
## path = '/scratch/users/paciorek/wikistats/dated_2017/'
## For demo we'll just use a small subset.
path = '/scratch/users/paciorek/wikistats/dated_2017_small/dated/'
wiki = db.read_text(path + 'part-0*gz')
```


Here we'll just count the number of records.

```python
#| eval: false
import time
t0 = time.time()
n = wiki.count().compute()
time.time() - t0   # 136 sec. for full data
```


And here is a more realistic example of filtering (subsetting).

```python
#| eval: false
import re

def find(line, regex = 'Armenia'):
    vals = line.split(' ')
    if len(vals) < 6:
        return(False)
    tmp = re.search(regex, vals[3])
    if tmp is None:
        return(False)
    else:
        return(True)


wiki.filter(find).count().compute()

armenia = wiki.filter(find)
smp = armenia.take(100)   # Grab a handful as proof of concept.
smp[0:5]
```


Note that it is quite inefficient to do the `find()` (and implicitly
read the data in) and then compute on top of that intermediate result
in two separate calls to `compute()`. Rather, we should set up the code
so that all the operations are set up before a single call to
`compute()`. This is discussed in detail in the [Dask/future tutorial](https://computing.stat.berkeley.edu/tutorial-dask-future/python-dask#63-avoid-repeated-calculations-by-embedding-tasks-within-one-call-to-compute).

Since the data are just treated as raw strings, we might want to
introduce structure by converting each line to a tuple and then
converting to a data frame.

```python
#| eval: false
def make_tuple(line):
    return(tuple(line.split(' ')))

dtypes = {'date': 'object', 'time': 'object', 'language': 'object',
'webpage': 'object', 'hits': 'float64', 'size': 'float64'}

## Let's create a Dask dataframe.
## This will take a while if done on full data.
df = armenia.map(make_tuple).to_dataframe(dtypes)
type(df)

## Now let's actually do the computation,
## returning a **Pandas** (not Dask) df to the main process.
result = df.compute()
type(result)
result[0:5]
```


### Dask arrays (numpy)

Dask arrays are numpy-like arrays where each array is split up by both
rows and columns into smaller numpy arrays.

One can do a lot of the kinds of computations that you would do on a
numpy array on a Dask array, but many operations are not possible. See
[here](http://docs.dask.org/en/latest/array-api.html).

By default arrays are handled via the `threads` scheduler.

#### Non-distributed arrays

Let's first see operations on a single node, using a single 13 GB two-dimensional
array. Again, Dask uses lazy evaluation, so creation of the array
doesn't happen until an operation requiring output is done.

```python
#| eval: false
import dask
dask.config.set(scheduler = 'threads', num_workers = 4)
import dask.array as da
x = da.random.normal(0, 1, size=(40000,40000), chunks=(10000, 10000))

---

[← 1. A few preparatory notes](02-1-a-few-preparatory-notes.md) · [Up: contents](index.md) · [square 10k x 10k chunks →](04-square-10k-x-10k-chunks.md)
