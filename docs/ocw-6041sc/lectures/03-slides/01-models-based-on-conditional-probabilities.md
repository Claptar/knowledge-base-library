---
title: Models based on conditional probabilities
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Models based on conditional probabilities

**Source:** `lectures/03-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Readings: Section 1.5

- Review

- Independence of two events

- Independence of a collection of events

Review

P( _A ∩ B_ <u>)</u> P( _A | B_ ) = _,_ assuming P( _B_ ) _>_ 0 P( _B_ )

- Multiplication rule:

   - P( _A ∩ B_ ) = P( _B_ ) _·_ P( _A | B_ ) = P( _A_ ) _·_ P( _B | A_ )

- 3 tosses of a biased coin: P( _H_ ) = _p_ , P( _T_ ) = 1 _− p_


<!-- Start of picture text -->
p HHH<br>p<br>1 - p HHT<br>p HTH<br>p 1 - p<br>1 - p HTT<br>p THH<br>1 - p p<br>1 - p THT<br>p TTH<br>1 - p<br>1 - p TTT<br><!-- End of picture text -->

- Total probability theorem:

   - P( _B_ ) = P( _A_ )P( _B | A_ ) + P( _Ac_ )P( _B | Ac_ )

- Bayes rule:

---

[Up: contents](index.md) · [Independence of two events →](02-independence-of-two-events.md)
