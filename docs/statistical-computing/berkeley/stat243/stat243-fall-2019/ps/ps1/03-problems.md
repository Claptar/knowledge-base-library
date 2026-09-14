---
title: Problems
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps1.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/ps/ps1.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problems

**Source:** [`ps/ps1.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/ps1.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. As preparation for the next few units, please read the sections titled “Memory hierarchy” and “Cache in depth” in the following brief piece that talks about the difference between the CPU cache, main memory (RAM) and disk. You don’t need to follow all the technical details in the “Cache in depth” section - just try to get the big picture of what the cache is and a bit about how it works.

1

2. Please read Unit 3 on good programming/project practices and incorporate what you’ve learned from that reading into your solution for Problem 4. As your response to this question, briefly (a few sentences) note what you did in your code that reflects the material in Sections 1.2 and 1.3 of Unit 3. Please also note anything in Unit 3 that you disagree with, if you have a different stylistic perspective.

3. This problem explores file sizes and their relationship to the file format. The _system()_ function in R calls out to the command line and in this case executes “ls -l”, which (among other output) shows the file size in bytes as the 5th element of information.

   - (a) Based on understanding storage in ASCII plain text versus binary formats and on the fact that numbers are (usually) stored as 8 bytes per number in binary format, explain the results below. If there are any that seem inconsistent with the class notes and our discussion in class, note that.

_## save letters in text format_ chars <- **sample** (letters, 1e6, replace = TRUE) **write.table** (chars, file = 'tmp1.csv', row.names = FALSE, quote = FALSE, col.names = FALSE) **system** ('ls -l tmp1.csv', intern = TRUE)

---

[← Formatting requirements](02-formatting-requirements.md) · [Up: contents](index.md) · [Ps 01 — Part 04 — →](04-ps-01-part-04.md)
