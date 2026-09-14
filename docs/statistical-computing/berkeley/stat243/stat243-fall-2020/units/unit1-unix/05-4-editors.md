---
title: 4 Editors
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit1-unix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Editors

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit1-unix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For statistical computing, we need a text editor, not a word processor, because we’re going to be operating on files of code and data files, for which word processing formatting gets in the way. Don’t use Microsoft Word or Google Docs to edit code files or Markdown/R Markdown/L<sup>A</sup> TEX.

### **4.1 Some useful editors**

- various editors available on all operating systems:

   - traditional editors born in UNIX: _emacs_ , _vim_

   - some newer editors: _Atom_ , _Sublime Text_

- Windows-specific: _WinEdt_

- Mac-specific: _Aquamacs Emacs, TextMate, TextEdit_

- Be careful in Windows - file suffixes are often hidden

- RStudio provides a built-in editor for R code files

As you get started it’s ok to use a very simple text editor such as Notepad in Windows, but you should take the time in the next few weeks to try out more powerful editors such as one of those listed above. It will be well worth your time over the course of your graduate work and then your career.

### **4.2 Basic emacs**

Emacs is one option as an editor. I use emacs a fair amount, so I’m including some tips here, but other editors listed above are just as good.

- _emacs_ has special modes for different types of files: R code files, C code files, Latex files – it’s worth your time to figure out how to set this up on your machine for the kinds of files you often work on

3

      - For working with R, ESS (emacs speaks statistics) mode is helpful. This is built into Aquamacs emacs. Alternatively, the Windows and Mac versions of R, as well as RStudio (available for all platforms) provide a GUI with a built-in editor.

- To open emacs in the terminal window rather than as a new window, which is handy when it’s too slow (or impossible) to pass (i.e., tunnel) the graphical emacs window through ssh:

   - emacs -nw file.txt

Table 1: Helpful _emacs_ control sequences

|Sequence|Result|
|---|---|
|**C-x,C-c**|Close the file|
|**C-x,C-s**|Save the file|
|**C-x,C-w**|Save with a new name|
|**C-s**|Search|
|**ESC**|Get out of command buffer at bottom of screen|
|**C-a**|Go to beginningof line|
|**C-e**|Go to end of line|
|**C-k**|Delete the rest of the line from cursor forward|
|**C-space**_,_then move to end of block|Highlight a block of text|
|**C-w**|Remove the highlighted block, puttingit in the kill buffer|
|**C-y** _(_after using**C-k**or**C-w**_)_|Paste from kill buffer(’y’ is for ’yank’)|


4

---

[← 3 Connecting to other machines](04-3-connecting-to-other-machines.md) · [Up: contents](index.md)
