---
title: for some reason the fromarray and da.mean calculations are not done lazily
  here
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# for some reason the fromarray and da.mean calculations are not done lazily here

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

t0 = time.time()
dx = da.from_array(x, chunks=(2500, 40000))
time.time() - t0   # 27 sec.
t0 = time.time()
mycalc = da.mean(x, axis = 1)  # what is this doing given .compute() also takes time?
time.time() - t0   # 28 sec.
t0 = time.time()
rs = mycalc.compute()
time.time() - t0   # 21 sec.
```


Dask will avoid storing all the chunks in memory. (It appears to just
generate them on the fly.) Here we have an 80 GB array but we never use
more than a few GB of memory (based on `top` or `free -h`).

```python
import dask
dask.config.set(scheduler='threads', num_workers = 4)
import dask.array as da
x = da.random.normal(0, 1, size=(100000,100000), chunks=(10000, 10000))
mycalc = da.mean(x, axis = 1)  # row means
import time
t0 = time.time()
rs = mycalc.compute()
time.time() - t0   # 205 sec.
rs[0:5]
```


#### Distributed arrays

Using arrays distributed across multiple machines should be straightforward based on using *Dask distributed*. However,
one would want to be careful about creating arrays by distributing the
data from a single Python process as that would involve copying between
machines.

## Spark (optional)

Note for 2019-2022: in past years we covered the use of Spark for
processing big datasets. This year we'll cover similar functionality in
Python's Dask package. I've kept this section (and related code in the
code files) in case anyone is interested in learning more about Spark,
but we won't cover it in class this year.

### Overview

We'll focus on Spark rather than Hadoop for the speed reasons described
above and because I think Spark provides a nicer environment/interface
in which to work. Plus it comes out of the (former) AmpLab here at
Berkeley. We'll start with the Python interface to Spark and then see a
bit of the *sparklyr* R package for interfacing with Spark.

More details on Spark are in the [Spark programming
guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html).

Some key aspects of Spark:

-   Spark can read/write from various locations, but a standard location
    is the HDFS, with read/write done in parallel across the cores of
    the Spark cluster.
-   The basic data structure in Spark is a *Resilient Distributed
    Dataset (RDD)*, which is basically a distributed dataset of
    individual units, often individual rows loaded from text files.
-   RDDs are stored in chunks called *partitions*, stored on the
    different nodes of the cluster (either in memory or if necessary on
    disk).
-   Spark has a core set of methods that can be applied to RDDs to do
    operations such as filtering/subsetting, transformation/mapping,
    reduction, and others.
-   The operations are done in parallel on the different partitions of
    the data
-   Some operations such as reduction generally involve a *shuffle*,
    moving data between nodes of the cluster. This is costly.
-   Recent versions of Spark have a distributed *DataFrame* data
    structure and the ability to run SQL queries on the data.

Question: what do you think are the tradeoffs involved in determining
the number of partitions to use?

Note that some headaches with Spark include:

-   whether and how to set the amount of memory available for Spark
    workers (executor memory) and the Spark master process (driver
    memory)
-   hard-to-diagnose failures (including out-of-memory issues)

### Getting started

We'll use Spark on Savio. You can also use Spark on NSF's XSEDE Bridges
supercomputer (among other XSEDE resources), and via commercial cloud
computing providers, as well as on your laptop (but obviously only to
experiment with small datasets). The demo works with a dataset of
Wikipedia traffic, ~110 GB of zipped data (~500 GB unzipped) from
October-December 2008, though for in-class presentation we'll work with
a much smaller set of 1 day of data.

The Wikipedia traffic are available through Amazon Web Services storage.
The steps to get it are:

1. Start an AWS EC2 virtual machine that mounts the data onto the VM
2. Install Globus on the VM
3. Transfer the data to Savio via Globus

Details on how I did this are in `get_wikipedia_data.sh`. The resulting
data are available to you in `/global/scratch/paciorek/wikistats_full/raw` on Savio.

### Storing data for use in Spark

In many Spark contexts, the data would be stored in a distributed
fashion across the hard drives attached to different nodes of a cluster
(i.e., in the HDFS).

On Savio, Spark is set up to just use the scratch file system, so one
would NOT run the code here, but I'm including it to give a sense for
what it's like to work with HDFS. First we would need to get the data
from the standard filesystem to the HDFS. Note that the file system
commands are like standard UNIX commands, but you need to do `hadoop fs`
in front of the command.

```bash
## DO NOT RUN THIS CODE ON SAVIO ##
## data for Spark on Savio is stored in scratch ##

hadoop fs -ls /
hadoop fs -ls /user
hadoop fs -mkdir /user/paciorek/data
hadoop fs -mkdir /user/paciorek/data/wikistats
hadoop fs -mkdir /user/paciorek/data/wikistats/raw
hadoop fs -mkdir /user/paciorek/data/wikistats/dated

hadoop fs -copyFromLocal /global/scratch/paciorek/wikistats/raw/* \
       /user/paciorek/data/wikistats/raw

---

[← x = da.fromarray(x, chunks=(2500, 40000)) # adjust chunk size of existing array](06-x-da-fromarray-x-chunks-2500-40000-adjust-chunk-size-of-exis.md) · [Up: contents](index.md) · [check files on the HDFS, e.g. →](08-check-files-on-the-hdfs-e-g.md)
