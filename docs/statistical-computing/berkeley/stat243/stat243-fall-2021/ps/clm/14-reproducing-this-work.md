---
title: Reproducing this work
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/clm.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/ps/clm.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`ps/clm.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/clm.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Reproducing this work

This research has been conducted in a full reproducible manner. 'Reproducibility' in this context means that the empirical results presented in this work can be fully and exactly recreated by other parties using the data and workflow documentation which we have made publicly available. Reproducibility is necessary for the verification of empirical work and, as a result, has been defined as a 'cornerstone' (Mccullough, 2009) or a 'fundamental tenet' (Crick et al., 2014) of good scientific practice. Additionally, research conducted in a reproducible manner has been shown to contain fewer errors (Camfield and Palmer-Jones, 2013), completed more efficiently (Donoho, 2010) and garner more citations (King, 1995).

All code used to create the data and analysis in this paper is available at https://github.com/andykrause/hhLocation. The documentation on this site will provide complete instructions for downloading and executing the necessary code to reproduce our analysis. The raw data (census geographic data and SF1 data) for this analysis are many gigabytes in size. The code will download, extract and clean these data. Users wishing to skip the time-consuming data download and cleaning process may download the cleaned set of data from Harvard's DataVerse repository – available at https://dataverse.harvard.edu/dataverse/repHHLoc. Users are encouraged to use our cleaned data for related research, provided the data are cited.

The model we propose here is also reproducible in other contexts. However, when thinking about external validity of the CLM, one should refer the two basic assumptions that this model was developed upon. Our first assumption that housing career increases over a household's life span should hold globally. Yet, our second assumption about how housing services are being offered across metropolitan regions is US-based and in order for this model to work in other context, this assumption needs to be modified accordingly. Once this assumption is modified, the model in Figure 1 can be reproduced in intersection of the two assumptions and we expect its geometric form to be different for different regions in the world. Future work can reproduce this model in other parts of the world, add more detailed age intervals, or incorporate other proxies for housing career change over time.

## Acknowledgements
We thank the three anonymous reviewers for their careful reading and constructive comments.

## Funding
This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Notes
1. To simplify the model, we consider housing provision to refer to structural utility-generating assets such as home size, number of bathrooms, lot size, etc. Location specific amenities – which vary in utility depending on household preference – are ignored.
2. http://www.census.gov/prod/cen2010/doc/sf1.pdf.
3. https://dataverse.harvard.edu/dataverse/repHHLoc.
4. Jittering is a function that adds an amount of random noise to the data in order to break ties, and is often used to avoid overplotting.

---

[← Conclusion and discussion](13-conclusion-and-discussion.md) · [Up: contents](index.md) · [References →](15-references.md)
