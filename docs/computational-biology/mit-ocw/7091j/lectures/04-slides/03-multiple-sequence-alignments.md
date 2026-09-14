---
title: Multiple Sequence Alignments
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/04-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Multiple Sequence Alignments

**Source:** `lectures/04-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Sequences are aligned so as to bring the greatest number of single characters into register, and maximize a score that rewards matches and penalizes mismatches, gaps

10

### **2 sequence alignment**


<!-- Start of picture text -->
Comp. complexity? O(mn)  or   O(n 2 ) if both have length n<br>i =0       1           2           3             4              5<br>Gap        V          D           S             C             Y<br>j =<br>0<br>0 4 -8 -16 -24 -32 -40<br>-3 -8<br>1 -8<br>-8 -4 -12 -20 -28<br>4<br>3<br>2 -16 -6 7 -1 -9 -17<br>2<br>3<br>-24 -14 -6 9 1 -7<br>4<br>-32 -22 -14 1 3<br>0<br>5 -40 -30 -22 -7 13 3<br>6<br>-48 -38 -30 -15 5<br>23<br><!-- End of picture text -->

11

**_For 3 sequences…._ Length**

**`ARDFSHGLLENKLLGCDSMRWE`**<sup>**m**</sup> `.::.  .:::. .:::: :::.` **`GRDYKMALLEQWILGCD-MRWD`**<sup>**n**</sup> `.::.  ::.:  .. :. .:::` **`SRDW--ALIEDCMV-CNFFRWD` p** **_An O(mnp) problem_ Consider sequences each 300 amino acids 2 sequences – (300)**<sup>**2**</sup> **3 sequences – (300)**<sup>**3**</sup> **but for** **_k_ sequences – (300)**<sup>**_k_**</sup> **=> Need a more efficient algorithm (e.g., CLUSTALW - see Z&B Ch.6)**

12

## Comparative Genomics

- Markov models

- Jukes-Cantor, Kimura models

- Types of Selection: neutral, negative, positive

- Comparative genomics to understand gene regulation

- a dozen examples

Readings:

- 12 papers posted under Comparative Genomics (optional)

- Sabeti review (first 3 pages recommended)

13

Limit Theorem for Markov Chains _Sn_ = base at generation _n Pij_<sup>=</sup><sup>_P_(</sup> _Sn_ +1<sup>=</sup><sup>_j_|</sup> _Sn_<sup>=</sup><sup>_i_)</sup> li What happens after a long time?       i.e. what is m _q_<sup></sup> _P_<sup>_n_</sup> =? _r_<sup></sup><sup>_n_→∞</sup>

If                  for all _i,j_ (and                      for all _i_ ) _Pij_<sup>>0</sup> ∑ _Pij_<sup>=1</sup> _j_

> then there is a unique vector        such that _r_<sup></sup>

_r_<sup></sup> = _r_<sup></sup> _P_<sup>and                                  (for any probability vector      )</sup> lim _q_<sup></sup> _P_<sup>_n_</sup> = _r_<sup></sup> _q_<sup></sup><sup>_n_→∞</sup>

_r_<sup></sup> is called the “stationary” or “limiting” distribution of _P_

See Ch. 4, Taylor & Karlin, An Introduction to Stochastic Modeling, 1984 for details

14

### Stationary Distribution Examples

2-letter alphabet: R = purine, Y = pyrimidine

###### <u>Stationary distributions for:</u>


15

###### **Jukes-Cantor Model**

Assume each nucleotide equally likely α T to change into any other nt, α with rate of change=α. α Overall rate of substitution = 3α α …so if G at t=0, at t=1, PG(1)=1-3α C α and PG(2)=(1-3α)PG(1) +α [1− PG(1) ] Solving recursion gives PG(t)=1/4 + (3/4)e<sup>-4αt</sup> Can show that this gives K = -3/4 ln[1-(4/3)d]


<!-- Start of picture text -->
α<br>G T<br>α<br>α<br>α<br>α<br>A C<br>α<br><!-- End of picture text -->

K = true number of substitutions that have occurred, d = fraction of nt that differ by a simple count (d ≤ 3/4) **_Captures general behavior…_**

16

###### More realistic models of DNA evolution

4-letter alphabet: A, C, G, T

Kimura model<sup>(1)</sup>

q = transition rate p = transversion rate ⎛1 − 2 _p_ − _q p q p_ ⎞ (q = ~2p) ⎜ ⎟ _p_ 1 − 2 _p_ − _q p q P_ = ⎜ ⎟ ⎜ _q p_ 1 − 2 _p_ − _q p_ ⎟ ⎜ ⎟ ⎝ _p q p_ 1 − 2 _p_ − _q_ ⎠ 0 < _p_ < _q_ < 1

Dinucleotide => Dinucleotide models<sup>(2)</sup> AA => AA, AC, AG, AT, CA, CC, CG, CT, GA, GC, GG, … AC => AA, AC, AG, AT, CA, …

Strand-specific models<sup>(3)</sup>

- (1)  Kimura J Mol Evol 1980

- (2)  Zhang & Gerstein Nucl Acids Res 2003

- (3)  Green et al. Nature Genet 2003

17

Detecting Positive/Negative Selection: Calculation of Ka/Ks ratio (aka dN/dS ratio)

```
           M   Q   R   P   F   G   K   A   R   G   V   S
human     ATG CAA CGG CCT TTG GGA AAG GCC AGA GGA GTC TCC
           M   Q   R   P   V   G   K   A   R   A   L   S
baboon    ATG CAG CGG CCT GTG GGG AAG GCC AGA GCA CTC TCC
```

```
           P   T   A   P   G   V   T   G   V   T
human     CCT ACA GCC CCA GGG GTA ACC GGC GTT ACA
           P   A   A   A   G   V   P   G   V   P
baboon    CCT GCA GCT GCA GGG GTA CCC GGC GTT CCA
```

```
dN = Ka = nonsynonymous substitutions / nonsynonymous sites
dS = Ks = synonymous substitutions / synonymous sites
```

18

###### Detecting Negative and Positive Selection in Coding Regions

Ka/Ks or dN/dS ratio:

Ka or dN = normalized rate of **nonsynonymous** changes per position Ks or dS = normalized rate of **synonymous** changes per position Corrected version:  dS = 3/4 ln(1 - 4/3 pS), etc. (see Z&B pp. 240-241) Common applications:

- Identify genes or regions with Ka/Ks significantly less than one - These regions are likely to be under selection to conserve amino acid sequence

What kinds of genes or regions would you expect to have Ka/Ks ~ 1?

Identify genes or regions with Ka/Ks significantly greater than one

- These regions are likely to be under selection to change amino acid sequence

More sophisticated tests for positive selection: McDonald-Kreitman, etc.

19

###### **A dozen comparative genomics papers**

To illustrate some of the types of things we can learn about gene regulation by comparing genomes, often using fairly simple methods

To provide examples of successful computational biology research projects

- To gain experience in reading the literature in regulatory genomics

20

###### **Types of comparative genomic analyses**

**Identification of regulatory elements of unknown function** Bejerano et al. 2002 **...characterization of their functions** Pennacchio et al 2006,  Visel et al 2008, Lareau et al 2007 **...exploration of their origins** Bejerano et al 2006

**Inference of the targeting rules for a class of trans-acting factors** Lewis et al 2003, 2005

**Identification of regulatory targets of a class of trans-acting factors** Kheradpour et al 2008, Friedman et al 2009

**Identification of new intra-genic interacting regulatory elements** Graveley 2005

**Identification of a new class of trans-acting factors** Jansen et al 2002

**Identification of trans-genomic interacting regulatory elements** Bolotin et al 2005

21

###### Bejerano et al. 2004 “Ultraconserved elements”

**Defined “ultraconserved elements” (UCEs) as unusually long segments that are 100% identical between human, mouse and rat using wholegenome alignments of the 3 species and studied their properties**

###### **From the SOM:**

Each column in the orthologous multiple alignment is considered to be an independent observation of a Bernoulli random variable that is 1 (“heads”) if the bases are completely conserved between the three species (a “3-way identity”) and 0 (“tails”) otherwise. ...The largest percent identity among ancestral repeat sites we obtained for any 1 Mb window with enough ancestral repeat sites to get a good estimate, i.e. at least 1000 sites, was actually 0.68. The distribution of the number of runs of at least 200 heads in a series of 2.9 billion tosses of a biased coin with probability p = 0.7 of heads can be approximated quite well using a Poisson distribution with mean (1p)·p<sup>200</sup> , and the probability of one or more such runs is very close to the mean of the Poisson distribution in this case, which is at most 10<sup>-22</sup>

Bejerano et al. Science 2004

22

###### **Features of UCEs**

**481 UCEs (≥ 200 bp):**

~100 overlap exons of known protein-coding genes

~100 located in introns of known genes

- ~300 intergenic

93 **type I genes** overlap with exonic ultraconserved elements 225 genes that are near the non-exonic elements are called **type II genes**


© American Association for the Advancement of Science. All rights reserved. This content is excluded

from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Bejerano et al. Science 2004 Source: Bejerano, Gill, Michael Pheasant, et al. "Ultraconserved Elements in the Human Genome." _Science_ 304, no. 5675 (2004): 1321-5.

23

###### **What do intergenic (ultra)conserved elements do?**

well established transgenic mouse enhancer assay that links the human conserved fragment to a minimal mouse heat shock promoter fused to a lacZ reporter gene... determined tissue-specific reporter gene expression at embryonic day 11.5 (e11.5), as this developmental stage allows for whole-mount staining and whole-embryo visualization. Moreover, at this time-point many of the major tissues and organs have been specified. We also expected this stage to be particularly informative because ‘extreme’ conserved non-coding elements tend to be enriched and clustered near genes expressed during embryonic development.

**We tested 167 of these extremely conserved sequences in a transgenic mouse enhancer assay. Here we report that 45% of these sequences functioned reproducibly as tissue-specific enhancers of gene expression at embryonic day 11.5.**

Courtesy of Macmillan Publishers Limited. Used with permission. Source: Pennacchio, Len A., Nadav Ahituv, et al. "In Vivo Enhancer Analysis of Human Conserved Non-coding Sequences." _Nature_ 444, no. 7118 (2006): 499-502.

Pennacchio et al. Nature 2006

24

###### Do **ultraconserved** differ from **highly conserved** enhancers?


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Pennacchio, Len A., Nadav Ahituv, et al. "In Vivo Enhancer Analysis of Human Visel et al. Nature Genet 2008 Conserved Non-coding Sequences." _Nature_ 444, no. 7118 (2006): 499-502.

25

###### **Where do UCEs come from?**


<!-- Start of picture text -->
Coelacanth (~400 Mya)<br><!-- End of picture text -->

Courtesy of Stuart Gold. Used with permission.


<!-- Start of picture text -->
Coelacanth (~1974)<br><!-- End of picture text -->

© Alberto Fernandez Fernandez. Some rights reserved. License: CC-BY-SA. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Bejerano et al. Nature 2006


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Bejerano, Gill, Craig B. Lowe, et al. "A Distal Enhancer and An Ultraconserved Exon are Derived from a Novel Retroposon." _Nature_ 441, no. 7089 (2006): 87-90.

26

###### **Interpretation**

After discovering mobile DNA elements, Barbara McClintock suggested that they were fundamentally involved in gene regulation, an idea further developed by Britten and Davidson, who speculated on the benefit of obtaining similar control regions for a ‘battery’ of co-regulated genes through **exaptation** .

At least 50% of our genome originates from characterized transposon-derived DNA ... it seems possible that, because these elements optimize their interaction with the host machinery under strong, virus-like evolutionary pressures, they are a particularly fecund source of evolutionary innovations, including new gene regulatory elements, and these are at times **exapted** by the host to improve its own fitness. If so, it is possible that many more of the one million conserved vertebrate genomic elements originated from ancient retroposon families.

Bejerano et al. Nature 2006

27

###### **What about exonic UCEs?**


Courtesy of Macmillan Publishers Limited. Used with permission. Source: Lareau, Liana F., Maki Inada, et al. "Unproductive Splicing of SR Genes Associated with Highly Conserved and Ultraconserved DNA Elements." _Nature_ 446, no. 7138 (2007): 926-29.

**SRp20** - a splicing factor involved in constitutive and alternative splicing - contains one of the longest UCEs, overlapping a “poison cassette exon”

- mRNAs containing “premature” termination codons (PTCs) are commonly degraded by the nonsense-mediated mRNA decay pathway

- many splicing factor genes express PTC-containing mRNA isoforms - and in some cases the SF is known to promote splicing of PTC isoforms from its own locus - may ensure reduced variability in levels between cells


Lareau et al. Nature 2007

28

## miR-1 **microRNAs**

defining features:

- RNA 2<sup>o</sup> structure of precursor


- Dicer processing

- Expressed product is ~20-23 nt

- Sequence conservation

Called microRNAs or miRNAs Named: _mir-X_ (gene), miR-X (RNA) miR-84

29

###### **microRNA biogenesis/function**


<!-- Start of picture text -->
microRNA<br>1 o  transcript<br>Drosha<br>pre-miRNA<br>Dicer<br>mature miRNA<br>target mRNA<br>RISC<br>RISC<br>translational repression<br>and/or mRNA degradation<br><!-- End of picture text -->

30

### MicroRNAs and apoptosis in _Drosophila_


<!-- Start of picture text -->
...<br><!-- End of picture text -->

Courtesy of Elsevier. Used with permission.

Brennecke _Curr. Biol._ 2003

31

### Phenotype of the _bantam_ knockout fly pupa

_bantam_ knockout pupa


<!-- Start of picture text -->
...<br><!-- End of picture text -->

Courtesy of Elsevier. Used with permission.


Pupa expressing _bantam_ microRNA

Brennecke et al. _Cell_ 2003

Courtesy of Elsevier. Used with permission. Source: Brennecke, Julius, David R. Hipfner, et al. " _bantam_ Encodes a Developmentally Regulated MicroRNA that Controls Cell Proliferation and Regulates the Proapoptotic Gene _hid_ in _Drosophila_ ." _Elsevier journal_ 113, no. 1 (2003): 25-36.

32

###### Original TargetScan Algorithm


<!-- Start of picture text -->
Example: miR-26a / SMAD-1<br>Require Watson-Crick<br>pairing to miRNA bases 2-8<br>1st Site<br>“seed match”<br>2nd Site “seed”<br>“seed”<br>SMAD-1 3' UTR<br>human<br>mouse<br>rat<br><!-- End of picture text -->

33

###### Perturbing the Model: “Sliding Seed” Experiment


<!-- Start of picture text -->
 -1..-7<br>UGAGGUAGUAGGUUGUAUAGUU<br>2..8<br>1..7<br>UGAGGUAGUAGGUUGUAUAGUU<br>UGAGGUAGUAGGUUGUAUAGUU<br><!-- End of picture text -->


<!-- Start of picture text -->
‘Signal’ - targets of real miRNAs<br>‘Background’ - targets of shuffled miRNAs<br>Position of seed heptamer<br>Position of seed heptamer<br>Bases 2-8 at the 5’ end of the miRNA give the best signal<br><!-- End of picture text -->

Courtesy of Elsevier. Used with permission. Source: Lewis, Benjamin P., I-hung Shih, et al. "Prediction of Mammalian MicroRNA Targets." _Cell_ 115, no. 7 (2003): 787-98. Lewis et al. _Cell_ 2003

34

### Conservation of _let-7_ Foldbacks


<!-- Start of picture text -->
mm-let-7c-1  -UGUGUGCAUCCGGGUUGAGGUAGUAGGUUGUAUGGUU--UAGAGUUACACCCUGG----------GAGUUAACUGUACAACCUUCUAGCUUUCCUUGGAGCACACU------<br>hs-let-7c    ------GCAUCCGGGUUGAGGUAGUAGGUUGUAUGGUU--UAGAGUUACACCCUGG----------GAGUUAACUGUACAACCUUCUAGCUUUCCUUGGAGC-----------<br>hs-let-7a-2  ------------AGGUUGAGGUAGUAGGUUGUAUAGUU--UAGAAUUACAUCAAGG----------GAGAUAACUGUACAGCCUCCUAGCUUUCCU-----------------<br>mm-let-7a-2  CUGCAUGUUCCCAGGUUGAGGUAGUAGGUUGUAUAGUU--UAGAGUUACAUCAAGG----------GAGAUAACUGUACAGCCUCCUAGCUUUCCUUGGGACUUGCAC-----<br>hs-let-7f-1  ----------UCAGAGUGAGGUAGUAGAUUGUAUAGUU-GUGGGGUAGUGAUUUUACCCUGUUCAGGAGAUAACUAUACAAUCUAUUGCCUUCCCUGA---------------<br>mm-let-7f-1  ---------AUCAGAGUGAGGUAGUAGAUUGUAUAGUU-GUGGGGUAGUGAUUUUACCCUGUUUAGGAGAUAACUAUACAAUCUAUUGCCUUCCCUGAG--------------<br>mm-let-7b    ----------GCAGGGUGAGGUAGUAGGUUGUGUGGUU-UCAGGGCAGUGAUGUUGCCCC--UCCGAAGAUAACUAUACAACCUACUGCCUUCCCUGA---------------<br>hs-let-7b    -----------CGGGGUGAGGUAGUAGGUUGUGUGGUU-UCAGGGCAGUGAUGUUGCCCC--UCGGAAGAUAACUAUACAACCUACUGCCUUCCCUG----------------<br>hs-let-7i    -----------CUGGCUGAGGUAGUAGUUUGUGCUGUUGGUCGGGUUGUGACAUUGCCCGCUGU-GGAGAUAACUGCGCAAGCUACUGCCUUGCUA-----------------<br>mm-let-7i    -----------CUGGCUGAGGUAGUAGUUUGUGCUGUUGGUCGGGUUGUGACAUUGCCCGCUGU-GGAGAUAACUGCGCAAGCUACUGCCUUGCUAG----------------<br>mm-let-7g    ----------CCAGGCUGAGGUAGUAGUUUGUACAGUUUGAGGGUCUAUGAUACCACCCGGUACAGGAGAUAACUGUACAGGCCACUGCCUUGCCAGG---------------<br>hs-let-7g    ------------AGGCUGAGGUAGUAGUUUGUACAGUUUGAGGGUCUAUGAUACCACCCGGUACAGGAGAUAACUGUACAGGCCACUGCCUUGCCA-----------------<br>hs-let-7a-3  -------------GGGUGAGGUAGUAGGUUGUAUAGUU--UGGGGCUCUG-CCCUGCUAU------GGGAUAACUAUACAAUCUACUGUCUUUCCU-----------------<br>mm-let-7c-2  ---ACGGCCUUUGGGGUGAGGUAGUAGGUUGUAUGGUU--UUGGGCUCUG-CCCCGCUCU------GCGGUAACUAUACAAUCUACUGUCUUUCCUGAAGUGGCCGC------<br>mm-let-7d    -AAUGGGUUCCUAGGAAGAGGUAGUAGGUUGCAUAGUU-UUAGGGCAGAGAUUUUGCCCAC--AAGGAGUUAACUAUACGACCUGCUGCCUUUCUUAGGGCCUUAUU------<br>hs-let-7d    ---------CCUAGGAAGAGGUAGUAGGUUGCAUAGUU-UUAGGGCAGGGAUUUUGCCCAC--AAGGAGGUAACUAUACGACCUGCUGCCUUUCUUAGG--------------<br>hs-let-7a-1  -----------UGGGAUGAGGUAGUAGGUUGUAUAGUU-UUAGGGUCACACCCACCACUG-----GGAGAUAACUAUACAAUCUACUGUCUUUCCUA----------------<br>mm-let-7a-1  ----UUCACUGUGGGAUGAGGUAGUAGGUUGUAUAGUU-UUAGGGUCACACCCACCACUG-----GGAGAUAACUAUACAAUCUACUGUCUUUCCUAAGGUGAU---------<br>hs-let-7f-2  ---------UGUGGGAUGAGGUAGUAGAUUGUAUAGUU-UUAGGGUCAUACCC-CAUCUU-----GGAGAUAACUAUACAGUCUACUGUCUUUCCCACG--------------<br>mm-let-7f-2  ---------UGUGGGAUGAGGUAGUAGAUUGUAUAGUU-UUAGGGUCAUACCC-CAUCUU-----GGAGAUAACUAUACAGUCUACUGUCUUUCCCACG--------------<br>mm-let-7e    --CGCGCCCCCCGGGCUGAGGUAGGAGGUUGUAUAGUU---GAGGAAGACACCCGA---------GGAGAUCACUAUACGGCCUCCUAGCUUUCCCCAGGCUGCGCC------<br>hs-let-7e    ---------CCCGGGCUGAGGUAGGAGGUUGUAUAGUU---GAGGAGGACACCCAA---------GGAGAUCACUAUACGGCCUCCUAGCUUUCCCCAGG-------------<br>cb-let-7     ---ACUG-GGGUACGGUGAGGUAGUAGGUUGUAUAGUU--UAGAAUAUUACUCUCG------------GUGAACUAUGCAAGUUUCUACCUCACCGAAUACCAGG--------<br>ce-let-7     UACACUGUGGAUCCGGUGAGGUAGUAGGUUGUAUAGUU--UGGAAUAUUACCACCG------------GUGAACUAUGCAAUUUUCUACCUUACCGGAGACAGAACUCUUCGA<br>dm-let-7     ------UCUGGCAAAUUGAGGUAGUAGGUUGUAUAGU----AGUA-AUUACACAUC------------AU--ACUAUACAAUGUGCUAGCUUUCUUUGCUUGA----------<br>100 100<br>75<br>50<br>50<br>25<br> 0<br>0<br>% 7mers identical<br><!-- End of picture text -->

35


<!-- Start of picture text -->
Dscam  - an extreme case of alternative splicing<br><!-- End of picture text -->


<!-- Start of picture text -->
Exon 4 Exon 6 Exon 9 Exon 17<br>Gene<br>mRN<br>A<br>Protei<br>n<br>Ig Repeats Fibronectin Domains<br>© source unknown. All rights reserved. This content is excluded from our Creative<br>Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.<br>Dscam can potentially express > 38,000 isoforms,<br>which control neuronal wiring<br>How is splicing regulated?<br>How is mutually exclusive<br>inclusion of exons achieved? Courtesy of Elsevier. Used with permission.<br>Source: Wojtowicz, Woj M., John J. Flanagan, et al. "Alternative Splicing of  Drosophila<br>Dscam Generates Axon Guidance Receptors that Exhibit Isoform-Specific Homophilic<br>Schmücker  et al .   Cell  2000<br>Binding."  Cell  118, no. 5 (2004): 619-33.<br><!-- End of picture text -->

36

### Motif downstream of DSCAM exon 5


Courtesy of Elsevier. Used with permission. Source: Graveley, Brenton R. "Mutually Exclusive Splicing of the Insect _Dscam_ Pre-mRNA Directed by Competing Intronic RNA Secondary Structures." _Cell_ 123, no. 1 (2005): 65-73.

Graveley _Cell 2005_

37

### Motif downstream of DSCAM exon 5


Courtesy of Elsevier. Used with permission. Source: Graveley, Brenton R. "Mutually Exclusive Splicing of the Insect _Dscam_ Pre-mRNA Directed by Competing Intronic RNA Secondary Structures." _Cell_ 123, no. 1 (2005): 65-73.

Graveley _Cell 2005_

38

### Mutually Exclusive Splicing of the Exon 6 Cluster Docking Site

##### Selector Sequences

Courtesy of Elsevier. Used with permission. Source: Graveley, Brenton R. "Mutually Exclusive Splicing of the Insect _Dscam_ Pre-mRNA Directed by Competing Intronic RNA Secondary Structures." _Cell_ 123, no. 1 (2005): 65-73.

Graveley _Cell 2005_

39

###### Defining a Branch Length Score to assess conservation


© sources unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Kheradpour et al Genome Res 2008

40


Using a similar branch length conservation measure to assess and classify mammalian miRNA target sites


Freely available online through the Genome Research Open Access option. License: CC-BY-NC. Source: Friedman, Robin C., Kyle Kai-How Farh, et al. "Most Mammalian MRNAs are Conserved Targets of MicroRNAs." _Genome Research_ 19, no. 1 (2009): 92-105.

Friedman et al Genome Res 2009

41

Identifying a family of genes (cas) associated with a bacterial repeat structure (CRISPR)


- © Society for General Microbiology. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/ .

Source: Bolotin, Alexander, Benoit Quinquis, et al. "Clustered Regularly Interspaced Short Palindrome Repeats(CRISPRs) have Spacers of Extrachromosomal Origin." _Microbiology_ 151, no. 8 (2005): 2551-61.


© Blackwell Science Ltd. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

Source: Jansen, Ruud, Jan Embden, et al. "Identification of Genes that are Associated with DNA Repeats in Prokaryotes." _Molecular Microbiology_ 43, no. 6 (2002): 1565-75.

Jansen et al Mol Microbiol 2002

42

###### CRISPR spacers match phage genomes


Number of spacers is correlated with resistance to phage

© Society for General Microbiology. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/. Source: Bolotin, Alexander, Benoit Quinquis, et al. "Clustered Regularly Interspaced Short Palindrome Repeats(CRISPRs) have Spacers of Extrachromosomal Origin." _Microbiology_ 151, no. 8 (2005): 2551-61.

Bolotin et al Microbiol 2005

43

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Issues with PAM Series?](02-issues-with-pam-series.md) · [Up: contents](index.md)
