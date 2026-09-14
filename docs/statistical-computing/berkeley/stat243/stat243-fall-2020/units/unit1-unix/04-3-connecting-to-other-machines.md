---
title: 3 Connecting to other machines
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit1-unix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit1-unix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Connecting to other machines

**Source:** [`units/unit1-unix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit1-unix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To connect to a remote machine, you need to use SSH. SSH is available as ssh when you are on the UNIX command line. There are also SSH clients for Windows. For more information on SSH client programs and on using SSH, please see this webpage. Here’s an example of connecting to one of the SCF machines (this assumes you have an SCF account, which you may, and that your user name is paciorek, which it is not).

> ssh paciorek@radagast.berkeley.edu

To copy files between machines, we can use _scp_ , which has similar options to _cp_ . The first command here copies a local file to a remote machine. The second copies from a remote machine to the machine you are on. You can use relative paths to refer to locations on the local machine. On the remote machine all paths need to be absolute or to be relative to your home directory on that machine. Again, this assumes you have an SCF account.

2

   - scp file.txt paciorek@radagast.berkeley.edu:~/research/.

   - scp paciorek@radagast.berkeley.edu:/data/file.txt

- ~/research/renamed.txt

There are also client programs for file transfer; see this webpage.

---

[← 2 Version control](03-2-version-control.md) · [Up: contents](index.md) · [4 Editors →](05-4-editors.md)
