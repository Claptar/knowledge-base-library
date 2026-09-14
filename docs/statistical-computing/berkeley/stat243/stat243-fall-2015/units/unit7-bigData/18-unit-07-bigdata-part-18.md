---
title: Unit 07 — bigData Part 18 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 07 — bigData Part 18 —

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

30

#### **6.3.2 Using Spark for pre-processing**

Now we’ll do some basic manipulations with the airline dataset. We’ll count the number of lines/observations in our dataset. Then we’ll do a map-reduce calculation that involves counting the number of flights by airline, so airline will serve as the key.

Note that all of the various operations are OOP methods applied to either the SparkContext management object or to a Spark dataset, called a Resilient Distributed Dataset (RDD). Here _lines_ and _output_ are both RDDs. However the result of _collect()_ is just a standard Python object.

In the last step, let’s compare how long it took to grab the SFO subset relative to the performance of R earlier in this Unit.

from operator import add import numpy as np lines = sc.textFile('/data/airline')

---

[← Unit 07 — bigData Part 17 —](17-unit-07-bigdata-part-17.md) · [Up: contents](index.md) · [Unit 07 — bigData Part 19 — →](19-unit-07-bigdata-part-19.md)
