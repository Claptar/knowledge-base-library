---
title: Problems
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps2.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/ps/ps2.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps2.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/ps/ps2.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Please read Unit 5 on good programming/project practices and incorporate what you’ve learned from that reading into your solutions (particularly for Problem 3). As your response to this question, briefly (a few sentences) note what you did in your code that reflects the material in Unit 5. You could also note anything in Unit 5 that you disagree with, if you have a different stylistic perspective.

2. This problem explores file sizes and file-reading speed and their relationship to the file format in light of understanding storage in ASCII plain text versus binary formats and the fact that numbers are stored as 8 bytes per number in binary format.

   - (a) Explain the sizes of the various files. In discussing the CSV text file, how many characters do you expect to be in the file (i.e., you should be able to estimate this very accurately without using _wc_ or any explicit program that counts characters).

1

n <- 1e7 a <- **matrix** ( **rnorm** (n), ncol = 100) a <- **round** (a, 10) **write.table** (a, file = '/tmp/tmp.csv', quote=FALSE, row.names=FALSE, col.names = FALSE, sep=',') **save** (a, file = '/tmp/tmp.Rda', compress = FALSE) **file.size** ('/tmp/tmp.csv') ## [1] 133890295 **file.size** ('/tmp/tmp.Rda') ## [1] 80000087

- (b) Now consider saving out the numbers one row per number. Given we no longer have to save all the commas, why is the file size unchanged?

b <- a **dim** (b) <- **c** (1e7, 1) _## change to one column by adjusting attribute_ **write.table** (b, file = '/tmp/tmp-onecolumn.csv', quote=FALSE, row.names=FALSE, col.names = FALSE, sep=',') **file.size** ('/tmp/tmp-onecolumn.csv') ## [1] 133890295

- (c) Consider the following ways of reading the data into R. Explain the difference in speed between the two situations in “First comparison”, then for the difference in “Second comparison”, and for “Third comparison”. Side note: in this case _read_csv()_ is rather faster than _read.csv()_ .

_## First comparison_ **system.time** (a0 <- **read.csv** ('/tmp/tmp.csv', header = FALSE)) ## user system elapsed ## 35.748 0.264 36.014 **system.time** (a1 <- **scan** ('/tmp/tmp.csv', sep = ',')) ## user system elapsed ## 5.236 0.048 5.283 _## Second comparison_ **system.time** (a0 <- **read.csv** ('/tmp/tmp.csv',header = FALSE, colClasses = 'numeric')) ## user system elapsed ## 5.336 0.028 5.363 **system.time** (a1 <- **scan** ('/tmp/tmp.csv', sep = ','))

2

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Ps 02 — Part 03 — →](03-ps-02-part-03.md)
