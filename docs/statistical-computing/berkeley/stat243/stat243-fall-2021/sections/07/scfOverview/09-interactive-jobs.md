---
title: Interactive jobs
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/07/scfOverview.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Interactive jobs

**Source:** [`sections/07/scfOverview.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/07/scfOverview.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can do work interactively.

For this, you may want to have used the -Y flag to ssh if you are running software with a GUI such as MATLAB.

```
#ssh-YSCF_USERNAME@arwen.berkeley.edu
srun--pty/bin/bash#interactivebashjob
srun--pty--x11=firstmatlab#interactivematlabjob
```

To display the graphical windows on your local machine, you’ll need X server software on your own machine to manage the graphical windows. For Windows, your options include _eXceed_ or _Xming_ and for Mac, there is _XQuartz_ .

---

[← Submitting jobs: accounts and partitions](08-submitting-jobs-accounts-and-partitions.md) · [Up: contents](index.md) · [Submitting a batch job →](10-submitting-a-batch-job.md)
