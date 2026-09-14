---
title: 3 Text manipulation, string processing and regular expressions (regex)
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Text manipulation, string processing and regular expressions (regex)

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Text manipulations in R have a number of things in common with Perl, Python and UNIX, as many of these evolved from UNIX. When I use the term _string_ here, I’ll be referring to any sequence of characters that may include numbers, white space, and special characters, rather than to the character class of R objects. The string or strings will generally be stored as R character vectors.

For material on string processing in R, see the tutorial, _String processing in R and Python_ . (You can ignore the sections on Python for now.) That tutorial then refers to the _Using the bash shell_ tutorial for details on regular expressions. Finally, to test out regular expression syntax see this online tool.

Recall that when characters are used for special purposes, we need to escape them if we want them interpreted as the actual character. In the second example, the first backslash says to interpret the next backslash literally, with the second backslash being used to indicate that the bracket should be interpreted literally.

10

_## for some reason, output from next few lines not printing out in pdf..._ tmp <- "Harry said, \"Hi\"" **cat** (tmp) tmp <- "Harry said, \"Hi\".\n" **cat** (tmp) _## search for either a '^' or a 'z':_ **grep** ("[\\^z]", **c** ("a^2", "93")) _## fails because '\^' is not an escape sequence:_ **grep** ("[\^z]", **c** ("a^2", "93")) **## Error: ’\^’ is an unrecognized escape in character string starting ""[\^"**

Challenge: explain why we use a single backslash to get a newline and double backslash to write out a Windows path in the examples here:

**cat** ("hello\nagain") ## hello ## again **cat** ("hello\\nagain") ## hello\nagain **cat** ("My Windows path is: C:\\Users\\My Documents.") ## My Windows path is: C:\Users\My Documents.

For more information, see ?Quotes in R.

Be careful when cutting and pasting from documents that are not text files as you may paste in something that looks like a single or double quote, but which R cannot interpret as a quote because it’s some other ASCII quote character. If you paste in a “ from PDF, it will not be interpreted as a standard R double quote mark.

### **3.1 Regex practice**

Write a regular expression that matches the following:

1. Only the strings “cat”, “at”, and “t”.

11

2. The strings “cat”, “caat”, “caaat”, etc.

3. “dog”, “Dog”, “dOg”, “doG”, “DOg”, etc. (the word dog in any combination of lower and upper case).

4. Any positive number with or without a decimal point.

5. Any line with exactly two words separated by any amount of whitespace (spaces or tabs). There may or may not be whitespace at the beginning or end of the line.

### **3.2 Regex/string processing challenges**

We’ll work on these challenges in class.

1. What regex would I use to find a spam-like pattern with digits or non-letters inside a word? E.g., I want to find "V1agra" or "Fancy repl!c@ted watches".

2. How would I extract email addresses from lines of text using regular expressions and R string processing?

3. Suppose a text string has dates in the form “Aug-3”, “May-9”, etc. and I want them in the form “3 Aug”, “9 May”, etc. How would I do this search and replace operation? (Alternatively, how could I do this without using regular expressions at all?)

4. How would I search for numeric URLs such as in the file _urls.txt_ .

---

[← Unit 04 — programming Part 15 —](15-unit-04-programming-part-15.md) · [Up: contents](index.md) · [4 Types, classes, and object-oriented programming →](17-4-types-classes-and-object-oriented-programming.md)
