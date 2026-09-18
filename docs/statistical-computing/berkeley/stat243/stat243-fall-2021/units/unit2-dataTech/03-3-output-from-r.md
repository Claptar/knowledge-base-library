---
title: 3 Output from R
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit2-dataTech.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit2-dataTech.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Output from R

## 3.1 Writing output to files

Functions for text output are generally analogous to those for input. *write.table()*, *write.csv()*,
and *writeLines()* are analogs of *read.table()*, *read.csv()*, and *readLines()*. *write_csv()* is the readr
version of *write.csv*. *write()* can be used to write a matrix to a file, specifying the number of
columns desired. *cat()* can be used when you want fine control of the format of what is written out
and allows for outputting to a connection (e.g., a file).

*toJSON()* in the *jsonlite* package will output R objects as JSON. One use of JSON as output
from R would be to *serialize* the information in an R object such that it could be read into another
program.

And of course you can always save to an R data file using *save.image()* (to save all the objects
in the workspace or *save()* to save only some objects. Happily this is platform-independent so can
be used to transfer R objects between different OS.

## 3.2 Formatting output

*cat()* is a good choice for printing a message to the screen, often better than *print()*, which is
an object-oriented method. You generally won’t have control over how the output of a *print()*
statement is actually printed.

```r
val <- 1.5
cat('My value is ', val, '.\n', sep = '')
## My value is 1.5.
print(paste('My value is ', val, '.', sep = ''))
## [1] "My value is 1.5."
```

We can do more to control formatting with *cat()*:

```r
## input
x <- 7
n <- 5
## display powers
cat("Powers of", x, "\n")
## Powers of 7
cat("exponent result\n\n")
## exponent result
result <- 1
for (i in 1:n) {
result <- result * x
cat(format(i, width = 8), format(result, width = 10),
"\n", sep = "")
}
## 1 7
## 2 49
## 3 343
## 4 2401
## 5 16807
x <- 7
n <- 5
## display powers
cat("Powers of", x, "\n")
## Powers of 7
cat("exponent result\n\n")
## exponent result
result <- 1
for (i in 1:n) {
result <- result * x
cat(i, '\t', result, '\n', sep = '')
}
## 1 7
## 2 49
## 3 343
## 4 2401
## 5 16807
```

One thing to be aware of when writing out numerical data is how many digits are included. For
example, the default with *write()* and *cat()* is the number of digits that R displays to the screen,
controlled by `options()$digits`. But note that `options()$digits` seems to have some
variability in behavior across operating systems. If you want finer control, use *sprintf()*, e.g., to
print out print out temperatures as reals (“f”=floating points) with four decimal places and nine
total character positions, followed by a C for Celsius:

```r
temps <- c(12.5, 37.234324, 1342434324.79997234, 2.3456e-6, 1e10)
sprintf("%9.4f C", temps)
## [1] " 12.5000 C" " 37.2343 C"
## [3] "1342434324.8000 C" " 0.0000 C"
## [5] "10000000000.0000 C"
city <- "Boston"
sprintf("The temperature in %s was %.4f C.", city, temps[1])
## [1] "The temperature in Boston was 12.5000 C."
sprintf("The temperature in %s was %9.4f C.", city, temps[1])
## [1] "The temperature in Boston was 12.5000 C."
```

Note, to change the number of digits printed to the screen, do `options(digits = 5)` or
specify as an argument to *print()* or use *sprintf()*.

---

[← 2 Reading data from text files into R](02-2-reading-data-from-text-files-into-r.md) · [Up: contents](index.md) · [4 Webscraping and working with HTML, XML, and JSON →](04-4-webscraping-and-working-with-html-xml-and-json.md)
