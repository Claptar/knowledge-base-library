---
title: Unit 08 — bigData Part 02 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 08 — bigData Part 02 —

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **2.3.5 Preprocessing the Wikipedia traffic data**

At this point, one complication is that the date-time information on the Wikipedia traffic is embedded in the file names. We’d like that information to be fields in the data files. This is done by running the code in _preprocess_wikipedia.py_ in the Python interface to Spark (pyspark). Note that trying to use multiple nodes and to repartition in various ways caused various errors I was unable to diagnose, but the code as is should work albeit somewhat slowly. The resulting data are available to you in _/global/scratch/paciorek/wikistats_full/dated_ . These are the data you will use for PS6.

In principle one could run _preprocess_wikipedia.py_ as a batch submission, but I was having problems getting that to run successfully.

#### **2.3.6 Spark in action: processing the Wikipedia traffic data**

Now we’ll do some basic manipulations with the Wikipedia dataset, with the goal of analyzing traffic to Barack Obama’s sites during the time around his election as president in 2008. Here are the steps we’ll follow:

- Count the number of lines/observations in our dataset.

- Filter to get only the Barack Obama sites.

- Map step that creates key-value pairs from each record/observation/row.

- Reduce step that counts the number of views by hour and language, so hour-day-lang will serve as the key.

- Map step to prepare the data so it can be output in a nice format.

Note that Spark uses _lazy evaluation_ . Actual computation only happens when one asks for a result to be returned or output written to disk.

First we’ll see how we read in the data and filter to the observations (lines / rows) of interest.

dir = '/global/scratch/paciorek/wikistats'

### read data and do some checks ###

14

## 'sc' is the SparkContext management object, created via PySpark ## if you simply start Python, without invoking PySpark, ## you would need to create the SparkContext object yourself lines = sc.textFile(dir + '/' + 'dated') lines.getNumPartitions() # 16800 (480 input files) for full dataset # note delayed evaluation lines.count() # 9467817626 for full dataset # watch the UI and watch wwall as computation progresses testLines = lines.take(10) testLines[0] testLines[9] ### filter to sites of interest ### import re from operator import add def find(line, regex = "Barack_Obama", language = None): vals = line.split(' ') if len(vals) < 6: return(False) tmp = re.search(regex, vals[3]) if tmp is None or (language != None and vals[2] != language): return(False) else: return(True) lines.filter(find).take(100) # pretty quick

---

[← Unit 8: Databases and Big Data](01-unit-8-databases-and-big-data.md) · [Up: contents](index.md) · [not clear if should repartition; will likely have small partitions if not →](03-not-clear-if-should-repartition-will-likely-have-small-parti.md)
