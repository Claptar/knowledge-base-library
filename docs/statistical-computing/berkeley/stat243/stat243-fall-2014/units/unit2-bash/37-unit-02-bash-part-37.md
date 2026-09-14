---
title: Unit 02 — bash Part 37 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 37 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now we put this new work up on the github server so it’s available from the internet

30

cd /tmp/test2 # working on computer #2 git push

Now let’s fetch that work from machine #1:

cd /tmp/git-demo git pull cat experiment.txt ## Already up-to-date. ## Some crazy idea

### **14.7 Conflict management**

While git is very good at merging, if two different users or two different branches modify the same file in the same location, it simply can’t decide which change should prevail. At that point, human intervention is necessary to make the decision. Git will help you by marking the location in the file that has a problem, but it’s up to you to resolve the conflict. Let’s see how that works by intentionally creating a conflict.

We start by creating a branch and making a change to our experiment file:

cd /tmp/git-demo git branch trouble git checkout trouble echo "This is going to be a problem..." >> experiment.txt git commit -am"Changes in the trouble branch"

---

[← Unit 02 — bash Part 36 —](36-unit-02-bash-part-36.md) · [Up: contents](index.md) · [Unit 02 — bash Part 38 — →](38-unit-02-bash-part-38.md)
