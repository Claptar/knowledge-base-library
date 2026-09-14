---
title: 'check files on the HDFS, e.g.: hadoop fs -ls /user/paciorek/data/wikistats/raw'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit8-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit8-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# check files on the HDFS, e.g.: hadoop fs -ls /user/paciorek/data/wikistats/raw

**Source:** [`units/unit8-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit8-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

6

## now do some processing with Spark, e.g., preprocess.{sh,py} # after processing can retrieve data from HDFS as needed hadoop fs -copyToLocal /user/paciorek/data/wikistats/dated .

#### **2.2.4 Using Spark on Savio**

Here are the steps to use Spark on Savio. We’ll demo using an interactive job (the _srun_ line here) but one could include the last three commands in the SLURM job script.

tmux new -s spark ## to get back in if disconnected: tmux a -t spark ## having some trouble with ic_stat243 and 4 nodes; check again srun -A ic_stat243 -p savio2 --nodes=4 -t 1:00:00 --pty bash module load java spark/2.1.0 python/3.5 source /global/home/groups/allhands/bin/spark_helper.sh spark-start ## note the environment variables created env | grep SPARK

spark-submit --master $SPARK_URL $SPARK_DIR/examples/src/main/python/pi.py

First we’ll load Python; then we can use Spark via the Python interface interactively. We’ll see how to submit batch jobs later.

---

[← Unit 8: Databases and Big Data](01-unit-8-databases-and-big-data.md) · [Up: contents](index.md) · [Unit 08 — bigData Part 03 — →](03-unit-08-bigdata-part-03.md)
