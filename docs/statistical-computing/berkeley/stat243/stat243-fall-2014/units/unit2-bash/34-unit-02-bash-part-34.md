---
title: Unit 02 — bash Part 34 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 34 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now we’ll merge the two together. Git can do this without guidance from us because the differences in the two branches do not conflict with each other.

cd /tmp/git-demo git checkout master git merge experiment git slog ls -l ## Merge made by the 'recursive' strategy. ## experiment.txt | 1 + ## 1 file changed, 1 insertion(+) ## create mode 100644 experiment.txt ## * e0c1389 Merge branch 'experiment' ## |\ ## | * 8d15486 Trying something new ## * | f6fca9b The mainline keeps moving ## |/ ## * 7d29889 added test file ## * da4d319 removed test file ## * 9c9c355 added test file ## * b60d29f I like this new name better ## * c628661 I have made great progress on this critical matter. ## * a1254fd This is our first commit ## total 16 ## -rw-r--r-- 1 paciorek scfstaff 16 Sep 3 08:34 experiment.txt

28

---

[← Unit 02 — bash Part 33 —](33-unit-02-bash-part-33.md) · [Up: contents](index.md) · [Unit 02 — bash Part 35 — →](35-unit-02-bash-part-35.md)
