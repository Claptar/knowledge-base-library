---
title: Announcements
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-05-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Announcements

**Source:** `recitations/2014-03-05-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Project specific aims due this ~~Friday (2/07)~~ – examples will be posted this evening

- Pset #2 due in 1 week (02/13) – For problem 2B, Matlab and Mathematica use a (1-p) parameterization in contrast to lecture slides (p):

• R or N = 1/k (same as in lecture slides) <u>1</u> _λ λ_ _<u>k</u>_ • P = _λ λ_ + <u>1</u> for Matlab/Mathematica vs. _λ λ_ +<sup><u>1</u></sup> in _k k_ lecture slides

2


<!-- Start of picture text -->
protein<br>ChIP-seq<br>B  protein<br>B<br>protein A<br>protein<br>protein A B  protein A<br>DNA<br><!-- End of picture text -->


<!-- Start of picture text -->
tightly but reversibly binds proteins to<br>(1) crosslink proteins and DNA<br>nearby DNA<br>protein<br>protein A B  protein A<br>DNA<br>(2) fragment DNA<br>(by sonication, etc.)<br>protein<br>protein A B  protein A<br>DNA<br><!-- End of picture text -->

3


<!-- Start of picture text -->
ChIP-seq<br>protein<br>protein A B  protein A<br>DNA<br>(3) immunoprecipitate use antibodies against protein of<br>interest (here protein A)<br>protein A protein A<br><!-- End of picture text -->

- (4) reverse crosslinks, purify DNA


- (5) sequence purified DNA, align reads to genome


###### reference genome in black reads in maroon


4


<!-- Start of picture text -->
ChIP-seq<br>protein<br>endogenous  Tagged<br>B<br>protein A protein A<br>DNA<br>(3) immunoprecipitate use antibodies against an epitope<br>tag fused to protein of interest<br>Tagged<br>protein A<br><!-- End of picture text -->

- -If a high-quality antibody is not available for your protein of interest, an alternative is to introduce a construct of the protein with an epitope tag into cells and use antibody to epitope

   - Epitope is a short (5-10) amino acid sequence with antibody available (e.g. HA, His)

   - Some caveats to keep in mind:

      - Expression of your construct may not be at WT levels

      - Epitope tag could alter function and/or localization of the protein, which could lead to non-native binding locations

5

---

[Up: contents](index.md) · [Peak-calling applications →](02-peak-calling-applications.md)
