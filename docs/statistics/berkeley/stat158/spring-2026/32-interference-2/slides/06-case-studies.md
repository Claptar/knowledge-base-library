---
title: Case Studies
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/32-interference-2/slides.html
source_file: sources/berkeley-stat158/spring-2026/32-interference-2/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Case Studies

**Source:** [`32-interference-2/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/32-interference-2/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

##

How would one person’s treatment influence another’s outcome in each one? What kind of bias could this introduce? Could you redesign the experiment to avoid the interference?

*3000 students at UC Berkeley agree to participate in a study, and 1000 of them are chosen at random to receive a new kind of flu shot. All students are monitored for flu virus for the following eight weeks.*

Even untreated students will gain immunity if many others are treated, so the control group may have lower flu rates than they would in a world where no one was treated. This could lead to an underestimate of the vaccine’s effectiveness. To avoid this, we could randomize at the dormitory level instead of the individual level, so that all students in a dorm either receive the vaccine or do not. This would help to isolate the direct effect of the vaccine without interference from untreated individuals gaining immunity through herd effects.

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

**Saturation Model**: Modeling spillover effects as a function of the fraction of treated individuals in a cluster (e.g., dormitory) rather than individual treatment status.

<span class="math display">\\$$ Y\_{ij}(D\_{ij}, S\_j) \\$$</span>

Where <span class="math inline">\$D\_{ij}\$</span> is the treatment status of individual <span class="math inline">\$i\$</span> in cluster <span class="math inline">\$j\$</span>, and <span class="math inline">\$S\_j\$</span> is the saturation level (fraction treated) in cluster <span class="math inline">\$j\$</span>.

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

##

How would one person’s treatment influence another’s outcome in each one? What kind of bias could this introduce? Could you redesign the experiment to avoid the interference?

*17 pairs of similar geographic locations in Lowell, MA with high crime incidences were identified (“hot-spots”) and one hot-spot in each pair was randomly assigned to receive extra visits from police and extra follow-up by police authorities. Control hot-spots did not receive attention and police captains didn’t know their locations. Rates of emergency calls from each hot-spot were recorded before and after the study.*

The treatment in one hot-spot could reduce crime in nearby hot-spots due to increased police presence and deterrence, leading to spillover effects. This could bias the estimated effect of the treatment if not accounted for. To redesign the experiment, we could increase the distance between treated and control hot-spots to minimize spillover.

Alternatively, the extra policing in treated hot-spots could displace crime to nearby areas, which would also bias the results. To address this, we could include a buffer zone around each hot-spot and exclude data from that zone in the analysis, or we could use a spatial model to account for potential spillover effects.

<style type="text/css">
        span.MJX_Assistive_MathML {
          position:absolute!important;
          clip: rect(1px, 1px, 1px, 1px);
          padding: 1px 0 0 0!important;
          border: 0!important;
          height: 1px!important;
          width: 1px!important;
          overflow: hidden!important;
          display:block!important;
      }</style>

##

How would one person’s treatment influence another’s outcome in each one? What kind of bias could this introduce? Could you redesign the experiment to avoid the interference?

*4.9 million eBay users were assigned either to a control condition, or to a treatment under which they received an email notification six hours before the end of any auction they bid in. The outcome is the amount of money spent by the user on eBay.*

##

How would one person’s treatment influence another’s outcome in each one? What kind of bias could this introduce? Could you redesign the experiment to avoid the interference?

*A retail store is introducing a new “Salesperson of the Month” award, which will be given at random to one of the employees. The record the amount of sales of all employees.*

## Sales Award Revisited {data-id="quarto-animate-title"}

<span class="math display">\\$$ Y\_{i}(D\_M, D\_P, D\_L) \\$$</span>

| agent | Y(1,0,0) | Y(0,1,0) | Y(0,0,1) |
|:------|---------:|---------:|---------:|
| Mary  |      100 |       50 |       70 |
| Peter |       50 |       50 |       50 |
| Linus |       90 |       50 |       90 |

## Sales Award Revisited {data-id="quarto-animate-title"}

<span class="math display">\\$$ Y\_i(D\_M, D\_P, D\_L) \\$$</span>

| agent | Y(1,0,0) | Y(0,1,0) | Y(0,0,1) | Y(0,0,0) |
|:------|---------:|---------:|---------:|---------:|
| Mary  |      100 |       50 |       70 |       70 |
| Peter |       50 |       50 |       50 |       50 |
| Linus |       90 |       50 |       90 |       90 |

## Sales Award Revisited {data-id="quarto-animate-title"}

<span class="math display">\\$$ Y\_i(D\_M, D\_P, D\_L) \\$$</span>

| store | agent | Y(1,0,0) | Y(0,1,0) | Y(0,0,1) | Y(0,0,0) |
|------:|:------|---------:|---------:|---------:|---------:|
|     1 | Mary  |      100 |       50 |       70 |       70 |
|     1 | Peter |       50 |       50 |       50 |       50 |
|     1 | Linus |       90 |       50 |       90 |       90 |
|     2 | Priya |       80 |       60 |       75 |       75 |
|     2 | Leo   |       60 |       60 |       55 |       55 |
|     2 | Ethan |       70 |       60 |       85 |       85 |

---

[← students in untreated households](05-students-in-untreated-households.md) · [Up: contents](index.md)
