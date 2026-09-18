---
title: "4. Markov Chains and CRISPR Genomics"
course: "MIT 7.091J"
chapter: 4
source: "https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 7.091J](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 4. Markov Chains and CRISPR Genomics

## What this covers

This chapter reconstructs Lecture 6 of the course ("Comparative Genomics," Feb 13, 2014): the
Markov-chain language for describing how a sequence changes from one generation to the next, and a
worked case study — the discovery of CRISPR spacer sequences and their match to phage genomes —
that shows comparative genomics finding a bacterial immune system by, in effect, matching short
bacterial sequences against a much longer viral genome. It assumes only conditional probability and
a rough sense of what a phylogenetic tree is.

One thing to flag before starting: the slide deck's own title and its agenda slide (below) promise
the two classical pairwise-alignment algorithms and the substitution matrices used to score protein
alignments. What survives of the deck does not actually contain that material — see the note at the
end of the next section, and **Sources**.

## The lecture's agenda

The second slide states the plan in three bullets:

- Global sequence alignment (Needleman-Wunsch-Sellers)
- Gapped local sequence alignment (Smith-Waterman)
- Substitution matrices for protein comparison

with a pointer to the textbook: "Background: Z&B Chapters 4, 5 (esp. pp. 119-125)."

None of the three is actually developed on the slides that follow. Instead the deck spends its time
on the probabilistic model that alignment scoring is built on top of — a Markov-chain description of
how a sequence changes along a lineage — and then on CRISPR, a case study in which matching short
sequences against a genome is exactly the kind of comparison those algorithms exist to do. Treat the
bullet list above as a map of where the topic is going, not as something covered in what follows —
the algorithm itself is picked up in the next lecture (see Sources).

## Three generations of a sequence

The deck opens with a picture of DNA sequence evolution: the same 51-base-pair stretch, shown for
three successive generations of one lineage.

```
Generation n-1 (grandparent)
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTACGCCTAGCCCATGCGA 3'

Generation n (parent)
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCATGCGA 3'

Generation n+1 (child)
5' TGGCATGCACCCTGTAAGTCAATATAAATGGCTATGCCTAGCCCGTGCGA 3'
```

Reading down each column: the grandparent-to-parent step carries a single substitution (a C becomes
a T, in "...GCTACGCC..." to "...GCTATGCC..."), and the parent-to-child step carries a second,
unrelated one (an A becomes a G, in "...CCCATGCGA" to "...CCCGTGCGA"). Two independent point changes,
one per generation. This is the object the rest of the lecture wants a mathematical description of:
a random process that occasionally, and independently, flips a base at each step.

## The Markov chain

A stochastic process is a random process, equivalently a sequence of random variables $X_1, X_2,
X_3, \dots$. It has the **Markov property** if

$$P(X_{n+1} = j \mid X_1=x_1, X_2=x_2, \dots, X_n=x_n) = P(X_{n+1} = j \mid X_n=x_n)$$

for every choice of the $x_i$, every $j$, and every $n$. In words: the future (the next state) is
conditionally independent of the past, given the present (the current state). A process with this
property is a **Markov chain**, after Andrey Markov (1856-1922).

This is exactly the simplifying assumption the sequence-evolution picture wants: to know the
distribution of tomorrow's base at a site, it should be enough to know today's base, not the whole
history of what it used to be several generations back.

## The Markov property in a pedigree

The slides give a second illustration, off DNA and onto genotypes: the genotype at the
Apolipoprotein locus (alleles $A$ and $a$) across three generations of the (illustrative) Simpson
family forms a Markov chain —

- **past**: Grandpa Simpson, Grandma Simpson
- **present**: Homer, Marge
- **future**: Bart

<figure>
<svg viewBox="0 0 360 230" role="img" aria-label="A three-generation pedigree showing the Markov property: the past generation reaches the future generation only through the present generation">
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 7 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>

  <text x="15" y="45" font-size="12" fill="currentColor">past</text>
  <text x="15" y="125" font-size="12" fill="currentColor">present</text>
  <text x="15" y="205" font-size="12" fill="currentColor">future</text>

  <text x="95" y="40" text-anchor="middle" font-size="12" fill="currentColor">Grandpa</text>
  <text x="275" y="40" text-anchor="middle" font-size="12" fill="currentColor">Grandma</text>
  <text x="95" y="120" text-anchor="middle" font-size="12" fill="currentColor">Homer</text>
  <text x="275" y="120" text-anchor="middle" font-size="12" fill="currentColor">Marge</text>
  <text x="185" y="205" text-anchor="middle" font-size="12" fill="currentColor">Bart</text>

  <line x1="95" y1="50" x2="95" y2="105" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="275" y1="50" x2="275" y2="105" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="105" y1="130" x2="175" y2="192" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="265" y1="130" x2="195" y2="192" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 95 48 C 20 120, 50 190, 165 200" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3" opacity="0.5" marker-end="url(#arrow)"/>
  <text x="8" y="168" font-size="10.5" fill="currentColor" opacity="0.75">screened off once</text>
  <text x="8" y="180" font-size="10.5" fill="currentColor" opacity="0.75">Homer is known</text>
</svg>
<figcaption>Grandpa and Grandma reach Bart only through Homer and Marge: the dashed path is the dependence the Markov property says carries no further information once the present generation is known.</figcaption>
</figure>

Concretely, Bart's genotype is conditionally independent of Grandpa's genotype, given Homer's
genotype:

$$P(\text{Bart} = a/a \mid \text{Grandpa} = A/a \text{ and } \text{Homer} = a/a) = P(\text{Bart} = a/a \mid \text{Homer} = a/a)$$

Once Homer's genotype is known, learning Grandpa's genotype on top of it tells you nothing more
about Bart — Homer already screens off Grandpa. Same property as in the classical definition,
applied one link of a pedigree at a time.

## Matrix notation for a Markov chain along a lineage

Back on DNA, and assuming no natural selection acting on the site, write $S_n$ for the base present
at generation $n$. The one-step transition probabilities

$$P_{ij} = P(S_{n+1} = j \mid S_n = i)$$

collect into a $4 \times 4$ transition matrix over the four bases,

$$P = \begin{pmatrix} P_{AA} & P_{AC} & P_{AG} & P_{AT} \\ P_{CA} & P_{CC} & P_{CG} & P_{CT} \\ P_{GA} & P_{GC} & P_{GG} & P_{GT} \\ P_{TA} & P_{TC} & P_{TG} & P_{TT} \end{pmatrix}$$

(rows indexed by the base at generation $n$, columns by the base at generation $n+1$, in the order
$A, C, G, T$). Writing $\vec{q}^{\,n} = (q_A^n, q_C^n, q_G^n, q_T^n)$ for the vector of probabilities
of each base at generation $n$, the one-step update is

$$\vec{q}^{\,n+1} = \vec{q}^{\,n} P.$$

The slide labels this the first of a list of "handy relations," and the source text is cut off
before it states the next one — presumably the analogous relation for several steps at once — so it
is not reproduced here (see Sources).

## Branch length as a measure of conservation

A phylogenetic tree relating several species can be read as several runs of the same kind of Markov
chain, one along each branch: the longer a branch, the more one-step transitions it represents, and
so the more chances a base — or a short motif — has had to be changed by neutral mutation. That makes
the total branch length over which a site survives intact a natural score for how strongly it is
being held in place by selection: a site preserved across a large total branch length has resisted
far more independent opportunities to mutate than one preserved across a short one.

The slides apply this to a specific regulatory element: the 8-nucleotide binding site for the
microRNA miR-1, in the gene *SLC35B4*. Summing the branch lengths of the mammalian phylogenetic tree
over which this particular site is conserved gives

$$0.07 + 0.20 + 0.05 + 0.05 + 0.21 + 0.19 + 0.06 + 0.07 + (\text{six smaller branch lengths}) = 1.0$$

(branch lengths normalised so the total tree length is 1). This is the branch-length conservation
measure used to assess and classify mammalian microRNA target sites in Friedman, Farh, et al.,
"Most Mammalian mRNAs are Conserved Targets of MicroRNAs," *Genome Research* 19 (2009): 92-105 —
cited on the slide as the source of the method, shown here worked through for one target site.

## Case study: CRISPR spacers are a bacterial memory of phage encounters

The second half of the lecture turns to a case study in comparative genomics: CRISPR (Clustered
Regularly Interspaced Short Palindromic Repeats), a repeat structure found in many bacterial
genomes.

Two papers cited on the slides supply the pieces of the story:

- Jansen, Embden, et al., "Identification of Genes that are Associated with DNA Repeats in
  Prokaryotes," *Molecular Microbiology* 43 (2002): 1565-75, identified a family of genes (the
  *cas* genes, CRISPR-associated) that consistently sit next to this repeat structure across
  bacterial genomes — found by comparing many genomes and noticing the same gene family recurring
  beside the same repeat structure.
- Bolotin, Quinquis, et al., "Clustered Regularly Interspaced Short Palindromic Repeats (CRISPRs)
  Have Spacers of Extrachromosomal Origin," *Microbiology* 151 (2005): 2551-61, asked where the
  variable "spacer" sequences between the repeats come from, and answered it by comparison: they
  matched the spacer sequences against a database of phage genomes and found direct hits.

Their Figure 4 shows one such match in detail: several CRISPR spacers line up against specific
positions along the genome of phage Sfi21, each hit called at a BLAST E-score below $0.001$, and
marked according to which DNA strand of the phage it matches. That a short, otherwise unremarkable
stretch of bacterial DNA turns out to be an exact match to a piece of a virus's genome is the
finding — the spacers are captured fragments of past phage DNA, sitting in the bacterial genome as a
record of an earlier infection.

That record turns out to be functional, not just historical. Bolotin et al.'s Figure 6 plots, across
strains of *Streptococcus thermophilus*, the number of spacers in a strain's CRISPR locus against
its resistance to a panel of phages. For strains that were not fully resistant, resistance falls off
with fewer spacers along a fitted line $y = -0.02x + 0.77$ ($R^2 = 0.51$); strains that were fully
resistant to every phage tested were excluded from that fit. Fewer spacers — a shorter memory of
past infections — means resistance to fewer of the phages tried against the strain: matching
sequence, in this case, is doing the work of immune memory.

## Sources

- Slides: `lectures/04-slides/01-global-alignment-of-protein-sequences-nw-sw-pam-blosum.md` and
  `02-number-of-spacers-is-correlated-with-resistance-to-phage.md`, from MIT OCW 7.91J / 7.36J /
  20.490J / 20.390J / 6.874J / 6.801J / HST.506, Spring 2014 ("C. Burge Lecture #6," Feb 13, 2014).
  Every definition, worked example, equation and citation above is drawn from these two files.
- **Not contained in the source, despite the title.** The deck is titled "Global Alignment of
  Protein Sequences (NW, SW, PAM, BLOSUM)" and its own agenda slide names Needleman-Wunsch-Sellers
  global alignment, Smith-Waterman local alignment, and protein substitution matrices as the
  lecture's topics, pointing to Z&B Chapters 4-5 (pp. 119-125) as background reading. None of that
  algorithmic material appears in what survives of the deck. The source file is marked
  `fidelity: reconstructed` — read by a model from a PDF with no text layer — so this is most likely
  lost in conversion rather than never presented; the next lecture in this course is titled
  "Backtracking," which is presumably where the alignment recurrence itself is worked out.
- The transition-matrix slide's "Handy relations" list is cut off mid-list in the source, right
  after the one-step relation $\vec{q}^{\,n+1} = \vec{q}^{\,n}P$; whatever relation came next is not
  reproduced here because it is not legible in the source.
- The two referenced figures (Figs. 4 and 6 of Bolotin et al. 2005, and the phylogenetic-tree figure
  behind the branch-length example from Friedman et al. 2009) are described here from their captions
  only. The images are explicitly marked in the source as excluded from the course's Creative
  Commons licence, and are not reproduced.
- No exercises. This lecture's slot in the file listing came with Problem Set 4 (Bayesian Networks;
  Refining Protein Structures in PyRosetta; Mutual Information of Protein Residues; due April 17,
  2014) and five weeks of recitation slides (April 2 - April 30, covering protein structure, protein
  interactions and gene networks, Boolean network models, chromatin structure, and QTLs/GWAS). Both
  fall roughly two months after this Feb 13 lecture and neither touches Markov chains, sequence
  alignment, or CRISPR — they are course materials numbered "4" by coincidence of file ordering, not
  this lecture's own exercises, so they are named here rather than attached to material they do not
  test.

---

[← 3. BLAST Statistics and Global Alignment](03-blast-statistics-and-global-alignment.md) · [Contents](index.md) · [5. Backtracking Search for Read Alignment →](05-backtracking-search-for-read-alignment.md)
