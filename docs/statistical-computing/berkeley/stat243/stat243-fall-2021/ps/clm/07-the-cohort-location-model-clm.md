---
title: The Cohort Location Model (CLM)
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/clm.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/ps/clm.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`ps/clm.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/ps/clm.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# The Cohort Location Model (CLM)

In the CLM, we argue that changes in households' housing careers (i.e. housing consumption, residential mobility and location choices) across the life span happen in a continuum and therefore we hypothesise that such changes could create spatial sorting effects within metropolitan areas. Our approach approximates household housing careers over a household's life span, which we conceptualise as a continuous variable that can be broken into as many segments as empirically testable. With this approach, modelling housing careers becomes more flexible, as any specific pattern can be approximated over multiple intervals based on data availability – i.e. the life span can be broken into years, decades, stages (as in lifecycle studies), or phases (as in the phasic model). Similar to the phasic model, we proxy a household's life span with age of the householder.

Also, similar to the phasic model, in CLM we assume that owing to the predominance of low-density residential development ('suburban') in most US metropolitan regions, the provision of housing services$^1$ generally increases with distance from city centre(s). By using the term 'city centre(s)' we imply the application to both monocentric and multi-centric cities – we conventionally substitute city centre(s) with CBD in this article. The increase in the provision of housing services may also be reflected in property values. Yet, there are distinctions in the type of housing services distributed between the suburbs and the metropolitan fringe that make each location favourable for specific groups of households.

The general assumption in the CLM is that because consumption of housing services increase over a household's housing career (which we approximate here with the age of the householder), the youngest cohort of households is more likely to live closest to the city centre(s) where fewer housing services are offered, and vice versa. We hypothesise that there is a broad spatial order to this pattern, as illustrated in Figure 1.

![Figure 1. A linear approximation for the probability (location quotient) of households' residential location across metropolitan regions.](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2021/c918dcc56a197cc539e270f1f7d076010b175c52/ps/placeholder)

*Figure 1. A linear approximation for the probability (location quotient) of households' residential location across metropolitan regions.*

The X axis in Figure 1 represents a two-dimensional profile of the metropolitan region, from the city centre (conventionally called the CBD) or a significant subcentre, to a hypothetical border between the city and the low density suburban areas (conventionally called the city–suburb fringe), and to the metropolitan fringe (i.e. where the metropolitant region ends). The Y axis represents the relative location quotient for each of the various cohorts. The location quotient represents the relative likelihood of a cohort living in a certain distance from the CBD. More specifically, it measures the proportion of households of a certain cohort at a given distance to the proportion of households of that cohort in the entire region. Changes in the location quotient for each cohort across metropolitan space are presented by a line, which is more compact on the left and more dispersed on the left – reflecting the relative compactness of central city locations compared with the metropolitan fringe. According to the model, as the age of the householder increases, the probability of the household living close to the city centre(s) decreases. The overall trend is as follows:

* At the city centre(s), the sorting pattern is more distinguishable for younger households (who are the prominent age groups at central city locations) and older households (who, based on the assumptions of this model, are the least expected age groups), than for the middle-aged householders – i.e. at the city centre(s), it should be easier to distinguish among the ages of, for example, 24 and 25, or 78 and 79, than 42 and 43.
* If modelled linearly, the trend lines (i.e. the linear approximations of the probability functions) begin to converge somewhere near the city–suburb fringe. The CLM assumes that middle-aged households are more likely to live in proximity to where suburbs emerge outside of central city locations. The middle-aged households in this geographic domain are followed by older and then younger households.
* Between the suburbs and the metropolitan fringe, the likelihood patterns exhibit gentler transitions. At the metropolitan fringe, the residential likelihood pattern is exactly opposite to the pattern at the city centre(s): older households are the most likely to live and difficult to distinguish, middle-aged households are less likely to reside but easy to distinguish, and younger households are least likely to live and also difficult to distinguish.

We argue that the model presented here is empirically testable with different time intervals – time intervals can be defined flexibly based on data availability and granularity of the data. Using 2010 US Census data, we evaluated this model for eight aggregate trend lines illustrated in Figure 1, representing 10-year age groups or cohorts. This aggregation is due to data availability.

## Method

To test the assumption discussed above we analysed household location data from the 50 largest (as of 2013) Core Based Statistical Areas (CBSAs) in the USA. A list of the 50 largest CBSAs and their 2010 population is provided in Appendix 1. Together, the selected CBSAs had a population of 166,033,092 in 2010 – comprising 54% of the total population in the USA. We derived data on household age and location (at the census block level) from the 2010 Census SF1 data set. In addition to the generalisability resulting from the population coverage, the 50 largest metropolitan regions were selected in previous studies that involved data and computations at similar spatial scales (for example, see Denton and Massey, 1991; Gober et al., 2013; Hunt and Balachandran, 2015; Lang, 2002; Lichter et al., 2015; Markusen and Schrock, 2006; Sivak, 2008).

---

[← Relaxing the phasic model](06-relaxing-the-phasic-model.md) · [Up: contents](index.md) · [Data preparation →](08-data-preparation.md)
