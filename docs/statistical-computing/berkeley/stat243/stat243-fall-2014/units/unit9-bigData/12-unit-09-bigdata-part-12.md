---
title: Unit 09 — bigData Part 12 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — bigData Part 12 —

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Next let’s get the airline dataset onto the master node and then into the HDFS. Note that the file system commands are like standard UNIX commands, but you need to do hadoop fs - in front of the command. At the end of this chunk we’ll start the Python interface for Spark.

export PATH=$PATH:/root/ephemeral-hdfs/bin/

hadoop fs -mkdir /data hadoop fs -mkdir /data/airline df -h mkdir /mnt/airline

scp paciorek@saruman.berkeley.edu:/scratch/users/paciorek/243/AirlineData/[12]*bz2 /mnt/airline

---

[← Unit 09 — bigData Part 11 —](11-unit-09-bigdata-part-11.md) · [Up: contents](index.md) · [for in-class demo →](13-for-in-class-demo.md)
