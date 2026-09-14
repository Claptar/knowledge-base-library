---
title: 1 Interacting with the operating system from R and controlling R’s behavior
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Interacting with the operating system from R and controlling R’s behavior

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- I’ll assume everyone knows about the following functions/functionality in R: _getwd(), setwd(), source(), pdf(), save(), save.image(), load()_

   - To run UNIX commands from within R, use _system()_ , as follows, noting that we can save the result of a system call to an R object:

1

**system** ("ls -al") _## knitr/Sweave doesn't seem to show the output of system()_ files <- **system** ("ls", intern = TRUE) files[1:5] ## [1] "badCode.R" "cache" "calc_mean.py" ## [4] "figures" "goodCode.R"

- There are also a bunch of functions that will do specific queries of the filesystem, including

**file.exists** ("unit2-bash.sh") ## [1] FALSE **list.files** ("../data") ## [1] "coop.txt.gz" "cpds.csv" ## [3] "hivSequ.csv" "IPs.RData" ## [5] "precip.txt" "precipData.txt" ## [7] "RTADataSub.csv" "stackoverflow-2016.db"

- There are some tools for dealing with differences between operating systems. Here’s an example:

**list.files** ( **file.path** ("..", "data"))

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 05 — programming Part 03 — →](03-unit-05-programming-part-03.md)
