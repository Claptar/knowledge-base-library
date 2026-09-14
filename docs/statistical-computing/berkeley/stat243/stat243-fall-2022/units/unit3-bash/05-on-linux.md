---
title: on Linux
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit3-bash.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# on Linux

**Source:** [`units/unit3-bash.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit3-bash.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

ps -o pid,pcpu,pmem,user,cmd -C R
ps -o pid,pcpu,pmem,user,cmd,start_time --sort=start_time -C R | tail -n 30
ps -o pid --sort=start_time -C R | tail -n ${nJobs} | xargs kill

---

[← 3. bash shell examples](04-3-bash-shell-examples.md) · [Up: contents](index.md) · [on a Mac →](06-on-a-mac.md)
