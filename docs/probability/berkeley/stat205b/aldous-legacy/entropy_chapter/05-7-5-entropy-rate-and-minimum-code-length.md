---
title: 7.5 Entropy rate and minimum code length
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.5 Entropy rate and minimum code length

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here we will outline in words the statement and proof of the fundamental result in the whole field. The case of an IID source (recall section 2.2) is Shannon’s source coding theorem from 1948. The “approximation” is as _n ! 1_ .

A string of length _n_ from a source with entropy rate _Ent_ can be coded as a binary string of length _⇡ n ⇥Ent_ but not of shorter length.

More briefly, the optimal coding rate is _Ent_ bits per letter.

**Why not shorter?** Think of the entire message ( _X_ 1 _, . . . , Xn_ ) as a single random object. The AEP says the entropy of its distribution is approximately _n ⇥Ent_ . Suppose we can code it as a binary string ( _Y_ 1 _, . . . , Ym_ ) of some length _m_ . By Fact 1, the entropy of the distribution of ( _Y_ 1 _, . . . , Ym_ ) also _⇡ n ⇥Ent_ , whereas by Fact 2 the entropy is at most _m_ . Thus _m_ is approximately _≥ n ⇥Ent_ as asserted.

_7.6. MORSE CODE AND ASCII_

111

**How to code this short.** We give an easy to describe but completely impractical scheme. Saying that a typical plaintext string has chance about 1 in a million implies there must be around 1 million such strings (if more then the total probability would be _>_ 1; if less then with some non-negligible chance a string has likelihood not near 1 in a million). So the AEP implies that a typical length- _n_ string is one of the set of about 2<sup>_n⇥Ent_</sup> strings which have likelihood about 2<sup>_−n⇥Ent_</sup> (and this is the origin of the phrase _asymptotic equipartition property_ ). So in principle we could devise a codebook which first lists all these strings as integers 1 _,_ 2 _, . . . ,_ 2<sup>_n⇥Ent_</sup> , and then the compressed message is just the binary expansion of this integer, whose length is log2 2<sup>_n⇥Ent_</sup> = _n ⇥Ent_ . So a typical message can be compressed to length about _n⇥Ent_ ; atypical messages (which could be coded in some non-efficient way) don’t a↵ect the limit assertion.

The second argument is really exploiting a loophole in the statement. Viewing the procedure as transmission, we imagine that transmitter and receiver are using some codebook, but we placed no restriction on the size of the codebook, and the code described above uses a ridiculously large and impractical codebook,

The classical way to get more practical codes is by fixing some small _k_ and coding blocks of length _k_ , Thus requires a codebook of size _A_<sup>_k_</sup> , where _A_ is the underlying alphabet size. However, making an optimal codebook of this type requires knowing the frequencies of blocks that will be produced by the source. Rather than explain further, we shall jump (after a brief historical digression) to more modern codes that don’t assume such knowledge..

---

[← 7.4 The asymptotic equipartition property](04-7-4-the-asymptotic-equipartition-property.md) · [Up: contents](index.md) · [7.6 Morse code and ASCII →](06-7-6-morse-code-and-ascii.md)
