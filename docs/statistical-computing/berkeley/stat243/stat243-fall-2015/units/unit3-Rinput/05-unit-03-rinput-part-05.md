---
title: Unit 03 — Rinput Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 05 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

One cool trick that can come in handy is to create a _text connection_ . This lets you ’read’ from an R character vector as if it were a text file and could be handy for processing text. For example,

7

you could then use _read.fwf()_ applied to _con_ .

dat <- **readLines** ('../data/precip.txt') con <- **textConnection** (dat[1], "r") **read.fwf** (con, **c** (3,8,4,2,4,2)) ## V1 V2 V3 V4 V5 V6 ## 1 DLY 1000807 PRCP HI 2010 2

We can create connections for writing output too. Just make sure to open the connection first. Be careful with the directory separator in Windows files: you can either do _“C:\\mydir\\file.txt”_ or _“C:/mydir/file.txt”_ , but not _“C:\mydir\file.txt”_ .

### **2.2 The** **_readr_ package**

_readr_ is intended to deal with some of the shortcomings of the base R functions, such as defaulting to stringsAsFactors=FALSE, leaving column names unmodified, and recognizing dates/times. It reads data in much more quickly than the base R equivalents. See this blog post. Some of the readr functions that are analogs to the comparably-named base R functions are _read_csv()_ , _read_fwf()_ , _read_lines()_ , and _read_table()_ .

Let’s try out _read_csv()_ on the airline dataset used in the R bootcamp.

**library** (readr) _## ## Attaching package: ’readr’ ## ## The following object is masked from ’package:curl’: ## ## parse_date_ **setwd** ('~/staff/workshops/r-bootcamp-2015/data') **system.time** (dat <- **read.csv** ('airline.csv', stringsAsFactors = FALSE)) ## user system elapsed ## 5.566 0.069 5.634 **system.time** (dat2 <- **read_csv** ('airline.csv')) ## user system elapsed ## 1.285 0.019 1.305

8

### **2.3 Reading data quickly**

In addition to the tips above, there are a number of packages that allow one to read large data files quickly, in particular _data.table_ , _ff_ , and _bigmemory_ . In general, these provide the ability to load datasets into R without having them in memory, but rather stored in clever ways on disk that allow for fast access. Metadata is stored in R. More on this in the unit on big data.

---

[← Unit 03 — Rinput Part 04 —](04-unit-03-rinput-part-04.md) · [Up: contents](index.md) · [3 Webscraping and working with XML and JSON →](06-3-webscraping-and-working-with-xml-and-json.md)
