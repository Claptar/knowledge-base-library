---
title: Data preparation
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/clm.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/ps/clm.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`ps/clm.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/clm.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Data preparation

We began by collecting geographic data (i.e. census block shape files) and SF1 data (flat files) from the USA. Census's FTP site$^2$ for each state which contains at least one county in one of the 50 largest CBSAs. From the geographic data, we isolated all geographic records at the census block level. These data include a unique identifier that links to the SF1 data, a field noting which CBSA each block is located in, if any, as well as fields indicating the latitude and the longitude for the census block centroid. Using the CBSA field within the geographic data, we removed all census blocks not located within the largest 50 CBSAs.

From the SF1 data we extracted the responses to question P22 that breaks down households into family and non-family households and by the age of the head of household. Because responses to this question are provided in 10-year cohorts (except for the 55 to 59 and 60 to 64 groups), we develop a consistent 10-year cohort categorisation for the analysis. As the family versus non-family designation does not play a role in this analysis, we combined these figures within each of the 10-year age cohorts, leaving us with eight age groups for each census block. We then merged the CBSA identification number and latitude and longitude value from the geographic data to the SF1 P22 data, using the unique census block identification number. Census blocks with no households were eliminated at this stage. This merged data set is hereafter referred to as the 'Household Location Data' or HLD – we have made this data set publicly available online.$^3$

We applied a systematic approach to identify centre and subcentre(s) for each metropolitan region. For each of the 50 CBSAs, the exact latitude and longitude points for all centre and subcentre(s) locations were obtained via Google Maps. CBSA centres are the first city to appear in the CBSA name – e.g. Phoenix in the Phoenix-Mesa-Scottsdale CBSA. Subcentres are the subsequent locations within the CBSA names – Mesa and Scottsdale, for example. Non-municipal subcentre names (such as Kenosha County or Northern New Jersey) were removed from this analysis as deriving a single centroid point is not possible. Using the HLD, the great-circle distance from each census block centroid to its corresponding CBSA centre and subcentres, if any, was then computed using the Haversine formula. The minimum distance from each census block to a centre or subcentre(s) was recorded and added to the Household Location Data.

## Computation of the distance variable

As we intend to compare household location by distance over a variety of metropolitan areas – many vastly different in size – we began by standardising the distance measurements. First, we removed all census blocks with a minimum centre/subcentre(s) distance of greater than 60 miles as these likely represent highly rural areas not within the economically functional range of the metropolitan region. The 60-mile cutoff was based on a natural break in the data. Next, we standardised all distances to be a fraction of the greatest minimum centre/subcentre(s) distance of the remaining census blocks. For instance, if the farthest census block in a given CBSA is 25 miles from its nearest centre/subcentre(s), and block X is 5 miles from its nearest centre/subcentre(s) then block X has a standardised distance of 0.2 (5/25). Doing so converts all distances to a value between 0 (at the centre/subcentre) and 1 (at the metropolitan fringe). Standardised distances were rounded to two digits. Figure 2 shows a map produced from the Atlanta-Sandy Springs-Marietta CBSA, an example of the data we compiled for each of the 50 CBSAs.

---

[← The Cohort Location Model (CLM)](07-the-cohort-location-model-clm.md) · [Up: contents](index.md) · [Computation of the location quotient →](09-computation-of-the-location-quotient.md)
