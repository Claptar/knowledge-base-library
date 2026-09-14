---
title: Dynamic Programming for sequence alignment
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Dynamic Programming for sequence alignment

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

• Setting up dynamic programming

##### 1. Find ‘matrix’ parameterization

• Prefix parameterization. Score(S1[1..i],S2[1..j])  M(i,j) • (i,j) only prefixes vs. (i,j,k,l) all substrings  simpler 2-d matrix

2. Make sure sub-problem space is finite! (not exponential) • It’s just n<sup>2</sup> , quadratic (which is polynomial, not exponential)

3. Traversal order: sub-results ready when you need them


Cols Rows

Cols Rows Diags LR topbot topRbotL

4. Recursion formula:  larger problems = Func(subparts)

   - Need formula for computing M[i,j] as function of previous results

   - Single increment at a time, only look at M[i-1,j], M[i,j-1], M[i-1,j-1] corresponding to 3 options: gap in S1, gap in S2, char in both

   - • Score in each case depends on gap/match/mismatch penalties

5. Remember choice: F() typically includes min() or max() • Remember which of three cells (top,left,diag) led to maximum

38

**Step 1: Setting up the scoring matrix M[i,j]** - A G T **Initialization:** - 0 • Top left: 0 **Update Rule:** A M( _i_ , _j_ )=max{ A } G **Termination:** • Bottom right C

39


<!-- Start of picture text -->
Step 2: Filling in the optimal scores from top left<br>-  A G T<br>Initialization:<br>-  0  -2  -4  -6<br>• Top left: 0<br>1<br>-1  -1<br>Update Rule:<br>A -2  1  -1  -3  M( i , j )=max{<br>1<br>-1  -1  • M( i -1 ,    j  ) - 2  gap<br>• M(   i   ,  j -1) - 2  gap<br>A -4  -1  0  -2<br>1  • M( i -1 ,  j -1) -1<br>mismatch<br>-1<br>-1<br>• M( i -1 ,  j -1)+1<br>match<br>G }<br>-6  -3  0  -1<br>-1  -1  Termination:<br>-1<br>• Bottom right<br>C  -8  -5  -2  -1<br><!-- End of picture text -->

###### Path segment that lead to the optimal choice

40

---

[← Computing alignments recursively: M[i,j]=F(smaller)](33-computing-alignments-recursively-m-i-j-f-smaller.md) · [Up: contents](index.md) · [Step 3: Trace back pointers to construct alignment →](35-step-3-trace-back-pointers-to-construct-alignment.md)
