---
title: Unit 03 — dataIO Part 04 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 04 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

More details on sequential (on-line) processing of large files can be found in the tutorial on large datasets mentioned in the reference list above.

One cool trick that can come in handy is to create a _text connection_ . This lets you ’read’ from

7

an R character vector as if it were a text file and could be handy for processing text. For example, you could then use _read.fwf()_ applied to _con_ .

dat <- **readLines** ('../data/precip.txt') con <- **textConnection** (dat[1], "r") **read.fwf** (con, **c** (3,8,4,2,4,2)) ## V1 V2 V3 V4 V5 V6 ## 1 DLY 1000807 PRCP HI 2010 2

We can create connections for writing output too. Just make sure to open the connection first.

### **2.2 File paths**

A few notes on file paths, related to ideas of reproducibility.

1. In general, you don’t want to hard-code absolute paths into your code files because those absolute paths won’t be available on the machines of anyone you share the code with. Instead, use paths relative to the directory the code file is in, or relative to a baseline directory for the project, e.g.:

<mark>dat <-</mark> **<mark>read.csv</mark>** <mark>('../data/cpds.csv')</mark>

2. Be careful with the directory separator in Windows files: you can either do _“C:\\mydir\\file.txt”_ or _“C:/mydir/file.txt”_ , but not _“C:\mydir\file.txt”_ , and note the next comment about avoiding use of ’\\‘ for portability.

3. Using UNIX style directory separators will work in Windows, Mac or Linux, but using Windows style separators is not portable across operating systems.

_## good: will work on Windows_ dat <- **read.csv** ('../data/cpds.csv') _## bad: won't work on Mac or Linux_ dat <- **read.csv** ('..\\data\\cpds.csv')

8

4. Even better, use _file.path()_ so that paths are constructed specifically for the operating system the user is using:

_## good: operating-system independent_ dat <- **read.csv** ( **file.path** ('..', 'data', 'cpds.csv'))

### **2.3 The** **_readr_ package**

_readr_ is intended to deal with some of the shortcomings of the base R functions, such as defaulting to stringsAsFactors=FALSE, leaving column names unmodified, and recognizing dates/times. It reads data in much more quickly than the base R equivalents. See this blog post. Some of the readr functions that are analogs to the comparably-named base R functions are _read_csv()_ , _read_fwf()_ , _read_lines()_ , and _read_table()_ .

Let’s try out _read_csv()_ on the airline dataset used in the R bootcamp.

**library** (readr) _## ## Attaching package: ’readr’ ## The following object is masked from ’package:curl’: ## ## parse_date ## I'm violating the rule about absolute paths here!! ## (airline.csv is big enough that I don't want to put it in the ## course repository)_ **setwd** ('~/staff/workshops/r-bootcamp-2018/data') **system.time** (dat <- **read.csv** ('airline.csv', stringsAsFactors = FALSE)) ## user system elapsed ## 5.652 0.136 5.788 **system.time** (dat2 <- **read_csv** ('airline.csv')) _## Parsed with column specification: ## cols( ## .default = col_integer(),_

9

_## UniqueCarrier = col_character(), ## TailNum = col_character(), ## Origin = col_character(), ## Dest = col_character(), ## CancellationCode = col_character() ## ) ## See spec(...) for full column specifications._ ## user system elapsed ## 1.056 0.060 1.119

### **2.4 Reading data quickly**

In addition to the tips above, there are a number of packages that allow one to read large data files quickly, in particular _data.table_ , _ff_ , and _bigmemory_ . In general, these provide the ability to load datasets into R without having them in memory, but rather stored in clever ways on disk that allow for fast access. Metadata is stored in R. More on this in the unit on big data and in the tutorial on large datasets mentioned in the reference list above.

---

[← 2 Reading data from text files into R](03-2-reading-data-from-text-files-into-r.md) · [Up: contents](index.md) · [3 Webscraping and working with XML and JSON →](05-3-webscraping-and-working-with-xml-and-json.md)
