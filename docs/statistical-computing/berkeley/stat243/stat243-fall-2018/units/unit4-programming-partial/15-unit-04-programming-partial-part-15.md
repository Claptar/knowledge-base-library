---
title: Unit 04 — programming partial Part 15 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 15 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Challenge: explain why we use a single backslash to get a newline and double backslash to write out a Windows path in the examples here:

10

**cat** ("hello\nagain") ## hello ## again **cat** ("hello\\nagain") ## hello\nagain **cat** ("My Windows path is: C:\\Users\\My Documents.") ## My Windows path is: C:\Users\My Documents.

For more information, see ?Quotes in R and the subsections of the string processing tutorial that discuss backslashes and escaping.

Be careful when cutting and pasting from documents that are not text files as you may paste in something that looks like a single or double quote, but which R cannot interpret as a quote because it’s some other ASCII quote character. If you paste in a “ from PDF, it will not be interpreted as a standard R double quote mark.

### 3.2 Regex practice

Write a regular expression that matches the following:

1. Only the strings “cat”, “at”, and “t”.

2. The strings “cat”, “caat”, “caaat”, etc.

3. “dog”, “Dog”, “dOg”, “doG”, “DOg”, etc. (the word dog in any combination of lower and upper case).

4. Any line with exactly two words separated by any amount of whitespace (spaces or tabs). There may or may not be whitespace at the beginning or end of the line.

5. Any positive number with or without a decimal point.

### 3.3 Regex/string processing challenges

We’ll work on these challenges in class in the process of working through the string processing tutorial.

11

1. What regex would I use to find a spam-like pattern with digits or non-letters inside a word? E.g., I want to find "V1agra" or "Fancy repl!c@ted watches".

2. How would I extract email addresses from lines of text using regular expressions and R string processing?

3. Suppose a text string has dates in the form “Aug-3”, “May-9”, etc. and I want them in the form “3 Aug”, “9 May”, etc. How would I do this search and replace operation? (Alternatively, how could I do this without using regular expressions at all?)

---

[← 3 Text manipulation, string processing and regular expressions (regex)](14-3-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [4 Types, classes, and object-oriented programming →](16-4-types-classes-and-object-oriented-programming.md)
