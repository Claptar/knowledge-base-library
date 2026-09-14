---
title: Table of tools
source: https://github.com/pachterlab/biophysics/blob/ca6fe2ae824eb4cc3508ce951e1a7a868f50a043/docs/source/index.rst
source_file: sources/pachter-biophysics-docs/docs/source/index.rst
licence: BSD-2-Clause
route: pandoc-rst
fidelity: high
converted: '2026-09-14'
---

# Table of tools

**Source:** [`docs/source/index.rst`](https://github.com/pachterlab/biophysics/blob/ca6fe2ae824eb4cc3508ce951e1a7a868f50a043/docs/source/index.rst) · **Licence:** BSD-2-Clause · Converted 2026-09-14 from `.rst` (high)

Below is a table of the Pachter Lab's current tools for biophysical modeling of high-throughput genomics data. The main features and input data types are listed across the columns. All methods require data with UMIs (molecular count data).

| Tool | Task | Resolution | Modalities | Steady State? | Technical Noise? | Language |
|-----------------|------------|--------|--------|---------|-----------|-------|
| `Monod<monod>` | Parameter Inference | gene | U/S RNA | yes | yes (3' seq) | Python |
| `biVI<bivi>` | Parameter Inference | cell/gene | U/S RNA | yes | coming soon | Python |
| `meK-Means<mekmeans>` | Clustering | gene | U/S RNA | yes | yes (3' seq) | Python |
| `Chronocell<chronocell>` | Trajectory Inference | gene | U/S RNA | no | no | Python |
| Spatial: coming soon | Parameter Inference | gene | S RNA | yes | yes | Python |

**For more details on the available methods see** `packages`.

Not sure which tool is best for your data? See `choose`.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Foundational Literature →](03-foundational-literature.md)
