---
title: 5 Regular expressions
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit3-bash.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Regular expressions

**Source:** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit3-bash.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Some of this material is duplicated from Section 3 of the String Processing tutorial.

### **5.1 Overview**

Regular expressions are a domain-specific language for finding patterns and are one of the key functionalities in scripting languages such as Python and R, as well as the UNIX commands _grep_ , _sed_ , and _awk_ .

The basic idea of regular expressions is that they allow us to find matches of strings or patterns in strings, as well as do substitution. Regular expressions are good for tasks such as:

- extracting pieces of text from documents;

- creating variables from information found in text;

- cleaning and transforming text into a uniform format;

- mining text by treating documents as data; and

- scraping the web for data.

That said, if we can avoid using regular expressions, it’s generally a good idea to use more specialized code that understands the structure of particular formats. For example, recall our case of

7

using R functions that treat HTML or XML or JSON in a structured way based on the exact syntax of HTML/XML/JSON. Doing that work using regular expressions would have been more difficult and error-prone.

See Section 3 of the _Using the bash shell_ tutorial for details on regular expression syntax. For other resources, Duncan Temple Lang (UC Davis Statistics) has written a nice tutorial that is part of the string processing tutorial repository or check out Sections 9.9 and 11 of Paul Murrell’s book. Also, here’s a cheatsheet on regular expressions (see the second page) and here is a website where you can interactively test regular expressions on example strings.

### **5.2 Versions of regular expressions**

One thing that can cause headaches is differences in version of regular expression syntax used. As discussed the grep man page, _extended regular expressions_ are standard, with _basic regular expressions_ providing somewhat less functionality and _Perl regular expressions_ additional functionality. In R, as can be seen in help(regex), _stringr_ provides _ICU regular expressions_ , which are based on Perl regular expressions. More details can be found in the regex Wikipedia page.

The tutorial on using bash provides a full documentation of the various _extended regular expressions_ syntax, which we’ll focus on here. This should be sufficient for most usage and should be usable in R and Python, but if you notice something funny going on, it might be due to differences between the regular expressions versions.

### **5.3 General principles for working with regex**

The syntax is very concise, so it’s helpful to break down individual regular expressions into the component parts to understand them. As Murrell notes, since regex are their own language, it’s a good idea to build up a regex in pieces as a way of avoiding errors just as we would with any computer code. _str_detect_ in R’s _stringr_ and _re.findall_ in Python are particularly useful in seeing **what** was matched to help in understanding and learning regular expression syntax and debugging your regex. As with many kinds of coding, I find that debugging my regex is usually what takes most of my time.

### **5.4 Practice problems**

Write a regular expression that matches the following:

1. Only the strings “cat”, “at”, and “t”.

2. The strings “cat”, “caat”, “caaat”, etc.

8

3. “dog”, “Dog”, “dOg”, “doG”, “DOg”, etc. (the word dog in any combination of lower and upper case).

4. Any line with exactly two words separated by any amount of whitespace (spaces or tabs). There may or may not be whitespace at the beginning or end of the line.

5. Any positive number with or without a decimal point.

9

---

[← 4 bash shell challenges](07-4-bash-shell-challenges.md) · [Up: contents](index.md)
