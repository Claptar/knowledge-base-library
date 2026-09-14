---
title: 1. Text manipulation, string processing and regular expressions (regex)
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1. Text manipulation, string processing and regular expressions (regex)

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Text manipulations in R have a number of things in common with Python,
Perl, and UNIX, as many of these evolved from UNIX. When I use the term
*string* here, I'll be referring to any sequence of characters that may
include numbers, white space, and special characters, rather than to the
character class of R objects. The string or strings will generally be
stored as an R character vector.

## String processing and regular expressions in R

For details of string processing in R, including use of regular expressions, see the [string
processing tutorial](https://berkeley-scf.github.io/tutorial-string-processing).
(You can ignore the sections on Python if you wish.) That tutorial then refers to
the [bash shell tutorial](https://berkeley-scf.github.io/tutorial-using-bash/regex)
for details on regular expressions.

In class we'll work through some problems in the string processing tutorial, focusing in
particular on the use of regular expressions with the *stringr* package.
This will augment our consideration of regular expressions in the shell, in particular
by seeing how we can replace patterns in addition to finding them.

## Regex/string processing challenges

We'll work on these challenges (and perhaps one or two others) in class in the process of working
through the string processing tutorial.

1.  What regex would I use to find any number with or without a decimal place.

2.  Suppose a text string has dates in the form "Aug-3", "May-9", etc.
    and I want them in the form "3 Aug", "9 May", etc. How would I do
    this search and replace operation? (Alternatively, how could I do
    this without using regular expressions at all?)

## Side notes on special characters in R

Recall that when characters are used for special purposes, we need to
'escape' them if we want them interpreted as the actual character. In what
follows, I show this in R, but similar manipulations are sometimes
needed in the shell and in Python.

This can get particularly confusing in R as the backslash is also used
to input special characters such as newline (`\n`) or tab (`\t`).

Here are some examples of using special characters.

> **Note**
> It is hard to compile the Rmd file correctly for these R chunks, so I am just pasting in the output from running in R 'manually' in some cases.)

```r
tmp <- "Harry said, \"Hi\""
## cat(tmp)   # prints out without a newline -- this is hard to show in the pdf
tmp <- "Harry said, \"Hi\".\n"
cat(tmp)      # prints out with the newline

tmp <- c("azar", "foo", "hello\tthere\n")
cat(tmp)
print(tmp)
grep("[\tz]", tmp)   ## search for a tab or a 'z'
```

As a result, in R we often need two backslashes when working with
regular expressions. In the next examples, the first backslash says to
interpret the next backslash literally, with the second backslash being
used to indicate that the caret (\^) should be interpreted literally and
not as a special character in the regular expression syntax.

```r
## Search for characters that are not 'z'
## (using ^ as regular expression syntax)
grep("[^z]", c("a^2", "93", "zzz", "zit", "azar"))

## Search for either a '^' (as a regular charcter) or a 'z':
grep("[\\^z]", c("a^2", "93", "zzz", "zit", "azar"))

## This fails (and the Rmd won't compile) because
## '\^' is not an escape sequence (i.e., a special character):
## grep("[\^z]", c("a^2", "93", "zit", "azar", "zzz"))
## Error: '\^' is an unrecognized escape in character string starting ""[\^"

## Search for exactly three characters
## (using . as regular expression syntax)
grep("^.{3}$", c("abc", "1234", "def"))

## Search for a period (as a regular character)
grep("\\.", c("3.9", "27", "4.2"))

## This fails (and the Rmd won't compile) because
## '\.' is not an escape sequence (i.e., a special character):
## grep("\.", c("3.9", "27")))
## Error: '\.' is an unrecognized escape in character string starting ""\."
```

> **Challenge**
> Explain why we use a single backslash to get a newline and double backslash to write out a Windows path in the examples here:

```r
## Suppose we want to use a \ in our string:
cat("hello\nagain")
cat("hello\\nagain")

cat("My Windows path is: C:\\Users\\My Documents.")
```

For more information, see `?Quotes` in R and the subsections of the
string processing tutorial that discuss backslashes and escaping.

Advanced note: Searching for an actual backslash gets even more
complicated, because we need to pass two backslashes as the regular
expression, so that a literal backslash is searched for. However, to
pass two backslashes, we need to escape each of them with a backslash so
R doesn't treat each backslash as part of a special character. So that's
four backslashes to search for a single backslash! Yikes. One rule of
thumb is just to keep entering backslashes until things work!

```r
## Search for an actual backslash
tmp <- "something \\ other\n"
cat(tmp)

grep("\\\\", tmp)
try(grep("\\", tmp))
```

> **Warning**
> Be careful when cutting and pasting from documents that are not text
> files as you may paste in something that looks like a single or double
> quote, but which R cannot interpret as a quote because it's some other
> ASCII quote character. If you paste in a " from PDF, it will not be
> interpreted as a standard R double quote mark.

Similar things come up in the shell and in Python, but in the shell you
often don't need two backslashes. E.g. you could do this to look for a
literal \^ character.

```bash
grep '\^' file.txt
```

---

[← Overview](02-overview.md) · [Up: contents](index.md) · [2. Interacting with the operating system and external code and configuring R →](04-2-interacting-with-the-operating-system-and-external-code-an.md)
