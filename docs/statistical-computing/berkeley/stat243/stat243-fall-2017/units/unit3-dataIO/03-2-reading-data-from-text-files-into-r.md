---
title: 2 Reading data from text files into R
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Reading data from text files into R

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Core R functions**

_read.table()_ is probably the most commonly-used function for reading in data. It reads in delimited files ( _read.csv()_ and _read.delim()_ are special cases of _read.table()_ ). The key arguments are the delimiter (the _sep_ argument) and whether the file contains a header, a line with the variable names. We can use _read.fwf()_ to read from a fixed width text file into a data frame.

The most difficult part of reading in such files can be dealing with how R determines the classes of the fields that are read in. There are a number of arguments to _read.table()_ and _read.fwf()_ that allow the user to control the classes. One difficulty is that character and numeric fields are sometimes read in as factors. Basically _read.table()_ tries to read fields in as numeric and if it finds non-numeric and non-NA values, it reads in as a factor. This can be annoying.

Let’s work through a couple examples. Before we do that, let’s look at the arguments to _read.table()_ . Note that _sep=”_ separates on any amount of white space. In the code chunk below, I’ve told _knitr_ not to print the output to the PDF; we’ll see the full output in class during the demo.

**getwd** () _# a common error is not knowing what directory R is looking at_ **setwd** ('../data') dat <- **read.table** ('RTADataSub.csv', sep = ',', head = TRUE) **sapply** (dat, class) **levels** (dat[ ,2]) dat2 <- **read.table** ('RTADataSub.csv', sep = ',', head = TRUE, na.strings = **c** ("NA", "x"), stringsAsFactors = FALSE) **unique** (dat2[ ,2]) _## hmmm, what happened to the blank values this time?_ **which** (dat[ ,2] == "") dat2[ **which** (dat[, 2] == "")[1], ] _# deconstruct it! # using 'colClasses'_ sequ <- **read.table** ('hivSequ.csv', sep = ',', header = TRUE,

4

colClasses = **c** ('integer','integer','character', 'character','numeric','integer')) _## let's make sure the coercion worked - sometimes R is obstinant_ **sapply** (sequ, class)

_## that made use of the fact that a data frame is a list_

Note that you can avoid reading in one or more columns by specifying _NULL_ as the column class for those columns to be omitted. Also, specifying the _colClasses_ argument explicitly should make for faster file reading. Finally, setting stringsAsFactors=FALSE is standard practice. You can set that by default to apply generally in your _.Rprofile_ using options(stringsAsFactors = FALSE). Or use _readr::read_csv()_ as discussed below.

If possible, it’s a good idea to look through the input file in the shell or in an editor before reading into R to catch such issues in advance. Using _less_ on _RTADataSub.csv_ would have revealed these various issues, but note that _RTADataSub.csv_ is a 1000-line subset of a much larger file of data available from the kaggle.com website. So more sophisticated use of UNIX utilities as we saw in Unit 2 is often useful before trying to read something into R.

The basic function _scan()_ simply reads everything in, ignoring lines, which works well and very quickly if you are reading in a numeric vector or matrix. _scan()_ is also useful if your file is free format - i.e., if it’s not one line per observation, but just all the data one value after another; in this case you can use _scan()_ to read it in and then format the resulting character or numeric vector as a matrix with as many columns as fields in the dataset. Remember that the default is to fill the matrix by column.

If the file is not nicely arranged by field (e.g., if it has ragged lines), we’ll need to do some more work. _readLines()_ will read in each line into a separate character vector, after which we can process the lines using text manipulation. Here’s an example from some US meteorological data where I know from metadata (not provided here) that the 4-11th values are an identifier, the 17-20th are the year, the 22-23rd the month, etc.

dat <- **readLines** ('../data/precip.txt') id <- **as.factor** ( **substring** (dat, 4, 11) ) year <- **substring** (dat, 18, 21) year[1:5] ## [1] "2010" "2010" "2010" "2010" "2010" **class** (year) ## [1] "character"

5

year <- **as.integer** ( **substring** (dat, 18, 21)) month <- **as.integer** ( **substring** (dat, 22, 23)) nvalues <- **as.integer** ( **substring** (dat, 28, 30))

Note that for _precip.txt_ , reading in using _read.fwf()_ would be a good strategy.

R allows you to read in not just from a file but from a more general construct called a _connection_ . Here are some examples of connections:

dat <- **readLines** ( **pipe** ("ls -al")) dat <- **read.table** ( **pipe** ("unzip dat.zip")) dat <- **read.csv** ( **gzfile** ("dat.csv.gz")) dat <- **readLines** ("http://www.stat.berkeley.edu/~paciorek/index.html")

In some cases, you might need to create the connection using _url()_ or using the _curl()_ function from the _curl_ package. Though for the example here, simply passing the URL to _readLines()_ does work. (In general, _curl::curl()_ provides some nice features for reading off the internet.)

wikip1 <- **readLines** ("https://wikipedia.org") wikip2 <- **readLines** ( **url** ("https://wikipedia.org")) **library** (curl) wikip3 <- **readLines** ( **curl** ("https://wikipedia.org"))

If a file is large, we may want to read it in in chunks (of lines), do some computations to reduce the size of things, and iterate. _read.table()_ , _read.fwf()_ and _readLines()_ all have the arguments that let you read in a fixed number of lines. To read-on-the-fly in blocks, we need to first establish the connection and then read from it sequentially.

con <- **file** ("../data/precip.txt", "r") _## "r" for 'read' - you can also open files for writing with "w" ## (or "a" for appending)_ **class** (con) blockSize <- 1000 _# obviously this would be large in any real application_ nLines <- 300000 **for** (i **in** 1: **ceiling** (nLines / blockSize)){ lines <- **readLines** (con, n = blockSize) _# manipulate the lines and store the key stuff_ } **close** (con)

6

Here’s an example of using _curl()_ to do this for a file on the web.

URL <- "https://www.stat.berkeley.edu/share/paciorek/2008.csv.gz" con <- **gzcon** ( **curl** (URL, open = "r")) _## url() in place of curl() works too_ **for** (i **in** 1:8) { **print** (i) **print** ( **system.time** (tmp <- **readLines** (con, n = 100000))) **print** (tmp[1]) } ## [1] 1 ## user system elapsed ## 0.736 0.008 0.745 ## [1] ## [1] 2 ## user system elapsed ## 0.624 0.004 0.631 ## [1] "2008,1,29,2,1938,1935,2308,2257,XE,7676,N11176,150,142,104,11,3,SLC,OKC,866,5,41,0,,0,NA,NA,NA,NA,NA" ## [1] 3 ## user system elapsed ## 0.544 0.000 0.543 ## [1] "2008,1,20,7,1540,1525,1651,1637,OO,5703,N227SW,71,72,58,14,15,SBA,SJC,234,5,8,0,,0,NA,NA,NA,NA,NA" ## [1] 4 ## user system elapsed ## 0.532 0.000 0.536 ## [1] "2008,1,2,3,1313,1250,1443,1425,WN,440,N461WN,150,155,138,18,23,MCO,STL,880,3,9,0,,0,2,0,0,0,16" ## [1] 5 ## user system elapsed ## 0.532 0.004 0.538 ## [1] "2008,1,24,4,1026,1015,1116,1110,MQ,3926,N653AE,50,55,38,6,11,MLI,ORD,139,6,6,0,,0,NA,NA,NA,NA,NA" ## [1] 6 ## user system elapsed ## 0.544 0.000 0.544 ## [1] "2008,1,4,5,1129,1125,1352,1350,AA,1145,N438AA,203,205,187,2,4,ORD,SLC,1249,3,13,0,,0,NA,NA,NA,NA,NA" ## [1] 7 ## user system elapsed

7

---

[← 1 Data storage and formats (outside R)](02-1-data-storage-and-formats-outside-r.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 04 — →](04-unit-03-dataio-part-04.md)
