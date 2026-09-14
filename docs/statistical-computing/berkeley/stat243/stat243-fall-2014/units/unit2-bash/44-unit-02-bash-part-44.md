---
title: Unit 02 — bash Part 44 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 44 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note: While it’s a good idea to understand the basics of fixing merge conflicts by hand, in some cases you may find the use of an automated tool useful. Git supports multiple merge tools: a merge tool is a piece of software that conforms to a basic interface and knows how to merge two files into a new one. Since these are typically graphical tools, there are various to choose from for the different operating systems, and as long as they obey a basic command structure, git can work with any of them.

### **14.8 Collaborating on github with a small team**

Single remote with shared access: we are going to set up a shared collaboration with one partner (the person sitting next to you). This will show the basic workflow of collaborating on a project with a small team where everyone has write privileges to the same repository.

We will have two people, let’s call them Alice and Bob, sharing a repository. Alice will be the owner of the repo and she will give Bob write privileges.

34

We begin with a simple synchronization example, much like we just did above, but now between two people instead of one person. Otherwise it’s the same:

- Bob clones Alice’s repository.

- Bob makes changes to a file and commits them locally.

- Bob pushes his changes to github.

- Alice pulls Bob’s changes into her own repository.

Next, we will have both parties make non-conflicting changes each, and commit them locally. Then both try to push their changes:

- Alice adds a new file, _alice.txt_ to the repo and commits.

- Bob adds _bob.txt_ and commits.

- Alice pushes to github.

- Bob tries to push to github.

What happens here?

The problem is that Bob’s changes create a commit that conflicts with Alice’s, so git refuses to apply them. It forces Bob to first do the merge on his machine, so that if there is a conflict in the merge, Bob deals with the conflict manually (git could try to do the merge on the server, but in that case if there’s a conflict, the server repo would be left in a conflicted state without a human to fix things up). The solution is for Bob to first pull the changes (pull in git is really fetch+merge), and then push again.

### **14.9 More Git resources**

- Git for Scientists: A Tutorial: http://nyuccl.org/pages/GitTutorial/

- Gitwash: workflow for scientific Python projects: http://matthew-brett.github.io/pydagogue/gitwash_build.html

- Git branching demo: http://pcottle.github.io/learnGitBranching/

35

---

[← Unit 02 — bash Part 43 —](43-unit-02-bash-part-43.md) · [Up: contents](index.md)
