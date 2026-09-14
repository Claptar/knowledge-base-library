---
title: Backtracking
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Backtracking

**Source:** `lectures/05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• Relevant alignments may lie along multiple paths – E.g., Q = “aaa”, T = “acaacg”


<!-- Start of picture text -->
“ a ” “ a ”<br>“ a ”<br><!-- End of picture text -->


<!-- Start of picture text -->
“ a ” “ a ” “ c ” “ a ” “ a ” “ c ”<br>“ a ” “ a ”<br>“ c ”<br><!-- End of picture text -->


```
acaacg
aaa
```

```
acaacg
aaa
```

```
acaacg
```

```
aaa
```

Courtesy of Ben Langmead. Used with permission.

42

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

#### Bowtie backtracks to leftmost just-visited position with minimal quality

- PHRED score = -10log(p)     Where p is probability of error

Sequence: <mark>G</mark> C <mark>C</mark> A <mark>T A C G G A T</mark> T <mark>A</mark> G <mark>C</mark> C Phred Quals: <mark>40</mark> 40 <mark>35</mark> 40 <mark>40 40 40 30 30 20 15</mark> 15 <mark>40</mark> 40 <mark>40</mark> 40 (higher number = higher confidence) <mark>G C C A T A C G G A C T A G C C 40</mark> 40 <mark>35</mark> 40 40 40 40 30 30 20 15 15 <mark>40</mark> 40 <mark>40</mark> 40 <mark>G</mark> C <mark>C</mark> A T A C G G G C T <mark>A</mark> G <mark>C</mark> C <mark>40</mark> 40 <mark>35</mark> 40 <mark>40 40 40 30 30 20 15</mark> 15 <mark>40</mark> 40 <mark>40</mark> 40

- Greedy, depth-first, not optimal, but simple

Courtesy of Ben Langmead. Used with permission.

43

**http://www.cbcb.umd.edu/~langmead/NCBI_Nov2008.ppt**

---

[← Backtracking](21-backtracking.md) · [Up: contents](index.md) · [Specifying match quality →](23-specifying-match-quality.md)
