---
title: 3. Output from R
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit2-dataTech.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Output from R

**Source:** [`units/unit2-dataTech.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Writing output to files

Functions for text output are generally analogous to those for input.
*write.table()*, *write.csv()*, and *writeLines()* are analogs of
*read.table()*, *read.csv()*, and *readLines()*. *write_csv()* is the
*readr* version of write.csv. *write()* can be used to write a matrix to
a file, specifying the number of columns desired. *cat()* can be used
when you want fine control of the format of what is written out and
allows for outputting to a connection (e.g., a file).

*toJSON()* in the *jsonlite* package will output R objects as JSON. One
use of JSON as output from R would be to *serialize* the information in
an R object such that it could be read into another program.

And of course you can always save to an R data file (a binary file format) using *save.image()*
(to save all the objects in the workspace or *save()* to save only some
objects. Happily this is platform-independent so can be used to transfer
R objects between different OS.

## Formatting output

*cat()* is a good choice for printing a message to the screen, often
better than *print()*, which is an object-oriented method. You generally
won't have control over how the output of a *print()* statement is
actually printed.

```r
val <- 1.5
cat('My value is ', val, '.\n', sep = '')
print(paste('My value is ', val, '.', sep = ''))
```


We can do more to control formatting with *cat()*:

```r
## input
x <- 7
n <- 5
## display powers
cat("Powers of", x, "\n")
cat("exponent   result\n\n")
result <- 1
for (i in 1:n) {
    result <- result * x
    cat(format(i, width = 8), format(result, width = 10),
            "\n", sep = "")
}
```


One thing to be aware of when writing out numerical data is how many
digits are included. For example, the default with `write` and
`cat` is the number of digits that R displays to the screen,
controlled by `options()$digits`. But note that `options()$digits` seems
to have some variability in behavior across operating systems. If you
want finer control, use `sprintf`. For example, here we print out
temperatures as reals ("f"=floating point) with four decimal places
and nine total character positions, followed by a C for Celsius:

```r
temps <- c(12.5, 37.234324, 1342434324.79997234, 2.3456e-6, 1e10)
sprintf("%9.4f C", temps)
city <- "Boston"
sprintf("The temperature in %s was %.4f C.", city, temps[1])
sprintf("The temperature in %s was %9.4f C.", city, temps[1])
```

To change the number of digits printed to the screen,
do `options(digits = 5)` or specify as an argument to `print` or
use `sprintf`.

---

[← 2. Reading data from text files into R](03-2-reading-data-from-text-files-into-r.md) · [Up: contents](index.md) · [4. Webscraping and working with HTML, XML, and JSON →](05-4-webscraping-and-working-with-html-xml-and-json.md)
