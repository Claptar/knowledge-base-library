---
title: Computation of the distance variable
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/clm.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/clm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Computation of the distance variable

**Source:** [`ps/clm.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/clm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As we intend to compare household location by distance over a variety of metropolitan areas – many vastly different in size – we began by standardising the distance measurements. First, we removed all census blocks with a minimum centre/subcentre(s) distance of greater than 60 miles as these likely represent highly rural areas not within the economically functional range of the metropolitan region. The 60-mile cutoff was based on a natural break in the data. Next, we standardised all distances to be a fraction

of the greatest minimum centre/subcentre(s) distance of the remaining census blocks. For instance, if the farthest census block in a given CBSA is 25 miles from its nearest centre/subcentre(s), and block X is 5 miles from its nearest centre/subcentre(s) then block X has a standardised distance of 0.2 (5/25). Doing so converts all distances to a value between 0 (at the centre/subcentre) and 1 (at the metropolitan fringe). Standardised distances were rounded to two digits. Figure 2 shows a map produced from the AtlantaSandy Springs-Marietta CBSA, an example of the data we compiled for each of the 50 CBSAs.

---

[← Data preparation](10-data-preparation.md) · [Up: contents](index.md) · [Computation of the location quotient →](12-computation-of-the-location-quotient.md)
