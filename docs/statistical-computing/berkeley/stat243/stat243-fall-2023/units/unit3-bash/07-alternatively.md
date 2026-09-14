---
title: alternatively
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit3-bash.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# alternatively

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

echo -e "import time\ntime.sleep(1e5)" > job.py

nJobs=30
for (( i=1; i<=${nJobs}; i++ )); do
   python job.py > job-${i}.out &
done

---

[← use a 'here document'](06-use-a-here-document.md) · [Up: contents](index.md) · [on Linux →](08-on-linux.md)
