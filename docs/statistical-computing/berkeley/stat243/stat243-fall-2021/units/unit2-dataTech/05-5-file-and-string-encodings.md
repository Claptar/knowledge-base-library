---
title: 5 File and string encodings
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit2-dataTech.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit2-dataTech.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 File and string encodings

Text (either in the form of a file with regular language in it or a data file with fields of character
strings) will often contain characters that are not part of the limited ASCII set of characters, which
has $2^7 = 128$ characters and control codes; basically what you see on a standard US keyboard.
Each character takes up one byte (8 bits) of space (there is an unused bit that comes in handy in
the UTF-8 context). We can actually hand-generate an ASCII file using the binary representation
of each character in R as an illustration.

The letter “M” is encoded based on the ASCII standard in bits as “01001101” as seen in the link
above. For convenience, this is often written as two base-16 numbers (i.e., hexadecimal), where
“0100”=”4” and “1101”=”d”, hence we have “4d” in hexadecimal.

```r
## 4d in hexadecimal is 'M'
## 0a is a newline (at least in Linux/Mac)
## "0x" is how we tell R we are using hexadecimal
x <- as.raw(c('0x4d','0x6f', '0x6d','0x0a')) ## i.e., "Mom\n" in ascii
x
## [1] 4d 6f 6d 0a
charToRaw('Mom\n')
## [1] 4d 6f 6d 0a
writeBin(x, 'tmp.txt')
readLines('tmp.txt')
## [1] "Mom"
system('ls -l tmp.txt', intern = TRUE)
## [1] "-rw-r--r-- 1 paciorek scfstaff 4 Aug 30 08:59 tmp.txt"
system('cat tmp.txt')
```

When encountering non-ASCII files, in some cases you may need to deal with the text encoding
(the mapping of individual characters (including tabs, returns, etc.) to a set of numeric codes).
There are a variety of different encodings for text files, with different ones common on different
operating systems. UTF-8 is an encoding for the Unicode characters that includes more than
110,000 characters from 100 different alphabets/scripts. It’s widely used on the web. Latin-1
encodes a small subset of Unicode and contains the characters used in many European languages
(e.g., letters with accents). Here’s an example of using a non-ASCII Unicode character:

```r
## n-tilde and division symbol as Unicode 'code points'
x2 <- 'Pe\u00f1a 3\u00f72'
Encoding(x2)
x2
writeBin(x2, 'tmp2.txt')
## here n-tilde and division symbol take up two bytes
## but there is an extraneous null byte in there; not sure why
system('ls -l tmp2.txt')
## so the system knows how to interpret the UTF-8 encoded file
## and represent the Unicode character on the screen:
system('cat tmp2.txt')
```

(I have turned off evaluation of that chunk as something strange is going on when I create the
PDF.)

UTF-8 is cleverly designed in terms of the bit-wise representation of characters such that ASCII
characters still take up one byte, and most other characters take two bytes, but some take four
bytes. In fact it is even more clever than that - the representation is such that the bits of a one-byte
character never appears within the representation of a two- or three- or four-byte character (and
similarly for two-byte characters in three- or four-byte characters, etc.).

The UNIX utility *file*, e.g. `file tmp.txt` can help provide some information. *read.table()*
in R takes arguments *fileEncoding* and *encoding* that allow one to specify the encoding as one
reads text in. The UNIX utility *iconv* and the R function *iconv()* can help with conversions.

In US installations of R, the default encoding is UTF-8; note below that various types of information are interpreted in US English with the encoding UTF-8:

```r
Sys.getlocale()
## [1] "LC_CTYPE=en_US.UTF-8;LC_NUMERIC=C;LC_TIME=en_US.UTF-8;LC_COLLATE=en_US.UTF-8;LC_MONETARY=en_US.UTF-8;LC_MESSAGES=en_US.UTF-8;LC_PAPER=en_US.UTF-8;LC_NAME=C;LC_ADDRESS=C;LC_TELEPHONE=C;LC_MEASUREMENT=en_US.UTF-8;LC_IDENTIFICATION=C"
```

With strings already in R, you can convert between encodings with *iconv()*:

```r
text <- "Melhore sua seguran\xe7a"
Encoding(text)
## [1] "unknown"
Encoding(text) <- "latin1"
text ## this prints out correctly in R, but is not correct in the PDF
## [1] "Melhore sua seguranÃ§a"
text <- "Melhore sua seguran\xe7a"
textUTF8 <- iconv(text, from = "latin1", to = "UTF-8")
Encoding(textUTF8)
## [1] "UTF-8"
textUTF8
## [1] "Melhore sua seguranÃ§a"
iconv(text, from = "latin1", to = "ASCII", sub = "???")
## [1] "Melhore sua seguran???a"
```

You can also mark a string with an encoding, so R knows how to display it correctly (again,
this prints out incorrectly in the PDF):

```r
x <- "fa\xE7ile"
Encoding(x) <- "latin1"
x
## [1] "faÃ§ile"
## playing around...
x <- "\xa1 \xa2 \xa3 \xf1 \xf2"
Encoding(x) <- "latin1"
x
## [1] "Â¡ Â¢ Â£ Ã± 2”
```

An R error message with "multi-byte string" in the message often indicates an encoding issue.
In particular errors often arise when trying to do string manipulations in R on character vectors for
which the encoding is not properly set. Here’s an example with some Internet logging data that we
used a few years ago in class in a problem set and which caused some problems.

```r
load('../data/IPs.RData') # loads in an object named 'text'
tmp <- substring(text, 1, 15)
## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@
[128.32.244.179] by ncpc-email with ESMTP
## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’
## the issue occurs with the 6402th element (found by trial and error):
tmp <- substring(text[1:6401],1,15)
tmp <- substring(text[1:6402],1,15)
## Error in substring(text[1:6402], 1, 15): invalid multibyte string
at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP
## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’
text[6402] # note the Latin-1 character
## [1] "from 5#c\xbfa7lw8lz2nX,%@ [128.32.244.179] by ncpc-email with ESMTP\n(SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800"
table(Encoding(text))
##
## unknown
## 6936
## Option 1
Encoding(text) <- "latin1"
tmp <- substring(text, 1, 15)
tmp[6402]
## [1] "from 5#cÂ¿a7lw8l"
## Option 2
load('../data/IPs.RData') # loads in an object named 'text'
tmp <- substring(text, 1, 15)
## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@
[128.32.244.179] by ncpc-email with ESMTP
## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’
text <- iconv(text, from = "latin1", to = "UTF-8")
tmp <- substring(text, 1, 15)
```

---

[← 4 Webscraping and working with HTML, XML, and JSON](04-4-webscraping-and-working-with-html-xml-and-json.md) · [Up: contents](index.md)
