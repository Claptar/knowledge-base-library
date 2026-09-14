---
title: 4 Using an Amazon Web Services EC2 virtual machine
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit8-parallel.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit8-parallel.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Using an Amazon Web Services EC2 virtual machine

**Source:** [`units/unit8-parallel.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit8-parallel.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We have a small grant from Amazon to use their EC2 service for class work. Mostly this will be used for Spark, but you can also use it for parallel processing on a single machine, either to test out the code in the parallel processing tutorial or to work on problem set questions. That said, for the most part you can also just use the BCE VM on your own machine provided your machine has enough cores, memory, and disk space that can be shared with the VM.

For details on starting up an Amazon EC2 instance that uses the BCE VM, please se the _AWSsetup.txt_ and _startEC2virtualMachine.txt_ files in the _howtos_ directory of the class repository. Please stop or terminate your instance as soon as you are done using it, so we don’t run out of credits, and please don’t run an EC2 instance for more than a couple of hours.

2

---

[← 3 Other approaches to parallel processing](03-3-other-approaches-to-parallel-processing.md) · [Up: contents](index.md)
