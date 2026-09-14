---
title: 2 Reading data from text files into R
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Reading data from text files into R

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_read.table()_ is probably the most commonly-used function for reading in data. It reads in delimited files ( _read.csv()_ and _read.delim()_ are special cases of _read.table()_ ). The key arguments are the delimiter (the _sep_ argument) and whether the file contains a header, a line with the variable names. We can use _read.fwf()_ to read from a fixed width text file into a data frame.

The most difficult part of reading in such files can be dealing with how R determines the classes of the fields that are read in. There are a number of arguments to _read.table()_ and _read.fwf()_ that allow the user to control the classes. One difficulty is that character and numeric fields are sometimes read in as factors. Basically _read.table()_ tries to read fields in as numeric and if it finds non-numeric and non-NA values, it reads in as a factor. This can be annoying.

Let’s work through a couple examples. Before we do that, let’s look at the arguments to _read.table()_ . Note that _sep=”_ separates on any amount of white space. In the code chunk below, I’ve told _knitr_ not to print the output to the PDF; we’ll see the full output in class during the demo.

**getwd** () _# a common error is not knowing what directory R is looking at_ **setwd** ("../data") dat <- **read.table** ("RTADataSub.csv", sep = ",", head = TRUE) **sapply** (dat, class) **levels** (dat[, 2]) dat2 <- **read.table** ("RTADataSub.csv", sep = ",", head = TRUE, na.strings = **c** ("NA", "x"), stringsAsFactors = FALSE) **unique** (dat2[, 2]) _## hmmm, what happened to the blank values this time?_ **which** (dat[, 2] == "") dat2[ **which** (dat[, 2] == "")[1], ] _# deconstruct it!_

3

sequ <- **read.table** ("hivSequ.csv", sep = ",", header = TRUE, colClasses = **c** ("integer", "integer", "character", "character", "numeric", "integer")) _## let's make sure the coercion worked - sometimes R is ## obstinant_ **sapply** (sequ, class) _## that made use of the fact that a data frame is a list_

Note that you can avoid reading in one or more columns by specifying _NULL_ as the column class for those columns to be omitted. Also, secifying the _colClasses_ argument explicitly should make for faster file reading.

If possible, it’s a good idea to look through the input file in the shell or in an editor before reading into R to catch such issues in advance. Using _less_ on _RTADataSub.csv_ would have revealed these various issues, but note that _RTADataSub.csv_ is a 1000-line subset of a much larger file of data available from the kaggle.com website.

The basic function _scan()_ simply reads everything in, ignoring lines, which works well and very quickly if you are reading in a numeric vector or matrix. _scan()_ is also useful if your file is free format - i.e., if it’s not one line per observation, but just all the data one value after another; in this case you can use _scan()_ to read it in and then format the resulting character or numeric vector as a matrix with as many columns as fields in the dataset. Remember that the default is to fill the matrix by column.

If the file is not nicely arranged by field (e.g., if it has ragged lines), we’ll need to do some more work. _readLines()_ will read in each line into a separate character vector, after which we can process the lines using text manipulation. Here’s an example from some US meteorological data where I know from metadata (not provided here) that the 4-11th values are an identifier, the 17-20th are the year, the 22-23rd the month, etc.

dat <- **readLines** ("../data/precip.txt") id <- **as.factor** ( **substring** (dat, 4, 11)) year <- **substring** (dat, 17, 20) year[1:5] ## [1] "I201" "I201" "I201" "I201" "I201" **class** (year) ## [1] "character"

4

year <- **as.integer** ( **substring** (dat, 18, 21)) month <- **as.integer** ( **substring** (dat, 22, 23)) nvalues <- **as.integer** ( **substring** (dat, 28, 30))

Note that for precip.txt, reading in using _read.fwf()_ would be a good strategy.

R allows you to read in not just from a file but from a more general construct called a _connection_ . Here are some examples of connections:

dat <- **readLines** ( **pipe** ("ls -al")) dat <- **read.table** ( **pipe** ("unzip dat.zip")) dat <- **read.csv** ( **gzfile** ("dat.csv.gz")) dat <- **readLines** ("http://www.stat.berkeley.edu/~paciorek/index.html")

If a file is large, we may want to read it in in chunks (of lines), do some computations to reduce the size of things, and iterate. _read.table()_ , _read.fwf()_ and _readLines()_ all have the arguments that let you read in a fixed number of lines. To read-on-the-fly in blocks, we need to first establish the connection and then read from it sequentially.

con <- **file** ("../data/precip.txt", "r") _# 'r' for 'read' - you can also open files for writing # with 'w' (or 'a' for appending)_ **class** (con) blockSize <- 1000 _# obviously this would be large in any real application_ nLines <- 3e+05 **for** (i **in** 1: **ceiling** (nLines/blockSize)) { lines <- **readLines** (con, n = blockSize) _# manipulate the lines and store the key stuff_ } **close** (con)

One cool trick that can come in handy is to create a _text connection_ . This lets you ’read’ from an R character vector as if it were a text file and could be handy for processing text. For example, you could then use _read.fwf()_ applied to _con_ .

dat <- **readLines** ("../data/precip.txt") con <- **textConnection** (dat[1], "r") **read.fwf** (con, **c** (3, 8, 4, 2, 4, 2))

5

---

[← 1 Data storage and formats (outside R)](01-1-data-storage-and-formats-outside-r.md) · [Up: contents](index.md) · [V1 V2 V3 V4 V5 V6 ## 1 DLY 1000807 PRCP HI 2010 2 →](03-v1-v2-v3-v4-v5-v6-1-dly-1000807-prcp-hi-2010-2.md)
