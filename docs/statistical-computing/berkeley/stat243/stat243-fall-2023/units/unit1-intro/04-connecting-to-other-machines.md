---
title: Connecting to other machines
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit1-intro.md
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit1-intro.md
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Connecting to other machines

**Source:** [`units/unit1-intro.md`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit1-intro.md) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.md` (lossless)

To connect to a remote machine, you generally need to use SSH. SSH is available as
`ssh` when you are on the UNIX command line. There are also SSH clients
for Windows. The SCF has [more information on SSH client programs and on using
SSH](http://statistics.berkeley.edu/computing/ssh). Here's an
example of connecting to one of the SCF machines (this assumes you have
an SCF account, which you may, and that your user name is paciorek,
which it is not).

```
ssh paciorek@radagast.berkeley.edu
```

To copy files between machines, we can use *scp*, which has similar
options to *cp*. Here's how we can copy a local file to a remote
machine.

```
scp file.txt paciorek@radagast.berkeley.edu:~/research/.
```

And here's how we can copy from a remote machine to the machine you are
on.

```
scp paciorek@radagast.berkeley.edu:/data/file.txt \
  ~/research/renamed.txt
```

You can use relative paths to refer to locations on the local
machine. On the remote machine all paths need to be absolute or to be
relative to your home directory on that machine.

There are also client programs for file transfer; see [this
webpage](http://statistics.berkeley.edu/computing/copying-files).

---

[← Parts of a computer](03-parts-of-a-computer.md) · [Up: contents](index.md) · [Editors →](05-editors.md)
