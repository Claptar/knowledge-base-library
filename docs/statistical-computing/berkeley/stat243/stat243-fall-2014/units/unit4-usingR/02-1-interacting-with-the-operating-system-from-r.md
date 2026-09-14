---
title: 1 Interacting with the operating system from R
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Interacting with the operating system from R

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- I’ll assume everyone knows about the following functions/functionality in R: _getwd(), setwd(), source(), pdf(), save(), save.image(), load()_

1

- To run UNIX commands from within R, use _system()_ , as follows, noting that we can save the result of a system call to an R object:

**system** ("ls -al") _# knitr/Sweave doesn't seem to show the output of system()_ files <- **system** ("ls", intern = TRUE) files[1:5] ## [1] "best-practices.png" "branchcommit.png" "cache" ## [4] "commit_anatomy.png" "example.bashrc"

- There are also a bunch of functions that will do specific queries of the filesystem, including

**file.exists** ("unit2-bash.sh") ## [1] TRUE **list.files** ("../data") ## [1] "cpds.csv" "hivSequ.csv" "IPs.RData" "precipData.txt" ## [5] "precip.txt" "prec.RData" "RTADataSub.csv" "urls.txt"

- There are some tools for dealing with differences between operating systems. Here’s an example:

**list.files** ( **file.path** ("..", "data")) ## [1] "cpds.csv" "hivSequ.csv" "IPs.RData" "precipData.txt" ## [5] "precip.txt" "prec.RData" "RTADataSub.csv" "urls.txt"

- To get some info on the system you’re running on:

2

**Sys.info** ()

|##|sysname|
|---|---|
|##|"Linux"|
|##|release|
|##|"3.2.0-67-generic"|
|##|version|
|## "#101-Ubuntu SMP Tue Jul 15|17:46:11 UTC 2014"|
|##|nodename|
|##|"smeagol"|
|##|machine|
|##|"x86_64"|
|##|login|
|##|"unknown"|
|##|user|
|##|"paciorek"|
|##|effective_user|
|##|"paciorek"|


- To see some of the options that control how R behaves, try the _options()_ function. The _width_ option changes the number of characters of width printed to the screen, while the _max.print_ option prevents too much of a large object from being printed to the screen. The _digits_ option changes the number of digits of numbers printed to the screen (but be careful as this can be deceptive if you then try to compare two numbers based on what you see on the screen).

_# options() # this would print out a long list of options_

**options** ()[1:5] ## $add.smooth ## [1] TRUE ## ## $bitmapType ## [1] "cairo" ## ## $browser

3

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 03 — →](03-unit-04-usingr-part-03.md)
