---
title: The Sequential Randomization Assumption
source: https://vanderlaan-lab.org/teach-files/survMSM2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/survMSM2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The Sequential Randomization Assumption

**Source:** [`survMSM2004.pdf`](https://vanderlaan-lab.org/teach-files/survMSM2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The SRA implies that:

_g_ ( _A_ ( _t_ ) _| A_<sup>¯</sup> ( _t −_ 1) _, X_ ) = _g_ ( _A_ ( _t_ ) _| A_<sup>¯</sup> ( _t −_ 1) _, L_<sup>¯</sup> ( _t_ )) _._

( _⇐⇒ g_ ( _A | X_ ) = _g_ ( _A | W_ ) for point-treatment data, i.e. RA)

If the SRA is violated, it might still be possible to identify _β_ in certain specific situations (instrumental variables).

However if one does not want to make assumptions only valid in certain specific scenarios likely not to hold, the SRA is required for identification of a causal effect.

Under the SRA we thus have:


Romain Neugebauer - 16

---

[← Overview of the issues to be addressed](01-overview-of-the-issues-to-be-addressed.md) · [Up: contents](index.md) · [Intuition behind the SRA →](03-intuition-behind-the-sra.md)
