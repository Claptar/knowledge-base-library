---
title: Unit 02 — dataIO Part 02 —
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit2-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/unit2-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — dataIO Part 02 —

**Source:** [`units/unit2-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/unit2-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

28

CONSUMER_KEY = "" CONSUMER_SECRET = "" OAUTH_TOKEN = "" OAUTH_TOKEN_SECRET = "" auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) api = twitter.Twitter(auth=auth) # get the list of senators senators = api.lists.members(owner_screen_name="gov", slug="us-senate", with open("senators-list.json", "w") as f: json.dump(senators, f, indent=4, sort_keys=True) # get all the senators' timelines names = [d["screen_name"] for d in senators["users"]] timelines = [api.statuses.user_timeline(screen_name=name, count = 500) for name in names] with open("timelines.json", "w") as f: json.dump(timelines, f, indent=4, sort_keys=True)

### **3.6 Accessing dynamic pages**

Some websites dynamically change in reaction to the user behavior. In these cases you need a tool that can mimic the behavior of a human interacting with a site. Some options are:

- _selenium_ (and the _RSelenium_ wrapper for R) is a popular tool for doing this.

- _splash_ (and the _splashr_ wrapper for R) is another approach.

## **4 File and string encodings**

Text (either in the form of a file with regular language in it or a data file with fields of character strings) will often contain characters that are not part of the limited ASCII set of characters, which has 2<sup>7</sup> = 128 characters and control codes; basically what you see on a standard US keyboard. Each character takes up one byte (8 bits) of space. We can actually hand-generate an ASCII file using the binary representation of each character in R as an illustration.

29

_## 39 in hexadecimal is '9' ## 0a is a newline (at least in Linux/Mac) ## 3a is ':'_ x <- **as.raw** ( **c** ('0x39','0x0a','0x3a')) _## i.e., "9\n:" in ascii_ x ## [1] 39 0a 3a **charToRaw** ('9\n:') ## [1] 39 0a 3a **writeBin** (x, 'tmp.txt') **readLines** ('tmp.txt') ## Warning in readLines("tmp.txt"): incomplete final line found on ’tmp.txt’ ## [1] "9" ":" **system** ('ls -l tmp.txt', intern = TRUE) ## [1] "-rw-r--r-- 1 paciorek scfstaff 3 Sep 5 09:37 tmp.txt" **system** ('cat tmp.txt')

For non-ASCII files you may need to deal with the text encoding (the mapping of individual characters (including tabs, returns, etc.) to a set of numeric codes). There are a variety of different encodings for text files, with different ones common on different operating systems. UTF-8 is an encoding for the Unicode characters that includes more than 110,000 characters from 100 different alphabets/scripts. It’s widely used on the web. Latin-1 encodes a small subset of Unicode and contains the characters used in many European languages (e.g., letters with accents). Here’s an example of using a non-ASCII Unicode character:

euro <- '\u20ac' _# Euro currency symbol as Unicode 'code point'_ **Encoding** (euro) euro **writeBin** (euro, 'tmp2.txt') **system** ('ls -l tmp2.txt') _## here the euro takes up four bytes_

30

_## so the system knows how to interpret the UTF-8 encoded file ## and represent the Unicode character on the screen:_ **system** ('cat tmp2.txt')

(I have turned off evaluation of that chunk as something strange is going on when I create the PDF.)

UTF-8 is cleverly designed in terms of the bit-wise representation of characters such that ASCII characters still take up one byte, and most other characters take two bytes, but some take four bytes.

The UNIX utility _file_ , e.g. file tmp.txt can help provide some information. _read.table()_ in R takes arguments _fileEncoding_ and _encoding_ that allow one to specify the encoding as one reads text in. The UNIX utility _iconv_ and the R function _iconv()_ can help with conversions.

In US installations of R, the default encoding is UTF-8; note that various types of information are interpreted in US English with the encoding UTF-8:

**Sys.getlocale** ()

## [1]

With strings already in R, you can convert between encodings with _iconv()_ :

text <- "_Melhore sua seguran\xe7a_" **Encoding** (text) ## [1] "unknown" **Encoding** (text) <- "latin1" text ## [1] "_Melhore sua seguranÃ§a_" text <- "_Melhore sua seguran\xe7a_" textUTF8 <- **iconv** (text, from = "latin1", to = "UTF-8") **Encoding** (textUTF8) ## [1] "UTF-8" textUTF8 ## [1] "_Melhore sua seguranÃ§a_" **iconv** (text, from = "latin1", to = "ASCII", sub = "???") ## [1] "_Melhore sua seguran???a_"

31

You can also mark a string with an encoding, so R knows how to display it correctly:

x <- "fa\xE7ile" **Encoding** (x) <- "latin1" x ## [1] "faÃ§ile" _## playing around..._ x <- "\xa1 \xa2 \xa3 \xf1 \xf2" **Encoding** (x) <- "latin1" x ## [1] "Â¡ Â¢ Â£ Ã _±_ 2”

An R error message with "multi-byte string" in the message often indicates an encoding issue. In particular errors often arise when trying to do string manipulations in R on character vectors for which the encoding is not properly set. Here’s an example with some Internet logging data that we used a few years ago in class in a problem set and which caused some problems.

**load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’** _## the issue occurs with the 6402th element (found by trial and error):_ tmp <- **substring** (text[1:6401],1,15) tmp <- **substring** (text[1:6402],1,15)

**## Error in substring(text[1:6402], 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’**

text[6402] _# note the Latin-1 character_

## [1] "from 5#c\xbfa7lw8lz2nX,%@ [128.32.244.179] by ncpc-email with **table** ( **Encoding** (text))

32

## ## unknown ## 6936 _## Option 1_ **Encoding** (text) <- "latin1" tmp <- **substring** (text, 1, 15) tmp[6402] ## [1] "from 5#cÂ¿a7lw8l" _## Option 2_ **load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’** text <- **iconv** (text, from = "latin1", to = "UTF-8") tmp <- **substring** (text, 1, 15)

## **5 Output from R**

### **5.1 Writing output to files**

Functions for text output are generally analogous to those for input. _write.table()_ , _write.csv()_ , and _writeLines()_ are analogs of _read.table()_ , _read.csv()_ , and _readLines()_ . _write_csv()_ is the _readr_ version of write.csv. _write()_ can be used to write a matrix to a file, specifying the number of columns desired. _cat()_ can be used when you want fine control of the format of what is written out and allows for outputting to a connection (e.g., a file).

_toJSON()_ in the _jsonlite_ package will output R objects as JSON. One use of JSON as output from R would be to _serialize_ the information in an R object such that it could be read into another program.

And of course you can always save to an R data file using _save.image()_ (to save all the objects in the workspace or _save()_ to save only some objects. Happily this is platform-independent so can be used to transfer R objects between different OS.

33

### **5.2 Formatting output**

_cat()_ is a good choice for printing a message to the screen, often better than _print()_ , which is an object-oriented method. You generally won’t have control over how the output of a _print()_ statement is actually printed.

val <- 1.5 **cat** ('My value is ', val, '.\n', sep = '') ## My value is 1.5. **print** ( **paste** ('My value is ', val, '.', sep = '')) ## [1] "My value is 1.5."

We can do more to control formatting with _cat()_ :

_## input_ x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n") ## Powers of 7 **cat** ("exponent result\n\n") ## exponent result result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** ( **format** (i, width = 8), **format** (result, width = 10), "\n", sep = "") } ## 1 7 ## 2 49 ## 3 343 ## 4 2401 ## 5 16807

34

x <- 7 n <- 5 _## display powers_ **cat** ("Powers of", x, "\n") ## Powers of 7 **cat** ("exponent result\n\n") ## exponent result result <- 1 **for** (i **in** 1:n) { result <- result * x **cat** (i, '\t', result, '\n', sep = '') } ## 1 7 ## 2 49 ## 3 343 ## 4 2401 ## 5 16807

One thing to be aware of when writing out numerical data is how many digits are included. For example, the default with _write()_ and _cat()_ is the number of digits that R displays to the screen, controlled by _options()$digits_ . But note that _options()$digits_ seems to have some variability in behavior across operating systems. If you want finer control, use _sprintf()_ , e.g., to print out print out temperatures as reals (“ _f_ ”=floating points) with four decimal places and nine total character positions, followed by a C for Celsius:

temps <- **c** (12.5, 37.234324, 1342434324.79997234, 2.3456e-6, 1e10) **sprintf** ("%9.4f C", temps)

## [1] " 12.5000 C" " 37.2343 C" ## [3] "1342434324.8000 C" " 0.0000 C" ## [5] "10000000000.0000 C" city <- "Boston" **sprintf** ("The temperature in %s was %.4f C.", city, temps[1])

35

## [1] "The temperature in Boston was 12.5000 C." **sprintf** ("The temperature in %s was %9.4f C.", city, temps[1]) ## [1] "The temperature in Boston was 12.5000 C."

Note, to change the number of digits printed to the screen, do options(digits = 5) or specify as an argument to _print()_ or use _sprintf()_ .

36

---

[← Unit 2: Data input/output and webscraping](01-unit-2-data-input-output-and-webscraping.md) · [Up: contents](index.md)
