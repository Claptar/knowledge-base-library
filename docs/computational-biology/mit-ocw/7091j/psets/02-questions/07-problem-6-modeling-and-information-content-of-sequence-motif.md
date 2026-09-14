---
title: Problem 6. Modeling and information content of sequence motifs (5 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/02-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Problem 6. Modeling and information content of sequence motifs (5 points).

**Source:** `psets/02-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To analyze gene evolution in three phylogenetic groups of protists, you collect samples of three different protist species, A, B, and C, that represent these lineages. You conduct both genome sequencing and cDNA sequencing from each and use spliced alignment of cDNAs to genomes to obtain sets of 10,000 confirmed 3' splice site (3'SS) sequences from each species.  In all three species the invariant AG at the end of each intron is preceded by an 8 base polypyrimidine tract ! (PPT), with frequencies fC = fT = at each position.  Your goal is to develop probabilistic models ! of the PPT motif in each species for use in exon-intron prediction.  Throughout this problem, <u>unless instructed otherwise, you should describe the simplest possible model (fewest parameters) that accurately models the frequencies of all 8mers in the training data (and should therefore give good predictive accuracy). Information content of models should be calculated using the formula given in lecture: I = 2w – H(model), in bits, where w is the width of the motif and H(model) is the Shannon entropy of the model. The abbreviation Y8 refers to 8mers that consist exclusively of pyrimidine (C or T) nucleotides.</u>

**(A) (1 pt.)** In species A, all four dinucleotides CC, CT, TC, and TT occur equally often ! _𝑓𝐶𝐶_ = _𝑓𝐶𝑇_ = _𝑓𝑇𝐶_ = _𝑓𝑇𝑇_ = !<sup>at each of the seven pairs of positions (1,2), (2,3),…,(7,8),</sup> and each 8mer of the form Y8 occurs with frequency 2<sup>-8</sup> .  In one sentence, describe a model for the PPT of species A.  What is the information content of this model?

The   simplest   model   is   a   weight   matrix   model,   with   P(C)   =   P(T)   =   ½   at   each   position.

H(model)   =   8   x   [-­‐((   ½   log2   (   ½   )   +   ½   log2   (   ½   )   )]   =   8   bits. Information   =   (2   x 8)   –   8   =   8   bits.

**(B) (1 pt.)** In species B, all four dinucleotides CC, CT, TC, and TT are equally likely ! = _𝑓𝐶𝐶_ = _𝑓𝐶𝑇_ = _𝑓𝑇𝐶_ = _𝑓𝑇𝑇_ !<sup>at each of the seven pairs of positions (1,2), (2,3),…,(</sup> 7,8), ! but examining the frequencies of 8mers reveals that _𝑓𝑇_ ! = _𝑓𝐶_ ! = _𝑓_ ( _𝑇𝐶_ )!<sup>=</sup><sup>_𝑓_</sup> ( _𝐶𝑇_ )!<sup>=</sup> !<sup>.  In</sup> one sentence, describe a model for the PPT of species B.  What is the information content of this motif? The   simplest   model   is   one   that   assigns _𝑓𝑇_ ! = _𝑓𝐶_ ! = _𝑓_ ( _𝑇𝐶_ )! = _𝑓_ ( _𝐶𝑇_ )! = !!<sup>.      (4   nonzero</sup> probabilities)

H(model)   =   -­‐[   4   x   (   ¼   log2   (   ¼   )   )   ]   =   2   bits   (using   the   fact   that   0  log! 0 is   defined   to   be   0   (by continuity)   in   information   theory).

Therefore,   Information   =   (2   x 8)   –   2   =   14   bits.

9

! ! = = = = **(C) (3 pt.)** In species C, _𝑓𝐶𝐶 𝑓𝑇𝑇_ ! , _𝑓𝑇𝐶 𝑓𝐶𝑇_ ! at each of the seven pairs of consecutive positions (1,2), (2,3),…,(7,8), and the frequencies of all 8mers of the form Y8 are equal to 3<sup>a+b</sup> /Z where a is the number CC dinucleotides in the 8mer and b is the number of TT dinucleotides in the 8mer, and Z is the normalization constant that causes the frequencies to sum to 1.  In one sentence, describe a model for the PPT of species B. What is the information content of this motif?

Recognize   that   this   distribution   can   be   achieved   by   use   of   a   first-­‐order   Markov   model with   parameters   fC   =   fT   =   !!<sup>at   position   1,   and   conditional   probabilities   P(C|C)   =   P(T|T)   =   ¾</sup> and   P(C|T)   =   P(T|C)   =   ¼   at   all   subsequent   positions.

To   calculate   the   information   content   of   the   model,   let _𝑘_ = 7 −( _𝑎_ + _𝑏_ )   be   the   number of   CT   and   TC   dinucleotides.   The   probability   of   generating   an   8mer   sequence   with _𝑘_ CT _𝑘 𝑘_ ! ! !<sup>!!</sup> and   TC   dinucleotides   is _𝑃𝑖_<sup>_𝑘_</sup> = ! ! ! (the   factor   of   ½   is   because   there   is   a   ½ probability   of   the   first   nucleotide   –   C   or   T).   The   total   number   of   sequences   with _𝑘_ CT   and TC   dinucleotides   is   2 ! _𝑘_ (the   factor   of   2   is   for   the   two   possible   first   nucleotides   –   C   or   T). You can   check   that   the   total   probability   of   all   sequences _𝑘_ !! _𝑘_ ! _𝑘_ !! _𝑃𝑡𝑜𝑡𝑎𝑙 𝑘_ = ! _𝑘_ !! 2 ! _𝑘_ !! !! !! = 1   as   required.


10

---

[← Problem 5. de Bruijn graphs (5 points)](06-problem-5-de-bruijn-graphs-5-points.md) · [Up: contents](index.md) · [(Extra 6.874 Problem) Multiple Hypothesis Testing (4 points) →](08-extra-6-874-problem-multiple-hypothesis-testing-4-points.md)
