---
title: 'Computing alignments recursively: M[i,j]=F(smaller)'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Computing alignments recursively: M[i,j]=F(smaller)

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- <u>Local update rules, only look at neighboring cells:</u> – Compute next alignment based on previous alignment

   - Just like Fibonacci numbers:  F[i] = F[i-1] + F[i-2]

   - Table lookup avoids repeated computation

- Computing the score of a cell from smaller neighbors M( i-1, j  ) -  gap <u>i-1 i</u>

- – M(i,j) = max{ M( i-1, j-1) + score } j-1 M(  i ,  j-1) -  gap j **(i,j)**

   - Only three possibilities for extending by one nucleotide: a gap in one species, a gap in the other, a (mis)match

- Compute scores for prefixes of increasing length – Start with prefixes of length 1, extend by one each time, until all prefixes have been computed

   - When you reach bottom right, alignment score of S1[1..m] and S2[1..n] is alignment of full S1 and full S2

– (Can then trace back to construct optimal path to it)

5

- **Dynamic Programming for sequence alignment**

- • Setting up dynamic programming

   1. Find ‘matrix’ parameterization

      - Prefix parameterization. Score(S1[1..i],S2[1..j])  M(i,j)

      - • (i,j) only prefixes vs. (i,j,k,l) all substrings  simpler 2-d matrix

   2. Make sure sub-problem space is finite! (not exponential) • It’s just n<sup>2</sup> , quadratic (which is polynomial, not exponential)

3. Traversal order: sub-results ready when you need them Cols Rows Diags LR topbot topRbotL

4. Recursion formula:  larger problems = Func(subparts)

   - Need formula for computing M[i,j] as function of previous results

   - Single increment at a time, only look at M[i-1,j], M[i,j-1], M[i-1,j-1] corresponding to 3 options: gap in S1, gap in S2, char in both

   - Score in each case depends on gap/match/mismatch penalties

5. Remember choice: F() typically includes min() or max()

   - Remember which of three cells (top,left,diag) led to maximum

   - • Trace-back from max score to identify path leading to it

6

---

[← Duality: seq. alignment  path through the matrix](03-duality-seq-alignment-path-through-the-matrix.md) · [Up: contents](index.md) · [Algorithmic variations (save time and/or space) →](05-algorithmic-variations-save-time-and-or-space.md)
