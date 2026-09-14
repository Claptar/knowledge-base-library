---
title: 1 Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/howtos/remoteConnect.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/howtos/remoteConnect.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Introduction

**Source:** [`howtos/remoteConnect.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/howtos/remoteConnect.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In order to access the SCF from a remote (non-SCF) computer, you must have a program which uses the secure shell (SSH) protocol to communicate with other computers. An SSH program alone will not allow you to run programs which open windows to display images or provide a nicer user interface, for example graphics windows from R, or the SAS display manager. For these purposes, you need an X Windows server (sometimes known as X11) either running natively on your computer, or via an X Windows emulator.

Depending on your operating system, one or both of these programs may already be installed on your computer. The next section will explain how to obtain the necessary programs if they are not already available, followed by an explanation of the commands necessary to connect to the SCF and run the programs you need. Finally, information on transfering files from the SCF to your local computer is presented.

If you don't have a broadband connection, you may find that the response when using X Windows remotely may be too slow to be useful; even with a broadband connection, some programs may seem nonresponsive at times. With patience, you should be able work remotely with few problems.

---

[Up: contents](index.md) · [2 Usernames and Hostnames →](02-2-usernames-and-hostnames.md)
