---
title: 5. Regular expressions
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 5. Regular expressions

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Regular expressions ("regex") are a *domain-specific language* for finding and manipulating patterns of characters and are a key tool used in UNIX commands such as `grep`, `sed`, and `awk` as well as
in scripting languages such as Python and R.

For the moment we'll focus on learning regular expression syntax in the context of the shell, but in Unit 5, we'll also use regular expressions within Python using the `re` package.

The basic idea of regular expressions is that they allow us to find
matches of strings or patterns in strings, as well as do substitution.
Regular expressions are good for tasks such as:

 - extracting pieces of text;
 - creating variables from information found in text;
 - cleaning and transforming text into a uniform format; and
 - mining text by treating documents as data.

Please see the [bash shell tutorial](https://berkeley-scf.github.io/tutorial-using-bash/regex) for a description of regular expressions. I'll assign a small set of regex problems due as an [assignment](../../schedule/index.md), and we'll talk through those problems in class to explore the regex syntax.

Other resources include:

  - Here's a [website where you can interactively test regular expressions on example strings](https://regex101.com).
  - Duncan Temple Lang (UC Davis Statistics) has written a [nice tutorial](http://berkeley-scf.github.io/tutorial-string-processing/regexpr-Lang.pdf) covering regular expressions, illustrated in R.
  - Sections 9.9 and 11 of [Paul Murrell's book](http://www.stat.auckland.ac.nz/~paul/ItDT)
  - The back/second page of RStudio's `stringr` cheatsheet has a [cheatsheet on regular expressions](https://raw.githubusercontent.com/rstudio/cheatsheets/main/strings.pdf).

In addition to the regular expression functionality we'll cover, there is a lot more advanced functionality we won't cover, such as callbacks, named groups, recursion, word boundaries, and lookaround assertions.

## Versions of regular expressions

One thing that can cause headaches is differences in version of regular expression syntax used. As discussed in `man grep`, *extended regular expressions* are standard, with *basic regular expressions* providing less functionality and *Perl regular expressions* additional functionality.

The [bash shell tutorial](https://berkeley-scf.github.io/tutorial-using-bash/regex) provides a full documentation of the *extended regular expressions* syntax, which we'll focus on here. This syntax should be sufficient for most usage and should be usable in Python and R, but if you notice something funny going on, it might be due to differences between the regular expressions versions.

  - In bash, `grep -E` (or `egrep`) enables use of the extended regular expressions, while `grep -P` enables Perl-style regular expressions.
  - In Python, the `re` package provides [syntax "similar to" Perl](https://docs.python.org/3/library/re.html).
  - In R, `stringr` provides *ICU regular expressions* (see `help(regex)`), which are based on Perl regular expressions.

More details about Perl regular expressions can be found in the [regex Wikipedia page](https://en.wikipedia.org/wiki/Regular_expression).

## General principles for working with regex

The syntax is very concise, so it's helpful to break down
individual regular expressions into the component parts to understand
them. As Murrell notes, since regex are their own language, it's
a good idea to build up a regex in pieces as a way of avoiding errors
just as we would with any computer code. `re.findall` in Python  and  `str_detect` in R's `stringr`,
as well as regex101.com are particularly
useful in seeing *what* was matched to help in understanding
and learning regular expression syntax and debugging your regex. As with
many kinds of coding, I find that debugging my regex is usually what takes
most of my time.

## Challenge problem

*Challenge*: Let's think about what regex syntax we would need to detect any number, integer- or real-valued. Let's start from a test-driven development perspective of writing out test cases including:

  - various cases we want to detect,
  - various tricky cases that are not numbers and we don't want to detect, and
  - "corner cases" -- tricky (perhaps unexpected) cases that might trip us up.

---

[← 4. bash shell challenges](12-4-bash-shell-challenges.md) · [Up: contents](index.md)
