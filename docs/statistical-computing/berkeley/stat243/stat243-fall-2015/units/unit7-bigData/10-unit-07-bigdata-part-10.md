---
title: Unit 07 — bigData Part 10 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — bigData Part 10 —

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Next let’s get the airline dataset onto the master node and then into the HDFS. Note that the file system commands are like standard UNIX commands, but you need to do hadoop fs - in front of the command. At the end of this chunk we’ll start the Python interface for Spark.

29

export PATH=$PATH:/root/ephemeral-hdfs/bin/

hadoop fs -mkdir /data hadoop fs -mkdir /data/airline

df -h mkdir /mnt/airline cd /mnt/airline # for in-class demo:

scp paciorek@smeagol.berkeley.edu:/scratch/users/paciorek/243/AirlineData/198*bz2 # scp paciorek@smeagol.berkeley.edu:/scratch/users/paciorek/243/AirlineData/[12]*bz2

---

[← Unit 07 — bigData Part 09 —](09-unit-07-bigdata-part-09.md) · [Up: contents](index.md) · [for students →](11-for-students.md)
