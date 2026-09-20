---
title: "12. Genomics: A Molecular Biology Primer"
course: "StatOmics Sga21"
chapter: 12
source: "https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [StatOmics Sga21](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/singleCell_intro1.Rmd), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Genomics: A Molecular Biology Primer

## What this covers

This is the opening lecture of the course, and it answers two different questions in sequence:
why does working with genomic data require statistics at all, and what is the minimum vocabulary
of molecular biology — genome, gene, DNA, transcription, translation, differential expression —
that the rest of the course will take for granted. It assumes no prior biology background; it does
assume the reader knows, in general terms, what a statistical sample and a variable are.

## Why genomics needs statistics

Bio-informatics research works from empirical data, and the data have a specific shape: the
number of observations (samples, patients, replicates) is almost always much smaller than the
number of features being measured (genes, proteins, sites in the genome). This is the
$n \ll p$ regime. When there are far more measured quantities than samples, it becomes easy to
find something that looks like a pattern — a gene that "differs" between groups, a correlation
between two variables — purely by chance. Statistics is the tool for telling a real biological
pattern apart from a pattern that is just noise in a high-dimensional data set, and that is the
reason a statistics course opens a genomics curriculum: scientific integrity and reproducibility in
this field depend on getting that distinction right.

## The genome, genes, and genomics

- The **genome** is the entire hereditary information of an organism. It contains everything
  needed to carry out every function the organism performs.
- Most of those functions are carried out by **proteins**.
- A **gene** is a region of the genome that directs the synthesis of a protein.
- **Genomics** is the study of all of an organism's genetic information together — the code
  itself, and its effects, functions and interactions — rather than one gene at a time.

## The genome is stored in DNA

The genome is stored in DNA, deoxyribonucleic acid (in many viruses it is stored in RNA instead).
DNA is a code written in four nucleotides, split into two chemical classes:

- **purines**: adenine (A) and guanine (G)
- **pyrimidines**: thymine (T) and cytosine (C)

Each nucleotide also carries a phosphate group and a deoxyribose sugar, which are the structural
parts that let nucleotides link into a chain. Two such chains wind around each other into DNA's
double helix, held together by hydrogen bonds between complementary bases. DNA is organized into
chromosomes; most of it sits in the nucleus, with a further, separate copy in the mitochondrion
(the cell's energy-producing organelle).

### The structure of the strand

A polynucleotide chain is directional: its two ends are chemically different, called the 3' end
and the 5' end, after the numbering of the carbon atoms in the sugar ring (the 3' end carries a
free hydroxyl group, the 5' end a phosphate group). When two complementary DNA strands pair up,
they run **antiparallel** — the 5'-to-3' direction of one strand is the reverse of the other's.
Most DNA is kept tightly coiled and condensed, which is what makes it a stable, durable store of
information.

## From DNA to protein: transcription and translation

The lecture frames the flow of information with a computing analogy:

- the **genome/DNA** is the cell's **hard drive** — the full four-letter (A, C, T, G) archive of
  genetic information;
- the **transcriptome/RNA** is the cell's **RAM** — the subset of that information the cell is
  actually using right now;
- the **proteome** is what gets built from what is loaded into RAM.

<figure>
<svg viewBox="0 0 420 150" role="img" aria-label="DNA is transcribed into RNA, which is translated into protein">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="15" y="45" width="100" height="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="65" y="68" text-anchor="middle" font-size="12" fill="currentColor">DNA</text>
  <text x="65" y="84" text-anchor="middle" font-size="11" fill="currentColor">"hard drive"</text>

  <rect x="160" y="45" width="100" height="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="210" y="68" text-anchor="middle" font-size="12" fill="currentColor">RNA</text>
  <text x="210" y="84" text-anchor="middle" font-size="11" fill="currentColor">"RAM"</text>

  <rect x="305" y="45" width="100" height="55" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="355" y="68" text-anchor="middle" font-size="12" fill="currentColor">Protein</text>

  <line x1="115" y1="72" x2="158" y2="72" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="136" y="60" text-anchor="middle" font-size="11" fill="currentColor">transcription</text>

  <line x1="260" y1="72" x2="303" y2="72" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="281" y="60" text-anchor="middle" font-size="11" fill="currentColor">translation</text>
</svg>
<figcaption>The genome is the archived information; the transcriptome is the working copy the
cell is currently using; translation turns that working copy into protein.</figcaption>
</figure>

**Transcription** copies a gene from DNA into RNA:

- the DNA is unwound;
- RNA polymerase reads the DNA template strand, which is the antisense strand of the gene;
- it builds a single, complementary RNA strand;
- the RNA is then spliced.

**Translation** turns RNA into protein:

- it happens at the ribosomes, the "factories of the cell";
- the slide lists 24 amino acids (aa) as the alphabet proteins are built from;
- three consecutive RNA bases form one **codon**;
- a tRNA molecule, carrying the matching anticodon, ferries one specific amino acid to the
  ribosome for each codon read;
- the genetic code is redundant: several different codons can specify the same amino acid;
- the start codon is AUG, coding for methionine (often removed afterwards); the stop codons are
  UAG, UAA and UGA.

After translation, the protein still undergoes post-translational modification and folding before
it is functional. (The deck marks the transition to proteins themselves with a photograph credited
to Science Daily rather than further text.)

## The human genome in numbers

- $2 \times 3$ billion base pairs per human cell, roughly 2 metres of DNA in total.
- Around 20,000 protein-coding genes, unevenly spread across chromosomes (roughly 500–4,000
  genes per chromosome).
- Humans are 99.9% identical to one another at the DNA level.
- Only about 2% of the human genome is protein-coding.
- Humans are about 96% identical to chimpanzees, and about 50% identical to a banana.
- The genome is organized into 23 pairs of chromosomes: 22 autosomal pairs plus one sex-chromosome
  pair (XX in females, XY in males). Within each pair, one chromosome is inherited from each
  parent, via meiosis.

## Differential gene expression

Every cell of an organism carries the same genome, yet a brain cell and a liver cell look and
behave completely differently, and an organism's own cells change dramatically over its lifetime
(the lecture's example is the development of a butterfly through its life stages). The genome
alone cannot explain this — the resolution is that cells do not use all of their genome at once:

- different genes are switched on in different cells and at different times;
- and the genes that are switched on are expressed at different **levels** across cells and time.

This is **differential gene expression**, and it is the central phenomenon the course's statistical
methods are built to detect. As illustrating evidence, the slides give a table of how many
(and what fraction of) annotated genes are actually detected as expressed in a few human tissues
and cell lines:

| Tissue/Cell | Number of genes | Fraction of genes | Ensembl genes |
| :--- | :--- | :--- | :--- |
| Skeletal muscle | 11,276 | 0.61 | 11,953 |
| Liver | 11,392 | 0.61 | 12,191 |
| BT474 | 11,844 | 0.64 | 12,808 |
| MB435 | 11,847 | 0.64 | — |

(BT474 and MB435 are breast-cancer cell lines. The source slide carries footnote markers on the
column headers and row labels whose legend was not captured by the conversion, so the precise
definitions behind "Number of genes" versus "Ensembl genes" are not available here — the table is
reproduced only to show that a large, tissue-dependent subset of the roughly 20,000 annotated genes
is expressed at all, which is the point the lecture uses it to make.)

## Sources

- `docs/omics-statistics/statomics/sga21/docs/intro.md` in the knowledge-base-library — a
  model's reconstruction of `docs/intro.pdf` from the statOmics SGA21 course (Lieven Clement,
  Ghent University), licensed CC BY-NC-SA 4.0. This is the only supplied material for this
  chapter; there was no separate transcript, slide deck, or exercise set to merge it with, and
  the source itself is flagged as reconstructed from a PDF with no text layer, so its wording is a
  paraphrase and any numeric detail in it (for instance the amino-acid count and the hydrogen-bond
  count above) should be checked against the original PDF rather than cited from here.
- The original PDF's pages (1–19) contain roughly thirty images — photographs and diagrams
  illustrating DNA structure, transcription, translation, chromosomes and the human genome — which
  the conversion extracted but only labelled by page number, without capturing what each one shows
  or where on the slide it sat. They are not described in this chapter because the conversion does
  not record their content.

---

[← 11. Course Description](11-course-description.md) · [Contents](index.md) · [13. RNA-seq versus Microarray Reproducibility →](13-rna-seq-versus-microarray-reproducibility.md)
