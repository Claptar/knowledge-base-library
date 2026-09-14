---
title: Unit 08 — bigData Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 08 — bigData Part 04 —

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now let’s use the mapReduce paradigm to get the aggregate statistics we want.

### map-reduce step to sum hits across date-time-language triplets ### def stratify(line): # create key-value pairs where: # key = date-time-language # value = number of website hits vals = line.split(' ') return(vals[0] + '-' + vals[1] + '-' + vals[2], int(vals[4])) # sum number of hits for each date-time-language value counts = obama.map(stratify).reduceByKey(add) # 5 minutes # 128889 for full dataset ### map step to prepare output ### def transform(vals): # split key info back into separate fields key = vals[0].split('-') return(",".join((key[0], key[1], key[2], str(vals[1])))) ### output to file ### # have one partition because one file per partition is written out outputDir = dir + '/' + 'obama-counts' counts.map(transform).repartition(1).saveAsTextFile(outputDir) # 5 sec.

#### **2.3.7 Spark monitoring**

There are various interfaces to monitor Spark and the HDFS.

- http://<master_url>:8080 – general information about the Spark cluster

16

- http://<master_url>:4040 – information about the Spark tasks being executed

- http://<master_url>:50070 – information about the HDFS

When one runs _spark-start_ on Savio, it mentions some log files. If you look in the log file for the master, you should see a line that says “Bound MasterWebUI to 0.0.0.0 and started at http://10.0.5.93:8080” that indicates what the <master_url> is (here it is 10.0.5.93). We need to connect to that URL to view the web UI.

On Savio, to view the interfaces in a web browser, you need to start a remote desktop (VNC) session, following these instructions: https://research-it.berkeley.edu/services/high-performancecomputing/using-brc-visualization-node-realvnc; I suggest using the VNC add-on to the Chrome browser. Once you have a window onto Savio in your VNC session, start a browser from the terminal windows by entering: /global/scratch/kmuriki/otterbrowser <master_url>:8080, e.g. 10.0.5.93:8080.

#### **2.3.8 Spark operations**

Let’s consider some of the core methods we used.

- _filter()_ : create a subset

- _map()_ : take an RDD and apply a function to each element, returning an RDD

- _reduce()_ and _reduceByKey()_ : take an RDD and apply a reduction operation to the elements, doing the reduction stratified by the key values for reduceByKey(). Reduction functions need to be associative (order across records doesn’t matter) and commutative (order of arguments doesn’t matter) and take 2 arguments and return 1, all so that they can be done in parallel in a straightforward way.

- _collect()_ : collect results back to the master

- _cache()_ : tell Spark to keep the RDD in memory for later use

- _repartition()_ : rework the RDD so it is divided into the specified number of partitions

Note that all of the various operations are OOP methods applied to either the SparkContext management object or to a Spark dataset, called a Resilient Distributed Dataset (RDD). Here _lines, obama,_ and _counts_ are all RDDs. However the result of _collect()_ is just a standard Python object.

17

#### **2.3.9 Nonstandard reduction**

Finding the median of a set of values is an example where we don’t have a simple commutative/associative reducer function. Instead we group all the observations for each key into a socalled iterable object. Then our second map function treats each key as an element, iterating over the observations grouped within each key.

As an example we could find the median page size by language (this is not a particularly interesting/useful computation in this dataset, but I wanted to illustrate how this would work).

import numpy as np def findShortLines(line): vals = line.split(' ') if len(vals) < 6: return(False) else: return(True)

def computeKeyValue(line): vals = line.split(' ') # key is language, val is page size return(vals[2], int(vals[5]))

def medianFun(input):

---

[← not clear if should repartition; will likely have small partitions if not](03-not-clear-if-should-repartition-will-likely-have-small-parti.md) · [Up: contents](index.md) · [Unit 08 — bigData Part 05 — →](05-unit-08-bigdata-part-05.md)
