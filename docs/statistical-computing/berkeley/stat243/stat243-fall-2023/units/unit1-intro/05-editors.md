---
title: Editors
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit1-intro.md
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit1-intro.md
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Editors

**Source:** [`units/unit1-intro.md`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit1-intro.md) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.md` (lossless)

For statistical computing, we need a text editor, not a word processor,
because we're going to be operating on code files, plain-text data files,
and markup language documents (e.g., Markdown/Quarto)
for which word processing formatting gets
in the way. **Don't use Microsoft Word or Google Docs to edit code files
or Markdown/Quarto/R Markdown/LaTeX.**

## Some useful editors

-   various editors available on all operating systems:
    -   traditional editors born in UNIX: *emacs*, *vim*
    -   some newer editors: *Atom*, *Sublime Text* (Sublime is
        proprietary/not free)
-   Windows-specific: *WinEdt*
-   Mac-specific: *Aquamacs Emacs*, *TextMate*, *TextEdit*
-   RStudio provides a built-in editor for R code and Quarto/R Markdown files.
    One can actually edit and run Python code chunks quite nicely in
    RStudio.
    (Note: RStudio as a whole is an IDE (integrated development environment.
    The editor is just the editing window where you edit code (and
    Markdown) files.)
-   *VSCode* has a powerful code editor that is customized to work with
    various languages, and it has a Quarto extension.

As you get started it's ok to use a very simple text editor such as
Notepad in Windows, but you should take the time in the next few weeks
to try out more powerful editors such as one of those listed above. It
will be well worth your time over the course of your graduate work and
then your career.

Be careful in Windows - file suffixes are often hidden.

## (Optional) Basic emacs

Emacs is one option as an editor. I use Emacs a fair amount, so I'm
including some tips here, but other editors listed above are just as
good.

-   *Emacs* has special modes for different types of files: Python
    code files, R code
    files, C code files, Latex files -- it's worth your time to figure
    out how to set this up on your machine for the kinds of files you
    often work on
    - If working with Python and R, one can start up a Python or R
    interpreter in an additional Emacs buffer and send code to that
    interpreter and see the results of running the code.
    -   For working with R, ESS (emacs speaks statistics) mode is
        helpful. This is built into Aquamacs Emacs.
-   To open emacs in the terminal window rather than as a new window,
    which is handy when it's too slow (or impossible) to pass (i.e.,
    tunnel) the graphical emacs window through ssh:
    ```
    emacs -nw file.txt
    ```

## (Optional) Emacs keystroke sequence shortcuts.

> **Note**
> Several of these (Ctrl-a, Ctrl-e, Ctrl-k, Ctrl-y) work in the command line, interactive Python and R sessions, and other places as well.

|                      Sequence               |                             Result                     |
|----------------------------------------|-------------------------------------------------------------|
|                     `Ctrl-x,Ctrl-c`            |                            Close the file|
|                     `Ctrl-x,Ctrl-s`             |                            Save the file|
|                     `Ctrl-x,Ctrl-w`             |                        Save with a new name|
|                       `Ctrl-s`               |                               Search|
|                       `ESC`               |            Get out of command buffer at bottom of screen|
|                       `Ctrl-a`               |                       Go to beginning of line|
|                       `Ctrl-e`               |                          Go to end of line|
|                       `Ctrl-k`               |           Delete the rest of the line from cursor forward|
|       `Ctrl-space`*,* then move to end of block   |                 Highlight a block of text|
|                       `Ctrl-w`                 |   Remove the highlighted block, putting it in the kill buffer|
|       `Ctrl-y` *(*after using `Ctrl-k` or `Ctrl-w`*)*   |        Paste from kill buffer ('y' is for 'yank')|

---

[← Connecting to other machines](04-connecting-to-other-machines.md) · [Up: contents](index.md)
