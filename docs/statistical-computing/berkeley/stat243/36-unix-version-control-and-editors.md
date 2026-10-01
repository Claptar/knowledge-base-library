---
title: "36. Unix, Version Control, and Editors"
course: "Berkeley Stat 243"
chapter: 36
source: "https://github.com/berkeley-stat243"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 243](https://github.com/berkeley-stat243), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 36. Unix, Version Control, and Editors

## What this covers

This chapter sets up the basic toolchain the rest of the course assumes: a command line on a
UNIX-like operating system, version control with Git, a way to connect to a remote machine, and a
text editor for working with code and plain-text documents. It assumes only ordinary computer
literacy. It does **not** teach UNIX commands or shell syntax in detail — the lecture material
itself defers that entirely to a separate hands-on tutorial, expected to be worked through before
class, and that tutorial's content is not reproduced here because it was not part of what was
supplied.

## The command line, and why UNIX

"UNIX" here means any UNIX-like operating system, including Linux and macOS. Most modern scientific
computing happens on UNIX-based machines, and often that means working on a machine you are not
sitting in front of: you log in remotely to a UNIX-based server. There are several ways to get a
UNIX-style command-line environment on your own machine, covered separately in a companion how-to
rather than in the lecture itself. Shell scripting proper — writing and combining commands into
scripts — is picked up later, as its own unit.

## Version control with Git

*Version control* is the practice of keeping track of changes to your materials on a computer —
most often code files, but any file can be tracked. It works particularly well for text files
because version control systems track the differences between two versions of a file on a
line-by-line basis, rather than treating every save as an unrelated new copy. The course treats
version control as a central practice of modern scientific computing, not an optional extra.

Git is the tool used throughout the course. Git organizes the files of a project into a
*repository*. Two commands cover the basic interaction with a repository hosted elsewhere, for
example on GitHub:

To clone — that is, copy — a repository to your own machine:

```bash
git clone https://github.com/berkeley-stat243/fall-2026
```

To bring a local copy up to date with changes made to the remote copy:

```bash
cd /to/any/directory/within/the/local/repository  ## e.g., cd fall-2026
git pull
```

Graphical front-ends to Git exist too (GitHub Desktop, for instance), for anyone who would rather
not do this from the command line. Git is used in the course for submitting problem sets, and it is
worth practicing with it on your own problem-set work rather than meeting it for the first time
under deadline.

## Parts of a computer, and where time goes

Programming effectively calls for only a basic picture of the hardware underneath, not a deep grasp
of computer architecture. The relevant components are:

- the **CPU**, which does the arithmetic, with a small amount of *cache* — fast memory sitting
  close to the CPU;
- **main memory (RAM)**;
- the **bus**, which moves data between components;
- **disk**, for persistent storage.

The reason to know this list is diagnostic. Depending on what a piece of code is doing, the slow
step in a computation can be any one of three quite different things:

- the arithmetic itself, running on the CPU;
- moving data back and forth between RAM and the CPU; or
- reading or writing data to and from disk (I/O).

These have very different costs, and which one is the actual bottleneck in a given piece of code
changes what is worth optimizing.

## Connecting to other machines

Connecting to a remote machine is normally done with SSH, available as the `ssh` command on the
UNIX command line (Windows has SSH clients too). For example, to log in to a remote server:

```bash
ssh paciorek@radagast.berkeley.edu
```

To move files between machines, `scp` behaves like `cp` but takes a machine name as part of the
path. Copying a local file to a remote machine:

```bash
scp file.txt paciorek@radagast.berkeley.edu:~/research/.
```

and copying from the remote machine back to the local one:

```bash
scp paciorek@radagast.berkeley.edu:/data/file.txt \
  ~/research/renamed.txt
```

Paths given for the local side of an `scp` command may be relative to your current directory, but
paths on the remote side must be absolute, or relative to your home directory on that machine.
(There are graphical file-transfer clients as well, and a way to configure SSH so that it does not
ask for a password every time — both are pointed at from the lecture material rather than covered
in it.)

### Knowing your context

Once you are routinely moving between your own machine, remote servers, and different Git branches
and computing environments, it is easy to lose track of exactly what you are operating on. The
recommended habit is to keep five questions answered at all times, in the shell or when running
code:

- What machine am I on?
- What user am I?
- What is the current working directory?
- What Git branch am I on, if the working directory is inside a Git repository?
- What Conda environment am I in, if relevant?

Losing track of any one of these is a common source of bugs that look mysterious: running the right
command in the wrong directory, or against the wrong environment, produces output that can look
just like a real failure until you check.

## Editors

Scientific computing calls for a *text editor*, not a word processor. Code files, plain-text data
files, and markup documents such as Markdown, Quarto, LaTeX, and R Markdown are all plain text, and
a word processor's formatting only gets in the way. Microsoft Word and Google Docs should not be
used to edit code, Markdown, Quarto, R Markdown, or LaTeX.

A partial list of options:

- traditional UNIX editors: *emacs*, *vim*;
- other general editors: *Sublime Text* (proprietary);
- Windows-specific: *WinEdt*, *Notepad++*;
- Mac-specific: *Aquamacs Emacs*, *TextMate*, *TextEdit*;
- *VS Code*, a full IDE with language-specific tooling, support for Jupyter notebooks and Quarto
  documents, and built-in AI assistance through GitHub Copilot;
- *RStudio*, an IDE whose built-in editor handles R code and Quarto/R Markdown well, and can also
  run Python code chunks.

It is fine to start with something as simple as Notepad, but it is worth taking the time early on
to try a more capable editor — the investment pays off over the course of graduate work and beyond.
On Windows specifically, file suffixes are often hidden by default, which is worth knowing before
renaming or creating files.

### Emacs basics

Emacs has file-type-specific modes — for Python, R, C, LaTeX, and more — that are worth setting up
for whatever you work in most. For R specifically, ESS ("Emacs Speaks Statistics") mode helps; it
comes built into Aquamacs Emacs. You can also start an interactive Python or R session in a separate
Emacs buffer and send code from a file to that running interpreter, seeing the results as you go.
To open Emacs directly in the terminal rather than as a separate graphical window — useful when a
graphical window cannot be tunneled through SSH:

```bash
emacs -nw file.txt
```

A few key bindings. Several of these — `Ctrl-a`, `Ctrl-e`, `Ctrl-k`, `Ctrl-y` — also work at the
command line and inside interactive Python and R sessions, not only inside Emacs:

| Sequence | Result |
|---|---|
| `Ctrl-x, Ctrl-c` | Close the file |
| `Ctrl-x, Ctrl-s` | Save the file |
| `Ctrl-x, Ctrl-w` | Save with a new name |
| `Ctrl-s` | Search |
| `Esc` | Get out of the command buffer at the bottom of the screen |
| `Ctrl-a` | Go to beginning of line |
| `Ctrl-e` | Go to end of line |
| `Ctrl-k` | Delete the rest of the line from the cursor forward |
| `Ctrl-space`, then move to end of block | Highlight a block of text |
| `Ctrl-w` | Remove the highlighted block into the kill buffer |
| `Ctrl-y` (after `Ctrl-k` or `Ctrl-w`) | Paste from the kill buffer ("y" for "yank") |

### Vim basics

Vim is worth knowing at least minimally for one very practical reason: running `git commit` without
a `-m` flag drops you into vim by default to write the commit message. (This can be reconfigured,
but by default vim is where you land.)

Vim has two modes. *Normal* mode is for navigation and operations — saving, moving, and deleting
lines. *Insert* mode is for typing text. From normal mode, `i` enters insert mode; `Esc` returns to
normal mode from insert mode.

From normal mode: `:w` saves, `:x` saves and exits, `:q` exits. To search the document for a
string, type `/` followed by the string — for example `/python docstring` — and press return;
`Esc` exits the search.

## Sources

- **UNIX command line basics** — berkeley-stat243 fall-2026, `units/unit1-intro.qmd`, section
  "1. UNIX command line basics"
  (`statistical-computing/berkeley/stat243/fall-2026/units/unit1-intro/01-1-unix-command-line-basics.md`).
  The same section is essentially unchanged in the fall-2024 and fall-2025 offerings
  (`.../fall-2024/.../01-1-unix-command-line-basics.md`,
  `.../fall-2025/.../01-1-unix-command-line-basics.md`) and, under different unit numbering, in
  stat243-fall-2021 (`.../stat243-fall-2021/units/unit1-unix/01-unit-1-basics-of-unix.md`).
- **Version control and Parts of a computer** — berkeley-stat243 fall-2026, same source file,
  section "2. Version control"
  (`.../fall-2026/units/unit1-intro/02-2-version-control.md`); unchanged in substance in
  fall-2024 and fall-2025. The "Parts of a computer" material does not appear in the
  stat243-fall-2021 offering.
- **Connecting to other machines, and Knowing your context** — berkeley-stat243 fall-2026,
  section "4. Connecting to other machines"
  (`.../fall-2026/units/unit1-intro/03-4-connecting-to-other-machines.md`). The SSH/`scp` material
  is shared with fall-2024, fall-2025, and stat243-fall-2021; the "Knowing your context" section
  (the five questions) is new to fall-2026 and does not appear in the earlier offerings.
- **Editors** — berkeley-stat243 fall-2026, section "6. (BACKGROUND) Editors"
  (`.../fall-2026/units/unit1-intro/04-6-background-editors.md`), which matches fall-2025's
  "5. Editors" (VS Code with GitHub Copilot, Notepad++). The fall-2024 version of the same section
  is very close but lists Atom instead. The stat243-fall-2021 editors unit
  (`.../stat243-fall-2021/units/unit1-unix/03-4-editors.md`) covers the same ground at lower
  fidelity — it is a model's reconstruction of a PDF with no text layer, flagged by its own header
  as not citable, and was used here only to confirm continuity, not as a source of distinct
  content.
- **Referred to but not supplied**, and so not reproduced in this chapter: the course's own
  UNIX-basics tutorial and Computing Skills Workshop, a Software Carpentry shell tutorial, a
  how-to on accessing a UNIX command line, a Git-basics tutorial, a CMU overview of computer
  architecture, and SCF pages on SSH, SSH keys, and copying files. All are named in the source
  material as pointers rather than included content.

---

[← 35. Course Structure and Policies](35-course-structure-and-policies.md) · [Contents](index.md) · [37. Numerical Linear Algebra →](37-numerical-linear-algebra.md)
