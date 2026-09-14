---
title: Biology Review
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Biology Review

**Source:** `recitations/2014-02-14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

29

## Selection

- Negative selection (purifying/natural selection) – removal of deleterious traits

- Positive selection – increases prevalence of adaptive traits

- Thinking about selection happening at different levels

   - _Protein level: Sequence -> Structure -> Function_

   - RNA level: splicing, degradation/processing (NMD)

   - DNA level: DNA-protein binding sites

30

## Synonymous/Non-synonymous mutations

- Redundancy built into the genetic code

- Synonymous – one base changes for another in an exon, but the s

- resulting amino acid sequence i unchanged

- Non-synonymous – new AA

- Can affect splicing, mRNA processing  - so may not be silent

||||||Second|Position||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|||U||C||A||G||||
||U|UUU<br>UUC<br>UUA<br>UUG|Phe<br>Leu|UCU<br>UCC<br>UCA<br>UCG|Ser|UAU<br>UAC<br>UAA<br>UAG|Tyr<br>_Stop_<br>_Stop_|UGU<br>UGC<br>UGA<br>UGG|Cys<br>_Stop_<br>Trp|U<br>C<br>A<br>G||
|First|C|CUU<br>CUC<br>CUA|Leu|CCU<br>CCC<br>CCA|Pro|CAU<br>CAC<br>CAA|His<br>l|CGU<br>CGC<br>CGA|Arg|U<br>C<br>A|Third|
|Position<br>'||CUG||CCG||CAG|Gn|CGG||G|Position<br>'|
|(5 end)||AUU<br>AUC|Ile|ACU<br>ACC|Th|AAU<br>AAC|Asn|AGU<br>AGC|Ser|U<br>C|(3 end)|
||A|AUA||ACA|r|AAA|L|AGA|A|A||
|||AUG|Met|ACG||AAG|ys|AGG|rg|G||
|||GUU||GCU||GAU|As|GGU||U||
||G|GUC|Val|GCC|Ala|GAC|p|GGC|Gl|C||
|||GUA||GCA||GAA|Gl|GGA|y|A||
|||GUG||GCG||GAG|u|GGG||G||


Image by MIT OpenCourseWare.

31

## Side-chain biochemistry

- Amino acids classified by properties of side chains

   - Grouped by general properties

- Substitutions of amino acid with another of similar chemical properties may conserve protein function


> © unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

32

## Side chain size (Trp – W)


© unknown source. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

33

## Disulfide bond

- Important in protein folding – holds two distant portions of protein together

- Occurs between Cys residues


34

## Next-generation sequencing

- Sequencing is always of DNA

   - Need to convert RNA to DNA by _reverse transcription_ (RT)

- Illumina is current leader in the field

   - 8 lanes on a flow cell

   - Each lane can sequence 200 million 100bp reads – 20 Gbps!

   - Can sequence multiple samples per lane by barcoding

   - Requires (heterogeneous) population of cells to get enough DNA for sample

- Single cell sequencing applications are becoming more common (RNAseq)

- Single molecule technologies are still being developed – PacBio

35

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Alignment →](03-alignment.md)
