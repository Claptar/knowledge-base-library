---
title: 3 Command history
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit2-bash.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Command history

**Source:** [`units/unit2-bash.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit2-bash.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

By using the up and down arrows, you can scroll through commands that you have entered previously. So if you want to rerun the same command, or fix a typo in a command you entered, just scroll up to it and hit enter to run it or edit the line and then hit enter.

Note that you can use emacs-like control sequences ( **C-a** , **C-e** , **C-k** ) to navigate and delete characters, just as you can at the prompt in the shell usually.

You can also rerun previous commands as follows:

> !-n # runs the _n_ th previous command

> !gi # runs the last command that started with ’gi’

If you’re not sure what command you’re going to recall, you can append **:p** at the end of the text you type to do the recall, and the result will be printed, but not executed. For example: > !gi:p

You can then use the up arrow key to bring back that statement for editing or execution.

You can also search for commands by doing **C-r** and typing a string of characters to search for in the search history. You can hit return to submit, **C-c** to get out, or **ESC** to put the result on the regular command line for editing.

---

[← 2 Tab completion](02-2-tab-completion.md) · [Up: contents](index.md) · [4 Wildcards in filenames →](04-4-wildcards-in-filenames.md)
