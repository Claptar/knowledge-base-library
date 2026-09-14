---
title: 'Data transfer: SCP/SFTP'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data transfer: SCP/SFTP

**Source:** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can use the _scp_ and _sftp_ protocols to transfer files from any login node on the SCF cluster. For example, we show how to transfer the file `data.csv` .

To transfer that to your directoy on the SCF cluster, the syntax for `scp` is `scp <from-place> <to-place>`

2

Below are some examples of transferring this file to various locations on the remote machine (your home directory, a folder called data in your home directory, and the tmp folder)

```
#toSCF,whileonyourlocalmachine
scpdata.csvandrew_vaughn@arwen.berkeley.edu:~/
scpdata.csvandrew_vaughn@arwen.berkeley.edu:~/data/newName.csv
scpdata.csvandrew_vaughn@arwen.berkeley.edu:/tmp/
```

Here is how to transfer data from the SCF to your local machine, while on your local machine. This will transfer the `new_name.csv` file to your Desktop with the name `data_scf.csv`

```
#fromSCF,whileonyourlocalmachine
```

```
scpandrew_vaughn@arwen.berkeley.edu:~/data/new_name.csv~/Desktop/data_scf.csv
```

One program you can use with Windows is _WinSCP_ , and a multi-platform program for doing transfers via SFTP is _FileZilla_ . After logging in, you’ll see windows for the SCF filesystem and your local filesystem on your machine. You can drag files back and forth.

---

[← Logging in](06-logging-in.md) · [Up: contents](index.md) · [Submitting jobs: accounts and partitions →](08-submitting-jobs-accounts-and-partitions.md)
