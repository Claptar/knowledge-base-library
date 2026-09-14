---
title: Data preparation
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s04/A
  Cohort Location Model of Household Sorting in US Metropolitan Regions.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/section/s04/A Cohort Location
  Model of Household Sorting in US Metropolitan Regions.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data preparation

**Source:** [`section/s04/A Cohort Location Model of Household Sorting in US Metropolitan Regions.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/section/s04/A Cohort Location Model of Household Sorting in US Metropolitan Regions.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We began by collecting geographic data (i.e. census block shape files) and SF1 data (flat files) from the USA. Census’s FTP site<sup>2</sup> for each state which contains at least one county in one of the 50 largest CBSAs. From the geographic data, we isolated all geographic records at the census block level. These data include a unique identifier that links to the SF1 data, a field noting which CBSA each block is located in, if any, as well as fields indicating the latitude and the longitude for the census block centroid. Using the CBSA field within the geographic data, we removed all census blocks not located within the largest 50 CBSAs.

From the SF1 data we extracted the responses to question P22 that breaks down households into family and non-family households and by the age of the head of household. Because responses to this question are provided in 10-year cohorts (except for the 55 to 59 and 60 to 64 groups), we develop a consistent 10-year cohort categorisation for the analysis. As the family versus non-family designation does not play a role in this analysis, we combined these figures within each of the 10-year age cohorts, leaving us with eight age groups for each census block. We then merged the CBSA

8

Urban Studies

identification number and latitude and longitude value from the geographic data to the SF1 P22 data, using the unique census block identification number. Census blocks with no households were eliminated at this stage. This merged data set is hereafter referred to as the ‘Household Location Data’ or HLD – we have made this data set publicly available online.<sup>3</sup>

We applied a systematic approach to identify centre and subcentre(s) for each metropolitan region. For each of the 50 CBSAs, the exact latitude and longitude points for all centre and subcentre(s) locations were obtained via Google Maps. CBSA centres are the first city to appear in the CBSA name – e.g. Phoenix in the Phoenix-Mesa-Scottsdale CBSA. Subcentres are the subsequent locations within the CBSA names – Mesa and Scottsdale, for example. Non-municipal subcentre names (such as Kenosha County or Northern New Jersey) were removed from this analysis as deriving a single centroid point is not possible. Using the HLD, the great-circle distance from each census block centroid to its corresponding CBSA centre and subcentres, if any, was then computed using the Haversine formula. The minimum distance from each census block to a centre or subcentre(s) was recorded and added to the Household Location Data.

---

[← Method](09-method.md) · [Up: contents](index.md) · [Computation of the distance variable →](11-computation-of-the-distance-variable.md)
