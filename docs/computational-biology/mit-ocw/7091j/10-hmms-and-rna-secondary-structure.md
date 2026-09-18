---
title: "10. HMMs and RNA Secondary Structure"
course: "MIT 7.091J"
chapter: 10
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 10. HMMs and RNA Secondary Structure

## What this covers

This lecture does two things back to back. First it finishes a thread on hidden Markov models
(HMMs) applied to real sequence problems — a toy model for CpG islands, then two "real world" HMMs:
profile HMMs for sequence alignment with insertions and deletions, and TMHMM for predicting
transmembrane helices in proteins. Second it opens a new topic, RNA secondary structure: why it
matters biologically, and two ways to predict it computationally — from evolutionary covariation,
and from energy minimization. It assumes the reader already has the basic vocabulary of an HMM
(hidden states, transition and emission probabilities) and has seen the Viterbi algorithm introduced
as a way to decode the most likely state path; this chapter builds on that with worked examples
rather than re-deriving it.

## The trellis picture of decoding

Rabiner's notation for an HMM names three kinds of parameter: initiation probabilities $\pi_j$ (the
chance of starting in state $j$), transition probabilities $a_{ij}$ (the chance of moving from state
$i$ to state $j$ between one position and the next), and emission probabilities $b_j(k)$ (the chance
that state $j$ emits observed symbol $k$).

Laid out as a picture, a sequence of length $L$ becomes a grid: one column per position, one row per
hidden state, and an edge from every state at position $i$ to every state at position $i+1$ — the
"full set of possible transitions" between adjacent columns. A **parse** of the sequence is a single
path through this grid, choosing one state per column; the observed sequence itself sits underneath,
one symbol per column. The **Viterbi algorithm** is the dynamic program that finds the single
highest-probability path through this graph, without enumerating all of them: the best score at
position $i$ in state $j$ depends only on the best scores at position $i-1$, so the whole path can be
built up column by column.

<figure>
<svg viewBox="0 0 400 220" role="img" aria-label="Trellis of genome and island states with all transitions between adjacent sequence positions">
  <defs>
    <marker id="arrow10" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="12" y="54" font-size="12" fill="currentColor">G</text>
  <text x="12" y="144" font-size="12" fill="currentColor">I</text>
  <g stroke="currentColor" stroke-width="1" fill="none" opacity="0.85" marker-end="url(#arrow10)">
    <line x1="88" y1="50" x2="173" y2="50"/>
    <line x1="88" y1="53" x2="172" y2="136"/>
    <line x1="88" y1="137" x2="172" y2="54"/>
    <line x1="88" y1="140" x2="173" y2="140"/>
    <line x1="188" y1="50" x2="273" y2="50"/>
    <line x1="188" y1="53" x2="272" y2="136"/>
    <line x1="188" y1="137" x2="272" y2="54"/>
    <line x1="188" y1="140" x2="273" y2="140"/>
    <line x1="288" y1="50" x2="373" y2="50"/>
    <line x1="288" y1="53" x2="372" y2="136"/>
    <line x1="288" y1="137" x2="372" y2="54"/>
    <line x1="288" y1="140" x2="373" y2="140"/>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <circle cx="80" cy="50" r="9"/>
    <circle cx="180" cy="50" r="9"/>
    <circle cx="280" cy="50" r="9"/>
    <circle cx="380" cy="50" r="9"/>
    <circle cx="80" cy="140" r="9"/>
    <circle cx="180" cy="140" r="9"/>
    <circle cx="280" cy="140" r="9"/>
    <circle cx="380" cy="140" r="9"/>
  </g>
  <g font-size="12" fill="currentColor" text-anchor="middle">
    <text x="80" y="175">A</text>
    <text x="180" y="175">C</text>
    <text x="280" y="175">T</text>
    <text x="380" y="175">C</text>
  </g>
</svg>
<figcaption>A window of the trellis for a two-state HMM: each column is a position in the sequence,
each node a hidden state (G = genomic background, I = island), and every state at position $i$ has
an edge to every state at $i+1$. Viterbi finds the one path through this graph with the highest
probability given the observed symbols below each column.</figcaption>
</figure>

## Worked example: a two-state HMM for CpG islands

CpG islands are stretches of genomic DNA in which the dinucleotide CG occurs more often than in the
surrounding sequence. The lecture models this with two hidden states, genome (G) and island (I), and
gives concrete Rabiner-notation parameters:

- Initiation: $P_g = 0.99$, $P_i = 0.01$ — a random starting position is overwhelmingly likely to be
  ordinary genome.
- Transition: $P_{gg} = 0.99999$, $P_{gi} = 0.00001$, $P_{ii} = 0.999$, $P_{ig} = 0.001$ — genome is
  "sticky" (it is rare to enter an island at all), and once inside an island the state is also
  fairly sticky, though roughly a hundred times more likely to exit per step than genome is to
  enter one.
- Emission, over $\{C, G, A, T\}$:

  | | C | G | A | T |
  |---|---|---|---|---|
  | CpG island | 0.3 | 0.3 | 0.2 | 0.2 |
  | Genome | 0.2 | 0.2 | 0.3 | 0.3 |

  So a C or a G is $0.3/0.2 = 1.5$ times more likely to have come from an island than from
  background, and by the same token an A or a T is $2/3$ as likely.

That last ratio is the quantity a decoder is actually weighing. Calling a stretch of the sequence an
island only pays off if the accumulated emission evidence for it (each C or G contributing a factor
of $1.5$ to the likelihood ratio, each A or T a factor of $2/3$) outweighs the cost of the two
transitions needed to enter and then leave the island state — and those transition probabilities are
tiny ($10^{-5}$ to enter, $10^{-3}$ to leave). The slide gives the relevant scale directly:

| $N =$ | 20 | 40 | 60 | 80 |
|---|---|---|---|---|
| $(1.5)^N =$ | $3\times10^3$ | $1\times10^7$ | $3\times10^{10}$ | $1\times10^{14}$ |

so a run of a few dozen consecutive C's and G's is already enough evidence to swamp a transition
penalty of $10^{-3}$ to $10^{-5}$, while a much shorter run is not. Deciding exactly where the
break-even point falls for a given sequence is left as an exercise below.

## Real-world HMMs: profile alignment and transmembrane topology

The CpG model is deliberately simple — two states, no structure beyond "stay or switch." Two
applied HMMs push further by giving the state graph itself a shape that mirrors the object being
modelled.

**Profile HMMs** model a multiple sequence alignment. Given an alignment like

```
N • F L S
N • F L S
N K Y L T
Q • W - T
```

each column is either a conserved **match** position (most sequences have a residue there), an
**insertion** relative to the consensus (an extra residue some sequences carry but others don't), or
a **deletion** (a sequence is missing a residue that the consensus has). A profile HMM gives each of
these three roles its own state type, chained together:

<figure>
<svg viewBox="0 0 420 200" role="img" aria-label="Simplified profile HMM topology with match, insert and delete state tracks">
  <defs>
    <marker id="arrow11" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <g font-size="12" fill="currentColor" text-anchor="middle">
    <text x="120" y="35">D1</text>
    <text x="220" y="35">D2</text>
    <text x="320" y="35">D3</text>
    <text x="70" y="100">I0</text>
    <text x="170" y="100">I1</text>
    <text x="270" y="100">I2</text>
    <text x="370" y="100">I3</text>
    <text x="25" y="150">Begin</text>
    <text x="120" y="150">M1</text>
    <text x="220" y="150">M2</text>
    <text x="320" y="150">M3</text>
    <text x="395" y="150">End</text>
  </g>
  <g fill="none" stroke="currentColor" stroke-width="1.5">
    <circle cx="120" cy="45" r="14"/>
    <circle cx="220" cy="45" r="14"/>
    <circle cx="320" cy="45" r="14"/>
    <circle cx="70" cy="110" r="13"/>
    <circle cx="170" cy="110" r="13"/>
    <circle cx="270" cy="110" r="13"/>
    <circle cx="370" cy="110" r="13"/>
    <circle cx="120" cy="140" r="14"/>
    <circle cx="220" cy="140" r="14"/>
    <circle cx="320" cy="140" r="14"/>
  </g>
  <g stroke="currentColor" stroke-width="1" fill="none" marker-end="url(#arrow11)" opacity="0.85">
    <line x1="35" y1="145" x2="105" y2="141"/>
    <line x1="134" y1="140" x2="205" y2="140"/>
    <line x1="234" y1="140" x2="305" y2="140"/>
    <line x1="334" y1="140" x2="382" y2="145"/>
    <line x1="134" y1="45" x2="205" y2="45"/>
    <line x1="234" y1="45" x2="305" y2="45"/>
    <line x1="120" y1="128" x2="120" y2="59"/>
    <line x1="220" y1="128" x2="220" y2="59"/>
    <line x1="320" y1="128" x2="320" y2="59"/>
    <line x1="70" y1="123" x2="70" y2="123" />
    <line x1="120" y1="126" x2="80" y2="115"/>
    <line x1="220" y1="126" x2="180" y2="115"/>
    <line x1="320" y1="126" x2="280" y2="115"/>
  </g>
</svg>
<figcaption>Schematic profile HMM: the match chain (bottom) is the main path from Begin to End;
insert states (middle) let extra residues appear between match columns without consuming one;
delete states (top) let a sequence skip a match column it lacks a residue for.</figcaption>
</figure>

The same idea generalises to DNA and RNA alignments, not just protein.

**TMHMM** (Krogh et al., *J. Mol. Biol.* 2001) predicts transmembrane helices in a protein sequence,
and claims about 97% accuracy on its authors' benchmark. Its state graph is built to mirror the
physical topology of a membrane protein rather than being a generic chain: a cycle running from a
cytoplasmic globular region, through a short loop and a "cap," into the fixed-length helix core
(modelled as a run of about 25 positions), out through another cap and a loop on the non-cytoplasmic
side, into a non-cytoplasmic globular region, and — since a multi-pass membrane protein crosses back
and forth — around again. Decoding assigns each residue of a real sequence (the example given is the
mouse chloride channel CLC6) to inside/outside/transmembrane, and the output includes both the
single best (Viterbi) parse and a posterior probability curve over the sequence, which is often more
informative than the single best path when the model is uncertain.

## RNA secondary structure: why it matters

Secondary structure means the pattern of intramolecular hydrogen bonds between bases of the same RNA
molecule, before or alongside any tertiary folding. Two ways of writing it down:

- **Parentheses notation**: unpaired bases are dots, and a base pair is a matching pair of
  parentheses, e.g. `..(((…..)))……((((……..............)).))…`
- **Arc ("rainbow") notation**: the sequence is drawn as a line, and each base pair is drawn as an
  arc connecting its two partners.

(What these look like as pictures, and how the two notations differ in what they can and can't
represent cleanly, is left as an exercise below.)

The lecture motivates the topic with three biological examples of RNA structure carrying function:

- **tRNA**: an acceptor stem carries the amino-acid attachment site at the $3'$/$5'$ ends, held
  together by hydrogen bonds between paired bases, with an anticodon loop elsewhere in the molecule.
- **The ribosome**: X-ray crystal structures of the 30S and 50S subunits and of functional
  ribosome complexes (Cate et al., *Science* 1999; Ban et al., *Science* 2000; Nissen et al.,
  *Science* 2000) show RNA and protein interleaved through the particle — the lecture's own image
  describes the RNA and protein components as "fettuccine" and "linguine" respectively, with the RNA
  strands doing far more of the structural work than their thin appearance suggests, including
  forming the exit channel for the growing polypeptide chain.
- **The ribosome is a ribozyme**: the catalytic peptidyl-transferase center is close to RNA and far
  from protein — the nearest proteins measured were 18–24 Å from the active site (Nissen et al.,
  *Science* 2000) — meaning the ribosome catalyses peptide bond formation using RNA, not protein,
  chemistry. Because that active site is RNA, it is also a drug target: several classes of
  antibiotics work by binding ribosomal RNA, which is part of why solving ribosome structures (e.g.
  of the *Deinococcus radiodurans* 50S subunit) has practical value beyond basic biology.

## Noncoding RNAs and the prediction problem

Not every functional RNA gets translated. The lecture frames the computational challenges of
noncoding RNA (ncRNA) as three separate problems: predicting an ncRNA's structure, identifying ncRNA
genes in a genome, and predicting an ncRNA's function. Classes named include tRNAs, rRNAs, UTRs,
snRNAs, snoRNAs, prokaryotic terminators, RNaseP, SRP RNA, tmRNA, miRNAs, lncRNAs and riboswitches.

## Predicting structure by covariation

The key fact that makes structure predictable from an alignment of homologous sequences is that
**secondary structure is more evolutionarily conserved than the primary sequence that realises it**.
A base pair can survive across homologs even while the actual bases at both of its positions
drift, provided the two positions drift together — a compensatory (covarying) change: if one partner
of a Watson–Crick pair mutates, the structure is preserved only if the other partner mutates to
match. The lecture's example alignment of five short sequences,

```
Seq1:  A  C  G  A  A  A  G  U
Seq2:  U  A  G  U  A  A  U  A
Seq3:  A  G  G  U  G  A  C  U
Seq4:  C  G  G  C  A  A  U  G
Seq5:  G  U  G  G  G  A  A  C
```

is read off as implying a stem-loop, on exactly this basis: at least one pair of columns co-varies
in a pattern consistent with base pairing even though neither column alone is conserved.

This is made quantitative with a **mutual information statistic** for a pair of alignment columns
$i, j$:

$$M_{ij} = \sum_{x,y} f_{x,y}^{(i,j)} \log_2 \frac{f_{x,y}^{(i,j)}}{f_x^{(i)} f_y^{(j)}}$$

where $f_{x,y}^{(i,j)}$ is the fraction of sequences with nucleotide $x$ in column $i$ and $y$ in
column $j$, $f_x^{(i)}$ is the fraction with $x$ in column $i$ alone, and the sum runs over
$x, y \in \{A, C, G, U\}$. $M_{ij}$ reaches its maximum of 2 bits exactly when the two columns are
individually unconstrained (all four bases equally likely at each) but perfectly covary — e.g.
whichever base is at $i$, the base at $j$ is always its Watson–Crick complement. That is precisely
the covariation signature of a conserved base pair, independent of which particular pairing has been
conserved. (Other dependence measures, such as a chi-square statistic, could be used in its place.)

Applying this to a real alignment (tRNA is the lecture's running example, with its acceptor stem,
anticodon and other named stems) recovers the paired columns and hence the secondary structure. But
the method only works under three conditions, stated directly in the lecture:

- secondary structure must be more highly conserved than primary sequence (already the premise
  above);
- there must be sufficient divergence between the homologs for many independent variations to have
  occurred at a pair of paired columns — but not so much that the sequences can no longer be reliably
  aligned to each other in the first place;
- there must be a sufficient number of homologs sequenced for the covariation signal to be
  statistically visible above noise.

## Predicting structure by energy minimization

The alternative to using an alignment is to fold a single sequence by minimizing an estimate of its
folding free energy. Define

$$\Delta G_{\text{folding}} = G_{\text{unfolded}} - G_{\text{folded}}$$

Because there are typically many possible folded conformations, this approach rests on a
**thermodynamic hypothesis**: that the minimum free-energy state (or states) is the one actually
occupied. Free energy itself decomposes as

$$\Delta G = \Delta H - T\Delta S$$

with enthalpy $\Delta H$ favouring folding (base pairing and stacking release energy) and entropy
$\Delta S$ favouring the unfolded state (a single strand has far more accessible conformations).
Which environmental variables shift this balance is posed as an open question in the lecture rather
than answered outright, and is left as an exercise below.

**The Nussinov algorithm** is the simplest version of this idea, replacing the true free energy with
a toy scoring system: $+1$ for every allowed base pair (C:G or A:U), $0$ otherwise. Maximizing this
score is equivalent to minimizing free energy under a model that assigns the same enthalpy to every
allowed pair and ignores everything else that a real energy model would need — base stacking, loop
penalties, entropy.

The algorithm finds the maximum-scoring structure by recursion. For a sequence of length $N$, define
$S(i,j)$ as the score of the best structure on the subsequence running from position $i$ to position
$j$. Because any structure on $(i,j)$ is built out of structures on smaller nested subintervals,
$S(i,j)$ can be written recursively in terms of $S$ on those smaller intervals. The lecture states
that there are four such cases in general, of which the surviving material gives only the first:

1. if $i$ and $j$ pair with each other, the score reduces to $S(i+1, j-1)$ (plus the point scored
   for that pair).

The other three cases — the standard ones being $i$ left unpaired, $j$ left unpaired, and a
bifurcation into two independently-optimal substructures — were not preserved in the slide as
converted; see Sources.

## Structure implementing function: the lysine riboswitch

A riboswitch is a noncoding RNA element, usually in an mRNA's untranslated region, that changes its
own secondary structure in response to binding a small molecule, and by doing so directly controls
gene expression without needing a protein transcription factor. The lysine riboswitch is the
lecture's worked example:

- **Absence of lysine (ON state)**: an anti-sequestering stem forms, leaving the ribosome binding
  site (RBS) and the start codon AUG exposed, so translation can proceed.
- **Presence of lysine (OFF state)**: lysine binds the riboswitch's junctional core, recognised by
  shape complementarity within an elongated binding pocket together with direct and
  potassium-mediated hydrogen bonds to its charged ends (Serganov et al., *Nature* 2008; Caron et
  al., *PNAS* 2012). This binding instead stabilises a sequestering stem that masks the RBS and AUG,
  blocking translation.

The net effect is a direct metabolite-sensing feedback loop: when lysine is abundant, the riboswitch
folds into the OFF conformation and shuts down expression of the enzymes involved in lysine
biosynthesis and transport; when lysine is scarce, it folds ON and those enzymes are made.

## Exercises

1. For the two-state CpG-island HMM above ($P_g=0.99$, $P_i=0.01$; $P_{gg}=0.99999$,
   $P_{gi}=0.00001$, $P_{ii}=0.999$, $P_{ig}=0.001$; emissions as tabulated), find the optimal
   (Viterbi) parse for each of the following sequences:
   - $(\text{ACGT})_{10000}$ — i.e. ACGT repeated ten thousand times;
   - $\text{A}_{1000}\text{C}_{80}\text{T}_{1000}\text{C}_{20}\text{A}_{1000}\text{G}_{60}\text{T}_{1000}$.

   Use the table of powers of $1.5$ given above as a starting point for comparing accumulated
   emission evidence against the transition penalty.

2. Write out what the structure `..(((…..)))……((((……..............)).))…` looks like under arc
   ("rainbow") notation. What can arc notation represent about a structure that parentheses notation
   cannot represent cleanly, and vice versa?

3. What environmental variables would you expect to shift the enthalpy/entropy balance
   $\Delta G = \Delta H - T\Delta S$ that governs whether an RNA molecule folds or stays unfolded?

## Sources

- Slides: `computational-biology/mit-ocw/7091j/lectures/11-slides.md` (C. Burge, Lecture #10, MIT
  7.91J/20.490J/6.874J/HST.506J/7.36J/20.390J/6.802J, Spring 2014, March 13 2014), covering: HMM
  terminology and the Viterbi trellis; the CpG island HMM and the "more Viterbi examples" slide;
  profile HMMs; TMHMM (citing Krogh et al., *J. Mol. Biol.* 2001, and the TMHMM architecture figure
  sourced in the slide to Chaturvedi et al., *Bioinformation* 2011); RNA secondary structure and the
  ribosome (citing Cate et al. 1999, Ban et al. 2000, and Nissen et al. 2000, all *Science*); the
  covariation/mutual-information slides; the energy-minimization and Nussinov slides; and the lysine
  riboswitch (citing Serganov et al., *Nature* 2008, and Caron et al., *PNAS* 2012). No transcript,
  notes or exercise set was supplied for this lecture; the "Exercises" above are the lecture's own
  in-slide questions, rewritten but not answered.
- The source file itself is flagged by its conversion as **reconstructed by a model** from a PDF
  with no extractable text layer, with "every equation... unverified" — the numbers and formulas
  reproduced here should be checked against the original slide PDF
  (`sources/ocw-7091j/lectures/11-slides.pdf` in the course materials) if precision matters.
- The slide on the Nussinov recursion states there are four cases relating $S(i,j)$ to optimal
  scores on smaller subsequences, but the source material breaks off after the first case (garbled
  text follows in the converted file); cases 2–4 are not reproduced here because they were not
  recoverable from what was supplied.
- Several figures referenced by the slides (the TMHMM output for CLC6, the ribosome crystal
  structures, the lysine riboswitch diagram) are copyrighted images excluded from the course's
  Creative Commons license and are not reproduced here; they are listed only by source citation
  above, as given in the slide deck.

---

[← 9. Hidden Markov Models of Sequences](09-hidden-markov-models-of-sequences.md) · [Contents](index.md)
