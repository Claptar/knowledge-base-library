---
title: 'Formulation 2: Longest common subsequence'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Formulation 2: Longest common subsequence

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• Given two possibly related strings S1 and S2

- What is the longest common subsequence? (gaps allowed)

S1 <mark>A C G T C A T C A</mark> S2 <mark>T A G T G T C A</mark>


<!-- Start of picture text -->
S1  A  C  G  T  C  A  T  C  A<br>S2<br>T  A  G  T  G  T  C  A<br>A  G  T  T  C  A<br><!-- End of picture text -->


<!-- Start of picture text -->
LCSS<br><!-- End of picture text -->

Related to: Edit distance:

- Number of changes needed for S1S2

- Uniform scoring

function

13

---

[← Formulation 1: Longest common substring](09-formulation-1-longest-common-substring.md) · [Up: contents](index.md) · [Formulation 3: Sequence alignment →](11-formulation-3-sequence-alignment.md)
