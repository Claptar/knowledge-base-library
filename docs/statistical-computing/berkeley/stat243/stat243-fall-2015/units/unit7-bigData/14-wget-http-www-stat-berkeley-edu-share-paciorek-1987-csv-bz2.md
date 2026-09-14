---
title: wget http://www.stat.berkeley.edu/share/paciorek/1987.csv.bz2
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit7-bigData.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# wget http://www.stat.berkeley.edu/share/paciorek/1987.csv.bz2

**Source:** [`units/unit7-bigData.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit7-bigData.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

hadoop fs -copyFromLocal /mnt/airline/*bz2 /data/airline

---

[← or individual files, e.g., data for 1987](13-or-individual-files-e-g-data-for-1987.md) · [Up: contents](index.md) · [check files on the HDFS, e.g.: hadoop fs -ls /data/airline →](15-check-files-on-the-hdfs-e-g-hadoop-fs--ls-data-airline.md)
