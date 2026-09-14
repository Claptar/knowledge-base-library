---
title: on Linux
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit3-bash.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# on Linux

**Source:** [`units/unit3-bash.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit3-bash.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

ps -o pid,pcpu,pmem,user,cmd -C python
ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C python | tail -n 30
ps -o pid --sort=start_time -C python | tail -n ${nJobs} | xargs kill

---

[← alternatively](07-alternatively.md) · [Up: contents](index.md) · [on a Mac →](09-on-a-mac.md)
