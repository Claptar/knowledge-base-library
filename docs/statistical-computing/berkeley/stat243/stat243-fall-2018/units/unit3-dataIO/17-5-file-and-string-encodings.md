---
title: 5 File and string encodings
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 File and string encodings

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Text (either in the form of a file with regular language in it or a data file with fields of character strings) will often contain characters that are not part of the limited ASCII set of characters, which has 2<sup>7</sup> = 128 characters and control codes; basically what you see on a standard US keyboard. Each character takes up one byte (8 bits) of space. We can actually hand-generate an ASCII file using the binary representation of each character in R as an illustration.

_## 39 in hexadecimal is '9' ## 0a is a newline (at least in Linux/Mac) ## 3a is ':'_ x <- **as.raw** ( **c** ('0x39','0x0a','0x3a')) _## i.e., "9\n:" in ascii_ x ## [1] 39 0a 3a

**charToRaw** ('9\n:') ## [1] 39 0a 3a

32

**writeBin** (x, 'tmp.txt') **readLines** ('tmp.txt') ## Warning in readLines("tmp.txt"): incomplete final line found on ’tmp.txt’ ## [1] "9" ":" **system** ('ls -l tmp.txt', intern = TRUE) ## [1] "-rw-r--r-- 1 paciorek scfstaff 3 Sep 5 2018 tmp.txt" **system** ('cat tmp.txt')

For non-ASCII files you may need to deal with the text encoding (the mapping of individual characters (including tabs, returns, etc.) to a set of numeric codes). There are a variety of different encodings for text files, with different ones common on different operating systems. UTF-8 is an encoding for the Unicode characters that includes more than 110,000 characters from 100 different alphabets/scripts. It’s widely used on the web. Latin-1 encodes a small subset of Unicode and contains the characters used in many European languages (e.g., letters with accents). Here’s an example of using a non-ASCII Unicode character:

euro <- '\u20ac' _# Euro currency symbol as Unicode 'code point'_ **Encoding** (euro) euro **writeBin** (euro, 'tmp2.txt') **system** ('ls -l tmp2.txt') _## here the euro takes up four bytes ## so the system knows how to interpret the UTF-8 encoded file ## and represent the Unicode character on the screen:_ **system** ('cat tmp2.txt')

(I have turned off evaluation of that chunk as something strange is going on when I create the PDF.)

UTF-8 is cleverly designed in terms of the bit-wise representation of characters such that ASCII characters still take up one byte, and most other characters take two bytes, but some take four bytes.

The UNIX utility _file_ , e.g. file tmp.txt can help provide some information. _read.table()_ in R takes arguments _fileEncoding_ and _encoding_ that allow one to specify the encoding as one reads text in. The UNIX utility _iconv_ and the R function _iconv()_ can help with conversions.

33

In US installations of R, the default encoding is UTF-8; note that various types of information are interpreted in US English with the encoding UTF-8:

**Sys.getlocale** ()

---

[← Unit 03 — dataIO Part 16 —](16-unit-03-dataio-part-16.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 18 — →](18-unit-03-dataio-part-18.md)
