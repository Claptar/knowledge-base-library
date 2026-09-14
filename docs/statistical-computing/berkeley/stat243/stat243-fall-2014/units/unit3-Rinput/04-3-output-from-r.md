---
title: 3 Output from R
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Output from R

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Writing output to files**

Functions for text output are generally analogous to those for input. _write.table()_ , _write.csv()_ , and _writeLines()_ are analogs of _read.table()_ , _read.csv()_ , and _readLines()_ . _write()_ can be used to write a matrix to a file, specifying the number of columns desired. _cat()_ can be used when you want fine control of the format of what is written out and allows for outputting to a connection (e.g., a file).

6

And of course you can always save to an R data file using _save.image()_ (to save all the objects in the workspace or _save()_ to save only some objects. Happily this is platform-independent so can be used to transfer R objects between different OS.

### **3.2 Formatting output**

_cat()_ is a good choice for printing a message to the screen, often better than _print()_ , which is an object-oriented method. You generally won’t have control over how the output of a _print()_ statement is actually printed.

val <- 1.5 **cat** ("My value is ", val, ".\n", sep = "") ## My value is 1.5. **print** ( **paste** ("My value is ", val, ".", sep = "")) ## [1] "My value is 1.5."

We can do more to control formatting with _cat()_ :

_# input_ x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n") **cat** ("exponent result\n\n") result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** ( **format** (i, width = 8), **format** (result, width = 10), "\n", sep = "") } x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n") **cat** ("exponent result\n\n")

7

result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** (i, "\t", result, "\n", sep = "") }

One thing to be aware of when writing out numerical data is how many digits are included. For example, the default with _write()_ and _cat()_ is the number of digits displayed to the screen, controlled by _options()$digits_ . (to change this, do options(digits = 5) or specify as an argument to _write()_ or _cat()_ ) If you want finer control, use _sprintf()_ , e.g. to print out print out temperatures as reals (“ _f_ ”=floating points) with four decimal places and nine total character positions, followed by a C for Celsius:

temps <- **c** (12.5, 37.234324, 1342434324.79997, 2.3456e-06, 1e+10) **sprintf** ("%9.4f C", temps) ## [1] " 12.5000 C" " 37.2343 C" ## [3] "1342434324.8000 C" " 0.0000 C" ## [5] "10000000000.0000 C" city <- "Boston" **sprintf** ("The temperature in %s was %.4f C.", city, temps[1]) ## [1] "The temperature in Boston was 12.5000 C." **sprintf** ("The temperature in %s was %9.4f C.", city, temps[1]) ## [1] "The temperature in Boston was 12.5000 C."

---

[← V1 V2 V3 V4 V5 V6 ## 1 DLY 1000807 PRCP HI 2010 2](03-v1-v2-v3-v4-v5-v6-1-dly-1000807-prcp-hi-2010-2.md) · [Up: contents](index.md) · [4 File and string encodings →](05-4-file-and-string-encodings.md)
