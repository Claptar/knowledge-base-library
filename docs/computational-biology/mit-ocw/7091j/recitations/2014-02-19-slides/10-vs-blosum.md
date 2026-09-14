---
title: vs. BLOSUM
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# vs. BLOSUM

**Source:** `recitations/2014-02-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Evolutionary time measured in Percent Accepted Mutations (PAMs)

- One PAM: 1% of the residues have changed, averaged over all 20 amino acids.

   - BLOSUM matrices are based on _local_ alignments

   - BLOSUM 62 is a matrix calculated from alignment of sequences with ~62% identity.

- To get the relative frequency of each type of mutation, count the times it was observed in a database of multiple sequence _global_ alignments

   - BLOSUM matrices are based on observed alignments; unlike PAM, they are not extrapolated from comparisons of closely related proteins

- The PAM1 is the matrix calculated from comparisons of sequences with no more than 1% divergence

   - BLOSUM 62 is the default matrix in BLAST. It’s tailored for comparisons of moderately distant proteins.

- Mutation frequencies assume a Markov model of evolution. Other matrices derived from PAM1:

- PAM250 ~ (PAM1)<sup>250</sup>

- Alignment of more distant proteins may be more accurate with a different matrix based on substitutions observed in more distantly evolved proteins

12

-See Nat. Biotech. 2 page primer for more in-depth discussion of BLOSUM62:<sup>http://selab.janelia.org/publications/Eddy-ATG2/Eddy-ATG2-reprint.pdf</sup>

---

[← PAM](09-pam.md) · [Up: contents](index.md) · [Jukes-Cantor model →](11-jukes-cantor-model.md)
