---
title: Unit 02 — bash Part 22 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 22 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Sometimes it’s handy to see a very summarized version of the log:

cd /tmp/git-demo git log --oneline --topo-order --graph ## * c628661 I have made great progress on this critical matter. ## * a1254fd This is our first commit

Git supports _aliases_ , new names given to command combinations. Let’s make this handy shortlog an alias, so we only have to type git slog and see this compact log:

cd /tmp/git-demo # We create our alias (this saves it in git's permanent configuration file): git config --global alias.slog "log --oneline --topo-order --graph" # And now we can use it git slog ## * c628661 I have made great progress on this critical matter. ## * a1254fd This is our first commit

#### **14.4.4 Renaming and removing files**

Once a file is added to a repository, we need to use git commands to rename and remove files. In familiar Unix fashion, the _mv_ and _rm_ git commands do precisely this:

cd /tmp/git-demo git mv file1.txt file-newname.txt git status ## # On branch master ## # Changes to be committed: ## # (use "git reset HEAD <file>..." to unstage) ## # ## # renamed: file1.txt -> file-newname.txt ## #

20

Note that these changes must be committed too, to become permanent! In git’s world, until something hasn’t been committed, it isn’t permanently recorded anywhere.

cd /tmp/git-demo git commit -am"I like this new name better" git slog

---

[← Author: Christopher Paciorek](21-author-christopher-paciorek.md) · [Up: contents](index.md) · [Unit 02 — bash Part 23 — →](23-unit-02-bash-part-23.md)
