---
title: Semiglobal Alignment
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Semiglobal Alignment

**Source:** `lectures/03-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Allow sequences to overhang at either end without penalty -usually gives better alignments of homologous sequences of different lengths**

**Same algorithm as before except**

- **initialize edges of DP matrix Si,0 and S0,j to 0**

- **instead of requiring traceback to begin at Sm,n, allow it to begin at highest score in bottom row or rightmost column**

35

Gapped Local Alignment **Temple Smith and Michael Waterman, 1981 – modified Needleman-Wunsch-Sellers**

**Local alignment is the best scoring alignment of a substring in sequence x to a substring in sequence y.**

**Key idea is not to force the alignment to extend to the ends of the sequences**

Photograph of scientists removed due to copyright restrictions.

36

#### Smith-Waterman Local Alignment

Again, use dynamic programming

**Same basic scheme as before except**

- **similarity matrix MUST include negative values for mismatches and**

- **when the value calculated for a position in the scoring matrix is negative, the value is set to zero - this terminates the alignment**

37

###### **<u>Smith-Waterman</u>** <u>:</u>

###### **Write one sequence across the top, and one down along the side**


<!-- Start of picture text -->
i =0  1  2  3  4  5<br>Gap  V  D  S  C  Y<br>j =<br>0 Gap  0 0 0  0  0  0<br>1 V<br>0 sij<br>2 E<br>0<br>Local alignments: Smith-Waterman<br>3 S<br>0<br>Sij  = max of:  Si-1, j-1 +  σ (xi, yj)  (diagonal)<br>4 L<br>0<br>5 C<br>Si-1, j – A  (from left to right)<br>0<br>6 Y<br>0<br>Si, j-1– A  (from top to bottom)<br>0<br><!-- End of picture text -->

38

###### **Need a metric of similarity between amino acid pairs**

|**S**|**im**<br>A|**plest**<br>C D|**me**<br>E|**tric**<br>F|**–**<br>G|**ide**<br>H|**nti**<br>I|**ty m**<br>K|**atrix**|
|---|---|---|---|---|---|---|---|---|---|
|A|1|0 0|0|0|0|0|0|0|OK for nucleic acids,<br>|
|C||1 0|0|0|0|0|0|0|but for proteins can<br>do substantially better|
|D||1|0|0|0|0|0|0|What properties should an|
|E|||1|0|0|0|0|0|<br>amino acid similarity matrix<br>h?|
|F||||1|0|0|0|0|ave|
|G|||||1|0|0|0||
|H||||||1|0|0||
|I|||||||1|0|**Refer to**<br>|
|K||||||||1|**Z&B pp. 119-125**|


39

**Scoring system should favor matching identical or related amino acids and penalize for poor matches and for gaps**

**Need to know how often a particular amino acid pair is found in related proteins compared with its occurence by chance, and also how often gaps (insertions/deletions) are found in related proteins relative to dissimilar amino acid pairs**

40

###### Scores and Evolution

**Any alignment scoring system brings with it an implicit evolutionary model**

41

Amino Acid Substitution Matrices **Margaret Dayhoff, 1978, PAM Matrices**

**<u>Explicit evolutionary model</u> Assumes symmetry: A** → **B = B** → **A Assumes amino acid substitutions observed over short periods of time can be extrapolated to long periods of time 71 groups of protein sequences, 85% similar 1572 amino acid changes.**

**Functional proteins** → **mutations “accepted” by natural selection PAM1 matrix means 1% divergence between proteins - i.e. 1 amino acid change per 100 residues. Some texts re-state this as the probability of each amino acid changing into another is ~ 1% and probability of not changing is ~99%**

42

Construction of a Dayhoff Matrix: PAM1 **Step 1:** **_Measure pairwise substitution frequencies_ for each amino acid within families of related proteins that can be confidently aligned**

**….GDSFHYFVSHG….. ….GDSFHYYVSFG….. ….GDSYHYFVSFG….. ….GDSFHYFVSFG….. ….GDSFHFFVSFG…..**

**900 Phe (F) remained F 100 Phe (F)** → **80 Tyr (Y), 3 Trp (W), 2 His (H).. Gives** **_n_ ab, i.e.** **_n_ YF=80** **_n_** indicates raw count **_n_ WF=3** of events

**..in evolution**

43

###### DNA Sequence Evolution


Generation **_n-1_** (grandparent)

- 5’ TGGCATGCACCCTGTAAGTCAATATAAATGGCTACGCCTAGCCCATGCGA 3’ |||||||||||||||||||||||||||||||||||||||||||||||||| 3’ ACCGTACGTGGGACATTCAGTTATATTTACCGATGCGGATCGGGTACGCT 5’ Generation **_n_** (parent)


- 5’ TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCATGCGA 3’ |||||||||||||||||||||||||||||||||||||||||||||||||| 3’ ACCGTACGTGGGACATTCAGTTATATTTACCGATACGGATCGGGTACGCT 5’

Generation **_n+1_** (child)


- 5’ TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCGTGCGA 3’ |||||||||||||||||||||||||||||||||||||||||||||||||| 3’ ACCGTACGTGGGACATTCAGTTATATTTACCGATACGGATCGGGCACGCT 5’

Images of The Simpsons © FOX. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

44

###### Markov Model (aka Markov Chain)

Stochastic Process:

- a random process or

<u>Classical Definition</u>

- a sequence of Random Variables

A discrete stochastic process X1, X2, X3, . which has the Markov property:

P(Xn+1 = j | X1=x1, X2=x2, . Xn=xn) = P(Xn+1 = j | Xn=xn )

(for all xi, all j, all n)


Image is in the public domain.

<u>In words:</u>

A random process which has the property that the future (next state) is conditionally independent of the past given the present (current state)

Andrey Markov, a Russian mathematician (1856 - 1922)

45

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← PAM250 Scoring Matrix](02-pam250-scoring-matrix.md) · [Up: contents](index.md)
