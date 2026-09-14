---
title: Unit 02 — bash Part 16 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 02 — bash Part 16 —

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the commit above, we used the ‘-m‘ flag to specify a message at the command line. If we don’t do that, git will open the editor we specified in our configuration above and require that we enter a message. By default, git refuses to record changes that don’t have a message to go along with them (though you can obviously ’cheat’ by using an empty or meaningless string).

We can use git log to see what has been committed to the repository so far:

cd /tmp/git-demo git log ## commit a1254fdd518f5728bb7028011ce82aac559277a0 ## Author: Christopher Paciorek <paciorek@scf.Berkeley.EDU> ## Date: Wed Sep 3 08:34:40 2014 -0700 ## ## This is our first commit

Let’s do a little bit more work... Again, in practice you’ll be editing the files by hand, here we do it via shell commands for the sake of automation (and therefore the reproducibility of this tutorial!)

cd /tmp/git-demo echo "And now some more text..." >> file1.txt

And now we can ask git what is different:

cd /tmp/git-demo git diff ## diff --git a/file1.txt b/file1.txt ## index ce645c7..4baa979 100644 ## --- a/file1.txt ## +++ b/file1.txt

18

---

[← Unit 02 — bash Part 15 —](15-unit-02-bash-part-15.md) · [Up: contents](index.md) · [@@ -1 +1,2 @@ ## My first bit of text ## +And now some more text... →](17--1-1-2-my-first-bit-of-text-and-now-some-more-text.md)
