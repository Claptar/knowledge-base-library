---
title: now is a path in my home directory on the SCF
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/labs/06/scf.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# now is a path in my home directory on the SCF

**Source:** [`labs/06/scf.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/labs/06/scf.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

scp <scf-username>@dorothy.berkeley.edu:~/data/new_name.csv ~/Desktop/data_scf.csv
```

For more information, see
[here](https://statistics.berkeley.edu/computing/copying-files). In particular,
if you have a very large dataset to transfer,
[Globus](https://statistics.berkeley.edu/computing/faqs/using-globus-file-transfers)
is a better option than either `scp` or `sftp`.

---

[← transfer to the dorothy-specific /tmp/ directory](06-transfer-to-the-dorothy-specific-tmp-directory.md) · [Up: contents](index.md) · [Running jobs on the SCF →](08-running-jobs-on-the-scf.md)
