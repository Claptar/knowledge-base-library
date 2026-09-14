---
title: 3 Text manipulation, string processing and regular expressions (regex)
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Text manipulation, string processing and regular expressions (regex)

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Text manipulations in R have a number of things in common with Python, Perl, and UNIX, as many of these evolved from UNIX. When I use the term _string_ here, I’ll be referring to any sequence of characters that may include numbers, white space, and special characters, rather than to the character class of R objects. The string or strings will generally be stored as R character vectors.

For material on string processing in R, see the tutorial, _String processing in R and Python_ . (You can ignore the sections on Python.) That tutorial then refers to the _Using the bash shell_ tutorial for details on regular expressions. Finally, to test out regular expression syntax see this online tool.

In class we’ll discuss various answers to the regex practice below to get started and then we’ll work through the string processing tutorial, focusing in particular on the use of regular expressions.

### **3.1 Regex practice**

Write a regular expression that matches the following:

1. Only the strings “cat”, “at”, and “t”.

2. The strings “cat”, “caat”, “caaat”, etc.

3. “dog”, “Dog”, “dOg”, “doG”, “DOg”, etc. (the word dog in any combination of lower and upper case).

4. Any line with exactly two words separated by any amount of whitespace (spaces or tabs). There may or may not be whitespace at the beginning or end of the line.

5. Any positive number with or without a decimal point.

### **3.2 Regex/string processing challenges**

We’ll work on these challenges in class in the process of working through the string processing tutorial.

1. What regex would I use to find a spam-like pattern with digits or non-letters inside a word? E.g., I want to find "V1agra" or "Fancy repl!c@ted watches".

2. How would I extract email addresses from lines of text using regular expressions and R string processing?

10

3. Suppose a text string has dates in the form “Aug-3”, “May-9”, etc. and I want them in the form “3 Aug”, “9 May”, etc. How would I do this search and replace operation? (Alternatively, how could I do this without using regular expressions at all?)

### **3.3 Side notes on special characters in R**

Recall that when characters are used for special purposes, we need to escape them if we want them interpreted as the actual character. In what follows, I show this in R, but similar manipulations are sometimes needed in the shell and in Python.

This can get particularly confusing in R as the backslash is also used to input special characters such as newline (\n) or tab (\t). (Note that it is hard to get the PDF to compile correctly for these R chunks, so I am just pasting in the output from running in R ’manually’.)

tmp <- "Harry said, \"Hi\"" _## cat(tmp) ## prints out without a newline (It's hard to show in the pdf.)_ tmp <- "Harry said, \"Hi\".\n" **cat** (tmp) _## Harry said, "Hi"._ tmp <- **c** ("azar", "foo", "hello\tthere\n") **cat** (tmp) _## azar foo hello there_ **print** (tmp) _## [1] "azar" "foo" "hello\tthere\n"_ **grep** ("[\tz]", tmp) _## [1] 1 3_

As a result in R, we often need two backslashes when working with regular expressions. In these examples, the first backslash says to interpret the next backslash literally, with the second backslash being used to indicate that the caret (^) should be interpreted literally and not as a special character used for specifying regular expressions.

_## Search for characters that are not 'z' ## (using ^ as regular expression syntax)_ **grep** ("[^z]", **c** ("a^2", "93", "zit", "azar", "zzz")) _# [1] 1 2 3 4_

11

_## Search for either a '^' (as a regular charcter) or a 'z':_ **grep** ("[\\^z]", **c** ("a^2", "93", "zit", "azar", "zzz")) _# [1] 1 2 3 5 ## This fails because '\^' is not an escape sequence:_ **grep** ("[\^z]", **c** ("a^2", "93", "zit", "azar", "zzz")) _# Error: '\^' is an unrecognized escape in character string starting ""[\^" ## Search for exactly three characters ## (using . as regular expression syntax)_ **grep** ("^.{3}$", **c** ("abc", "1234")) _# [1] 1 ## Search for a period (as a regular character)_ **grep** ("\\.", **c** ("3.9", "27")) _# [1] 1 ## This fails because '\.' is not an escape sequence_ **grep** ("\.", **c** ("3.9", "27")) _# Error: '\.' is an unrecognized escape in character string starting ""\."_

Challenge: explain why we use a single backslash to get a newline and double backslash to write out a Windows path in the examples here:

_## Suupose we want to use a \ in our string:_ **cat** ("hello\nagain") ## hello ## again **cat** ("hello\\nagain") ## hello\nagain **cat** ("My Windows path is: C:\\Users\\My Documents.") ## My Windows path is: C:\Users\My Documents.

12

For more information, see ?Quotes in R and the subsections of the string processing tutorial that discuss backslashes and escaping.

Advanced note: Searching for an actual backslash gets even more complicated, because we need to pass two backslashes as the regular expression, so that a literal backslash is searched for. However, to pass two backslashes, we need to escape each of them with a backslash so R doesn’t treat each backslash as part of a special character. So that’s four backslashes to search for a single backslash. Yikes. One rule of thumb is just to keep entering backslashes until things work!

_## Search for an actual backslash_ tmp <- "something \\ other\n" **cat** (tmp) _# something \ other_ **grep** ("\\\\", tmp) _# [1] 1_ **grep** ("\\", tmp) _# Error in grep("\\", tmp) : # invalid regular expression '\', reason 'Trailing backslash'_

<mark>grep '\^' file.txt</mark>

---

[← Unit 05 — programming Part 14 —](14-unit-05-programming-part-14.md) · [Up: contents](index.md) · [4 Types, classes, and object-oriented programming →](16-4-types-classes-and-object-oriented-programming.md)
