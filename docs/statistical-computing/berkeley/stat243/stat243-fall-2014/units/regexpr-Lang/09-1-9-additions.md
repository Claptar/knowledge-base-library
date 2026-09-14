---
title: 1.9 Additions
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/regexpr-Lang.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.9 Additions

**Source:** [`units/regexpr-Lang.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We should add some material on useful and reasonably common extensions to the basic regular expression language and which are supported in R (and other languages) via the perl = TRUE option to use the PCRE (Perl Compatible Regular Expression library). Of note are the

- non-greedy (or lazy) matching using the ? qualifer after a quantifier, e.g.

regexpr("ˆa+?", "aaab", perl = TRUE)

See p140 of Friedl.

- Look-arounds

str = "(-0.791,-0.263].(-38,-1.24].(0.96,2.43]" strsplit(str, "\\.(?![0-9])", perl = TRUE)

- Avoiding capturing a group (?:pattern) and explicitly naming captured matches.

- Unicode (i.e. adding unicode to patterns)

- Working with different locales and languages.

15

---

[← 1.8 Resources](08-1-8-resources.md) · [Up: contents](index.md)
