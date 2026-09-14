---
title: now is a path in my home directory on the SCF
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd
source_file: sources/berkeley-stat243/fall-2025/labs/lab6-scfparallel.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# now is a path in my home directory on the SCF

**Source:** [`labs/lab6-scfparallel.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/labs/lab6-scfparallel.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

scp <scf-username>@gandalf.berkeley.edu:~/data/new_name.csv ~/Desktop/data_scf.csv
```

For more information, see
[here](https://statistics.berkeley.edu/computing/copying-files). In particular,
if you have a very large dataset to transfer,
[Globus](https://statistics.berkeley.edu/computing/faqs/using-globus-file-transfers)
is a better option than either `scp` or `sftp`.

---

[← transfer to the gandalf-specific /tmp/ directory](06-transfer-to-the-gandalf-specific-tmp-directory.md) · [Up: contents](index.md) · [Running jobs on the SCF →](08-running-jobs-on-the-scf.md)
