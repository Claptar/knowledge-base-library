---
title: Logging in
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Logging in

**Source:** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can use login nodes for non-intensive interactive work such as job submission and monitoring, basic compilation, managing your disk space, and transferring data to/from the server.

To login, you need to have software on your own machine that gives you access to a UNIX terminal (commandline) session. These come built-in with Mac (see `Applications -> Utilities -> Terminal` ). For Windows, some options include PuTTY.

Here are instructions for doing this setup, and for logging in.

Login servers include: `arwen, beren, bilbo, gandalf, gimli, legolas, pooh, radagast, roo, shelob, springer, treebeard`

Then to login:

```
sshSCF_USERNAME@LOGINSERVER.berkeley.edu
```

Then enter your password.

One can then navigate around and get information using standard UNIX commands such as `ls` , `cd` , `du` , `df` , etc.

---

[← Disk Space](05-disk-space.md) · [Up: contents](index.md) · [Data transfer: SCP/SFTP →](07-data-transfer-scp-sftp.md)
