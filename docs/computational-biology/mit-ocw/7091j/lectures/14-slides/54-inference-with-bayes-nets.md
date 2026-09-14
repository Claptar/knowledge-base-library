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

P(S=T|A=T) = P(S=T,A=T)/P(A=T) A=T) = P(S=T,A=T)/P(A=T) =T) = P(S=T,A=T)/P(A=T) A=T)/P(A=T) =T)/P(A=T) A=T) =T) Or, using Bayes Rule: = P(S=T)P(A=T|S=T)/P(A=T) A=T|S=T)/P(A=T) =T|S=T)/P(A=T) A=T) =T)

**S** P(S=T|A=T) = P(S=T,A=T)/P(A=T) A=T) = P(S=T,A=T)/P(A=T) =T) = P(S=T,A=T)/P(A=T) A=T)/P(A=T) =T)/P(A=T) A=T) =T) **Smart** Or, using Bayes Rule: = P(S=T)P(A=T|S=T)/P(A=T) A=T|S=T)/P(A=T) =T|S=T)/P(A=T) A=T) =T) **G R Grade GREs s** P(S=T) = 0.5 **A** P(A=T|S=T) calculated on previous slide =.29 **Admit** P(A=T|S=F) =.14

P(A=T) = Σ Σ Σ P(S)P(G|S)P(R|S)P(A=T|G,R)

> <sup>S=F,T   G=F,TR=F,T</sup>

= P(S=T)P(A=T|S=T) + P(S=F)P(A=T|S=F)  = 0.21

P(S=T) = 0.5, P(S=F) = 0.5, P(A=T|S=F) calculated analogously to P(A=T|S=T)

98

---

[← Bayes Nets](53-bayes-nets.md) · [Up: contents](index.md) · [Inference with Bayes Nets →](55-inference-with-bayes-nets.md)
