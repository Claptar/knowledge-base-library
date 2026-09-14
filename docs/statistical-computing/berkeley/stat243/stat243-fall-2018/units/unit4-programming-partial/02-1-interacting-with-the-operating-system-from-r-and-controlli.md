---
title: 1 Interacting with the operating system from R and controlling R’s behavior
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Interacting with the operating system from R and controlling R’s behavior

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- I’ll assume everyone knows about the following functions/functionality in R: getwd(), setwd(), source(), pdf(), save(), save.image(), load()

   - To run UNIX commands from within R, use system(), as follows, noting that we can save the result of a system call to an R object:

1

**system** ("ls -al") ## knitr/Sweave doesn't seem to show the output of system() files <- **system** ("ls", intern = TRUE) files[1:5] ## [1] "badCode.R" "cache" ## [3] "class1_shell_history.sh" "class2.log" ## [5] "class2_shell_history.sh"

- There are also a bunch of functions that will do specific queries of the filesystem, including

**file.exists** ("unit2-bash.sh") ## [1] TRUE **list.files** ("../data") ## [1] "cpds.csv" "hivSequ.csv" "IPs.RData" ## [4] "precip.txt" "RTADataSub.csv" "tmp2.txt" ## [7] "tmp.txt" "tmp.txt~"

- There are some tools for dealing with differences between operating systems. Here’s an example:

**list.files** ( **file.path** ("..", "data")) ## [1] "cpds.csv" "hivSequ.csv" "IPs.RData" ## [4] "precip.txt" "RTADataSub.csv" "tmp2.txt" ## [7] "tmp.txt" "tmp.txt~"

- To get some info on the system you’re running on:

**Sys.info** () ## sysname

2

|##||"Linux"|
|---|---|---|
|##||release|
|##||"4.4.0-124-generic"|
|##||version|
|## "#148-Ubuntu SMP|Wed May|2 13:00:18 UTC 2018"|
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


- To see some of the options that control how R behaves, try the options() function. The width option changes the number of characters of width printed to the screen, while the max.print option prevents too much of a large object from being printed to the screen. The digits option changes the number of digits of numbers printed to the screen (but be careful as this can be deceptive if you then try to compare two numbers based on what you see on the screen).

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 03 — →](03-unit-04-programming-partial-part-03.md)
