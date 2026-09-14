---
title: '[1] "Do an internship course." ## gsub(''<.>'', '''', text)'
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# [1] "Do an internship course." ## gsub('<.>', '', text)

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

What went wrong?

One solution is to append a ? to the repetition syntax to cause the matching to be non-greedy. Here’s an example.

**str_replace_all** (text, "<.*?>", "") ## [1] "Do an internship in place of one course." _## gsub('<.*?>', '', text)_

However, one can often avoid greedy matching by being more clever.

**Challenge** : How could we change our regexp to avoid the greedy matching without using the “?”?

**Regular expressions in other contexts** Regular expression can be used in a variety of places. E.g., to split by any number of white space characters

line <- "a dog\tjumped\nover \tthe moon." **cat** (line) ## a dog jumped ## over the moon. **strsplit** (line, split = "[[:space:]]+") ## [[1]] ## [1] "a" "dog" "jumped" "over" "the" ## [6] "moon." **strsplit** (line, split = "[[:blank:]]+") ## [[1]] ## [1] "a" "dog" "jumped\nover" ## [4] "the" "moon."

66

_Table 2. Regular expression syntax._

|Syntax|What it matches|
|---|---|
|_^ab_|match ’ab’ at the beginningof the string|
|_ab$_|match ’ab’ at the end of the string|
|_[abc]_|match a or b or c anywhere(this is a character class)|
|_[ \t]_|match a space or a tab|
|_(ab|cd|def)_|match anyof the strings in the set|
|_(ab){2,9}_|match ’ab’ repeated at least 2 and no more than 9 times|
|_(ab){2,}_|match ’ab’ repeated 2 or more times|
|_[0-9a-z]_|match a single digit or lower-case alphabetical|
|_[^0-9]_|match anysingle character except a digit|
|_a.b_|match a and b separated bya single character|
|_a.*b_|match a and b separated byanynumber of(or no)characters|
|_a.+b_|like a.*b but must have at least one character in between|
|_[[:digit:]]_|match_digit_class; other classes are_alpha_,_alnum_,_lower_,_upper_,_punct_,<br>_blank_,_space_ (see ?regexp)|
|_\\[_|double backslashes are used if we want to search for a meta-character used<br>in regexpsyntax|


**Summary** Table 2 summarizes the key syntax in regular expressions.

### **8.4 Webscraping**

A couple useful packages for this are _RCurl_ and _XML_ .

- _RCurl_ allows one to interact with webpages, making HTTP requests, downloading information, submitting forms, etc.

- We’ve already seen the use of the _XML_ package to process HTML in Unit 3.

67

---

[← Unit 04 — usingR Part 48 —](48-unit-04-usingr-part-48.md) · [Up: contents](index.md)
