---
title: Unit 02 — bash Part 32 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 32 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Now suppose I realize I don’t want to remove _test.txt_ .

cd /tmp/git-demo git reset -- test.txt # restore file in index (unstage) git checkout -- test.txt # get a copy of the file back ls -l test* git status ## Unstaged changes after reset: ## D test.txt ## -rw-r--r-- 1 paciorek scfstaff 6 Sep 3 08:34 test.txt ## # On branch master ## nothing to commit (working directory clean)

Note that if you want to unstage an addition before you’ve committed it, you can do git reset -- <file>. If you want to remove a file from the repository but not the filesystem after you’ve committed the addition of the file, you can do git rm --cached and then a commit.

If you have a bunch of files that have been removed or changed (but not committed) and you want to reset for all of them, you can do: git reset --hard HEAD, which should remove working directory changes and changes changed through git, e.g. _git add_ and _git rm_ changes.

Understanding the difference between the working directory, the index, and HEAD can be confusing and something I’m still wrapping my head around. Fig. 3 helps.

The _working directory_ or _working tree_ is the state of your local directory on the filesystem. The staging area (or _index_ ) reflects your _git add_ , _git rm_ , etc. changes that have been staged but not committed. The repository reflects your commits. HEAD is the last commit on the current branch.

24


Figure 3: Working tree, staging area, and repository. Credit: ProGit book, by Scott Chacon, CC License.

In our _git reset_ and _git checkout_ operations above, we had to use _git reset_ to restore the file in the index from HEAD (from the commit). We then had to use _git checkout_ to check the file back into the working directory (i.e, have the index and the working directory match).

### **14.5 Branches**

What is a branch? It’s a label for the ’current’ commit in a sequence of ongoing commits.

There can be multiple branches alive at any point in time; the working directory is the state of a special pointer called HEAD.

Let’s now illustrate all of this with a concrete example. Let’s get our bearings first:

cd /tmp/git-demo git status ls -l ## # On branch master ## nothing to commit (working directory clean) ## total 8 ## -rw-r--r-- 1 paciorek scfstaff 47 Sep 3 08:34 file-newname.txt ## -rw-r--r-- 1 paciorek scfstaff 6 Sep 3 08:34 test.txt

25

We are now going to try two different routes of development: on the _master_ branch we will add one file and on the _experiment_ branch, which we will create, we will add a different one. We will then merge the experimental branch into _master_ .

cd /tmp/git-demo git branch experiment # creating new branch git checkout experiment # switch to it echo "Some crazy idea" > experiment.txt git add experiment.txt git commit -am"Trying something new" ls -l git slog ## [experiment 8d15486] Trying something new ## Committer: Christopher Paciorek <paciorek@scf.Berkeley.EDU> ## Your name and email address were configured automatically based ## on your username and hostname. Please check that they are accurate. ## You can suppress this message by setting them explicitly: ## ## git config --global user.name "Your Name" ## git config --global user.email you@example.com ## ## After doing this, you may fix the identity used for this commit with: ## ## git commit --amend --reset-author ## ## 1 file changed, 1 insertion(+) ## create mode 100644 experiment.txt ## total 12 ## -rw-r--r-- 1 paciorek scfstaff 16 Sep 3 08:34 experiment.txt ## -rw-r--r-- 1 paciorek scfstaff 47 Sep 3 08:34 file-newname.txt ## -rw-r--r-- 1 paciorek scfstaff 6 Sep 3 08:34 test.txt ## * 8d15486 Trying something new ## * 7d29889 added test file ## * da4d319 removed test file ## * 9c9c355 added test file ## * b60d29f I like this new name better

26

---

[← Unit 02 — bash Part 31 —](31-unit-02-bash-part-31.md) · [Up: contents](index.md) · [Unit 02 — bash Part 33 — →](33-unit-02-bash-part-33.md)
