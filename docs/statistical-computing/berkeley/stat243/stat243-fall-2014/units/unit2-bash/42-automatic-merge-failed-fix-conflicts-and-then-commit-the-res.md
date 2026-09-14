---
title: Automatic merge failed; fix conflicts and then commit the result.
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Automatic merge failed; fix conflicts and then commit the result.

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let’s see what git has put into our file:

32

cd /tmp/git-demo cat experiment.txt ## Some crazy idea ## <<<<<<< HEAD ## More work on the master branch... ## ======= ## This is going to be a problem... ## >>>>>>> trouble

At this point, we go into the file with a text editor, decide which changes to keep, and make a new commit that records our decision. To automate my edits, I use the ‘sed‘ command.

cd /tmp/git-demo sed -i '/^</d' experiment.txt sed -i '/^>/d' experiment.txt sed -i '/^=/d' experiment.txt cat experiment.txt ## Some crazy idea ## More work on the master branch... ## This is going to be a problem...

I’ve now made the edits, in this case I decided that both pieces of text were useful, so I just accepted both additions.

Let’s then make our new commit:

cd /tmp/git-demo

git commit -am"Completed merge of trouble, fixing conflicts along the way" git slog

---

[← CONFLICT (content): Merge conflict in experiment.txt](41-conflict-content-merge-conflict-in-experiment-txt.md) · [Up: contents](index.md) · [Unit 02 — bash Part 43 — →](43-unit-02-bash-part-43.md)
