---
title: Statistical (Shannon) Entropy
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Statistical (Shannon) Entropy

**Source:** `lectures/09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Motif probabilities: pk (k = A, C, G, T) Background probabilities: qk =<sup>1</sup> (k = A, C, G, T) 4 = ? 2 bits H(q) = −∑4 _qk_ log 2 _qk k_ =1 H(p) =<sup>−</sup> ∑4 _pk_ log 2 _pk_ ( > or < H(q)?) _k_ =1

Log base 2 gives entropy/information in ‘bits’

Relation to Boltzmann entropy: S = kB ln(Ω)

9

#### **Information, uncertainty, entropy**

Claude Shannon on what name to give to the “measure of uncertainty” or attenuation in phone-line signals (1949):

“My greatest concern was what to call it. I thought of calling it ‘information’, but the word was overly used, so I decided to call it ‘uncertainty’. When I discussed it with John von Neumann, he had a better idea. Von Neumann told me, ‘You should call it entropy, for two reasons. In the first place your uncertainty function has been used in statistical mechanics under that name, so it already has a name. In the second place, and more important, nobody knows what entropy really is, so in a debate you will always have the advantage.”

source: Wikipedia

10

**Information Content of a DNA Motif** Information at position j: Ij = Hbefore – Hafter Motif probabilities: pk (k = A, C, G, T) Background probabilities: qk =<sup>1</sup> (k = A, C, G, T) 4 4 _qk_ log 2 _qk_ – −∑ 2 _k_ Ij =<sup>−</sup> ∑ _k_ =1 _k_ 4 =1 _pk_ log _p_ = 2 – Hj

If positions in the motif are **independent** , then _w_ Imotif = ∑ _I j_ = 2w - Hmotif (for motif of width w bases) _j_ =1 Otherwise, this relation does not hold in general. Log base 2 gives entropy/information in ‘bits’

11

### **The Motif Finding Problem**

###### Unaligned

###### Aligned

agggcactagcccatgtgagagggcaaggaccagcggaag taattcagggccaggatgtatctttctcttaaaaataaca tatcctacagatgatgaatgcaaatcagcgtcacgagctt tggcgggcaaggtgcttaaaagataatatcgaccctagcg attcgggtaccgttcataaaagtacgggaatttcgggtag gttatgttaggcgagggcaaaagtcatatacttttaggtc aagagggcaatgcctcctctgccgattcggcgagtgatcg gatggggaaaatatgagaccaggggagggccacactgcag ctgccgggctaacagacacacgtctagggctgtgaaatct gtaggcgccgaggccaacgctgagtgtcgatgttgagaac attagtccggttccaagagggcaactttgtatgcaccgcc gcggcccagtgcgcaacgcacagggcaaggtttactgcgg ccacatgcgagggcaacctccctgtgttgggcggttctga gcaattgtaaaacgacggcaatgttcggtcgcctaccctg gataaagaggggggtaggaggtcaactcttccgtattaat aggagtagagtagtgggtaaactacgaatgcttataacat gcgagggcaatcgggatctgaaccttctttatgcgaagac tccaggaggaggtcaacgactctgcatgtctgacaacttg gtcatagaattccatccgccacgcggggtaatttggacgt gtgccaacttgtgccggggggctagcagcttcccgtcaaa cgcgtttggagtgcaaacatacacagcccgggaatataga aagatacgagttcgatttcaagagttcaaaacgtgacggg gacgaaacgagggcgatcaatgcccgataggactaataag tagtacaaacccgctcacccgaaaggagggcaaatacctt atatacagccaggggagacctataactcagcaaggttcag cgtatgtactaattgtggagagcaaatcattgtccacgtg ...

gcggaagagggcactagcccatgtgagagggcaaggacca atctttctcttaaaaataacataattcagggccaggatgt gtcacgagctttatcctacagatgatgaatgcaaatcagc taaaagataatatcgaccctagcgtggcgggcaaggtgct gtagattcgggtaccgttcataaaagtacgggaatttcgg tatacttttaggtcgttatgttaggcgagggcaaaagtca ctctgccgattcggcgagtgatcgaagagggcaatgcctc aggatggggaaaatatgagaccaggggagggccacactgc acacgtctagggctgtgaaatctctgccgggctaacagac gtgtcgatgttgagaacgtaggcgccgaggccaacgctga atgcaccgccattagtccggttccaagagggcaactttgt ctgcgggcggcccagtgcgcaacgcacagggcaaggttta tgtgttgggcggttctgaccacatgcgagggcaacctccc gtcgcctaccctggcaattgtaaaacgacggcaatgttcg cgtattaatgataaagaggggggtaggaggtcaactcttc aatgcttataacataggagtagagtagtgggtaaactacg tctgaaccttctttatgcgaagacgcgagggcaatcggga tgcatgtctgacaacttgtccaggaggaggtcaacgactc cgtgtcatagaattccatccgccacgcggggtaatttgga tcccgtcaaagtgccaacttgtgccggggggctagcagct acagcccgggaatatagacgcgtttggagtgcaaacatac acgggaagatacgagttcgatttcaagagttcaaaacgtg cccgataggactaataaggacgaaacgagggcgatcaatg ttagtacaaacccgctcacccgaaaggagggcaaatacct agcaaggttcagatatacagccaggggagacctataactc gtccacgtgcgtatgtactaattgtggagagcaaatcatt

...

###### ...can be posed as an alignment problem

12

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Approaches to Motif Finding →](03-approaches-to-motif-finding.md)
