---
title: 7.8 Checking for yourself
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.8 Checking for yourself

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

On my Mac I can use the Unix `compress` command, which implements one version of the Lempel-Ziv algorithm. A simple theoretical prediction is that if you take a long piece of text, split it into two halves of equal uncompressed length, and compress each half separately, then the two compressed halves will be approximately the same length. It takes only a few minutes to check an example. I used a text of _Don Quixote_ , in English translation, downloaded from Project Gutenberg.

Table 7.2: Bytes in Don Quixote

||uncompressed|compressed|
|---|---|---|
|first half|1109963|444456|
|second half|1109901|451336|
|whole|2219864|895223|


The prediction works pretty well. Further predictions can be made based on the notion that the algorithm incurs some “start-up cost” before the coding becomes efficient, implying

- The compressed size of a complete text will be shorter than the sums of compressed sizes of its parts. (We see this in the example above, though the di↵erence is very small).

- For a text broken into pieces of di↵erent sizes, the compression ratio for the pieces will be roughly constant but also will tend to decrease slightly as size increases.

To illustrate the latter, I used the L<sup>A</sup> TEX text of the Grinsted-Snell textbook _Introduction to Probability_ .

_CHAPTER 7. CODING AND ENTROPY_

114

Table 7.3: Bytes in Grinsted-Snell

|chapter|uncompressed|compressed|ratio|
|---|---|---|---|
|1|101082|46029|.465|
|2|73966|32130|.434|
|3|139490|61571|.441|
|4|123784|53962|.436|
|5|100155|43076|.430|
|6|134256|57577|.429|
|7|39975|18021|.451|
|8|39955|18759|.470|
|9|90019|39853|.443|
|10|79560|35058|.441|
|11|166626|69181|.415|
|12|56463|25299|.448|

---

[← 7.7 Lempel-Ziv algorithms](07-7-7-lempel-ziv-algorithms.md) · [Up: contents](index.md) · [7.9 . . . but English text is not random →](09-7-9-but-english-text-is-not-random.md)
