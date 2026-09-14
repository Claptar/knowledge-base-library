---
title: 'Data transfer: SCP/SFTP'
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/scfOverview.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data transfer: SCP/SFTP

**Source:** [`section/08/scfOverview.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/scfOverview.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We can use the *scp* and *sftp* protocols to transfer files from any login node
on the SCF cluster.

For example, the file `bayArea.csv` is too large to store on Github; you can obtain it
[here](https://www.stat.berkeley.edu/share/paciorek/bayArea.csv).

To transfer that to your directoy on the SCF cluster, the syntax for `scp` is
`scp <from-place> <to-place>`

```

---

[← Logging in](06-logging-in.md) · [Up: contents](index.md) · [to SCF, while on your local machine →](08-to-scf-while-on-your-local-machine.md)
