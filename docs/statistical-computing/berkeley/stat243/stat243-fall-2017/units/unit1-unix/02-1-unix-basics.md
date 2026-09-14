---
title: 1 UNIX basics
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit1-unix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 UNIX basics

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit1-unix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Please see the material in our tutorial on the basics of UNIX to get up to speed on working in a UNIX-style command line environment. The tutorial is presented in the context of the BCE virtual machine, but you should be able to replicate what is done if you use other ways to access a command line environment.

To connect to a remote machine, you need to use SSH. SSH is available as ssh when you are on the UNIX command line. There are also SSH clients for Windows. For more information on SSH client programs and on using SSH, please see this webpage. Here’s an example of connecting to one of the SCF machines (this assumes you have an SCF account, which you may, and that your user name is paciorek, which it is not).

> ssh paciorek@radagast.berkeley.edu

To copy files between machines, we can use _scp_ , which has similar options to _cp_ . The first command here copies a local file to a remote machine. The second copies from a remote machine to the machine you are on. You can use relative paths to refer to locations on the local machine. On the remote machine all paths need to be absolute or to be relative to your home directory on that machine. Again, this assumes you have an SCF account.

1

   - scp file.txt paciorek@radagast.berkeley.edu:~/research/.

   - scp paciorek@radagast.berkeley.edu:/data/file.txt

- ~/research/renamed.txt

There are also client programs for file transfer; see this webpage.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Version control →](03-2-version-control.md)
