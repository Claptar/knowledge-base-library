---
title: 4 A variety of UNIX tools/capabilities
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit1-unix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 A variety of UNIX tools/capabilities

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit1-unix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Many UNIX programs are small programs (tools, utilities) that can be combined to do complicated things.

1. For help on a UNIX program, including command-line utilities like _ls_ , _cp_ , etc.

   - man cp

2. What’s the path of an executable (and implicitly, does it exist on the system)?

   - which R

3. Tools for remotely mounting the filesystem of a remote UNIX machine/filesystem as a ’local’ directory on your machine - see this SCF FAQ

   - (a) Cloud storage: Dropbox and other services will mirror directories on multiple machines and on their servers.

4. To do something at the UNIX command line from within R, use the system() function in R:

   - system(“ls -al”)

5. Files that provide info about a UNIX machine:

   - _/proc/meminfo_ [in particular the _MemTotal_ value]

   - _/proc/cpuinfo_ [or use nproc --all]

   - _/etc/issue_

   - Example: to find out how many processors a machine has:

      - grep processor /proc/cpuinfo

4

6. There are (free) tools in UNIX to convert files between lots of formats (pdf, ps, html, latex, jpg). This is particularly handy when preparing figures for a publication. My computing tips page lists a number of these. On a related note _pandoc_ is a program for converting between markup formats, including Markdown, HTML, Latex and MS Word.

---

[← 3 Files and directories](04-3-files-and-directories.md) · [Up: contents](index.md) · [5 Editors →](06-5-editors.md)
