---
title: setup plan
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# setup plan

**Source:** [`section/08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

nCores = 2
future::plan(strategy = multisession, workers = nCores)

---

[← safer way](05-safer-way.md) · [Up: contents](index.md) · [setup base and name globals →](07-setup-base-and-name-globals.md)
