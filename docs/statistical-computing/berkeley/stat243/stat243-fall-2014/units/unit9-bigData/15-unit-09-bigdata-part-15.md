---
title: Unit 09 — bigData Part 15 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit9-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 09 — bigData Part 15 —

**Source:** [`units/unit9-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit9-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **6.3.2 Using Spark for pre-processing**

Now we’ll do some basic manipulations with the airline dataset. We’ll count the number of lines/observations in our dataset. Then we’ll do a map-reduce calculation that involves counting the number of flights by airline, so airline will serve as the key.

Note that all of the various operations are OOP methods applied to either the SparkContext management object or to a Spark dataset, called a Resilient Distributed Dataset (RDD). Here _lines_ and _output_ are both RDDs. However the result of _collect()_ is just a standard Python object.

In the last step, let’s compare how long it took to grab the SFO subset relative to the performance of R earlier in this Unit.

from operator import add import numpy as np lines = sc.textFile('/data/airline').cache() numLines = lines.count()

---

[← scp paciorek@saruman.berkeley.edu:/scratch/users/paciorek/243/AirlineData/198bz2](14-scp-paciorek-saruman-berkeley-edu-scratch-users-paciorek-243.md) · [Up: contents](index.md) · [Unit 09 — bigData Part 16 — →](16-unit-09-bigdata-part-16.md)
