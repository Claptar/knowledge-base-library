---
title: Unit 07 — bigData Part 18 —
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unit 07 — bigData Part 18 —

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```

### Other comments

#### Running a batch Spark job

We can run a Spark job using Python code as a batch script rather than
interactively. Here's an example, which computes the value of Pi by
Monte Carlo simulation.

```python
spark-submit --master $SPARK_URL $SPARK_DIR/examples/src/main/python/pi.py
```

The file `example_spark_job.sh` is an example SLURM job submission
script that runs the PySpark code in `test_batch.py`. If you want to run
a Spark job as a batch submission to the scheduler you can follow that
example, submitting the job using `sbatch`: `sbatch name_of_job_script.sh`.

#### Python vs. Scala/Java

Spark is implemented natively in Java and Scala, so all calculations in
Python involve taking Java data objects converting them to Python
objects, doing the calculation, and then converting back to Java. This
process is called serialization and takes time, so the [speed when
implementing your work in Scala (or Java) may be faster](http://apache-spark-user-list.1001560.n3.nabble.com/Scala-vs-Python-performance-differences-td4247.html).

### R interfaces to Spark

Both `SparkR` (from the Spark folks) and `sparklyr` (from the RStudio
folks) allow you to interact with Spark-based data from R. There are
some limitations to what you can do (both in what is possible and in
what will execute with reasonable speed), so for heavy use of Spark you
may want to use Python or even the Scala or Java interfaces. We'll focus
on `sparklyr`.

With `sparklyr`, you can:

-   use `dplyr` functionality
-   use distributed apply computations via `spark_apply()`.

There are some limitations though:

-   the `dplyr` functionality translates operations to SQL so there are
    limited operations one can do, particularly in terms of computations
    on a given row of data.
-   `spark_apply()` appears to run very slowly, presumably because data
    is being serialized back and forth between R and Java data
    structures.

### sparklyr example

Here's some example code that works on Savio. One important note is that
if you don't adjust the memory, you'll get obscure Java errors that
occur because Spark runs out of memory, and this is only clear if you
look in the right log files in the directory `$SPARK_LOG_DIR`.

```R
## see notes above for starting Spark

## local installation on your own computer
if(!require(sparklyr)) {
    install.packages("sparklyr")
    # spark_install() ## if spark not already installed
}

### connect to Spark ###

## need to increase memory otherwise get hard-to-interpret Java
## errors due to running out of memory; total memory on the node is 64 GB
conf <- spark_config()
conf$spark.driver.memory <- "8G"
conf$spark.executor.memory <- "50G"

---

[← Unit 07 — bigData Part 17 —](17-unit-07-bigdata-part-17.md) · [Up: contents](index.md) · [sc <- sparkconnect(master = "local") # if doing on laptop →](19-sc---sparkconnect-master-local-if-doing-on-laptop.md)
