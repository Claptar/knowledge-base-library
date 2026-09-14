---
title: specify dtypes so Pandas doesn't complain about column type heterogeneity
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# specify dtypes so Pandas doesn't complain about column type heterogeneity

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

air
```


Dask will reads the data in parallel from the various .csv.bz2 files
(unzipping on the fly), but note the caveat in the previous section
about the possibilities for truly parallel I/O.

However, recall that Dask uses delayed evaluation. In this case, the reading is delayed until
`compute()` is called. For that matter, the various other calculations
(`max`, `groupby`, `mean`) shown below are only done after `compute()` is called.

```python
air.DepDelay.max().compute()   # this takes a while
sub = air[(air.UniqueCarrier == 'UA') & (air.Origin == 'SFO')]
byDest = sub.groupby('Dest').DepDelay.mean()
byDest.compute()               # this takes a while too
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

Note: calling compute twice is a bad idea as Dask will read in the data
twice - more on this in a bit.

### Dask bags

Bags are like lists but there is no particular ordering, so it doesn't
make sense to ask for the i'th element.

You can think of operations on Dask bags as being like parallel map
operations on lists in Python or R.

By default bags are handled via the `multiprocessing` scheduler.

Let's see some basic operations on a large dataset of Wikipedia log
files. You can get a subset of the Wikipedia data
[here](https://www.stat.berkeley.edu/share/paciorek/wikistats_example.tar.gz).

Here we again read the data in (which Dask will do in parallel):

```python
import dask.multiprocessing
dask.config.set(scheduler='processes', num_workers = 4)
import dask.bag as db
## This is the full data
## path = '/scratch/users/paciorek/wikistats/dated_2017/'
## For demo we'll just use a small subset
path = '/scratch/users/paciorek/wikistats/dated_2017_small/dated/'
wiki = db.read_text(path + 'part-0000*gz')
```


Here we'll just count the number of records.

```python
import time
t0 = time.time()
wiki.count().compute()
time.time() - t0   # 136 sec. for full data
```


And here is a more realistic example of filtering (subsetting).

```python
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
`compute()`. More on this the [Dask/future tutorial](https://berkeley-scf.github.io/tutorial-dask-future/python-dask#63-avoid-repeated-calculations-by-embedding-tasks-within-one-call-to-compute)

Since the data are just treated as raw strings, we might want to
introduce structure by converting each line to a tuple and then
converting to a data frame.

```python
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
result.head()
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
import dask
dask.config.set(scheduler = 'threads', num_workers = 4)
import dask.array as da
x = da.random.normal(0, 1, size=(40000,40000), chunks=(10000, 10000))

---

[← 2. MapReduce, Dask, Hadoop, and Spark](03-2-mapreduce-dask-hadoop-and-spark.md) · [Up: contents](index.md) · [square 10k x 10k chunks →](05-square-10k-x-10k-chunks.md)
