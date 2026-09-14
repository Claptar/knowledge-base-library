---
title: Inference with Bayes Nets
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Inference with Bayes Nets

**Source:** `lectures/14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If a student is not admitted, is it more likely they had bad GREs or bad grades?


<!-- Start of picture text -->
S<br>If a student is not admitted, is it more<br>Smart<br>likely they had bad GREs or bad grades?<br>G<br>R  Compute P(R=F|A=F)  and P(G=F|A=T)<br>Grade<br>GREs<br>s<br>A<br>Admit<br>Tedious but straightforward to compute<br><!-- End of picture text -->

P(R=F|A=F) = P(R=F,A=F) / P(A=F) = [Σ Σ  P(S)P(G=F)P(R)P(A=F)]/P(A=F)<sup>G=F,TR=F,T</sup>

P(A=F)  = Σ Σ Σ P(S)P(G|S)P(R|S)P(A=T|G,R) (as before)

<u>P(G=F|A=T)</u> = .92 = 1.6 P(R=F|A=F)      .56

99

---

[← Inference with Bayes Nets](54-inference-with-bayes-nets.md) · [Up: contents](index.md) · [End of worked example →](56-end-of-worked-example.md)
