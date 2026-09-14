---
title: FASTQ format - sequence ID line
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/images_sequencing/fastqLine.pdf
source_file: sources/statomics-sga21/images_sequencing/fastqLine.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# FASTQ format - sequence ID line

**Source:** [`images_sequencing/fastqLine.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/images_sequencing/fastqLine.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- D7MHBFNI - unique instrument name

- 202 - run ID

   - 1 - member of pair (1 or 2). Older versions: /1 and /2

- D1BUDACXX - flowcell ID

- 4 - flowcell lane

- 1101 - tile number within lane

- 1340 - x-coordinate of cluster within tile

   - Y/N - whether the read failed quality control (Y = bad)

   - 0 - none of the control bits are on

   - CATGCA - index sequence (barcode)

- 1967 - y-coordinate of cluster within tile

---

[Up: contents](../index.md)
