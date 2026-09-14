---
title: 'Unit 8: Databases and Big Data'
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 8: Databases and Big Data

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

October 21, 2020

References:

- Tutorial on parallel processing using Python’s Dask and R’s future: https://github.com/berkeleyscf/tutorial-dask-future

- SCF tutorial on “Working with large datasets in SQL, R, and Python”

- Murrell: Introduction to Data Technologies

- Adler: R in a Nutshell

- Spark Programming Guide

I’ve also pulled material from a variety of other sources, some mentioned in context below.

Note that for a lot of the demo code I ran the code separately outside of _knitr_ and this document because of the time involved in working with large datasets.

## **1 A few preparatory notes**

### **1.1 An editorial on ’big data’**

Big data is trendy these days, though I guess it’s not quite the buzzword/buzzphrase that it was a few years ago.

Personally, I think some of the hype is justified and some is hype. Large datasets allow us to address questions that we can’t with smaller datasets, and they allow us to consider more sophisticated (e.g., nonlinear) relationships than we might with a small dataset. But they do not directly help with the problem of correlation not being causation. Having medical data on every American still doesn’t tell me if higher salt intake causes hypertension. Internet transaction data does not tell me if one website feature causes increased viewership or sales. One either needs to carry out a

1

designed experiment or think carefully about how to infer causation from observational data. Nor does big data help with the problem that an ad hoc ’sample’ is not a statistical sample and does not provide the ability to directly infer properties of a population. A well-chosen smaller dataset may be much more informative than a much larger, more ad hoc dataset. However, having big datasets might allow you to select from the dataset in a way that helps get at causation or in a way that allows you to construct a population-representative sample. Finally, having a big dataset also allows you to do a large number of statistical analyses and tests, so multiple testing is a big issue. With enough analyses, something will look interesting just by chance in the noise of the data, even if there is no underlying reality to it.

Here’s a different way to summarize it.

Different people define the ’big’ in big data differently. One definition involves the actual size of the data, and in some cases the speed with which it is collected. Our efforts here will focus on dataset sizes that are large for traditional statistical work but would probably not be thought of as large in some contexts such as Google or the US National Security Agency (NSA). Another definition of ’big data’ has more to do with how pervasive data and empirical analyses backed by data are in society and not necessarily how large the actual dataset size is.

### **1.2 Logistics and data size**

One of the main drawbacks with R in working with big data is that all objects are stored in memory, so you can’t directly work with datasets that are more than 1-20 Gb or so, depending on the memory on your machine.

The techniques and tools discussed in this Unit (apart from the section on MapReduce/Spark) are designed for datasets in the range of gigabytes to tens of gigabytes, though they may scale to larger if you have a machine with a lot of memory or simply have enough disk space and are willing to wait. If you have 10s of gigabytes of data, you’ll be better off if your machine has 10s of GBs of memory, as discussed in this Unit.

If you’re scaling to 100s of GBs, terabytes or petabytes, tools such as carefully-administered databases and Spark are probably your best bet.

Note: in handling big data files, it’s best to have the data on the local disk of the machine you are using to reduce traffic and delays from moving data over the network.

### **1.3 What we already know about handling big data!**

UNIX operations are generally very fast, so if you can manipulate your data via UNIX commands and piping, that will allow you to do a lot. We’ve already seen UNIX commands for extracting columns. And various commands such as _grep_ , _head_ , _tail_ , etc. allow you to pick out rows based

2

on certain criteria. As some of you have done in problem sets, one can use _awk_ to extract rows. So basic shell scripting may allow you to reduce your data to a more manageable size.

And don’t forget simple things. If you have a dataset with 30 columns that takes up 10 Gb but you only need 5 of the columns, get rid of the rest and work with the smaller dataset. Or you might be able to get the same information from a random sample of your large dataset as you would from doing the analysis on the full dataset. Strategies like this will often allow you to stick with the tools you already know.

Also, remember that we can often store data more compactly in binary formats than in flat text (e.g., csv) files.

Finally, for many applications, storing large datasets in a standard database will work well. We’ll see databases later in this Unit.

## **2 Hadoop, MapReduce, Spark, and Dask**

Traditionally, high-performance computing (HPC) has concentrated on techniques and tools for message passing such as MPI and on developing efficient algorithms to use these techniques. In the last 20 years, focus has shifted to technologies for processing large datasets that are distributed across multiple machines, but can be manipulated as if they are one dataset.

Two commonly-used tools for doing this are Spark and Python’s Dask package. We’ll cover Dask.

### **2.1 Overview**

A basic paradigm for working with big datasets is the _MapReduce_ paradigm. The basic idea is to store the data in a distributed fashion across multiple nodes and try to do the computation in pieces on the data on each node. Results can also be stored in a distributed fashion.

A key benefit of this is that if you can’t fit your dataset on disk on one machine you can on a cluster of machines. And your processing of the dataset can happen in parallel. This is the basic idea of _MapReduce_ .

The basic steps of _MapReduce_ are as follows:

- read individual data objects (e.g., records/lines from CSVs or individual data files)

- map: create key-value pairs using the inputs (more formally, the map step takes a key-value pair and returns a new key-value pair)

- reduce - for each key, do an operation on the associated values and create a result - i.e., aggregate within the values assigned to each key

3

#### • write out the {key,result} pair

A similar paradigm that is implemented in _dplyr_ is the split-apply-combine strategy (http://www.jstatsoft.org/v40/i01/paper

A few additional comments. In our map function, we could exclude values or transform them in some way, including producing multiple records from a single record. And in our reduce function, we can do more complicated analysis. So one can actually do fairly sophisticated things within what may seem like a restrictive paradigm. But we are constrained such that in the map step, each record needs to be treated independently and in the reduce step each key needs to be treated independently. This allows for the parallelization.

**One important note is that any operations that require moving a lot of data between the workers can take a long time.** (This is sometimes called a _shuffle_ .) This could happen if, for example, you computed the median value within each of many groups if the data for each group are spread across the workers. In contrast, if we compute the mean or sum, one can compute the partial sums on each worker and then just add up the partial sums.

Note that the idea of concepts of map and reduce are core concepts in functional programming (and that we said R was a functional programming language). The various _lapply/sapply/apply_ commands are base R’s version of a map operation.

_Hadoop_ is an infrastructure for enabling MapReduce across a network of machines. The basic idea is to hide the complexity of distributing the calculations and collecting results. Hadoop includes a file system for distributed storage (HDFS), where each piece of information is stored redundantly (on multiple machines). Calculations can then be done in a parallel fashion, often on data in place on each machine thereby limiting the amount of communication that has to be done over the network. Hadoop also monitors completion of tasks and if a node fails, it will redo the relevant tasks on another node. Hadoop is based on Java. Given the popularity of Spark, I’m not sure how much usage these approaches currently see. Setting up a Hadoop cluster can be tricky. Hopefully if you’re in a position to need to use Hadoop, it will be set up for you and you will be interacting with it as a user/data analyst.

Ok, so what is Spark? You can think of Spark as in-memory Hadoop. Spark allows one to treat the memory across multiple nodes as a big pool of memory. So just as _data.table_ was faster than _ff_ because we kept everything in memory, Spark should be faster than Hadoop when the data will fit in the collective memory of multiple nodes. In cases where it does not, Spark will make use of the HDFS (and generally, Spark will be reading the data initially from HDFS.) While Spark is more user-friendly than Hadoop, there are also some things that can make it hard to use. Setting up a Spark cluster also involves a bit of work, Spark can be hard to configure for optimal performance, and Spark calculations have a tendency to fail (often involving memory issues) in ways that are hard for users to debug.

4

### **2.2 Using Dask for big data processing**

Unit 7 on parallelization gives an overview of using Dask in similar fashion to how we used R’s _future_ package for flexible parallelization on different kinds of computational resources (in particular, parallelizing across multiple cores on one machine versus parallelizing across multiple cores across multiple machines/ndoes).

Here we’ll see the use of Dask to work with distributed datasets. Dask can process datasets (potentially very large ones) by parallelizing operations across subsets of the data using multiple cores on one or more machines.

Like Spark, Dask automatically reads data from files in parallel and operates on chunks (also called partitions or shards) of the full dataset in parallel. There are two big advantages of this:

- You can do calculations (including reading from disk) in parallel because each worker will work on a piece of the data.

- When the data is split across machines, you can use the memory of multiple machines to handle much larger datasets than would be possible in memory on one machine. That said, Dask processes the data in chunks, so one often doesn’t need a lot of memory, even just on one machine.

While reading from disk in parallel is a good goal, if all the data are on one hard drive, there are limitations on the speed of reading the data from disk because of having multiple processes all trying to access the disk at once. Supercomputing systems will generally have parallel file systems that support truly parallel reading (and writing, i.e., _parallel I/O_ ). Hadoop/Spark deal with this by distributing across multiple disks, generally one disk per machine/node.

Because computations are done in external compiled code (e.g., via _numpy_ ) it’s effective to use the threaded scheduler when operating on one node to avoid having to copy and move the data.

#### **2.2.1 Dask dataframes (pandas)**

Dask dataframes are Pandas-like dataframes where each dataframe is split into groups of rows, stored as smaller Pandas dataframes.

One can do a lot of the kinds of computations that you would do on a Pandas dataframe on a Dask dataframe, but many operations are not possible. See here.

By default dataframes are handled by the _threads_ scheduler.

Here’s an example of reading from a dataset of flight delays (about 11 GB data). You can get the data here.

5

import dask dask.config.set(scheduler='threads', num_workers = 4) import dask.dataframe as ddf path = '/scratch/users/paciorek/243/AirlineData/csvs/' air = ddf.read_csv(path + '*.csv.bz2', compression = 'bz2', encoding = 'latin1', # (unexpected) latin1 value(s) in TailNum field dtype = {'Distance': 'float64', 'CRSElapsedTime': 'float64', 'TailNum': 'object', 'CancellationCode': 'object'}) # specify dtypes so Pandas doesn't complain about column type heterogeneity air

Dask will reads the data in parallel from the various .csv.bz2 files (unzipping on the fly), but note the caveat in the previous section about the possibilities for truly parallel I/O.

However, recall delayed evaluation in Dask – the reading is delayed until _compute()_ is called. For that matter, the various other calculations (max, groupby, mean) are only done after _compute()_ is called.

air.DepDelay.max().compute() # this takes a while sub = air[(air.UniqueCarrier == 'UA') & (air.Origin == 'SFO')] byDest = sub.groupby('Dest').DepDelay.mean() byDest.compute() # this takes a while too

You should see this:

Dest ACV 26.200000 BFL 1.000000 BOI 12.855069 BOS 9.316795 CLE 4.000000

Note: calling compute twice is a bad idea as Dask will read in the data twice - see the end of Section 2.3.2 for more discussion.

6

#### **2.2.2 Dask bags**

Bags are like lists but there is no particular ordering, so it doesn’t make sense to ask for the i’th element.

You can think of operations on Dask bags as being like parallel map operations on lists in Python or R.

By default bags are handled via the _multiprocessing_ scheduler.

Let’s see some basic operations on a large dataset of Wikipedia log files. You can get a subset of the Wikipedia data here.

Here we again read the data in (which Dask will do in parallel):

import dask.multiprocessing dask.config.set(scheduler='processes', num_workers = 4) # multiprocessing import dask.bag as db ## This is the full data ## path = '/scratch/users/paciorek/wikistats/dated_2017/' ## For demo we'll just use a small subset path = '/scratch/users/paciorek/wikistats/dated_2017_small/dated/' wiki = db.read_text(path + 'part-0000*gz')

Here we’ll just count the number of records.

import time t0 = time.time() wiki.count().compute() time.time() - t0 # 136 sec. for full data

And here is a more realistic example of filtering (subsetting).

import re def find(line, regex = 'Armenia'): vals = line.split(' ') if len(vals) < 6: return(False) tmp = re.search(regex, vals[3]) if tmp is None: return(False) else:

7

return(True)

wiki.filter(find).count().compute() armenia = wiki.filter(find) smp = armenia.take(100) ## grab a handful as proof of concept smp[0:5]

Note that it is quite inefficient to do the _find()_ (and implicitly reading the data in) and then compute on top of that intermediate result in two separate calls to _compute()_ . Rather, we should set up the code so that all the operations are set up before a single call to _compute()_ . More on this in Section 6 of the Dask content in the Dask/future tutorial.

Since the data are just treated as raw strings, we might want to introduce structure by converting each line to a tuple and then converting to a data frame.

def make_tuple(line): return(tuple(line.split(' ')))

dtypes = {'date': 'object', 'time': 'object', 'language': 'object', 'webpage': 'object', 'hits': 'float64', 'size': 'float64'} ## Let's create a Dask dataframe. ## This will take a while if done on full data. df = armenia.map(make_tuple).to_dataframe(dtypes) type(df) ## Now let's actually do the computation, returning a Pandas df result = df.compute() type(result) result.head()

#### **2.2.3 Dask arrays (numpy)**

Dask arrays are numpy-like arrays where each array is split up by both rows and columns into smaller numpy arrays.

One can do a lot of the kinds of computations that you would do on a numpy array on a Dask array, but many operations are not possible. See here.

8

By default arrays are handled via the _threads_ scheduler.

**Non-distributed arrays** Let’s first see operations on a single node, using a single 13 GB 2-d array. Again, Dask uses lazy evaluation, so creation of the array doesn’t happen until an operation requiring output is done.

import dask dask.config.set(scheduler = 'threads', num_workers = 4) import dask.array as da x = da.random.normal(0, 1, size=(40000,40000), chunks=(10000, 10000)) # square 10k x 10k chunks mycalc = da.mean(x, axis = 1) # by row import time t0 = time.time() rs = mycalc.compute() time.time() - t0 # 41 sec.

For a row-based operation, we would presumably only want to chunk things up by row, but this doesn’t seem to actually make a difference, presumably because the mean calculation can be done in pieces and only a small number of summary statistics moved between workers.

import dask dask.config.set(scheduler='threads', num_workers = 4) import dask.array as da # x = da.from_array(x, chunks=(2500, 40000)) # adjust chunk size of existing x = da.random.normal(0, 1, size=(40000,40000), chunks=(2500, 40000)) mycalc = da.mean(x, axis = 1) # row means import time t0 = time.time() rs = mycalc.compute() time.time() - t0 # 42 sec.

Of course, given the lazy evaluation, this timing comparison is not just timing the actual row mean calculations.

But this doesn’t really clarify the story...

9

import dask dask.config.set(scheduler='threads', num_workers = 4) import dask.array as da import numpy as np import time t0 = time.time() x = np.random.normal(0, 1, size=(40000,40000)) time.time() - t0 # 110 sec. # for some reason the from_array and da.mean calculations are not done lazily t0 = time.time() dx = da.from_array(x, chunks=(2500, 40000)) time.time() - t0 # 27 sec. t0 = time.time() mycalc = da.mean(x, axis = 1) # what is this doing given .compute() also time.time() - t0 # 28 sec. t0 = time.time() rs = mycalc.compute() time.time() - t0 # 21 sec.

Dask will avoid storing all the chunks in memory. (It appears to just generate them on the fly.) Here we have an 80 GB array but we never use more than a few GB of memory (based on ‘top‘ or ‘free -h‘).

import dask dask.config.set(scheduler='threads', num_workers = 4) import dask.array as da x = da.random.normal(0, 1, size=(100000,100000), chunks=(10000, 10000)) mycalc = da.mean(x, axis = 1) # row means import time t0 = time.time() rs = mycalc.compute() time.time() - t0 # 205 sec. rs[0:5]

**Distributed arrays** This should be straightforward based on using Dask distributed. However, one would want to be careful about creating arrays by distributing the data from a single Python

10

process as that would involve copying between machines.

### **2.3 Spark (optional)**

Note for 2020: in past years we covered the use of Spark for processing big datasets. This year we’ll cover similar functionality in Python’s Dask package. I’ve kept this section (and related code in the code files) in case anyone is interested in learning more about Spark, but we won’t cover it in class this year.

#### **2.3.1 Overview**

We’ll focus on Spark rather than Hadoop for the speed reasons described above and because I think Spark provides a nicer environment/interface in which to work. Plus it comes out of the (former) AmpLab here at Berkeley. We’ll start with the Python interface to Spark and then see a bit of the _sparklyr_ R package for interfacing with Spark.

More details on Spark are in the Spark programming guide. Some key aspects of Spark:

- Spark can read/write from various locations, but a standard location is the HDFS, with read/write done in parallel across the cores of the Spark cluster.

- The basic data structure in Spark is a _Resilient Distributed Dataset (RDD)_ , which is basically a distributed dataset of individual units, often individual rows loaded from text files.

- RDDs are stored in chunks called _partitions_ , stored on the different nodes of the cluster (either in memory or if necessary on disk).

- Spark has a core set of methods that can be applied to RDDs to do operations such as filtering/subsetting, transformation/mapping, reduction, and others.

- The operations are done in parallel on the different partitions of the data

- Some operations such as reduction generally involve a _shuffle_ , moving data between nodes of the cluster. This is costly.

- Recent versions of Spark have a distributed _DataFrame_ data structure and the ability to run SQL queries on the data.

Question: what do you think are the tradeoffs involved in determining the number of partitions to use?

Note that some headaches with Spark include:

11

- whether and how to set the amount of memory available for Spark workers (executor memory) and the Spark master process (driver memory)

- hard-to-diagnose failures (including out-of-memory issues)

#### **2.3.2 Getting started**

We’ll use Spark on Savio. You can also use Spark on NSF’s XSEDE Bridges supercomputer (among other XSEDE resources), and via commercial cloud computing providers, as well as on your laptop (but obviously only to experiment with small datasets). The demo works with a dataset of Wikipedia traffic, ~110 GB of zipped data (~500 GB unzipped) from October-December 2008, though for in-class presentation we’ll work with a much smaller set of 1 day of data.

The Wikipedia traffic are available through Amazon Web Services storage. The steps to get it

are:

1. Start an AWS EC2 virtual machine that mounts the data onto the VM

2. Install Globus on the VM

3. Transfer the data to Savio via Globus

Details on how I did this are in _get_wikipedia_data.sh_ . The resulting data are available to you in _/global/scratch/paciorek/wikistats_full/raw_ on Savio.

#### **2.3.3 Storing data for use in Spark**

In many Spark contexts, the data would be stored in a distributed fashion across the hard drives attached to different nodes of a cluster (i.e., in the HDFS).

On Savio, Spark is set up to just use the scratch file system, so one would NOT run the code here, but I’m including it to give a sense for what it’s like to work with HDFS. First we would need to get the data from the standard filesystem to the HDFS. Note that the file system commands are like standard UNIX commands, but you need to do hadoop fs in front of the command.

## DO NOT RUN THIS CODE ON SAVIO ## ## data for Spark on Savio is stored in scratch ##

hadoop fs -ls / hadoop fs -ls /user hadoop fs -mkdir /user/paciorek/data hadoop fs -mkdir /user/paciorek/data/wikistats

12

hadoop fs -mkdir /user/paciorek/data/wikistats/raw hadoop fs -mkdir /user/paciorek/data/wikistats/dated hadoop fs -copyFromLocal /global/scratch/paciorek/wikistats/raw/* \ /user/paciorek/data/wikistats/raw # check files on the HDFS, e.g.: hadoop fs -ls /user/paciorek/data/wikistats/raw ## now do some processing with Spark, e.g., preprocess.{sh,py} # after processing can retrieve data from HDFS as needed hadoop fs -copyToLocal /user/paciorek/data/wikistats/dated .

#### **2.3.4 Using Spark on Savio**

Here are the steps to use Spark on Savio. We’ll demo using an interactive job (the _srun_ line here) but one could include the last three commands in the SLURM job script.

tmux new -s spark ## to get back in if disconnected: tmux a -t spark ## having some trouble with ic_stat243 and 4 nodes; check again srun -A ic_stat243 -p savio2 --nodes=4 -t 1:00:00 --pty bash module load java spark/2.1.0 python/3.5 source /global/home/groups/allhands/bin/spark_helper.sh spark-start ## note the environment variables created env | grep SPARK spark-submit --master $SPARK_URL $SPARK_DIR/examples/src/main/python/pi.py

First we’ll load Python; then we can use Spark via the Python interface interactively. We’ll see how to submit batch jobs later.

13

---

[Up: contents](index.md) · [Unit 08 — bigData Part 02 — →](02-unit-08-bigdata-part-02.md)
