---
title: from Savio, while on your local machine
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s07/intro.md
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# from Savio, while on your local machine

**Source:** [`section/s07/intro.md`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s07/intro.md) · **Licence:** unresolved · Converted 2026-09-14 from `.md` (lossless)

scp paciorek@dtn.brc.berkeley.edu:~/data/newName.csv ~/Desktop/.
```

If you can ssh to your local machine or want to transfer files to other systems on to which you can ssh, you can login to the dtn node to execute the scp commands:

```
ssh SAVIO_USERNAME@dtn.brc.berkeley.edu
[SAVIO_USERNAME@dtn ~]$ scp ~/file.csv OTHER_USERNAME@other.domain.edu:~/data/.
```

If you're already connected to a Savio login node, you can use `ssh dtn` to login to the dtn.

One program you can use with Windows is *WinSCP*, and a multi-platform program for doing transfers via SFTP is *FileZilla*. After logging in, you'll see windows for the Savio filesystem and your local filesystem on your machine. You can drag files back and forth.

---

[← to Savio, while on your local machine](09-to-savio-while-on-your-local-machine.md) · [Up: contents](index.md) · [Software modules →](11-software-modules.md)
