---
title: 'Due: Thursday, February 20th at noon.'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/01-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Due: Thursday, February 20th at noon.

**Source:** `psets/01-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Problem 1. Sequence search (6 points)**

To better understand inborn disorders of metabolism, you isolate a strain of mice that becomes ill unless fed a diet lacking phenylalanine. You sequence the genome of this mouse and find several differences from wildtype including a change to a region that encodes a highly expressed 68 nucleotide RNA which has sequence

5’-UGUACAUGAUGAAGUCAUAGCGAACGGAGAAGGGCCGGCUGAGGAA ACUGCACGUCACCCUCCUGAAA-3’

in your strain and

5’-UGUACAUGAUGAAAACAGUCUCCCUCUUCUGAAUCUCGCUGAGGAA ACUGCACGUCACCCUCCUGAAA-3’

in wildtype mice.

Search the sequence in your strain against the mouse genome and transcriptome using NCBI’s BLASTn: from the BLAST homepage, click on “nucleotide blast” (not “Mouse”) and use the “Mouse genomic + transcript” (G+T) Database, optimized for “Somewhat similar sequences”. By expanding the “Algorithm Parameters” box at the bottom, set the Match/Mismatch scores to +1/-3.

**(A) (1 pt.)** How many statistically significant hits are there at an E-value of 0.05? In one sentence, what does an E-value of 0.05 mean? For transcript hits, what are the maximum reported scores, and are they raw scores or bit scores? (Click on the hyperlink to view individual hits.) To what parts of your RNA do these hits correspond, and what is the % match?

1

**(B) (1 pt.)** Using the E-value and reported score from the result with the highest % identity match from part (A), calculate the approximate length of the Mouse (G+T) Database.

**(C) (1 pt.)** Consider a query sequence Q of length L that matches perfectly to a sequence in the database, yielding a BLAST E-value E1. How would the E-value change if only the first half of Q were searched against the database? In particular, would it stay the same, go up, go down, and how (linearly, exponentially, etc.)?

2

**(D) (1 pt.)** Returning to the BLAST results from part (A), to what genes and RNA classes do the transcript hits with E-values below 0.05 belong? Does your RNA match the sense or antisense direction of these hits? (Click on the hyperlink of the hit and look at the “Strand” section, which tells you the DNA strand of the Hit/Query.)

**(E) (2 pts.)** After performing an RNA-protein affinity purification (pull-down) from mouse cell lysates followed by mass spectrometry, you determine that your RNA interacts with the product of the _ADAR1_ gene. What does this enzyme do, and what type of RNA does this enzyme act on? Looking back at the function and strand of the gene hit to the second part of your RNA, state a hypothesis as to how your RNA might function to cause your mouse’s metabolic disorder. (Hint: on the BLAST hit entry corresponding to the mRNA, click on the “Graphics” link to see the hit in red and how your query at the bottom overlaps with it. If ADAR1 acts at the UAU codon, what is the resulting change during translation?)

3

---

[← 01 questions Part 01 —](01-01-questions-part-01.md) · [Up: contents](index.md) · [Problem 2. Gapped sequence alignment ( 6 points) →](03-problem-2-gapped-sequence-alignment-6-points.md)
