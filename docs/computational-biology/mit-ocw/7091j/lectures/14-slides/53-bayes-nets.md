---
title: Bayes Nets
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/14-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bayes Nets

**Source:** `lectures/14-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
Bayes Nets<br>S<br>Smart<br>Recall:<br>P(X,Y) = P(X|Y)P(Y)<br>G<br>R<br>Grade<br>GREs<br>s<br>A<br>Admit<br><!-- End of picture text -->

P(S,G,R,D) = P(S)P(G|S)P(R|G,S)P(A|S,G,R)

= P(S)P(G|S)P(R|S)P(A|G,R)    (why?) (because of conditional independence assumption)

96


<!-- Start of picture text -->
Prediction with Bayes Nets<br>        G<br>S  P(F) P(T) S  S<br>Smart<br>F    0.9    0.1  P(F) P(T)<br>T    0.8    0.2  0.5  0.5  R<br>S  P(F) P(T)<br>G<br>R  F    0.8    0.2<br>Grade<br>s  GREs  T    0.2    0.8  GREs are better<br>correlated with<br>       A<br>Rough grading:  intelligence than<br>G  R  P(F) P(T)<br>being smart  the grades<br>A<br>F  F   0.9    0.1<br>doesn’t help very  Admit<br>F  T   0.8    0.2<br>much!<br>T  F   0.5    0.5<br>T  T   0.2    0.8<br>P(A=T|S=T) =  ΣΣ  P(G|S=T)P(R|S=T)P(A=T|G,R)<br>G=F,T   R=F,T<br>= (0.8)(0.2)(0.1) + (0.8)(0.8)(0.2) + (0.2)(0.2)(0.5) + (0.2)(0.8)(0.8) =.29<br>F F F T T F T T<br><!-- End of picture text -->

97

---

[← Chain Rule of Probability for](52-chain-rule-of-probability-for.md) · [Up: contents](index.md) · [Inference with Bayes Nets →](54-inference-with-bayes-nets.md)
