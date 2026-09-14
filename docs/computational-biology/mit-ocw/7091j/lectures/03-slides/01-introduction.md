---
title: Introduction
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `lectures/03-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7.36 / 20.390 / 6.802 7.91 / 20.490 / 6.874 / HST.506 Lecture #3 C. Burge Feb. 11, 2014 Global Alignment of Protein Sequences (NW, SW, PAM, BLOSUM)

1

###### Topic 1 Info

- Overview slide has blue background - readings for upcoming lectures are listed at bottom of overview slide

- Review slides will have purple background

- Send your background/interests to T A for posting if reg’d for grad version

- PS1 is posted. BLAST tutorial may be helpful

- PS2 is posted. Look at the programming problem

2

Local Alignment (BLAST) and Statistics

- Sequencing

- Conventional

- 2nd generation

- Local Alignment:

   - a simple BLAST-like algorithm

- Statistics of matching

- - Target frequencies and mismatch penalties for nucleotide alignments

Background for 2/7, 2/12 lectures: Z&B Ch. 4 & 5, **BLAST tutorial**

3

Questions: Chemistry / Library Prep Dye terminator chemistry: dye is attached to base How to put different adapters on the two ends? At least three ways: 1) RNA ligation OH p OH p

- 2) polyA tailing/polyTVN-ad2priming/circularization (PMID 19213877)

- 3) ligation of Y-shaped adapters


<!-- Start of picture text -->
T  A<br>A  T<br><!-- End of picture text -->

4

###### DNA Sequence Alignment I: Motivation

You are studying a recently discovered human non-coding RNA. You search it against the mouse genome using BLASTN (N for nucleotide) and obtain the following alignment:

Q: 1   ttgacctagatgagatgtcgttcacttttactcaggtacagaaaa 45 |||| |||||||||||| | |||||||||||| || ||||||||| S: 403 ttgatctagatgagatgccattcacttttactgagctacagaaaa 447

Is this alignment significant? Is this likely to represent a homologous RNA? How to find alignments?

5

###### DNA Sequence Alignment II

Identify high scoring segments whose score S exceeds a cutoff x using a **local alignment** algorithm (e.g., BLAST) Scores follow an extreme value (aka Gumbel) distribution:

P(S > x) = 1 - exp[-KMN e<sup>-λx</sup> ]

For sequences/databases of length M, N where K, λ are positive parameters that depend on the score matrix and the composition of the sequences being compared

Conditions: expected score is negative, but positive scores possible

###### **Alternate algorithm**

Karlin & Altschul 1990

6

Computational Efficiency Measure efficiency in cpu run time and memory O() = “big-oh” notation (computational Order of problem) Consider the number of individual computations required to run algorithm as a function of the number of ‘units’ in the problem (e.g., base pairs, amino acid residues) Analyze the asymptotic worst-case running time or sometimes just do the experiment and measure run time If problem scales as square of the number of units it is

O(n2) “order n-squared”

7

###### DNA Sequence Alignment III

How is λ related to the score matrix?

λ is the unique positive solution to the equation*:

∑ pirje<sup>λsij</sup> = 1 i,j pi = freq. of nt i in query, rj = freq. of nt j in subject sij = score for aligning an i,j pair

“Target frequencies”* : qij = pirje<sup>λsij</sup>

*Karlin & Altschul, 1990

8

###### DNA Sequence Alignment VI

Optimal mismatch penalty m for given target identity fraction r

m = ln(4(1-r)/3)/ln(4r)

Examples: r 0.75    0.95      0.99 m -1         -2         -3

r = expected fraction of identities in high-scoring BLAST hits

9

###### DNA Sequence Alignment VII

Meaning of mismatch penalty equation

Examples:

r 0.75 0.95 0.99 m = ln(4(1-r)/3)/ln(4r) m -1 -2 -3

So why is m = -3 better for finding matches with 99% identity?

Does it mean that you can only find 99% identical matches with a mismatch score of -3? Answer: No. It’s also possible to find 99% matches with m = -1 or -2.

But m changes the match length required to achieve statistical significance

- λ is the unique positive solution to the equation

- ∑ pipje<sup>λsij</sup> = 1 pi = frequency of nt i, sij = score for aligning an i,j pair i,j

###### and P(S > x) = 1 - exp[-KMN e<sup>-λx</sup> ]

If we change the mismatch score from -1 to -3, λ will increase. Therefore, the score required to achieve a given level of significance will decrease, i.e. shorter hits will be significant. So why would you ever want to use m = -1?

10


<!-- Start of picture text -->
Google:<br>blastn<br><!-- End of picture text -->


Courtesy of National Library of Medicine. In the public domain.

11


Courtesy of National Library of Medicine. In the public domain.

12

###### DNA Sequence Alignment VIII

Translating searches: translate in all possible reading frames search peptides against protein database (BLASTP)

ttgacctagatgagatgtcgttcacttttactgagctacagaaaa

ttg|acc|tag|atg|aga|tgt|cgt|tca|ctt|tta|ctg|agc|tac|aga|aaa **L   T   x   M   R   C   R   S   L   L   L   S   Y   R   K**

t|tga|cct|aga|tga|gat|gtc|gtt|cac|ttt|tac|tga|gct|aca|gaa|aa **x   P   R   x   D   V   V   H   F   Y   x   S   T   E** tt|gac|cta|gat|gag|atg|tcg|ttc|act|ttt|act|gag|cta|cag|aaa|a **D   L   D   E   M   S   F   T   F   T   E   L   Q   K** Also consider reading frames on complementary DNA strand

13

###### DNA Sequence Alignment IX

Common flavors of BLAST:

|Program<br>|Query<br> Database|
|---|---|
|BLASTP|aa <br> aa|
|BLASTN|nt<br> nt|
|BLASTX|nt(⇒ aa)aa|
|TBLASTN|aant(⇒ aa)|
|TBLASTX|nt(⇒ aa)nt(⇒ aa)|
|PsiBLAST|aa(aamsa)aa|


###### msa = multiple sequence alignment

Which would be best for searching ESTs against a genome?

14

Global Alignment of Protein Sequences (NW, SW, PAM, BLOSUM)

- Global sequence alignment (Needleman-Wunch-Sellers)

- Gapped local sequence alignment (Smith-Waterman)

- Substitution matrices for protein comparison

Background for today: Z&B Chapters 4,5 (esp. pp. 119-125)

15

#### Why align protein sequences?

- Functional predictions based on identifying homologous proteins or protein domains

###### **Assumes**

Sequence similarity Similarity in function (and/or structure) implies

- almost always true for similarity > 30%

- 20-30% similarity is “the twilight zone”

**BUT:** Function carried out at level of folded protein, i.e. 3-D structure Sequence conservation occurs at level of 1-D sequence

**Converse is not true**

Structural similarity

Sequence similarity X (or even homology)

16

## Convergent Evolution


<!-- Start of picture text -->
hummingbird<br><!-- End of picture text -->

Courtesy of Matthew Field. License: CC-BY.


<!-- Start of picture text -->
hawk moth<br><!-- End of picture text -->


Last common ancestor lived > 500 Mya and lacked wings (and probably legs and eyes)

Same idea for proteins - can result in similar structures with no significant similarity in sequence

© Dave Green at Butterfly Conservation. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

17

###### **Convergent Evolution of Fe3+-binding Proteins**


<!-- Start of picture text -->
hummingbird<br><!-- End of picture text -->

_Haemophilus_ Fe3+-binding protein (hFBP)

Last common ancestor occurred > 2Bya and bound anions

Eukaryotic lactoferrin

Courtesy of Nature Publishing Group. Used with permission. Source: Bruns, Christopher M., Andrew J. Nowalk, et al. "Structure of Haemophilus Influenzae Fe+3-Binding Protein Reveals Convergent Evolutionwithin a Superfamily." _Nature Structural & Molecular Biology_ 4, no. 11 (1997): 919-24.

Bruns et al. Nature Struct. Biol. 1997

18

###### **Convergent Evolution of a Protein and an RNA**


RRF (protein)

###### Yeast tRNA<sup>Phe</sup>

Unlikely to have ever had a common molecular ancestor

© American Association for the Advancement of Science. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Selmer, Maria, Salam Al-Karadaghi, et al. "Crystal Structure of Thermotoga Maritima Ribosome Recycling Factor: A tRNA Mimic." _Science_ 286, no. 5448 (1999): 2349-52.

Selmer et al. Science 286. 2349 -. 1999

###### _T. maritima_ ribosome recycling factor (RRF)

19

### Types of Alignments

###### **Scope:**

- **Local**

- **Global**

- **Semiglobal**

###### **Scoring system:**

- **Ungapped**

- **Gapped linear affine**

20

## Dot Matrix Alignment Example


<!-- Start of picture text -->
Sequence #1<br><!-- End of picture text -->


<!-- Start of picture text -->
1  n<br>Sequence #2<br>1<br>Insertion in seq2<br>Insertion in seq1<br>m<br>What type of alignment would be most appropriate for this pair of sequences?  Global<br><!-- End of picture text -->

**What type of alignment would be most appropriate for this pair of sequences?**

21

##### Dot Matrix Alignment Example 2

###### **Sequence #1**


<!-- Start of picture text -->
Sequence #2  1   n<br>1<br>m<br><!-- End of picture text -->

**What type of alignment would be most appropriate for this pair of sequences?**


<!-- Start of picture text -->
Local<br><!-- End of picture text -->

22

**AKHFRGCVS Gaps (aka “Indels”) AKKF--CVG**

- **Linear Gap Penalty**

   - γ(n) **= n** A **, n= no. of gaps,** A **= gap penalty**

- **“Affine” gap penalty**

**Wn = G + n** γ,

- **n = no. of gaps,** γ **= gap extension penalty, and G = gap opening penalty**

- **Or:**

**Wn = G + (n-1)** γ

**with alternative definition of gap opening penalty**

23

**Obtain optimal global alignment using** **_Dynamic Programming_** _:_ **First write one sequence across the top, and one down along the side**


<!-- Start of picture text -->
Gap  V  D  S  C  Y<br>Gap  0  1 gap  2 gaps<br>V  1 gap<br>E<br>2 gaps<br>S<br>L<br>C<br>Y<br><!-- End of picture text -->

**_Note – linear gap penalty:_** γ **_(n)=nA, where A=gap penalty a negative number_**

24

###### **Dynamic Programming:**

###### **Initialize the alignment matrix**

- **i =0 1 2 3 4 5**

- **Gap V D S C Y**

- **j = 0 Gap 0 -8 -16 -24 -32 -40 1 V -8 sij 2 E -16 Sij** = score of optimal alignment ending at position **i** in

- **3 S -24** seq 1 and **j** in seq 2. Requires that we know **S(i-1, j-1), S(i, j-1), S(i-1, j).**

- **4 L -32** _Recursive_ : Solution to larger problem is built up from solutions to smaller problems

- **5 C -40** Store **Sij** and how we arrived at **Sij** in a matrix Often called ‘dynamic programming’ or more generally

- **6 Y -48** ‘recursive optimization’

What is the gap penalty in this example?

25

###### **Dynamic Programming: Recursion**


<!-- Start of picture text -->
Sequence 1<br>i =0  1  2  3  4  5<br>Sequence 2<br>Gap  V  D  S  C  Y<br>j =<br>0  Gap  0   -8  -16  -24  -32  -40<br>1 V<br>-8   sij<br>2  E  -16<br>Global alignments: Needleman-Wunsch-Sellers<br>3  S  -24<br>Sij  = max of:  Si-1, j-1 +  σ (xi, yj)  (diagonal)<br>4  L  -32<br>5  C  -40   Si-1, j + A  (from left to right)<br>6   Y  -48<br>Si, j-1+ A  (from top to bottom)<br><!-- End of picture text -->

**Computational complexity? O(mn) with linear gap penalty**

26

---

[Up: contents](index.md) · [PAM250 Scoring Matrix →](02-pam250-scoring-matrix.md)
