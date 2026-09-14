---
title: '14 field is ArrDelay # 18 field is Distance # 3 field is DayOfWeek'
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 field is ArrDelay # 18 field is Distance # 3 field is DayOfWeek

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

lines = lines.filter(screen).repartition(192).cache() # 192 is a multiple of the total number of cores: 24 (12 nodes * 2 cores/node)

n = lines.count() import numpy as np from operator import add P = 8 ####################### # calc xtx and xty ####################### def crossprod(line): vals = line.split(',') y = float(vals[14]) dist = float(vals[18]) dayOfWeek = int(vals[3]) xVec = np.array([0.0] * P) xVec[0] = 1.0 xVec[1] = float(dist)/1000 if dayOfWeek > 1: xVec[dayOfWeek] = 1.0 xtx = np.outer(xVec, xVec) xty = xVec * y return(np.c_[xtx, xty]) xtxy = lines.map(crossprod).reduce(add) # 11 minutes # now just solve system of linear equations!!

35

####################### # calc xtx and xty w/ mapPartitions #######################

---

[← Unit 07 — bigData Part 21 —](21-unit-07-bigdata-part-21.md) · [Up: contents](index.md) · [Unit 07 — bigData Part 23 — →](23-unit-07-bigdata-part-23.md)
