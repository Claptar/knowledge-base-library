---
title: Logging in
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s07/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Logging in

**Source:** [`section/s07/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

To login, you need to have software on your own machine that gives you access to a UNIX terminal (command-line) session. These come built-in with Mac (see `Applications -> Utilities -> Terminal`). For Windows, some options include [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).

You also need to set up your smartphone or tablet with *Google Authenticator* to generate one-time passwords for you.

Here are instructions for [doing this setup, and for logging in](http://research-it.berkeley.edu/services/high-performance-computing/logging-savio).

Then to login:
```
ssh SAVIO_USERNAME@hpc.brc.berkeley.edu
```

Then enter XXXXXYYYYYY where XXXXXX is your PIN and YYYYYY is the one-time password. YYYYYY will be shown when you open your *Google authenticator* app on your phone/tablet.

One can then navigate around and get information using standard UNIX commands such as `ls`, `cd`, `du`, `df`, etc.

If you want to be able to open programs with graphical user interfaces:
```
ssh -Y SAVIO_USERNAME@hpc.brc.berkeley.edu
```

To display the graphical windows on your local machine, you'll need X server software on your own machine to manage the graphical windows. For Windows, your options include *eXceed* or *Xming* and for Mac, there is *XQuartz*.

---

[← Login nodes, compute nodes, and DTN nodes](06-login-nodes-compute-nodes-and-dtn-nodes.md) · [Up: contents](index.md) · [Data transfer: SCP/SFTP →](08-data-transfer-scp-sftp.md)
