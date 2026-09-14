---
title: 8 Text manipulations and regular expressions
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Text manipulations and regular expressions

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Text manipulations in R have a number of things in common with Perl, Python and UNIX, as many of these evolved from UNIX. When I use the term _string_ here, I’ll be refering to any sequence of characters that may include numbers, white space, and special characters, rather than to the character class of R objects. The string or strings will generally be stored as R character vectors.

56

### **8.1 Basic text manipulation**

A few of the basic R functions for manipulating strings are _paste()_ , _strsplit()_ , and _substring()_ . _paste()_ and _strsplit()_ are basically inverses of each other: _paste()_ concatenates together an arbitrary set of strings (or a vector, if using the _collapse_ argument) with a user-specified separator character, while _strsplit()_ splits apart based on a delimiter/separator. _substring()_ splits apart the elements of a character vector based on fixed widths. Note that all of these operate in a vectorized fashion.

out <- **paste** ("My", "name", "is", "Chris", ".", sep = " ") **paste** ( **c** ("My", "name", "is", "Chris", "."), collapse = " ") _# equivalent_ ## [1] "My name is Chris ." **strsplit** (out, split = " ") ## [[1]] ## [1] "My" "name" "is" "Chris" "."

Note that _strsplit()_ returns a list because it can operate on a character vector (i.e., on multiple strings).

_nchar()_ tells the number of characters in a string.

To identify particular subsequences in strings, there are several related R functions. _grep()_ will look for a specified string within an R character vector and report back indices identifying the elements of the vector in which the string was found in (using the _fixed=TRUE_ argument ensures that regular expressions are NOT used). _gregexpr()_ will indicate the position in each string that the specified string is found (use _regexpr()_ if you only want the first occurrence). _gsub()_ can be used to replace a specified string with a replacement string (use _sub()_ if you only want to replace only the first occurrence).

vars <- **c** ("P", "HCA24", "SOH02") **substring** (vars, 2, 3) ## [1] "" "CA" "OH"

vars <- **c** ("date98", "size98", "x98weights98", "sdfsd") **grep** ("98", vars) ## [1] 1 2 3 **gregexpr** ("98", vars)

57

---

[← Unit 04 — usingR Part 38 —](38-unit-04-usingr-part-38.md) · [Up: contents](index.md) · [Unit 04 — usingR Part 40 — →](40-unit-04-usingr-part-40.md)
