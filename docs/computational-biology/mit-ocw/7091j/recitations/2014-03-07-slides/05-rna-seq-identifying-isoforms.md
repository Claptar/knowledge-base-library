---
title: 'RNA-seq: identifying isoforms �'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# RNA-seq: identifying isoforms �

**Source:** `recitations/2014-03-07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Some reads map completely within a single exon – don’t directly tell us which isoforms are present, although expression levels of different exons can be helpful (e.g. twice as many exon

- 1 reads compared to exon 4 – probably some isoforms that include exon 1 but not exon 4)


<!-- Start of picture text -->
Non-junction<br>spanning reads<br>exon 1  exon 2  exon 3  exon 4<br>genome seq<br>putative exons<br><!-- End of picture text -->

- How do we directly identify the isoforms that generated these reads? Look

- at junction-spanning reads!

- Assuming exons 1 and 4 must be included, which isoform(s) are consistent with the following reads?


<!-- Start of picture text -->
or<br><!-- End of picture text -->

7

---

[← RNA-seq Protocol](04-rna-seq-protocol.md) · [Up: contents](index.md) · [RNA-seq: identifying isoforms � →](06-rna-seq-identifying-isoforms.md)
