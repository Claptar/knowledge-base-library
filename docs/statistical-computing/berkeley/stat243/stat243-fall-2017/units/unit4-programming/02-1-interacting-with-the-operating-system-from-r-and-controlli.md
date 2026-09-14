---
title: 1 Interacting with the operating system from R and controlling R’s behavior
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Interacting with the operating system from R and controlling R’s behavior

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- I’ll assume everyone knows about the following functions/functionality in R: _getwd(), setwd(), source(), pdf(), save(), save.image(), load()_

   - To run UNIX commands from within R, use _system()_ , as follows, noting that we can save the result of a system call to an R object:

1

**system** ("ls -al") _## knitr/Sweave doesn't seem to show the output of system()_ files <- **system** ("ls", intern = TRUE) files[1:5] ## [1] "cache" "class2.log" ## [3] "class3.log" "class4.log" ## [5] "exampleRscript.R"

- There are also a bunch of functions that will do specific queries of the filesystem, including

**file.exists** ("unit2-bash.sh") ## [1] TRUE **list.files** ("../data") ## [1] "coop.txt.gz" "cpds.csv" "IPs.RData" ## [4] "precip.txt" "RTADataSub.csv"

- There are some tools for dealing with differences between operating systems. Here’s an example:

**list.files** ( **file.path** ("..", "data")) ## [1] "coop.txt.gz" "cpds.csv" "IPs.RData" ## [4] "precip.txt" "RTADataSub.csv"

- To get some info on the system you’re running on:

**Sys.info** () ## sysname ## "Linux" ## release

2

|##||"4.4.0-93-generic"|
|---|---|---|
|##||version|
|## "#116-Ubuntu SMP Fri|Aug 11|21:17:51 UTC 2017"|
|##||nodename|
|##||"smeagol"|
|##||machine|
|##||"x86_64"|
|##||login|
|##||"unknown"|
|##||user|
|##||"paciorek"|
|##||effective_user|
|##||"paciorek"|


- To see some of the options that control how R behaves, try the _options()_ function. The _width_ option changes the number of characters of width printed to the screen, while the _max.print_ option prevents too much of a large object from being printed to the screen. The _digits_ option changes the number of digits of numbers printed to the screen (but be careful as this can be deceptive if you then try to compare two numbers based on what you see on the screen).

_## options() # this would print out a long list of options_ **options** ()[1:5] ## $add.smooth ## [1] TRUE ## ## $bitmapType ## [1] "cairo" ## ## $browser ## [1] "xdg-open" ## ## $browserNLdisabled ## [1] FALSE ## ## $CBoundsCheck

3

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 04 — programming Part 03 — →](03-unit-04-programming-part-03.md)
