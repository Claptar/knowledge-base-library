---
title: Independence of a collection of events
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Independence of a collection of events

**Source:** `lectures/03-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Intuitive definition: Information on some of the events tells us nothing about probabilities related to the remaining events

E.g.:

   - P( _A_ 1 _∩_ ( _Ac_ 2 _∪ A_ 3) _| A_ 5 _∩Ac_ 6 ) = P( _A_ 1 _∩_ ( _Ac_ 2 _∪ A_ 3))

   - Mathematical definition: Events _A_ 1 _, A_ 2 _, . . . , An_ are called independent if:

      - P( _Ai∩Aj∩· · ·∩Aq_ ) = P( _Ai_ )P( _Aj_ ) _· · ·_ P( _Aq_ ) for any distinct indices _i, j, . . . , q_ ,

      - (chosen from _{_ 1 _, . . . , n}_ )

- Once we know it is coin _A_ , are tosses independent?

- If we do not know which coin it is, are tosses independent?

- Compare: P(toss 11 = _H_ ) P(toss 11 = _H |_ first 10 tosses are heads)

---

[← Conditioning may affect independence](04-conditioning-may-affect-independence.md) · [Up: contents](index.md) · [Independence vs. pairwise independence →](06-independence-vs-pairwise-independence.md)
