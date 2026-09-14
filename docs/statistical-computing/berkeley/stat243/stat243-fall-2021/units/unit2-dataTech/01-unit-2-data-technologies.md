---
title: 'Unit 2: Data technologies'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit2-dataTech.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 2: Data technologies

**Source:** [`units/unit2-dataTech.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

August 30, 2021

References:

- Adler

- Nolan and Temple Lang, XML and Web Technologies for Data Sciences with R.

- Chambers

- R intro manual on CRAN (R-intro).

- Venables and Ripley, Modern Applied Statistics with S

- Murrell, Introduction to Data Technologies.

- R Data Import/Export manual on CRAN (R-data).

- SCF tutorial on “Working with large datasets in SQL, R, and Python”, available from http://statistics.berkeley.edu/computing/training/tutorials.

## **(Optional) Videos**

There are four videos from 2020 in the bCourses Media Gallery that you can use for reference if you want to:

1. Text files and ASCII

2. Encodings and UTF-8

3. HTML

4. XML and JSON

1

## **1 Data storage and file formats on a computer**

We’re going to start early in the data analysis pipeline: getting data, reading data in, writing data out to disk, and webscraping. We’ll focus on doing these manipulations in R, but the concepts and tools involved are common to other languages, so familarity with these in R should allow you to pick up other tools more easily. The main downside to working with datasets in R (true for Python as well) is that the entire dataset resides in memory, so R is not so good for dealing with very large datasets. More on alternatives in a later unit. Another common frustration is controlling how the variables are interpreted (numeric, character, factor) when reading data into a data frame. R (and similar languages) has the capability to read in a wide variety of file formats.

### **1.1 Text and binary files**

In general, files can be divided into text files and binary files. In both cases, information is stored as a series of bits. Recall that a bit is a single value in base 2 (i.e., a 0 or a 1), while a byte is 8 bits.

A **text file** is one in which the bits in the file encode individual characters. Note that the characters can include the digit characters 0-9, so one can include numbers in a text file by writing down the digits needed for the number of interest. Examples of text file formats include CSV, XML, HTML, and JSON.

Text files may be simple ASCII files (i.e., files encoded using ASCII) or in other encodings such as UTF-8, both covered in Section 4. ASCII files have 8 bits (1 byte) per character and can represent 128 characters (the 52 lower and upper case letters in English, 10 digits, punctuation and a few other things – basically what you see on a standard US keyboard). UTF-8 files have between 1 and 4 bytes per character.

A **binary file** is one in which the bits in the file encode the information in a custom format and not simply individual characters. Binary formats are not (easily) human readable but can be more space-efficient and faster to work with (because it can allow random access into the data rather than requiring sequential reading). The meaning of the bytes in such files depends on the specific binary format being used and a program that uses the file needs to know how the format represents information. Examples of binary files include netCDF files, R data (e.g., .Rda) files, and compiled code files.

Numbers in binary files are usually stored as 8 bytes per number. We’ll discuss this much more in Unit 6.

### **1.2 Common file types**

Here are some of the common file types. Any of these types can be categorized as text or binary.

2

1. ’Flat’ text files: data are often provided as simple text files. Often one has one record or observation per row and each column or field is a different variable or type of information about the record. Such files can either have a fixed number of characters in each field (fixed width format) or a special character (a delimiter) that separates the fields in each row. Common delimiters are tabs, commas, one or more spaces, and the pipe (|). Common file extensions are _.txt_ and _.csv_ . Metadata (information about the data) are often stored in a separate file. CSV files are quite common, but if you have files where the data contain commas, other delimiters can be good. Text can be put in quotes in CSV files, and this can allow use of commas within the data. This is difficult to deal with in bash, but _read.table()_ in R handles this situation.

   - One occasionally tricky difficulty is as follows. If you have a text file created in Windows, the line endings are coded differently than in UNIX (a newline (the ASCII character _\n_ ) and a carriage return (the ASCII character _\r_ ) in Windows vs. only a newline in UNIX). There are UNIX utilities ( _fromdos_ in Ubuntu, including the SCF Linux machines and _dos2unix_ in other Linux distributions) that can do the necessary conversion. If you see _^M_ at the end of the lines in a file, that’s the tool you need. Alternatively, if you open a UNIX file in Windows, it may treat all the lines as a single line. You can fix this with _todos_ or _unix2dos_ .

2. In some contexts, such as textual data and bioinformatics data, the data may in a text file with one piece of information per row, but without meaningful columns/fields.

3. In scientific contexts, netCDF ( _.nc_ ) (and the related HDF5) are popular format for gridded data that allows for highly-efficient storage and contains the metadata within the file. The basic structure of a netCDF file is that each variable is an array with multiple dimensions (e.g., latitude, longitude, and time), and one can also extract the values of and metadata about each dimension. The _ncdf4_ package in R nicely handles working with netCDF files.

4. Data may also be in text files in formats designed for data interchange between various languages, in particular XML or JSON. These formats are “self-describing”; namely the metadata is part of the file. The _XML2, rvest_ , and _jsonlite_ packages are useful for reading and writing from these formats.

5. You may be scraping information on the web, so dealing with text files in various formats, including HTML. The _XML2_ and _rvest_ packages are also useful for reading HTML.

6. Data may already be in a database or in the data storage of another statistical package ( _Stata_ , _SAS_ , _SPSS_ , etc.). The _foreign_ package in R has excellent capabilities for importing Stata

3

( _read.dta()_ ), SPSS ( _read.spss()_ ), and SAS ( _read.ssd()_ and, for XPORT files, _read.xport()_ ), among others.

7. For Excel, there are capabilities to read an Excel file (see the _readxl_ and _XLConnect_ package among others), but you can also just go into Excel and export as a CSV file or the like and then read that into R. In general, it’s best not to pass around data files as Excel or other spreadsheet format files because (1) Excel is proprietary, so someone may not have Excel and the format is subject to change, (2) Excel imposes limits on the number of rows, (3) one can easily manipulate text files such as CSV using UNIX tools, but this is not possible with an Excel file, (4) Excel files often have more than one sheet, graphs, macros, etc., so they’re not a data storage format per se.

8. R can easily interact with databases (SQLite, PostgreSQL, MySQL, Oracle, etc.), querying the database using SQL and returning results to R. More in the big data unit and in the large datasets tutorial mentioned above.

## **2 Reading data from text files into R**

### **2.1 Core R functions**

_read.table()_ is probably the most commonly-used function for reading in data. It reads in delimited files ( _read.csv()_ and _read.delim()_ are special cases of _read.table()_ ). The key arguments are the delimiter (the _sep_ argument) and whether the file contains a header, a line with the variable names. We can use _read.fwf()_ to read from a fixed width text file into a data frame.

The most difficult part of reading in such files can be dealing with how R determines the classes of the fields that are read in. There are a number of arguments to _read.table()_ and _read.fwf()_ that allow the user to control the classes. One difficulty in older versions of R was that character fields were read in as factors.

Let’s work through a couple examples. Before we do that, let’s look at the arguments to _read.table()_ . Note that _sep=”_ separates on any amount of white space. In the code chunk below, I’ve told _knitr_ not to print the output to the PDF; you can see the full output by running the code yourself.

dat <- **read.table** ( **file.path** ('..', 'data', 'RTADataSub.csv'), sep = ',', header = TRUE)

**sapply** (dat, class)

_## whoops, there is an 'x', presumably indicating missingness:_

4

**unique** (dat[ , 2]) _## let's treat 'x' as a missing value indicator_ dat2 <- **read.table** ( **file.path** ('..', 'data', 'RTADataSub.csv'), sep = ',', header = TRUE, na.strings = **c** ("NA", "x")) **unique** (dat2[ ,2]) _## hmmm, what happened to the blank values this time?_ **which** (dat[ ,2] == "") dat2[ **which** (dat[, 2] == "")[1], ] _# pull out a line with a missing string # using 'colClasses'_ sequ <- **read.table** ( **file.path** ('..', 'data', 'hivSequ.csv'), sep = ',', header = TRUE, colClasses = **c** ('integer','integer','character', 'character','numeric','integer')) _## let's make sure the coercion worked - sometimes R is obstinant_ **sapply** (sequ, class) _## that made use of the fact that a data frame is a list_

Note that you can avoid reading in one or more columns by specifying _NULL_ as the column class for those columns to be omitted. Also, specifying the _colClasses_ argument explicitly should make for faster file reading. Finally, setting stringsAsFactors=FALSE is standard practice and is the default in R as of version 4.0. ( _readr::read_csv()_ has always set stringsAsFactors=FALSE.

If possible, it’s a good idea to look through the input file in the shell or in an editor before reading into R to catch such issues in advance. Using _less_ on _RTADataSub.csv_ would have revealed these various issues, but note that _RTADataSub.csv_ is a 1000-line subset of a much larger file of data available from the kaggle.com website. So more sophisticated use of UNIX utilities as we saw in Unit 2 is often useful before trying to read something into R.

The basic function _scan()_ simply reads everything in, ignoring lines, which works well and very quickly if you are reading in a numeric vector or matrix. _scan()_ is also useful if your file is free format - i.e., if it’s not one line per observation, but just all the data one value after another; in this case you can use _scan()_ to read it in and then format the resulting character or numeric vector as a matrix with as many columns as fields in the dataset. Remember that the default is to fill the matrix by column.

If the file is not nicely arranged by field (e.g., if it has ragged lines), we’ll need to do some more work. _readLines()_ will read in each line into a separate character vector, after which we

5

can process the lines using text manipulation. Here’s an example from some US meteorological data where I know from metadata (not provided here) that the 4-11th values are an identifier, the 17-20th are the year, the 22-23rd the month, etc.

dat <- **readLines** ( **file.path** ('..', 'data', 'precip.txt')) id <- **as.factor** ( **substring** (dat, 4, 11) ) year <- **substring** (dat, 18, 21) year[1:5] ## [1] "2010" "2010" "2010" "2010" "2010" **class** (year) ## [1] "character" year <- **as.integer** ( **substring** (dat, 18, 21)) month <- **as.integer** ( **substring** (dat, 22, 23)) nvalues <- **as.integer** ( **substring** (dat, 28, 30))

Actually, that file, _precip.txt_ , is in a fixed-width format (i.e., every element in a given column has the exact same number of characters),so reading in using _read.fwf()_ would be a good strategy.

R allows you to read in not just from a file but from a more general construct called a _connection_ . Here are some examples of connections:

dat <- **readLines** ( **pipe** ("ls -al")) dat <- **read.table** ( **pipe** ("unzip dat.zip")) dat <- **read.csv** ( **gzfile** ("dat.csv.gz")) dat <- **readLines** ("http://www.stat.berkeley.edu/~paciorek/index.html")

In some cases, you might need to create the connection using _url()_ or using the _curl()_ function from the _curl_ package. Though for the example here, simply passing the URL to _readLines()_ does work. (In general, _curl::curl()_ provides some nice features for reading off the internet.)

wikip1 <- **readLines** ("https://wikipedia.org") wikip2 <- **readLines** ( **url** ("https://wikipedia.org")) **library** (curl) _## Using libcurl 7.68.0 with GnuTLS/3.6.13_ wikip3 <- **readLines** ( **curl** ("https://wikipedia.org"))

6

If a file is large, we may want to read it in in chunks (of lines), do some computations to reduce the size of things, and iterate. _read.table()_ , _read.fwf()_ and _readLines()_ all have the arguments that let you read in a fixed number of lines. To read-on-the-fly in blocks, we need to first establish the connection and then read from it sequentially. (If you don’t, you’ll read from the start of the file every time you read from the file.)

con <- **file** ( **file.path** ("..", "data", "precip.txt"), "r") _## "r" for 'read' - you can also open files for writing with "w" ## (or "a" for appending)_ **class** (con) blockSize <- 1000 _# obviously this would be large in any real application_ nLines <- 300000 **for** (i **in** 1: **ceiling** (nLines / blockSize)){ lines <- **readLines** (con, n = blockSize) _# manipulate the lines and store the key stuff_ } **close** (con)

Here’s an example of using _curl()_ to do this for a file on the web.

URL <- "https://www.stat.berkeley.edu/share/paciorek/2008.csv.gz" con <- **gzcon** ( **curl** (URL, open = "r")) _## url() in place of curl() works too_ **for** (i **in** 1:8) { **print** (i) **print** ( **system.time** (tmp <- **readLines** (con, n = 100000))) **print** (tmp[1]) } ## [1] 1 ## user system elapsed ## 0.583 0.000 0.583 ## [1] ## [1] 2 ## user system elapsed ## 0.562 0.002 0.564 ## [1] "2008,1,29,2,1938,1935,2308,2257,XE,7676,N11176,150,142,104,11,3,SLC,OKC,866,5,41,0,,0,NA,NA,NA,NA,NA"

7

## [1] 3 ## user system elapsed ## 0.572 0.000 0.573 ## [1] "2008,1,20,7,1540,1525,1651,1637,OO,5703,N227SW,71,72,58,14,15,SBA,SJC,234,5,8,0,,0,NA,NA,NA,NA,NA" ## [1] 4 ## user system elapsed ## 0.554 0.000 0.554 ## [1] "2008,1,2,3,1313,1250,1443,1425,WN,440,N461WN,150,155,138,18,23,MCO,STL,880,3,9,0,,0,2,0,0,0,16" ## [1] 5 ## user system elapsed ## 0.547 0.000 0.548 ## [1] "2008,1,24,4,1026,1015,1116,1110,MQ,3926,N653AE,50,55,38,6,11,MLI,ORD,139,6,6,0,,0,NA,NA,NA,NA,NA" ## [1] 6 ## user system elapsed ## 0.561 0.000 0.561 ## [1] "2008,1,4,5,1129,1125,1352,1350,AA,1145,N438AA,203,205,187,2,4,ORD,SLC,1249,3,13,0,,0,NA,NA,NA,NA,NA" ## [1] 7 ## user system elapsed ## 0.547 0.000 0.547 ## [1] "2008,1,10,4,716,720,1025,1024,DL,1590,N991DL,129,124,107,1,-4,AUS,ATL,813,6,16,0,,0,NA,NA,NA,NA,NA" ## [1] 8 ## user system elapsed ## 0.558 0.000 0.558 ## [1] "2008,2,15,5,2127,2132,2254,2312,XE,7663,N33182,87,100,71,-18,-5,SLC,ABQ,493,6,10,0,,0,NA,NA,NA,NA,NA" **close** (con)

More details on sequential (on-line) processing of large files can be found in the tutorial on large datasets mentioned in the reference list above.

One cool trick that can come in handy is to create a _text connection_ . This lets you ’read’ from an R character vector as if it were a text file and could be handy for processing text. For example, you could then use _read.fwf()_ applied to _con_ .

dat <- **readLines** ('../data/precip.txt') con <- **textConnection** (dat[1], "r") **read.fwf** (con, **c** (3,8,4,2,4,2))

8

## V1 V2 V3 V4 V5 V6 ## 1 DLY 1000807 PRCP HI 2010 2

We can create connections for writing output too. Just make sure to open the connection first.

### **2.2 File paths**

A few notes on file paths, related to ideas of reproducibility.

1. In general, you don’t want to hard-code absolute paths into your code files because those absolute paths won’t be available on the machines of anyone you share the code with. Instead, use paths relative to the directory the code file is in, or relative to a baseline directory for the project, e.g.:

<mark>dat <-</mark> **<mark>read.csv</mark>** <mark>('../data/cpds.csv')</mark>

2. Be careful with the directory separator in Windows files: you can either do _“C:\\mydir\\file.txt”_ or _“C:/mydir/file.txt”_ , but not _“C:\mydir\file.txt”_ , and note the next comment about avoiding use of ’\\‘ for portability.

3. Using UNIX style directory separators will work in Windows, Mac or Linux, but using Windows style separators is not portable across operating systems.

_## good: will work on Windows_ dat <- **read.csv** ('../data/cpds.csv') _## bad: won't work on Mac or Linux_ dat <- **read.csv** ('..\\data\\cpds.csv')

4. Even better, use _file.path()_ so that paths are constructed specifically for the operating system the user is using:

_## good: operating-system independent_ dat <- **read.csv** ( **file.path** ('..', 'data', 'cpds.csv'))

9

### **2.3 The** **_readr_ package**

_readr_ is intended to deal with some of the shortcomings of the base R functions, such as defaulting to stringsAsFactors=FALSE (no longer relevant with R 4.0), leaving column names unmodified, and recognizing dates/times. It reads data in much more quickly than the base R equivalents. See this blog post. Some of the readr functions that are analogs to the comparably-named base R functions are _read_csv()_ , _read_fwf()_ , _read_lines()_ , and _read_table()_ .

Let’s try out _read_csv()_ on the airline dataset used in the R bootcamp.

**library** (readr) _## ## Attaching package: ’readr’ ## The following object is masked from ’package:curl’: ## ## parse_date ## I'm violating the rule about absolute paths here!! ## (airline.csv is big enough that I don't want to put it in the ## course repository)_ **setwd** ('~/staff/workshops/r-bootcamp-fall-2020/data') **system.time** (dat <- **read.csv** ('airline.csv', stringsAsFactors = FALSE)) ## user system elapsed ## 4.072 0.186 4.266 **system.time** (dat2 <- **read_csv** ('airline.csv')) _## Rows: 539895 Columns: 29 ## - Column specification --------------------## Delimiter: "," ## chr (5): UniqueCarrier, TailNum, Origin, Dest, Canc... ## dbl (24): Year, Month, DayOfMonth, DayOfWeek, DepTim... ## ## i Use ‘spec()‘ to retrieve the full column specification for this data. ## i Specify the column types or set ‘show_col_types = FALSE‘ to quiet this message._ ## user system elapsed ## 1.714 0.045 1.016

10

### **2.4 Reading data quickly**

In addition to the tips above, there are a number of packages that allow one to read large data files quickly, in particular _data.table_ , _ff_ , and _bigmemory_ . In general, these provide the ability to load datasets into R without having them in memory, but rather stored in clever ways on disk that allow for fast access. Metadata is stored in R. More on this in the unit on big data and in the tutorial on large datasets mentioned in the reference list above.

## **3 Output from R**

### **3.1 Writing output to files**

Functions for text output are generally analogous to those for input. _write.table()_ , _write.csv()_ , and _writeLines()_ are analogs of _read.table()_ , _read.csv()_ , and _readLines()_ . _write_csv()_ is the _readr_ version of write.csv. _write()_ can be used to write a matrix to a file, specifying the number of columns desired. _cat()_ can be used when you want fine control of the format of what is written out and allows for outputting to a connection (e.g., a file).

_toJSON()_ in the _jsonlite_ package will output R objects as JSON. One use of JSON as output from R would be to _serialize_ the information in an R object such that it could be read into another program.

And of course you can always save to an R data file using _save.image()_ (to save all the objects in the workspace or _save()_ to save only some objects. Happily this is platform-independent so can be used to transfer R objects between different OS.

### **3.2 Formatting output**

_cat()_ is a good choice for printing a message to the screen, often better than _print()_ , which is an object-oriented method. You generally won’t have control over how the output of a _print()_ statement is actually printed.

val <- 1.5 **cat** ('My value is ', val, '.\n', sep = '') ## My value is 1.5.

**print** ( **paste** ('My value is ', val, '.', sep = '')) ## [1] "My value is 1.5."

11

We can do more to control formatting with _cat()_ :

_## input_ x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n") ## Powers of 7 **cat** ("exponent result\n\n") ## exponent result result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** ( **format** (i, width = 8), **format** (result, width = 10), "\n", sep = "") } ## 1 7 ## 2 49 ## 3 343 ## 4 2401 ## 5 16807 x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n") ## Powers of 7 **cat** ("exponent result\n\n") ## exponent result

12

result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** (i, '\t', result, '\n', sep = '') } ## 1 7 ## 2 49 ## 3 343 ## 4 2401 ## 5 16807

One thing to be aware of when writing out numerical data is how many digits are included. For example, the default with _write()_ and _cat()_ is the number of digits that R displays to the screen, controlled by _options()$digits_ . But note that _options()$digits_ seems to have some variability in behavior across operating systems. If you want finer control, use _sprintf()_ , e.g., to print out print out temperatures as reals (“ _f_ ”=floating points) with four decimal places and nine total character positions, followed by a C for Celsius:

temps <- **c** (12.5, 37.234324, 1342434324.79997234, 2.3456e-6, 1e10) **sprintf** ("%9.4f C", temps)

## [1] " 12.5000 C" " 37.2343 C" ## [3] "1342434324.8000 C" " 0.0000 C" ## [5] "10000000000.0000 C"

city <- "Boston" **sprintf** ("The temperature in %s was %.4f C.", city, temps[1]) ## [1] "The temperature in Boston was 12.5000 C." **sprintf** ("The temperature in %s was %9.4f C.", city, temps[1]) ## [1] "The temperature in Boston was 12.5000 C."

Note, to change the number of digits printed to the screen, do options(digits = 5) or specify as an argument to _print()_ or use _sprintf()_ .

13

## **4 Webscraping and working with HTML, XML, and JSON**

The book _XML and Web Technologies for Data Sciences with R_ by Deb Nolan (UCB Stats faculty) and Duncan Temple Lang (UCB Stats PhD alumnus and UC Davis Stats faculty) provides extensive information about getting and processing data off of the web, including interacting with web services such as REST and SOAP and programmatically handling authentication.

Here are some UNIX command-line tools to help in webscraping and working with files in formats such as JSON, XML, and HTML: http://jeroenjanssens.com/2013/09/19/seven-commandline-tools-for-data-science.html.

We’ll cover a few basic examples in this section, but HTML and XML formatting and navigating the structure of such pages in great detail is beyond the scope of what we can cover. The key thing is to see the main concepts and know that the tools exist so that you can learn how to use them if faced with such formats.

### **4.1 Reading HTML**

HTML (Hypertext Markup Language) is the standard markup language used for displaying content in a web browser. In simple webpages (ignoring the more complicated pages that involve Javascript), what you see in your browser is simply a rendering of a text file containing HTML.

However, instead of rendering the HTML in a browser, we might want to use code to extract information from the HTML.

Let’s see a brief example of reading in HTML tables.

Note that before doing any coding, it can be helpful to look at the raw HTML source code for a given page. We can explore the underlying HTML source in advance of writing our code by looking at the page source directly in the browser (e.g., in Firefox under the 3-lines “open menu” symbol, see Web Developer (or More Tools) -> Page Source and in Chrome View -> Developer -> View Source), or by downloading the webpage and looking at it in an editor, although in some cases (such as the nytimes.com case), what we might see is a lot of JavaScript.

One lesson here is not to write a lot of your own code to do something that someone else has probably already written a package for. We’ll use the _rvest_ package.

**library** (rvest) _# uses xml2 ## ## Attaching package: ’rvest’_

14

_## The following object is masked from ’package:readr’: ## ## guess_encoding_ URL <- "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population" html <- **read_html** (URL) tbls <- **html_table** ( **html_elements** (html, "table")) **sapply** (tbls, nrow) ## [1] 242 12 pop <- tbls[[1]] **head** (pop) ## # A tibble: 6 x 8 ## Rank ` Country or depe~ Region Population ` % of world ` ## <chr> <chr> <chr> <chr> <chr> ## 1 â World World 7,892,069~ 100% ## 2 1 China (more) Asia 1,411,778~ 17.9% ## 3 2 India (more) Asia 1,381,270~ 17.5% ## 4 3 United States (m~ Ameri~ 332,277,3~ 4.21% ## 5 4 Indonesia (more) Asia 271,350,0~ 3.44% ## 6 5 Pakistan (more) Asia 225,200,0~ 2.85% ## # ... with 3 more variables: Date <chr>, ...

_read_html()_ works by reading in the HTML as text and then parsing it to build up a tree containing the HTML elements. Then _html_nodes()_ finds the HTML tables and _html_table()_ converts them to data frames. rvest is part of the tidyverse, so it’s often used with piping, e.g.,

**library** (magrittr) _## Turns out that html_table can take the entire html doc as input_ tbls <- URL %>% **read_html** () %>% **html_table** ()

It’s often useful to be able to extract the hyperlinks in an HTML document. We’ll find the link using CSS selectors, which allow you to search for elements within HTML:

15

URL <- "http://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year" _## approach 1: search for elements with 'href' attribute_ links <- **read_html** (URL) %>% **html_elements** ("[href]") %>% **html_attr** ('href') _## approach 2: search for HTML 'a' tags_ links <- **read_html** (URL) %>% **html_elements** ("a") %>% **html_attr** ('href') **head** (links, n = 10)

## [1] "?C=N;O=D" "?C=M;O=A" ## [3] "?C=S;O=A" "?C=D;O=A" ## [5] "/pub/data/ghcn/daily/" "1763.csv.gz" ## [7] "1764.csv.gz" "1765.csv.gz" ## [9] "1766.csv.gz" "1767.csv.gz"

More generally, we may want to read an HTML document, parse it into its components (i.e., the HTML elements), and navigate through the tree structure of the HTML. Here we use the _XPath_ language to specify elements rather than CSS selectors. XPath can also be used for navigating through XML documents.

_## find all 'a' elements that have attribute 'href'; then ## extract the 'href' attribute_ links <- **read_html** (URL) %>% **html_elements** (xpath = "//a[@href]") %>% **html_attr** ('href') **head** (links) ## [1] "?C=N;O=D" "?C=M;O=A" ## [3] "?C=S;O=A" "?C=D;O=A" ## [5] "/pub/data/ghcn/daily/" "1763.csv.gz" _## we can extract various information_ listOfANodes <- **read_html** (URL) %>% **html_elements** (xpath = "//a[@href]") listOfANodes %>% **html_attr** ('href') %>% **head** (n = 10)

## [1] "?C=N;O=D" "?C=M;O=A" ## [3] "?C=S;O=A" "?C=D;O=A" ## [5] "/pub/data/ghcn/daily/" "1763.csv.gz" ## [7] "1764.csv.gz" "1765.csv.gz" ## [9] "1766.csv.gz" "1767.csv.gz"

16

listOfANodes %>% **html_name** () %>% **head** (n = 10)

## [1] "a" "a" "a" "a" "a" "a" "a" "a" "a" "a"

listOfANodes %>% **html_text** () %>% **head** (n = 10) ## [1] "Name" "Last modified" ## [3] "Size" "Description" ## [5] "Parent Directory" "1763.csv.gz" ## [7] "1764.csv.gz" "1765.csv.gz" ## [9] "1766.csv.gz" "1767.csv.gz"

Here’s another example of extracting specific components of information from a webpage (results not shown, since headlines will vary from day to day).

URL <- "https://www.nytimes.com"

headlines2 <- **read_html** (URL) %>% **html_elements** ("h2") %>% **html_text** () **head** (headlines2) headlines3 <- **read_html** (URL) %>% **html_elements** ("h3") %>% **html_text** () **head** (headlines3)

### **4.2 XML**

XML is a markup language used to store data in self-describing (no metadata needed) format, often with a hierarchical structure. It consists of sets of elements (also known as nodes because they generally occur in a hierarchical structure and therefore have parents, children, etc.) with tags that identify/name the elements, with some similarity to HTML. Some examples of the use of XML include serving as the underlying format for Microsoft Office and Google Docs documents and for the KML language used for spatial information in Google Earth.

Here’s a brief example. The book with id attribute _bk101_ is an element; the author of the book is also an element that is a child element of the book. The id attribute allows us to uniquely identify the element.

<?xml version="1.0"?>

<catalog>

<book id="bk101">

<author>Gambardella, Matthew</author>

17

<title>XML Developer's Guide</title> <genre>Computer</genre> <price>44.95</price> <publish_date>2000-10-01</publish_date> <description>An in-depth look at creating applications with XML.</description> </book> <book id="bk102"> <author>Ralls, Kim</author> <title>Midnight Rain</title> <genre>Fantasy</genre> <price>5.95</price> <publish_date>2000-12-16</publish_date> <description>A former architect battles corporate zombies, an evil </book> </catalog>

We can read XML documents into R using xml2::read_xml() and then manipulate it using other functions from the _xml2_ package. Here’s an example of working with lending data from the Kiva lending non-profit. You can see the XML format in a browser at http://api.kivaws.org/v1/loans/newest.xml.

XML documents have a tree structure with information at nodes. As above with HTML, one can use the _XPath_ language for navigating the tree and finding and extracting information from the node(s) of interest. Here is some example code for extracting loan info from the Kiva data.

**library** (xml2) doc <- **read_xml** ("https://api.kivaws.org/v1/loans/newest.xml") data <- **as_list** (doc) **names** (data) ## [1] "response" **names** (data$response) ## [1] "paging" "loans" **length** (data$response$loans) ## [1] 20

18

data$response$loans[[2]][ **c** ('name', 'activity', 'sector', 'location', 'loan_amount')] ## $name ## $name[[1]] ## [1] "Ablaba Eva" ## ## ## $activity ## $activity[[1]] ## [1] "Sewing" ## ## ## $sector ## $sector[[1]] ## [1] "Services" ## ## ## $location ## $location$country_code ## $location$country_code[[1]] ## [1] "TG" ## ## ## $location$country ## $location$country[[1]] ## [1] "Togo" ## ## ## $location$town ## $location$town[[1]] ## [1] "baguida" ## ## ## $location$geo ## $location$geo$level

19

## $location$geo$level[[1]] ## [1] "town" ## ## ## $location$geo$pairs ## $location$geo$pairs[[1]] ## [1] "6.160584 1.31352" ## ## ## $location$geo$type ## $location$geo$type[[1]] ## [1] "point" ## ## ## ## ## $loan_amount ## $loan_amount[[1]] ## [1] "150" _## alternatively, extract only the 'loans' info (and use pipes)_ loansNode <- doc %>% **html_elements** ('loans') loanInfo <- loansNode %>% **xml_children** () %>% **as_list** () **length** (loanInfo)

## [1] 20

**names** (loanInfo[[1]])

## [1] "id" ## [2] "name" ## [3] "description" ## [4] "status" ## [5] "funded_amount" ## [6] "basket_amount" ## [7] "image" ## [8] "activity"

20

|##|[9]|"sector"|
|---|---|---|
|##|[10]|"use"|
|##|[11]|"location"|
|##|[12]|"partner_id"|
|##|[13]|"posted_date"|
|##|[14]|"planned_expiration_date"|
|##|[15]|"loan_amount"|
|##|[16]|"borrower_count"|
|##|[17]|"lender_count"|
|##|[18]|"bonus_credit_eligibility"|
|##|[19]|"tags"|
|**nam**|**es**(l|oanInfo[[1]]$location)|
|##|[1]|"country_code" "country"<br>"town"|
|##|[4]|"geo"|
|_## _|_supp_|_ose we only want the country locations of the loans (using XPath)_|
|**xml**|**_fin**|**d_all**(loansNode, '//location//country')|
|##|{xml|_nodeset (20)}|
|##|[1]|<country>Togo</country>|
|##|[2]|<country>Togo</country>|
|##|[3]|<country>El Salvador</country>|
|##|[4]|<country>Guatemala</country>|
|##|[5]|<country>Haiti</country>|
|##|[6]|<country>El Salvador</country>|
|##|[7]|<country>El Salvador</country>|
|##|[8]|<country>Georgia</country>|
|##|[9]|<country>El Salvador</country>|
|##|[10]|<country>El Salvador</country>|
|##|[11]|<country>El Salvador</country>|
|##|[12]|<country>El Salvador</country>|
|##|[13]|<country>Kenya</country>|
|##|[14]|<country>Indonesia</country>|
|##|[15]|<country>Kenya</country>|
|##|[16]|<country>Kenya</country>|


21

## [17] <country>El Salvador</country> ## [18] <country>El Salvador</country> ## [19] <country>El Salvador</country> ## [20] <country>Honduras</country>

**xml_find_all** (loansNode, '//location//country') %>% **xml_text** ()

- ## [1] "Togo" "Togo" "El Salvador" ## [4] "Guatemala" "Haiti" "El Salvador" ## [7] "El Salvador" "Georgia" "El Salvador" ## [10] "El Salvador" "El Salvador" "El Salvador" ## [13] "Kenya" "Indonesia" "Kenya" ## [16] "Kenya" "El Salvador" "El Salvador" ## [19] "El Salvador" "Honduras"

_## or extract the geographic coordinates_

**xml_find_all** (loansNode, '//location//geo/pairs')

|##|{xml_nodeset (20)}|
|---|---|
|##|[1] <pairs>6.160584 1.31352</pairs>|
|##|[2] <pairs>6.160584 1.31352</pairs>|
|##|[3] <pairs>13.833333 -88.916667</pairs>|
|##|[4] <pairs>14.944972 -91.108924</pairs>|
|##|[5] <pairs>37.55 22.083333</pairs>|
|##|[6] <pairs>13.833333 -88.916667</pairs>|
|##|[7] <pairs>13.341347 -88.275314</pairs>|
|##|[8] <pairs>42.605475 42.000951</pairs>|
|##|[9] <pairs>13.833333 -88.916667</pairs>|
|##|[10] <pairs>13.833333 -88.916667</pairs>|
|##|[11] <pairs>13.833333 -88.916667</pairs>|
|##|[12] <pairs>13.833333 -88.916667</pairs>|
|##|[13] <pairs>-0.583333 35.183333</pairs>|
|##|[14] <pairs>-6.178056 106.63</pairs>|
|##|[15] <pairs>-1.307941 36.714256</pairs>|
|##|[16] <pairs>-1.307941 36.714256</pairs>|
|##|[17] <pairs>13.341347 -88.275314</pairs>|
|##|[18] <pairs>13.833333 -88.916667</pairs>|


22

## [19] <pairs>13.833333 -88.916667</pairs> ## [20] <pairs>14.033333 -86.583333</pairs>

### **4.3 JSON**

JSON files are structured as “attribute-value” pairs (aka “key-value” pairs), often with a hierarchical structure. Here’s a brief example:

{ "firstName": "John", "lastName": "Smith", "isAlive": true, "age": 25, "address": { "streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021-3100" }, "phoneNumbers": [ { "type": "home", "number": "212 555-1234" }, { "type": "office", "number": "646 555-4567" } ], "children": [], "spouse": null }

A set of key-value pairs is a named array and is placed inside braces (squiggly brackets). Note the nestedness of arrays within arrays (e.g., address within the overarching person array and the use of square brackets for unnamed arrays (i.e., vectors of information), as well as the use of different

23

types: character strings, numbers, null, and (not shown) boolean/logical values. JSON and XML can be used in similar ways, but JSON is less verbose than XML.

We can read JSON into R using _fromJSON()_ in the _jsonlite_ package. Let’s play again with the Kiva data. The same data that we had worked with in XML format is also available in JSON format: http://api.kivaws.org/v1/loans/newest.json.

**library** (jsonlite) data <- **fromJSON** ("http://api.kivaws.org/v1/loans/newest.json") **class** (data) ## [1] "list" **names** (data) ## [1] "paging" "loans" **class** (data$loans) _# nice!_ ## [1] "data.frame" **head** (data$loans)

## id name languages status ## 1 2233588 Sogninde fr, en fundraising ## 2 2233590 Ablaba Eva fr, en fundraising ## 3 2233155 Maria Consuelo es, en fundraising ## 4 2233167 Sacpulupense Group es, en fundraising ## 5 2233592 Elisemene fr, en fundraising ## 6 2233154 Ada Yessenia es, en fundraising ## funded_amount basket_amount image.id ## 1 0 0 3242990 ## 2 0 0 4400807 ## 3 0 0 4400045 ## 4 0 0 4400078 ## 5 0 0 3766325 ## 6 0 0 4400042 ## image.template_id activity sector ## 1 1 Used Clothing Clothing ## 2 1 Sewing Services

24

|##|3|1|General Store<br>Retail|
|---|---|---|---|
|##|4|1|Textiles<br>Arts|
|##|5|1|Beverages<br>Food|
|##|6|1|Fish Selling<br>Food|
|##|||use|
|##|1|to b|uy 2 bundles of second-hand clothing.|
|##|2|to|buy 10 pagnes [traditional clothes].|
|##|3|to buy drinks and|other staple food products wholesale.|
|##|4||to purchase a variety of thread.|
|##|5||to increase her stock of soft drinks.|
|##|6|to buy fresh|fish to distribute to her customers.|
|##||location.country_c|ode location.country|
|##|1||TG<br>Togo|
|##|2||TG<br>Togo|
|##|3||SV<br>El Salvador|
|##|4||GT<br>Guatemala|
|##|5||HT<br>Haiti|
|##|6||SV<br>El Salvador|
|##|||location.town|
|##|1||baguida|
|##|2||baguida|
|##|3||<NA>|
|##|4|Chichicastenango,|Departamento El Quiche|
|##|5||Croix-des-Bouquets|
|##|6||<NA>|
|##||location.geo.level|location.geo.pairs|
|##|1|town|6.160584 1.31352|
|##|2|town|6.160584 1.31352|
|##|3|country|13.833333 -88.916667|
|##|4|town|14.944972 -91.108924|
|##|5|town|37.55 22.083333|
|##|6|country|13.833333 -88.916667|
|##||location.geo.type|partner_id<br>posted_date|
|##|1|point|296 2021-08-30T15:50:58Z|
|##|2|point|296 2021-08-30T15:50:58Z|
|##|3|point|167 2021-08-30T15:50:55Z|


25

|##|4||point<br>55|2021-08-30T15:50:04Z|
|---|---|---|---|---|
|##|5||point<br>442|2021-08-30T15:30:15Z|
|##|6||point<br>167|2021-08-30T15:30:10Z|
|##||pl|anned_expiration_date loan|_amount borrower_count|
|##|1||2021-09-29T15:50:58Z|200<br>1|
|##|2||2021-09-29T15:50:58Z|150<br>1|
|##|3||2021-09-29T15:50:55Z|500<br>1|
|##|4||2021-09-29T15:50:03Z|3000<br>8|
|##|5||2021-09-29T15:30:15Z|775<br>1|
|##|6||2021-09-29T15:30:10Z|1000<br>1|
|##||le|nder_count bonus_credit_el|igibility tags|
|##|1||0|FALSE NULL|
|##|2||0|FALSE NULL|
|##|3||0|TRUE NULL|
|##|4||0|TRUE NULL|
|##|5||0|FALSE NULL|
|##|6||0|TRUE NULL|
|##|||themes||
|##|1||NULL||
|##|2||NULL||
|##|3|Vu|lnerable Groups||
|##|4||NULL||
|##|5||NULL||
|##|6||NULL||
|da|ta|$lo|ans[1, 'location.geo.pairs|'] _# hmmm..._|
|##|N|ULL|||
|da|ta|$lo|ans[1, 'location']||
|##||co|untry_code country<br>town|geo.level|
|##|1||TG<br>Togo baguida|town|
|##|||geo.pairs geo.type||
|##|1|6.|160584 1.31352<br>point||


One disadvantage of JSON is that it is not set up to deal with missing values, infinity, etc.

26

### **4.4 Webscraping and web APIs**

Here we’ll see some examples of making requests over the Web to get data. We’ll use APIs to systematically query a website for information. Ideally, but not always, the API will be documented. In many cases that simply amounts to making an HTTP GET request, which is done by constructing a URL.

The packages _RCurl_ and _httr_ are useful for a wide variety of such functionality. Note that much of the functionality I describe below is also possible within bash using either _wget_ or _curl_ .

#### **4.4.1 Webscraping ethics and best practices**

Webscraping is the process of extracting data from the web, either directly from a website or using a web API (application programming interface).

1. **Should you webscrape?** In general, if we can avoid webscraping (particularly if there is not an API) and instead directly download a data file from a website, that is greatly preferred.

2. **May you webscrape?** Before you set up any automated downloading of materials/data from the web you should make sure that what you are about to do is consistent with the rules provided by the website.

Some places to look for information on what the website allows are:

- legal pages such as Terms of Service or Terms and Conditions on the website.

- check the robots.txt file (e.g., https://scholar.google.com/robots.txt) to see what a web crawler is allowed to do, and whether the site requires a particular delay between requests to the sites

- potentially contact the site owner if you plan to scrape a large amount of data

Here are some links with useful information:

- A blog post overview on webscraping and robots.txt

- Blog post on webscraping ethics

- Some information on how to understand a robots.txt file

In many cases you will want to include a time delay between your automated requests to a site, including if you are not actually crawling a site but just want to automate a small number of queries.

27

#### **4.4.2 What is HTTP?**

HTTP (hypertext transfer protocol) is a system for communicating information from a server (i.e., the website of interest) to a client (e.g., your laptop). The client sends a request and the server sends a response.

When you go to a website in a browser, your browser makes an HTTP GET request to the website. Similarly, when we did some downloading of html from webpages above, we used an HTTP GET request.

Anytime the URL you enter includes ’param’ information (www.somewebsite.com?param=arg), you are using an API.

The response to an HTTP request will include a status code, which can be interpreted based on this information.

The response will generally contain content in the form of text (e.g., HTML, XML, JSON) or raw bytes.

#### **4.4.3 APIs: REST- and SOAP-based web services**

Ideally a web service documents their API (Applications Programming Interface) that serves data or allows other interactions. REST and SOAP are popular API standards/styles. Both REST and SOAP use HTTP requests; we’ll focus on REST as it is more common and simpler. The API will (hopefully) document what information it expects from the user and will return the result in a standard format (e.g., a particular file format rather than producing a webpage).

When using REST, we access _resources_ , which might be a Facebook account or a database of stock quotes. The resource may return information in the form of an HTML file or JSON, CSV or something else.

Often the format of the request is a URL (aka an endpoint) plus a query string, passed as a GET request. Let’s search for plumbers near Berkeley, and we’ll see the GET request, in the form: https://www.yelp.com/search?find_desc=plumbers&find_loc=Berkeley+CA&ns=1

- the query string begins with ?

- there are one or more Parameter=Argument pairs

- pairs are separated by &

- + is used in place of each space

We don’t always get HTML back - try searching for “Purple Rain” at _apple.com_ . What format do you get back?

28

Let’s see an example of accessing climate model output data from the World Bank. The API is documented by following some links from here: http://datahelpdesk.worldbank.org/knowledgebase. Following that documentation we can download monthly average precipitation predictions for 2080-2099 for the US (ISO3 code ‘USA’) based on global climate model simulations. In this case our REST-based query is simply constructing a straightforward URL.

times <- **c** (2080, 2099) countryCode <- 'USA' baseURL <- "http://climatedataapi.worldbank.org/climateweb/rest/v1/country" _##" http://climatedataapi.worldbank.org/climateweb/rest/v1/country"_ type <- "mavg" var <- "pr"

data <- **read.csv** ( **paste** (baseURL, type, var, times[1], times[2], **paste0** (countryCode, '.csv'), sep = '/'))

**head** (data)

|##||GCM var|scenario|from_year|to_year|Jan|
|---|---|---|---|---|---|---|
|##|1<br>bccr_bc|m2_0<br>pr|a2|2080|2099|67.03573|
|##|2<br>bccr_bc|m2_0<br>pr|b1|2080|2099|62.36411|
|##|3 cccma_cgc|m3_1<br>pr|a2|2080|2099|73.05678|
|##|4 cccma_cgc|m3_1<br>pr|b1|2080|2099|68.13736|
|##|5<br>cnrm|_cm3<br>pr|a2|2080|2099|72.18374|
|##|6<br>cnrm|_cm3<br>pr|b1|2080|2099|69.87911|
|##|Feb|Mar|Apr|May|Jun|Jul|
|##|1 60.34472|68.55613|69.73249|70.75057|68.87670|75.50839|
|##|2 57.25621|65.37839|66.83145|71.42986|66.70454|76.21705|
|##|3 65.88258|69.07827|70.52308|71.27610|71.40891|71.73378|
|##|4 56.80470|64.87122|64.26042|65.26155|65.63476|68.85459|
|##|5 64.47102|76.22999|79.40222|94.16236|93.20071|92.61398|
|##|6 59.47017|70.12903|80.61524|92.51666|92.54483|96.00988|
|##|Aug|Sep|Oct|Nov|Dec||
|##|1 79.16541|76.60718|79.72601|72.12957|71.83717||
|##|2 76.50563|81.48503|73.44661|67.69188|62.61851||
|##|3 71.16824|72.37070|72.17842|85.11507|77.58228||
|##|4 68.02093|66.02112|70.71792|77.58472|77.31110||
|##|5 87.12436|87.24258|86.20070|77.22606|78.49393||
|##|6 91.05730|88.87449|82.81388|70.25031|71.83962||


29

_<mark>### 4.4.4 HTTP requests by deconstructing an (undocumented) API</mark>_

As another example, here we can see the Kiva API, which allows us to construct queries on the Kiva data that we saw some of earlier.

The Nolan and Temple Lang book provides a number of examples of different ways of authenticating with web services that control access to the service.

Finally, some web services allow us to pass information to the service in addition to just getting data or information. E.g., you can programmatically interact with your Facebook, Dropbox, and Google Drive accounts using REST based on HTTP POST, PUT, and DELETE requests. Authentication is of course important in these contexts and some times you would first authenticate with your login and password and receive a “token”. This token would then be used in subsequent interactions in the same session.

I created your _github.berkeley.edu_ accounts from Python by interacting with the Github API using the _requests_ package.

#### **4.4.4 HTTP requests by deconstructing an (undocumented) API**

In some cases an API may not be documented or we might be lazy and not use the documentation. Instead we might deconstruct the queries a browser makes and then mimic that behavior, in some cases having to parse HTML output to get at data. Note that if the webpage changes even a little bit, our carefully constructed query syntax may fail.

Let’s look at some UN data (agricultural crop data). By going to

http://data.un.org/Explorer.aspx?d=FAO, and clicking on “Crops”, we’ll see a bunch of agricultural products with “View data” links. Click on “apricots” as an example and you’ll see a “Download” button that allows you to download a CSV of the data. Let’s select a range of years and then try to download “by hand”. Sometimes we can right-click on the link that will download the data and directly see the URL that is being accessed and then one can deconstruct it so that you can create URLs programmatically to download the data you want.

In this case, we can’t see the full URL that is being used because there’s some Javascript involved. Therefore, rather than looking at the URL associated with a link we need to view the actual HTTP request sent by our browser to the server. We can do this using features of the browser (e.g., in Firefox see Web Developer -> Network and in Chrome More tools -> Developer tools -> Network) (or right-click on the webpage and select Inspect and then Network). Based on this we can see that an HTTP GET request is being used with a URL such as:

http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526;year:2012,2013,2014,2015,2016,2017&DataMartId=FAO&Format=csv&c=2,4,5,6,7&s=countryName:asc,elementCode:asc,year:desc

30

We’e now able to easily download the data using that URL, which we can fairly easily construct using string processing in bash, R, or Python, such as this:

_## example URL: ## http://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526; ##year:2012,2013,2014,2015,2016,2017&DataMartId=FAO&Format=csv&c=2,4,5,6,7& ##s=countryName:asc,elementCode:asc,year:desc_ itemCode <- 526 baseURL <- "http://data.un.org/Handlers/DownloadHandler.ashx" yrs <- **paste** ( **as.character** (2012:2017), collapse = ",") filter <- **paste0** ("?DataFilter=itemCode:", itemCode, ";year:", yrs) args1 <- "&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&" args2 <- "s=countryName:asc,elementCode:asc,year:desc" url <- **paste0** (baseURL, filter, args1, args2) _## if the website provided a CSV we could just do this: ## apricots <- read.csv(url) ## but it zips the file_ temp <- **tempfile** () _## give name for a temporary file_ **download.file** (url, temp) dat <- **read.csv** ( **unzip** (temp)) _## using a connection (see Section 2)_

**head** (dat)

|##|Country.or.Area|Element.Code|Element|Year|Unit|
|---|---|---|---|---|---|
|##|1<br>Afghanistan|5312|Area harvested|2017|ha|
|##|2<br>Afghanistan|5312|Area harvested|2016|ha|
|##|3<br>Afghanistan|5312|Area harvested|2015|ha|
|##|4<br>Afghanistan|5312|Area harvested|2014|ha|
|##|5<br>Afghanistan|5312|Area harvested|2013|ha|
|##|6<br>Afghanistan|5312|Area harvested|2012|ha|
|##|Value Value.Foo|tnotes||||
|##|1 13413|Im||||
|##|2<br>8595|||||
|##|3<br>9116|||||
|##|4<br>9005|||||
|##|5<br>9005|||||
|##|6<br>8350|||||


31

**library** (httr) _## ## Attaching package: ’httr’ ## The following object is masked from ’package:curl’: ## ## handle_reset_ output2 <- **GET** (baseURL, query = **list** ( DataFilter = **paste0** ("itemCode:", itemCode, ";year:", yrs), DataMartID = "FAO", Format = "csv", c = "2,3,4,5,6,7", s = "countryName:asc,elementCode:asc,year:desc")) temp <- **tempfile** () _## give name for a temporary file_ **writeBin** ( **content** (output2, 'raw'), temp) _## write out as zip file_ dat <- **read.csv** ( **unzip** (temp)) **head** (dat) ## Country.or.Area Element.Code Element Year Unit ## 1 Afghanistan 5312 Area harvested 2017 ha ## 2 Afghanistan 5312 Area harvested 2016 ha ## 3 Afghanistan 5312 Area harvested 2015 ha ## 4 Afghanistan 5312 Area harvested 2014 ha ## 5 Afghanistan 5312 Area harvested 2013 ha ## 6 Afghanistan 5312 Area harvested 2012 ha ## Value Value.Footnotes ## 1 13413 Im ## 2 8595 ## 3 9116 ## 4 9005 ## 5 9005 ## 6 8350

In some cases we may need to send a lot of information as part of the URL in a GET request. If it gets to be too long (e.g„ more than 2048 characters) many web servers will reject the request. Instead we may need to use an HTTP POST request (POST requests are often used for submitting web forms). A typical request would have syntax like this search (using _RCurl_ ):

32

**if** ( **url.exists** ('http://www.wormbase.org/db/searches/advanced/dumper')) { x = **postForm** ('http://www.wormbase.org/db/searches/advanced/dumper', species="briggsae", list="", flank3="0", flank5="0", feature="Gene Models", dump = "Plain TEXT", orientation = "Relative to feature", relative = "Chromsome", DNA ="flanking sequences only", .cgifields = **paste** ( **c** ("feature", "orientation", "DNA", "dump","relative"), collapse=", ")) }

Unfortunately that specific search doesn’t work because the server URL and/or API seem to have changed. But it gives you an idea of what the format would look like.

_httr_ and _RCurl_ can handle other kinds of HTTP requests such as PUT and DELETE. Finally, some websites use cookies to keep track of users and you may need to download a cookie in the first interaction with the HTTP server and then send that cookie with later interactions. More details are available in the Nolan and Temple Lang book.

#### **4.4.5 Packaged access to an API**

For popular websites/data sources, a developer may have packaged up the API calls in a userfriendly fashion for use from R, Python or other software. For example there are Python (twitter) and R (twitteR) packages for interfacing with Twitter via its API.

Here’s some example code for Python (the Python package seems to be more fully-featured than the R package). This looks up the US senators’ Twitter names and then downloads a portion of each of their timelines, i.e., the time series of their tweets. Note that Twitter has limits on how much one can download at once.

import json import twitter

---

[Up: contents](index.md) · [Unit 02 — dataTech Part 02 — →](02-unit-02-datatech-part-02.md)
