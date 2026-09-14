---
title: Gibbs Sampler
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Gibbs Sampler

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Transcription factor

`1. ttgccacaaaataatccgccttcgcaaattgaccTACCTCAATAGCGGTAgaaaaacgcaccactgcctgacag`

`2. gtaagtacctgaaagttacggtctgcgaacgctattccacTGCTCCTTTATAGGTAcaacagtatagtctgatgga`

`3. ccacacggcaaataaggagTAACTCTTTCCGGGTAtgggtatacttcagccaatagccgagaatactgccattccag 4. ccatacccggaaagagttactccttatttgccgtgtggttagtcgcttTACATCGGTAAGGGTAgggattttacagca 5. aaactattaagatttttatgcagatgggtattaaggaGTATTCCCCATGGGTAacatattaatggctctta`

`6. ttacagtctgttatgtggtggctgttaaTTATCCTAAAGGGGTAtcttaggaatttactt`

Courtesy of Carl Kingsford. Used with permission.

Start with _N_ sequences, searching for motif of length _W_ ( _W_ < length each of sequence) -Randomly choose a starting position in each sequence (a1, a2, …, aN) – the starting guess as to where motif is in each sequence

- Randomly choose one sequence to leave-out (will optimize motif position in this

- sequence)

- Make a PWM from _N_ -1 subsequences at the starting positions in all sequences

- except the one left-out - For the left-out sequence (has length _L_ ), assign a probability

10

http://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/gibbs.pdf Hundreds of papers, many formulations (Tompa05)

---

[← Gibbs Sampler](07-gibbs-sampler.md) · [Up: contents](index.md) · [Gibbs Sampler →](09-gibbs-sampler.md)
