---
title: 5 Editors
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit1-unix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Editors

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit1-unix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For statistical computing, we need an editor, not a word processor, because we’re going to be operating on files of code and data files, for which word processing formatting gets in the way.

### **5.1 Some useful editors**

- traditional UNIX: _emacs_ , _vim_

- Windows: _WinEdt_

- Mac: _Aquamacs Emacs, TextMate, TextEdit_

- Be careful in Windows - file suffixes are often hidden

- RStudio provides a built-in editor for R code files

### **5.2 Basic emacs**

- _emacs_ has special modes for different types of files: R code files, C code files, Latex files – it’s worth your time to figure out how to set this up on your machine for the kinds of files you often work on

      - For working with R, ESS (emacs speaks statistics) mode is helpful. This is built into Aquamacs emacs. Alternatively, the Windows and Mac versions of R, as well as RStudio (available for all platforms) provide a GUI with a built-in editor.

- To open emacs in the terminal window rather than as a new window, which is handy when it’s too slow (or impossible) to tunnel the graphical emacs window through ssh:

   - emacs -nw file.txt

5

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


6

---

[← 4 A variety of UNIX tools/capabilities](05-4-a-variety-of-unix-tools-capabilities.md) · [Up: contents](index.md)
