---
title: 2 Using the bash shell
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Using the bash shell

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Please see the tutorial on using the bash shell. For our purposes in this Unit, you should work through all of the material EXCEPT as follows:

- You can skip Section 1.4.1.

- You can skip regular expressions (Section 3), but do look at Sections 3.6.1 and 3.6.2

1

- You can skip _screen_ (Section 4.3.4)

- Feel free to skim over Section 4 for now; I’ll ask you to read it more carefully later.

When we talk about string processing and regular expressions in R in Unit 4, we’ll come back to the material on regular expressions.

When looking at Sections 3.6.1 and 3.6.2, note that you can use _grep_ to look for and _sed_ to replace simple strings in files without needing to know how to specify patterns based on regular expressions. So try to see how to do that without getting bogged down in the examples in those sections that use the complicated regular expression syntax. For example:

grep "," file.txt _# look for lines with commas in file.txt_ sed -i ’s/,/;/g’ file.txt _# replace commas with semicolons in file.txt_

---

[← 1 Shell basics](02-1-shell-basics.md) · [Up: contents](index.md) · [3 bash shell examples →](04-3-bash-shell-examples.md)
