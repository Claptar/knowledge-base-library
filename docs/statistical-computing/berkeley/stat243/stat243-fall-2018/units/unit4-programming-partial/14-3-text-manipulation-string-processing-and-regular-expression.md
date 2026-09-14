---
title: 3 Text manipulation, string processing and regular expressions (regex)
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Text manipulation, string processing and regular expressions (regex)

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Text manipulations in R have a number of things in common with Perl, Python and UNIX, as many of these evolved from UNIX. When I use the term string here, I’ll be referring to any sequence of characters that may include numbers, white space, and special characters, rather than to the character class of R objects. The string or strings will generally be stored as R character vectors.

For material on string processing in R, see the tutorial, String processing in R and Python. (You can ignore the sections on Python.) That tutorial then refers to the Using the bash shell tutorial for details on regular expressions. Finally, to test out regular expression syntax see this online tool.

In class we’ll discuss various answers to the regex practice below to get started and then we’ll work through the string processing tutorial, focusing in particular on the use of regular expressions.

### 3.1 Side notes on special characters

Recall that when characters are used for special purposes, we need to escape them if we want them interpreted as the actual character. In the second example, the first backslash says to interpret the next backslash literally, with the second backslash being used to indicate that the bracket should be interpreted literally.

---

[← Unit 04 — programming partial Part 13 —](13-unit-04-programming-partial-part-13.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 15 — →](15-unit-04-programming-partial-part-15.md)
