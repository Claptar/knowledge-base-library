---
title: after processing can retrieve data from HDFS as needed
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# after processing can retrieve data from HDFS as needed

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

hadoop fs -copyToLocal /user/paciorek/data/wikistats/dated .
```


### Using Spark on Savio

Here are the steps to use Spark on Savio. We'll demo using an
interactive job (the `srun` line here) but one could include the last
three commands in the SLURM job script.

```bash
tmux new -s spark  ## to get back in if disconnected: tmux a -t spark

## having some trouble with ic_stat243 and 4 nodes; check again
srun -A ic_stat243 -p savio2 --nodes=4 -t 1:00:00 --pty bash
module load java spark/2.1.0 python/3.5
source /global/home/groups/allhands/bin/spark_helper.sh
spark-start
## note the environment variables created
env | grep SPARK

spark-submit --master $SPARK_URL  $SPARK_DIR/examples/src/main/python/pi.py
```


First we'll load Python; then we can use Spark via the Python interface
interactively. We'll see how to submit batch jobs later.

```bash
pyspark --master $SPARK_URL --conf "spark.executorEnv.PYTHONHASHSEED=321"  --executor-memory 60G
```

### Preprocessing the Wikipedia traffic data

At this point, one complication is that the date-time information on the
Wikipedia traffic is embedded in the file names. We'd like that
information to be fields in the data files. This is done by running the
code in `preprocess_wikipedia.py` in the Python interface to Spark
(pyspark). Note that trying to use multiple nodes and to repartition in
various ways caused various errors I was unable to diagnose, but the
code as is should work albeit somewhat slowly.

In principle one could run `preprocess_wikipedia.py` as a batch
submission, but I was having problems getting that to run successfully.

### Spark in action: processing the Wikipedia traffic data

Now we'll do some basic manipulations with the Wikipedia dataset, with
the goal of analyzing traffic to Barack Obama's sites during the time
around his election as president in 2008. Here are the steps we'll
follow:

-   Count the number of lines/observations in our dataset.
-   Filter to get only the Barack Obama sites.
-   Map step that creates key-value pairs from each
    record/observation/row.
-   Reduce step that counts the number of views by hour and language, so
    hour-day-lang will serve as the key.
-   Map step to prepare the data so it can be output in a nice format.

Note that Spark uses *lazy evaluation*. Actual computation only happens
when one asks for a result to be returned or output written to disk.

First we'll see how we read in the data and filter to the observations
(lines / rows) of interest.

```python
dir = '/global/scratch/paciorek/wikistats'

### read data and do some checks ###

## 'sc' is the SparkContext management object, created via PySpark
## if you simply start Python, without invoking PySpark,
## you would need to create the SparkContext object yourself

lines = sc.textFile(dir + '/' + 'dated')

lines.getNumPartitions()  # 16800 (480 input files) for full dataset

---

[← check files on the HDFS, e.g.](08-check-files-on-the-hdfs-e-g.md) · [Up: contents](index.md) · [note delayed evaluation →](10-note-delayed-evaluation.md)
