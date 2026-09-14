---
title: Unit 02 — bash Part 33 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 33 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can see the branches, and which branch we are currently in with git branch. We’ll switch to the master and notice that _experiment.txt_ is not in the master branch.

cd /tmp/git-demo git branch git checkout master ls -l # notice the lack of 'experiment.txt' ## * experiment ## master ## total 8 ## -rw-r--r-- 1 paciorek scfstaff 47 Sep 3 08:34 file-newname.txt ## -rw-r--r-- 1 paciorek scfstaff 6 Sep 3 08:34 test.txt

Now, let’s make a different change to the master branch.

cd /tmp/git-demo echo "All the while, more work goes on in master..." >> progress.txt git add progress.txt git commit -am"The mainline keeps moving" git slog ## [master f6fca9b] The mainline keeps moving ## Committer: Christopher Paciorek <paciorek@scf.Berkeley.EDU> ## Your name and email address were configured automatically based ## on your username and hostname. Please check that they are accurate. ## You can suppress this message by setting them explicitly: ## ## git config --global user.name "Your Name" ## git config --global user.email you@example.com ## ## After doing this, you may fix the identity used for this commit with: ## ## git commit --amend --reset-author

27

---

[← Unit 02 — bash Part 32 —](32-unit-02-bash-part-32.md) · [Up: contents](index.md) · [Unit 02 — bash Part 34 — →](34-unit-02-bash-part-34.md)
