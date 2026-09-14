---
title: 2. Reading data from text files into R
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit2-dataTech.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Reading data from text files into R

**Source:** [`units/unit2-dataTech.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Core R functions

*read.table()* is probably the most commonly-used function for reading
in data. It reads in delimited files (*read.csv()* and *read.delim()*
are special cases of *read.table()*). The key arguments are the
delimiter (the *sep* argument) and whether the file contains a header, a
line with the variable names. We can use *read.fwf()* to read from a
fixed width text file into a data frame.

The most difficult part of reading in such files can be dealing with how
R determines the classes of the fields that are read in. There are a
number of arguments to *read.table()* and *read.fwf()* that allow the
user to control the classes. One difficulty in older versions of R was
that character fields were read in as factors.

Let's work through a couple examples. Before we do that, let's look at
the arguments to *read.table()*. Note that `sep=''` separates on any
amount of white space.

```r
dat <- read.table(file.path('..', 'data', 'RTADataSub.csv'),
                  sep = ',', header = TRUE)
sapply(dat, class)[1:10]  # What are the classes of the columns?
## whoops, there is an 'x', presumably indicating missingness:
unique(dat[ , 2])
## let's treat 'x' as a missing value indicator
dat2 <- read.table(file.path('..', 'data', 'RTADataSub.csv'),
                   sep = ',', header = TRUE,
                   na.strings = c("NA", "x"))
unique(dat2[ , 2])
## Let's check that the empty strings from 'dat' are now NAs in 'dat2'
which(dat[ , 2] == "")[1:10]
dat2[which(dat[, 2] == "")[1], ] # pull out a line with a missing string
```

Using `colClasses` is a good way to control how data are read in.

```r
sequ <- read.table(file.path('..', 'data', 'hivSequ.csv'),
  sep = ',', header = TRUE,
  colClasses = c('integer','integer','character',
    'character','numeric','integer'))
## let's make sure the coercion worked - sometimes R is obstinant
sapply(sequ, class)
## that made use of the fact that a data frame is a list
```

Note that you can avoid reading in one or more columns by specifying
*NULL* as the column class for those columns to be omitted. Also,
specifying the *colClasses* argument explicitly should make for faster
file reading. Finally, setting `stringsAsFactors=FALSE` is standard
practice and is the default in R as of version 4.0. (*readr::read_csv()*
has always set `stringsAsFactors=FALSE`).

If possible, it's a good idea to look through the input file in the
shell or in an editor before reading into R to catch such issues in
advance. Using the UNIX command *less* on *RTADataSub.csv* would have revealed these
various issues, but note that *RTADataSub.csv* is a 1000-line subset of
a much larger file of data available from the kaggle.com website. So
more sophisticated use of UNIX utilities (as we will see in Unit 3) is often
useful before trying to read something into a program.

The basic function *scan()* simply reads everything in, ignoring lines,
which works well and very quickly if you are reading in a numeric vector
or matrix. *scan()* is also useful if your file is free format - i.e.,
if it's not one line per observation, but just all the data one value
after another; in this case you can use *scan()* to read it in and then
format the resulting character or numeric vector as a matrix with as
many columns as fields in the dataset. Remember that the default is to
fill the matrix by column.

If the file is not nicely arranged by field (e.g., if it has ragged
lines), we'll need to do some more work. *readLines()* will read in each
line into a separate character vector, after which we can process the
lines using text manipulation. Here's an example from some US
meteorological data where I know from metadata (not provided here) that
the 4-11th values are an identifier, the 17-20th are the year, the
22-23rd the month, etc.

```r
dat <- readLines(file.path('..', 'data', 'precip.txt'))
id <- as.factor(substring(dat, 4, 11) )
year <- substring(dat, 18, 21)
year[1:5]
class(year)
year <- as.integer(substring(dat, 18, 21))
month <- as.integer(substring(dat, 22, 23))
nvalues <- as.integer(substring(dat, 28, 30))
```


Actually, that file, *precip.txt*, is in a fixed-width format (i.e.,
every element in a given column has the exact same number of
characters),so reading in using *read.fwf()* would be a good strategy.

## Connections

R allows you to read in not just from a file but from a more general
construct called a *connection*. This can include reading in text from the output of running a shell command and from unzipping a file on the fly.

Here are some examples of connections:

```r
dat <- readLines(pipe("ls -al"))
dat <- read.table(pipe("unzip dat.zip"))
dat <- read.csv(gzfile("dat.csv.gz"))
dat <- readLines("http://www.stat.berkeley.edu/~paciorek/index.html")
```


In some cases, you might need to create the connection using *url()* or
using the *curl()* function from the *curl* package. Though for the
example here, simply passing the URL to *readLines()* does work. (In
general, *curl::curl()* provides some nice features for reading off the
internet.)

```r
wikip1 <- readLines("https://wikipedia.org")
wikip2 <- readLines(url("https://wikipedia.org"))
library(curl)
wikip3 <- readLines(curl("https://wikipedia.org"))
```

If a file is large, we may want to read it in in chunks (of lines), do
some computations to reduce the size of things, and iterate. This is referred
to as online processing.
*read.table()*, *read.fwf()* and *readLines()* all have the arguments
that let you read in a fixed number of lines. To read-on-the-fly in
blocks, we need to first establish the connection and then read from it
sequentially. (If you don't, you'll read from the start of the file
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
 


Here's an example of using *curl()* to do this for a file on the web.

```r
URL <- "https://www.stat.berkeley.edu/share/paciorek/2008.csv.gz"
con <- gzcon(curl(URL, open = "r"))
## url() in place of curl() works too
for(i in 1:4) {   ## Read in first four chunks as an example
	print(i)
	print(system.time(tmp <- readLines(con, n = 100000)))
	print(tmp[1])
}
close(con)
```

More details on sequential (on-line) processing of large files can be
found in the tutorial on large datasets mentioned in the reference list
above.

One cool trick that can come in handy is to create a *text connection*.
This lets you 'read' from an R character vector as if it were a text
file and could be handy for processing text. For example, you could then
use *read.fwf()* applied to *con*.

```r
dat <- readLines('../data/precip.txt')
con <- textConnection(dat[1], "r")
read.fwf(con, c(3,8,4,2,4,2))
```


We can create connections for writing output too. Just make sure to open
the connection first.

## File paths

A few notes on file paths, related to ideas of reproducibility.

1.  In general, you don't want to hard-code absolute paths into your
    code files because those absolute paths won't be available on the
    machines of anyone you share the code with. Instead, use paths
    relative to the directory the code file is in, or relative to a
    baseline directory for the project, e.g.:\

    ```r
    dat <- read.csv('../data/cpds.csv')
    ```

2.  Be careful with the directory separator in Windows files: you can
    either do `C:\\mydir\\file.txt` or `C:/mydir/file.txt`, but
    not `C:\mydir\file.txt`, and note the next comment about
    avoiding use of '\\' for portability.

3.  Using UNIX style directory separators will work in Windows, Mac or
    Linux, but using Windows style separators is not portable across
    operating systems.\

    ```r
    ## good: will work on Windows
    dat <- read.csv('../data/cpds.csv')
    ## bad: won't work on Mac or Linux
    dat <- read.csv('..\\data\\cpds.csv')
    ```

4.  Even better, use *file.path()* so that paths are constructed
    specifically for the operating system the user is using:\

    ```r
    ## good: operating-system independent
    dat <- read.csv(file.path('..', 'data', 'cpds.csv'))
    ```

## The *readr* package

*readr* is intended to deal with some of the shortcomings of the base R
functions, such as leaving column names unmodified, and recognizing
dates/times. It reads data in much more quickly than the base R
equivalents. See [this blog
post](http://blog.rstudio.org/2015/04/09/readr-0-1-0/). Some of the
readr functions that are analogs to the comparably-named base R
functions are *read_csv()*, *read_fwf()*, *read_lines()*, and
*read_table()*.

Let's try out *read_csv()* on the airline dataset used in the R
bootcamp.

```r
library(readr)
## I'm violating the rule about absolute paths here!!
## (airline.csv is big enough that I don't want to put it in the
##    course repository)
dir <- "../data"
system.time(dat <- read.csv(file.path(dir, 'airline.csv'), stringsAsFactors = FALSE))
system.time(dat2 <- read_csv(file.path(dir, 'airline.csv')))
```


## Reading data quickly

In addition to the tips above, there are a number of packages that allow
one to read large data files quickly, in particular *data.table*, *arrow*,
and *fst*. In general, these provide the ability to load datasets
into R without having them in memory, but rather stored in clever ways
on disk that allow for fast access. Metadata is stored in R. More on
this in the unit on big data and in the tutorial on large datasets
mentioned in the reference list above.

---

[← 1. Data storage and file formats on a computer](02-1-data-storage-and-file-formats-on-a-computer.md) · [Up: contents](index.md) · [3. Output from R →](04-3-output-from-r.md)
