---
title: Unit 03 — Rinput Part 25 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 25 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

With strings already in R, you can convert between encodings with _iconv()_ :

text <- "_Melhore sua seguran\xe7a_" textUTF8 <- **iconv** (text, from = "latin1", to = "UTF-8") **Encoding** (textUTF8) ## [1] "UTF-8" textUTF8 ## [1] "_Melhore sua segurança_" **iconv** (text, from = "latin1", to = "ASCII", sub = "???") ## [1] "_Melhore sua seguran???a_"

You can also mark a string with an encoding, so R knows how to display it correctly:

x <- "fa\xE7ile" **Encoding** (x) <- "latin1" x ## [1] "façile" _## playing around..._ x <- "\xa1 \xa2 \xa3 \xf1 \xf2" **Encoding** (x) <- "latin1" x ## [1] "¡ ¢ £ ñ ò"

An R error message with "multi-byte string" in the message often indicates an encoding issue. In particular errors often arise when trying to do string manipulations in R on character vectors for which the encoding is not properly set. Here’s an example with some Internet logging data that we used last year in 243 in a problem set and which caused some problems.

29

**load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8’** _## the issue occurs with the 6402th element (found by trial and error):_ tmp <- **substring** (text[1:6401],1,15) tmp <- **substring** (text[1:6402],1,15) **## Error in substring(text[1:6402], 1, 15): invalid multibyte string at ’<bf>a7lw8’** text[6402] _# note the Latin-1 character_ ## [1] "from 5#c\xbfa7lw8lz2nX,%@ [128.32.244.179] by ncpc-email with _## Interesting:_ **table** ( **Encoding** (text)) ## ## unknown ## 6936 _## Option 1_ **Encoding** (text) <- "latin1" tmp <- **substring** (text, 1, 15) _## Option 2_ **load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8’** text <- **iconv** (text, from = "latin1", to = "UTF-8") tmp <- **substring** (text, 1, 15)

30

---

[← 5 File and string encodings](24-5-file-and-string-encodings.md) · [Up: contents](index.md)
