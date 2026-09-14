---
title: Biomolecular Sequence Motif
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Biomolecular Sequence Motif

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- A pattern common to a set of DNA, RNA or protein sequences that share a common biological property

   - nucleotide binding sites for a particular protein (TATA box in promoter, 5’ and 3’ splice site sequences)

   - amino acid residues that fold into a characteristic structure (zinc finger domains of TFs)

- Consensus sequence is the one most common occurrence of the motif (e.g. TATAAA for TATA box)

   - Stronger motifs (= more information, lower entropy, less degenerate) have less deviation from consensus sequence

- Position weight matrix gives the probability of each nucleotide or amino acid at each position

   - Assumes independence between positions

   - Can be visualized with a Sequence Logo

   - showing probability at each position

or with each position height scaled by the information content of that position


2

---

[Up: contents](index.md) · [Shannon Entropy →](02-shannon-entropy.md)
