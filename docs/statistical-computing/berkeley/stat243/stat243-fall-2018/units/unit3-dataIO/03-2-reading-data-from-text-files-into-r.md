---
title: 2 Reading data from text files into R
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Reading data from text files into R

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Core R functions**

_read.table()_ is probably the most commonly-used function for reading in data. It reads in delimited files ( _read.csv()_ and _read.delim()_ are special cases of _read.table()_ ). The key arguments are the delimiter (the _sep_ argument) and whether the file contains a header, a line with the variable names. We can use _read.fwf()_ to read from a fixed width text file into a data frame.

The most difficult part of reading in such files can be dealing with how R determines the classes of the fields that are read in. There are a number of arguments to _read.table()_ and _read.fwf()_ that allow the user to control the classes. One difficulty is that character and numeric fields are

3

sometimes read in as factors. Basically _read.table()_ tries to read fields in as numeric and if it finds non-numeric and non-NA values, it reads in as a factor. This can be annoying.

Let’s work through a couple examples. Before we do that, let’s look at the arguments to _read.table()_ . Note that _sep=”_ separates on any amount of white space. In the code chunk below, I’ve told _knitr_ not to print the output to the PDF; you can see the full output by running the code yourself.

dat <- **read.table** ( **file.path** ('..', 'data', 'RTADataSub.csv'), sep = ',', head = TRUE) **sapply** (dat, class) _## whoops, there is an 'x', presumably indicating missingness:_ **levels** (dat[ ,2]) _## let's treat 'x' as a missing value indicator_ dat2 <- **read.table** ( **file.path** ('..', 'data', 'RTADataSub.csv'), sep = ',', head = TRUE, na.strings = **c** ("NA", "x"), stringsAsFactors = FALSE) **unique** (dat2[ ,2]) _## hmmm, what happened to the blank values this time?_ **which** (dat[ ,2] == "") dat2[ **which** (dat[, 2] == "")[1], ] _# pull out a line with a missing string # using 'colClasses'_ sequ <- **read.table** ( **file.path** ('..', 'data', 'hivSequ.csv'), sep = ',', header = TRUE, colClasses = **c** ('integer','integer','character', 'character','numeric','integer')) _## let's make sure the coercion worked - sometimes R is obstinant_ **sapply** (sequ, class) _## that made use of the fact that a data frame is a list_

Note that you can avoid reading in one or more columns by specifying _NULL_ as the column class for those columns to be omitted. Also, specifying the _colClasses_ argument explicitly should make for faster file reading. Finally, setting stringsAsFactors=FALSE is standard practice. You can set that by default to apply generally in your _.Rprofile_ using options(stringsAsFactors = FALSE). Or use _readr::read_csv()_ as discussed below.

If possible, it’s a good idea to look through the input file in the shell or in an editor before reading into R to catch such issues in advance. Using _less_ on _RTADataSub.csv_ would have revealed

4

these various issues, but note that _RTADataSub.csv_ is a 1000-line subset of a much larger file of data available from the kaggle.com website. So more sophisticated use of UNIX utilities as we saw in Unit 2 is often useful before trying to read something into R.

The basic function _scan()_ simply reads everything in, ignoring lines, which works well and very quickly if you are reading in a numeric vector or matrix. _scan()_ is also useful if your file is free format - i.e., if it’s not one line per observation, but just all the data one value after another; in this case you can use _scan()_ to read it in and then format the resulting character or numeric vector as a matrix with as many columns as fields in the dataset. Remember that the default is to fill the matrix by column.

If the file is not nicely arranged by field (e.g., if it has ragged lines), we’ll need to do some more work. _readLines()_ will read in each line into a separate character vector, after which we can process the lines using text manipulation. Here’s an example from some US meteorological data where I know from metadata (not provided here) that the 4-11th values are an identifier, the 17-20th are the year, the 22-23rd the month, etc.

dat <- **readLines** ( **file.path** ('..', 'data', 'precip.txt')) id <- **as.factor** ( **substring** (dat, 4, 11) ) year <- **substring** (dat, 18, 21) year[1:5] ## [1] "2010" "2010" "2010" "2010" "2010"

**class** (year) ## [1] "character" year <- **as.integer** ( **substring** (dat, 18, 21)) month <- **as.integer** ( **substring** (dat, 22, 23)) nvalues <- **as.integer** ( **substring** (dat, 28, 30))

Note that for _precip.txt_ , reading in using _read.fwf()_ would be a good strategy.

R allows you to read in not just from a file but from a more general construct called a _connection_ . Here are some examples of connections:

dat <- **readLines** ( **pipe** ("ls -al")) dat <- **read.table** ( **pipe** ("unzip dat.zip")) dat <- **read.csv** ( **gzfile** ("dat.csv.gz")) dat <- **readLines** ("http://www.stat.berkeley.edu/~paciorek/index.html")

5

In some cases, you might need to create the connection using _url()_ or using the _curl()_ function from the _curl_ package. Though for the example here, simply passing the URL to _readLines()_ does work. (In general, _curl::curl()_ provides some nice features for reading off the internet.)

wikip1 <- **readLines** ("https://wikipedia.org") wikip2 <- **readLines** ( **url** ("https://wikipedia.org")) **library** (curl) wikip3 <- **readLines** ( **curl** ("https://wikipedia.org"))

If a file is large, we may want to read it in in chunks (of lines), do some computations to reduce the size of things, and iterate. _read.table()_ , _read.fwf()_ and _readLines()_ all have the arguments that let you read in a fixed number of lines. To read-on-the-fly in blocks, we need to first establish the connection and then read from it sequentially.

con <- **file** ( **file.path** ("..", "data", "precip.txt"), "r") _## "r" for 'read' - you can also open files for writing with "w" ## (or "a" for appending)_ **class** (con) blockSize <- 1000 _# obviously this would be large in any real application_ nLines <- 300000 **for** (i **in** 1: **ceiling** (nLines / blockSize)){ lines <- **readLines** (con, n = blockSize) _# manipulate the lines and store the key stuff_ } **close** (con)

Here’s an example of using _curl()_ to do this for a file on the web.

URL <- "https://www.stat.berkeley.edu/share/paciorek/2008.csv.gz" con <- **gzcon** ( **curl** (URL, open = "r")) _## url() in place of curl() works too_ **for** (i **in** 1:8) { **print** (i) **print** ( **system.time** (tmp <- **readLines** (con, n = 100000))) **print** (tmp[1]) } ## [1] 1

6

---

[← 1 Data storage and formats (outside R)](02-1-data-storage-and-formats-outside-r.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 04 — →](04-unit-03-dataio-part-04.md)
