---
title: 4. Connecting to other machines
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit1-intro.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit1-intro.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Connecting to other machines

**Source:** [`units/unit1-intro.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit1-intro.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

To connect to a remote machine, you generally need to use SSH. SSH is available as
`ssh` when you are on the UNIX command line. There are also SSH clients
for Windows. The SCF has [more information on SSH client programs and on using
SSH](http://statistics.berkeley.edu/computing/ssh), including [connecting without
entering your password](https://statistics.berkeley.edu/computing/ssh-keys). Here's an
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

[← 3. Parts of a computer](03-3-parts-of-a-computer.md) · [Up: contents](index.md) · [5. Editors →](05-5-editors.md)
