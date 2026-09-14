---
title: 5. File and string encodings
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit2-dataTech.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. File and string encodings

**Source:** [`units/unit2-dataTech.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Text (either in the form of a file with regular language in it or a data
file with fields of character strings) will often contain characters
that are not part of the [limited ASCII set of
characters](http://en.wikipedia.org/wiki/ASCII), which has $2^{7}=128$
characters and control codes; basically what you see on a standard US
keyboard. Each character takes up one byte (8 bits) of space (there is
an unused bit that comes in handy in the UTF-8 context). We can actually
hand-generate an ASCII file using the binary representation of each
character in R as an illustration.

The letter "M" is encoded based on the ASCII standard in bits as
"01001101" as seen in the link above. For convenience, this is often
written as two base-16 numbers (i.e., hexadecimal), where "0100"="4" and
"1101"="d", hence we have "4d" in hexadecimal.

```r
## 4d in hexadecimal is 'M'
## 0a is a newline (at least in Linux/Mac)
## "0x" is how we tell R we are using hexadecimal
x <- as.raw(c('0x4d','0x6f', '0x6d','0x0a'))  ## i.e., "Mom\n" in ascii
x
charToRaw('Mom\n')
writeBin(x, 'tmp.txt')
readLines('tmp.txt')
system('ls -l tmp.txt', intern = TRUE)
system('cat tmp.txt')
```


When encountering non-ASCII files, in some cases you may need to deal
with the text encoding (the mapping of individual characters (including
tabs, returns, etc.) to a set of numeric codes). There are a variety of
different encodings for text files, with different ones common on
different operating systems.
[UTF-8](https://en.wikipedia.org/wiki/UTF-8) is an encoding for the
Unicode characters that includes more than 110,000 characters from 100
different alphabets/scripts. It's widely used on the web. Latin-1
encodes a small subset of Unicode and contains the characters used in
many European languages (e.g., letters with accents). Here's an example
of using a non-ASCII Unicode character:

```r
## n-tilde and division symbol as Unicode 'code points'
x2_unicode <- 'Pe\u00f1a 3\u00f72'
Encoding(x2_unicode)
x2_unicode
charToRaw(x2_unicode)
charToRaw('\u00f1')    # indeed - two bytes, not one
## specified directly as hexadecimal in UTF-8 encoding
x2_utf8 <- 'Pe\xc3\xb1a 3\xc3\xb72'
x2_utf8

writeBin(x2_unicode, 'tmp2.txt')
## Here n-tilde and division symbol take up two bytes
## but there is an extraneous null byte in there; not sure why.
system('ls -l tmp2.txt')
## The system knows how to interpret the UTF-8 encoded file
## and represent the Unicode character on the screen:
system('cat tmp2.txt')
```

UTF-8 is cleverly designed in terms of the bit-wise representation of
characters such that ASCII characters still take up one byte, and most
other characters take two bytes, but some take four bytes. In fact it is
even more clever than that - the representation is such that the bits of
a one-byte character never appear within the representation of a two-
or three- or four-byte character (and similarly for two-byte characters
in three- or four-byte characters, etc.).

The UNIX utility *file*, e.g. `file tmp.txt` can help provide some
information. *read.table()* in R takes arguments *fileEncoding* and
*encoding* that allow one to specify the encoding as one reads text in.
The UNIX utility *iconv* and the R function *iconv()* can help with
conversions.

In US installations of R, the default encoding is UTF-8; note below that
various types of information are interpreted in US English with the
encoding UTF-8:

```r
Sys.getlocale()
```


With strings already in R, you can convert between encodings with
*iconv()*:

```r
text <- "Melhore sua seguran\xe7a"
Encoding(text)
Encoding(text) <- "latin1"
text  ## this prints out correctly in R, but is not correct in the PDF

text <- "Melhore sua seguran\xe7a"
textUTF8 <- iconv(text, from = "latin1", to = "UTF-8")
Encoding(textUTF8)
textUTF8
iconv(text, from = "latin1", to = "ASCII", sub = "???")
```


You can also mark a string with an encoding, so R knows how to display
it correctly (again, this prints out incorrectly in the PDF):

```r
x <- "fa\xE7ile"
Encoding(x) <- "latin1"
x
## playing around...
x <- "\xa1 \xa2 \xa3 \xf1 \xf2"
Encoding(x) <- "latin1"
x
```


An R error message with multi-byte string in the message often indicates
an encoding issue. In particular errors often arise when trying to do
string manipulations in R on character vectors for which the encoding is
not properly set. Here's an example with some Internet logging data that
we used a few years ago in class in a problem set and which caused some
problems.

```r
load('../data/IPs.RData') # loads in an object named 'text'
tmp <- try(substring(text, 1, 15))
## the issue occurs with the 6402th element (found by trial and error):
tmp <- try(substring(text[1:6401],1,15))
tmp <- try(substring(text[1:6402],1,15))
text[6402] # note the Latin-1 character

table(Encoding(text))
## Option 1
Encoding(text) <- "latin1"
tmp <- try(substring(text, 1, 15))
tmp[6402]
## Option 2
load('../data/IPs.RData') # loads in an object named 'text'
tmp <- try(substring(text, 1, 15))
text <- iconv(text, from = "latin1", to = "UTF-8")
tmp <- try(substring(text, 1, 15))
```

---

[← save information out to JSON](19-save-information-out-to-json.md) · [Up: contents](index.md) · [6. Data structures →](21-6-data-structures.md)
