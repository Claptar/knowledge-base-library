---
title: Unit 03 — dataIO Part 23 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 23 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can also mark a string with an encoding, so R knows how to display it correctly:

x <- "fa\xE7ile" **Encoding** (x) <- "latin1" x ## [1] "façile" _## playing around..._ x <- "\xa1 \xa2 \xa3 \xf1 \xf2" **Encoding** (x) <- "latin1" x ## [1] "¡ ¢ £ ñ ò"

An R error message with "multi-byte string" in the message often indicates an encoding issue. In particular errors often arise when trying to do string manipulations in R on character vectors for which the encoding is not properly set. Here’s an example with some Internet logging data that we used a few years ago in class in a problem set and which caused some problems.

**load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’** _## the issue occurs with the 6402th element (found by trial and error):_ tmp <- **substring** (text[1:6401],1,15) tmp <- **substring** (text[1:6402],1,15)

34

**## Error in substring(text[1:6402], 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’** text[6402] _# note the Latin-1 character_ ## [1] "from 5#c\xbfa7lw8lz2nX,%@ [128.32.244.179] by ncpc-email with **table** ( **Encoding** (text)) ## ## unknown ## 6936 _## Option 1_ **Encoding** (text) <- "latin1" tmp <- **substring** (text, 1, 15) tmp[6402] ## [1] "from 5#c¿a7lw8l" _## Option 2_ **load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15) **## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’** text <- **iconv** (text, from = "latin1", to = "UTF-8") tmp <- **substring** (text, 1, 15)

35

---

[← Unit 03 — dataIO Part 22 —](22-unit-03-dataio-part-22.md) · [Up: contents](index.md)
