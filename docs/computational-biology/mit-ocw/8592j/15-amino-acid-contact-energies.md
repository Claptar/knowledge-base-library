---
title: "15. Amino Acid Contact Energies"
course: "MIT 8.592J"
chapter: 15
source: "https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 8.592J](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. Amino Acid Contact Energies

## What this covers

The only material supplied for this chapter is a single scanned table, reproduced below: a
20 x 20 grid of amino-acid contact energies, in units of $RT$ (thermal energy), with the header
row and the file's own name (`mj-table3-slides`) pointing to a table conventionally known as a
Miyazawa-Jernigan contact-energy table. No slides, transcript or problem set accompany it in the
supplied material, so this chapter does what the numbers themselves support: it explains what the
two triangles of the grid mean, works through the arithmetic that connects them, and reads off the
one pattern in the data that is unambiguous - which residues attract their own kind strongly and
which barely do. It assumes only that a "contact" between two amino acid side chains, and an energy
measured in units of $RT$, are meaningful ideas to the reader; nothing else about the derivation of
the table is given here beyond what the table itself displays.

## The table

| | Cys | Met | Phe | Ile | Leu | Val | Trp | Tyr | Ala | Gly | Thr | Ser | Asn | Gln | Asp | Glu | His | Arg | Lys | Pro |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Cys | -5.44 | -4.99 | -5.80 | -5.50 | -5.83 | -4.96 | -4.95 | -4.16 | -3.57 | -3.16 | -3.11 | -2.86 | -2.59 | -2.85 | -2.41 | -2.27 | -3.60 | -2.57 | -1.95 | -3.07 |
| Met | 0.46 | -5.46 | -6.56 | -6.02 | -6.41 | -5.32 | -5.55 | -4.91 | -3.94 | -3.39 | -3.51 | -3.03 | -2.95 | -3.30 | -2.57 | -2.89 | -3.98 | -3.12 | -2.48 | -3.45 |
| Phe | 0.54 | -0.20 | -7.26 | -6.84 | -7.28 | -6.29 | -6.16 | -5.66 | -4.81 | -4.13 | -4.28 | -4.02 | -3.75 | -4.10 | -3.48 | -3.56 | -4.77 | -3.98 | -3.36 | -4.25 |
| Ile | 0.49 | -0.01 | 0.06 | -6.54 | -7.04 | -6.05 | -5.78 | -5.25 | -4.58 | -3.78 | -4.03 | -3.52 | -3.24 | -3.67 | -3.17 | -3.27 | -4.14 | -3.63 | -3.01 | -3.76 |
| Leu | 0.57 | 0.01 | 0.03 | -0.08 | -7.37 | -6.48 | -6.14 | -5.67 | -4.91 | -4.16 | -4.34 | -3.92 | -3.74 | -4.04 | -3.40 | -3.59 | -4.54 | -4.03 | -3.37 | -4.20 |
| Val | 0.52 | 0.18 | 0.10 | -0.01 | -0.04 | -5.52 | -5.18 | -4.62 | -4.04 | -3.38 | -3.46 | -3.05 | -2.83 | -3.07 | -2.48 | -2.67 | -3.58 | -3.07 | -2.49 | -3.32 |
| Trp | 0.30 | -0.29 | 0.00 | 0.02 | 0.08 | 0.11 | -5.06 | -4.66 | -3.82 | -3.42 | -3.22 | -2.99 | -3.07 | -3.11 | -2.84 | -2.99 | -3.98 | -3.41 | -2.69 | -3.73 |
| Tyr | 0.64 | -0.10 | 0.05 | 0.11 | 0.10 | 0.23 | -0.04 | -4.17 | -3.36 | -3.01 | -3.01 | -2.78 | -2.76 | -2.97 | -2.76 | -2.79 | -3.52 | -3.16 | -2.60 | -3.19 |
| Ala | 0.51 | 0.15 | 0.17 | 0.05 | 0.13 | 0.08 | 0.07 | 0.09 | -2.72 | -2.31 | -2.32 | -2.01 | -1.84 | -1.89 | -1.70 | -1.51 | -2.41 | -1.83 | -1.31 | -2.03 |
| Gly | 0.68 | 0.46 | 0.62 | 0.62 | 0.65 | 0.51 | 0.24 | 0.20 | 0.18 | -2.24 | -2.08 | -1.82 | -1.74 | -1.66 | -1.59 | -1.22 | -2.15 | -1.72 | -1.15 | -1.87 |
| Thr | 0.67 | 0.28 | 0.41 | 0.30 | 0.40 | 0.36 | 0.37 | 0.13 | 0.10 | 0.10 | -2.12 | -1.96 | -1.88 | -1.90 | -1.80 | -1.74 | -2.42 | -1.90 | -1.31 | -1.90 |
| Ser | 0.69 | 0.53 | 0.44 | 0.59 | 0.60 | 0.55 | 0.38 | 0.14 | 0.18 | 0.14 | -0.06 | -1.67 | -1.58 | -1.49 | -1.63 | -1.48 | -2.11 | -1.62 | -1.05 | -1.57 |
| Asn | 0.97 | 0.62 | 0.72 | 0.87 | 0.79 | 0.77 | 0.30 | 0.17 | 0.36 | 0.22 | 0.02 | 0.10 | -1.68 | -1.71 | -1.68 | -1.51 | -2.08 | -1.64 | -1.21 | -1.53 |
| Gln | 0.64 | 0.20 | 0.30 | 0.37 | 0.42 | 0.46 | 0.19 | -0.12 | 0.24 | 0.24 | -0.08 | 0.11 | -0.10 | -1.54 | -1.46 | -1.42 | -1.98 | -1.80 | -1.29 | -1.73 |
| Asp | 0.91 | 0.77 | 0.75 | 0.71 | 0.89 | 0.89 | 0.30 | -0.07 | 0.26 | 0.13 | -0.14 | -0.19 | -0.24 | -0.09 | -1.21 | -1.02 | -2.32 | -2.29 | -1.68 | -1.33 |
| Glu | 0.91 | 0.30 | 0.52 | 0.46 | 0.55 | 0.55 | 0.00 | -0.25 | 0.30 | 0.36 | -0.22 | -0.19 | -0.21 | -0.19 | 0.05 | -0.91 | -2.15 | -2.27 | -1.80 | -1.26 |
| His | 0.65 | 0.28 | 0.39 | 0.66 | 0.67 | 0.70 | 0.08 | 0.09 | 0.47 | 0.50 | 0.16 | 0.26 | 0.29 | 0.31 | -0.19 | -0.16 | -3.05 | -2.16 | -1.35 | -2.25 |
| Arg | 0.93 | 0.38 | 0.42 | 0.41 | 0.43 | 0.47 | -0.11 | -0.30 | 0.30 | 0.18 | -0.07 | -0.01 | -0.02 | -0.26 | -0.91 | -1.04 | 0.14 | -1.55 | -0.59 | -1.70 |
| Lys | 0.83 | 0.31 | 0.33 | 0.32 | 0.37 | 0.33 | -0.10 | -0.46 | 0.11 | 0.03 | -0.19 | -0.15 | -0.30 | -0.46 | -1.01 | -1.28 | 0.23 | 0.24 | -0.12 | -0.97 |
| Pro | 0.53 | 0.16 | 0.25 | 0.39 | 0.35 | 0.31 | -0.33 | -0.23 | 0.20 | 0.13 | 0.04 | 0.14 | 0.18 | -0.08 | 0.14 | 0.07 | 0.15 | -0.05 | -0.04 | -1.75 |

Rows and columns run over the twenty amino acids, always in the same order. The entry in row $i$,
column $j$ is a number in $RT$: an effective free energy assigned to bringing the side chains of
residue types $i$ and $j$ into contact, negative meaning favourable. A table of this shape is the
kind of ingredient a coarse (lattice or reduced) model of a folding protein needs once "the
monomers attract each other" is made specific enough to compute with - it replaces a full physical
force field between two side chains by one number per pair of residue types.

The caption distinguishes two conventions carried by the same grid:

- **$e_{ij}$**, for the diagonal and the upper-right half: the contact energy of the pair $(i,j)$
  itself.
- **$e'_{ij}$**, for the lower-left half: a second number for the same pair, always sitting in the
  mirror-image cell.

## Two questions about the same pair

The two conventions are not printing the same number twice. Comparing a cell in the upper triangle
with its mirror image in the lower triangle shows the relation between them. Take cysteine and
methionine: $e_{\text{Cys,Met}} = -4.99$ (row Cys, column Met), while the mirrored cell (row Met,
column Cys) reads $e'_{\text{Cys,Met}} = 0.46$. The two diagonal entries are $e_{\text{Cys,Cys}} =
-5.44$ and $e_{\text{Met,Met}} = -5.46$, whose average is $-5.45$. And indeed

$$e_{\text{Cys,Met}} - \frac{e_{\text{Cys,Cys}} + e_{\text{Met,Met}}}{2} = -4.99 - (-5.45) = 0.46,$$

matching $e'_{\text{Cys,Met}}$ exactly. The same identity,

$$e'_{ij} = e_{ij} - \frac{e_{ii} + e_{jj}}{2},$$

checks out (to the rounding in the table) for every pair tried. So $e_{ij}$ answers "how favourable
is a contact between $i$ and $j$, in absolute terms?", while $e'_{ij}$ answers a different question:
"...compared with what you'd expect from how much $i$ likes itself and $j$ likes itself?" It nets
out each residue's own general stickiness and isolates the pair-specific part of the preference.

Most $e'_{ij}$ entries in the table are small and positive - typically between $0$ and about
$+1\,RT$, topping out around $+0.97$ (asparagine with cysteine). A positive $e'_{ij}$ means the
heterotypic pair is slightly *less* favourable than the average of the two homotypic pairs: left to
themselves, two different residue types would rather each keep company with their own kind than
swap partners.

The clearest exception is instructive. For lysine and glutamate, $e_{\text{Lys,Glu}} = -1.80$, while
the self-terms are both weak: $e_{\text{Lys,Lys}} = -0.12$ and $e_{\text{Glu,Glu}} = -0.91$, averaging
$-0.515$. That makes

$$e'_{\text{Lys,Glu}} = -1.80 - (-0.515) = -1.28,$$

matching the table's $-1.28$, and it is the most negative $e'_{ij}$ entry anywhere in the grid - more
negative than any hydrophobic pair achieves. Arginine and glutamate show the same effect a little
less strongly ($e'_{\text{Arg,Glu}} = -1.04$). Both are oppositely-charged pairs capable of forming a
salt bridge: an attraction that has essentially nothing to do with either residue's affinity for
itself, and $e'_{ij}$ is exactly the quantity built to reveal it, since it has already subtracted
away the self-affinity that dominates $e_{ij}$.

## The diagonal: which residues are "sticky"

The plainest signal in the table is the diagonal, $e_{ii}$ - how favourable it is for two copies of
the same residue type to touch. Ranking all twenty:

<figure>
<svg viewBox="0 0 330 336" role="img" aria-label="Bar chart of the twenty self-contact energies e_ii ranked from most to least attractive">
  <line x1="95" y1="4" x2="95" y2="326" stroke="currentColor" stroke-width="1"/>
  <rect x="95" y="10" width="200" height="11" fill="currentColor"/>
  <text x="88" y="19" text-anchor="end" font-size="11" fill="currentColor">Leu</text>
  <text x="299" y="19" font-size="11" fill="currentColor">-7.37 RT</text>
  <rect x="95" y="26" width="197" height="11" fill="currentColor"/>
  <text x="88" y="35" text-anchor="end" font-size="11" fill="currentColor">Phe</text>
  <rect x="95" y="42" width="177" height="11" fill="currentColor"/>
  <text x="88" y="51" text-anchor="end" font-size="11" fill="currentColor">Ile</text>
  <rect x="95" y="58" width="150" height="11" fill="currentColor"/>
  <text x="88" y="67" text-anchor="end" font-size="11" fill="currentColor">Val</text>
  <rect x="95" y="74" width="148" height="11" fill="currentColor"/>
  <text x="88" y="83" text-anchor="end" font-size="11" fill="currentColor">Met</text>
  <rect x="95" y="90" width="148" height="11" fill="currentColor"/>
  <text x="88" y="99" text-anchor="end" font-size="11" fill="currentColor">Cys</text>
  <rect x="95" y="106" width="137" height="11" fill="currentColor"/>
  <text x="88" y="115" text-anchor="end" font-size="11" fill="currentColor">Trp</text>
  <rect x="95" y="122" width="113" height="11" fill="currentColor"/>
  <text x="88" y="131" text-anchor="end" font-size="11" fill="currentColor">Tyr</text>
  <rect x="95" y="138" width="83" height="11" fill="currentColor"/>
  <text x="88" y="147" text-anchor="end" font-size="11" fill="currentColor">His</text>
  <rect x="95" y="154" width="74" height="11" fill="currentColor"/>
  <text x="88" y="163" text-anchor="end" font-size="11" fill="currentColor">Ala</text>
  <rect x="95" y="170" width="61" height="11" fill="currentColor"/>
  <text x="88" y="179" text-anchor="end" font-size="11" fill="currentColor">Gly</text>
  <rect x="95" y="186" width="58" height="11" fill="currentColor"/>
  <text x="88" y="195" text-anchor="end" font-size="11" fill="currentColor">Thr</text>
  <rect x="95" y="202" width="47" height="11" fill="currentColor"/>
  <text x="88" y="211" text-anchor="end" font-size="11" fill="currentColor">Pro</text>
  <rect x="95" y="218" width="46" height="11" fill="currentColor"/>
  <text x="88" y="227" text-anchor="end" font-size="11" fill="currentColor">Asn</text>
  <rect x="95" y="234" width="45" height="11" fill="currentColor"/>
  <text x="88" y="243" text-anchor="end" font-size="11" fill="currentColor">Ser</text>
  <rect x="95" y="250" width="42" height="11" fill="currentColor"/>
  <text x="88" y="259" text-anchor="end" font-size="11" fill="currentColor">Arg</text>
  <rect x="95" y="266" width="42" height="11" fill="currentColor"/>
  <text x="88" y="275" text-anchor="end" font-size="11" fill="currentColor">Gln</text>
  <rect x="95" y="282" width="33" height="11" fill="currentColor"/>
  <text x="88" y="291" text-anchor="end" font-size="11" fill="currentColor">Asp</text>
  <rect x="95" y="298" width="25" height="11" fill="currentColor"/>
  <text x="88" y="307" text-anchor="end" font-size="11" fill="currentColor">Glu</text>
  <rect x="95" y="314" width="3" height="11" fill="currentColor"/>
  <text x="88" y="323" text-anchor="end" font-size="11" fill="currentColor">Lys</text>
  <text x="102" y="323" font-size="11" fill="currentColor">-0.12 RT</text>
</svg>
<figcaption>Diagonal entries $e_{ii}$ of Table 3, ranked from most to least negative. Leucine, phenylalanine, isoleucine and the other aliphatic, aromatic and sulphur-containing residues sit at one end with strongly favourable self-contacts; the charged and small polar residues sit at the other, close to zero.</figcaption>
</figure>

Leucine, phenylalanine, isoleucine, valine, methionine, cysteine, tryptophan and tyrosine - the
aliphatic, aromatic and sulphur-containing side chains - occupy the strongly negative end, several
times more attractive to themselves than any other residue is. Alanine and glycine sit in the
middle. The charged and small polar residues (aspartate, glutamate, and above all lysine, at
essentially $0\,RT$) barely favour self-contact at all. This is the same twenty residues sorted by
how much each one, on its own, wants to be buried against more of itself - the single number behind
why a folded protein tends to pack its hydrophobic side chains into an interior core and leave the
charged and polar ones facing solvent.

## The five summary rows

Below the 20 x 20 grid the source carries five further rows of numbers, each labelled with a
symbol rather than explained:

- $e_{rr} = -2.55$, followed by $e_{ir}$ for each of the twenty residues.
- $e_r = -3.60$, followed by $e_i$ for each residue.
- $f_r = -3.60$, followed by $f_i$ for each residue.
- $N_{ir}/N_i$, one value per residue (plus one extra).
- $q_i$, one value per residue (plus two extra).

None of these symbols is defined in the material supplied, so nothing beyond what is directly
readable should be taken as established. Two things can be said honestly. First, the subscript
grammar of the first row matches the main table exactly: $e_{rr}$ pairs with $e_{ir}$ the same way
$e_{ii}$ pairs with $e_{ij}$, so whatever $r$ denotes is being carried as if it were a twenty-first
residue type, with its own self-term and its own cross-terms with each real residue. What $r$
stands for physically is not stated here - a plausible guess is some generic or averaged
environment, but that is a guess, not something this table says. Second, the row lengths in this
reconstruction do not all match the twenty-residue header: $N_{ir}/N_i$ carries one entry too many
and $q_i$ two too many for the twenty columns, which is consistent with the source note's own
warning that this file is a model's reconstruction of a scanned page with no text layer, and that
every equation in it is unverified. Anyone wanting to use these five rows quantitatively should
check them against the original page rather than this transcription.

## Sources

- The entire chapter is built from the one file supplied for it:
  `computational-biology/mit-ocw/8592j`, `other/mj-table3-slides.md` (library path
  `docs/computational-biology/mit-ocw/8592j/other/mj-table3-slides.md`), converted from
  `sources/ocw-8592j/other/mj-table3-slides.pdf`. No slides, transcript or exercises were supplied
  for this chapter.
- That file's own header flags it as a model's reconstruction of a PDF with no usable text layer,
  with every equation unverified - a caveat repeated above wherever it bears on how much weight a
  number in the five summary rows can carry.
- The identity $e'_{ij} = e_{ij} - (e_{ii}+e_{jj})/2$, the ranking of self-contact energies, and
  the lysine-glutamate observation are all arithmetic performed directly on the numbers in the
  supplied table; they are not stated as such in the source and should be treated as this chapter's
  reading of the data rather than as reported results.
- What the symbols $e_{rr}, e_{ir}, e_r, e_i, f_r, f_i, N_{ir}/N_i$ and $q_i$ formally denote, and
  what produced the underlying contact-energy estimates in the first place, is not contained in the
  supplied material and is not reconstructed here.

---

[← 14. Synchronization and Turing Patterns](14-synchronization-and-turing-patterns.md) · [Contents](index.md)
