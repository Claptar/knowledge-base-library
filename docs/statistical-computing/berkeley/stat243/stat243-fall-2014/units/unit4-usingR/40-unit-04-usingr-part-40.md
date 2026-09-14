---
title: Unit 04 — usingR Part 40 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 40 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

58

_Table 1. Dictionary of stringr functions._

|Function|What it does|
|---|---|
|str_detect|detectspattern,returningTRUE/FALSE|
|str_count|counts matches|
|str_locate/str_locate_all|detectspattern,returning positions of matchingcharacters|
|str_extract/str_extract_all|detectspattern,returningmatches|
|str_replace/str_replace_all|detectspattern and replaces matches|


### **8.2 Using** **_stringr_**

The _stringr_ package wraps the various core string manipulation functions to provide a common interface. It also removes some of the clunkiness involved in some of the string operations with the base string functions, such as having to to call _gregexpr()_ and then _regmatches()_ to pull out the matched strings. For PS3 and your future endeavors, I’d suggest using _stringr_ functions in place of R’s base string functions.

The basic interface is function(strings, pattern, [replace]).

Table 1 provides an overview of the key functions, which are basically wrappers for _grep()_ , _gsub()_ , _gregexpr()_ , etc.

The analogue of _regexpr()_ vs. _gregexpr()_ and _sub()_ vs. _gsub()_ is that most of the functions have versions that return all the matches, not just the first match, e.g. _str_locate_all()_ , _str_extract_all(),_ etc. Note that the _all functions return lists while the non-_all functions return vectors.

To specify options, you can wrap these functions around the pattern argument: fixed(pattern), ignore.case(pattern), and perl(pattern). For example,

**require** (stringr) _## Loading required package: stringr_ str <- **c** ("Apple", "Basic", "applied") **str_locate** (str, **ignore.case** ("app")) ## start end ## [1,] 1 3 ## [2,] NA NA ## [3,] 1 3

59

### **8.3 Regular expressions (regexp/regex)**

**Overview and core syntax** The _grep()_ , _gregexpr()_ and _gsub()_ functions and their _stringr_ analogs are more powerful when used with regular expressions. Regular expressions are a domain-specific language for finding patterns and are one of the key functionalities in scripting languages such as Perl and Python, as well as the UNIX utilities _sed_ , _awk_ and _grep_ . Duncan Temple Lang (UC Davis Statistics) has written a nice tutorial that I’ve put in the repository ( _regexpr-Lang.pdf_ ) or check out Sections 9.9 and 11 of Murrell. We’ll just cover the use of regular expressions in R, but once you know that, it would be easy to use them elsewhere (Python, grep and other UNIX commands, etc.). What I describe here is the “extended regular expression” syntax (POSIX 1003.2), but with the argument Perl=TRUE or perl(pattern) in _stringr_ , you can get Perl-style regular expressions. At the level we’ll consider them, the syntax is quite similar.

The basic idea of regular expressions is that they allow us to find matches of strings or patterns in strings, as well as do substitution. Regular expressions are good for tasks such as:

- extracting pieces of text - for example finding all the links in an html document;

- creating variables from information found in text;

- cleaning and transforming text into a uniform format;

- mining text by treating documents as data; and

- scraping the web for data.

Regular expressions are constructed from three things:

_Literal characters_ are matched only by the characters themselves,

_Character classes_ are matched by any single member in the class, and

_Modifiers_ operate on either of the above or combinations of them.

Note that the syntax is very concise, so it’s helpful to break down individual regular expressions into the component parts to understand them. As Murrell notes, since regexp are their own language, it’s a good idea to build up a regexp in pieces as a way of avoiding errors just as we would with any computer code. _gregexpr()_ is particularly useful in seeing **what** was matched to help in understanding and learning regular expression syntax and debugging your regexp.

The special characters (meta-characters) used for defining regular expressions are: _* . ^ $ + ? ( ) [ ] { } | \_ . To use these characters literally as characters, we have to ’escape’ them. In R, we have to use two backslashes insstead of a single backslash because R uses a single backslash to symbolize certain control characters, such as _\n_ for newline. Outside of R, one would only need a single backslash.

60

**Character sets and character classes** If we want to search for any one of a set of characters, we use a character set, such as [13579] or [abcd] or [0-9] (where the dash indicates a sequence) or [0-9a-z] or [ \t]. To indicate any character not in a set, we place a ^ just inside the first bracket: [^abcd]. The period stands for any character.

There are a bunch of named character classes so that we don’t have write out common sets of characters. The syntax is [:class:] where _class_ is the name of the class. The classes include the _digit_ , _alpha_ , _alnum_ , _lower_ , _upper_ , _punct_ , _blank_ , _space_ (see ?regexp in R for formal definitions of all of these, but most are fairly self-explanatory). To make a character set with a character class you need two square brackets, e.g. the digit class: [[:digit:]]. Or we can make a combined character set such as [[:alnum:]_]. E.g., the latter would be useful in looking for email addresses. If you use the [:class:] syntax, you need to use the perl=TRUE argument to the relevant function to make use of Perl-style regular expressions.

addresses <- **c** ("john@att.com", "stat243@bspace.berkeley.edu", "john_smith@att.com") **str_detect** (addresses, **perl** ("[[:digit:]_]")) ## [1] FALSE TRUE TRUE

_## grep('[[:digit:]_]', addresses, perl = TRUE)_

Some synonyms for the various classes are: \\w = [:alnum:], \\W = ^[:alnum:], \\d = [:digit], \\D = ^[:digit:], \\s = [:space:], \\S = ^[:space:]. Here are some more examples showing a wide range of string functionality:

text <- **c** ("john", "jennifer pierce", "Juan carlos rey") **str_detect** (text, "[ \t]")

---

[← 8 Text manipulations and regular expressions](39-8-text-manipulations-and-regular-expressions.md) · [Up: contents](index.md) · [[1] FALSE TRUE TRUE ## grep('[ \t]', text) strlocateall (text, "[ \t]") →](41-1-false-true-true-grep-t-text-strlocateall-text-t.md)
