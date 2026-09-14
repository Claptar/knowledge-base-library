---
title: Unit 02 — bash Part 35 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 35 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **14.6 Using remotes as a single user**

We are now going to introduce the concept of a remote repositor _y_ : a pointer to another copy of the repository that lives on a different location. This can be simply a different path on the filesystem or a server on the internet. Of course we’ve already used a remote repository a little by cloning the class repository from Github.

For this discussion, we’ll be using remotes hosted on the Github.com service, but you can equally use other services like BitBucket (http://bitbucket.org) or Gitorious (http://gitorious.org). The SCF provides hosting of git repositories as well.

cd /tmp/git-demo # Let's see if we have any remote repositories here git remote -v

Since the git remote -v call didn’t produce any results, it means we have no remote repositories configured. We will now proceed to do so. We need a Github account. Login to GitHub, and go to the new repository page (https://github.com/new). For our demo purposes, we’ll make a repository called _test_ . Do **not** check the box that says ‘Initialize this repository with a README‘, since we already have an existing repository on our local machine. That option is useful when you’re starting first at Github and don’t have a repo made already on a local computer.

We can now follow the instructions from the next page:

cd /tmp/git-demo

git remote add origin git@github.com:berkeley-stat243/test.git git push -u origin master git remote -v

---

[← Unit 02 — bash Part 34 —](34-unit-02-bash-part-34.md) · [Up: contents](index.md) · [Unit 02 — bash Part 36 — →](36-unit-02-bash-part-36.md)
