---
title: 2 Evolutionary signatures of motifs
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Evolutionary signatures of motifs

**Source:** `psets/03-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, you will search for enriched (over-represented) k-mers in regions conserved across the yeast clade _Saccharomyces_ . Submit all code you write.

- (a) We have provided the sequence of all intergenic regions in _S. cerevisiae_ in the file `allinter` . We have also provided an annotation of conservation in the file `allintercons` . Each position marked with _∗_ corresponds to a conserved nucleotide. For simplicity, we will look for motifs which are non-degenerate, exact matches.

Compute the frequency and conservation of all 6-mers. Submit a plain text file with the 50 most frequently occurring and 50 most conserved motifs (those with the highest proportion of conserved instances).

> 1 `http://weblogo.threeplusone.com/create.cgi`

1

- (b) Compare frequently occurring motifs to highly conserved motifs. Are there biases in the sequence properties of either class? If so, where does this bias come from?

Which of the two lists should we use to direct further inquiry into yeast transcription factor binding sites? We have provided an annotation of known yeast motifs `yeast motifs.txt` . Which known motifs does your scan of 6-mers find?

---

[← 1 Gibbs sampling for motif discovery](02-1-gibbs-sampling-for-motif-discovery.md) · [Up: contents](index.md) · [3 RNA secondary structure →](04-3-rna-secondary-structure.md)
