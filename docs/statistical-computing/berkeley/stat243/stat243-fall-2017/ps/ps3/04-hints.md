---
title: HINTS
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/ps/ps3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# HINTS

**Source:** [`ps/ps3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/ps/ps3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that for part (c), I relied in part on indentation to indicate the beginnings and continuations of spoken chunks. The fourth play (The Comedy of Errors) has different indentation than the others, so in my solution I excluded it. You are allowed to exclude it or alternatively to exclude a small number of other plays that make your processing particularly difficult.

In my processing, I did a bit of preprocessing in UNIX (including a lot of exploratory grepping just to get a sense for formatting) and also did some preprocessing on a single character string containing the whole file in R. This allowed me to clean up some of the inconsistent formatting (e.g., “ACT 1” vs. “Act I.”). It also allowed me to insert some special symbols of my own that later allowed me to split the chunks of spoken text more easily. (In particular I inserted a special character just before the name of each speaker of a chunk.)

For one time steps such as stripping off the lines that don’t contain plays, you are allowed to hard-code in appropriate constants, such as what lines to extract.

I haven’t had time to investigate this in full but it appears the the regex “.*” does NOT catch newlines (\n) when used with _stringr_ functions. I had to work around this by making use of the :space: character class. Extra credit for anyone who tracks down why this is the case for stringr functions and if there is a solution.

3. This problem asks you to design an object-oriented programming (OOP) approach to the Shakespeare analysis of problem 2. You don’t need to code anything up, but rather to decide what the fields and methods would be for a class that represents a Shakespeare play. You can think of this in the context of S4 or reference classes, or in the context of classes in an object-oriented language like Python or C++.

3

- (a) What are the fields (i.e., member data, slots, etc.) for the class? Describe the kind of variable of each field (e.g., it might be a named numeric vector, or an unnamed list). You might decide to have a field contain an object of yet another class that you should describe.

- (b) What are the methods for the class? Some of the methods should relate to processing the text of the plays to produce the fields and other methods should relate to providing information to a user who wants to know something about a play or see the text of the play. Indicate very briefly what the method does, and any input arguments to each method, fields that are created or modified by the method, and any output that is produced.

4

---

[← Translation](03-translation.md) · [Up: contents](index.md)
