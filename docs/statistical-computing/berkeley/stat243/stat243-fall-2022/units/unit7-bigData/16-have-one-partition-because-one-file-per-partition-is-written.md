---
title: have one partition because one file per partition is written out
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# have one partition because one file per partition is written out

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

outputDir = dir + '/' + 'obama-counts'
counts.map(transform).repartition(1).saveAsTextFile(outputDir) # 5 sec.
```

### Spark monitoring

There are various interfaces to monitor Spark and the HDFS.

-   `http://<master_url>:8080` general information about the Spark
    cluster
-   `http://<master_url>:4040` information about the Spark tasks being
    executed
-   `http://<master_url>:50070` information about the HDFS

When one runs `spark-start` on Savio, it mentions some log files. If you
look in the log file for the master, you should see a line that says
"Bound MasterWebUI to 0.0.0.0 and started at http://10.0.5.93:8080" that
indicates what the `<master_url>` is (here it is `10.0.5.93`). We need to
connect to that URL to view the web UI.

### Spark operations

Let's consider some of the core methods we used.

-   `filter`: create a subset
-   `map`: take an RDD and apply a function to each element, returning
    an RDD
-   `reduce` and `reduceByKey`: take an RDD and apply a reduction
    operation to the elements, doing the reduction stratified by the key
    values for `reduceByKey`. Reduction functions need to be associative
    (order across records doesn't matter) and commutative (order of
    arguments doesn't matter) and take 2 arguments and return 1, all so
    that they can be done in parallel in a straightforward way.
-   `collect`: collect results back to the master
-   `cache`: tell Spark to keep the RDD in memory for later use
-   `repartition`: rework the RDD so it is divided into the specified
    number of partitions

Note that all of the various operations are OOP methods applied to
either the SparkContext management object or to a Spark dataset, called
a Resilient Distributed Dataset (RDD). Here `lines`, `obama`, and `counts`
are all RDDs. However the result of `collect()` is just a standard
Python object.

### Nonstandard reduction

Finding the median of a set of values is an example where we don't have
a simple commutative/associative reducer function. Instead we group all
the observations for each key into a so-called iterable object. Then our
second map function treats each key as an element, iterating over the
observations grouped within each key.

As an example we could find the median page size by language (this is
not a particularly interesting/useful computation in this dataset, but I
wanted to illustrate how this would work).

```python
import numpy as np

def findShortLines(line):
    vals = line.split(' ')
    if len(vals) < 6:
        return(False)
    else:
        return(True)


def computeKeyValue(line):
    vals = line.split(' ')
    # key is language, val is page size
    return(vals[2], int(vals[5]))


def medianFun(input):
    # input[1] is an iterable object containing the page sizes for one key
    # this list comprehension syntax creates a list from the iterable object
    med = np.median([val for val in input[1]])
    # input[0] is the key
    # return a tuple of the key and the median for that key
    return((input[0], med))


output = lines.filter(findShortLines).map(computeKeyValue).groupByKey()
medianResults = output.map(medianFun).collect()
```

Note that because we need to aggregate all the data by key before doing
the reduction on the full data in each key (which is actually just a
*map* operation in this case once the data are already grouped by key),
this is much slower than a reduce operation like max or mean.

### Spark DataFrames and SQL queries

In recent versions of Spark, one can work with more structured data
objects than RDDs. Spark now provides *DataFrames*, which are
collections of row and behave like distributed versions of R or Pandas
dataframes. DataFrames seem to be taking the place of RDDs, at least for
general, high-level use. They can also be queried using SQL syntax.

Here's some example code for using DataFrames.

```python
dir = '/global/scratch/paciorek/wikistats'

lines = sc.textFile(dir + '/' + 'dated')

### create DataFrame and do some operations on it ###

def remove_partial_lines(line):
    vals = line.split(' ')
    if len(vals) < 6:
        return(False)
    else:
        return(True)

def create_df_row(line):
    p = line.split(' ')
    return(int(p[0]), int(p[1]), p[2], p[3], int(p[4]), int(p[5]))


tmp = lines.filter(remove_partial_lines).map(create_df_row)

## 'sqlContext' is the Spark sqlContext management object, created via PySpark
## if you simply start Python without invoking PySpark,
## you would need to create the sqlContext object yourself

df = sqlContext.createDataFrame(tmp, schema = ["date", "hour", "lang", "site", "hits", "size"])

df.printSchema()

## note similarity to dplyr and R/Pandas dataframes
df.select('site').show()
df.filter(df['lang'] == 'en').show()
df.groupBy('lang').count().show()
```

And here's how we use SQL with a DataFrame:

```python
### use SQL with a DataFrame ###

df.registerTempTable("wikiHits")  # name of 'SQL' table is 'wikiHits'

subset = sqlContext.sql("SELECT * FROM wikiHits WHERE lang = 'en' AND site LIKE '%Barack_Obama%'")

subset.take(5)

---

[← 128889 for full dataset](15-128889-for-full-dataset.md) · [Up: contents](index.md) · [Unit 07 — bigData Part 17 — →](17-unit-07-bigdata-part-17.md)
