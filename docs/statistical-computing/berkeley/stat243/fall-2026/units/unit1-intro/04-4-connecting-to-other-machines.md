---
title: 4. Connecting to other machines
source: https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit1-intro.qmd
source_file: sources/berkeley-stat243/fall-2026/units/unit1-intro.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Connecting to other machines

**Source:** [`units/unit1-intro.qmd`](https://github.com/berkeley-stat243/fall-2026/blob/c74395ec9c420005c80bbcc5f315729aaee3dc32/units/unit1-intro.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

To connect to a remote machine, you generally need to use SSH. SSH is available as
`ssh` when you are on the UNIX command line. There are also SSH clients
for Windows. The SCF has [more information on SSH client programs and on using
SSH](https://computing.stat.berkeley.edu/access/ssh), including [connecting without
entering your password](https://computing.stat.berkeley.edu/kb/ssh-keys). Here's an
example of connecting to one of the SCF machines (this assumes you have
an SCF account, which you may, and that your user name is paciorek,
which it is not).

```bash
ssh paciorek@radagast.berkeley.edu
```

To copy files between machines, we can use *scp*, which has similar
options to *cp*. Here's how we can copy a local file to a remote
machine.

```bash
scp file.txt paciorek@radagast.berkeley.edu:~/research/.
```

And here's how we can copy from a remote machine to the machine you are
on.

```bash
scp paciorek@radagast.berkeley.edu:/data/file.txt \
  ~/research/renamed.txt
```

You can use relative paths to refer to locations on the local
machine. On the remote machine all paths need to be absolute or to be
relative to your home directory on that machine.

There are also client programs for file transfer; see [this
webpage](https://computing.stat.berkeley.edu/access/copying-files).

---

[← 3. Parts of a computer](03-3-parts-of-a-computer.md) · [Up: contents](index.md) · [5. Knowing your context →](05-5-knowing-your-context.md)
