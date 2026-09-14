---
title: Unit 02 — dataTech Part 06 —
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit2-dataTech.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — dataTech Part 06 —

**Source:** [`units/unit2-dataTech.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit2-dataTech.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

34

#### **4.4.6 Accessing dynamic pages**

Some websites dynamically change in reaction to the user behavior. In these cases you need a tool that can mimic the behavior of a human interacting with a site. Some options are:

- _selenium_ (and the _RSelenium_ wrapper for R) is a popular tool for doing this.

- _splash_ (and the _splashr_ wrapper for R) is another approach.

- _htmlunit_ is another tool for this.

## **5 File and string encodings**

Text (either in the form of a file with regular language in it or a data file with fields of character strings) will often contain characters that are not part of the limited ASCII set of characters, which has 2<sup>7</sup> = 128 characters and control codes; basically what you see on a standard US keyboard. Each character takes up one byte (8 bits) of space (there is an unused bit that comes in handy in the UTF-8 context). We can actually hand-generate an ASCII file using the binary representation of each character in R as an illustration.

The letter “M” is encoded based on the ASCII standard in bits as “01001101” as seen in the link above. For convenience, this is often written as two base-16 numbers (i.e., hexadecimal), where “0100”=”4” and “1101”=”d”, hence we have “4d” in hexadecimal.

_## 4d in hexadecimal is 'M' ## 0a is a newline (at least in Linux/Mac) ## "0x" is how we tell R we are using hexadecimal_ x <- **as.raw** ( **c** ('0x4d','0x6f', '0x6d','0x0a')) _## i.e., "Mom\n" in ascii_ x

## [1] 4d 6f 6d 0a **charToRaw** ('Mom\n') ## [1] 4d 6f 6d 0a **writeBin** (x, 'tmp.txt') **readLines** ('tmp.txt') ## [1] "Mom"

35

**system** ('ls -l tmp.txt', intern = TRUE) ## [1] "-rw-r--r-- 1 paciorek scfstaff 4 Aug 30 08:59 tmp.txt" **system** ('cat tmp.txt')

When encountering non-ASCII files, in some cases you may need to deal with the text encoding (the mapping of individual characters (including tabs, returns, etc.) to a set of numeric codes). There are a variety of different encodings for text files, with different ones common on different operating systems. UTF-8 is an encoding for the Unicode characters that includes more than 110,000 characters from 100 different alphabets/scripts. It’s widely used on the web. Latin-1 encodes a small subset of Unicode and contains the characters used in many European languages (e.g., letters with accents). Here’s an example of using a non-ASCII Unicode character:

_## n-tilde and division symbol as Unicode 'code points'_ x2 <- 'Pe\u00f1a 3\u00f72' **Encoding** (x2) x2 **writeBin** (x2, 'tmp2.txt') _## here n-tilde and division symbol take up two bytes ## but there is an extraneous null byte in there; not sure why_ **system** ('ls -l tmp2.txt') _## so the system knows how to interpret the UTF-8 encoded file ## and represent the Unicode character on the screen:_ **system** ('cat tmp2.txt')

(I have turned off evaluation of that chunk as something strange is going on when I create the PDF.)

UTF-8 is cleverly designed in terms of the bit-wise representation of characters such that ASCII characters still take up one byte, and most other characters take two bytes, but some take four bytes. In fact it is even more clever than that - the representation is such that the bits of a one-byte character never appears within the representation of a two- or three- or four-byte character (and similarly for two-byte characters in three- or four-byte characters, etc.).

The UNIX utility _file_ , e.g. file tmp.txt can help provide some information. _read.table()_ in R takes arguments _fileEncoding_ and _encoding_ that allow one to specify the encoding as one reads text in. The UNIX utility _iconv_ and the R function _iconv()_ can help with conversions.

In US installations of R, the default encoding is UTF-8; note below that various types of information are interpreted in US English with the encoding UTF-8:

36

**Sys.getlocale** ()

## [1]

With strings already in R, you can convert between encodings with _iconv()_ :

text <- "Melhore sua seguran\xe7a" **Encoding** (text) ## [1] "unknown" **Encoding** (text) <- "latin1" text _## this prints out correctly in R, but is not correct in the PDF_ ## [1] "Melhore sua seguranÃ§a" text <- "Melhore sua seguran\xe7a" textUTF8 <- **iconv** (text, from = "latin1", to = "UTF-8") **Encoding** (textUTF8) ## [1] "UTF-8" textUTF8 ## [1] "Melhore sua seguranÃ§a" **iconv** (text, from = "latin1", to = "ASCII", sub = "???") ## [1] "Melhore sua seguran???a"

You can also mark a string with an encoding, so R knows how to display it correctly (again, this prints out incorrectly in the PDF):

x <- "fa\xE7ile" **Encoding** (x) <- "latin1" x ## [1] "faÃ§ile" _## playing around..._

37

x <- "\xa1 \xa2 \xa3 \xf1 \xf2" **Encoding** (x) <- "latin1" x

## [1] "Â¡ Â¢ Â£ Ã _±_ 2”

An R error message with "multi-byte string" in the message often indicates an encoding issue. In particular errors often arise when trying to do string manipulations in R on character vectors for which the encoding is not properly set. Here’s an example with some Internet logging data that we used a few years ago in class in a problem set and which caused some problems.

**load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’**

_## the issue occurs with the 6402th element (found by trial and error):_ tmp <- **substring** (text[1:6401],1,15) tmp <- **substring** (text[1:6402],1,15)

**## Error in substring(text[1:6402], 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’**

text[6402] _# note the Latin-1 character_

## [1] "from 5#c\xbfa7lw8lz2nX,%@ [128.32.244.179] by ncpc-email with **table** ( **Encoding** (text))

## ## unknown ## 6936 _## Option 1_ **Encoding** (text) <- "latin1" tmp <- **substring** (text, 1, 15) tmp[6402]

38

## [1] "from 5#cÂ¿a7lw8l" _## Option 2_ **load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’** text <- **iconv** (text, from = "latin1", to = "UTF-8") tmp <- **substring** (text, 1, 15)

39

---

[← Unit 02 — dataTech Part 05 —](05-unit-02-datatech-part-05.md) · [Up: contents](index.md)
