---
title: ssh -Y SCFUSERNAME@arwen.berkeley.edu
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/scfOverview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ssh -Y SCFUSERNAME@arwen.berkeley.edu

**Source:** [`section/08/scfOverview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

srun --pty /bin/bash           # interactive bash job
srun --pty --x11=first matlab  # interactive matlab job
```

To display the graphical windows on your local machine, you'll need X server
software on your own machine to manage the graphical windows. For Windows,
your options include *eXceed* or *Xming* and for Mac, there is *XQuartz*.

---

[← Interactive jobs](11-interactive-jobs.md) · [Up: contents](index.md) · [Submitting a batch job →](13-submitting-a-batch-job.md)
