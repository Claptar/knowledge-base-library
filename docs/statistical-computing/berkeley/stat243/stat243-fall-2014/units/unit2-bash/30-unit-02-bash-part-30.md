---
title: Unit 02 — bash Part 30 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 30 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Be careful: _git rm_ removes the file from the local filesystem as well as the repository. If we want to remove a file from the repository but keep it on the local disk, we can do: git rm --cached file

#### **14.4.5 Undoing changes**

If we want to make a change before we do a commit, we can do that as follows.

First, let’s remove a file.

cd /tmp/git-demo echo 'stuff' > test.txt git add test.txt git commit -am'added test file' git rm test.txt git status

---

[← Unit 02 — bash Part 29 —](29-unit-02-bash-part-29.md) · [Up: contents](index.md) · [Unit 02 — bash Part 31 — →](31-unit-02-bash-part-31.md)
