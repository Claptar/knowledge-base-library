---
title: 7.6 Morse code and ASCII
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.6 Morse code and ASCII

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Invented around 1840, Morse code codes each letter and numeral as a sequence of dots and dashes: for instance T is _−_ and Z is _−−••_ . Logically this is like coding into a _three_ -letter alphabet, because one also needs to indicate (by a pause) the spaces between letters. As is intuitively natural, common letters (like T) are coded as short sequences and uncommon letters (like Z) are coded as longer sequences. Given frequencies of letters, there is a theoretical optimal way (Hu↵man coding) to implement such a _variable length_ code, and this has the same intuitive feature. But it’s important to note that Hu↵man coding is optimal only amongst codes applied to individual letters, and depends on known fixed frequencies for letters.

Developed in the 1960s, ASCII codes letters, numerals and other symbols

_CHAPTER 7. CODING AND ENTROPY_

#### 112

into 128 7-bit strings: for instance T is 101 0100 and Z is 101 1010. At first sight it may seem surprising that ASCII, and its current extension unicode, don’t use variable length codes as did Morse code. But the modern idea is that with any kind of original data one can first digitize into binary in some simple way, and then compress later if needed.

---

[← 7.5 Entropy rate and minimum code length](05-7-5-entropy-rate-and-minimum-code-length.md) · [Up: contents](index.md) · [7.7 Lempel-Ziv algorithms →](07-7-7-lempel-ziv-algorithms.md)
