---
title: 1.6 Summary
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/regexpr-Lang.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.6 Summary

**Source:** [`units/regexpr-Lang.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/regexpr-Lang.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this chapter we introduced six basic concepts of regular expressions.

1. **Literal String** – Basic matching occurs one character at a time from left to right. Look for the first character in the pattern, when it is found in the string, see if the next character in the sting matches the second character in the pattern, and so on.

2. **Character Sets** – These are collections of equivalent characters, where a match could be any one of the characters specified in the character set. A character set is the collection of of characters between [ and ]. Some of the most common collections are named, such as [[:alpha:]] for the letters of the alphabet.

14

3. **Repetition** – A match may be repeated a specific number of times, e.g. {m} for m times. Or a range of times, such as {m,} m or more times and {m,n} m through n times. In addition the meta characters * ?+ denote zero or more, one or more, and zero or one, respectively. These quantifiers modify the character or group of characters that immediately precedes it.

4. **Grouping** – Parentheses can be used to form sub-patterns. Groups are useful for alternation, repetition, and referencing.

5. **Alternation** – Alternate patterns may be provided via the _|_ symbol. For example this|that matches either this or that. Parentheses limit the alternation, e.g. th(is|at) has the same effect as the previous alternation.

6. **References** – A sub-pattern may be referred to later in the same pattern or in a substitution pattern. The reference is based on the position of the sub-pattern. The first or leftmost sub-pattern is referred to as \\1, the second as \\2, and so on.

---

[← 1.5 Greedy Matching](05-1-5-greedy-matching.md) · [Up: contents](index.md) · [1.7 Exercises →](07-1-7-exercises.md)
