---
title: Logging in
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/scfOverview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Logging in

**Source:** [`section/08/scfOverview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

You can use login nodes for non-intensive interactive work such as job submission
and monitoring, basic compilation, managing your disk space, and transferring data
to/from the server.

To login, you need to have software on your own machine that gives you access to
a UNIX terminal (command-line) session. These come built-in with Mac
(see `Applications -> Utilities -> Terminal`). For Windows, some options include
[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

Here are instructions for [doing this setup, and for logging in](https://statistics.berkeley.edu/computing/servers/cluster#access-job-restrictions).

Login servers include: `arwen, beren, bilbo, gandalf, gimli, legolas, pooh, radagast, roo, shelob, springer, treebeard`

Then to login:
```
ssh SCF_USERNAME@LOGINSERVER.berkeley.edu
```

Then enter your password.
One can then navigate around and get information using standard UNIX commands
such as `ls`, `cd`, `du`, `df`, etc.

---

[← Disk Space](05-disk-space.md) · [Up: contents](index.md) · [Data transfer: SCP/SFTP →](07-data-transfer-scp-sftp.md)
