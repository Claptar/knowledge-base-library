---
title: Gibbs Sampling Algorithm VII
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Gibbs Sampling Algorithm VII

**Source:** `lectures/09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

7. Iterate until convergence ( sites = 0 or Θ ~ 0)


<!-- Start of picture text -->
Θ<br><!-- End of picture text -->

25

### Input Sequences with Strong Motif


<!-- Start of picture text -->
100%<br>T<br>75%<br>G<br>50%<br>C<br>25%<br>A<br>0%<br>ACGTAGCA<br>Cumulative frequency<br><!-- End of picture text -->

26


<!-- Start of picture text -->
Gibbs Sampler - Strong Motif Example<br>A C G T A G C A  Current<br>Current  Position<br>weight   in seq<br>matrix<br>Position in seq<br>Nucleotide:<br>Information content<br>Probability<br>density<br>Motif<br>strength<br>Gibbs sampler<br>animation by<br>M. Yahyanejad<br>Iteration  Position in seq<br>Sequence No.<br>Cum. Frequency (x 4)<br>Sequence<br>Information (bits)<br><!-- End of picture text -->


<!-- Start of picture text -->
Courtesy of Mehdi Yahyanejad. Used with permission.<br><!-- End of picture text -->

27

#### Input Sequences (Weak Motif)

gcggaagagggcactagcccatgtgagagggcaaggacca atctttctcttaaaaataacataattcagggccaggatgt gtcacgagctttatcctacagatgatgaatgcaaatcagc taaaagataatatcgaccctagcgtggcgggcaaggtgct gtagattcgggtaccgttcataaaagtacgggaatttcgg tatacttttaggtcgttatgttaggcgagggcaaaagtca ctctgccgattcggcgagtgatcgaagagggcaatgcctc aggatggggaaaatatgagaccaggggagggccacactgc acacgtctagggctgtgaaatctctgccgggctaacagac gtgtcgatgttgagaacgtaggcgccgaggccaacgctga atgcaccgccattagtccggttccaagagggcaactttgt ctgcgggcggcccagtgcgcaacgcacagggcaaggttta tgtgttgggcggttctgaccacatgcgagggcaacctccc gtcgcctaccctggcaattgtaaaacgacggcaatgttcg cgtattaatgataaagaggggggtaggaggtcaactcttc aatgcttataacataggagtagagtagtgggtaaactacg tctgaaccttctttatgcgaagacgcgagggcaatcggga tgcatgtctgacaacttgtccaggaggaggtcaacgactc cgtgtcatagaattccatccgccacgcggggtaatttgga tcccgtcaaagtgccaacttgtgccggggggctagcagct acagcccgggaatatagacgcgtttggagtgcaaacatac acgggaagatacgagttcgatttcaagagttcaaaacgtg cccgataggactaataaggacgaaacgagggcgatcaatg ttagtacaaacccgctcacccgaaaggagggcaaatacct agcaaggttcagatatacagccaggggagacctataactc gtccacgtgcgtatgtactaattgtggagagcaaatcatt

28

#### Gibbs Sampler - Weak Motif Example


<!-- Start of picture text -->
Current<br>Position<br>Current<br> in seq<br>weight<br>matrix<br>Position in seq<br>Nucleotide:<br>Information content<br>Probability<br>density<br>Motif<br>strength<br>Gibbs sampler<br>movie by<br>M. Yahyanejad<br>Iteration  Position in seq<br>Courtesy of Mehdi Yahyanejad. Used with permission.<br>Sequence No.<br>Cum. Frequency (x 4)<br>ce<br>Sequen<br>Information (bits)<br><!-- End of picture text -->

29

## Gibbs Sampler Summary

- A stochastic (Monte Carlo) algorithm for motif finding

- Works by ‘stumbling’ onto a few motif instances, which bias the weight matrix, which causes it to sample more motif instances, which biases the weight matrix more,

   - … until convergence

- Not guaranteed to converge to same motif every time - run several times, compare results

- Works for protein, DNA, RNA motifs

30

What does this algorithm accomplish? The likelihood function for a set of sequences _s_  with motif locations _A_ 


<!-- Start of picture text -->
background<br>freq. vector<br>weight matrix<br><br> | Θ,θ<br>P ( s  ,  A B )  =<br>∏ θ B , s k  ,1  × ... ×θ B ,  s k  , Ak −1  × Θ1,  × Θ2,  × ... × Θ8,  ×θ B ,  s k  , Ak =8 × ... ×θ B ,  L<br>k s k , A k s k , A k +1  s k , A k + 7<br>s k<br>= “actactgtatcgtactgactgattaggccatgactgcat”<br>Motif location A k<br>Likelihood function tends to increase<br><!-- End of picture text -->

31

agggcactagcccatgtgagagggcaaggaccagcggaag taattcagggccaggatgtatctttctcttaaaaataaca tatcctacagatgatgaatgcaaatcagcgtcacgagctt tggcgggcaaggtgcttaaaagataatatcgaccctagcg attcgggtaccgttcataaaagtacgggaatttcgggtag gttatgttaggcgagggcaaaagtcatatacttttaggtc aagagggcaatgcctcctctgccgattcggcgagtgatcg gatggggaaaatatgagaccaggggagggccacactgcag ctgccgggctaacagacacacgtctagggctgtgaaatct gtaggcgccgaggccaacgctgagtgtcgatgttgagaac attagtccggttccaagagggcaactttgtatgcaccgcc gcggcccagtgcgcaacgcacagggcaaggtttactgcgg ccacatgcgagggcaacctccctgtgttgggcggttctga gcaattgtaaaacgacggcaatgttcggtcgcctaccctg gataaagaggggggtaggaggtcaactcttccgtattaat aggagtagagtagtgggtaaactacgaatgcttataacat gcgagggcaatcgggatctgaaccttctttatgcgaagac tccaggaggaggtcaacgactctgcatgtctgacaacttg gtcatagaattccatccgccacgcggggtaatttggacgt gtgccaacttgtgccggggggctagcagcttcccgtcaaa cgcgtttggagtgcaaacatacacagcccgggaatataga aagatacgagttcgatttcaagagttcaaaacgtgacggg gacgaaacgagggcgatcaatgcccgataggactaataag tagtacaaacccgctcacccgaaaggagggcaaatacctt atatacagccaggggagacctataactcagcaaggttcag cgtatgtactaattgtggagagcaaatcattgtccacgtg ...

**Features that affect motif finding**

No. of sequences

Length of sequences Information content of motif Match between expected length and actual length of motif

**Motif finding issues** “shifted” motifs

biased background composition

32

## Practical Motif Finding

• MEME is a classic method Deterministic - like Gibbs, but uses expectation maximization Bailey & Elkan 1995 paper is posted. Run MEME at:

http://meme.nbcr.net/meme/

The Fraenkel lab’s WebMotifs combines

AlignACE (similar to Gibbs), MDscan, MEME, Weeder, THEME Described in Romer et al. and references therein http://fraenkel.mit.edu/webmotifs.html

33

**Mean Log-odds (bit-) Score of a Motif** _<u>p</u>_ _~~k~~_ _<u>p</u>_ _~~k~~_ bit-score: log ( ) mean bit-score: ∑ _n pk_ log ~~(~~ ) _k_ =1 2 _qk_ 2 _qk_ motif width w, n = 4<sup>w</sup>

_If_ qk =<sup>1</sup> _then_ mean bit-score = 2w - Hmotif = Imotif 4 _w_

**What is the use of knowing the information content of a motif?**

**<u>Rule of thumb*:</u>** a motif with m bits of information will occur about once every 2<sup>m</sup> bases of random sequence * Strictly true for regular expressions, approximately true for general motifs

For more on information theory, see: Elements of Information Theory by T. Cover

34

Relative Entropy* _<u>p</u>_ _~~k~~_ ) Relative entropy, D(p||q) = mean bit-score: ∑ _n pk_ log 2 ~~(~~ _k_ =1 _qk_ 1 _If_ qk = _w_<sup>_then_mean RelEnt = 2w - Hmotif = Imotif</sup> 4

RelEnt is a measure of **information** , not entropy/uncertainty. In general RelEnt is different from Hbefore - Hafter and is a better measure when background is non-random

Example: qA = qT = 3/8, qC = qG = 1/8 Suppose: pC = 1. H(q) - H(p) < 2

But RelEnt D(p||q) = log2(1/(1/8)) = 3 Which one better describes frequency of C in background seq?

- Alternate names: “Kullback-Leibler distance”, “information for discrimination”

35

MIT OpenCourseWare http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Gibbs Sampling Algorithm VI](09-gibbs-sampling-algorithm-vi.md) · [Up: contents](index.md)
