---
title: 4 Wildcards in filenames
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Wildcards in filenames

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The shell will expand certain special characters to match patterns of file names, before passing those filenames on to a program. Note that the programs themselves don’t know anything about

2

||Table 1: Wildcards|
|---|---|
|Syntax|What it matches|
|_?_|anysingle character|
|_*_|zero or more characters|
|_[c_1_c_2 _. . .]_|anycharacter in the set|
|_[!c_1_c_2 _. . .]_|anythingnot in the set|
|_[c_1 _−c_2_]_|anythingin the range from_c_1 to_c_2|
|_{string1,string2,...}_|anythingin the set of strings|


wildcards; it is the shell that does the expansion, so that programs don’t see the wildcards. Table 1 shows some of the special characters that the shell uses for expansion:

Here are some examples of using wildcards:

- List all files ending with a digit:

   - ls *[0-9]

- Make a copy of _filename_ as _filename.old_

   - cp filename{,.old}

- Remove all files beginning with _a_ or _z_ :

   - rm [az]*

- List all the R code files with a variety of suffixes:

   - ls *.{r,q,R}

The _echo_ command can be used to verify that a wildcard expansion will do what you think it will: > echo cp filename{,.old} # returns cp filename filename.old If you want to suppress the special meaning of a wildcard in a shell command, precede it with a backslash ( **_\_** ). Note that this is a general rule of thumb in many similar situations when a character has a special meaning but you just want to treat it as a character.

---

[← 3 Command history](03-3-command-history.md) · [Up: contents](index.md) · [5 Basic UNIX utilities →](05-5-basic-unix-utilities.md)
