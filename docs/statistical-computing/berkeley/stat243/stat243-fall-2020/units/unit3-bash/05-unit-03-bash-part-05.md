---
title: Unit 03 — bash Part 05 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit3-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit3-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — bash Part 05 —

**Source:** [`units/unit3-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit3-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Notice that man tail indicates it can take input from a FILE or from _stdin_ . Here it uses _stdin_ , so it is gives the last five lines of the output of _ls_ , not the last five lines of the files indicated in that output.

man grep also indicates it can take input from a FILE or from _stdin_ . However, we want grep to operate on the content of the files indicated in stdin. So we use _xargs_ to convert _stdin_ to be recognized as arguments, which then are the FILE inputs to _grep_ .

**Our fourth mission** : write a function that will move the most recent _n_ files in your Downloads directory to another directory.

In general, we want to start with a specific case, and then generalize to create the function.

ls -rt ~/Downloads | tail -n 1

---

[← 3 bash shell examples](04-3-bash-shell-examples.md) · [Up: contents](index.md) · [Unit 03 — bash Part 06 — →](06-unit-03-bash-part-06.md)
