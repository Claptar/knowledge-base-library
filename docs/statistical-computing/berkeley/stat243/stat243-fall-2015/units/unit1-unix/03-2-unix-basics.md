---
title: 2 UNIX basics
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit1-unix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 UNIX basics

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit1-unix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Please see the material in our tutorial on the basics of UNIX to get up to speed on working in a UNIX-style command line environment. The tutorial is presented in the context of BCE, so you should be able to follow and replicate what is done exactly. There are some questions at the end of the tutorial you can use to self-test your understanding.

1

To connect to a remote machine, you need to use SSH. SSH is available as ssh from the BCE command line as well as the Mac Terminal. There are also SSH clients for Windows. For more information on SSH client programs and on using SSH, please see this webpage. Here’s an example of connecting to one of the SCF machines from BCE (this assumes you have an SCF account, which you may, and that your user name is paciorek, which it is not).

> ssh paciorek@radagast.berkeley.edu

To copy files between machines, we can use _scp_ , which has similar options to _cp_ . The first command here copies a local file to a remote machine. The second copies from a remote machine to the machine you are on. You can use relative paths to refer to locations on the local machine. On the remote machine all paths need to be absolute or to be relative to your home directory on that machine. Again, this assumes you have an SCF account.

> scp file.txt paciorek@radagast.berkeley.edu:~/research/.

- scp paciorek@radagast.berkeley.edu:/data/file.txt

~/research/renamed.txt

There are also client programs for file transfer; see this webpage.

---

[← 1 BCE](02-1-bce.md) · [Up: contents](index.md) · [3 Version control →](04-3-version-control.md)
