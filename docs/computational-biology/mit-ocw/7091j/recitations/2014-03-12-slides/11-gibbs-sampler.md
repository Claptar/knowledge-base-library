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

#### Transcription factor

`1. ttgccacaaaataatccgccttcgcaaattgaccTACCTCAATAGCGGTAgaaaaacgcaccactgcctgacag`

`2. gtaagtacctgaaagttacggtctgcgaacgctattccacTGCTCCTTTATAGGTAcaacagtatagtctgatgga`

`3. ccacacggcaaataaggagTAACTCTTTCCGGGTAtgggtatacttcagccaatagccgagaatactgccattccag 4. ccatacccggaaagagttactccttatttgccgtgtggttagtcgcttTACATCGGTAAGGGTAgggattttacagca 5. aaactattaagatttttatgcagatgggtattaaggaGTATTCCCCATGGGTAacatattaatggctctta 6. ttacagtctgttatgtggtggctgttaaTTATCCTAAAGGGGTAtcttaggaatttactt`

When is convergence?

Courtesy of Carl Kingsford. Used with permission.

   - Different options: go through _N_ updates (each sequence once on average) and

      - (1) No motif subsequence location changes

      - (2) PWM changes less than desired amount (e.g. 1% at each position)

- -Gibbs sampler works better when:

   - motif is present in each sequence

   - motif is strong

   - _L_ is small (less flanking non-motif sequence)

   - _W_ is (close to) correct length

- PWM may be a shifted version of true motif (missing first or last positions of motif) – once converged, you can shift PWM by 1+ positions forward or backward and see if you converge to better results (higher likelihood of generating sequences from new PWMs)

- If computationally feasible, want to run the Gibbs sampler (1) for multiple motif lengths _W_ , and

- 13 (2) multiple times to gauge robustness of results http://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/gibbs.pdf

---

[← Gibbs Sampler](10-gibbs-sampler.md) · [Up: contents](index.md) · [Review: Markov Chains →](12-review-markov-chains.md)
