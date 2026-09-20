---
title: Problem 1. Sequence search (6 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/01-questions-pset1-ans.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/01-questions-pset1-ans.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Problem 1. Sequence search (6 points)

7.36/7.91/20.390/20.490/6.802/6.874
PROBLEM SET 1. Sequence search, global alignment, BLAST statistics (19 Points)

Due: Thursday, February $20^{\text{th}}$ at noon.

To better understand inborn disorders of metabolism, you isolate a strain of mice that becomes ill unless fed a diet lacking phenylalanine. You sequence the genome of this mouse and find several differences from wildtype including a change to a region that encodes a highly expressed 68 nucleotide RNA which has sequence

5'-UGUACAUGAUGAAGUCAUAGCGAACGGAGAAGGGCCGGCUGAGGAA
ACUGCACGUCACCCUCCUGAAA-3'

in your strain and

5'-UGUACAUGAUGAAAACAGUCUCCCUCUUCUGAAUCUCGCUGAGGAA
ACUGCACGUCACCCUCCUGAAA-3'

in wildtype mice.

Search the sequence in your strain against the mouse genome and transcriptome using NCBI's BLASTn: from the BLAST homepage, click on "nucleotide blast" (not "Mouse") and use the "Mouse genomic + transcript" (G+T) Database, optimized for "Somewhat similar sequences". By expanding the "Algorithm Parameters" box at the bottom, set the Match/Mismatch scores to +1/-3.

**(A) (1 pt.)** How many statistically significant hits are there at an E-value of 0.05? In one sentence, what does an E-value of 0.05 mean? For transcript hits, what are the maximum reported scores, and are they raw scores or bit scores? (Click on the hyperlink to view individual hits.) To what parts of your RNA do these hits correspond, and what is the % match?

There are two transcript and two genome hits at an E-value of 0.05. The E-value is the expected number of hits with score at least as high as the hit's reported score when searching a query of length 68 nt against the Mouse G+T database. The maximum scores for the two transcript hits are 54 and 50.1 bits. The hit with score 54 bits corresponds to positions 38-68 of the query and has 97% identity to its match (matches 30 of 31 positions), while the hit with score 50.1 bits corresponds to positions 14-38 of the query and has 100% identity.

**(B) (1 pt.)** Using the E-value and reported score from the result with the highest % identity match from part (A), calculate the approximate length of the Mouse (G+T) Database.

Using the score $S = 50.1\text{ bits}$ and $\text{E-value} = 2 * 10^{-4}$ along with $m = 68\text{nt}$ in the formula $\text{E - value} = mn2^{-S}$ yields a mouse G+T Database length of $n = 3.55 * 10^9$. Note that the mouse haploid genome assembly is about 2.7 billion base pairs, so after adding in transcript sequences, the estimate from the formula is around what we would expect (various corrections to the simple formula are made for base content, repetitive regions, and other parameters for the reported BLAST values).

**(C) (1 pt.)** Consider a query sequence Q of length L that matches perfectly to a sequence in the database, yielding a BLAST E-value $\text{E}_1$. How would the E-value change if only the first half of Q were searched against the database? In particular, would it stay the same, go up, go down, and how (linearly, exponentially, etc.)?

Intuitively, decreasing the length of query (and therefore match) should make the match more likely simply by chance and therefore less significant, so we should expect the E-value to increase. Quantitatively, if the sequence query length were halved ($m \to m/2$), the score $S$ would decrease by a factor of 2 ($S \to S/2$) since there are half as many positions at which to accumulate positive match scores. Plugging these into equations for the original query sequence (with score $\text{E}_1$) and the half-length query sequence (with score $\text{E}_2$) yields:

$$\text{E}_1 = mn2^{-S}\text{ and }\text{E}_2 = \frac{m}{2}n2^{-S/2} \Rightarrow \text{E}_1 2^S = 2\text{E}_2 2^{S/2} \Rightarrow \text{E}_2 = \text{E}_1 2^{(S/2 - 1)}$$

Thus, the E-value increases essentially exponentially, with an additional decreasing linear factor of 2 due to halving $m$. But this latter effect is much smaller than the exponential increase resulting from the decreased score.

**(D) (1 pt.)** Returning to the BLAST results from part (A), to what genes and RNA classes do the transcript hits with E-values below 0.05 belong? Does your RNA match the sense or antisense direction of these hits? (Click on the hyperlink of the hit and look at the "Strand" section, which tells you the DNA strand of the Hit/Query.)

Of the 2 statistically transcript significant hits at an E-value of 0.05, one matches nucleotides 14-38 of your RNA complementary to (matching the antisense direction of) an mRNA that encodes the phenylalanine hydroxylase (PAH) enzyme. Nucleotides 38-68 of your RNA match the sense direction of Snord100, a C/D Box snoRNA (a type of noncoding RNA that directs posttranscriptional modifications of other RNAs).

**(E) (2 pts.)** After performing an RNA-protein affinity purification (pull-down) from mouse cell lysates followed by mass spectrometry, you determine that your RNA interacts with the product of the *ADAR1* gene. What does this enzyme do, and what type of RNA does this enzyme act on? Looking back at the function and strand of the gene hit to the second part of your RNA, state a hypothesis as to how your RNA might function to cause your mouse's metabolic disorder. (Hint: on the BLAST hit entry corresponding to the mRNA, click on the "Graphics" link to see the hit in red and how your query at the bottom overlaps with it. If ADAR1 acts at the UAU codon, what is the resulting change during translation?)

The ADAR1 enzyme catalyzes A-to-I editing, post-transcriptionally deaminating adenosine in double-stranded RNA duplexes, yielding inosine. Since I is interpreted as G during translation, A-to-I changes in protein-coding sequences may lead to codon changes and altered functional properties of the proteins. In addition, A-to-I editing can play important roles in regulating gene expression, such as by altering alternative splicing, miRNA sequences, or miRNA target sites in the mRNA.

The *PAH* gene product is a critical enzyme in phenylalanine metabolism and catalyzes the rate-limiting step in its complete catabolism. Nucleotides 14-38 of your RNA overlap a region of the *PAH* ORF antisense to the mRNA, including Tyrosine 414 encoded by the codon UAU. Deamination of this adenosine by ADAR would result in the ribosome interpreting a UGU codon, which encodes for the much smaller Cysteine. Thus, your mutant snoRNA provides an RNA duplex for ADAR1 to cause a missense mutation, which could resulting in reduced activity of the PAH enzyme and contribute to your mouse's metabolic disorder. Indeed, genetic Y414C mutations have been observed in human Phenylketonuria patients, and the mutation has been shown to induce global PAH conformational changes (Gersting *et al.* Am. Journ. Human Genetics 83 2008 http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2443833/pdf/main.pdf). Note that the RNA found in the wildtype mouse is very similar to the normal Snord100 snoRNA, which directs 2'O-ribose methylation of rRNA and does not affect PAH.

The example in this problem was inspired by SNORD115 (HBII-52), a human brain-specific C/D box snoRNA that exhibits sequence complementarity to an alternatively spliced transcript of the serotonin receptor. For more details of how SNORD115 regulates serotonin processing through A-to-I editing and alternative splice products, see Kishore and Stamm *Science* 2006 (http://www.sciencemag.org/content/311/5758/230.full.pdf).

---

[Up: contents](index.md) · [Problem 2. Gapped sequence alignment (6 points) →](02-problem-2-gapped-sequence-alignment-6-points.md)
