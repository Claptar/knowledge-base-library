---
title: 4 Output from R
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Output from R

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Writing output to files**

Functions for text output are generally analogous to those for input. _write.table()_ , _write.csv()_ , and _writeLines()_ are analogs of _read.table()_ , _read.csv()_ , and _readLines()_ . _write_csv()_ is the _readr_ version of write.csv. _write()_ can be used to write a matrix to a file, specifying the number of columns desired. _cat()_ can be used when you want fine control of the format of what is written out and allows for outputting to a connection (e.g., a file).

_toJSON()_ in the _jsonlite_ package will output R objects as JSON. One use of JSON as output from R would be to _serialize_ the information in an R object such that it could be read into another program.

And of course you can always save to an R data file using _save.image()_ (to save all the objects in the workspace or _save()_ to save only some objects. Happily this is platform-independent so can be used to transfer R objects between different OS.

### **4.2 Formatting output**

_cat()_ is a good choice for printing a message to the screen, often better than _print()_ , which is an object-oriented method. You generally won’t have control over how the output of a _print()_ statement is actually printed.

30

val <- 1.5 **cat** ('My value is ', val, '.\n', sep = '') ## My value is 1.5. **print** ( **paste** ('My value is ', val, '.', sep = '')) ## [1] "My value is 1.5."

We can do more to control formatting with _cat()_ :

_## input_ x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n") ## Powers of 7 **cat** ("exponent result\n\n") ## exponent result result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** ( **format** (i, width = 8), **format** (result, width = 10), "\n", sep = "") } ## 1 7 ## 2 49 ## 3 343 ## 4 2401 ## 5 16807 x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n")

31

---

[← [1] "paging" "loans" class (data$loans) # nice! ## [1] "data.frame"](17-1-paging-loans-class-data-loans-nice-1-data-frame.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 19 — →](19-unit-03-dataio-part-19.md)
