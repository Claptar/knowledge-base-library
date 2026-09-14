---
title: 'Unit 8: Databases and Big Data'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 8: Databases and Big Data

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

October 24, 2019

References:

- Tutorial on parallel processing using Python’s Dask and R’s future: https://github.com/berkeleyscf/tutorial-dask-future

- Spark Programming Guide

- SCF tutorial on “Working with large datasets in SQL, R, and Python”

- Murrell: Introduction to Data Technologies

- Adler: R in a Nutshell

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

If you’re scaling to 100s of GBs, terabytes or petabytes, tools such as Spark may be your best bet, or possibly carefully-administered databases.

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

- write out the {key,result} pair

A similar paradigm that is implemented in _dplyr_ is the split-apply-combine strategy (http://www.jstatsoft.org/v40/i01/paper A few additional comments. In our map function, we could exclude values or transform them in some way, including producing multiple records from a single record. And in our reduce function, we can do more complicated analysis. So one can actually do fairly sophisticated things within what may seem like a restrictive paradigm. But we are constrained such that in the map step, each record needs to be treated independently and in the reduce step each key needs to be treated independently. This allows for the parallelization.

Note that the idea of concepts of map and reduce are core concepts in functional programming (and that we said R was a functional programming language). The various _lapply/sapply/apply_ commands are base R’s version of a map operation.

_Hadoop_ is an infrastructure for enabling MapReduce across a network of machines. The basic idea is to hide the complexity of distributing the calculations and collecting results. Hadoop includes a file system for distributed storage (HDFS), where each piece of information is stored redundantly (on multiple machines). Calculations can then be done in a parallel fashion, often on data in place on each machine thereby limiting the amount of communication that has to be done over the network. Hadoop also monitors completion of tasks and if a node fails, it will redo the relevant tasks on another node. Hadoop is based on Java. Given the popularity of Spark, I’m not sure how much usage these approaches currently see. Setting up a Hadoop cluster can be tricky. Hopefully if you’re in a position to need to use Hadoop, it will be set up for you and you will be interacting with it as a user/data analyst.

Ok, so what is Spark? You can think of Spark as in-memory Hadoop. Spark allows one to treat the memory across multiple nodes as a big pool of memory. So just as _data.table_ was faster than _ff_ because we kept everything in memory, Spark should be faster than Hadoop when the data will fit in the collective memory of multiple nodes. In cases where it does not, Spark will make use of the HDFS (and generally, Spark will be reading the data initially from HDFS.) While Spark is more user-friendly than Hadoop, there are also some things that can make it hard to use. Setting up a Spark cluster also involves a bit of work, Spark can be hard to configure for optimal performance, and Spark calculations have a tendency to fail (often involving memory issues) in ways that are hard for users to debug.

### **2.2 Spark**

Note for 2019: in past years we covered the use of Spark for processing big datasets. This year we’ll cover similar functionality in Python’s Dask package. I’ve kept this section in case anyone is interested in learning more about Spark, but we won’t cover it in class this year.

4

#### **2.2.1 Overview**

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

- whether and how to set the amount of memory available for Spark workers (executor memory) and the Spark master process (driver memory)

- hard-to-diagnose failures (including out-of-memory issues)

#### **2.2.2 Getting started**

We’ll use Spark on Savio. You can also use Spark on NSF’s XSEDE Bridges supercomputer (among other XSEDE resources), and via commercial cloud computing providers, as well as on

5

your laptop (but obviously only to experiment with small datasets). The demo works with a dataset of Wikipedia traffic, ~110 GB of zipped data (~500 GB unzipped) from October-December 2008, though for in-class presentation we’ll work with a much smaller set of 1 day of data.

The Wikipedia traffic are available through Amazon Web Services storage. The steps to get it

are:

1. Start an AWS EC2 virtual machine that mounts the data onto the VM

2. Install Globus on the VM

3. Transfer the data to Savio via Globus

Details on how I did this are in _get_wikipedia_data.sh_ . The resulting data are available to you in _/global/scratch/paciorek/wikistats_full/raw_ on Savio.

#### **2.2.3 Storing data for use in Spark**

In many Spark contexts, the data would be stored in a distributed fashion across the hard drives attached to different nodes of a cluster (i.e., in the HDFS).

On Savio, Spark is set up to just use the scratch file system, so one would NOT run the code here, but I’m including it to give a sense for what it’s like to work with HDFS. First we would need to get the data from the standard filesystem to the HDFS. Note that the file system commands are like standard UNIX commands, but you need to do hadoop fs in front of the command.

## DO NOT RUN THIS CODE ON SAVIO ## ## data for Spark on Savio is stored in scratch ##

hadoop fs -ls / hadoop fs -ls /user hadoop fs -mkdir /user/paciorek/data hadoop fs -mkdir /user/paciorek/data/wikistats hadoop fs -mkdir /user/paciorek/data/wikistats/raw hadoop fs -mkdir /user/paciorek/data/wikistats/dated

hadoop fs -copyFromLocal /global/scratch/paciorek/wikistats/raw/* \ /user/paciorek/data/wikistats/raw

---

[Up: contents](index.md) · [check files on the HDFS, e.g.: hadoop fs -ls /user/paciorek/data/wikistats/raw →](02-check-files-on-the-hdfs-e-g-hadoop-fs--ls-user-paciorek-data.md)
