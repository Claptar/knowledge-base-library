---
title: 4 File and string encodings
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 File and string encodings

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Text (either in the form of a file with regular language in it or a data file with fields of character strings) will often contain characters that are not part of the [limited ASCII set of characters](http://en.wikipedia.org/wiki/ASCII), which has 2<sup>7</sup> = 128 characters and control codes; basically what you see on a standard US keyboard. So for non-ASCII files you may need to deal with

8

the text encoding (the mapping of individual characters (including tabs, returns, etc.) to a set of numeric codes). There are a variety of different encodings for text files, with different ones common on different operating systems. UTF-8 is an encoding for the Unicode characters that include more than 110,000 characters from 100 different alphabets/scripts. It’s widely used on the web. Latin-1 encodes a small subset of Unicode and contains the characters used in many European languages (e.g., letters with accents).

The UNIX utility _file_ , e.g. file tmp.txt can help provide some information. _read.table()_ in R takes arguments _fileEncoding_ and _encoding_ that address this issue. The UNIX utility _iconv_ and the R function _iconv()_ can help with conversions.

In US installations of R, the default encoding is UTF-8; note that various types of information are interpreted in US English with the encoding UTF-8:

**Sys.getlocale** ()

---

[← 3 Output from R](04-3-output-from-r.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 06 — →](06-unit-03-rinput-part-06.md)
