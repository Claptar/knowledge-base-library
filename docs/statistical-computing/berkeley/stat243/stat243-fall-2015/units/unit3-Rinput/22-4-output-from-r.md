---
title: 4 Output from R
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Output from R

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Writing output to files**

Functions for text output are generally analogous to those for input. _write.table()_ , _write.csv()_ , and _writeLines()_ are analogs of _read.table()_ , _read.csv()_ , and _readLines()_ . _write_csv()_ is the _readr_ version of write.csv. _write()_ can be used to write a matrix to a file, specifying the number of columns desired. _cat()_ can be used when you want fine control of the format of what is written out and allows for outputting to a connection (e.g., a file).

_toJSON()_ in the _jsonlite_ package will output R objects as JSON. One use of JSON as output from R would be to _serialize_ the information in an R object such that it could be read into another program.

And of course you can always save to an R data file using _save.image()_ (to save all the objects in the workspace or _save()_ to save only some objects. Happily this is platform-independent so can be used to transfer R objects between different OS.

### **4.2 Formatting output**

_cat()_ is a good choice for printing a message to the screen, often better than _print()_ , which is an object-oriented method. You generally won’t have control over how the output of a _print()_ statement is actually printed.

26

val <- 1.5 **cat** ('My value is ', val, '.\n', sep = '') ## My value is 1.5. **print** ( **paste** ('My value is ', val, '.', sep = '')) ## [1] "My value is 1.5."

We can do more to control formatting with _cat()_ :

_# input_ x <- 7 n <- 5 _# display powers_ **cat** ("Powers of", x, "\n") **cat** ("exponent result\n\n") result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** ( **format** (i, width = 8), **format** (result, width = 10),"\n", } x <- 7 n <- 5 _# display powers_ **cat** ("Powers of", x, "\n") **cat** ("exponent result\n\n") result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** (i, '\t', result, '\n', sep = '') }

sep = "")

One thing to be aware of when writing out numerical data is how many digits are included. For example, the default with _write()_ and _cat()_ is the number of digits displayed to the screen, controlled by _options()$digits_ . (to change this, do options(digits = 5) or specify as an argument to _write()_ or _cat()_ ) If you want finer control, use _sprintf()_ , e.g. to print out print

27

out temperatures as reals (“ _f_ ”=floating points) with four decimal places and nine total character positions, followed by a C for Celsius:

temps <- **c** (12.5, 37.234324, 1342434324.79997234, 2.3456e-6, 1e10) **sprintf** ("%9.4f C", temps)

---

[← Unit 03 — Rinput Part 21 —](21-unit-03-rinput-part-21.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 23 — →](23-unit-03-rinput-part-23.md)
