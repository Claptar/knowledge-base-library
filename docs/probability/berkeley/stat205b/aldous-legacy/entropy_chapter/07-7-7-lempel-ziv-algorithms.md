---
title: 7.7 Lempel-Ziv algorithms
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.7 Lempel-Ziv algorithms

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the 1970s it was realized that with computing power you don’t need a fixed codebook at all – there are schemes that are (asymptotically) optimal for any source. Such schemes are known as Lempel-Ziv style<sup>5</sup> algorithms, though the specific version described below, chosen as easy to describe, is not the textbook form.

Suppose we want to transmit the message

#### 010110111010 _|_ 011001000 _. . . . . ._

and that we have transmitted the part up to _|_ , and this has been decoded by the receiver. We will next code some initial segment of the subsequent text 011001000 _. . . . . ._ . To do this, first find the longest initial segment that has appeared in the already-transmitted text. In this example it is 0110 which appeared in the position shown.

#### 010110111010 _|_ <u>011001000</u> _. . . . . ._

Writing _n_ for the position of the current (first not transmitted) bit, let _n − k_ be the position of the start of the closest previous appearance of this segment, and _`_ for the length of the segment. In the example, ( _k, `_ ) = (10 _,_ 4). We transmit the pair ( _k, `_ ); the receiver knows where to look to find the desired segment and append it to the previously decoded text. Now we just repeat the procedure:

#### 0101101110100110 _|_ <u>01000</u> _. . . . . ._

the next maximal segment is 0100 and we transmit this as (7 _,_ 4).

How efficient is this scheme? We argue informally as follows. When we’re a long way into the text – position _n_ say – we will be transmitting segments of some typical length _`_ = _`_ ( _n_ ) which grows with _n_ (in fact it grows as order log _n_ but that isn’t needed for this argument). By the AEP the likelihood

> 5The current Wikipedia article is not so helpful for the general reader.

113

#### _7.8. CHECKING FOR YOURSELF_

of a particular typical such segment is about 2<sup>_−`⇥Ent_</sup> and so the distance _k_ we need to look back to find the same segment is order 2<sup>+</sup><sup>_`⇥Ent_</sup> . So to transmit the pair ( _k, `_ ) we need log2 _`_ + log2 _k ⇡ ` ⇥Ent_ bits. Because this is transmitting _`_ letters of the text, we are transmitting at rate _Ent_ bits per letter, which is the optimal rate.

---

[← 7.6 Morse code and ASCII](06-7-6-morse-code-and-ascii.md) · [Up: contents](index.md) · [7.8 Checking for yourself →](08-7-8-checking-for-yourself.md)
