---
title: alternatively
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit3-bash.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# alternatively

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit3-bash.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

echo -e "import time\ntime.sleep(1e5)" > job.py

nJobs=30
for (( i=1; i<=${nJobs}; i++ )); do
   python job.py > job-${i}.out &
done

---

[← Use a 'here document'](07-use-a-here-document.md) · [Up: contents](index.md) · [on Linux →](09-on-linux.md)
