---
title: 2 Reading data from text files into R
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit2-dataTech.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit2-dataTech.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Reading data from text files into R

## 2.1 Core R functions

*read.table()* is probably the most commonly-used function for reading in data. It reads in delimited
files (*read.csv()* and *read.delim()* are special cases of *read.table()*). The key arguments are the
delimiter (the *sep* argument) and whether the file contains a header, a line with the variable names.
We can use *read.fwf()* to read from a fixed width text file into a data frame.

The most difficult part of reading in such files can be dealing with how R determines the classes
of the fields that are read in. There are a number of arguments to *read.table()* and *read.fwf()* that
allow the user to control the classes. One difficulty in older versions of R was that character fields
were read in as factors.

Let’s work through a couple examples. Before we do that, let’s look at the arguments to
*read.table()*. Note that sep=” separates on any amount of white space. In the code chunk below, I’ve told knitr not to print the output to the PDF; you can see the full output by running the
code yourself.

```r
dat <- read.table(file.path('..', 'data', 'RTADataSub.csv'),
sep = ',', header = TRUE)
sapply(dat, class)
## whoops, there is an 'x', presumably indicating missingness:
unique(dat[ , 2])
## let's treat 'x' as a missing value indicator
dat2 <- read.table(file.path('..', 'data', 'RTADataSub.csv'),
sep = ',', header = TRUE,
na.strings = c("NA", "x"))
unique(dat2[ ,2])
## hmmm, what happened to the blank values this time?
which(dat[ ,2] == "")
dat2[which(dat[, 2] == "")[1], ] # pull out a line with a missing string

# using 'colClasses'
sequ <- read.table(file.path('..', 'data', 'hivSequ.csv'),
sep = ',', header = TRUE,
colClasses = c('integer','integer','character',
'character','numeric','integer'))
## let's make sure the coercion worked - sometimes R is obstinant
sapply(sequ, class)
## that made use of the fact that a data frame is a list
```

Note that you can avoid reading in one or more columns by specifying NULL as the column
class for those columns to be omitted. Also, specifying the *colClasses* argument explicitly should
make for faster file reading. Finally, setting `stringsAsFactors=FALSE` is standard practice
and is the default in R as of version 4.0. (`readr::read_csv()` has always set `stringsAsFactors=FALSE`.

If possible, it’s a good idea to look through the input file in the shell or in an editor before
reading into R to catch such issues in advance. Using *less* on *RTADataSub.csv* would have revealed
these various issues, but note that *RTADataSub.csv* is a 1000-line subset of a much larger file of
data available from the kaggle.com website. So more sophisticated use of UNIX utilities as we
saw in Unit 2 is often useful before trying to read something into R.

The basic function *scan()* simply reads everything in, ignoring lines, which works well and
very quickly if you are reading in a numeric vector or matrix. *scan()* is also useful if your file is
free format - i.e., if it’s not one line per observation, but just all the data one value after another; in
this case you can use *scan()* to read it in and then format the resulting character or numeric vector
as a matrix with as many columns as fields in the dataset. Remember that the default is to fill the
matrix by column.

If the file is not nicely arranged by field (e.g., if it has ragged lines), we’ll need to do some
more work. *readLines()* will read in each line into a separate character vector, after which we
can process the lines using text manipulation. Here’s an example from some US meteorological
data where I know from metadata (not provided here) that the 4-11th values are an identifier, the
17-20th are the year, the 22-23rd the month, etc.

```r
dat <- readLines(file.path('..', 'data', 'precip.txt'))
id <- as.factor(substring(dat, 4, 11) )
year <- substring(dat, 18, 21)
year[1:5]
## [1] "2010" "2010" "2010" "2010" "2010"
class(year)
## [1] "character"
year <- as.integer(substring(dat, 18, 21))
month <- as.integer(substring(dat, 22, 23))
nvalues <- as.integer(substring(dat, 28, 30))
```

Actually, that file, *precip.txt*, is in a fixed-width format (i.e., every element in a given column has
the exact same number of characters),so reading in using *read.fwf()* would be a good strategy.

R allows you to read in not just from a file but from a more general construct called a *connection*. Here are some examples of connections:

```r
dat <- readLines(pipe("ls -al"))
dat <- read.table(pipe("unzip dat.zip"))
dat <- read.csv(gzfile("dat.csv.gz"))
dat <- readLines("http://www.stat.berkeley.edu/~paciorek/index.html")
```

In some cases, you might need to create the connection using *url()* or using the *curl()* function
from the curl package. Though for the example here, simply passing the URL to *readLines()* does
work. (In general, *curl::curl()* provides some nice features for reading off the internet.)

```r
wikip1 <- readLines("https://wikipedia.org")
wikip2 <- readLines(url("https://wikipedia.org"))
library(curl)
## Using libcurl 7.68.0 with GnuTLS/3.6.13
wikip3 <- readLines(curl("https://wikipedia.org"))
```

If a file is large, we may want to read it in in chunks (of lines), do some computations to reduce
the size of things, and iterate. *read.table()*, *read.fwf()* and *readLines()* all have the arguments that
let you read in a fixed number of lines. To read-on-the-fly in blocks, we need to first establish the
connection and then read from it sequentially. (If you don’t, you’ll read from the start of the file
every time you read from the file.)

```r
con <- file(file.path("..", "data", "precip.txt"), "r")
## "r" for 'read' - you can also open files for writing with "w"
## (or "a" for appending)
class(con)
blockSize <- 1000 # obviously this would be large in any real application
nLines <- 300000
for(i in 1:ceiling(nLines / blockSize)){
lines <- readLines(con, n = blockSize)
# manipulate the lines and store the key stuff
}
close(con)
```

Here’s an example of using *curl()* to do this for a file on the web.

```r
URL <- "https://www.stat.berkeley.edu/share/paciorek/2008.csv.gz"
con <- gzcon(curl(URL, open = "r"))
## url() in place of curl() works too
for(i in 1:8) {
print(i)
print(system.time(tmp <- readLines(con, n = 100000)))
print(tmp[1])
}
## [1] 1
## user system elapsed
## 0.583 0.000 0.583
## [1] "Year,Month,DayofMonth,DayOfWeek,DepTime,CRSDepTime,ArrTime,CRSArrTime,UniqueCarrier,FlightNum,TailNum,ActualElapsedTime,CRSElapsedTime,AirTime,ArrDelay,DepDelay,Origin,Dest,Distance,TaxiIn,TaxiOut,Cancelled,CancellationCode,Diverted,CarrierDelay,WeatherDelay,NASDelay,SecurityDelay,LateAircraftDelay"
## [1] 2
## user system elapsed
## 0.562 0.002 0.564
## [1] "2008,1,29,2,1938,1935,2308,2257,XE,7676,N11176,150,142,104,11,3,SLC,OKC,866,5,41,0,,0,NA,NA,NA,NA,NA"
## [1] 3
## user system elapsed
## 0.572 0.000 0.573
## [1] "2008,1,20,7,1540,1525,1651,1637,OO,5703,N227SW,71,72,58,14,15,SBA,SJC,234,5,8,0,,0,NA,NA,NA,NA,NA"
## [1] 4
## user system elapsed
## 0.554 0.000 0.554
## [1] "2008,1,2,3,1313,1250,1443,1425,WN,440,N461WN,150,155,138,18,23,MCO,STL,880,3,9,0,,0,2,0,0,0,16"
## [1] 5
## user system elapsed
## 0.547 0.000 0.548
## [1] "2008,1,24,4,1026,1015,1116,1110,MQ,3926,N653AE,50,55,38,6,11,MLI,ORD,139,6,6,0,,0,NA,NA,NA,NA,NA"
## [1] 6
## user system elapsed
## 0.561 0.000 0.561
## [1] "2008,1,4,5,1129,1125,1352,1350,AA,1145,N438AA,203,205,187,2,4,ORD,SLC,1249,3,13,0,,0,NA,NA,NA,NA,NA"
## [1] 7
## user system elapsed
## 0.547 0.000 0.547
## [1] "2008,1,10,4,716,720,1025,1024,DL,1590,N991DL,129,124,107,1,-4,AUS,ATL,813,6,16,0,,0,NA,NA,NA,NA,NA"
## [1] 8
## user system elapsed
## 0.558 0.000 0.558
## [1] "2008,2,15,5,2127,2132,2254,2312,XE,7663,N33182,87,100,71,-18,-5,SLC,ABQ,493,6,10,0,,0,NA,NA,NA,NA,NA"
close(con)
```

More details on sequential (on-line) processing of large files can be found in the tutorial on
large datasets mentioned in the reference list above.

One cool trick that can come in handy is to create a *text connection*. This lets you 'read' from
an R character vector as if it were a text file and could be handy for processing text. For example,
you could then use *read.fwf()* applied to con.

```r
dat <- readLines('../data/precip.txt')
con <- textConnection(dat[1], "r")
read.fwf(con, c(3,8,4,2,4,2))
## V1 V2 V3 V4 V5 V6
## 1 DLY 1000807 PRCP HI 2010 2
```

We can create connections for writing output too. Just make sure to open the connection first.

## 2.2 File paths

A few notes on file paths, related to ideas of reproducibility.

1. In general, you don’t want to hard-code absolute paths into your code files because those absolute paths won’t be available on the machines of anyone you share the code with. Instead,
use paths relative to the directory the code file is in, or relative to a baseline directory for the
project, e.g.:

```r
dat <- read.csv('../data/cpds.csv')
```

2. Be careful with the directory separator in Windows files: you can either do “C:\\\\mydir\\\\file.txt”
or “C:/mydir/file.txt”, but not “C:\mydir\file.txt”, and note the next comment about avoiding
use of '\\' for portability.

3. Using UNIX style directory separators will work in Windows, Mac or Linux, but using
Windows style separators is not portable across operating systems.

```r
## good: will work on Windows
dat <- read.csv('../data/cpds.csv')
## bad: won't work on Mac or Linux
dat <- read.csv('..\\data\\cpds.csv')
```

4. Even better, use *file.path()* so that paths are constructed specifically for the operating system
the user is using:

```r
## good: operating-system independent
dat <- read.csv(file.path('..', 'data', 'cpds.csv'))
```

## 2.3 The readr package

*readr* is intended to deal with some of the shortcomings of the base R functions, such as defaulting
to `stringsAsFactors=FALSE` (no longer relevant with R 4.0), leaving column names unmodified, and recognizing dates/times. It reads data in much more quickly than the base R equivalents.
See this blog post. Some of the readr functions that are analogs to the comparably-named base R
functions are `read_csv()`, `read_fwf()`, `read_lines()`, and `read_table()`.

Let’s try out `read_csv()` on the airline dataset used in the R bootcamp.

```r
library(readr)
##
## Attaching package: ’readr’
## The following object is masked from ’package:curl’:
##
## parse_date
## I'm violating the rule about absolute paths here!!
## (airline.csv is big enough that I don't want to put it in the
## course repository)
setwd('~/staff/workshops/r-bootcamp-fall-2020/data')
system.time(dat <- read.csv('airline.csv', stringsAsFactors = FALSE))
## user system elapsed
## 4.072 0.186 4.266
system.time(dat2 <- read_csv('airline.csv'))
## Rows: 539895 Columns: 29
## - Column specification ---------------------
## Delimiter: ","
## chr (5): UniqueCarrier, TailNum, Origin, Dest, Canc...
## dbl (24): Year, Month, DayOfMonth, DayOfWeek, DepTim...
##
## i Use ‘spec()‘ to retrieve the full column specification for this
data.
## i Specify the column types or set ‘show_col_types = FALSE‘ to quiet
this message.
## user system elapsed
## 1.714 0.045 1.016
```

## 2.4 Reading data quickly

In addition to the tips above, there are a number of packages that allow one to read large data files
quickly, in particular *data.table*, *ff*, and *bigmemory*. In general, these provide the ability to load
datasets into R without having them in memory, but rather stored in clever ways on disk that allow
for fast access. Metadata is stored in R. More on this in the unit on big data and in the tutorial on
large datasets mentioned in the reference list above.

---

[← 1 Data storage and file formats on a computer](01-1-data-storage-and-file-formats-on-a-computer.md) · [Up: contents](index.md) · [3 Output from R →](03-3-output-from-r.md)
