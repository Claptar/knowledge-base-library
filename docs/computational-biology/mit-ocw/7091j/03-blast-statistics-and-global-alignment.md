---
title: "3. BLAST Statistics and Global Alignment"
course: "MIT 7.091J"
chapter: 3
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 3. BLAST Statistics and Global Alignment

## What this covers

This chapter follows lecture 3 of 7.91J (C. Burge, 11 February 2014) from the statistics of a BLAST
hit into the start of global alignment: how do you decide whether a local alignment found by BLAST
is more than chance, how does the mismatch penalty you choose change what counts as significant, and
how do you compute an optimal global alignment by dynamic programming? It ends with amino-acid
substitution matrices (PAM) and the formal definition of a Markov chain, which the lecture reaches
for to make precise an assumption the PAM construction needs. It assumes you already know roughly
what BLAST does (find locally similar segments between two sequences) and have seen a substitution
matrix used informally to score an alignment; no statistics beyond basic probability is assumed.

Only the slide deck survives for this lecture — no transcript. The deck itself is a reconstruction
from a PDF with no text layer, and its own banner warns that every equation in it is unverified and
that a few slides (the dynamic-programming matrix, in particular) come through visibly truncated.
Where the prose below fills a gap between two bullet points or completes a standard algorithm the
slide was visibly building toward, that is flagged.

## A leftover question: adapters on paired-end reads

Before turning to alignment, the lecture closed out a question held over from a previous class about
sequencing chemistry. In dye-terminator sequencing the dye is attached to the base, and a library
needs different adapters on the two ends of a fragment; the slide lists three ways to get there:
RNA ligation, polyA tailing together with polyT-VN adapter-2 priming and circularization (citing PMID
19213877), or ligation of a Y-shaped adapter. The slide does not elaborate beyond naming the three
routes.

## Is a BLAST hit real? The statistics of local alignment

The motivating example: you search a newly discovered human non-coding RNA against the mouse genome
with BLASTN and get back

```
Q:   1 ttgacctagatgagatgtcgttcacttttactcaggtacagaaaa 45
       |||| |||||||||||| | |||||||||||| || |||||||||
S: 403 ttgatctagatgagatgccattcacttttactgagctacagaaaa 447
```

Is this alignment significant? Is it likely to represent a homologous RNA? You cannot answer either
question by eyeballing the percentage of matched columns — you need to know how good an alignment
this good could be by chance alone.

A local-alignment algorithm such as BLAST reports high-scoring segments: those whose score $S$ exceeds
some cutoff. Under the null model — the two sequences are unrelated, with the given base or amino-acid
composition — the score of the best such segment behaves like the maximum of many locally-tested
random walks, and its distribution is not normal but an **extreme value (Gumbel) distribution**:

$$P(S > x) = 1 - \exp[-KMN e^{-\lambda x}]$$

for sequences or databases of length $M$ and $N$, where $K$ and $\lambda$ are positive constants that
depend on the scoring matrix and the sequence composition (Karlin & Altschul, 1990). This holds
provided the *expected* score of a random aligned pair is negative — so an alignment only accumulates
a high score by a run of good luck — while individual positive scores are still possible; otherwise
scores would simply grow without bound and there would be nothing to control for.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="Right-skewed extreme-value distribution of the best local-alignment score, with the tail beyond a cutoff shaded">
  <line x1="40" y1="180" x2="325" y2="180" stroke="currentColor" stroke-width="1.2"/>
  <path d="M 185.9,180 L 185.9,137.2 L 188.2,140.3 L 190.6,143.2 L 192.9,145.9 L 195.3,148.5 L 197.6,150.8 L 200.0,153.0 L 202.4,155.1 L 204.7,157.0 L 207.1,158.7 L 209.4,160.4 L 211.8,161.9 L 214.1,163.3 L 216.5,164.6 L 218.8,165.8 L 221.2,166.9 L 223.5,167.9 L 225.9,168.9 L 228.2,169.7 L 230.6,170.5 L 232.9,171.3 L 235.3,172.0 L 237.6,172.6 L 240.0,173.2 L 242.4,173.7 L 244.7,174.2 L 247.1,174.7 L 249.4,175.1 L 251.8,175.5 L 254.1,175.9 L 256.5,176.2 L 258.8,176.5 L 261.2,176.8 L 263.5,177.0 L 265.9,177.3 L 268.2,177.5 L 270.6,177.7 L 272.9,177.9 L 275.3,178.1 L 277.6,178.2 L 280.0,178.4 L 282.4,178.5 L 284.7,178.6 L 287.1,178.7 L 289.4,178.8 L 291.8,178.9 L 294.1,179.0 L 296.5,179.1 L 298.8,179.2 L 301.2,179.2 L 303.5,179.3 L 305.9,179.3 L 308.2,179.4 L 310.6,179.4 L 312.9,179.5 L 315.3,179.5 L 317.6,179.6 L 320.0,179.6 L 320.0,180 Z" fill="currentColor" fill-opacity="0.15" stroke="none"/>
  <path d="M 40.0,180.0 L 42.4,180.0 L 44.7,180.0 L 47.1,180.0 L 49.4,180.0 L 51.8,180.0 L 54.1,180.0 L 56.5,179.9 L 58.8,179.8 L 61.2,179.7 L 63.5,179.4 L 65.9,178.8 L 68.2,177.9 L 70.6,176.5 L 72.9,174.5 L 75.3,171.7 L 77.6,167.9 L 80.0,163.0 L 82.4,157.0 L 84.7,149.7 L 87.1,141.4 L 89.4,132.0 L 91.8,121.8 L 94.1,110.9 L 96.5,99.7 L 98.8,88.4 L 101.2,77.4 L 103.5,66.8 L 105.9,56.9 L 108.2,48.0 L 110.6,40.2 L 112.9,33.6 L 115.3,28.3 L 117.6,24.3 L 120.0,21.7 L 122.4,20.2 L 124.7,20.0 L 127.1,20.9 L 129.4,22.7 L 131.8,25.5 L 134.1,29.0 L 136.5,33.1 L 138.8,37.8 L 141.2,42.9 L 143.5,48.3 L 145.9,54.0 L 148.2,59.8 L 150.6,65.7 L 152.9,71.6 L 155.3,77.4 L 157.6,83.2 L 160.0,88.8 L 162.4,94.2 L 164.7,99.5 L 167.1,104.6 L 169.4,109.5 L 171.8,114.1 L 174.1,118.5 L 176.5,122.7 L 178.8,126.7 L 181.2,130.4 L 183.5,133.9 L 185.9,137.2 L 188.2,140.3 L 190.6,143.2 L 192.9,145.9 L 195.3,148.5 L 197.6,150.8 L 200.0,153.0 L 202.4,155.1 L 204.7,157.0 L 207.1,158.7 L 209.4,160.4 L 211.8,161.9 L 214.1,163.3 L 216.5,164.6 L 218.8,165.8 L 221.2,166.9 L 223.5,167.9 L 225.9,168.9 L 228.2,169.7 L 230.6,170.5 L 232.9,171.3 L 235.3,172.0 L 237.6,172.6 L 240.0,173.2 L 242.4,173.7 L 244.7,174.2 L 247.1,174.7 L 249.4,175.1 L 251.8,175.5 L 254.1,175.9 L 256.5,176.2 L 258.8,176.5 L 261.2,176.8 L 263.5,177.0 L 265.9,177.3 L 268.2,177.5 L 270.6,177.7 L 272.9,177.9 L 275.3,178.1 L 277.6,178.2 L 280.0,178.4 L 282.4,178.5 L 284.7,178.6 L 287.1,178.7 L 289.4,178.8 L 291.8,178.9 L 294.1,179.0 L 296.5,179.1 L 298.8,179.2 L 301.2,179.2 L 303.5,179.3 L 305.9,179.3 L 308.2,179.4 L 310.6,179.4 L 312.9,179.5 L 315.3,179.5 L 317.6,179.6 L 320.0,179.6" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="185.6" y1="180" x2="185.6" y2="20" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="185.6" y="196" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="260" y="150" font-size="12" fill="currentColor">P(S &#62; x)</text>
  <text x="330" y="184" text-anchor="end" font-size="12" fill="currentColor">S</text>
</svg>
<figcaption>Under the null model of unrelated random sequences, the best local-alignment score S has a
right-skewed extreme-value (Gumbel) distribution. The P-value of an observed hit is the shaded area
beyond it, $P(S > x) = 1 - \exp[-KMNe^{-\lambda x}]$; a larger $\lambda$ compresses this tail so that a
smaller score is enough to fall in it.</figcaption>
</figure>

Why a Gumbel shape rather than, say, a normal distribution centred on zero? One of the connections
problems on problem set 3 makes the mechanism concrete without any biology in it: a bank line that
grows by one customer with probability $\tfrac14$ each minute and shrinks by one with probability
$\tfrac34$, but can never go below zero, is exactly a local-alignment score under a $+1$/$-1$,
match/mismatch scheme, reset to $0$ whenever it would go negative. The line length over a long period
is dominated by rare lucky runs upward, and the length of the longest such run — like the score of
the best local alignment — is governed by the same $KMNe^{-\lambda x}$ tail.

## Tuning $\lambda$: the mismatch penalty and what significance means

$\lambda$ is not a free parameter: given the scoring scheme, it is pinned down as the unique positive
solution of

$$\sum_{i,j} p_i r_j e^{\lambda s_{ij}} = 1,$$

where $p_i$ is the frequency of nucleotide $i$ in the query, $r_j$ the frequency of nucleotide $j$ in
the subject, and $s_{ij}$ the score for aligning an $i,j$ pair. The slide also names
$q_{ij} = p_i r_j e^{\lambda s_{ij}}$ the **target frequencies** — the composition of aligned pairs the
scoring scheme is implicitly tuned to reward, as opposed to the background frequency $p_i r_j$ two
unrelated sequences would produce by chance. (This is the same idea that resurfaces below as "every
scoring matrix encodes an evolutionary model.")

One concrete design question: given that you want to detect alignments with expected identity
fraction $r$, what mismatch penalty $m$ should you use?

$$m = \ln\!\big(4(1-r)/3\big)\,/\,\ln(4r)$$

| $r$ | 0.75 | 0.95 | 0.99 |
|---|---|---|---|
| $m$ | $-1$ | $-2$ | $-3$ |

So why is $m = -3$ better for finding matches at 99% identity? Not because $m=-1$ makes such matches
impossible to find — a 99%-identical alignment can still score well with a $-1$ mismatch penalty.
What changes is $\lambda$: a harsher mismatch penalty increases $\lambda$, and since the significance
threshold $x$ shrinks as $\lambda$ grows (from the formula above, a larger $\lambda$ means a smaller
$x$ is already deep in the tail), a *shorter* alignment becomes statistically significant. The slide
then asks, without answering it: so why would you ever want to use $m=-1$? The natural completion of
the same trade-off is that a harsh penalty that is efficient for near-identical matches is
correspondingly unforgiving of a real but more divergent homolog — but the deck leaves this as an open
question rather than stating it.

## A short aside: measuring efficiency

Algorithms are compared by CPU time and memory, using **big-O notation**: the number of elementary
computations required as a function of the number of "units" in the problem (base pairs, residues).
This is usually the asymptotic worst-case running time, though sometimes it is simpler just to run
the experiment and measure. An algorithm whose cost scales as the square of the input size is
$O(n^2)$, an "order $n$-squared" algorithm.

## Six-frame translation, and the BLAST family

A nucleotide query can be compared against a protein database (or vice versa) by translating it in
all three reading frames on both strands and searching the resulting peptides — six frames in all.
For the same query sequence as above, the three forward frames read:

```
t t g a c c t a g a t g a g a t g t c g t t c a c t t t t a c t g a g c t a c a g a a a a
```

```
ttg|acc|tag|atg|aga|tgt|cgt|tca|ctt|tta|ctg|agc|tac|aga|aaa
 L   T   x   M   R   C   R   S   L   L   L   S   Y   R   K
```

```
t|tga|cct|aga|tga|gat|gtc|gtt|cac|ttt|tac|tga|gct|aca|gaa|aa
   x   P   R   x   D   V   V   H   F   Y   x   S   T   E
```

```
tt|gac|cta|gat|gag|atg|tcg|ttc|act|ttt|act|gag|cta|cag|aaa|a
    D   L   D   E   M   S   F   T   F   T   E   L   Q   K
```

and the complementary strand supplies three more. This is the logic behind the family of BLAST
programs, distinguished by what is translated on which side:

| Program | Query | Database |
|---|---|---|
| BLASTP | aa | aa |
| BLASTN | nt | nt |
| BLASTX | nt ($\Rightarrow$ aa) | aa |
| TBLASTN | aa | nt ($\Rightarrow$ aa) |
| TBLASTX | nt ($\Rightarrow$ aa) | nt ($\Rightarrow$ aa) |
| PsiBLAST | aa (aa multiple alignment) | aa |

The slide poses, without answering, which of these would be best for searching ESTs against a genome
— left as a question for the reader rather than resolved on the slide.

## Why align protein sequences at all?

The payoff is functional prediction: if a protein is homologous to one of known function, that
function is a reasonable prediction for the new one, because sequence similarity is taken to imply
similarity of function and/or structure. That assumption is almost always safe above about 30%
sequence identity; between 20% and 30% is what the slide calls "the twilight zone." But the logic
only runs one way. Function is carried out by the folded, three-dimensional protein, while what an
alignment can directly measure — sequence conservation — lives at the level of the one-dimensional
sequence. **The converse fails**: structural similarity does not imply sequence similarity, or even
common ancestry.

Three examples make the point:

- Hummingbirds and hawk moths both fly with wings that converge on a similar shape, despite a last
  common ancestor, more than 500 million years ago, that had no wings (and probably no legs or eyes).
  The same thing happens to proteins: similar structures can arise with no significant similarity of
  sequence.
- The Fe$^{3+}$-binding protein of *Haemophilus influenzae* and eukaryotic lactoferrin are
  structurally convergent, with a last common ancestor, more than two billion years ago, that is
  inferred only to have bound anions (Bruns et al., *Nature Structural Biology*, 1997).
- *Thermotoga maritima*'s ribosome recycling factor (RRF, a protein) mimics the shape of yeast
  tRNA$^{\text{Phe}}$ closely enough to occupy the same ribosomal site — and a protein and an RNA are
  unlikely to ever have shared a molecular ancestor at all (Selmer et al., *Science*, 1999).

So sequence alignment is doing real work precisely because structural similarity by itself proves
nothing about sequence, and the reverse inference (sequence similarity to structure/function) has to
be justified statistically rather than assumed.

## Alignment types and gap penalties

Alignments vary along two independent axes: **scope** — local, global, or semiglobal — and
**scoring system** — ungapped, or gapped with either a linear or an affine gap penalty. A dot-matrix
plot is a quick way to see, before computing anything, which scope a pair of sequences calls for:

<figure>
<svg viewBox="0 0 340 190" role="img" aria-label="Two dot-matrix plots: one with a near-complete diagonal suited to global alignment, one with a short diagonal segment amid scatter suited to local alignment">
  <line x1="20" y1="20" x2="20" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="20" y1="150" x2="150" y2="150" stroke="currentColor" stroke-width="1"/>
  <text x="85" y="168" text-anchor="middle" font-size="11" fill="currentColor">sequence 1</text>
  <text x="8" y="90" text-anchor="middle" font-size="11" fill="currentColor" transform="rotate(-90 8 90)">sequence 2</text>
  <line x1="20" y1="150" x2="70" y2="100" stroke="currentColor" stroke-width="1.6"/>
  <line x1="70" y1="100" x2="70" y2="85" stroke="currentColor" stroke-width="1.6"/>
  <line x1="70" y1="85" x2="120" y2="35" stroke="currentColor" stroke-width="1.6"/>
  <line x1="120" y1="35" x2="135" y2="35" stroke="currentColor" stroke-width="1.6"/>
  <line x1="135" y1="35" x2="150" y2="20" stroke="currentColor" stroke-width="1.6"/>
  <text x="85" y="185" text-anchor="middle" font-size="12" fill="currentColor">appropriate: global</text>
  <line x1="200" y1="20" x2="200" y2="150" stroke="currentColor" stroke-width="1"/>
  <line x1="200" y1="150" x2="330" y2="150" stroke="currentColor" stroke-width="1"/>
  <text x="265" y="168" text-anchor="middle" font-size="11" fill="currentColor">sequence 1</text>
  <circle cx="215" cy="40" r="1.4" fill="currentColor"/>
  <circle cx="240" cy="120" r="1.4" fill="currentColor"/>
  <circle cx="310" cy="45" r="1.4" fill="currentColor"/>
  <circle cx="225" cy="100" r="1.4" fill="currentColor"/>
  <circle cx="300" cy="130" r="1.4" fill="currentColor"/>
  <circle cx="255" cy="60" r="1.4" fill="currentColor"/>
  <circle cx="280" cy="35" r="1.4" fill="currentColor"/>
  <circle cx="235" cy="140" r="1.4" fill="currentColor"/>
  <line x1="245" y1="95" x2="285" y2="55" stroke="currentColor" stroke-width="1.6"/>
  <text x="265" y="185" text-anchor="middle" font-size="12" fill="currentColor">appropriate: local</text>
</svg>
<figcaption>A dot-matrix plot puts a mark at $(i,j)$ when position $i$ of sequence 1 matches position $j$
of sequence 2. A run of matches shows up as a diagonal run of dots; a step sideways or down is an
indel. Left: the two sequences line up almost end to end, with two short offsets — a global alignment.
Right: only a short stretch lines up, surrounded by unrelated positions — a local alignment.</figcaption>
</figure>

A gap (an "indel") is a run of $n$ inserted or deleted positions, for example

```
AKHFRGCVS
AKKF--CVG
```

Under a **linear** gap penalty, a run of $n$ gaps costs $\gamma(n) = nA$ for a fixed per-gap penalty
$A$. Under an **affine** penalty, opening a gap and extending it cost different amounts:

$$W_n = G + n\gamma$$

(or, with the alternative convention that $G$ already includes the first position of the gap,
$W_n = G + (n-1)\gamma$), where $G$ is the gap-opening penalty and $\gamma$ the (smaller) per-position
extension penalty. This is the standard way to make a single long gap cheaper than the same number of
residues spread over many short gaps — which is usually the biologically more plausible event.

## Computing a global alignment: dynamic programming (Needleman–Wunsch)

Write one sequence across the top of a matrix and the other down the side, with an extra leading row
and column for "all gap." The slide's own worked start looks like this (linear gap penalty
$\gamma(n) = nA$ with $A$ a negative number):

| | Gap | V | D | S | C | Y |
|---|---|---|---|---|---|---|
| **Gap** | 0 | 1 gap | 2 gaps | $\cdots$ | | |
| **V** | 1 gap | | | | | |
| **E** | 2 gaps | | | | | |
| **S** | $\vdots$ | | | | | |
| **L** | | | | | | |
| **C** | | | | | | |
| **Y** | | | | | | |

The border cells are already the whole idea in miniature: aligning a length-$k$ prefix of one
sequence entirely against gaps costs $k$ gap penalties, so row 0 and column 0 are just the running sum
$0, A, 2A, 3A, \dots$. The reconstruction of this slide breaks off at exactly this point — the
initialization is shown but the general fill rule is not legible in the source. What it is building
toward is the standard **Needleman–Wunsch recurrence**: having filled in every cell above and to the
left of $(i,j)$, the best score for aligning the length-$i$ and length-$j$ prefixes is

$$F(i,j) = \max \begin{cases} F(i-1,j-1) + s(x_i, y_j) & \text{align } x_i \text{ with } y_j \\ F(i-1,j) + \gamma & \text{gap in } y \\ F(i,j-1) + \gamma & \text{gap in } x \end{cases}$$

filled row by row (or column by column), with the optimal global alignment read off by tracing the
choice made at each cell back from the bottom-right corner to the top-left. A **local** alignment
(Smith–Waterman, named on the lecture's title slide but not developed further in this deck) uses the
same recurrence with one change: a fourth option, $0$, is added inside the max, and the traceback
starts from the highest-scoring cell anywhere in the matrix rather than the corner. That "floor the
score at zero" rule is exactly the reset described in the bank-queue problem above — the score is not
allowed to accumulate a negative debt, since a local alignment can always choose to start over.

## Substitution matrices carry an evolutionary model

Whatever else it does, any scoring system for an alignment brings an implicit model of evolution with
it: a run of matches scores well because matches are assumed more likely between related sequences
than chance would predict, and the specific mismatch scores encode which substitutions are treated as
more or less costly. The PAM matrices make this model explicit instead of implicit.

## PAM matrices (Dayhoff, 1978)

Margaret Dayhoff's PAM (**P**oint **A**ccepted **M**utation) matrices are built on an explicit
evolutionary model, with two stated assumptions: that substitution is symmetric ($A \to B$ is as
likely as $B \to A$), and that substitution rates measured over short evolutionary distances can be
extrapolated to long ones. The original data: 71 groups of protein sequences, each at least 85%
similar internally, yielding 1572 observed amino-acid changes — changes that survived natural
selection acting on a functional protein, i.e. "accepted" mutations.

**PAM1** is defined as one accepted change per 100 residues — 1% divergence between two sequences.
Equivalently (and this is how some texts restate it), it is the matrix under which the probability of
any given residue changing to another over that evolutionary distance is about 1%, and the probability
of no change is about 99%.

Building it starts by tallying raw substitution counts across confidently-aligned, closely related
sequences — for instance a column like

$$\begin{aligned}
\dots \text{GDS}&\mathbf{F}\text{H}\mathbf{Y}\text{FVS}\mathbf{HG}\dots \\
\dots \text{GDS}&\mathbf{F}\text{H}\mathbf{Y}\mathbf{Y}\text{VS}\mathbf{FG}\dots \\
\dots \text{GDS}&\mathbf{Y}\text{H}\mathbf{Y}\text{FVS}\mathbf{FG}\dots \\
\dots \text{GDS}&\mathbf{F}\text{H}\mathbf{Y}\text{FVS}\mathbf{FG}\dots \\
\dots \text{GDS}&\mathbf{F}\text{H}\mathbf{F}\mathbf{F}\text{VS}\mathbf{FG}\dots
\end{aligned}$$

where, across many such families, 900 phenylalanines (F) stayed F while 100 became something else —
80 to tyrosine (Y), 3 to tryptophan (W), 2 to histidine (H), and so on. Written as raw counts
$n_{ab}$: $n_{YF} = 80$, $n_{WF} = 3$. These counts, once turned into rates and normalized, are the
raw material for the PAM1 matrix; longer evolutionary distances (PAM250, etc.) are then meant to be
obtained by extrapolating — composing PAM1 with itself. That composition step is exactly where the
second Dayhoff assumption above needs to be a genuine mathematical property of the substitution
process, not just a convenient approximation — which is the reason the lecture turns to Markov chains
next.

## From generations to Markov chains

The slide illustrates the same point with a three-generation family tree of a DNA sequence — a
grandparent, a parent (one substitution different from the grandparent), and a child (a further
substitution different from the parent):

```
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTACGCCTAGCCCATGCGA 3'   (grandparent)
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCATGCGA 3'   (parent)
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCGTGCGA 3'   (child)
```

Whether the child differs from the parent does not depend on how the parent came to differ from the
grandparent — only on the parent's sequence itself. That is precisely the property Dayhoff's
extrapolation assumption needs, and the lecture closes by naming it formally.

A discrete stochastic process $X_1, X_2, X_3, \dots$ — a sequence of random variables — has the
**Markov property** if

$$P(X_{n+1} = j \mid X_1 = x_1, X_2 = x_2, \dots, X_n = x_n) = P(X_{n+1} = j \mid X_n = x_n)$$

for all states $x_i$, all $j$, and all $n$. In words: the future is conditionally independent of the
past, given the present. A process with this property is a **Markov chain** (or Markov model), named
for the Russian mathematician Andrey Markov (1856–1922). The deck ends immediately after this
definition; the machinery it sets up is presumably what the next lecture uses to justify composing
short-range substitution rates into long-range ones.

## Exercises

The problems below are drawn from Problem Set 3 (due Thursday, 3 April). Most of that set concerns
material from later lectures (the Gibbs sampler, Nussinov RNA-structure prediction, and PyRosetta —
covered around lecture 11 and after) and is not reproduced here since it does not belong to this
lecture. One "connections" problem, however, draws directly on the statistics developed above.

**Queuing theory and BLAST statistics.** A small bank hires a consultant to work out whether it can
afford to offer a year of free checking (worth \$150) to any customer who has to wait in line more
than 15 minutes. Each minute the bank is open, the line grows by one customer with probability
$\tfrac14$, and — if there is a line — shrinks by one customer with probability $\tfrac34$. The bank
is open 2400 minutes a week. Let $X$ be the probability that, over a 12-week period, the line never
exceeds 10 people (a reference case whose empirical frequency the bank already knows), and let $Y$ be
the probability that, over the same period, it never exceeds 15 people (the proposed length of the
promotion). Using an equation covered in this lecture, find $\dfrac{\ln(X)}{\ln(Y)}$.

## Sources

- Slide deck: `lectures/03-slides.md` (ocw-7091j, 7.91J/20.490J/6.874J/HST.506, Lecture 3, C. Burge,
  11 Feb 2014), reconstructed by a model from a PDF with no text layer — every equation in it is
  flagged unverified in the source, and the dynamic-programming matrix slides are visibly truncated
  in the reconstruction. No transcript or notes were supplied for this lecture.
- Cited within the deck: Karlin, S. & Altschul, S.F. (1990) for the extreme-value statistics of local
  alignment; Bruns, C.M., Nowalk, A.J. et al., *Nature Structural & Molecular Biology* 4(11), 1997,
  for the Fe$^{3+}$-binding protein comparison; Selmer, M., Al-Karadaghi, S. et al., *Science*
  286(5448), 1999, for the ribosome-recycling-factor/tRNA comparison; PMID 19213877 for one of the
  library-prep adapter methods. None of these were separately supplied and are named only as the
  lecture named them.
- Exercise: `psets/03-questions.md`, Problem Set 3, Q4 ("Queuing theory/connections"), with the
  solution stripped out.
- Also supplied for this task but not used, because they belong to later lectures and do not overlap
  this one's content: the rest of Problem Set 3 (P1 Gibbs sampler, P2 RNA secondary structure via the
  Nussinov algorithm and mfold — explicitly tied to "Lecture 11" in its own text, P3 PyRosetta protein
  structure), and the recitation slides dated 2014-03-05, 2014-03-07, 2014-03-12, and 2014-03-19
  (covering negative-binomial dispersion, PCA, sequence motifs and information content, and RNA
  secondary structure — recitations for lectures 7 through 10, well after this one).

---

[← 2. Local Alignment (BLAST) and Statistics](02-local-alignment-blast-and-statistics.md) · [Contents](index.md) · [4. Markov Chains and CRISPR Genomics →](04-markov-chains-and-crispr-genomics.md)
