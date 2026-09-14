---
title: Unit 03 — Rinput Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 04 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

5

If a file is large, we may want to read it in in chunks (of lines), do some computations to reduce the size of things, and iterate. _read.table()_ , _read.fwf()_ and _readLines()_ all have the arguments that let you read in a fixed number of lines. To read-on-the-fly in blocks, we need to first establish the connection and then read from it sequentially.

con <- **file** ("../data/precip.txt", "r") _## "r" for 'read' - you can also open files for writing with "w" ## (or "a" for appending)_ **class** (con) blockSize <- 1000 _# obviously this would be large in any real application_ nLines <- 300000 **for** (i **in** 1: **ceiling** (nLines / blockSize)){ lines <- **readLines** (con, n = blockSize) _# manipulate the lines and store the key stuff_ } **close** (con)

Here’s an example of using _curl()_ to do this for a file on the web.

**library** (jsonlite) _## Loading required package: methods ## ## Attaching package: ’jsonlite’ ## ## The following object is masked from ’package:utils’: ## ## View_ URL <- "http://www.stat.berkeley.edu/share/paciorek/2008.csv.gz" con <- **gzcon** ( **curl** (URL, open = "r")) _# url() would work here for http too_ **for** (i **in** 1:8) { **print** (i) **print** ( **system.time** (tmp <- **readLines** (con, n = 100000))) **print** (tmp[1]) }

6

---

[← Unit 03 — Rinput Part 03 —](03-unit-03-rinput-part-03.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 05 — →](05-unit-03-rinput-part-05.md)
