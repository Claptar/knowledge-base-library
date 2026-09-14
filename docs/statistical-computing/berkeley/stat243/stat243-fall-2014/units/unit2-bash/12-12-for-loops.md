---
title: 12 For loops
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12 For loops

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_for_ loops in shell scripting are primarily designed for iterating through a set of files or directories. Here’s an example:

for file in $(ls *.txt) do

mv $file ${file/.txt/.R} # this syntax replaces .txt with .R in $file done

You could also have done that with for file in ‘ls *.txt‘

Another use of _for_ loops is automating file downloads: see the demo code file. And, in my experience, _for_ loops are very useful for starting a series of jobs: see the demo code files in the repository: _forloopDownload.sh_ and _forloopJobs.sh_ .

---

[← 11 If/then/else](11-11-if-then-else.md) · [Up: contents](index.md) · [13 How much shell scripting should I learn? →](13-13-how-much-shell-scripting-should-i-learn.md)
