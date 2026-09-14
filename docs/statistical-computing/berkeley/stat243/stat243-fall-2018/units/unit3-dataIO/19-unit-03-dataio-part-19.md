---
title: Unit 03 — dataIO Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 19 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

An R error message with "multi-byte string" in the message often indicates an encoding issue. In particular errors often arise when trying to do string manipulations in R on character vectors for which the encoding is not properly set. Here’s an example with some Internet logging data that we used a few years ago in class in a problem set and which caused some problems.

**load** ('../data/IPs.RData') _# loads in an object named 'text'_ tmp <- **substring** (text, 1, 15)

**## Error in substring(text, 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’** _## the issue occurs with the 6402th element (found by trial and error):_ tmp <- **substring** (text[1:6401],1,15) tmp <- **substring** (text[1:6402],1,15)

**## Error in substring(text[1:6402], 1, 15): invalid multibyte string at ’<bf>a7lw8<6c>z2nX,%@ [128.32.244.179] by ncpc-email with ESMTP ## (SMTPD32-7.04) id A06E24A0116; Mon, 10 Jun 2002 11:43:42 +0800’**

text[6402] _# note the Latin-1 character_

---

[← Unit 03 — dataIO Part 18 —](18-unit-03-dataio-part-18.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 20 — →](20-unit-03-dataio-part-20.md)
