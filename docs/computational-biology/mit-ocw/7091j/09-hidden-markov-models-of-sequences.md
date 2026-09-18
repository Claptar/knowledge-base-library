---
title: "9. Hidden Markov Models of Sequences"
course: "MIT 7.091J"
chapter: 9
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Hidden Markov Models of Sequences

## What this covers

This chapter picks up a lecture on scoring DNA motifs and carries it into hidden Markov models
(HMMs). It first finishes the motif-scoring material — relative entropy as a measure of
information, position-specific probability matrices, the move from treating positions as
independent to modelling them as a Markov chain, and the pseudocount fix for small training sets —
then introduces HMMs from scratch through the CpG-island example and the Viterbi algorithm for
decoding a hidden state sequence. It assumes Shannon entropy, conditional probability and Bayes'
rule, and (for the opening section) the position-weight-matrix picture of a motif from the
preceding lecture. It does **not** cover the Gibbs sampling algorithm for motif discovery or
TMHMM in any detail — both are named on the slides as topics but not worked through in this
lecture.

## Relative entropy: a better measure of information than entropy alone

For a motif with observed base frequencies $p$ at some position, and a background distribution
$q$, the **relative entropy** (also called Kullback–Leibler divergence, or "information for
discrimination") is

$$D(p\|q) = \sum_{k=1}^{n} p_k \log_2\!\left(\frac{p_k}{q_k}\right),$$

read as a mean bit-score: on average, how many bits of information does observing a base drawn
from $p$ give you for distinguishing $p$ from $q$. When the background is uniform, $q_k = 1/4^w$
for a motif of width $w$, this collapses to the more familiar information-content formula

$$\text{RelEnt} = 2w - H_{\text{motif}} = I_{\text{motif}},$$

i.e. the number of bits "saved" relative to a maximally uncertain background. But relative entropy
is the more general and more honest quantity: it measures **information**, not entropy, and in
general it is *not* the same thing as $H_{\text{before}} - H_{\text{after}}$. It is the better
choice whenever the background itself is not uniform.

The point is sharpest with a background that is skewed. Take $q_A = q_T = 3/8$, $q_C = q_G = 1/8$
— an AT-rich background, as in much real genomic sequence — and suppose a motif position is
completely conserved, $p_C = 1$. The entropy drop $H(q) - H(p)$ is less than 2 bits, because $H(q)$
itself is already less than 2 bits (it's the entropy of a skewed four-letter distribution). But the
relative entropy only has one non-zero term, from $k=C$:

$$D(p\|q) = \log_2\!\left(\frac{1}{1/8}\right) = 3 \text{ bits}.$$

Relative entropy says this position is *more* informative than a plain entropy comparison would
suggest, because it correctly credits how rare C already is in this background — seeing C every
single time is much more surprising against an AT-rich background than the entropy difference
alone reflects. That is the sense in which $D(p\|q)$, not $H(q)-H(p)$, is "the" measure of
information here.

## Position-specific probability matrices, and their independence assumption

A **position-specific probability matrix** (PSPM) records, position by position across a motif,
the probability of each base. The lecture's running example is the human 5' splice site, scored
over positions $-3$ to $+6$ (position $0$ is the exon/intron boundary itself and is not part of
the matrix):

| Pos | -3 | -2 | -1 | +1 | +2 | +3 | +4 | +5 | +6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A | 0.3 | 0.6 | 0.1 | 0.0 | 0.0 | 0.4 | 0.7 | 0.1 | 0.1 |
| C | 0.4 | 0.1 | 0.0 | 0.0 | 0.0 | 0.1 | 0.1 | 0.1 | 0.2 |
| G | 0.2 | 0.2 | 0.8 | 1.0 | 0.0 | 0.4 | 0.1 | 0.8 | 0.2 |
| T | 0.1 | 0.1 | 0.1 | 0.0 | 1.0 | 0.1 | 0.1 | 0.0 | 0.5 |

The nearly-fixed G at $+1$ and T at $+2$ are the canonical "GT" of the splice donor site. To score a
candidate sequence $S = S_1 S_2 \cdots S_9$ against this matrix, multiply the position-specific
probabilities of the bases actually observed:

$$P(S\mid +) = P_{-3}(S_1)\,P_{-2}(S_2)\,P_{-1}(S_3)\cdots P_5(S_8)\,P_6(S_9).$$

For the example sequence **TAGGTCAGT**, reading off the matrix entry for the base at each
position (T at $-3$: 0.1, A at $-2$: 0.6, G at $-1$: 0.8, G at $+1$: 1.0, T at $+2$: 1.0, C at
$+3$: 0.1, A at $+4$: 0.7, G at $+5$: 0.8, T at $+6$: 0.5) gives

$$P(S\mid+) = 0.1 \times 0.6 \times 0.8 \times 1.0 \times 1.0 \times 0.1 \times 0.7 \times 0.8
\times 0.5 \approx 0.00134.$$

This kind of matrix is called **inhomogeneous**, because the probability distribution changes from
position to position — but it still treats positions as *independent*: the base at $+3$ contributes
its own factor to the product regardless of what appeared at $+2$. The natural next question, which
the lecture poses directly: what if that is not true?

## Allowing dependence: the inhomogeneous first-order Markov model

Drop the independence assumption and let the base at each position depend on the base at the
previous position. The transition probability

$$P_{-2}(A\mid C) = \frac{N_{CA}^{(-3,-2)}}{N_C^{(-3)}}$$

is estimated directly from a training set: among sequences with C at position $-3$, what fraction
have A at position $-2$. Chaining these along the motif, $-3 \to -2 \to -1 \to 1 \to 2 \to \cdots
\to 6$, the scoring formula for the "true site" model becomes a first-order Markov chain rather
than a product of independent terms:

$$P(S\mid+) = P_{-3}(S_1)\,P_{-2}(S_2\mid S_1)\,P_{-1}(S_3\mid S_2)\cdots P_6(S_9\mid S_8).$$

To decide whether a candidate site is real, this is compared against a **decoy** model — the same
kind of chain, but with a single, position-independent (**homogeneous**) set of transition
probabilities estimated from background sequence:

$$P(S\mid-) = P_{bg}(S_1)\,P_{bg}(S_2\mid S_1)\,P_{bg}(S_3\mid S_2)\cdots P_{bg}(S_9\mid S_8).$$

The discrimination score is the log-odds ratio of the two models:

$$R = \frac{P(S\mid+)}{P(S\mid-)}, \qquad s = \log_2 R.$$

Comparing scores from the plain (independent-position) weight matrix model against the
first-order Markov model on true versus decoy human 5' splice sites, the Markov model separates
the two populations better — the same effect Zhou & Liu (*Bioinformatics*, 2004) report for
transcriptional motifs.

## Parameter estimation, and the cost of going to higher order

The same idea generalizes to a **$k$-th order Markov model**: the base at each position depends on
the previous $k$ bases. The cost is in the number of parameters: a $k$-th order model needs on the
order of $4^{k+1}$ parameters per position (one distribution over 4 bases for each of $4^k$
possible contexts of length $k$). Going from order 0 (independent positions) to order 1 to order 2
buys more discriminating power at the price of a rapidly growing number of parameters to estimate
— and every one of them has to be estimated from a finite training set.

## Limited training data, and pseudocounts

That last point has a sharp illustration. Suppose the true frequency of T at some position is
genuinely 10%, and ten training sequences are collected. What is the probability of not seeing a
single T?

$$P(N=0) = \binom{10}{0}(0.1)^0(0.9)^{10} \approx 35\%.$$

More than a third of the time, a real 10%-frequency base would be estimated, from ten sequences, as
having probability exactly zero — which is disastrous for a probabilistic model, since it means any
future sequence containing that base at that position gets scored with probability zero no matter
how well it matches everywhere else. The fix is to add a **pseudocount** ($\Psi$count) to every
observed count before normalizing, so that no outcome is ever assigned probability exactly zero
just because it happened not to appear in a small sample. With ten sequences observed as A:8, C:1,
G:1, T:0, and a pseudocount of $+1$ added to each:

| Nt | Count | $\Psi$count | Bayes count | ML est. | Bayes est. |
| :---: | :---: | :---: | :---: | :---: | :---: |
| A | 8 | +1 | 9 | 0.80 | 0.64 |
| C | 1 | +1 | 2 | 0.10 | 0.14 |
| G | 1 | +1 | 2 | 0.10 | 0.14 |
| T | 0 | +1 | 1 | 0.00 | 0.07 |
| | 10 | | 14 | 1.00 | 1.00 |

The **ML** (maximum-likelihood) estimate is just the raw observed frequency; the **Bayes estimate**
is the count-plus-pseudocount normalized, which is the posterior mean under a Dirichlet prior whose
parameters are the pseudocounts. Adding pseudocounts is exactly a Bayesian move: instead of
trusting ten observations completely, it blends them with a weak prior belief that all four bases
are possible.

## Hidden Markov models: motivation

A Markov chain models a sequence of states where each state depends only on the one before it. A
**hidden Markov model** (HMM) adds one more layer: the state sequence itself is not observed
directly — only some signal that depends probabilistically on the state is.

The lecture's example is a pedigree. Genotype at the Apolipoprotein locus (alleles A and a),
tracked down a lineage — Grandpa Simpson (past) $\to$ Grandma Simpson $\to$ Homer (present) $\to$
Marge $\to$ Bart (future) — is an ordinary, fully-observed Markov chain: each generation's genotype
depends only on the parent's genotype (Mendelian inheritance), so

$$P(\text{Bart} = a/a \mid \text{Grandpa} = A/a,\ \text{Homer} = a/a) = P(\text{Bart} = a/a \mid
\text{Homer} = a/a).$$

Bart's genotype is conditionally independent of Grandpa's, given Homer's — the defining property of
a Markov chain.

Now suppose genotype cannot be observed directly, and all that is measured is a phenotype that
depends on it probabilistically — say, LDL cholesterol:

| | Genotype (hidden) | Phenotype — LDL cholesterol (observed) |
| :--- | :---: | :---: |
| Grandpa Simpson | $A/a$ | 150 |
| Homer | $a/a$ | 250 |
| Bart | $a/a$ | 200 |

The genotype sequence is still a Markov chain, but it is now **hidden**; only the phenotype, which
depends probabilistically on the hidden state at each generation, is observed. That is a hidden
Markov model.

HMMs were developed in electrical engineering, originally for speech recognition (see Rabiner's
tutorial), and generalize far beyond pedigrees: they give a foundation for **sequence labeling**
problems — assigning a hidden label to every position along an observed sequence — and can be
specified just by drawing the state graph, which is why they've been called "the Legos of
computational sequence analysis." Bacterial gene finding is a sequence-labeling problem in exactly
this sense: label each base of a genome as inside or outside an open reading frame,

$$\text{Start} \to \text{ORF} \to \text{Stop},$$

...accgatattcaaccatggagagtttatccggtatagtcgcccctaaataccgtagaccttgagagactgactcatgacgtagtcttacgg...

with the hidden labeling (which stretches are genes, which are intergenic) inferred from the
observed nucleotide sequence alone.

## Terminology, and the HMM as a generator

Following Rabiner's notation: an HMM has a set of hidden **states**, an **initial state
distribution** $\pi$, a **transition probability** $a_{ij}$ (probability of moving from state $i$
to state $j$), and, for each state, an **emission probability** $b_i(k)$ (probability that state
$i$ emits observable symbol $k$). It is helpful to think of the HMM as a machine that *generates*
an observation sequence $O = O_1 O_2 \cdots O_T$:

1. Choose an initial state $q_1 = S_i$ according to $\pi$.
2. Set $t = 1$.
3. Choose $O_t = v_k$ according to the emission distribution of the current state, $b_i(k)$.
4. Move to a new state $q_{t+1} = S_j$ according to the transition distribution of the current
   state, $a_{ij}$.
5. Set $t = t+1$; return to step 3 if $t < T$, otherwise stop.

The states are never seen; only the sequence of symbols they emit is.

## Worked example: the CpG-island HMM

**CpG islands** are regions of high C+G content, with relatively high abundance of the CpG
dinucleotide — normally rare elsewhere in the genome — that are unmethylated; they are found at the
promoters of roughly half of human genes. Modeled as an HMM, the hidden states are just "Genome"
and "Island," and the observable at each position is the base itself (A, C, G, or T). One
parameterization used in the lecture (Rabiner notation):

- Initiation probabilities: $\pi_{\text{genome}} = 0.99$, $\pi_{\text{island}} = 0.01$.
- Transition probabilities: $a_{gg} = 0.99999$, $a_{gi} = 0.00001$, $a_{ig} = 0.001$,
  $a_{ii} = 0.999$.
- Emission probabilities:

| | C | G | A | T |
| :--- | :---: | :---: | :---: | :---: |
| **Island** | 0.3 | 0.3 | 0.2 | 0.2 |
| **Genome** | 0.2 | 0.2 | 0.3 | 0.3 |

Islands are entered only very rarely from ordinary genome ($a_{gi}=0.00001$), and the model starts
in Genome the overwhelming majority of the time ($\pi_{\text{genome}} = 0.99$); but once in an
island, C and G are 1.5 times as likely per base as in ordinary genome ($0.3/0.2 = 1.5$), which is
the whole discriminating signal available to detect one.

<figure>
<svg viewBox="0 0 420 220" role="img" aria-label="Two-state hidden Markov chain switching between Genome and Island, with transition probabilities on each arrow">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0 0, 8 4, 0 8" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="120" cy="130" r="50" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="120" y="126" text-anchor="middle" font-size="13" fill="currentColor">Genome</text>
  <text x="120" y="143" text-anchor="middle" font-size="11" fill="currentColor">C,G: 0.2 each</text>

  <circle cx="320" cy="130" r="50" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="320" y="126" text-anchor="middle" font-size="13" fill="currentColor">Island</text>
  <text x="320" y="143" text-anchor="middle" font-size="11" fill="currentColor">C,G: 0.3 each</text>

  <path d="M 95 85 A 28 28 0 1 1 145 85" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="120" y="45" text-anchor="middle" font-size="11" fill="currentColor">a_gg = 0.99999</text>

  <path d="M 295 85 A 28 28 0 1 1 345 85" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="320" y="45" text-anchor="middle" font-size="11" fill="currentColor">a_ii = 0.999</text>

  <line x1="172" y1="112" x2="268" y2="112" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="220" y="103" text-anchor="middle" font-size="11" fill="currentColor">a_gi = 0.00001</text>

  <line x1="268" y1="155" x2="172" y2="155" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <text x="220" y="175" text-anchor="middle" font-size="11" fill="currentColor">a_ig = 0.001</text>
</svg>
<figcaption>The CpG-island HMM: a hidden two-state chain that emits a base at every step. Islands
are rarely entered from genome but, once entered, are richer in C and G; only the emitted
sequence is observed, never the state itself.</figcaption>
</figure>

Given only an observed sequence such as **A C T C G A G T A**, the task is to infer which stretches
were most likely generated by the Island state and which by the Genome state — but the model as
written runs in the wrong direction: it says how states generate observations, not how to read
states off from observations.

## Reversing the conditioning: Bayes' rule

To go from "observable given hidden" to "hidden given observable," invoke the definition of
conditional probability, $P(A\mid B) = P(A,B)/P(B)$, twice — this is exactly Bayes' rule:

$$P(B\mid A) = \frac{P(B)\,P(A\mid B)}{P(A)}, \qquad
P(B_i \mid A) = \frac{P(B_i)\,P(A\mid B_i)}{\sum_k P(B_k)\,P(A \mid B_k)}.$$

Write $H = (h_1,\ldots,h_n)$ for the hidden state sequence and $O = (o_1,\ldots,o_n)$ for the
observed sequence. Then

$$P(H=h_1,\ldots,h_n \mid O=o_1,\ldots,o_n)
= \frac{P(H=h_1,\ldots,h_n,\ O=o_1,\ldots,o_n)}{P(O=o_1,\ldots,o_n)}
= \frac{P(H=h_1,\ldots,h_n)\,P(O=o_1,\ldots,o_n \mid H=h_1,\ldots,h_n)}{P(O=o_1,\ldots,o_n)}.$$

The denominator $P(O = o_1,\ldots,o_n)$ is awkward to compute directly, but it is the same number
for every candidate hidden sequence $h_1,\ldots,h_n$ — it doesn't depend on which hidden sequence is
being tested. So finding the *most likely* hidden sequence never requires computing it: it's enough
to maximize the joint probability $P(H=h_1,\ldots,h_n,\ O=o_1,\ldots,o_n)$ over choices of the
hidden sequence.

## The Viterbi algorithm

The problem is now: find the hidden sequence $H^{opt} = h_1^{opt}, h_2^{opt}, \ldots$ that
maximizes the joint probability $P(H=h_1,\ldots,h_n,\ O=o_1,\ldots,o_n)$ — the **optimal parse** of
the observed sequence. Searching over all $N^T$ possible hidden sequences directly is hopeless for
any realistic $T$. The trick is to solve it **recursively**.

Define $\delta_t(i)$ as the probability of the best (highest-probability) path through the hidden
states, ending in state $i$ at time $t$, that accounts for the first $t$ observations — and
$\psi_t(i)$ as the state at $t-1$ that path passed through. The key observation that makes a
recursion possible: the best path ending in state $j$ at time $t$ must consist of the best path to
*some* state $i$ at time $t-1$, followed by the transition $i \to j$ and the emission of $O_t$ from
$j$ — so $\delta_t(j)$ can be built directly out of the $\delta_{t-1}(i)$ values already computed.
Writing $N$ for the number of hidden states and $T$ for the sequence length, the algorithm
(Rabiner, 1989) is:

1. **Initialization:**
   $$\delta_1(i) = \pi_i\, b_i(O_1), \qquad \psi_1(i) = 0, \qquad 1 \le i \le N.$$
2. **Recursion**, for $2 \le t \le T$, $1 \le j \le N$:
   $$\delta_t(j) = \max_{1 \le i \le N} \big[\delta_{t-1}(i)\, a_{ij}\big]\, b_j(O_t), \qquad
   \psi_t(j) = \operatorname*{argmax}_{1 \le i \le N} \big[\delta_{t-1}(i)\, a_{ij}\big].$$
3. **Termination:**
   $$P^* = \max_{1 \le i \le N} \delta_T(i), \qquad q_T^* = \operatorname*{argmax}_{1 \le i \le N}
   \delta_T(i).$$
4. **Backtracking**, for $t = T-1, T-2, \ldots, 1$:
   $$q_t^* = \psi_{t+1}(q_{t+1}^*).$$

Each step only ever looks at the $N$ values $\delta_{t-1}(\cdot)$ computed at the previous
position, so the whole computation for a $k$-state HMM on a sequence of length $L$ costs
$O(k^2 L)$ — linear in the sequence length, rather than exponential. That efficiency, more than
anything else, is why HMMs became and remain popular for sequence analysis.

(The algorithm is named for Andrew Viterbi, who was an MIT bachelor's/master's student in
electrical engineering before going on to found Qualcomm.)

## Exercises

The following are the lecture's own worked prompts, given with the CpG-island HMM parameterized
above; none is solved here.

1. Using the Viterbi recursion, find the optimal (most likely) hidden state path for the observed
   sequence **ACG** under the CpG-island HMM. Work out $\delta_t(i)$ and $\psi_t(i)$ at each
   position and backtrack to recover the path.

2. What is the optimal parse of $(\text{ACGT})_{10000}$ (the four-base pattern ACGT repeated ten
   thousand times) under the same HMM?

3. What is the optimal parse of
   $\text{A}_{1000}\text{C}_{80}\text{T}_{1000}\text{C}_{20}\text{A}_{1000}\text{G}_{60}\text{T}_{1000}$
   (runs of the indicated base, of the indicated length, concatenated in that order)? As a hint
   toward reasoning about how long a run of C's or G's it takes before the model prefers to switch
   into the Island state and back, note that $C$ and $G$ are each 1.5 times as likely under Island
   as under Genome, and

   | $N=$ | 20 | 40 | 60 | 80 |
   | :--- | :---: | :---: | :---: | :---: |
   | $(1.5)^N=$ | $3\times10^3$ | $1\times10^7$ | $3\times10^{10}$ | $1\times10^{14}$ |

## Sources

All material is from a single input: the slide deck for MIT 7.91J/20.490J/6.874J/HST.506J
"Foundations of Computational and Systems Biology," Spring 2014, Lecture 10, "Markov & Hidden
Markov Models of Genomic & Protein Features," C. Burge, March 11, 2014 —
`docs/computational-biology/mit-ocw/7091j/lectures/10-slides.md` (converted from the source PDF by
a model; the deck's own header flags every equation as unverified against the original, and this
chapter inherits that caveat). No transcript, notes or exercise file was supplied for this lecture,
so the exposition follows the slide sequence directly rather than merging with spoken commentary;
figures embedded as page-images in the source file were not legible text and are not reproduced.

- Relative entropy, PSPM, the first-order Markov splice-site model, order-$k$ parameter counts and
  pseudocounts: slides "Relative Entropy," "Position-specific probability matrix (PSPM),"
  "Inhomogeneous 1st-Order Markov Model," "WMM vs 1st-order Markov Models of Human 5'ss,"
  "Estimating Parameters for a Markov Model," "Dealing With Limited Training Sets," and
  "Pseudocounts."
- HMM terminology, the generative-process list, and the Simpsons pedigree example: slides "Hidden
  Markov Models (HMMs)," "Markov Model Example," "Hidden Markov Model Example," "HMMs as
  Generative Models," and "'Sequence Labeling' Problems."
- The CpG-island HMM, Bayes' rule, and the Viterbi algorithm and its worked prompts: slides "CpG
  Islands," "CpG Island Hidden Markov Model," "CpG Island HMM," "Reversing the Conditioning
  (Bayes' Rule)," "Notation for HMM Calculations," "Inferring the Hidden from the Observable
  (Viterbi Algorithm)," "Viterbi Algorithm," "Viterbi Example," "More Viterbi Examples," and "Run
  time for k-state HMM."
- Administrative slides (midterm date, format and topic coverage) were stripped as lecture
  logistics, not course content.

Named but not contained in the supplied material, and not covered further in this chapter: the
Gibbs sampling algorithm for motif discovery (listed as a topic heading but not worked through in
this deck — presumably covered in the preceding lecture); TMHMM for transmembrane helices (named
as a forthcoming example only); Rabiner's "Tutorial on Hidden Markov Models and Selected
Applications in Speech Recognition" (cited as the source of the generative-process list and the
Viterbi algorithm as given); the NBT Primer on HMMs and Z&B Chapter 6 (background reading named
for this lecture); Zhou & Liu, *Bioinformatics* 2004 (cited for the claim that Markov models also
improve transcriptional-motif discrimination); and the appendix of Durbin, Eddy, Krogh & Mitchison,
*Biological Sequence Analysis*, together with the course's own "Probability and Statistics Primer,"
both named as further reading on pseudocounts and Bayesian estimation.

---

[← 8. Modeling & Discovery of Sequence Motifs](08-modeling-discovery-of-sequence-motifs.md) · [Contents](index.md) · [10. HMMs and RNA Secondary Structure →](10-hmms-and-rna-secondary-structure.md)
