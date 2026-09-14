---
title: specify some dtypes so Pandas doesn't complain about column type heterogeneity
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit7-bigData.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# specify some dtypes so Pandas doesn't complain about column type heterogeneity

**Source:** [`units/unit7-bigData.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit7-bigData.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

air
```

Dask will reads the data in parallel from the various .csv.bz2 files
(unzipping on the fly), but note the caveat in the previous section
about the possibilities for truly parallel I/O.

However, recall that Dask uses delayed evaluation. In this case, the reading is delayed until
`compute()` is called. For that matter, the various other calculations
(`max`, `groupby`, `mean`) shown below are only done after `compute()` is called.

```python
#| eval: false
import time

t0 = time.time()
air.DepDelay.max().compute()   # this takes a while
print(time.time() - t0)

t0 = time.time()
air.DepDelay.mean().compute()   # this takes a while
print(time.time() - t0)

air.DepDelay.median().compute()
```

We'll discuss in class why Dask won't do the median. Consider the discussion about moving data in the earlier section on MapReduce.

Next let's see a full split-apply-combine (aka MapReduce) type of analysis.

```python
#| eval: false
sub = air[(air.UniqueCarrier == 'UA') & (air.Origin == 'SFO')]
byDest = sub.groupby('Dest').DepDelay.mean()
results = byDest.compute()            # this takes a while too
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

> **Warning**
> Think carefully about the size of the result from calling `compute`. The
> result will be returned as a standard Python object, not distributed across
> multiple workers (and possibly machines), and with the object entirely in memory.
> It's easy to accidentally return an entire giant dataset.


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
## For demo we'll just use a small subset
path = '/scratch/users/paciorek/wikistats/dated_2017_small/dated/'
wiki = db.read_text(path + 'part-0*gz')
```


Here we'll just count the number of records.

```python
#| eval: false
import time
t0 = time.time()
wiki.count().compute()
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
smp = armenia.take(100) ## grab a handful as proof of concept
smp[0:5]
```


Note that it is quite inefficient to do the `find()` (and implicitly
reading the data in) and then compute on top of that intermediate result
in two separate calls to `compute()`. Rather, we should set up the code
so that all the operations are set up before a single call to
`compute()`. This is discussed in detail in the [Dask/future tutorial](https://berkeley-scf.github.io/tutorial-dask-future/python-dask#63-avoid-repeated-calculations-by-embedding-tasks-within-one-call-to-compute).

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

## Now let's actually do the computation, returning a Pandas df
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

[← 2. MapReduce, Dask, Hadoop, and Spark](03-2-mapreduce-dask-hadoop-and-spark.md) · [Up: contents](index.md) · [square 10k x 10k chunks →](05-square-10k-x-10k-chunks.md)
