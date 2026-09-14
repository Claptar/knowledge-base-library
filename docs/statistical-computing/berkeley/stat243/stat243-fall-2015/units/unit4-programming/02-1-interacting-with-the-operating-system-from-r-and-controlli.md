---
title: 1 Interacting with the operating system from R and controlling R’s behavior
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Interacting with the operating system from R and controlling R’s behavior

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- I’ll assume everyone knows about the following functions/functionality in R: _getwd(), setwd(), source(), pdf(), save(), save.image(), load()_

   - To run UNIX commands from within R, use _system()_ , as follows, noting that we can save the result of a system call to an R object:

1

**system** ("ls -al") _# knitr/Sweave doesn't seem to show the output of system()_ files <- **system** ("ls", intern = TRUE) files[1:5] ## [1] "badCode.R" "cache" ## [3] "exampleRscript.R" "exampleRscript.R~" ## [5] "exons.Rda"

- There are also a bunch of functions that will do specific queries of the filesystem, including

**file.exists** ("unit2-bash.sh") ## [1] TRUE **list.files** ("../data") ## [1] "cpds.csv" "file2.csv" "file.csv" ## [4] "hivSequ.csv" "IPs.RData" "mingdp.txt" ## [7] "precip.txt" "RTADataSub.csv" "urls.txt"

- There are some tools for dealing with differences between operating systems. Here’s an example:

**list.files** ( **file.path** ("..", "data")) ## [1] "cpds.csv" "file2.csv" "file.csv" ## [4] "hivSequ.csv" "IPs.RData" "mingdp.txt" ## [7] "precip.txt" "RTADataSub.csv" "urls.txt"

- To get some info on the system you’re running on:

**Sys.info** () ## sysname

2

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 04 — programming Part 03 — →](03-unit-04-programming-part-03.md)
