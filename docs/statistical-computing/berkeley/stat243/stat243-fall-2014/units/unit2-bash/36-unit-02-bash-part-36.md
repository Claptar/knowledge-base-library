---
title: Unit 02 — bash Part 36 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 36 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can now see the repository publicly.

Let’s see how this can be useful for backup and syncing work between two different computers.

29

cd /tmp # Here I clone my 'test' repo but with a different name, test2, to # in class we'll actually do this on a separate computer git clone git@github.com:berkeley-stat243/test.git test2 cd test2 ls -l git remote -v ## /tmp/test2 ## total 16 ## -rw-r--r-- 1 paciorek scfstaff 152 Aug 31 15:17 experiment.txt ## -rw-r--r-- 1 paciorek scfstaff 47 Aug 28 09:56 file-newname.txt ## -rw-r--r-- 1 paciorek scfstaff 46 Aug 28 09:56 progress.txt ## -rw-r--r-- 1 paciorek scfstaff 6 Aug 28 09:56 test.txt ## origin git@github.com:paciorek/test.git (fetch) ## origin git@github.com:paciorek/test.git (push)

Let’s now make some changes in one computer.

cd /tmp/test2 # working on computer #2 echo "More new content on my experiment" >> experiment.txt git commit -am"More work, on machine #2"

---

[← Unit 02 — bash Part 35 —](35-unit-02-bash-part-35.md) · [Up: contents](index.md) · [Unit 02 — bash Part 37 — →](37-unit-02-bash-part-37.md)
